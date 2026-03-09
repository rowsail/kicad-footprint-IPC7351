#!/usr/bin/env python3

"""
Add a pin 1 triangle marker to existing .kicad_mod footprint files.

Parses the s-expression format, finds pad 1, determines the best approach
direction from the other pads, and injects a filled equilateral triangle
on F.SilkS just outside pad 1.

Usage:
    python tidykicadfp.py <pattern> [options]

    # Process a single file (auto-detect approach):
    python tidykicadfp.py MyPart.kicad_mod

    # Process files matching a wildcard pattern:
    python tidykicadfp.py 'Resistor_*.kicad_mod'

    # Recursively process all .kicad_mod under a directory:
    python tidykicadfp.py /path/to/footprints/ -r

    # Recursively process matching files:
    python tidykicadfp.py '*.kicad_mod' -r

    # Force approach direction:
    python tidykicadfp.py MyPart.kicad_mod --approach left

    # Dry-run (show what would change):
    python tidykicadfp.py /path/to/footprints/ -r --dry-run
"""

import argparse
import concurrent.futures
import glob
import math
import os
import re
import sys


def _custom_pad_extent(collapsed_text):
    """Return (width, height) of the bounding box of a custom pad's primitives.

    Coordinates in the primitives block are relative to the pad center.
    The returned size is the full extent (max - min) including stroke width,
    so the caller can use w/2 and h/2 as radii from the pad centre.
    Returns (None, None) if no primitive points could be parsed.
    """
    # Extract the (primitives ...) block
    prim_m = re.search(r'\(primitives\s+(.*)\)', collapsed_text)
    if not prim_m:
        return None, None

    prim_text = prim_m.group(1)

    # Collect all (xy X Y) points
    pts = re.findall(r'\(xy\s+([-\d.]+)\s+([-\d.]+)\)', prim_text)
    if not pts:
        return None, None

    xs = [float(x) for x, _ in pts]
    ys = [float(y) for _, y in pts]

    # Find the stroke width of the primitives (applies as half-width outward)
    wm = re.search(r'\(width\s+([-\d.]+)\)', prim_text)
    stroke = float(wm.group(1)) if wm else 0

    w = max(xs) - min(xs) + stroke
    h = max(ys) - min(ys) + stroke
    return w, h


def parse_pad(text, line_idx=None):
    """
    Parse a (pad ...) s-expression (possibly multi-line) and return a dict with:
      number, type, shape, at (x, y), size (w, h)
    Returns None if the text is not a pad or cannot be parsed.

    For custom pads the (size) field is usually meaningless; the real copper
    extent is computed from the primitives bounding box.
    """
    # Collapse whitespace so multi-line pads can be matched
    collapsed = ' '.join(text.split())
    m = re.match(
        r'\s*\(pad\s+'
        r'("(?:[^"\\]|\\.)*"|\S+)\s+'   # pad number (may be quoted)
        r'(\S+)\s+'                       # type: smd, thru_hole, np_thru_hole, connect
        r'(\S+)',                          # shape: rect, circle, oval, roundrect, custom
        collapsed)
    if not m:
        return None
    pad_num = m.group(1).strip('"')
    pad_type = m.group(2)
    pad_shape = m.group(3)

    am = re.search(r'\(at\s+([-\d.]+)\s+([-\d.]+)', collapsed)
    if not am:
        return None
    pad_x = float(am.group(1))
    pad_y = float(am.group(2))

    sm = re.search(r'\(size\s+([-\d.]+)\s+([-\d.]+)\)', collapsed)
    if not sm:
        return None
    pad_w = float(sm.group(1))
    pad_h = float(sm.group(2))

    # For custom pads, derive effective size from the primitives bounding box
    if pad_shape == 'custom':
        cw, ch = _custom_pad_extent(collapsed)
        if cw is not None:
            pad_w = cw
            pad_h = ch

    return {
        'number': pad_num,
        'type': pad_type,
        'shape': pad_shape,
        'x': pad_x,
        'y': pad_y,
        'w': pad_w,
        'h': pad_h,
        'line_idx': line_idx,
    }


def find_pads(lines):
    """Return list of parsed pad dicts from the file lines.
    Handles both single-line and multi-line pad definitions."""
    pads = []
    i = 0
    while i < len(lines):
        if '(pad ' in lines[i]:
            start = i
            # Accumulate lines until parens balance for this pad block
            buf = lines[i]
            depth = buf.count('(') - buf.count(')')
            while depth > 0 and i + 1 < len(lines):
                i += 1
                buf += lines[i]
                depth += lines[i].count('(') - lines[i].count(')')
            p = parse_pad(buf, line_idx=start)
            if p is not None:
                pads.append(p)
        i += 1
    return pads


def already_has_pin1_marker(lines):
    """Return True if there is already a filled polygon on F.SilkS (our marker)."""
    for line in lines:
        if '(fp_poly' in line and 'F.SilkS' in line and 'fill solid' in line:
            return True
    return False


def determine_approach(pad1, all_pads):
    """
    Determine the best approach direction for the triangle.

    Rules:
      1. The triangle must be outside the footprint, pointing at pad 1.
      2. The tip points into the shortest edge of the pad.
      3. The base is parallel to the shortest edge.

    For a pad of size w × h:
      - pw <= ph → top/bottom edges (spanning pw) are shortest
                   → approach from top or bottom.
      - ph < pw  → left/right edges (spanning ph) are shortest
                   → approach from left or right.

    The specific direction on the chosen axis is the one facing away from
    the centroid of the other pads (i.e. outside the footprint).
    """
    others = [p for p in all_pads
              if p['number'] != pad1['number'] and p['number'] != '']

    if not others:
        return 'top'

    cx = sum(p['x'] for p in others) / len(others)
    cy = sum(p['y'] for p in others) / len(others)

    pw, ph = pad1['w'], pad1['h']

    if pw <= ph:
        # Shortest edges are top and bottom (each pw wide)
        # Place triangle on the side that faces away from centroid
        return 'top' if pad1['y'] <= cy else 'bottom'
    else:
        # Shortest edges are left and right (each ph tall)
        return 'left' if pad1['x'] <= cx else 'right'


def get_courtyard_extent(lines):
    """Return (width, height) of the front courtyard bounding box, or None.

    Scans fp_line elements on F.CrtYd and computes the bounding box from
    their start/end coordinates.
    """
    xs, ys = [], []
    for line in lines:
        if 'F.CrtYd' not in line:
            continue
        for m in re.finditer(r'\((?:start|end)\s+([-\d.]+)\s+([-\d.]+)\)', line):
            xs.append(float(m.group(1)))
            ys.append(float(m.group(2)))
    if not xs:
        return None
    return (max(xs) - min(xs), max(ys) - min(ys))


def _snap_outward(val, grid):
    """Round val away from zero to the nearest grid step."""
    if val >= 0:
        return math.ceil(val / grid) * grid
    else:
        return math.floor(val / grid) * grid


def _collect_graphic_elements(lines):
    """Yield collapsed text for each top-level graphic element (fp_line, etc.).

    Handles both single-line (KiCad 5/6) and multi-line (KiCad 7/8) formats
    by accumulating lines until parentheses balance.
    """
    graphic_prefixes = ('(fp_line', '(fp_rect', '(fp_circle', '(fp_arc', '(fp_poly')
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        if any(stripped.startswith(p) for p in graphic_prefixes):
            depth = lines[i].count('(') - lines[i].count(')')
            if depth <= 0:
                # Single-line element
                yield ' '.join(lines[i].split())
            else:
                # Multi-line: accumulate until balanced
                buf = [lines[i]]
                j = i + 1
                while j < len(lines) and depth > 0:
                    depth += lines[j].count('(') - lines[j].count(')')
                    buf.append(lines[j])
                    j += 1
                yield ' '.join(''.join(buf).split())
                i = j
                continue
        i += 1


def _compute_footprint_bbox(lines, pads):
    """Return (xmin, ymin, xmax, ymax) bounding box of all pads and graphics.

    Includes pad extents, fp_line/fp_rect/fp_circle/fp_arc on F.SilkS and
    F.Fab (but excludes our own fp_poly marker, text, and courtyard lines).
    Handles both single-line and multi-line element formats.
    """
    xs, ys = [], []

    # Pad extents
    for p in pads:
        xs.extend([p['x'] - p['w'] / 2, p['x'] + p['w'] / 2])
        ys.extend([p['y'] - p['h'] / 2, p['y'] + p['h'] / 2])

    for elem in _collect_graphic_elements(lines):
        # Only consider front silk and fab layers
        if 'F.SilkS' not in elem and 'F.Fab' not in elem:
            continue
        # Skip text elements (reference, value, user text)
        if 'fp_text' in elem:
            continue
        # Skip our own filled polygon markers
        if 'fp_poly' in elem and 'fill solid' in elem:
            continue

        # fp_line / fp_rect: start and end points
        for m in re.finditer(r'\((?:start|end)\s+([-\d.]+)\s+([-\d.]+)\)', elem):
            xs.append(float(m.group(1)))
            ys.append(float(m.group(2)))

        # fp_circle: center ± radius
        cm = re.search(r'\(center\s+([-\d.]+)\s+([-\d.]+)\)', elem)
        em = re.search(r'\(end\s+([-\d.]+)\s+([-\d.]+)\)', elem)
        if cm and em and 'fp_circle' in elem:
            cx, cy = float(cm.group(1)), float(cm.group(2))
            ex, ey = float(em.group(1)), float(em.group(2))
            r = math.hypot(ex - cx, ey - cy)
            xs.extend([cx - r, cx + r])
            ys.extend([cy - r, cy + r])

        # fp_arc: start (center) and end (point on arc)
        if 'fp_arc' in elem:
            sm = re.search(r'\(start\s+([-\d.]+)\s+([-\d.]+)\)', elem)
            em2 = re.search(r'\(end\s+([-\d.]+)\s+([-\d.]+)\)', elem)
            if sm and em2:
                cx, cy = float(sm.group(1)), float(sm.group(2))
                ex, ey = float(em2.group(1)), float(em2.group(2))
                r = math.hypot(ex - cx, ey - cy)
                xs.extend([cx - r, cx + r])
                ys.extend([cy - r, cy + r])

    if not xs:
        return None
    return (min(xs), min(ys), max(xs), max(ys))


def make_courtyard_lines(lines, pads, margin=0.25, grid=0.05, line_width=0.05):
    """Generate fp_line strings for a front courtyard rectangle.

    Computes the bounding box of all pads and graphics, adds margin,
    snaps outward to the grid, and returns a list of line strings.
    Returns an empty list if bounding box cannot be computed.
    """
    bbox = _compute_footprint_bbox(lines, pads)
    if bbox is None:
        return []

    xmin, ymin, xmax, ymax = bbox
    x1 = _snap_outward(xmin - margin, grid)
    y1 = _snap_outward(ymin - margin, grid)
    x2 = _snap_outward(xmax + margin, grid)
    y2 = _snap_outward(ymax + margin, grid)

    x1, y1, x2, y2 = (round(v, 6) for v in (x1, y1, x2, y2))

    layer = 'F.CrtYd'
    w = line_width
    return [
        f'  (fp_line (start {x1} {y1}) (end {x2} {y1}) (layer {layer}) (width {w}))\n',
        f'  (fp_line (start {x2} {y1}) (end {x2} {y2}) (layer {layer}) (width {w}))\n',
        f'  (fp_line (start {x2} {y2}) (end {x1} {y2}) (layer {layer}) (width {w}))\n',
        f'  (fp_line (start {x1} {y2}) (end {x1} {y1}) (layer {layer}) (width {w}))\n',
    ]


def make_triangle_line(pad1, approach, triangle_side=1.0, width=0, layer='F.SilkS'):
    """
    Return the fp_poly s-expression string for a filled equilateral triangle
    marker on the given layer, placed just outside pad 1.
    Width is 0 because the polygon is filled solid; the vertices alone
    define the visible shape.
    """
    h = triangle_side * math.sqrt(3) / 2
    gap = 0.15

    px, py = pad1['x'], pad1['y']
    pw, ph = pad1['w'], pad1['h']

    if approach == 'left':
        tip_x = px - pw / 2 - gap
        tip_y = py
        base_x = tip_x - h
        pts = [(tip_x, tip_y),
               (base_x, tip_y - triangle_side / 2),
               (base_x, tip_y + triangle_side / 2)]
    elif approach == 'right':
        tip_x = px + pw / 2 + gap
        tip_y = py
        base_x = tip_x + h
        pts = [(tip_x, tip_y),
               (base_x, tip_y - triangle_side / 2),
               (base_x, tip_y + triangle_side / 2)]
    elif approach == 'top':
        tip_x = px
        tip_y = py - ph / 2 - gap
        base_y = tip_y - h
        pts = [(tip_x, tip_y),
               (tip_x - triangle_side / 2, base_y),
               (tip_x + triangle_side / 2, base_y)]
    else:  # bottom
        tip_x = px
        tip_y = py + ph / 2 + gap
        base_y = tip_y + h
        pts = [(tip_x, tip_y),
               (tip_x - triangle_side / 2, base_y),
               (tip_x + triangle_side / 2, base_y)]

    xy_strs = ' '.join(f'(xy {round(x, 6)} {round(y, 6)})' for x, y in pts)
    return f'  (fp_poly (pts {xy_strs}) (layer {layer}) (width {width}) (fill solid))\n'


def make_pad1_rect(lines, pads):
    """
    If pad 1 (or a1) is a through-hole circular pad, change its shape to rect.
    Modifies lines in-place.  Returns True if a change was made.
    """
    pad1 = None
    for candidate in ('1', 'A1', 'a1'):
        pad1_list = [p for p in pads if p['number'] == candidate]
        if pad1_list:
            pad1 = pad1_list[0]
            break
    if pad1 is None:
        return False
    if pad1['type'] != 'thru_hole' or pad1['shape'] != 'circle':
        return False

    idx = pad1['line_idx']
    lines[idx] = re.sub(
        r'(\(pad\s+"?(?:1|A1|a1)"?\s+thru_hole\s+)circle',
        r'\1rect',
        lines[idx]
    )
    return True


def convert_rect_to_roundrect(lines, rratio=0.25):
    """Convert all rect pads to roundrect with the given corner ratio.

    Handles both single-line and multi-line pad definitions.
    Modifies lines in-place.  Returns the number of pads converted.
    """
    count = 0
    for i in range(len(lines)):
        # Match 'rect' as pad shape (after smd/thru_hole, before '(' or newline)
        # Single-line: (pad "1" smd rect (at ...
        # Multi-line:  (pad "1" smd rect\n
        if re.search(r'\(pad\s+"?[^"]*"?\s+\w+\s+rect\b', lines[i]):
            # Replace 'rect' shape keyword with 'roundrect'
            lines[i] = re.sub(
                r'(\(pad\s+"?[^"]*"?\s+\w+\s+)rect\b',
                r'\1roundrect',
                lines[i]
            )
            # Add roundrect_rratio if not already present in this pad
            # For single-line pads, insert before the closing paren
            # For multi-line pads, we need to find where to add it
            # Check if rratio is already somewhere in this pad block
            # First, check if the pad is single-line (balanced parens)
            depth = lines[i].count('(') - lines[i].count(')')
            if depth <= 0:
                # Single-line pad — insert rratio before last ')'
                if 'roundrect_rratio' not in lines[i]:
                    lines[i] = re.sub(
                        r'\)\s*$',
                        f' (roundrect_rratio {rratio}))\n',
                        lines[i]
                    )
            else:
                # Multi-line pad — find the closing line and insert before it
                j = i + 1
                has_rratio = 'roundrect_rratio' in lines[i]
                while j < len(lines) and depth > 0:
                    depth += lines[j].count('(') - lines[j].count(')')
                    if 'roundrect_rratio' in lines[j]:
                        has_rratio = True
                    if depth <= 0 and not has_rratio:
                        # Insert rratio before this closing line
                        indent = re.match(r'(\s*)', lines[j]).group(1)
                        lines.insert(j, f'{indent}\t(roundrect_rratio {rratio})\n')
                        break
                    j += 1
            count += 1
    return count


def find_insertion_point(lines):
    """
    Find the line index where the triangle should be inserted.
    Strategy: insert just before the first (model ...) line, or before the
    closing ')' of the module if there is no model.
    """
    for i, line in enumerate(lines):
        if line.strip().startswith('(model '):
            return i
    # No model found — insert before the last closing paren
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].strip() == ')':
            return i
    return len(lines) - 1


def process_file(filepath, approach_override=None, dry_run=False,
                 triangle_side=1.0, width=0, force=False):
    """
    Add a pin 1 triangle marker to a single .kicad_mod file.

    Returns (status, pad1_changed, crtyd_added, roundrect_count) where status is one of:
    'added', 'skipped-exists', 'skipped-nopad1', 'skipped-npth', or 'error'.
    """
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
    except OSError as e:
        print(f'  ERROR reading {filepath}: {e}', file=sys.stderr)
        return 'error', False, False, 0

    has_marker = already_has_pin1_marker(lines)

    # Always ensure courtyard encompasses all pads and graphics
    crtyd_added = False
    pads = find_pads(lines)
    if pads:
        # Compute what the courtyard should be (excluding existing courtyard lines)
        lines_no_crtyd = [l for l in lines if 'F.CrtYd' not in l and 'CrtYd' not in l]
        new_crtyd_lines = make_courtyard_lines(lines_no_crtyd, pads)
        if new_crtyd_lines:
            existing = get_courtyard_extent(lines)
            needed = get_courtyard_extent(new_crtyd_lines)
            if existing is None or (needed is not None and
                    (needed[0] > existing[0] + 0.001 or needed[1] > existing[1] + 0.001)):
                # Remove old courtyard lines and insert new ones
                lines = [l for l in lines if 'F.CrtYd' not in l and 'CrtYd' not in l]
                idx = find_insertion_point(lines)
                for cl in reversed(new_crtyd_lines):
                    lines.insert(idx, cl)
                crtyd_added = True

    # Convert all rect pads to roundrect (always, even if marker exists)
    roundrect_count = convert_rect_to_roundrect(lines)

    if not force and has_marker:
        if crtyd_added or roundrect_count > 0:
            try:
                with open(filepath, 'w') as f:
                    f.writelines(lines)
            except OSError as e:
                print(f'  ERROR writing {filepath}: {e}', file=sys.stderr)
                return 'error', False, False, 0
        return 'skipped-exists', False, crtyd_added, roundrect_count

    # When forcing, remove any existing pin 1 marker(s) first
    if force:
        lines = [l for l in lines
                 if not ('(fp_poly' in l and 'F.SilkS' in l and 'fill solid' in l)]

    pads = find_pads(lines)
    if not pads:
        return 'skipped-nopad1', False, False, 0

    # Find pad 1: try numeric "1", then BGA "A1", then letter-row "a1",
    # then the first rect-shaped pad (likely pin 1), then just the first pad.
    pad1 = None
    for candidate in ('1', 'A1', 'a1'):
        pad1_list = [p for p in pads if p['number'] == candidate]
        if pad1_list:
            pad1 = pad1_list[0]
            break

    if pad1 is None:
        # Try the first pad with rect shape (conventional pin 1 indicator)
        rect_pads = [p for p in pads
                     if p['shape'] in ('rect', 'roundrect') and p['number'] != '']
        if rect_pads:
            pad1 = rect_pads[0]

    if pad1 is None:
        # Fall back to the first numbered pad
        numbered = [p for p in pads if p['number'] != '']
        if numbered:
            pad1 = numbered[0]

    if pad1 is None:
        return 'skipped-nopad1', False, False, 0

    # Skip if pad 1 is NPTH (non-plated through hole, e.g. mounting holes)
    if pad1['type'] == 'np_thru_hole':
        return 'skipped-npth', False, False, 0

    if approach_override:
        approach = approach_override
    else:
        approach = determine_approach(pad1, pads)

    # Clamp triangle size to courtyard dimension along the base direction
    crtyd = get_courtyard_extent(lines)
    if crtyd is not None:
        cw, ch = crtyd
        # top/bottom → base is horizontal → clamp to courtyard width
        # left/right → base is vertical   → clamp to courtyard height
        limit = cw if approach in ('top', 'bottom') else ch
        triangle_side = min(triangle_side, limit)

    # Convert circular THT pad 1 to rect (then roundrect conversion below catches it)
    pad1_changed = make_pad1_rect(lines, pads)

    # Rect pads already converted to roundrect above (before skip check)

    triangle_line = make_triangle_line(pad1, approach, triangle_side, width)

    insert_idx = find_insertion_point(lines)
    lines.insert(insert_idx, triangle_line)

    if dry_run:
        msg = f'  Would add {approach} triangle at pad 1 ({pad1["x"]}, {pad1["y"]})'
        if pad1_changed:
            msg += ' [pad 1 circle->rect]'
        if crtyd_added:
            msg += ' [courtyard added]'
        print(msg)
        return 'added', pad1_changed, crtyd_added, roundrect_count

    try:
        with open(filepath, 'w') as f:
            f.writelines(lines)
    except OSError as e:
        print(f'  ERROR writing {filepath}: {e}', file=sys.stderr)
        return 'error', False, False, 0

    return 'added', pad1_changed, crtyd_added, roundrect_count


def collect_kicad_mod_files(pattern, recursive=False):
    """Collect .kicad_mod files matching pattern.

    If pattern is a directory, collect all .kicad_mod files in it
    (recursively if -r is set, otherwise just the top level).
    Otherwise treat pattern as a glob (with ** honoured when recursive).
    """
    if os.path.isdir(pattern):
        if recursive:
            matches = []
            for root, dirs, filenames in os.walk(pattern):
                for fn in sorted(filenames):
                    if fn.endswith('.kicad_mod'):
                        matches.append(os.path.join(root, fn))
            return matches
        else:
            return sorted(glob.glob(os.path.join(pattern, '*.kicad_mod')))

    if os.path.isfile(pattern):
        return [pattern] if pattern.endswith('.kicad_mod') else []

    # Treat as a glob pattern
    if recursive:
        # If the pattern doesn't already include '**', prepend it
        if '**' not in pattern:
            matches = sorted(glob.glob(os.path.join('**', pattern), recursive=True))
        else:
            matches = sorted(glob.glob(pattern, recursive=True))
    else:
        matches = sorted(glob.glob(pattern))

    return [f for f in matches if f.endswith('.kicad_mod')]


def main():
    parser = argparse.ArgumentParser(
        description='Add a pin 1 triangle marker to .kicad_mod footprint files.')
    parser.add_argument('path', help='File, directory, or wildcard pattern to process')
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='Recursively process subdirectories')
    parser.add_argument('--approach', choices=['left', 'right', 'top', 'bottom'],
                        default=None, help='Force approach direction (default: auto-detect)')
    parser.add_argument('--side', type=float, default=1.0,
                        help='Triangle side length in mm (default: 1.0)')
    parser.add_argument('--width', type=float, default=0,
                        help='Polygon stroke width in mm (default: 0; filled shape needs no stroke)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Show what would change without modifying files')
    parser.add_argument('--force', action='store_true',
                        help='Add marker even if one already exists')
    parser.add_argument('-j', '--jobs', type=int, default=None,
                        help='Number of parallel workers (default: number of CPUs)')
    args = parser.parse_args()

    files = collect_kicad_mod_files(args.path, args.recursive)
    if not files:
        print(f'No .kicad_mod files found matching: {args.path}')
        sys.exit(1)

    counts = {'added': 0, 'skipped-exists': 0, 'skipped-nopad1': 0,
              'skipped-npth': 0, 'error': 0}
    pad1_rect_count = 0
    crtyd_count = 0
    total_roundrect = 0

    def _tally(counts, status, pad1_changed, crtyd_added, roundrect_count,
               fp, dry_run):
        nonlocal pad1_rect_count, crtyd_count, total_roundrect
        counts[status] = counts.get(status, 0) + 1
        if pad1_changed:
            pad1_rect_count += 1
        if crtyd_added:
            crtyd_count += 1
        total_roundrect += roundrect_count
        if status == 'added':
            action = 'Would add' if dry_run else 'Added'
            suffix = ''
            if pad1_changed:
                suffix += ' [pad 1 circle->rect]'
            if crtyd_added:
                suffix += ' [courtyard added]'
            if roundrect_count:
                suffix += f' [{roundrect_count} rect->roundrect]'
            print(f'  {action} pin 1 marker: {os.path.basename(fp)}{suffix}')

    jobs = args.jobs if args.jobs else os.cpu_count()

    if len(files) == 1 or jobs == 1:
        # Sequential path — no multiprocessing overhead
        for fp in files:
            status, pad1_changed, crtyd_added, roundrect_count = process_file(
                fp, args.approach, args.dry_run, args.side, args.width, args.force)
            _tally(counts, status, pad1_changed, crtyd_added, roundrect_count,
                   fp, args.dry_run)
    else:
        with concurrent.futures.ProcessPoolExecutor(max_workers=jobs) as executor:
            future_to_fp = {
                executor.submit(process_file, fp, args.approach, args.dry_run,
                                args.side, args.width, args.force): fp
                for fp in files
            }
            for future in concurrent.futures.as_completed(future_to_fp):
                fp = future_to_fp[future]
                try:
                    status, pad1_changed, crtyd_added, roundrect_count = future.result()
                except Exception as e:
                    print(f'  ERROR processing {fp}: {e}', file=sys.stderr)
                    counts['error'] += 1
                    continue
                _tally(counts, status, pad1_changed, crtyd_added, roundrect_count,
                       fp, args.dry_run)

    total = len(files)
    print(f'\nProcessed {total} file(s) using {jobs} worker(s): '
          f'{counts["added"]} added, '
          f'{counts["skipped-exists"]} already had marker, '
          f'{counts["skipped-nopad1"]} no pad 1, '
          f'{counts["skipped-npth"]} NPTH only, '
          f'{counts["error"]} errors, '
          f'{pad1_rect_count} pad 1 circle->rect, '
          f'{crtyd_count} courtyard added, '
          f'{total_roundrect} rect->roundrect')


if __name__ == '__main__':
    main()

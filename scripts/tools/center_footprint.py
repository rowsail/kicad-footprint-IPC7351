#!/usr/bin/env python3

"""
Center a .kicad_mod footprint so that (0,0) is at the geometric center of all pads.

Parses the s-expression format, finds the centroid of all pad positions,
then shifts every coordinate in the file so the centroid becomes the origin.

Usage:
    python center_footprint.py <file_or_dir> [options]

    # Center a single file:
    python center_footprint.py MyPart.kicad_mod

    # Process all .kicad_mod in a directory tree:
    python center_footprint.py /path/to/footprints/

    # Dry-run (show offsets without modifying):
    python center_footprint.py /path/to/footprints/ --dry-run
"""

import argparse
import math
import os
import re
import sys


# Number of decimal places to round coordinates to
COORD_DECIMALS = 6


def _fmt(v):
    """Format a float, stripping unnecessary trailing zeros."""
    s = f'{v:.{COORD_DECIMALS}f}'
    if '.' in s:
        s = s.rstrip('0').rstrip('.')
    return s


def parse_pads(text):
    """
    Return a list of (x, y) for every pad in the file.
    Matches:  (pad <name> <type> <shape> (at <x> <y> [<rot>]) ...)
    """
    pads = []
    for m in re.finditer(
            r'\(pad\s+\S+\s+\S+\s+\S+\s+\(at\s+([-\d.eE+]+)\s+([-\d.eE+]+)',
            text):
        pads.append((float(m.group(1)), float(m.group(2))))
    return pads


def compute_centroid(pads):
    """Return (cx, cy) geometric center of the pad positions."""
    if not pads:
        return (0.0, 0.0)
    cx = sum(x for x, y in pads) / len(pads)
    cy = sum(y for x, y in pads) / len(pads)
    return (cx, cy)


def _shift_xy(match, dx, dy):
    """Shift a regex match containing two coordinate groups."""
    x = float(match.group(1)) + dx
    y = float(match.group(2)) + dy
    return match.group(0).replace(match.group(1), _fmt(x), 1).replace(
        match.group(2), _fmt(y), 1)


def shift_coordinates(text, dx, dy):
    """
    Shift all geometric coordinates in a .kicad_mod file by (dx, dy).

    Handles:
      (at X Y)           — pads, text
      (at X Y ROT)       — pads, text with rotation
      (start X Y)        — fp_line, fp_arc
      (end X Y)          — fp_line, fp_arc
      (center X Y)       — fp_circle
      (xy X Y)           — fp_poly points
      (at (xyz X Y Z))   — 3D model offset (shift X and Y, keep Z)
    """

    def _shift_at(m):
        """Shift (at X Y) or (at X Y ROT), but NOT (at (xyz ...))."""
        x = float(m.group(1)) + dx
        y = float(m.group(2)) + dy
        rest = m.group(3) or ''
        return f'(at {_fmt(x)} {_fmt(y)}{rest})'

    def _shift_start(m):
        x = float(m.group(1)) + dx
        y = float(m.group(2)) + dy
        return f'(start {_fmt(x)} {_fmt(y)})'

    def _shift_end(m):
        x = float(m.group(1)) + dx
        y = float(m.group(2)) + dy
        return f'(end {_fmt(x)} {_fmt(y)})'

    def _shift_center(m):
        x = float(m.group(1)) + dx
        y = float(m.group(2)) + dy
        return f'(center {_fmt(x)} {_fmt(y)})'

    def _shift_xy(m):
        x = float(m.group(1)) + dx
        y = float(m.group(2)) + dy
        return f'(xy {_fmt(x)} {_fmt(y)})'

    def _shift_xyz(m):
        x = float(m.group(1)) + dx
        y = float(m.group(2)) + dy
        z = m.group(3)
        return f'(at (xyz {_fmt(x)} {_fmt(y)} {z}))'

    # Process 3D model (at (xyz ...)) FIRST, before the generic (at ...) pattern
    text = re.sub(
        r'\(at \(xyz\s+([-\d.eE+]+)\s+([-\d.eE+]+)\s+([-\d.eE+]+)\)\)',
        _shift_xyz, text)

    # (at X Y) or (at X Y ROT) — but not (at (xyz ...)) which was already handled
    text = re.sub(
        r'\(at\s+([-\d.eE+]+)\s+([-\d.eE+]+)(\s+[-\d.eE+]+)?\)',
        _shift_at, text)

    text = re.sub(
        r'\(start\s+([-\d.eE+]+)\s+([-\d.eE+]+)\)',
        _shift_start, text)

    text = re.sub(
        r'\(end\s+([-\d.eE+]+)\s+([-\d.eE+]+)\)',
        _shift_end, text)

    text = re.sub(
        r'\(center\s+([-\d.eE+]+)\s+([-\d.eE+]+)\)',
        _shift_center, text)

    text = re.sub(
        r'\(xy\s+([-\d.eE+]+)\s+([-\d.eE+]+)\)',
        _shift_xy, text)

    return text


def process_file(filepath, dry_run=False, threshold=0.001):
    """
    Center a single .kicad_mod file on its pad centroid.

    Returns a status string: 'centered', 'skipped-already', 'skipped-nopads',
    or 'error', plus the (dx, dy) shift applied.
    """
    try:
        with open(filepath, 'r') as f:
            text = f.read()
    except OSError as e:
        print(f'  ERROR reading {filepath}: {e}', file=sys.stderr)
        return 'error', (0, 0)

    pads = parse_pads(text)
    if not pads:
        return 'skipped-nopads', (0, 0)

    cx, cy = compute_centroid(pads)

    # If already centered (within threshold), skip
    if abs(cx) < threshold and abs(cy) < threshold:
        return 'skipped-already', (cx, cy)

    dx, dy = -cx, -cy

    if dry_run:
        print(f'  Would shift by ({_fmt(dx)}, {_fmt(dy)}) '
              f'— centroid was ({_fmt(cx)}, {_fmt(cy)}), {len(pads)} pads')
        return 'centered', (dx, dy)

    new_text = shift_coordinates(text, dx, dy)

    try:
        with open(filepath, 'w') as f:
            f.write(new_text)
    except OSError as e:
        print(f'  ERROR writing {filepath}: {e}', file=sys.stderr)
        return 'error', (dx, dy)

    return 'centered', (dx, dy)


def collect_kicad_mod_files(path):
    """Recursively collect all .kicad_mod files under path."""
    if os.path.isfile(path):
        if path.endswith('.kicad_mod'):
            return [path]
        return []
    files = []
    for root, dirs, filenames in os.walk(path):
        for fn in sorted(filenames):
            if fn.endswith('.kicad_mod'):
                files.append(os.path.join(root, fn))
    return files


def main():
    parser = argparse.ArgumentParser(
        description='Center .kicad_mod footprints on the geometric center of all pads.')
    parser.add_argument('path', help='File or directory to process')
    parser.add_argument('--dry-run', action='store_true',
                        help='Show offsets without modifying files')
    parser.add_argument('--threshold', type=float, default=0.001,
                        help='Skip files already centered within this tolerance (mm, default: 0.001)')
    args = parser.parse_args()

    files = collect_kicad_mod_files(args.path)
    if not files:
        print(f'No .kicad_mod files found at {args.path}')
        sys.exit(1)

    counts = {'centered': 0, 'skipped-already': 0, 'skipped-nopads': 0, 'error': 0}

    for fp in files:
        status, (dx, dy) = process_file(fp, args.dry_run, args.threshold)
        counts[status] = counts.get(status, 0) + 1
        if status == 'centered':
            action = 'Would center' if args.dry_run else 'Centered'
            print(f'  {action}: {os.path.basename(fp)}  '
                  f'shift=({_fmt(dx)}, {_fmt(dy)})')

    total = len(files)
    print(f'\nProcessed {total} file(s): '
          f'{counts["centered"]} centered, '
          f'{counts["skipped-already"]} already centered, '
          f'{counts["skipped-nopads"]} no pads, '
          f'{counts["error"]} errors')


if __name__ == '__main__':
    main()

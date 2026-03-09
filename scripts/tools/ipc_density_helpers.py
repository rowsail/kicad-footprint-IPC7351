#!/usr/bin/env python3

"""
IPC-7351 density level helpers for footprint generators.

Provides:
  - Density suffix naming ("M", "N", "L") per IPC-7351 land protrusion
  - Pin 1 markers: external triangle (silkscreen) and internal circle (fab layer)
  - Iteration over all three density levels
"""

import math
import os
import sys

sys.path.append(os.path.join(sys.path[0], "..", ".."))
from KicadModTree import *  # NOQA

# Mapping from internal density names to IPC-7351 suffix codes.
# Land protrusion letter only:
#   M = Most (Level A)    - maximum land protrusion
#   N = Nominal (Level B) - median land protrusion
#   L = Least (Level C)   - least land protrusion
DENSITY_SUFFIX_MAP = {
    'most':    'M',
    'nominal': 'N',
    'least':   'L',
}

ALL_DENSITY_LEVELS = ['most', 'nominal', 'least']

# CLI letter to internal density name
DENSITY_LETTER_MAP = {
    'M': 'most',
    'N': 'nominal',
    'L': 'least',
}


def get_density_suffix(density_name):
    """Return the IPC-7351 density suffix string (e.g. 'N') for a density name."""
    return DENSITY_SUFFIX_MAP.get(density_name, 'N')


# Base output directory for all generated footprints.
# Uses FP_OUTPUT_ROOT env var if set, otherwise 'newfp' relative to cwd.
FP_OUTPUT_DIR = os.environ.get('FP_OUTPUT_ROOT', 'newfp')


def get_density_subdir(density_name):
    """Return the density subdirectory path (e.g. '<root>/N') for a density name."""
    return os.path.join(FP_OUTPUT_DIR, DENSITY_SUFFIX_MAP.get(density_name, 'N'))


def append_density_suffix(fp_name, density_name):
    """Append the IPC-7351 density suffix to a footprint name."""
    return fp_name + '_' + get_density_suffix(density_name)


def add_pin1_marker_triangle(kicad_mod, pin1_pos, pad_size, approach='left',
                             silk_line_width=0, triangle_side=1.0, layer="F.SilkS"):
    """
    Add an external pin 1 marker as a filled equilateral triangle on the
    silkscreen layer.  The triangle tip points toward pad 1 from the given
    approach direction, placed just outside the pad edge.

    Parameters:
        kicad_mod:       The Footprint object to append to.
        pin1_pos:        (x, y) center of pad 1.
        pad_size:        (w, h) size of pad 1.
        approach:        Direction from which the triangle approaches pad 1:
                         'left', 'right', 'top', or 'bottom'.
        silk_line_width: Width of silkscreen lines.
        triangle_side:   Side length of the equilateral triangle in mm.
        layer:           Layer name for the marker.
    """
    h = triangle_side * math.sqrt(3) / 2
    gap = 0.15  # clearance between triangle tip and pad edge

    px, py = pin1_pos
    pw, ph = pad_size

    if approach == 'left':
        # Triangle to the left of pad, pointing right
        tip_x = px - pw / 2 - gap
        tip_y = py
        base_x = tip_x - h
        triangle = [
            {'x': tip_x, 'y': tip_y},
            {'x': base_x, 'y': tip_y - triangle_side / 2},
            {'x': base_x, 'y': tip_y + triangle_side / 2},
        ]
    elif approach == 'right':
        # Triangle to the right of pad, pointing left
        tip_x = px + pw / 2 + gap
        tip_y = py
        base_x = tip_x + h
        triangle = [
            {'x': tip_x, 'y': tip_y},
            {'x': base_x, 'y': tip_y - triangle_side / 2},
            {'x': base_x, 'y': tip_y + triangle_side / 2},
        ]
    elif approach == 'top':
        # Triangle above pad, pointing down
        tip_x = px
        tip_y = py - ph / 2 - gap
        base_y = tip_y - h
        triangle = [
            {'x': tip_x, 'y': tip_y},
            {'x': tip_x - triangle_side / 2, 'y': base_y},
            {'x': tip_x + triangle_side / 2, 'y': base_y},
        ]
    else:  # 'bottom'
        # Triangle below pad, pointing up
        tip_x = px
        tip_y = py + ph / 2 + gap
        base_y = tip_y + h
        triangle = [
            {'x': tip_x, 'y': tip_y},
            {'x': tip_x - triangle_side / 2, 'y': base_y},
            {'x': tip_x + triangle_side / 2, 'y': base_y},
        ]

    kicad_mod.append(Polygon(
        nodes=triangle,
        width=silk_line_width,
        layer=layer,
        fill=True))


def add_pin1_marker_circle(kicad_mod, body_edge, pad_details, device_params,
                           fab_line_width=0.1, circle_diameter=1.0, layer="F.Fab"):
    """
    Add an internal pin 1 marker as a filled circle on the fabrication layer.
    The circle is placed inside the body outline near pin 1 (top-left corner).

    Parameters:
        kicad_mod:      The Footprint object to append to.
        body_edge:      Dict with 'left', 'right', 'top', 'bottom' body edges.
        pad_details:    Pad details dict.
        device_params:  Device parameters dict.
        fab_line_width: Width of fabrication layer lines.
        circle_diameter: Diameter of the circle in mm.
        layer:          Layer name for the marker.
    """
    radius = circle_diameter / 2
    inset = radius + 0.3  # offset from body edge

    num_pins_x = device_params.get('num_pins_x', 0)
    num_pins_y = device_params.get('num_pins_y', 0)

    # Compute the gap between opposing pad inner edges.
    # Skip the circle if there isn't enough room (< 3mm).
    if pad_details:
        if num_pins_y > 0 and 'left' in pad_details and 'right' in pad_details:
            pdl = pad_details['left']
            pdr = pad_details['right']
            lx = pdl.get('center', pdl.get('start', [0, 0]))[0]
            rx = pdr.get('center', pdr.get('start', [0, 0]))[0]
            gap_x = (rx - pdr['size'][0] / 2) - (lx + pdl['size'][0] / 2)
        else:
            gap_x = float('inf')

        if num_pins_x > 0 and 'top' in pad_details and 'bottom' in pad_details:
            pdt = pad_details['top']
            pdb = pad_details['bottom']
            ty = pdt.get('center', pdt.get('start', [0, 0]))[1]
            by = pdb.get('center', pdb.get('start', [0, 0]))[1]
            gap_y = (by - pdb['size'][1] / 2) - (ty + pdt['size'][1] / 2)
        else:
            gap_y = float('inf')

        if min(gap_x, gap_y) < 3.0:
            return

    if num_pins_y > 0 and num_pins_x == 0:
        # Dual-row: pin 1 at top of left side
        pitch = device_params.get('pitch', 0)
        pin1_y = -(num_pins_y - 1) * pitch / 2
        cx = body_edge['left'] + inset
        cy = max(pin1_y, body_edge['top'] + inset)
    else:
        # Quad or other: pin 1 near top-left
        cx = body_edge['left'] + inset
        cy = body_edge['top'] + inset

    kicad_mod.append(Circle(
        center=[cx, cy],
        radius=radius,
        width=0,
        layer=layer,
        fill=True))
    kicad_mod.append(Circle(
        center=[cx, cy],
        radius=radius,
        width=0,
        layer="F.SilkS",
        fill=True))

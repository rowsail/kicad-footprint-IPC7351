# KiCad Footprint Generator — IPC-7351 Multi-Density Edition

Based on [pointhi/kicad-footprint-generator](https://github.com/pointhi/kicad-footprint-generator),
this fork adds support for generating footprint libraries at all three
**IPC-7351** density levels and applies consistent post-processing to every
generated footprint.

**Licence:** GNU GPLv3+

## IPC-7351 Density Levels

IPC-7351 defines three land-pattern density levels that trade soldering
ease against board area:

| Level | Directory | Description |
|-------|-----------|-------------|
| **M** (Most) | `newfp/M/` | Maximum pad size — easiest to solder, largest footprint |
| **N** (Nominal) | `newfp/N/` | Standard pad size — general-purpose |
| **L** (Least) | `newfp/L/` | Minimum pad size — smallest footprint, tightest boards |

Generators that natively support the `--density` / `--all-densities`
flags (IPC gullwing, QFN/DFN, BGA, PLCC, SMD chip, electrolytic
capacitors) write directly into the appropriate density sub-directory.
For generators that produce only a single density, the build script
reconciles the output so that every `.pretty` library appears in all
three directories (copying N→M, N→L, or L→N as needed).

## Quick Start

```sh
cd scripts
python3 -m venv ../../.venv && source ../../.venv/bin/activate
pip install -r ../requirements.txt
bash regenerate_all.sh
```

`regenerate_all.sh` runs every generator in parallel, collects the
output into `scripts/newfp/{M,N,L}/`, reconciles densities, and
applies post-processing. On a typical machine it finishes in ~3 minutes
and produces ~25,000 footprints.

## Post-Processing (`tidykicadfp.py`)

After generation, `scripts/tools/tidykicadfp.py` is run across every
footprint in every density directory. It can also be used standalone on
any `.kicad_mod` file or `.pretty` directory. The post-processing steps
are:

### Pin 1 Marker Triangle

A small filled triangle is added to the silkscreen layer near pad 1.
The triangle is placed outside the pad extent, approaching from the
direction that has the most clearance (left, right, top, or bottom).
Its size is clamped so it never extends beyond the courtyard boundary.
THT footprints additionally have pad 1 converted from a circle to a
rectangle for visual identification.

### Courtyard Generation

If a footprint has no courtyard lines, or its existing courtyard is
smaller than the computed one, a new `F.CrtYd` rectangle is generated:

- **Margin:** 0.25 mm beyond the bounding box of all pads and graphic
  elements (text is excluded from the bounding box).
- **Grid snap:** Coordinates are snapped outward to the nearest 0.05 mm.
- **Line width:** 0.05 mm.

### Rect-to-Roundrect Pad Conversion

All rectangular SMD pads are converted to roundrect with a corner
radius ratio of 0.25 (i.e. the corner radius is 25% of the shorter
pad dimension). This matches the IPC-7351 recommended land-pattern
shape and improves solder paste release.

## Standalone Usage

`tidykicadfp.py` can be used independently on any footprint library:

```sh
# Process a single file
python3 scripts/tools/tidykicadfp.py path/to/footprint.kicad_mod

# Recursively process a .pretty directory
python3 scripts/tools/tidykicadfp.py -r path/to/Library.pretty/

# Dry run (report changes without writing)
python3 scripts/tools/tidykicadfp.py --dry-run -r path/to/Library.pretty/

# Use multiple workers
python3 scripts/tools/tidykicadfp.py -r -j 8 path/to/Library.pretty/
```

Options:

| Flag | Description |
|------|-------------|
| `-r` | Recurse into directories |
| `-j N` | Use N parallel workers (default: CPU count) |
| `--dry-run` | Report what would change without writing files |
| `--force` | Re-add pin 1 marker even if one already exists |
| `--approach DIR` | Force triangle approach direction (left/right/top/bottom) |
| `--side F` | Triangle side length multiplier (default: 1.0) |
| `--width W` | Triangle line width; 0 = filled (default: 0) |

## Project Structure

```
KicadModTree/           - The KicadModTree framework for footprint generation
scripts/                - Generator scripts, organised by component family
scripts/tools/          - Shared tools and helpers
  tidykicadfp.py        - Post-processing: pin 1 marker, courtyard, roundrect
  ipc_density_helpers.py - Density subdirectory helpers, pin 1 marker functions
  center_footprint.py   - Footprint centering utility
scripts/regenerate_all.sh - Parallel master build script
scripts/newfp/          - Generated output (M/N/L density directories)
```

## Changes from Upstream

This fork includes the following modifications to the original generators:

- **IPC generators** (gullwing, noLead, BGA, PLCC): output to M/N/L density
  sub-directories via `ipc_density_helpers.get_density_subdir()`.
- **SMD chip and electrolytic capacitor generators**: density-aware output.
- **Bug fixes**: BGA undefined variable, CP_Elec_round YAML key mismatch,
  mecf_connector 3D coordinates in 2D vectors, pin_headers absolute path,
  socket_strips typo, Python 2→3 syntax in potentiometers, Hirose/Samtec
  connector fixes.
- **KicadModTree**: `fill` parameter support for Circle and Polygon nodes.

## Original Framework

The underlying KicadModTree framework is by
[Thomas Pointhuber](https://github.com/pointhi/kicad-footprint-generator).
See the original [documentation](http://kicad-footprint-generator.readthedocs.io/en/latest/)
for details on writing custom generator scripts.

#!/bin/bash
# Master script to regenerate all footprints and add pin 1 markers.
# Run from: kicad-footprint-generator/scripts/
set -e

SCRIPTS="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPTS"
START_TIME=$SECONDS

# All footprints go into scripts/newfp/{M,N,L}/<lib>.pretty/
export FP_OUTPUT_ROOT="$SCRIPTS/newfp"
rm -rf "$FP_OUTPUT_ROOT"

echo "========================================="
echo "  Regenerating all footprints"
echo "========================================="

# --- Parallel infrastructure ---
MAX_JOBS=$(( $(nproc 2>/dev/null || echo 4) * 2 ))
PIDS=()
PID_LABELS=()
LOGDIR=$(mktemp -d)
FAIL_COUNT=0

# Run a generator in the background, throttled to MAX_JOBS
run() {
    local dir="$1"; shift
    local label="[$dir] $*"

    # Throttle: wait if we've hit the job limit
    while (( ${#PIDS[@]} >= MAX_JOBS )); do
        _reap_one
    done

    local logbase
    logbase="$(echo "$label" | tr '/ ' '__')"
    # Truncate log filename to stay within filesystem limits
    if (( ${#logbase} > 200 )); then
        logbase="${logbase:0:200}"
    fi
    local logfile="$LOGDIR/${logbase}.log"
    (cd "$dir" && PYTHONPATH="${SCRIPTS}/..${PYTHONPATH:+:$PYTHONPATH}" python "$@") > "$logfile" 2>&1 &
    PIDS+=($!)
    PID_LABELS+=("$label")
}

# Wait for one job to finish and check its exit code
_reap_one() {
    # Wait for any single child
    local i
    for i in "${!PIDS[@]}"; do
        if ! kill -0 "${PIDS[$i]}" 2>/dev/null; then
            wait "${PIDS[$i]}" || {
                echo "  FAILED: ${PID_LABELS[$i]}" >&2
                FAIL_COUNT=$((FAIL_COUNT + 1))
            }
            unset 'PIDS[i]' 'PID_LABELS[i]'
            PIDS=("${PIDS[@]}")
            PID_LABELS=("${PID_LABELS[@]}")
            return
        fi
    done
    # All still running — brief sleep then retry
    sleep 0.1
}

# Wait for ALL remaining background jobs
wait_all() {
    while (( ${#PIDS[@]} > 0 )); do
        _reap_one
    done
    if (( FAIL_COUNT > 0 )); then
        echo ""
        echo "WARNING: $FAIL_COUNT generator(s) failed. Check logs in $LOGDIR" >&2
    fi
}

echo "Running generators with up to $MAX_JOBS parallel jobs..."

# --- SMD chip (resistors, caps, inductors, diodes, LEDs, fuses, tantalum) ---
run SMD_chip_package_rlc-etc \
    SMD_chip_package_rlc-etc.py SMD_chip_devices.yaml \
    --ipc_definition ipc7351B_smd_two_terminal_chip.yaml \
    --global_config config_KLCv3.0.yaml \
    --series_config ipc_smd_two_terminal_chip.yaml

# --- Electrolytic caps ---
run Capacitors_SMD C_Elec_round.py --all-densities C_Elec_round.yaml
run Capacitors_SMD CP_Elec_round.py CP_Elec_round.yaml

# --- Trimmers ---
run Capacitors_SMD C_Trimmer_factory.py

# --- IPC packages ---
# Globs must be expanded after cd, so we build the file lists inline.
run Packages/Package_Gullwing__QFP_SOIC_SO ipc_gullwing_generator.py \
    $(cd Packages/Package_Gullwing__QFP_SOIC_SO && echo size_definitions/*.yaml)
run Packages/Package_NoLead__DFN_QFN_LGA_SON ipc_noLead_generator.py \
    $(cd Packages/Package_NoLead__DFN_QFN_LGA_SON && echo size_definitions/*.yaml size_definitions/qfn/*.yaml)
run Packages/Package_BGA ipc_bga_generator.py bga.yaml bga_xilinx.yaml csp.yaml
run Packages/Package_PLCC ipc_plcc_jLead_generator.py plcc_jLead_definitions.yaml

# --- DIP ---
run Packages/Package_DIP make_DIP_footprints.py

# --- DPAK ---
run Packages/TO_SOT_Packages_SMD DPAK.py

# --- TO_SOT_THT ---
run Packages/TO_SOT_THT TO_SOT_THT_generate.py

# --- Pin headers and socket strips ---
run pin-headers_socket-strips make_pin_headers.py
run pin-headers_socket-strips make_socket_strips.py
run pin-headers_socket-strips make_idc_headers.py
run Connector_PinSocket socket_strips.py

# --- Terminal blocks ---
run TerminalBlock_Phoenix make_TerminalBlock_Phoenix.py
run TerminalBlock_WAGO make_TerminalBlock_WAGO.py
run TerminalBlock_RND make_TerminalBlock_RND.py
run TerminalBlock_4Ucon make_TerminalBlock_4Ucon.py
run TerminalBlock_Altech Altech.py
run TerminalBlock_MetzConnect make_TerminalBlock_MetzConnect.py
run TerminalBlock_MetzConnect make_SingleTerminalBlock_MetzConnect.py
run TerminalBlock_Philmore make_TerminalBlock_Philmore.py
run TerminalBlock_TE-Connectivity make_TerminalBlock_TE-Connectivity.py

# --- Passive THT ---
run Resistor_THT make_Resistors_THT.py
run Capacitors_THT make_Capacitors_THT.py
run Diodes_THT make_Diodes_THT.py
run Chokes_THT make_Chokes_THT.py
run LEDs_THT make_LEDs_THT.py
run ResistorArrays_SIP_THT make_Resistor_array_SIP.py

# --- Crystals / Oscillators ---
run Crystals_Resonators_SMD make_crystal_smd.py
run Crystals_Resonators_THT make_crystal.py
run Oscillators_SMD make_oscillators.py

# --- Potentiometers ---
run Potentiometers make_Potentiometer_THT.py
run Potentiometers make_Potentiometer_SMD.py
run Potentiometers slide_Potentiometer.py

# --- Connectors DSub ---
run Connectors_DSub make_dsubs.py

# --- DIP switches ---
run Buttons_Switches make_DIPSwitches.py
run Buttons_Switches rotary_coded_switch.py

# --- Recom DCDC ---
run Recom_DCDC Recom_SIP.py

# --- Connector JST ---
for f in Connector/Connector_JST/conn_jst_*.py; do
    run "$(dirname "$f")" "$(basename "$f")"
done

# --- Connector Molex ---
for f in Connector/Connector_Molex/conn_molex_*.py Connector/Connector_Molex/conn_ffc_molex_*.py; do
    run "$(dirname "$f")" "$(basename "$f")"
done

# --- Connector Hirose ---
for f in Connector/Connector_Hirose/conn_*.py; do
    run "$(dirname "$f")" "$(basename "$f")"
done

# --- Connector TE ---
for f in Connector/Connector_TE-Connectivity/conn_*.py; do
    run "$(dirname "$f")" "$(basename "$f")"
done

# --- Connector PhoenixContact ---
run Connector/Connector_PhoenixContact mc.py
run Connector/Connector_PhoenixContact mstb.py

# --- Connector Wago ---
run Connector/Connector_Wago conn_wago_734_horizontal.py
run Connector/Connector_Wago conn_wago_734_vertical.py

# --- Connector Harwin ---
for f in Connector/Connector_Harwin/*.py; do
    run "$(dirname "$f")" "$(basename "$f")"
done

# --- Connector Samtec ---
run Connector/Connector_Samtec conn_samtec_hle.py
run Connector/Connector_Samtec conn_samtec_LSHM_smd_top.py
run Connector/Connector_Samtec mecf_connector.py
run Connector/Connector_Samtec mecf_socket.py

# --- Connector SMD single row ---
run Connector/Connector_SMD_single_row_plus_mounting_pad smd_single_row_plus_mounting_pad.py conn_hirose.yaml conn_jst.yaml conn_molex.yaml

# --- Connector JAE ---
for f in Connector/Connector_JAE/conn_*.py; do
    run "$(dirname "$f")" "$(basename "$f")"
done

# --- Connector Audio ---
for f in Connector/Connector_Audio/*.py; do
    run "$(dirname "$f")" "$(basename "$f")"
done

# --- Connector Wire ---
run Connector/Connector_Wire solder_wire_tht.py wire_MC_Flexivolt.yaml

# --- Connector PCBEdge ---
run Connector/Connector_PCBEdge molex_EDGELOCK.py

# --- Connector Stocko ---
run Connector/Connector_Stocko conn_Stocko_MKS_16xx.py

# --- Connector Wuerth ---
run Connector/Connector_Wuerth wuerth_6480xx11622.py

# --- Connector IEC DIN ---
run Connector/Connector_IEC_DIN generate_din41612.py

# --- Battery ---
run Battery BatteryHolder.py BatteryHolder.yml

# --- Converter DCDC ---
run Converter_DCDC Converter_DCDC.py
run Converter_DCDC XP_Power_SF_THT.py

# --- Buzzers ---
run Buzzers_Beepers buzzer_round_tht.py

# --- Fuse ---
run Fuse ptc-fuse-tht.py

# --- Inductors THT ---
for f in Inductors/*.py; do
    run "$(dirname "$f")" "$(basename "$f")"
done

# --- Inductor SMD ---
run Inductor_SMD Inductor_SMD.py

# --- LEDs SMD ---
run LEDs_SMD plcc4.py
run LEDs_SMD smlvn6.py

# --- Mounting Hardware ---
run Mounting_Hardware mounting_hole.py ../Mounting_Holes/mounting_hole_long.yaml
run Mounting_Hardware wuerth_smt_spacer.py

# --- Shielding ---
run Shielding smd_shielding.py laird_technologies_smd_shielding.kicad_mod.yaml wuerth_smd_shielding.kicad_mod.yaml
run Shielding wuerth_electronic_smd_shielding.py
run Shielding wuerth_electronic_tht_shielding.py

# --- Socket ---
run Socket 3M_Textool.py

# --- Vigortronix ---
run Vigortronix vigotronix.py

# --- general ---
run general smd_chip.py

# --- QFN (separate from ipc_noLead) ---
if [ -f Packages/Package_NoLead__DFN_QFN_LGA_SON/qfn.py ]; then
    run Packages/Package_NoLead__DFN_QFN_LGA_SON qfn.py
fi

# Wait for all background generators to finish before post-processing
wait_all

echo ""
echo "========================================="
echo "  All generators complete."
echo "========================================="
echo ""

# Count generated files
TOTAL=$(find . -name "*.kicad_mod" | wc -l)
echo "Total .kicad_mod files: $TOTAL"

echo ""
echo "========================================="
echo "  Copying non-density footprints into M/N/L"
echo "========================================="
# Density-aware generators output directly into newfp/{M,N,L}/<lib>.pretty/.
# All other generators output .pretty/ directories in their own subdirs.
# Find every .pretty/ that is NOT inside newfp/, and copy it into
# newfp/M/, newfp/N/, newfp/L/ so footprints are available at every density.
total_copied=0
while IFS= read -r -d '' pretty_dir; do
    base="$(basename "$pretty_dir")"
    for density_dir in M N L; do
        dest="$FP_OUTPUT_ROOT/$density_dir/$base"
        mkdir -p "$dest"
        cp -a "$pretty_dir"/. "$dest"/
    done
    count=$(find "$pretty_dir" -name '*.kicad_mod' | wc -l)
    total_copied=$((total_copied + count))
    rm -rf "$pretty_dir"
done < <(find . -not -path './newfp/*' -type d -name '*.pretty' -print0)
echo "  Copied $total_copied footprints into each of newfp/{M,N,L}/"

# Some generators (e.g. Potentiometers) write bare .kicad_mod files into their
# own directory without a .pretty wrapper.  Collect those too, grouping by the
# directory name they came from (e.g. Potentiometers → Potentiometer_SMD.pretty
# / Potentiometer_THT.pretty based on the footprint's 3D model reference, or
# just <dirname>.pretty as a fallback).
bare_copied=0
while IFS= read -r -d '' fp; do
    dir="$(dirname "$fp")"
    base="$(basename "$dir")"
    dest_lib="${base}.pretty"
    for density_dir in M N L; do
        dest="$FP_OUTPUT_ROOT/$density_dir/$dest_lib"
        mkdir -p "$dest"
        cp -a "$fp" "$dest"/
    done
    bare_copied=$((bare_copied + 1))
    rm -f "$fp"
done < <(find . -not -path './newfp/*' -not -path './.venv/*' -not -path './tools/*' -name '*.kicad_mod' -print0)
if (( bare_copied > 0 )); then
    echo "  Copied $bare_copied bare footprints into each of newfp/{M,N,L}/"
fi

echo ""
echo "========================================="
echo "  Reconciling density directories"
echo "========================================="
# Ensure every footprint that exists in any of M/N/L also exists in all three.
# A density-aware generator may omit some footprints for certain density levels;
# fill the gap from the nearest density:
#   Missing M → use N
#   Missing N → use L
#   Missing L → use N
declare -A FALLBACK
FALLBACK[M]="N"
FALLBACK[N]="L"
FALLBACK[L]="N"

# Collect all unique relative paths across all three density dirs
all_fps=$(mktemp)
for d in M N L; do
    (cd "$FP_OUTPUT_ROOT/$d" && find . -name '*.kicad_mod' -print0) >> "$all_fps"
done
sort -zu "$all_fps" > "${all_fps}.sorted"

reconciled=0
while IFS= read -r -d '' rel; do
    for dst_density in M N L; do
        dst="$FP_OUTPUT_ROOT/$dst_density/$rel"
        if [ ! -f "$dst" ]; then
            for src_density in ${FALLBACK[$dst_density]}; do
                src="$FP_OUTPUT_ROOT/$src_density/$rel"
                if [ -f "$src" ]; then
                    mkdir -p "$(dirname "$dst")"
                    cp -a "$src" "$dst"
                    reconciled=$((reconciled + 1))
                    break
                fi
            done
        fi
    done
done < "${all_fps}.sorted"
rm -f "$all_fps" "${all_fps}.sorted"
echo "  Reconciled $reconciled footprints across density directories"

echo ""
echo "========================================="
echo "  Adding pin 1 markers to all footprints"
echo "========================================="
python tools/tidykicadfp.py "$FP_OUTPUT_ROOT" -r

echo ""
FINAL_TOTAL=$(find "$FP_OUTPUT_ROOT" -name "*.kicad_mod" | wc -l)
ELAPSED=$((SECONDS - START_TIME))
echo "========================================="
echo "  DONE — $FINAL_TOTAL footprints in newfp/"
printf "  Elapsed: %d min %d sec\n" $((ELAPSED / 60)) $((ELAPSED % 60))
echo "========================================="

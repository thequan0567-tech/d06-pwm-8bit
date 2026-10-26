#!/usr/bin/env python3
import json, sys
if len(sys.argv) < 2: sys.exit(0)
with open(sys.argv[1], "r", encoding="utf-8") as f: m = json.load(f)
for label, keys in [
    ("So o (Total cells)", ["design__instance__count__stdcell", "synth__design__instance__count__stdcell"]),
    ("So Flip-Flop", ["design__instance__count__class:sequential_cell", "synth__design__instance__count__class:sequential_cell"]),
    ("Dien tich logic (um2)", ["design__instance__area__stdcell", "synth__design__instance__area__stdcell"]),
    ("Dien tich die (um2)", ["design__die__area"]),
    ("Tong do dai day (um)", ["route__wirelength"]),
    ("Setup WNS (ns)", ["timing__setup__wns"]),
    ("Hold WNS (ns)", ["timing__hold__wns"]),
    ("Clock skew (ns)", ["clock__skew__worst_setup"]),
    ("DRC (Magic / KLayout)", ["magic__drc_error__count", "klayout__drc_error__count"]),
    ("LVS errors", ["netgen__lvs_error__count"]),
    ("Cong suat tong (W)", ["power__total"]),
]:
    val = next((m[k] for k in keys if k in m), "N/A")
    print(f"{label:26s}: {val}")

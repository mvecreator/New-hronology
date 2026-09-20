#!/usr/bin/env python3
"""
Reproduce MDL-1 selector-entropy sensitivity analysis.

The 54-claim sample is fixed in data/mdl1_claims.csv.
No claims are added or removed here.

Conservative coding choices:
- structural/new-rule cost unit is converted with log2(6) bits; this is favorable
  to the grammar because larger bits/unit increases savings from rule reuse.
- selector_lb is a lower-bound fanout/source-choice cost already frozen in the CSV.
- direct mappings get zero selector cost.
- Eulenspiegel order freedom is reported in three scenarios:
  0 bits; log2(7!); log2(10!).
"""

import csv, math, argparse
from collections import defaultdict

def load(path):
    rows=[]
    with open(path,encoding="utf-8",newline="") as f:
        for r in csv.DictReader(f):
            for k in ["role_swap","event_sub","order_break","metaphor","source_jump","new_rule"]:
                r[k]=int(r[k])
            for k in ["fanout_bits_lb","source_selector_bits_lb","selector_lb"]:
                r[k]=float(r[k])
            rows.append(r)
    return rows

def run(rows):
    op_bits=math.log2(6)
    transformed=[r for r in rows if r["rule"]!="DIRECT"]
    base_ops=sum(r["role_swap"]+r["event_sub"]+r["order_break"]+r["metaphor"]+r["source_jump"] for r in rows)
    selector=sum(r["selector_lb"] for r in rows)
    families=sorted(set(r["family"] for r in transformed))
    frozen_families=[f for f in families if f.startswith("R")]
    new_families=[f for f in families if f.startswith("N")]

    # Frozen scoring convention: an independent exact transformation receives
    # the 1.5 "new rule" charge. This is deliberately a cheap baseline.
    baseline_units=base_ops+1.5*len(transformed)
    baseline_bits=baseline_units*op_bits

    full_dict_units=base_ops+1.5*len(families)
    f0_sunk_units=base_ops+1.5*len(new_families)

    orders=[
        ("no_order_penalty",0.0),
        ("seven_ordered_items",math.log2(math.factorial(7))),
        ("ten_ordered_items",math.log2(math.factorial(10))),
    ]

    print(f"claims={len(rows)} transformed={len(transformed)} direct={len(rows)-len(transformed)}")
    print(f"base_structural_operations={base_ops}")
    print(f"families_total={len(families)} frozen_R={len(frozen_families)} new_N={len(new_families)}")
    print(f"selector_lower_bound_bits={selector:.6f}")
    print(f"operation_unit_bits=log2(6)={op_bits:.6f}")
    print(f"independent_baseline_bits={baseline_bits:.6f}")
    print()
    for name,order_bits in orders:
        full=full_dict_units*op_bits+selector+order_bits
        sunk=f0_sunk_units*op_bits+selector+order_bits
        print(name)
        print(f"  order_bits={order_bits:.6f}")
        print(f"  full_dictionary_bits={full:.6f} delta_vs_baseline={full-baseline_bits:+.6f} pct={(full/baseline_bits-1)*100:+.3f}%")
        print(f"  F0_sunk_bits={sunk:.6f} delta_vs_baseline={sunk-baseline_bits:+.6f} pct={(sunk/baseline_bits-1)*100:+.3f}%")

    # Prequential test: train on Hamlet+Faust, evaluate Eulenspiegel+Don Juan.
    hold=[r for r in rows if r["corpus"] in ("Eulenspiegel","Don Juan")]
    hold_trans=[r for r in hold if r["rule"]!="DIRECT"]
    hold_base=sum(r["role_swap"]+r["event_sub"]+r["order_break"]+r["metaphor"]+r["source_jump"] for r in hold)
    hold_sel=sum(r["selector_lb"] for r in hold)
    train_fams=set(r["family"] for r in rows if r["corpus"] in ("Hamlet","Faust") and r["rule"]!="DIRECT")
    hold_fams=set(r["family"] for r in hold_trans)
    hold_new=hold_fams-train_fams
    hold_baseline=(hold_base+1.5*len(hold_trans))*op_bits
    hold_grammar_no=(hold_base+1.5*len(hold_new))*op_bits+hold_sel

    print()
    print("prequential_Hamlet_Faust_to_Eulenspiegel_DonJuan")
    print(f"  holdout_claims={len(hold)} transformed={len(hold_trans)} new_families={len(hold_new)}")
    print(f"  baseline_bits={hold_baseline:.6f}")
    for name,order_bits in orders:
        val=hold_grammar_no+order_bits
        print(f"  {name}: grammar_bits={val:.6f} delta={val-hold_baseline:+.6f} pct={(val/hold_baseline-1)*100:+.3f}%")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("csv_file")
    args=ap.parse_args()
    run(load(args.csv_file))

if __name__=="__main__":
    main()

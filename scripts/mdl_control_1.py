#!/usr/bin/env python3
import csv, math, argparse
from collections import defaultdict

OP_BITS=math.log2(6)

def read_rows(path):
    out=[]
    with open(path,encoding="utf-8",newline="") as f:
        for r in csv.DictReader(f):
            for k in ["role_swap","event_sub","order_break","metaphor","source_jump"]:
                r[k]=int(r[k])
            r["selector_bits"]=float(r["selector_bits"])
            r["transformed"]=r["family"]!="DIRECT"
            out.append(r)
    return out

def base_ops(rows):
    return sum(sum(r[k] for k in ["role_swap","event_sub","order_break","metaphor","source_jump"]) for r in rows)

def independent_baseline(rows):
    return (base_ops(rows)+1.5*sum(r["transformed"] for r in rows))*OP_BITS

def frozen_grammar(rows, new_family_count=0, order_bits=0):
    return (base_ops(rows)+1.5*new_family_count)*OP_BITS + sum(r["selector_bits"] for r in rows) + order_bits

def pct(a,b):
    return (a/b-1)*100

def summarize(label, rows, new_family_count=0, order_scenarios=(("none",0.0),)):
    base=independent_baseline(rows)
    print(label)
    print(f"  claims={len(rows)} direct={sum(not r['transformed'] for r in rows)} transformed={sum(r['transformed'] for r in rows)}")
    print(f"  direct_rate={sum(not r['transformed'] for r in rows)/len(rows):.6f}")
    print(f"  base_ops={base_ops(rows)} selector_bits={sum(r['selector_bits'] for r in rows):.6f}")
    print(f"  independent_baseline_bits={base:.6f}")
    for name,ob in order_scenarios:
        g=frozen_grammar(rows,new_family_count,ob)
        print(f"  {name}: grammar_bits={g:.6f} delta={g-base:+.6f} pct={pct(g,base):+.3f}%")
    print()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("control_csv")
    ap.add_argument("positive_csv")
    args=ap.parse_args()

    controls=read_rows(args.control_csv)
    negatives=[r for r in controls if r["group"]=="internal_negative"]
    christian=[r for r in controls if r["group"]=="christian_control"]

    # Internal negatives: both texts are searched adversarially across their plots.
    order2=[
      ("no_order",0.0),
      ("log2_7_fact_per_text",2*math.log2(math.factorial(7))),
      ("log2_10_fact_per_text",2*math.log2(math.factorial(10))),
    ]
    summarize("internal_negative_controls",negatives,0,order2)

    # Christian controls: direct-match density is the main diagnostic.
    summarize("christian_controls",christian,0,[
      ("no_order",0.0),
      ("log2_7_fact_per_text",2*math.log2(math.factorial(7))),
      ("log2_10_fact_per_text",2*math.log2(math.factorial(10))),
    ])

    # Positive prequential comparator: Hamlet+Faust train; Eulenspiegel+Don Juan holdout.
    pos=read_rows(args.positive_csv)
    train=[r for r in pos if r["corpus"] in ("Hamlet","Faust")]
    hold=[r for r in pos if r["corpus"] in ("Eulenspiegel","Don Juan")]
    train_fams={r["family"] for r in train if r["transformed"]}
    hold_fams={r["family"] for r in hold if r["transformed"]}
    new=len(hold_fams-train_fams)
    summarize("NH_positive_later_holdout",hold,new,[
      ("no_order",0.0),
      ("Eulenspiegel_log2_7_fact",math.log2(math.factorial(7))),
      ("Eulenspiegel_log2_10_fact",math.log2(math.factorial(10))),
    ])

if __name__=="__main__":
    main()

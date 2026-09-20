#!/usr/bin/env python3
import argparse, csv, itertools, statistics

DIMENSIONS = ["R","O","P","C","N","L","S"]

def load(path):
    rows=[]
    with open(path, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            for k in DIMENSIONS + ["D","A"]:
                r[k]=int(r[k])
            calc=sum(r[k] for k in DIMENSIONS)
            if calc != r["D"]:
                raise ValueError(f"{r['case']}: D={r['D']} but dimensions sum to {calc}")
            rows.append(r)
    return rows

def cls(d):
    if d >= 10: return "strong"
    if d >= 7: return "ambiguous"
    return "weak"

def exact_perm(pos, ctl):
    vals=pos+ctl
    n=len(pos)
    obs=statistics.mean(ctl)-statistics.mean(pos)
    count=total=0
    for idx in itertools.combinations(range(len(vals)), n):
        s=set(idx)
        a=[v for i,v in enumerate(vals) if i in s]
        b=[v for i,v in enumerate(vals) if i not in s]
        # group b minus group a; label orientation is exchangeable
        diff=statistics.mean(b)-statistics.mean(a)
        total += 1
        if diff >= obs - 1e-12:
            count += 1
    return obs, count/total, total

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("csv_file")
    args=ap.parse_args()
    rows=load(args.csv_file)

    for r in rows:
        print(f"{r['case']}: class={r['class']} D={r['D']}/14 structural={cls(r['D'])} A={r['A']}")

    pos=[r["D"] for r in rows if r["class"]=="NH_positive"]
    ctl=[r["D"] for r in rows if r["class"]!="NH_positive"]
    print()
    print(f"NH_positive n={len(pos)} mean={statistics.mean(pos):.6f} strong={sum(d>=10 for d in pos)}")
    print(f"controls n={len(ctl)} mean={statistics.mean(ctl):.6f} strong={sum(d>=10 for d in ctl)}")
    obs,p,nperm=exact_perm(pos,ctl)
    print(f"controls_minus_positive_mean={obs:.6f}")
    print(f"exact_one_sided_permutation_p={p:.6f} permutations={nperm}")
    print("NOTE: descriptive only; n=3+3 and holdout set is purposive, not a random population sample.")

if __name__=="__main__":
    main()

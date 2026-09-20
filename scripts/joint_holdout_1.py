#!/usr/bin/env python3
import argparse, csv, statistics, itertools

SEM=["baptism","temptation","disciples","healings","cana","judas","last_supper","passion","resurrection"]
STR=["R","O","P","C","N","L","S"]

def load(path):
    rows=[]
    with open(path,encoding="utf-8",newline="") as f:
        for r in csv.DictReader(f):
            for k in SEM+STR+["G","K","D","A"]:
                r[k]=int(r[k])
            g=sum(r[k] for k in SEM)
            k=sum(r[x]>=2 for x in SEM)
            d=sum(r[x] for x in STR)
            if (g,k,d)!=(r["G"],r["K"],r["D"]):
                raise ValueError(f"{r['case']}: stored={(r['G'],r['K'],r['D'])} calculated={(g,k,d)}")
            joint=(g>=9 and k>=3 and d>=10)
            stored=r["joint_pass"].lower()=="true"
            if joint != stored:
                raise ValueError(f"{r['case']}: joint mismatch")
            r["joint"]=joint
            rows.append(r)
    return rows

def exact_perm(pos,ctl):
    vals=pos+ctl
    n=len(pos)
    obs=statistics.mean(ctl)-statistics.mean(pos)
    ge=tot=0
    for idx in itertools.combinations(range(len(vals)), n):
        s=set(idx)
        a=[v for i,v in enumerate(vals) if i in s]
        b=[v for i,v in enumerate(vals) if i not in s]
        d=statistics.mean(b)-statistics.mean(a)
        tot+=1
        ge+=d>=obs-1e-12
    return obs,ge/tot,tot

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("csv_file")
    args=ap.parse_args()
    rows=load(args.csv_file)
    for r in rows:
        sem=(r["G"]>=9 and r["K"]>=3)
        st=r["D"]>=10
        print(f"{r['case']}: class={r['class']} G={r['G']}/27 K={r['K']} D={r['D']}/14 semantic={sem} structural={st} joint={r['joint']} A={r['A']}")
    pos=[r for r in rows if r["class"]=="NH_positive"]
    ctl=[r for r in rows if r["class"]!="NH_positive"]
    print()
    print(f"NH_positive: n={len(pos)} mean_G={statistics.mean(r['G'] for r in pos):.6f} mean_D={statistics.mean(r['D'] for r in pos):.6f} joint={sum(r['joint'] for r in pos)}")
    print(f"controls: n={len(ctl)} mean_G={statistics.mean(r['G'] for r in ctl):.6f} mean_D={statistics.mean(r['D'] for r in ctl):.6f} joint={sum(r['joint'] for r in ctl)}")
    obs,p,n=exact_perm([r["G"] for r in pos],[r["G"] for r in ctl])
    print(f"G controls_minus_positive_mean={obs:.6f} exact_one_sided_p={p:.6f} permutations={n}")
    obs,p,n=exact_perm([r["D"] for r in pos],[r["D"] for r in ctl])
    print(f"D controls_minus_positive_mean={obs:.6f} exact_one_sided_p={p:.6f} permutations={n}")
    print("NOTE: descriptive only; purposive n=3+3 holdout.")

if __name__=="__main__":
    main()

#!/usr/bin/env python3
import argparse,json
C={"role_swap":1.0,"event_substitution":1.0,"order_break":1.0,"metaphoric_jump":1.0,"source_jump":1.0,"new_ad_hoc_rule":1.5}
def weight(p):
 w=1.0
 for k in ["importance","specificity","prediction","causality","role","order","independence"]: w*=float(p.get(k,1.0))
 return w
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("json_file"); ap.add_argument("--lambda-cost",type=float,default=1.0); a=ap.parse_args(); data=json.load(open(a.json_file,encoding="utf-8")); total=0
 for p in data:
  base=weight(p)*float(p.get("match",1.0)); cost=sum(C.get(k,1.0)*float(v) for k,v in p.get("transformations",{}).items()); s=base-a.lambda_cost*cost; total+=s; print(f"{p.get('id','?')}: score={s:.4f} base={base:.4f} cost={cost:.4f}")
 print(f"TOTAL={total:.4f}")
if __name__=="__main__": main()

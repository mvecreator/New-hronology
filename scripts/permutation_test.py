#!/usr/bin/env python3
import argparse,csv,itertools
def mean(x): return sum(x)/len(x)
def test(a,b):
 v=a+b; n=len(a); obs=mean(a)-mean(b); ge=tot=0
 for idx in itertools.combinations(range(len(v)),n):
  s=set(idx); aa=[x for i,x in enumerate(v) if i in s]; bb=[x for i,x in enumerate(v) if i not in s]; d=mean(aa)-mean(bb); tot+=1; ge+=d>=obs-1e-12
 return obs,ge/tot,tot
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('csv_file'); ap.add_argument('--group-a',required=True); ap.add_argument('--group-b',required=True); ap.add_argument('--group-col',default='class'); ap.add_argument('--value-col',default='score_27'); a=ap.parse_args(); rows=list(csv.DictReader(open(a.csv_file,encoding='utf-8'))); x=[float(r[a.value_col]) for r in rows if r[a.group_col]==a.group_a]; y=[float(r[a.value_col]) for r in rows if r[a.group_col]==a.group_b]; obs,p,n=test(x,y); print(f'nA={len(x)} nB={len(y)} observed_mean_diff={obs:.6f}'); print(f'exact_one_sided_p={p:.6f} permutations={n}')
if __name__=='__main__': main()

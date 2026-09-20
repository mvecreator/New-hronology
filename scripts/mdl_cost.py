#!/usr/bin/env python3
import argparse
C={"role":1.0,"event":1.0,"order":1.0,"metaphor":1.0,"source":1.0,"newrule":1.5}
def main():
 ap=argparse.ArgumentParser(); [ap.add_argument('--'+k,type=float,default=0.0) for k in C]; a=vars(ap.parse_args()); parts={k:a[k]*C[k] for k in C}; [print(f'{k}: {v:.3f}') for k,v in parts.items()]; print(f'MDL_TRANSFORMATION_COST={sum(parts.values()):.3f}')
if __name__=='__main__': main()

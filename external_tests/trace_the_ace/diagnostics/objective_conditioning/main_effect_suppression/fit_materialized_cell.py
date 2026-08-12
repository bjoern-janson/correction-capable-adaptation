#!/usr/bin/env python3
from __future__ import annotations
import argparse,importlib.util,json,os,sys,time
from pathlib import Path
import numpy as np,yaml
from scipy import sparse

def loadmod(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def sigmoid(x):
 x=np.asarray(x,float);o=np.empty_like(x);p=x>=0;o[p]=1/(1+np.exp(-x[p]));e=np.exp(x[~p]);o[~p]=e/(1+e);return o
def main():
 p=argparse.ArgumentParser();p.add_argument('--arm',required=True);p.add_argument('--outer-fold',type=int,required=True);p.add_argument('--config',type=Path,required=True);p.add_argument('--matrix-dir',type=Path,required=True);p.add_argument('--parent-runner',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();cfg=yaml.safe_load(a.config.read_text());parent=loadmod('parent',a.parent_runner);prefix=f'{a.arm}_fold{a.outer_fold}';X=sparse.load_npz(a.matrix_dir/f'{prefix}_X.npz').tocsr();V=sparse.load_npz(a.matrix_dir/f'{prefix}_V.npz').tocsr();z=np.load(a.matrix_dir/f'{prefix}_meta.npz');y=z['y_train'];row=z['row_index'];m=parent.make_classifier(cfg['base_classifier']);t=time.perf_counter();m.fit(X,y);fit_s=time.perf_counter()-t;score=np.asarray(m.decision_function(V),float);prob=sigmoid(score);ni=int(np.asarray(m.n_iter_).max());a.output.parent.mkdir(parents=True,exist_ok=True);np.savez_compressed(a.output,row_index=row.astype(np.int32),probability=prob.astype(np.float64),n_iter=np.asarray([ni],np.int32));print(json.dumps({'arm':a.arm,'fold':a.outer_fold,'fit_seconds':fit_s,'n_iter':ni,'rows':len(row),'output':str(a.output)}),flush=True);sys.stdout.flush();sys.stderr.flush();os._exit(0)
if __name__=='__main__':main()

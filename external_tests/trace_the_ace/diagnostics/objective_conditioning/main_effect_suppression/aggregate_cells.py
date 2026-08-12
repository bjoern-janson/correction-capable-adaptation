#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
import numpy as np,pandas as pd,yaml
from sklearn.metrics import log_loss,roc_auc_score

def sha(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def loss(y,p):
 p=np.clip(np.asarray(p,float),1e-15,1-1e-15);y=np.asarray(y,float);return -(y*np.log(p)+(1-y)*np.log(1-p))
def boot(g,d,reps,seed):
 a=pd.DataFrame({'s':g,'d':d}).groupby('s',sort=True).d.agg(['sum','count']);su=a['sum'].to_numpy(float);co=a['count'].to_numpy(float);n=len(a);r=np.random.default_rng(seed);o=np.empty(reps);x=0
 while x<reps:
  k=min(100,reps-x);z=r.integers(0,n,size=(k,n));o[x:x+k]=su[z].sum(1)/co[z].sum(1);x+=k
 q=np.quantile(o,[.025,.975]);return {'point':float(np.mean(d)),'ci95_lower':float(q[0]),'ci95_upper':float(q[1]),'clusters':int(n),'replicates':int(reps),'seed':int(seed)}
def main():
 p=argparse.ArgumentParser();p.add_argument('--config',type=Path,required=True);p.add_argument('--index',type=Path,required=True);p.add_argument('--folds',type=Path,required=True);p.add_argument('--eligible-objectives',type=Path,required=True);p.add_argument('--cell-dir',type=Path,required=True);p.add_argument('--output-dir',type=Path,required=True);a=p.parse_args();cfg=yaml.safe_load(a.config.read_text());idx=pd.read_csv(a.index,usecols=['response_id','session_id','learning_objective_id','is_correct']);fd=pd.read_csv(a.folds);df=idx.merge(fd,on='session_id',validate='many_to_one');elig=set(a.eligible_objectives.read_text().splitlines());df=df[df.learning_objective_id.astype(str).isin(elig)].reset_index(drop=True);y=df.is_correct.to_numpy(np.int8);g=df.session_id.astype(str).to_numpy();arms=['B0','C0','B1','C1'];pred={k:np.full(len(df),np.nan) for k in arms};iters={k:[] for k in arms}
 for f in range(5):
  expected=set(np.flatnonzero(df.fold.to_numpy(int)==f))
  for k in arms:
   z=np.load(a.cell_dir/f'{k}_fold{f}.npz');ix=set(map(int,z['row_index']));assert ix==expected;ii=z['row_index'].astype(int);pred[k][ii]=z['probability'];iters[k].append(int(z['n_iter'][0]))
 if any(not np.isfinite(pred[k]).all() for k in arms):raise AssertionError('coverage')
 L={k:loss(y,pred[k]) for k in arms};d0=L['C0']-L['B0'];d1=L['C1']-L['B1'];psi=d0-d1;u=cfg['uncertainty'];a0=boot(g,d0,int(u['replicates']),int(u['seed_delta_no_main']));a1=boot(g,d1,int(u['replicates']),int(u['seed_delta_with_main']));ap=boot(g,psi,int(u['replicates']),int(u['seed_suppression_difference']));support=a0['point']<0 and a0['ci95_upper']<0 and ap['point']<0 and ap['ci95_upper']<0;against=a0['ci95_lower']>=0 and ap['ci95_lower']>=0;status='SUPPORT' if support else ('WEIGH_AGAINST' if against else 'UNRESOLVED');m={k:{'log_loss':float(log_loss(y,pred[k])),'auc':float(roc_auc_score(y,pred[k]))} for k in arms};rec={'schema_version':1,'experiment_id':'M2_D_MAIN','implementation':{'all_base_models_converged':all(n<int(cfg['base_classifier']['max_iter']) for v in iters.values() for n in v),'fit_count':20,'max_n_iter':max(max(v) for v in iters.values()),'iters':iters},'metrics':m,'delta_no_main':a0,'delta_with_main':a1,'suppression_difference':ap,'D_main_local_diagnostic':status,'authority':{'broad_H_O':'OPEN','new_conditioning_operator_authorized':False,'CCA_derived_feature_authority':False}};out=a.output_dir;out.mkdir(parents=True,exist_ok=True);od=df[['response_id','session_id','learning_objective_id','is_correct']].copy()
 for k in arms:od[f'{k.lower()}_raw_probability']=pred[k]
 op=out/'oof_predictions.csv';od.to_csv(op,index=False,lineterminator='\n');rec['artifacts']={'oof_sha256':sha(op)};rp=out/'m2_d_main_record.json';rp.write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n');print(json.dumps(rec,indent=2,sort_keys=True))
if __name__=='__main__':main()

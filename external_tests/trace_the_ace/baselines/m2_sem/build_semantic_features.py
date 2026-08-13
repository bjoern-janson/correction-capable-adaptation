#!/usr/bin/env python3
"""Build frozen M2-SEM semantic features without reading outcome labels.

Produces session-level Z_S and response-level R_TO from the constituted GloVe resource.
This script does not fit any predictive model or inspect any outcome-bearing score.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, re, time
from pathlib import Path
import numpy as np
import pandas as pd
import yaml


def sha256_file(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024), b''): h.update(b)
    return h.hexdigest()


def transcript_path_map(roots: list[Path]) -> dict[str,Path]:
    out={}
    for root in roots:
        for p in root.rglob('*.csv'):
            if p.stem in out: raise AssertionError(f'duplicate transcript {p.stem}')
            out[p.stem]=p
    return out


def l2norm(v: np.ndarray) -> np.ndarray:
    n=float(np.linalg.norm(v))
    return v/n if n>0 else np.zeros_like(v)


def mean_embedding(text: str, token_re, vectors: dict[str,np.ndarray], dim:int) -> np.ndarray:
    toks=token_re.findall((text or '').lower())
    arr=[vectors[t] for t in toks if t in vectors]
    if not arr: return np.zeros(dim,dtype=np.float32)
    return l2norm(np.mean(np.stack(arr,axis=0),axis=0,dtype=np.float64).astype(np.float32))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--index',required=True,type=Path)
    ap.add_argument('--transcripts-root',action='append',required=True,type=Path)
    ap.add_argument('--vector-file',required=True,type=Path)
    ap.add_argument('--config',required=True,type=Path)
    ap.add_argument('--output-dir',required=True,type=Path)
    a=ap.parse_args()
    cfg=yaml.safe_load(a.config.read_text())
    assert cfg['experiment_id']=='M2_SEM'
    res=cfg['external_semantic_resource']; dim=int(res['vector_dimension'])
    assert a.vector_file.name==res['extracted_member_name_required']
    assert a.vector_file.stat().st_size==int(res['extracted_vector_byte_size'])
    assert sha256_file(a.vector_file)==res['extracted_vector_sha256_required']

    # Deliberately exclude outcome labels from semantic feature construction.
    idx=pd.read_csv(a.index,usecols=['response_id','session_id','learning_objective_id','learning_objective'])
    assert idx['response_id'].is_unique
    sessions=sorted(idx['session_id'].astype(str).unique())
    paths=transcript_path_map(a.transcripts_root)
    if set(paths)!=set(sessions): raise AssertionError('transcript coverage mismatch')
    token_re=re.compile(cfg['semantic_tokenization']['token_pattern'],flags=re.UNICODE)

    t0=time.time(); needed=set()
    for text in idx['learning_objective'].astype(str).unique(): needed.update(token_re.findall(text.lower()))
    for sid in sessions:
        with paths[sid].open('r',encoding='utf-8-sig',newline='') as f:
            r=csv.DictReader(f)
            if r.fieldnames!=['session_id','utterance_id','role','content','timestamp']: raise AssertionError(f'schema {sid}')
            for row in r: needed.update(token_re.findall((row['content'] or '').lower()))
    needed_count=len(needed)

    vectors={}; rows=0
    with a.vector_file.open('r',encoding='utf-8',errors='strict') as f:
        for line in f:
            if not line.strip(): continue
            rows+=1
            word, sep, tail=line.rstrip('\n').partition(' ')
            if word not in needed: continue
            vals=np.fromstring(tail,sep=' ',dtype=np.float32)
            if vals.size!=dim or not np.isfinite(vals).all(): raise AssertionError(f'bad vector for {word}')
            vectors[word]=vals
    if rows!=int(res['vocabulary_rows_validated']): raise AssertionError(f'vector row count mismatch {rows}')
    coverage=len(vectors)

    # Objective embeddings once per objective id.
    objectives=(idx[['learning_objective_id','learning_objective']]
                .drop_duplicates('learning_objective_id').sort_values('learning_objective_id').reset_index(drop=True))
    obj_emb={}
    for row in objectives.itertuples(index=False):
        e=mean_embedding(str(row.learning_objective),token_re,vectors,dim)
        if not np.any(e): raise AssertionError(f'zero objective embedding {row.learning_objective_id}')
        obj_emb[str(row.learning_objective_id)]=e

    # Compute per-session Z_S and per (session, objective) R_TO.
    beta=float(cfg['semantic_conditioning']['beta'])
    session_zs={}; pair_resid={}; nonzero_utterances={}
    obj_by_session=idx.groupby('session_id',sort=False)['learning_objective_id'].apply(lambda s: sorted(set(map(str,s))))
    for n,sid in enumerate(sessions,1):
        q=[]
        with paths[sid].open('r',encoding='utf-8-sig',newline='') as f:
            r=csv.DictReader(f)
            for row in r:
                e=mean_embedding(row['content'] or '',token_re,vectors,dim)
                if np.any(e): q.append(e)
        if not q: raise AssertionError(f'no semantic utterances {sid}')
        Q=np.stack(q).astype(np.float32,copy=False)
        zs=Q.mean(axis=0,dtype=np.float64).astype(np.float32)
        session_zs[sid]=zs; nonzero_utterances[sid]=len(q)
        for oid in obj_by_session.loc[sid]:
            qo=obj_emb[oid]
            logits=beta*(Q@qo)
            logits=logits-float(logits.max())
            w=np.exp(logits,dtype=np.float64); w=w/w.sum()
            zc=(w[:,None]*Q).sum(axis=0,dtype=np.float64).astype(np.float32)
            pair_resid[(sid,oid)]=zc-zs
        if n%2000==0: print(json.dumps({'sessions_done':n,'elapsed_seconds':time.time()-t0}),flush=True)

    # Frozen validity checks.
    multi=idx.groupby('session_id')['learning_objective_id'].nunique()
    varying=False
    for sid in multi[multi>1].index.astype(str):
        rs=[pair_resid[(sid,oid)] for oid in obj_by_session.loc[sid]]
        if any(not np.array_equal(rs[0],x) for x in rs[1:]): varying=True; break
    residual_nonzero=any(np.any(v) for v in pair_resid.values())
    if not varying or not residual_nonzero: raise AssertionError('semantic residual validity failed')

    sess_df=pd.DataFrame({'session_id':sessions})
    Z=np.stack([session_zs[s] for s in sessions])
    for j in range(dim): sess_df[f'z_s_{j:02d}']=Z[:,j]
    sess_df['nonzero_semantic_utterances']=[nonzero_utterances[s] for s in sessions]

    resp=idx[['response_id','session_id','learning_objective_id']].copy()
    R=np.stack([pair_resid[(str(s),str(o))] for s,o in zip(resp.session_id,resp.learning_objective_id)])
    for j in range(dim): resp[f'r_to_{j:02d}']=R[:,j]
    a.output_dir.mkdir(parents=True,exist_ok=True)
    sess_path=a.output_dir/'session_semantic_features.csv'; resp_path=a.output_dir/'response_conditioning_features.csv'
    sess_df.to_csv(sess_path,index=False,lineterminator='\n'); resp.to_csv(resp_path,index=False,lineterminator='\n')
    rec={
      'experiment_id':'M2_SEM','stage':'SEMANTIC_FEATURES_BUILT_NO_OUTCOMES','result_observed':False,
      'sessions':len(sessions),'responses':len(idx),'objectives':len(obj_emb),'dimension':dim,
      'needed_token_types':needed_count,'matched_glove_token_types':coverage,
      'all_objective_embeddings_nonzero':True,'every_session_has_nonzero_utterance_embedding':True,
      'Z_S_objective_independent_by_construction':True,'R_TO_nonzero':bool(residual_nonzero),'R_TO_multiobjective_variation':bool(varying),
      'vector_sha256':sha256_file(a.vector_file),'session_features_sha256':sha256_file(sess_path),'response_features_sha256':sha256_file(resp_path),
      'elapsed_seconds':time.time()-t0,
    }
    (a.output_dir/'semantic_feature_record.json').write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
    print(json.dumps(rec,indent=2,sort_keys=True))
if __name__=='__main__': main()

import multiprocessing as mp
import numpy as np
from scipy.special import ndtr
import math
import run_calibration_information_scaling as base

_T = _CODES = _ORDER = _STARTS = _SIGNS = None

def _worker(task):
    si, ri, c, path = task
    s = _SIGNS[si]
    mm = np.memmap(path, mode='r+', dtype=np.float64, shape=(16*base.S0, base.N_REP))
    block = mm[c*base.S0:(c+1)*base.S0, :]
    for rep in range(base.N_REP):
        rng = base.rng_for(1831, si, ri, rep, c)
        Z = rng.normal(size=base.S0)
        eps = rng.normal(size=base.N0)
        L = math.sqrt(base.RHO)*Z[_CODES] + math.sqrt(1-base.RHO)*eps
        Y = ndtr(L) <= _T
        q = s*(_T-Y)
        block[:, rep] = np.add.reduceat(q[_ORDER], _STARTS)
    mm.flush(); del mm
    return si, ri, c

def parallel_generate(T, codes, order, starts):
    global _T, _CODES, _ORDER, _STARTS, _SIGNS
    _T, _CODES, _ORDER, _STARTS = T, codes, order, starts
    _SIGNS = [base.scale_sign(T, h) for _, h, _ in base.SENTINELS]
    paths, tasks = {}, []
    for si, (label, h, _) in enumerate(base.SENTINELS):
        for ri, Rtrue in enumerate(base.RATIOS):
            path = base.WORKDIR/f'noise_{label}_r{ri}.dat'
            mm = np.memmap(path, mode='w+', dtype=np.float64, shape=(16*base.S0, base.N_REP))
            mm.flush(); del mm
            paths[(si, ri)] = path
            for c in range(16):
                tasks.append((si, ri, c, str(path)))
    with mp.get_context('fork').Pool(processes=5) as pool:
        for si, ri, c in pool.imap_unordered(_worker, tasks):
            print(f'NOISE sentinel={base.SENTINELS[si][0]} R={base.RATIOS[ri]:g} cohort={c+1}/16', flush=True)
    return paths

if __name__ == '__main__':
    base.generate_nested_session_noise = parallel_generate
    base.run()

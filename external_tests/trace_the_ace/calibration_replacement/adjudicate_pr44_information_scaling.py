import hashlib
import json
from pathlib import Path

SOURCE = Path('/mnt/data/calibration_information_scaling_run/results/final_partitioned.json')
OUT = Path('/mnt/data/pr44_successor_adjudication')
OUT.mkdir(parents=True, exist_ok=True)

SOURCE_SHA256 = '788109fbec94649a9f7aa94d77a09c8b8141ef7b440fbb0e79e98838ff8807c7'
PR44_HEAD = '8626826364fb31318750ba8c9f70866e524cb577'
PR45_HEAD = '9ba62109641a33dc45103a3dec947a07cabfb79c'
MULTIPLIERS = [1, 2, 4, 8, 16]
SENTINELS = ['coarse', 'fine']
R_KEYS = ['R_0', 'R_0.125', 'R_0.25', 'R_0.5']

# Authorized successor semantics from PR #45:
# - R=0 is analytically STRUCTURALLY_DEGENERATE under the PR #44 oracle runner.
#   PR #44 computes rb=zeros_like(cb) whenever delta==0, so every valid interval
#   endpoint is exactly 0 before any empirical result is considered.
# - For that cell, coverage must equal 1.00 and inherited NI / denominator /
#   invalid-bootstrap gates must all pass.
# - All nonzero-R cells are STOCHASTIC: coverage >= 0.90, with no upper cap,
#   and the inherited NI / denominator / invalid-bootstrap gates remain conjunctive.
# No outcomes, bootstrap draws, synthetic arrays, margins, or thresholds are regenerated.


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def successor_cell(cell, r_true):
    if r_true == 0.0:
        classification = 'STRUCTURALLY_DEGENERATE'
        structural_exactness = True  # analytic from the frozen PR #44 operator identity
        g_cov = structural_exactness and abs(float(cell['coverage']) - 1.0) <= 1e-12
    else:
        classification = 'STOCHASTIC'
        structural_exactness = None
        g_cov = float(cell['coverage']) >= 0.90

    g_ni = bool(cell['NI_pass'])
    g_den = bool(cell['denominator_pass'])
    g_inv = bool(cell['invalid_bootstrap_pass'])
    passed = bool(g_cov and g_ni and g_den and g_inv)

    return {
        'classification': classification,
        'structural_exactness_from_operator_identity': structural_exactness,
        'coverage': float(cell['coverage']),
        'NI_pass_rate': float(cell['NI_pass_rate']),
        'denominator_guard_rate': float(cell['denominator_guard_rate']),
        'max_invalid_bootstrap_fraction': float(cell['max_invalid_bootstrap_fraction']),
        'G_cov_successor': bool(g_cov),
        'G_NI_inherited': g_ni,
        'G_denominator_inherited': g_den,
        'G_invalid_bootstrap_inherited': g_inv,
        'pass_successor': passed,
    }


def main():
    got_sha = sha256(SOURCE)
    assert got_sha == SOURCE_SHA256, (got_sha, SOURCE_SHA256)
    src = json.loads(SOURCE.read_text())
    assert src['experiment_id'] == 'GAMMA_CAL_INFORMATION_SCALING'

    result = {
        'experiment_id': 'GAMMA_CAL_INFORMATION_SCALING_PR44_SUCCESSOR_ADJUDICATION',
        'status': 'EXECUTED_NO_REGENERATION',
        'source': {
            'pr44_head': PR44_HEAD,
            'pr44_final_partitioned_sha256': got_sha,
            'pr45_authorized_gate_head': PR45_HEAD,
            'synthetic_outcomes_regenerated': False,
            'bootstrap_regenerated': False,
            'historical_vectors_read': False,
        },
        'multipliers': {},
        'outputs': {},
        'authority': {},
    }

    coarse_vector = []
    fine_vector = []
    joint_vector = []

    for m in MULTIPLIERS:
        src_m = src['curve'][f'm_{m}']
        mrec = {'m': m, 'rows': int(src_m['rows']), 'sessions': int(src_m['sessions']), 'sentinels': {}}
        sentinel_pass = {}
        for sentinel in SENTINELS:
            cells = {}
            for rkey in R_KEYS:
                r_true = float(rkey.split('_', 1)[1])
                cell = src_m['sentinels'][sentinel]['cells'][rkey]
                cells[rkey] = successor_cell(cell, r_true)
            spass = all(c['pass_successor'] for c in cells.values())
            mrec['sentinels'][sentinel] = {'cells': cells, 'pass_successor': spass}
            sentinel_pass[sentinel] = spass

        joint = bool(sentinel_pass['coarse'] and sentinel_pass['fine'])
        mrec['joint_pass_successor'] = joint
        result['multipliers'][f'm_{m}'] = mrec
        coarse_vector.append(bool(sentinel_pass['coarse']))
        fine_vector.append(bool(sentinel_pass['fine']))
        joint_vector.append(joint)

    def first_passing(vector):
        for m, passed in zip(MULTIPLIERS, vector):
            if passed:
                return m
        return None

    m_coarse = first_passing(coarse_vector)
    m_fine = first_passing(fine_vector)
    m_joint = first_passing(joint_vector)
    n_joint = None if m_joint is None else 35072 * m_joint
    sessions_joint = None if m_joint is None else 22821 * m_joint

    result['outputs'] = {
        'coarse_pass_vector_successor': coarse_vector,
        'fine_pass_vector_successor': fine_vector,
        'joint_pass_vector_successor': joint_vector,
        'm_min_decision_coarse': m_coarse if m_coarse is not None else 'NONE_IDENTIFIED_WITHIN_GRID',
        'm_min_decision_fine': m_fine if m_fine is not None else 'NONE_IDENTIFIED_WITHIN_GRID',
        'm_min_decision_joint': m_joint if m_joint is not None else 'NONE_IDENTIFIED_WITHIN_GRID',
        'n_min_decision_joint': n_joint if n_joint is not None else 'NONE_IDENTIFIED_WITHIN_GRID',
        'sessions_min_decision_joint': sessions_joint if sessions_joint is not None else 'NONE_IDENTIFIED_WITHIN_GRID',
    }

    supported = m_joint is not None and m_joint > 1
    result['authority'] = {
        'D_additional_evidence': 'SUPPORTED_AS_INFORMATION_QUANTITY' if supported else 'NOT_IDENTIFIED_WITHIN_GRID',
        'scope': 'LOCAL_SYNTHETIC_ORACLE_INFORMATION_QUANTITY_ONLY',
        'historical_availability_established': False,
        'replacement_measurement': False,
        'Gamma_cal_replacement': False,
        'historical_calibration_closure': False,
        'M_mature': False,
        'Z_E': False,
        'Z_D': False,
        'Z_C': False,
        'Z_P': False,
    }

    out = OUT / 'final.json'
    out.write_text(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result['outputs'], indent=2, sort_keys=True))
    print(json.dumps(result['authority'], indent=2, sort_keys=True))
    print('final_sha256', sha256(out))
    return result


if __name__ == '__main__':
    main()

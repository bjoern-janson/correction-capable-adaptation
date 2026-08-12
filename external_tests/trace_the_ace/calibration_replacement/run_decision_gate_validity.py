import json, math
from pathlib import Path
import yaml

SPEC = Path(__file__).with_name('DECISION_GATE_VALIDITY_SPEC.yaml')
OUT = Path('/mnt/data/decision_gate_validity_run')
OUT.mkdir(parents=True, exist_ok=True)
TOL = 1e-12


def ni_gate(r_true, ni_pass_rate):
    if r_true in (0.0, 0.125):
        return ni_pass_rate >= 0.80
    if r_true in (0.25, 0.50):
        return ni_pass_rate <= 0.10
    raise ValueError(f'unsupported R_true={r_true}')


def evaluate_gate(fx):
    cls = fx['classification']
    r_true = float(fx['R_true'])
    coverage = float(fx['coverage'])
    ni = float(fx['NI_pass_rate'])
    g_ni = ni_gate(r_true, ni)
    g_den = bool(fx['denominator_pass'])
    g_inv = bool(fx['invalid_bootstrap_pass'])

    if cls == 'STRUCTURALLY_DEGENERATE':
        lo = float(fx['interval_lower'])
        hi = float(fx['interval_upper'])
        g_cov = (
            abs(lo - r_true) <= TOL and
            abs(hi - r_true) <= TOL and
            abs(coverage - 1.0) <= TOL
        )
        mcse = None
    elif cls == 'STOCHASTIC':
        g_cov = coverage >= 0.90
        n = int(fx['n_sim'])
        mcse = math.sqrt(coverage * (1.0 - coverage) / n)
    else:
        raise ValueError(f'unknown classification={cls}')

    gate_pass = bool(g_cov and g_ni and g_den and g_inv)
    return {
        'classification': cls,
        'R_true': r_true,
        'G_cov': bool(g_cov),
        'G_NI': bool(g_ni),
        'G_denominator': bool(g_den),
        'G_invalid_bootstrap': bool(g_inv),
        'MCSE_coverage': mcse,
        'gate_pass': gate_pass,
    }


def main():
    spec = yaml.safe_load(SPEC.read_text())
    suite = spec['validation_suite']
    ordered = [f'V{i}' for i in range(6)]
    result = {
        'experiment_id': spec['experiment_id'],
        'status': 'EXECUTING',
        'fixtures': {},
        'authority': False,
        'stopped_at': None,
    }

    for name in ordered:
        fx = suite[name]
        got = evaluate_gate(fx)
        expected_gate_pass = (fx['expected'] == 'PASS')
        validation_pass = (got['gate_pass'] == expected_gate_pass)
        got.update({
            'fixture_name': fx['name'],
            'expected': fx['expected'],
            'expected_gate_pass': expected_gate_pass,
            'validation_pass': validation_pass,
        })
        result['fixtures'][name] = got
        print(name, json.dumps(got, sort_keys=True), flush=True)
        if not validation_pass:
            result['status'] = 'STOPPED_VALIDITY_FIXTURE_FAILURE'
            result['stopped_at'] = name
            (OUT/'final.json').write_text(json.dumps(result, indent=2, sort_keys=True))
            return result

    result['status'] = 'PASS_ALL_VALIDITY_FIXTURES'
    result['authority'] = True
    (OUT/'final.json').write_text(json.dumps(result, indent=2, sort_keys=True))
    print('AUTH', True, flush=True)
    return result


if __name__ == '__main__':
    main()

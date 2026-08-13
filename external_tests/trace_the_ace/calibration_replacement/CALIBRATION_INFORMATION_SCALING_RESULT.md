# Calibration information-scaling diagnostic result

## Status

**EXECUTED — RAW CONTRACT VERDICT PRESERVED; SCIENTIFIC AUTHORITY WITHHELD DUE DECISION-GATE VALIDITY FAILURE**

Historical M1-cal/M2-S vectors were not read. No replacement calibration operator was selected.

## Baseline reproducibility

The required `m=1` PR #43 endpoint reproduction gate passed exactly:

```text
2 sentinels x 4 ratio cells
exact substantive mismatches = 0
```

Baseline reproduction artifact SHA-256:

```text
56a028d64f81fe850b62d216cbd33a1317303be8a71669f9dad679d0d61fd72c
```

## Execution apparatus

The first monolithic execution hit runtime plumbing while prospectively seeded synthetic cohort blocks were being materialized, before any scaling decision cell had been computed. A parallel cohort materializer was then introduced without changing any RNG stream, outcome, session aggregation, bootstrap, statistic, threshold, or gate.

Bit-for-bit apparatus equivalence was demonstrated on a complete 16-cohort block:

```text
serial SHA-256   7d4ff4c435a6eb7330fcfcc5b8e0c08e43397190540122ad4d57c3082d96e16f
parallel SHA-256 7d4ff4c435a6eb7330fcfcc5b8e0c08e43397190540122ad4d57c3082d96e16f
```

The final calculation was partitioned by multiplier/cell only to cross the execution wall. Each partition used the same committed functions, stored seeded cohort blocks, exact bootstrap draws, and frozen gates.

## Frozen raw contract verdict

Literal full-gate pass vectors:

```text
m                     1      2      4      8      16
coarse full gate      FAIL   FAIL   FAIL   FAIL   FAIL
fine full gate        FAIL   FAIL   FAIL   FAIL   FAIL
joint full gate       FAIL   FAIL   FAIL   FAIL   FAIL
```

Therefore the raw frozen outputs are:

```text
m_min_decision_coarse = NONE_IDENTIFIED_WITHIN_GRID
m_min_decision_fine   = NONE_IDENTIFIED_WITHIN_GRID
m_min_decision_joint  = NONE_IDENTIFIED_WITHIN_GRID
n_min_decision_joint  = NONE_IDENTIFIED_WITHIN_GRID
raw D_additional_evidence = NOT_IDENTIFIED_WITHIN_GRID
```

**That raw verdict is preserved but does not acquire scientific authority.**

## Decision-gate validity contradiction

The frozen gate required empirical 95% interval coverage in `[0.90, 0.99]` for every ratio cell, including `R=0`.

But under the prospectively frozen paired oracle construction, when `R=0`:

```text
P_C = P_R
C_hat_C = C_hat_R
R_hat_oracle = 0 exactly
bootstrap interval for R_hat = [0,0] on every valid dataset
```

Therefore, as information increases and denominator/interval validity approaches 100%, empirical coverage must approach exactly `1.00`.

Observed:

```text
m=1   R=0 coverage: coarse 0.99, fine 0.97
m=2   R=0 coverage: coarse 1.00, fine 1.00
m=4   R=0 coverage: coarse 1.00, fine 1.00
m=8   R=0 coverage: coarse 1.00, fine 1.00
m=16  R=0 coverage: coarse 1.00, fine 1.00
```

Thus the frozen upper coverage bound `<=0.99` penalizes *increasing information/validity* in the exactly degenerate null cell. This is a methodological gate-validity defect, not evidence that additional information is insufficient.

At `m=16`, the fine `R=0.25` cell also produced empirical coverage `1.00` across the 100 synthetic datasets and therefore failed only the same upper coverage cap despite NI, denominator, and invalid-bootstrap behavior being otherwise correct. This further shows that the upper cap can create a false gate failure under finite Monte Carlo adjudication.

## Information-response curve

The scientifically discriminating sub-margin cell `R=0.125` shows strong precision gain as independent information increases.

### Coarse sentinel (`h=0.1`)

| m | rows | coverage | NI pass | median 95% width | frozen cell pass |
|---:|---:|---:|---:|---:|:---:|
| 1 | 35,072 | 0.93 | 0.57 | 0.138021 | FAIL |
| 2 | 70,144 | 0.97 | 0.83 | 0.090258 | PASS |
| 4 | 140,288 | 0.98 | 1.00 | 0.057569 | PASS |
| 8 | 280,576 | 0.98 | 1.00 | 0.040327 | PASS |
| 16 | 561,152 | 0.96 | 1.00 | 0.027988 | PASS |

### Fine sentinel (`h=4.8828125e-05`)

| m | rows | coverage | NI pass | median 95% width | frozen cell pass |
|---:|---:|---:|---:|---:|:---:|
| 1 | 35,072 | 0.91 | 0.45 | 0.178870 | FAIL |
| 2 | 70,144 | 0.88 | 0.75 | 0.101014 | FAIL |
| 4 | 140,288 | 0.96 | 1.00 | 0.062928 | PASS |
| 8 | 280,576 | 0.95 | 1.00 | 0.042380 | PASS |
| 16 | 561,152 | 0.94 | 1.00 | 0.028726 | PASS |

At `m=4` and `m=8`, **all nondegenerate ratio cells** (`R=0.125, 0.25, 0.50`) pass all of their frozen cell-level coverage, NI, denominator, and invalid-bootstrap requirements at both sentinels.

This is strong directional evidence that independent information quantity improves decision precision. However, because the full conjunctive gate contains an invalid `R=0` coverage requirement, the experiment cannot validly convert that directional result into `SUPPORTED_AS_INFORMATION_QUANTITY` authority.

## Diagnosis

```text
raw contract verdict:
  D_additional_evidence = NOT_IDENTIFIED_WITHIN_GRID

scientific diagnosis after validity check:
  D_decision_gate_validity = FAIL
  D_additional_evidence = UNRESOLVED_DUE_GATE_VALIDITY
```

The shallowest live boundary is therefore **decision-gate validity**, not decision-object inadequacy and not another calibration estimator.

The result does not authorize relaxing the 25% margin, changing NI semantics, changing the construct, or claiming that additional historical evidence exists.

## Authority

Gained:

- exact PR #43 baseline reproducibility;
- the local synthetic information-response curve;
- strong directional evidence that the `R=0.125` decision becomes much more precise with independent information;
- a diagnosed methodological defect in the frozen coverage gate.

Withheld / not gained:

```text
formal D_additional_evidence support authority
replacement-measurement authority
AUTH(Gamma'_cal)
historical calibration closure
M_mature
Z_E / Z_D / Z_C / Z_P
```

## Provenance

```text
final_partitioned.json SHA-256
788109fbec94649a9f7aa94d77a09c8b8141ef7b440fbb0e79e98838ff8807c7

hash_manifest.json SHA-256
b08c47b094a174ca41a7f14b932040538aae24676acc0c1f04059eb3aec73b5d
```

Generated synthetic arrays remain local. Only contracts, apparatus-equivalence evidence, result summaries, hashes, and authority state are committed.

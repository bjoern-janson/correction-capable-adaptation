# Calibration information-scaling diagnostic

## Status

**PROSPECTIVE CANDIDATE-NEUTRAL DIAGNOSTIC — RESULT UNOBSERVED**

This successor opens only the `D_additional_evidence` boundary exposed by PR #43. It does not select a replacement calibration operator, change the calibration construct, change the 25% relative NI decision, inspect historical M1-cal/M2-S vectors, or authorize any CCA-derived feature.

The predecessor result established, locally:

```text
D_detect   = identifiable through the full frozen spatial grid under the sign-informed oracle
D_decision = NONE_IDENTIFIED at the current information quantity
```

Its authority ceiling was empirical and regime-specific, not a universal impossibility claim.

## Governing question

> If the construct, oracle geometry, practical margin, NI semantics, and uncertainty protocol are held fixed, does genuinely independent additional information make the same practical decision identifiable?

The manipulated variable is **independent information quantity only**.

## Information-response object

The primary object is the curve

```text
m -> [NI_pass_rate_m, coverage_m, interval_width_m]
```

where `m` is the number of independent cohort-equivalents of the canonical label-free Trace-the-Ace information geometry.

The diagnostic returns:

```text
R_info = (
  m_min_decision_coarse,
  m_min_decision_fine,
  m_min_decision_joint,
  n_min_decision_joint
)
```

if identified within the frozen grid.

`n_min_decision_joint = 35072 * m_min_decision_joint`.

This is an **information requirement**, not evidence that such additional observations are actually obtainable or admissible in the historical competition dataset.

## Frozen cohort multipliers

```text
m in {1, 2, 4, 8, 16}
```

Corresponding response-equivalent information quantities:

```text
35,072
70,144
140,288
280,576
561,152
```

and session-cluster counts:

```text
22,821
45,642
91,284
182,568
365,136
```

No multiplier may be inserted, removed, or interpolated after results are observed.

## Independent cohort-equivalent construction

Each cohort copy repeats the same deterministic label-free prediction/truth geometry but receives independent synthetic outcome information.

For cohort `c`:

```text
T_i and s_h(T_i) are unchanged
session IDs become (c, session_id)
new Gaussian-copula session factors and row-level innovations are independently sampled
```

There is no stochastic dependence across cohort copies.

Thus increasing `m` changes only the amount of independent Bernoulli information available about the same construct/design geometry.

This is a synthetic information-equivalent diagnostic. It does not assert that repeated independent cohorts exist in the historical dataset.

## Frozen scientific objects

Unchanged from PR #43:

```text
construct                    C_cal,L1
reference construct          C_R = 0.010
relative degradations        R in {0, 0.125, 0.25, 0.50}
practical NI boundary        R < 0.25
NI decision                  upper95(R_hat_oracle) < 0.25
uncertainty                  paired session-cluster percentile bootstrap
bootstrap B                  2000
confidence                   95%
within-session copula rho    0.15
```

No margin, ratio definition, bootstrap family, coverage criterion, or decision threshold may change inside this diagnostic.

## Scale sentinels

PR #43 showed detection through the complete frozen grid and decision failure at every scale. This successor does not reopen spatial-resolution search.

It therefore fixes the two structural endpoints of that already-frozen grid:

```text
h_coarse = 0.1
h_fine   = 0.000048828125
```

Both information-response curves must be reported.

The joint information threshold is the smallest frozen multiplier at which **both** sentinel scales satisfy the full decision gate.

A pass at one sentinel and failure at the other is preserved as scale-dependent evidence; it is not averaged away.

## Oracle estimator

The same sign-informed upper-bound estimator is retained:

```text
m_i = s_h(T_i) * (P_i - Y_i)
C_hat_oracle = mean(m_i) / mean|s_h(T_i)|
```

For paired reference/candidate predictors:

```text
R_hat_oracle = (C_hat_C - C_hat_R) / C_hat_R
```

The oracle remains an information upper-bound apparatus, not a candidate calibration measurement.

## Baseline reproducibility gate

Before any `m>1` result is interpreted, the `m=1` endpoint cells must reproduce the corresponding PR #43 endpoint decision results under the predecessor execution identity.

Required baseline identity:

```text
same source index SHA
same T design
same scale signs
same decision seed 1823
same bootstrap seed 1824
same 100 replicates per ratio cell
same B=2000 session-cluster bootstrap
```

The reproduction artifact must match the committed PR #43 endpoint substantive cell values exactly to floating-point serialization precision used by the predecessor result record.

Failure here is `D_implementation = FAIL/UNOBSERVED` and stops the successor before information scaling.

## Decision gate at each information multiplier

For every `(m, h_sentinel, R)` cell:

```text
100 independent clustered synthetic datasets
paired reference/candidate outcomes within each dataset
paired session-cluster percentile bootstrap
B=2000
95% interval
```

A sentinel scale passes at multiplier `m` iff **every** ratio cell satisfies:

```text
coverage in [0.90, 0.99]
R=0,0.125 -> NI pass rate >= 0.80
R=0.25,0.50 -> NI pass rate <= 0.10
lower95(C_hat_R) > 0 in >=95% of datasets
invalid bootstrap fraction <=0.01 in every dataset
```

The information curve must additionally record for every cell:

```text
NI pass rate
coverage
median 95% interval width for R_hat_oracle
median lower bound for C_hat_R
maximum invalid-bootstrap fraction
```

## Information-threshold outputs

For each sentinel:

```text
m_min_decision_* = smallest frozen m whose full decision gate passes
```

Joint threshold:

```text
m_min_decision_joint = smallest frozen m at which both sentinels pass
```

If no multiplier passes:

```text
NONE_IDENTIFIED_WITHIN_GRID
```

No monotonicity is assumed. All pass/fail vectors and the full response curves are retained. A pass followed by a failure at larger `m` is preserved as diagnostic irregularity rather than smoothed into a threshold.

## Diagnostic interpretation

If a finite `m>1` jointly passes:

```text
D_additional_evidence = SUPPORTED_AS_INFORMATION_QUANTITY
```

meaning only that additional independent information can, in this synthetic oracle regime, make the unchanged decision burden identifiable.

This does **not** establish that the required evidence is historically available, practically collectible, or admissible. Those would be separate evidence-availability questions.

If no frozen multiplier jointly passes:

```text
D_additional_evidence = NOT_IDENTIFIED_WITHIN_GRID
```

which may justify opening `D_decision_object`, but does not itself authorize changing the 25% margin or NI semantics.

## Hard prohibitions

After any scaling result is observed, this branch may not:

```text
change the multiplier grid
change the 25% practical boundary
change C_R
change the relative-degradation formulation
change the oracle estimator
change the scale sentinels
change replicate counts
change bootstrap B or interval family
change coverage/NI/denominator gates
inspect historical M1-cal/M2-S vectors
select a replacement calibration operator from partial scaling results
```

Observed failure cannot authorize its own easier decision rule.

## Authority ceiling

Even a complete success can establish only:

```text
local synthetic evidence that information quantity is sufficient for the frozen oracle decision burden
and an estimated cohort/row-equivalent information threshold within the declared grid
```

It cannot establish:

```text
replacement-measurement authority
AUTH(Gamma'_cal)
historical calibration closure
availability of the required additional historical evidence
M_mature
CCA / G1 / PMC / JT / C_improve
Z_E / Z_D / Z_C / Z_P
```

## Reachability

Current topology:

```text
D_resolution
-> D_decision_precision
-> D_additional_evidence
-> (if information quantity is supported and legitimately available) G_operator

or, if information quantity remains unresolved/infeasible,

D_decision_object
```

Historical calibration and all CCA-derived features remain unreachable throughout this diagnostic.

# Calibration resolution diagnostic

## Status

**PROSPECTIVE CANDIDATE-NEUTRAL DIAGNOSTIC — RESULT UNOBSERVED**

This artifact opens only the resolution boundary exposed by the failed SmoothECE candidate. It does not select a replacement measurement operator, authorize a calibration metric, inspect historical M1-cal/M2-S predictions, or modify the mature-baseline authority state.

The governing question is:

> What calibration-error spatial scale is actually identifiable from the available Bernoulli sample, first for defect detection and separately for the practical non-inferiority decision?

The diagnostic exists because the prior F5 fixture mixed two questions:

1. can a measurement preserve local magnitude before sign cancellation; and
2. is that local structure identifiable at the available finite-sample information resolution?

Those questions must now be separated.

## Governing operator gate

Future candidate admissibility remains:

```text
G_operator = R1 & R2 & R3_star & R4
```

where:

```text
R1       where can signed residuals first interact?
R2       is local magnitude represented before cancellation can erase it?
R3_star  is the spatial scale whose magnitude is promised itself identifiable at n=35,072?
R4       can the observable support a valid uncertainty procedure and the practical NI decision?
```

This diagnostic addresses only `R3_star`.

## Output object

The diagnostic must return:

```text
R_res = (h_min_detect, h_min_decision)
```

or an equivalent admissible scale class.

Interpretation:

```text
h >= h_min_detect
    defect detection is identifiable under the declared oracle upper-bound challenge.

h >= h_min_decision
    the practical relative-degradation decision is identifiable under the declared oracle upper-bound challenge.
```

The diagnostic is intentionally an **oracle upper bound**. It is given the synthetic defect's sign/phase pattern before observing outcomes. Therefore:

```text
oracle failure at scale h
    => no ordinary candidate lacking extra information may claim that scale is identifiable under this challenge.

oracle pass at scale h
    != authority for any real replacement measurement operator.
```

A future operator must still earn `R1`, `R2`, and `R4`, then pass its own prospectively frozen F0-F6 validation.

## Information regime

Only the canonical label-free Trace-the-Ace response/session geometry is used:

```text
index path   external_tests/trace_the_ace/artifacts/index.csv
index SHA256 296399770b0818fa528f33382497bc7f4793b3c54a2e49e56e77efbc19d55c60
rows         35,072
sessions     22,821
allowed      response_id, session_id
labels       forbidden
```

Synthetic truth probabilities are generated independently of historical labels from the deterministic hash design frozen in the SmoothECE candidate:

```text
salt = "SMECE_CAL_REPLACEMENT_V1|"
u_i = (uint64_be(sha256(salt + response_id)[0:8]) + 0.5) / 2^64
T_i = 0.05 + 0.90*u_i
```

This preserves the same label-free information geometry while reopening only spatial resolution.

## Scale family

Define spatial period:

```text
h_j = 0.1 / 2^j
j = 0,...,11
```

so the frozen scale grid is:

```text
0.1000000000
0.0500000000
0.0250000000
0.0125000000
0.0062500000
0.0031250000
0.0015625000
0.0007812500
0.0003906250
0.0001953125
0.00009765625
0.000048828125
```

The finest declared scale is deliberately near the row-alternating geometry implicated by the prior F5 failure. No scale may be added, removed, or interpolated after results are observed.

## Scale-indexed calibration defect

At each `h`, define the known sign pattern:

```text
s_h(T_i) = sign(sin(2*pi*T_i/h))
```

Rows exactly on a zero of the sine receive sign `0`.

For construct magnitude `C > 0`:

```text
a(C,h) = C / mean_i |s_h(T_i)|
P_i(C,h) = T_i + a(C,h)*s_h(T_i)
Q(P_i) = T_i
```

Fixture constitution requires:

```text
all P_i in [0,1]
mapping i -> P_i injective at tolerance 1e-12
abs(mean|P-T| - C) <= 1e-12
clipping forbidden
```

A constitution failure is an apparatus/fixture failure at that scale, not negative evidence about identifiability.

## Synthetic outcome generator

Use the already frozen clustered Bernoulli information regime:

```text
rho = 0.15
Z_s ~ N(0,1)
epsilon_si ~ N(0,1)
L_si = sqrt(rho)*Z_s + sqrt(1-rho)*epsilon_si
U_si = Phi(L_si)
Y_si = 1[U_si <= T_i]
```

The same sampled outcomes are used for all predictor arms inside a paired cell.

Frozen seeds:

```text
resolution null-training seed   1821
resolution detection seed       1822
resolution decision seed        1823
resolution bootstrap seed       1824
```

No seed changes are permitted after any result is observed.

## Oracle measurement

The diagnostic uses the known defect sign pattern to demodulate the signed calibration residual before aggregation:

```text
m_i(P,Y;h) = s_h(T_i) * (P_i - Y_i)
```

Define the oracle construct estimator:

```text
C_hat_oracle(P,Y;h)
    = mean_i m_i(P,Y;h) / mean_i |s_h(T_i)|
```

under the positive-amplitude synthetic alternative.

For the declared family:

```text
E[C_hat_oracle] = C
```

up to finite-design/copula sampling variation.

This operator is not a candidate calibration metric. It uses knowledge unavailable to a real general-purpose measurement operator and exists only to establish a best-case information-resolution ceiling.

## Detection-identifiability diagnostic

Detection target:

```text
C_detect = 0.010
```

For every frozen scale `h`:

1. Generate `200` independent F0 null-training datasets.
2. Define the one-sided null critical value as the 95th percentile of `C_hat_oracle` using NumPy quantile method `higher`.
3. Generate `100` independent F0 evaluation datasets.
4. Generate `100` independent `C=0.010` defect datasets.
5. Count detection when `C_hat_oracle > null_critical(h)`.

A scale is **detection-identifiable** iff:

```text
F0 false-positive rate <= 0.10
AND
C=0.010 detection rate >= 0.80
```

`h_min_detect` is the finest (smallest) frozen `h` satisfying both requirements.

If no scale passes, `h_min_detect = NONE_IDENTIFIED`.

## Decision-identifiability diagnostic

This is separate from defect detection.

For each scale `h`, define a reference construct magnitude:

```text
C_R = 0.010
```

and paired candidate construct magnitudes using the inherited practical relative-degradation convention only as a **resolution challenge**:

```text
R_construct in {0.00, 0.125, 0.25, 0.50}
C_C = (1 + R_construct) * C_R
```

This does not authorize a future candidate's numerical margin mapping. It asks only whether the information regime can support the same practical burden when the construct itself is known.

For every `(h, R_construct)` cell:

```text
100 independent clustered synthetic datasets
same Y used for reference and candidate predictors
paired session-cluster percentile bootstrap
B = 2000
95% interval
```

Dataset statistic:

```text
R_hat_oracle = (C_hat_C - C_hat_R) / C_hat_R
```

Invalid bootstrap replicate:

```text
C_hat_R <= 0
```

Maximum invalid-replicate fraction:

```text
0.01
```

Dataset-level NI passes iff:

```text
upper95(R_hat_oracle) < 0.25
```

A scale is **decision-identifiable** iff, for every ratio cell:

```text
true R=0.00   -> NI pass rate >= 0.80
true R=0.125  -> NI pass rate >= 0.80
true R=0.25   -> NI pass rate <= 0.10
true R=0.50   -> NI pass rate <= 0.10
```

and the paired 95% interval has empirical coverage in `[0.90, 0.99]` for every ratio cell.

Additionally, the reference denominator must be resolved:

```text
lower95(C_hat_R) > 0
```

in at least 95% of datasets in every ratio cell.

`h_min_decision` is the finest frozen `h` satisfying all decision requirements.

If no scale passes, `h_min_decision = NONE_IDENTIFIED`.

## Monotonicity diagnosis

No monotonicity across scale is assumed prospectively.

After all scale cells are evaluated, report the complete pass/fail vector. If a finer scale passes while a coarser neighboring scale fails, do not smooth or force a threshold. Record the topology as non-monotone and leave `h_min` as the finest passing declared scale while flagging resolution irregularity for diagnosis.

## Stop / execution rules

Unlike a candidate gate sequence, the resolution diagnostic must evaluate **all frozen scales** because the output is the resolution topology itself.

Permitted before execution:

```text
implementation validation
fixture constitution validation
runtime partitioning/checkpointing
```

Forbidden after any result is observed:

```text
changing scale grid
changing C_detect or C_R
changing 25% relative decision burden
changing seeds or replicate counts
changing bootstrap procedure
changing false-positive/power/coverage/decision thresholds
changing oracle sign pattern
historical M1-cal/M2-S access
candidate metric/operator selection based on partial scale results
```

## Authority ceiling

Even a complete diagnostic can establish only:

```text
local upper-bound evidence about calibration-error resolution in the declared synthetic information regime
R_res = (h_min_detect, h_min_decision)
```

It cannot establish:

```text
replacement-measurement authority
AUTH(Gamma'_cal)
construct change from C_cal,L1
historical calibration closure
M_mature
CCA / G1 / PMC / JT / C_improve
Z_E / Z_D / Z_C / Z_P
```

## Reachability after result

Only after `R_res` exists may a replacement operator be screened under:

```text
G_operator = R1 & R2 & R3_star & R4
```

with `R3_star` constrained by the earned resolution topology.

The branch topology is therefore:

```text
F5 diagnosis
-> D_resolution
-> G_operator
-> one candidate
-> candidate-specific contract
-> F0-F6
```

Historical vectors and all CCA-derived features remain unreachable throughout this diagnostic.
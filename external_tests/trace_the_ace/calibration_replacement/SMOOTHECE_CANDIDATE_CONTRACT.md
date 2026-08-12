# SmoothECE replacement-calibration candidate contract

## Status

**PROSPECTIVE CANDIDATE CONTRACT — RESULT UNOBSERVED**

This child contract instantiates exactly one candidate under PR #41's candidate-neutral design envelope: **SmoothECE (smECE)**.

No scientific fixture has been executed. Historical M1-cal/M2-S predictions remain forbidden until all four prospective gates pass.

The exact machine-readable experiment identity is `SMOOTHECE_FIXTURE_SPEC.yaml`. This document states the scientific contract; the YAML fixes row geometry, formulas, seeds, searches, resampling, and thresholds. Any inconsistency is a contract defect and must be repaired before execution, never after a candidate result.

## Selection rationale

The diagnosed predecessor failure is fixed-bin cancellation: ECE-10 can erase opposing local calibration residuals within a bin. SmoothECE is selected because it removes fixed histogram bins and smooths calibration residuals locally over prediction space.

Selection is based on the diagnosed failure mechanism, not historical model behavior, leaderboard performance, popularity, or convenience. Literature support is background justification only and grants no project authority.

## Pinned candidate identity

Reference:

```text
Jarosław Błasiok, Preetum Nakkiran
Smooth ECE: Principled Reliability Diagrams via Kernel Smoothing
ICLR 2024 / arXiv:2309.12236
```

Pinned authors' implementation:

```text
repo   apple/ml-calibration
commit 18ff21a7e4e409fc4885690129f50211b32ea144
metrics.py blob 662821b962ea67c21515b1a133a7692ae6ac793d
kernels.py blob a55bec6793ef18ea735e58466e6d5143f5e5b660
config.py  blob 65059c7f156df78ef44b8bd43dfd85fda216ef8d
```

Frozen candidate defaults:

```text
residual                  r_i = f_i - y_i
kernel                    reflected Gaussian
use_logit_scaling         false
smECE_mesh_pts            200
manual bandwidth          forbidden
bandwidth-search eps      0.001
search start              1
binary refinements        10
predicate(alpha)          alpha < eps OR alpha < smECE_sigma(alpha)
```

A local implementation must first reproduce the pinned reference implementation on the prospectively frozen equivalence suite with `max_abs_error <= 1e-10` for both point SmoothECE and selected bandwidth. Failure stops execution before F0.

## Calibration construct

The intended construct remains

\[
Q(p)=E[Y\mid P=p],
\qquad
C_{cal,L1}=E|P-Q(P)|.
\]

SmoothECE is not assumed numerically equal to `C_cal,L1`. Construct fidelity must be earned.

## Exact synthetic design

Synthetic geometry uses only `response_id` and `session_id` from canonical `index.csv` SHA-256:

```text
296399770b0818fa528f33382497bc7f4793b3c54a2e49e56e77efbc19d55c60
```

No labels or historical model predictions may enter fixture construction.

For each canonical response ID, a deterministic SHA-256 transform creates a latent truth probability

\[
T_i\in[0.05,0.95].
\]

For defect family `j`, a deterministic shape `s_j(T_i)` defines the predictor family

\[
P_{j,a,i}=T_i+a\,s_j(T_i).
\]

Whenever the finite mapping `i -> P_i` is injective,

\[
Q(P_i)=T_i,
\]

so the exact finite-design calibration construct is

\[
C_{cal,L1}=\operatorname{mean}|P_i-T_i|.
\]

Clipping is forbidden. Bounds or injectivity failure causes fixture-constitution failure before sampling.

## F0-F6

The exact formulas are frozen in `SMOOTHECE_FIXTURE_SPEC.yaml`:

```text
F0  perfect calibration
F1  global shift
F2  linear tilt
F3  smooth low-frequency sinusoid
F4  localized triangular band
F5  exactly bin-balanced legacy-ECE-bin alternating defect
F6  high-frequency sinusoid with period 0.025
```

The construct-fidelity challenge magnitudes are:

```text
C_cal,L1 = 0.005, 0.010, 0.020
```

These are synthetic measurement challenges only, not the historical practical margin.

## Finite-sample cluster structure

Outcomes have exact Bernoulli marginals `T_i` and within-session dependence via the frozen Gaussian-copula generator with `rho=0.15`.

The same sampled outcomes are used for reference and candidate predictors in paired decision cells.

All seeds are frozen in the YAML before execution.

## G_F — construct fidelity

`G_F` passes only if all prospective conditions hold on exact finite-design population objects, before Bernoulli sampling:

1. F0 SmoothECE <= `1e-4`.
2. F1-F6 SmoothECE is positive at each declared construct magnitude.
3. For every F1-F6:

```text
theta(0.005) < theta(0.010) < theta(0.020)
```

4. At `C_cal,L1=0.010`, F5 and F6 retain at least 10% of construct magnitude in SmoothECE scale.

The 10% floor is only a minimum fidelity safeguard against repeating ECE-10 near-erasure; it does not assert scale equality.

```text
G_F failure -> STOP CANDIDATE
```

No bandwidth, kernel, fixture, or fidelity-threshold tuning is authorized.

## G_detect — sensitivity and specificity

At `C_cal,L1=0.010`:

- a frozen independent F0 null-training set supplies the 95th-percentile point-SmoothECE critical value;
- a separate F0 evaluation set measures false positives;
- each F1-F6 is evaluated on its own frozen replicate set.

The exact critical-value quantile convention and seeds are fixed in the YAML.

Requirements:

```text
F0 false-positive rate <= 0.10
F1-F6 detection rate   >= 0.80 each
```

```text
G_detect failure -> STOP CANDIDATE
```

No threshold tuning is authorized.

## Practical-margin mapping

The predecessor practical convention is preserved as **25% relative calibration degradation**, not by copying the numerical ECE margin.

For SmoothECE population values `theta_R` and `theta_C`:

\[
R_{sm}=\frac{\theta_C-\theta_R}{\theta_R}.
\]

The practical candidate-scale NI claim is:

\[
R_{sm}<0.25.
\]

This dimensionless relative rule is the scale-aware mapping. There is no `epsilon_ECE -> epsilon_smECE` substitution.

## Paired synthetic decision populations

For every F1-F6, the reference predictor is fixed at

\[
C_{cal,L1}=0.010.
\]

Its population SmoothECE is `theta_R`.

Candidate amplitudes are then selected by the exact deterministic population search in the YAML to realize:

```text
R_sm = 0.00, 0.125, 0.25, 0.50
```

No sampled outcome can influence this search. Failure to realize a target while preserving bounds/injectivity is fixture-constitution failure, not evidence about the candidate.

## G_U — uncertainty validity

The frozen uncertainty procedure is:

```text
paired session-cluster percentile bootstrap
B = 2000
confidence = 95%
resampling unit = session
statistic R_sm_hat = (smECE_C - smECE_R) / smECE_R
```

For every F1-F6 and every declared ratio cell, 100 synthetic datasets are generated.

`G_U` passes only if empirical 95% interval coverage of the known population `R_sm` lies in `[0.90,0.99]` in every cell.

```text
G_U failure -> STOP CANDIDATE
```

No bootstrap inflation or interval replacement is authorized after failure.

## G_decision — practical decision validity

A synthetic or historical comparison passes non-inferiority only if

\[
U_{95}(R_{sm})<0.25.
\]

Required synthetic NI behavior in every F1-F6 family:

```text
true R_sm = 0.00   -> NI pass rate >= 0.80
true R_sm = 0.125  -> NI pass rate >= 0.80
true R_sm = 0.25   -> NI pass rate <= 0.10
true R_sm = 0.50   -> NI pass rate <= 0.10
```

The denominator-resolution guard is:

```text
lower95(theta_R) > 0.001
```

and must hold in at least 95% of replicates in every decision cell.

```text
G_decision failure -> STOP CANDIDATE
```

No practical-margin tuning is authorized.

## Methodological authority

\[
\boxed{
AUTH(\Gamma'_{cal,smECE})
=
G_F\land G_{detect}\land G_U\land G_{decision}
}
\]

The gates are conjunctive and non-compensatory.

Only complete passage opens historical access.

## Historical firewall and adjudication

Before all four gates pass:

```text
M1-cal prediction read   FORBIDDEN
M2-S prediction read     FORBIDDEN
historical candidate tuning FORBIDDEN
```

If authority is earned, the historical comparison is:

\[
R_{sm,hist}
=
\frac{smECE(M2S)-smECE(M1cal)}{smECE(M1cal)}.
\]

Historical SmoothECE NI passes iff:

```text
lower95(smECE(M1cal)) > 0.001
AND
upper95(R_sm,hist) < 0.25
```

Previously earned LL, Brier, and mean-bias requirements remain unchanged. This successor reopens only the inadequate ECE measurement edge.

A historical failure or unresolved result does not automatically authorize a second metric or new calibrator.

## Authority ceiling

Even full success can earn only:

```text
local methodological authority for SmoothECE as replacement calibration measurement
plus possible closure of the mature non-CCA calibration boundary after historical adjudication
```

It cannot earn CCA, G1, PMC, JT, C_improve, broad H_O, or any `Z_E/Z_D/Z_C/Z_P` authority.

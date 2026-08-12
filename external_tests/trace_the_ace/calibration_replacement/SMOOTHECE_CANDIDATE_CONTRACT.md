# SmoothECE replacement-calibration candidate contract

## Status

**PROSPECTIVE CANDIDATE CONTRACT — RESULT UNOBSERVED**

This child contract instantiates exactly one candidate under PR #41's candidate-neutral design envelope: **SmoothECE (smECE)**.

Historical M1-cal/M2-S predictions remain forbidden until all prospective candidate gates pass.

## Selection rationale

The diagnosed failure is fixed-bin cancellation: ECE-10 can erase opposing local calibration residuals inside a bin. SmoothECE is selected because it removes fixed histogram bins and smooths residuals locally in prediction space. Selection is mechanism-driven, not historical-score-, leaderboard-, or convenience-driven.

Literature support motivates this choice but grants no project authority.

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

Frozen defaults:

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

At fixed `sigma`, residuals are locally smoothed with the reflected Gaussian kernel and the absolute smoothed residual is integrated against the smoothed prediction density. Automatic bandwidth is the deterministic fixed-point/search rule above.

Any local implementation must first match the pinned reference implementation on a deterministic equivalence suite with `max_abs_error <= 1e-10`; otherwise execution stops before scientific fixtures.

## Construct

The intended calibration construct remains

\[
Q(p)=E[Y\mid P=p],
\qquad
C_{cal,L1}=E|P-Q(P)|.
\]

SmoothECE is not assumed numerically equal to this construct. It must earn fidelity.

## Common synthetic geometry

All synthetic fixtures:

```text
prediction P is primitive
Q(P)=E[Y|P] is explicit
P support = [0.05,0.95]
session sizes = canonical label-free Trace-the-Ace session-size distribution
within-session P coordinates = deterministic low-discrepancy quantiles
```

Defect amplitude is determined before outcome sampling by deterministic search to hit the declared population `C_cal,L1` target within `1e-5` absolute error. If Q leaves `[0,1]`, fixture constitution fails; clipping after selection is forbidden.

## F0-F6

```text
F0 perfect
   Q(p)=p

F1 global shift
   Q(p)=p+a

F2 linear tilt
   Q(p)=p+a(2p-1)

F3 smooth low-frequency
   Q(p)=p+a sin(2*pi*p)

F4 localized band
   Q(p)=p+a*triangular(p; center=0.65, half_width=0.15)

F5 legacy-bin alternating
   u=frac(10p)
   Q(p)=p+a*sign(sin(2*pi*u))
   deterministic balancing enforces zero mean residual inside each legacy 0.1 ECE bin

F6 high-frequency local
   Q(p)=p+a sin(20*pi*p)
```

Construct-fidelity challenge magnitudes:

```text
C_cal,L1 = 0.005, 0.010, 0.020
```

These are synthetic validity levels only, not the historical practical margin.

## Clustered finite-sample generator

Bernoulli marginals remain exactly Q(P), with within-session dependence induced by a Gaussian copula:

```text
rho = 0.15
Z_s ~ N(0,1)
epsilon_si ~ N(0,1)
L_si = sqrt(rho) Z_s + sqrt(1-rho) epsilon_si
Y_si = 1[Phi(L_si) <= Q(P_si)]
```

Frozen randomness:

```text
fixture master seed   1811
bootstrap master seed 1812
replicates per cell   100
```

## G_F — construct fidelity

Pass iff all are true on exact population fixtures, before sampled outcomes:

1. F0 candidate population value <= `1e-4`.
2. F1-F6 candidate population value > 0 at each declared construct magnitude.
3. For each F1-F6:
   `theta(0.005) < theta(0.010) < theta(0.020)`.
4. At `C_cal,L1=0.010`, F5 and F6 must retain at least 10% of construct magnitude in candidate scale.

The 10% floor is a minimum local-fidelity safeguard against repeating ECE-10's near-erasure; it does not assert scale equality.

`G_F` failure => stop candidate. No tuning.

## G_detect — sensitivity / specificity

For each F1-F6 at `C_cal,L1=0.010`, run 100 clustered synthetic datasets.

The prospectively frozen F0 synthetic distribution supplies the null critical value; historical data may not contribute.

Requirements:

```text
F0 false-positive rate <= 0.10
F1-F6 detection rate   >= 0.80 each
```

`G_detect` failure => stop candidate. No tuning.

## Scale-aware practical-margin mapping

The predecessor practical convention is preserved as **25% relative calibration degradation**, not by copying the ECE numerical margin.

For candidate measurement theta:

\[
R_{sm}=\frac{\theta_C-\theta_R}{\theta_R}.
\]

The candidate-scale practical NI boundary is dimensionless:

\[
R_{sm}<0.25.
\]

This is the complete scale mapping. No `epsilon_ECE -> epsilon_smECE` numerical substitution is permitted.

## G_U — uncertainty validity

Frozen uncertainty procedure:

```text
paired session-cluster percentile bootstrap
B = 2000
95% interval
resampling unit = session
```

For every F1-F6, paired synthetic reference/candidate populations are deterministically constituted at true candidate-scale relative degradations:

```text
R_sm = 0.00, 0.125, 0.25, 0.50
```

Population amplitude search occurs before outcome sampling. Each reference must satisfy population `theta_R >= 0.005`; otherwise fixture constitution fails.

`G_U` passes iff empirical 95% interval coverage is within `[0.90,0.99]` for every family/ratio cell.

`G_U` failure => stop candidate. No B inflation or interval substitution.

## G_decision — practical NI decision validity

Dataset-level NI passes iff:

\[
U_{95}(R_{sm})<0.25.
\]

Required synthetic behavior for every F1-F6:

```text
true R_sm = 0.00   -> NI pass rate >= 0.80
true R_sm = 0.125  -> NI pass rate >= 0.80
true R_sm = 0.25   -> NI pass rate <= 0.10
true R_sm = 0.50   -> NI pass rate <= 0.10
```

Denominator-resolution guard:

```text
lower95(theta_R) > 0.001
```

must hold in at least 95% of decision replicates in every family/ratio cell. Otherwise decision validity is unresolved.

`G_decision` failure => stop candidate. No margin tuning.

## Authority gate

\[
\boxed{
AUTH(\Gamma'_{cal,smECE})
=
G_F\land G_{detect}\land G_U\land G_{decision}
}
\]

The gates are conjunctive and non-compensatory.

Only if all four pass may historical M1-cal/M2-S prediction vectors be read.

## Historical adjudication if authority is earned

Reference: sealed `M1-cal`.
Candidate: sealed historical `M2-S` Platt probability treatment.

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

Previously earned LL, Brier, and mean-bias requirements remain unchanged; this successor reopens only the inadequate ECE measurement edge.

If historical NI fails or is unresolved, no alternate calibrator or metric is automatically authorized.

## Stop / authority ceiling

```text
G_F failure        -> stop
G_detect failure   -> stop
G_U failure        -> stop
G_decision failure -> stop
```

No within-candidate tuning is allowed after a gate failure.

Maximum authority even on complete success:

```text
local methodological authority for SmoothECE as the replacement calibration measurement
plus possible closure of the mature non-CCA calibration boundary after historical adjudication
```

No CCA, G1, PMC, JT, C_improve, broad H_O, or Z_E/Z_D/Z_C/Z_P authority can be earned here.

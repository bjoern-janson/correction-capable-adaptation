# Calibration replacement-measurement design envelope

## Status

**FROZEN METHODOLOGICAL DESIGN ENVELOPE — CANDIDATE UNINSTANTIATED — EXECUTION UNAUTHORIZED**

This artifact opens only the replacement-measurement boundary authorized by the construct-faithful ECE-10 object-adequacy result. It does not select a replacement statistic, does not authorize historical OOF access, and changes no current scientific authority state.

The predecessor finding is local and specific:

\[
\boxed{\text{fixed equal-width ECE-10 can erase construct-faithful local calibration error through within-bin cancellation}.}
\]

The successor must solve that measurement problem. It may not be selected because it is popular, favorable on historical predictions, numerically convenient, or easier to pass.

## Governing construct

The intended calibration construct remains standard probabilistic calibration:

\[
Q(P)=E[Y\mid P].
\]

A replacement observable must earn fidelity to calibration deviation with respect to this construct. No candidate inherits authority merely from ECE-10 failure.

The methodological hierarchy is fixed as:

\[
\boxed{
C_{\mathrm{cal}}
\rightarrow
\mathcal M_{\mathrm{cal}}^{\mathrm{successor}}
\rightarrow
\text{synthetic construct validity}
\rightarrow
\text{uncertainty validity}
\rightarrow
\text{practical-margin mapping}
\rightarrow
\operatorname{AUTH}(\Gamma'_{\mathrm{cal}})
}
\]

Only after `AUTH(Gamma'_cal)` is earned may the successor measurement touch sealed historical model vectors.

## Candidate class constraint

The concrete successor candidate is **not yet selected**.

A candidate must be bin-free or otherwise demonstrate prospectively that its finite-sample observable is not vulnerable to the diagnosed fixed-bin cancellation pathology. Merely increasing the number of ECE bins, switching to equal-mass bins, tuning bins after observing results, or choosing a metric because it gives a friendlier historical answer is outside this envelope.

Any concrete candidate must be frozen in a separately identified prospective candidate contract before synthetic execution.

## Adversarial synthetic fixture family

Every concrete candidate must be tested on the following prospectively fixed qualitative fixture classes, instantiated quantitatively before candidate execution:

```text
F0  perfect calibration / no defect
F1  global calibration shift
F2  linear calibration tilt
F3  smooth low-frequency calibration defect
F4  localized-band calibration defect
F5  within-ECE-bin alternating calibration defect
F6  high-frequency local calibration defect near the candidate's effective resolution boundary
```

All fixtures must be construct-faithful:

```text
P is primitive
Q(P) = E[Y | P] is explicitly defined
truth is defined independently of the candidate observable
```

Fixture definitions, defect amplitudes, sample structure, seeds, detection criteria, false-positive criteria, uncertainty criteria, and stopping rules must be committed before observing candidate performance.

Historical OOF predictions are forbidden during candidate selection, fixture construction, and candidate-method validation.

## Construct sensitivity versus decision sensitivity

The successor must separate two questions that may not be conflated:

1. **Construct sensitivity** — does the measurement faithfully respond to declared calibration defects?
2. **Decision sensitivity** — can the finite-sample measurement support the practical non-inferiority decision with adequate uncertainty behavior?

A candidate that detects a defect but cannot support the decision rule does not earn methodological authority for the mature-baseline gate.

## Authority gates

The methodological authority gate is conjunctive and non-compensatory:

\[
\boxed{
\operatorname{AUTH}(\Gamma'_{\mathrm{cal}})
=
G_F
\land
G_{\mathrm{detect}}
\land
G_U
\land
G_{\mathrm{decision}}
}
\]

### `G_F` — construct fidelity

The candidate observable must track prospectively declared construct-faithful calibration deviations across the full fixture family without the diagnosed cancellation failure becoming a hidden blind spot.

Failure on a declared material construct defect fails `G_F` unless the candidate contract prospectively and independently identifies that defect as outside its intended construct scope.

### `G_detect` — sensitivity and specificity

The candidate must prospectively demonstrate both:

```text
sensitivity to declared material defects
specificity under F0 and declared sub-material defects
```

Detection, miss, false-positive, and correct-null criteria must be frozen numerically in the candidate contract before execution.

### `G_U` — uncertainty validity

The candidate's uncertainty procedure must be prospectively specified and validated on clustered finite-sample synthetic fixtures matching the relevant sampling structure.

At minimum, the candidate contract must predeclare:

```text
coverage target
resampling / analytic uncertainty procedure
cluster unit
finite-sample validation fixtures
nonregularity or degeneracy safeguards
failure criteria
```

More Monte Carlo repetitions may reduce simulation error in a validated procedure; they may not substitute for a procedure whose sampling uncertainty is inadequate or invalid.

### `G_decision` — practical-margin decision validity

The candidate must support the actual mature-baseline decision rather than merely produce a calibrated point score.

The practical concept of material degradation may be inherited, but the numerical ECE margin may **not** be copied onto a different measurement scale:

\[
\boxed{
\epsilon_{\mathrm{ECE}}
\not\Rightarrow
\epsilon_{\mathrm{candidate}}
\text{ by numerical substitution.}
}
\]

Instead:

\[
\boxed{
\text{practical materiality}
\rightarrow
\text{prospective scale-aware mapping}
\rightarrow
\epsilon_{\mathrm{candidate}}.
}
\]

The mapping procedure, its assumptions, and candidate-specific decision thresholds must be frozen before candidate performance is observed.

The decision-validity fixture must separately demonstrate:

```text
reliable non-inferiority decisions for declared sub-material defects
non-inferiority failure / degradation detection for declared supra-material defects
controlled behavior at the practical boundary
```

## Candidate adjudication

A concrete candidate may acquire methodological authority only if all four gates pass prospectively:

```text
G_F            PASS
G_detect       PASS
G_U            PASS
G_decision     PASS
```

Ordinary nulls or mixed gates remain unresolved. One favorable gate may not compensate for another failed gate.

Candidate failure does not automatically authorize a different metric. Failure must first be localized to construct, representation, estimator, uncertainty procedure, decision mapping, or validation apparatus before a successor candidate is opened.

## Historical adjudication firewall

Until a candidate earns `AUTH(Gamma'_cal)`:

```text
historical M1-cal / M2-S OOF access for replacement adjudication   FORBIDDEN
replacement-driven retrospective threshold tuning                 FORBIDDEN
historical result-based candidate selection                       FORBIDDEN
leaderboard-based metric selection                                FORBIDDEN
```

After methodological authority is earned, historical adjudication must itself be prospectively specified before the replacement measurement is applied to sealed model vectors.

## Authority ceiling

This design envelope and any later synthetic success can at most earn authority for a calibration measurement protocol within the declared scope.

It cannot by itself establish:

```text
mature non-CCA baseline constitution
M2-S probability-treatment authority on historical data
Z_E / Z_D / Z_C / Z_P authorization
G1
PMC
JT
C_improve
CCA causal or ontological claims
```

The eventual first CCA feature test remains blocked until calibration closes and `M_mature` is constituted.

## Reachability consequence

Current reachable set remains intentionally narrow:

\[
\boxed{
\mathcal T_t
=
\{\text{instantiate and validate one prospective replacement-calibration measurement candidate}\}.
}
\]

No downstream CCA edge is opened by freezing this envelope.

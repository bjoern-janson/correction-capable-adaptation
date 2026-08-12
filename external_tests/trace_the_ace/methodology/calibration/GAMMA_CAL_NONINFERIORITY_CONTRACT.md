# Calibration-gate uncertainty methodological successor

## Status

**PROSPECTIVE METHOD CONTRACT — RESULT UNOBSERVED — NO SCIENTIFIC AUTHORITY MOVEMENT**

This is a methodological successor under the frozen Trace the Ace governing interface and reachability invariant. It does not introduce a new calibrator, change any predictive model, authorize a CCA-derived feature, or retroactively rewrite the historical M2-S calibration result.

The predecessor evidence that licenses reopening is the closed ECE-stability diagnostic: the historical M2-S vs M1-cal ECE-10 point degradation was positive but not stably identified under paired session-cluster resampling.

## Reopened rule

The predecessor rule treated pointwise ECE-10 non-degradation as a deterministic gate. This successor reopens only the uncertainty semantics of that gate.

It asks:

> What uncertainty-bearing claim should the calibration gate identify before a probability treatment is allowed to count as mature?

## Methodological target

Define the local calibration-preservation object:

\[
G_{cal}^{NI}=\text{the candidate probability treatment exhibits no practically relevant degradation in probabilistic quality relative to the predecessor calibrated baseline, under paired session-cluster uncertainty.}
\]

This is predictive/methodological non-inferiority, not a causal claim.

The candidate and reference probability vectors remain sealed historical OOF objects:

```text
reference: M1-cal
candidate: M2-S Platt
```

No model refit is permitted in this methodological test.

## Practical tolerances

The practical calibration tolerances are anchored to the predecessor M1 calibration contract's already-established 25% materiality convention, not to the observed M2-S differences and not to the public leaderboard.

Reference values:

```text
M1-cal ECE-10                   0.0159898481
M1-cal absolute mean bias       0.0105359299
```

Therefore freeze:

```text
epsilon_ECE   = 0.25 * 0.0159898481 = 0.003997462025
epsilon_bias  = 0.25 * 0.0105359299 = 0.002633982475
```

Log loss and Brier score are proper scoring rules and receive no positive degradation tolerance in this successor.

## Uncertainty procedure

All differences are candidate minus reference and lower is better.

Use paired `session_id` cluster bootstrap with 2,000 replicates. Resampling is over sessions, preserving all response rows belonging to a sampled session.

Freeze independent seeds:

```text
Delta LL       1741
Delta Brier    1742
Delta ECE-10   1743
Delta bias     1744
```

For every metric report the point difference and percentile 95% interval.

## Successor gate

The methodological rule is conjunctive:

\[
\boxed{
G_{cal}^{NI}
=
G_{LL}
\land
G_{Brier}
\land
G_{ECE}^{NI}
\land
G_{bias}^{NI}
}
\]

where:

```text
G_LL       : CI95 upper[Delta LL]      < 0
G_Brier    : CI95 upper[Delta Brier]   < 0
G_ECE^NI   : CI95 upper[Delta ECE-10]  < epsilon_ECE
G_bias^NI  : CI95 upper[Delta bias]    < epsilon_bias
```

A point estimate alone cannot pass or fail the ECE/bias non-inferiority claim.

The historical deterministic ECE verdict remains historical. This successor, if validated and authorized, creates a new methodological adjudication rather than editing that predecessor result.

## Measurement-validity challenge suite

Before this rule may govern the historical M1-cal vs M2-S comparison, it must survive a prospectively frozen finite synthetic validation suite.

Use the canonical label-free session-size distribution. For each synthetic dataset:

1. draw one latent reference probability per session as `p_ref = 0.1 + 0.8 * Beta(7,3)`;
2. repeat that probability for every response row in the session;
3. draw outcomes `Y ~ Bernoulli(p_ref)` independently conditional on `p_ref`;
4. define candidate probabilities as `p_cand = p_ref + delta`, which remains inside `(0,1)` for the frozen deltas;
5. evaluate only the ECE non-inferiority rule with the same 10 equal-width bins and paired session-cluster bootstrap.

Three scenarios, each across 10 predeclared seeds:

```text
S0: delta = 0
S1: delta = 0.5 * epsilon_ECE
S2: delta = 2.0 * epsilon_ECE
```

Use 300 bootstrap replicates per synthetic dataset for this finite validation suite and deterministic seeds derived from the dataset seed.

Finite-suite validity gates:

```text
S0 pass count >= 9 / 10
S1 pass count >= 7 / 10
S2 fail count >= 9 / 10
```

This suite has a deliberately local authority ceiling: surviving it establishes only that the proposed uncertainty rule behaves correctly on these declared null, sub-threshold, and materially degraded synthetic fixtures. It does not establish universal frequentist validity.

## Authorization sequence

Only if the finite synthetic suite passes all three validity gates may the rule be applied to the sealed historical OOF vectors.

Then:

```text
method contract
-> finite synthetic measurement-validity suite
-> D_method
-> AUTH(Gamma_cal_NI)
-> sealed historical successor adjudication
```

If the suite fails, `Gamma_t` remains governing and no historical calibration authority changes.

## Authority ceiling

Possible authority from this successor is limited to:

```text
local authorization of an uncertainty-bearing calibration-preservation rule
local successor adjudication of M1-cal vs M2-S Platt under that rule
```

It cannot by itself authorize:

```text
new calibrators
objective conditioning
broad H_O support/refutation
Z_E / Z_D / Z_C / Z_P
CCA, G1, PMC, JT, repeated-correction, or C_improve claims
```

No public leaderboard value enters any threshold, tolerance, bootstrap, or validity fixture.
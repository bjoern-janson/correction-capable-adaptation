# ECE uncertainty methodological successor — results

## Method validity

The prospectively frozen finite synthetic suite passed all declared gates:

```text
S0: delta = 0                     pass 10 / 10
S1: delta = 0.5 * epsilon_ECE     pass 10 / 10
S2: delta = 2.0 * epsilon_ECE     fail  9 / 10
```

Therefore the local method rule earns:

```text
AUTH(Gamma_cal_NI) = TRUE
```

for the declared finite-suite scope only.

This does not alter the historical deterministic ECE verdict. It authorizes a successor adjudication under the new rule.

## Historical successor adjudication

Sealed OOF objects:

```text
reference  M1-cal
candidate  M2-S Platt
rows       35,072
sessions   22,821
```

Point differences, candidate minus reference:

```text
Delta LL       -0.0324006054
Delta Brier    -0.0130501776
Delta ECE-10   +0.0009539310
Delta bias     -0.0002853314
```

Paired session-cluster 95% intervals:

```text
Delta LL       [-0.0346942278, -0.0299214574]
Delta Brier    [-0.0139800959, -0.0120194857]
Delta ECE-10   [-0.0032400811, +0.0050161782]
Delta bias     [-0.0012835725, +0.0007164329]
```

Inherited practical margins:

```text
epsilon_ECE    0.003997462025
epsilon_bias   0.002633982475
```

Frozen successor gates:

```text
G_LL          PASS
G_Brier       PASS
G_ECE_NI      FAIL
G_bias_NI     PASS
```

The ECE upper bound `0.0050161782` exceeds the predeclared practical margin `0.003997462025`.

Therefore:

```text
G_cal_NI historical successor     FAIL / UNRESOLVED
mature probability treatment      NOT AUTHORIZED
mature non-CCA baseline            UNCONSTITUTED
CCA-derived feature authority      FALSE
```

## Diagnosis

The methodological question is no longer whether a pointwise ECE increase should automatically veto the baseline. The new uncertainty-bearing rule is locally validated, but the current data do not identify ECE non-inferiority tightly enough at the inherited 25% practical margin.

The remaining calibration boundary is therefore **ECE precision / identification at the declared practical margin**, not calibrator search.

No equivalence claim is made from the interval crossing zero.

## Provenance

Local result record SHA-256:

```text
c20e8691dd01f0eace7fddfb06854f77b36baf23969803d4ac61cbddc8f4a12e
```

No public leaderboard value entered the target, practical tolerances, synthetic fixtures, or adjudication.
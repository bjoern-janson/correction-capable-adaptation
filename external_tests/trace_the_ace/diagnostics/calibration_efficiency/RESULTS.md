# ECE efficiency diagnostic V1 result

## Status

**CLOSED — METHOD-VALIDATION FIXTURE FAILURE — HISTORICAL OOF NOT ADJUDICATED**

The prospectively frozen paired session-cluster influence-function/sandwich candidate was not permitted to read the sealed historical OOF vectors because its synthetic method-validation suite failed.

## Frozen synthetic result

```text
regularity pass rate across regular scenarios   0.12
nonregular negative-control fail rate           1.00

coverage S0  1.00
coverage S1  0.16
coverage SB  0.19
coverage S2  0.17

NI pass S0   1.00
NI pass S1   1.00
NI pass SB   0.52
NI pass S2   0.00
```

Median interval widths for S1/SB were approximately numerical zero.

## Failure localization

The synthetic candidate probabilities were defined by a uniform additive shift from the reference. When bin residual signs remain fixed, the paired ECE difference under that construction can become algebraically deterministic even though outcomes are sampled, causing the influence-function difference to cancel and producing a near-zero interval width.

Therefore the failed coverage/NI behavior does not identify the historical ECE comparison and does not yet identify the influence-function estimator itself as the causal failure locus.

The shallowest implicated boundary is the **synthetic method-validation fixture**: it is not a sufficiently discriminating sampling-uncertainty challenge for the candidate interval method.

## Consequence

```text
historical OOF adjudication       FORBIDDEN / NOT RUN
D_efficiency                      UNRESOLVED
ECE precision boundary            OPEN
fixture successor                 AUTHORIZED
```

The authorized successor may repair only the synthetic validation fixture so that the true ECE difference is known but remains genuinely sample-dependent. It may not change the ECE-10 target, practical margin, historical OOF vectors, or candidate influence-function estimator.

## Authority ceiling

No authority is gained for mature calibration, `M_mature`, CCA, or any CCA-derived feature. The result only identifies a failure of the V1 method-validation apparatus.

Local full-record SHA-256:

```text
b5078957a9abc940de55df67e4b76faf0b21e0cbfb891ff256855838ca1b6f51
```

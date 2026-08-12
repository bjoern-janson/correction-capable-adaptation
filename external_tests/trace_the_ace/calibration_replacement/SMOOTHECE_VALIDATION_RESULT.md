# SmoothECE candidate validation result

## Status

**STOPPED AT `G_F` — candidate construct-fidelity gate failed**

The frozen validation order was obeyed:

```text
implementation equivalence  PASS
G_F                         FAIL
G_detect                    NOT RUN
G_U                         NOT RUN
G_decision                  NOT RUN
historical adjudication     NOT RUN
```

Historical M1-cal and M2-S prediction vectors were not read for this candidate.

## Geometry / provenance checks

The frozen label-free geometry was verified before `G_F`:

```text
index rows       35,072
sessions         22,821
index SHA-256    296399770b0818fa528f33382497bc7f4793b3c54a2e49e56e77efbc19d55c60
columns read     response_id, session_id only
labels read      no
```

All `F1..F6` population fixtures at construct targets `0.005`, `0.010`, and `0.020` passed the frozen bounds, injectivity, and exact-construct-magnitude constitution checks.

`F0` also passed:

```text
population SmoothECE  0.0
required maximum      0.0001
```

## `G_F` population results

SmoothECE values at construct-faithful `C_cal,L1` targets:

```text
family   theta@0.005      theta@0.010      theta@0.020
F1       0.00499999999    0.00999999997    0.01999999994
F2       0.00499919472    0.00999483995    0.01999008064
F3       0.00499810369    0.00998591723    0.01987341233
F4       0.00499999999    0.00999999887    0.01999932018
F5       0.00022612643    0.00052605116    0.00152171090
F6       0.00152703091    0.00373714782    0.00379765441
```

Every `F1..F6` family remained strictly positive and strictly ordered across the three declared construct magnitudes.

The decisive frozen local-retention checks at `C_cal,L1 = 0.010` were:

```text
F5 legacy-bin alternating
SmoothECE                0.0005260511578
retention ratio          0.0526051158
required minimum         0.10
result                   FAIL

F6 high-frequency local
SmoothECE                0.0037371478195
retention ratio          0.3737147820
required minimum         0.10
result                   PASS
```

Therefore:

```text
G_F = FAIL
```

because the gate is conjunctive and `F5` retains only about **5.26%** of the construct-faithful calibration deviation, below the prospectively frozen 10% minimum.

## Diagnosis

SmoothECE substantially improves local sensitivity relative to the predecessor ECE-10 failure on the declared alternating pathology, but under the exact frozen `F5` construction it still smooths away too much of the local calibration deviation to satisfy the candidate contract's minimum construct-fidelity requirement.

This is a **candidate construct-fidelity failure**, not an uncertainty failure, decision failure, historical calibration result, or evidence about CCA.

Per the frozen stop rule, no bandwidth tuning, fixture modification, threshold change, alternative interval, `G_detect`, `G_U`, `G_decision`, or historical adjudication is authorized inside this candidate.

## Authority

```text
AUTH(Gamma'_cal,smECE)             FALSE
SmoothECE replacement authority    FALSE
historical calibration closure     NOT TESTED
M_mature                            UNCONSTITUTED
AUTH(Z_E,Z_D,Z_C,Z_P)              FALSE
```

The result returns control to the candidate-neutral calibration replacement design envelope.

Local exact-result artifacts:

```text
implementation_equivalence.json SHA-256
791f9d9f75f06fb786a27a32cd5a76bebdd9f13beb6acc31ee1105627695979f

G_F.json SHA-256
2c249d5b692fce7641dcc038d40c79b32ab80e59b17666c82a65c23fedaa10d2

combined final.json SHA-256
0a80250e7bb6df9c2c35b3b71df1c3ba3449c39d506e8b3dd934f1e3a74b693a
```

Generated local result artifacts are not committed; only this result record, hashes, and authority ledger are committed.

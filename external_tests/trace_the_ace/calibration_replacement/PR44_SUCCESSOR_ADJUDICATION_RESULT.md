# PR #44 successor adjudication under authorized decision gate

## Status

**EXECUTED — NO EVIDENCE REGENERATION — LOCAL INFORMATION-QUANTITY SUPPORT EARNED**

This record applies the independently authorized `Gamma'_decision_gate` from PR #45 to the already-generated, frozen PR #44 information-scaling summaries. PR #44's original raw verdict remains immutable.

No synthetic outcomes were regenerated. No bootstrap draws were regenerated. Historical M1-cal/M2-S vectors were not read.

## Frozen inputs

```text
PR #44 head
8626826364fb31318750ba8c9f70866e524cb577

PR #44 final_partitioned.json SHA-256
788109fbec94649a9f7aa94d77a09c8b8141ef7b440fbb0e79e98838ff8807c7

Authorized PR #45 gate head
9ba62109641a33dc45103a3dec947a07cabfb79c

Successor adjudicator commit
caef3ab77c2faa35fad55b15fb81866a6c426445
```

The source artifact hash was verified before adjudication.

## Authorized successor semantics

`R=0` is analytically `STRUCTURALLY_DEGENERATE` under the frozen PR #44 oracle operator. In the frozen runner, `delta=0` implies every valid bootstrap `R_hat` value is exactly `0`, hence every valid interval endpoint is exactly `0`.

Therefore the successor cell requires:

```text
coverage == 1.00
AND inherited NI gate
AND inherited denominator gate
AND inherited invalid-bootstrap gate
```

For all nonzero `R` cells (`STOCHASTIC`):

```text
coverage >= 0.90
AND inherited NI gate
AND inherited denominator gate
AND inherited invalid-bootstrap gate
```

There is no stochastic upper-coverage failure cap under the authorized successor. Decision usefulness remains governed by the unchanged NI operating-characteristic gates.

## Successor pass topology

```text
m                     1      2      4      8      16
coarse successor      FAIL   PASS   PASS   PASS   PASS
fine successor        FAIL   FAIL   PASS   PASS   PASS
joint successor       FAIL   FAIL   PASS   PASS   PASS
```

Thus:

```text
m_min_decision_coarse = 2
m_min_decision_fine   = 4
m_min_decision_joint  = 4
n_min_decision_joint  = 140288 response-equivalents
sessions_joint        = 91284 independent session-clusters
```

The `m=2` fine sentinel still fails legitimately: the `R=0.125` stochastic cell has coverage `0.88` and NI pass rate `0.75`, both below their unchanged gates.

At `m=4`, every ratio cell at both sentinels satisfies the authorized successor gate. The same is true at `m=8` and `m=16`.

## Scientific diagnosis

The successor-adjudicated result is:

```text
D_additional_evidence = SUPPORTED_AS_INFORMATION_QUANTITY
```

within the declared local synthetic oracle regime.

Interpretation:

> Increasing genuinely independent information quantity is sufficient, within the frozen synthetic oracle regime, to make the unchanged 25% relative-NI decision identifiable. The smallest tested joint-passing information multiplier is `m=4`.

This establishes an information-quantity diagnosis only. It does **not** establish that four cohort-equivalents exist historically, are practically collectible, or are admissible for the Trace-the-Ace task.

Therefore the remaining live boundary is not `D_decision_object` merely because the current dataset is smaller. The next shallow question is evidence availability/admissibility: whether genuinely additional independent information of the required kind is available or can legitimately be acquired while preserving the scientific object.

## Historical preservation

PR #44 remains unchanged:

```text
raw D_additional_evidence = NOT_IDENTIFIED_WITHIN_GRID
raw authority             = WITHHELD_DUE_GATE_VALIDITY
```

This successor record does not rewrite that result. It adds a new authorized interpretation after PR #45 independently validated the corrected decision gate.

## Authority

Earned:

```text
D_additional_evidence = SUPPORTED_AS_INFORMATION_QUANTITY
scope = LOCAL_SYNTHETIC_ORACLE_INFORMATION_QUANTITY_ONLY
m_min_decision_joint = 4
n_min_decision_joint = 140288
sessions_min_decision_joint = 91284
```

Not earned:

```text
historical availability of additional evidence
replacement-measurement authority
AUTH(Gamma'_cal)
historical calibration closure
M_mature
Z_E / Z_D / Z_C / Z_P authority
```

## Provenance

```text
successor final.json SHA-256
233986a41afbec57164a270d94a0cf835d70e668d8002696b13b19c157198f45
```

Generated evidence was not touched. This is a pure successor adjudication over frozen PR #44 summaries under the independently authorized PR #45 gate.

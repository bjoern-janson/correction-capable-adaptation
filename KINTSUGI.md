# Kintsugi

> **Commit hard. Preserve lineage. Reopen on evidence.**

This document describes a repository-design discipline, not a new scientific primitive, metric, gate, or empirical claim.

Correction-Capable Adaptation treats its own history the way kintsugi treats a repaired vessel: **the fracture is not hidden, the repair is not mistaken for the original, and the object becomes more intelligible because its lineage remains visible.**

## The repository posture

\[
\boxed{\textbf{Local closure + global reopenability}}
\]

CCA needs enough closure to accumulate science and enough openness to remain correctable.

```text
PAST      preserve
PRESENT   commit
FUTURE    reopen on evidence
```

A result can be closed locally. A rule can be binding presently. A contract can be frozen for the identity of an experiment. None of those states grants permanent immunity from future discriminating evidence.

## The gold seam

The gold seam is **provenance**.

When the program changes its mind, the old state is not silently polished away. The repository should retain:

- what was believed or authorized;
- what evidence supported it;
- what failed or remained unresolved;
- what new evidence forced reopening;
- what changed;
- what did not change;
- what authority was gained, lost, narrowed, or transferred.

A scientific correction therefore creates a lineage:

\[
R_0\rightarrow R_1\rightarrow R_2\rightarrow\cdots
\]

not a rewritten past in which only the latest rule appears ever to have existed.

## Temporal asymmetry

CCA distinguishes four things that must not collapse:

| Object | Question |
| --- | --- |
| **Current authority** | What governs now? |
| **Provenance** | Why did it acquire authority? |
| **Revisability** | What evidence could legitimately displace it? |
| **Historical integrity** | Can we still reconstruct what governed, when, and why? |

The operating asymmetry is:

\[
\boxed{\textbf{Future authority is revisable; historical provenance is persistent.}}
\]

Persistent provenance does **not** mean historical interpretation is frozen. Later evidence may change what an old result means for the present. It may not silently change what was observed, decided, or executed under the old object identity.

## Frozen does not mean sacred

A frozen contract preserves the prospective identity of an empirical object.

A closed result preserves the historical outcome produced under that identity.

A canonical rule records current program authority.

None means "true forever."

\[
\boxed{\text{frozen contract}\neq\text{frozen research program}}
\]

\[
\boxed{\text{historical immutability}\neq\text{epistemic irreversibility}}
\]

If new evidence reaches an old assumption, CCA creates an explicit amendment, successor, descendant, or revised interpretation while preserving the ancestor.

## Repair discipline

The repository should make every important repair legible:

```text
observation
→ localization
→ competing explanations
→ discriminating evidence
→ minimal sufficient revision
→ retest
→ preserved lineage
→ current authority
```

The smallest sufficient failure locus retains priority.

\[
\boxed{\text{redescription}\neq\text{re-localization}}
\]

A deeper abstraction does not earn revision authority merely because it can subsume a shallower explanation. If the localized revision survives retest and no discriminating residual remains, escalation stops.

## What Kintsugi forbids

Kintsugi is incompatible with:

- deleting a negative result because a descendant works better;
- loosening an executed contract after seeing its outcome;
- presenting a successor experiment as though it were the original experiment repaired;
- erasing abandoned hypotheses from the lineage;
- converting a local result into broader authority without independent evidence;
- treating current canonical status as permanent truth;
- reopening a stable local result merely because a more elegant meta-description exists.

## What Kintsugi permits

Kintsugi explicitly permits:

- saying **we were wrong**;
- revising a canonical methodological rule;
- narrowing or expanding a claim when new evidence earns it;
- replacing a mechanism hypothesis;
- reconstituting a scientific object through a new prospective contract;
- creating descendants of closed failures;
- changing radically while preserving the record that makes the change intelligible.

## The research posture

Two commitments govern the aesthetic and the science:

\[
\boxed{\textbf{Maximum ambition; minimum unearned authority.}}
\]

\[
\boxed{\textbf{Nothing is authoritative enough to become immune to justified revision.}}
\]

The research question may be enormous. The licensed conclusion remains exactly as large as the evidence permits.

That is the repository's Kintsugi: **freedom to change without freedom to falsify the record of change.**

## Where this lives operationally

- [`CARS.md`](CARS.md) — localization, discrimination, minimal revision, stopping.
- [`methodology/RESEARCH_RETURNABILITY.md`](methodology/RESEARCH_RETURNABILITY.md) — reopening current authority without rewriting closed history.
- [`methodology/RESEARCH_STATE_MACHINE.md`](methodology/RESEARCH_STATE_MACHINE.md) — lifecycle and execution authority.
- [`lineage/EVIDENCE_LEDGER.md`](lineage/EVIDENCE_LEDGER.md) — the preserved evidence spine.
- [`research_state.json`](research_state.json) — machine-readable current authority.

The metaphor stops here. The scientific objects still have to earn their own measurement validity.
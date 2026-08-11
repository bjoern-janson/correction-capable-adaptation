# Lineage

> **The lineage is the gold seam.**

This directory is the provenance spine of Correction-Capable Adaptation.

CCA is allowed to change its mind. It is not allowed to manufacture a history in which it never changed its mind.

\[
\boxed{\textbf{Authority is revisable; provenance is persistent.}}
\]

## Why this exists

Scientific correction requires a stable record of:

- what object was actually under test;
- what evidence was available;
- what was concluded;
- what authority was gained;
- what authority was explicitly **not** gained;
- what failed;
- why a descendant object was opened;
- what later evidence changed the interpretation.

Without that lineage, correction and retrospective reconstruction become indistinguishable.

## The lineage rule

```text
ancestor object
→ prospective identity
→ observation / result
→ authority gained
→ authority not gained
→ diagnosis
→ closure or successor
→ preserved ancestor
```

A descendant may inherit a question, a failure boundary, or a validated local relation. It does **not** inherit authority the ancestor failed to earn.

A successor also does not overwrite the ancestor.

\[
\boxed{\text{successor}\neq\text{repaired ancestor}}
\]

## What remains immutable

A closed empirical result is immutable **as the historical result under its original identity and contract**.

That means the repository does not silently alter:

- the frozen intervention;
- the estimand;
- the estimator or analysis rule;
- the recorded observation;
- the result;
- the stopping condition;
- the fact that the result once carried whatever authority it actually carried.

Later science may change what that result means **now**. It may not change what happened **then**.

\[
\boxed{\text{historical immutability}\neq\text{epistemic irreversibility}}
\]

See [`../methodology/RESEARCH_RETURNABILITY.md`](../methodology/RESEARCH_RETURNABILITY.md).

## Canonical evidence ledger

[`EVIDENCE_LEDGER.md`](EVIDENCE_LEDGER.md) is the human-readable program ledger.

Each entry records:

| Field | Purpose |
| --- | --- |
| **Object** | What scientific object or methodological claim was actually examined? |
| **Status** | What lifecycle/authority state does it currently have? |
| **Observation** | What was actually established or observed? |
| **Authority gained** | What may later claims legitimately use? |
| **Authority not gained** | What tempting inference remains forbidden? |
| **Consequence** | Why did the program stop, revise, or open a descendant? |

The ledger is deliberately asymmetric: **authority gained** and **authority not gained** are equally important.

## Negative results are structure

CCA does not treat a negative result as failed documentation.

A clean negative result can establish:

- an impossibility boundary;
- a non-equivalence;
- a failed mechanism;
- a scope limit;
- an identification failure;
- a reason not to spend authority downstream.

The repository should therefore look repaired rather than pristine.

A visible scar is preferable to an invisible rescue.

## How to read a repair

When a later object changes the program, ask:

```text
What failed?
Where was the failure localized?
What evidence discriminated the alternatives?
What exactly changed?
What stayed fixed?
What old authority was withdrawn or narrowed?
What new authority was earned?
What ancestor remains inspectable?
```

If those questions cannot be answered from the lineage, the repair is not yet scientifically legible.

## Decision records

The [`decisions/`](decisions/) directory contains role-level and methodological decisions that currently govern the program.

`CANONICAL` means current authority, not permanent truth. If a decision is later reopened, the preferred pattern is:

```text
old decision preserved
→ new discriminating evidence / residual
→ explicit successor or amendment
→ changed current authority
```

not silent replacement.

## Repository Kintsugi

The broader repository-design discipline is documented in [`../KINTSUGI.md`](../KINTSUGI.md).

The compact posture is:

\[
\boxed{\textbf{Commit hard. Preserve lineage. Reopen on evidence.}}
\]

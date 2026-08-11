# Scientific Contracts

> **Experiments begin with a prospective scientific identity, not with code.**

A CCA contract defines what would count **before** observing whether it happens.

It exists to make a later result interpretable, falsifiable, and historically reconstructible.

## Governing documents

- [`../methodology/RESEARCH_STATE_MACHINE.md`](../methodology/RESEARCH_STATE_MACHINE.md) — lifecycle and authorization.
- [`../methodology/RESEARCH_RETURNABILITY.md`](../methodology/RESEARCH_RETURNABILITY.md) — how frozen objects remain scientifically reopenable through explicit successors without rewriting history.
- [`../research_state.json`](../research_state.json) — machine-readable current authority.
- [`EXPERIMENT_RECORD_TEMPLATE.md`](EXPERIMENT_RECORD_TEMPLATE.md) — contract record template.
- [`../KINTSUGI.md`](../KINTSUGI.md) — repository lineage discipline.

A contract may freeze only after the relevant scientific object has reached `MEASUREMENT_VALID`.

## Required order

```text
01  scientific object
02  causal path actually claimed
03  separable variables / transformations
04  identification or apparatus status of every required transformation
05  admissible intervention space
06  independent truth / warrant mapping where required
07  target and protected outcomes
08  admissible transformation class
09  prospective nulls and disconfirmation criteria
10  estimands and estimators
11  uncertainty and multiplicity
12  sample / randomization structure
13  authorization rule
14  implementation validation
15  execution
```

Statistical machinery may implement a scientific object. It may not define the object retroactively.

---

## What `CONTRACT_FROZEN` means

A frozen contract protects the **identity of one empirical object**.

It means that the prospective choices needed to interpret that experiment will not be silently changed after the outcome is observed.

\[
\boxed{\text{frozen contract}\neq\text{supported hypothesis}}
\]

It also does **not** mean the surrounding research program is frozen.

If later evidence establishes that a different estimand, intervention, threshold, measurement structure, or scientific object is needed, CCA opens an explicit successor or amendment and preserves the original contract in the lineage.

\[
\boxed{\text{frozen contract}\neq\text{frozen research program}}
\]

This is the Kintsugi rule for empirical identity: **repair the lineage; do not repaint the ancestor.**

---

## CCA causal composition principle

Every contract is subject to the current canonical rule:

> **A downstream causal claim may not inherit authority from an upstream validated relation across a separable transformation unless that transformation is independently identified, prospectively specified and validated as an apparatus guarantee, or explicitly excluded from the claim.**

\[
\boxed{\text{validated endpoints}\not\Rightarrow\text{validated pathway}}
\]

For every separable transformation crossed by the claim, the contract must record one of:

```text
INDEPENDENTLY_IDENTIFIED
VALIDATED_APPARATUS_GUARANTEE
NOT_CROSSED_BY_CLAIM
```

`VALIDATED_APPARATUS_GUARANTEE` requires prospective specification plus independent validation or mechanical verification over the claimed domain.

`NOT_CROSSED_BY_CLAIM` narrows the claim. It does not validate the edge.

Decision record: [`../lineage/decisions/CCA_CAUSAL_COMPOSITION_PRINCIPLE.md`](../lineage/decisions/CCA_CAUSAL_COMPOSITION_PRINCIPLE.md).

---

## Contract lifecycle

```text
PROPOSED
    ↓
ADVERSARIAL_REVIEW
    ↓
MEASUREMENT_VALID
    ↓
CONTRACT_FROZEN
    ↓
AUTHORIZED
    ↓
EXECUTED
    ↓
ANALYZED
    ↓
CLOSED
```

The states carry different kinds of authority:

| State | Meaning |
| --- | --- |
| `PROPOSED` | A candidate object exists. Nothing empirical follows. |
| `ADVERSARIAL_REVIEW` | The object is being attacked before implementation convenience can define it. |
| `MEASUREMENT_VALID` | The intended object is identifiable in principle under the declared measurement structure. |
| `CONTRACT_FROZEN` | The empirical object now has a stable prospective identity. |
| `AUTHORIZED` | Execution is explicitly permitted; truth is not implied. |
| `EXECUTED` | Outcome-bearing execution occurred, or implementation failure was recorded. |
| `ANALYZED` | Frozen analysis rules were applied. |
| `CLOSED` | The historical result is fixed under its original identity and stopping condition. |

A closed result can generate descendants. It cannot be repaired retrospectively under the same identity.

---

## Contract template

Every empirical contract should make the following reconstructible.

### Status

```text
OBJECT_ID
PROGRAM_LEVEL
LIFECYCLE_STATE
MEASUREMENT_STATE
CONTRACT_STATE
EXECUTION_STATE
IMPLEMENTATION_AUTHORIZED
```

### Scientific proposition

What proposition is actually under test?

### Causal path and separability

What object-level causal path does the claim assert? Which transformations are treated as separable? What warrants crossing each one?

### Measurement structure

What observations constitute the scientific object? Which transformations preserve its identity?

### Intervention

What can vary under `do(·)`? What is held fixed or matched?

### Estimand

What causal or descriptive quantity is to be recovered?

### Disconfirmation

What evidence would count against the object, mechanism, or claimed relation?

### Protected structure

What must remain unchanged, and under what prospectively fixed tolerance or equivalence relation?

### Failure validity

Which implementation defects make the scientific object `UNOBSERVED/INVALID` rather than scientifically zero?

### Authorization

What exact conjunction of results and path-validity conditions permits the next claim or execution step?

---

## No compensatory scoring

Where several causal prerequisites are required, authorization is conjunctive.

For an end-to-end path \(\pi\):

\[
\mathrm{ADVANCE}_{\pi}
\iff
\left(\bigwedge_k G_k\right)
\land
\mathrm{PathValid}(\pi)
\]

A strong downstream score cannot compensate for a failed upstream prerequisite or an unvalidated separable transformation.

---

## Implementation gate

A contract directory, available compute, an open issue, a model, or a plausible benchmark does not authorize empirical implementation.

Before execution work, check [`../research_state.json`](../research_state.json).

If the measurement object is unresolved, the contract remains unfrozen, or a required causal transformation lacks authority, implementation must not make those scientific decisions implicitly through code, prompts, data, or apparatus convenience.

\[
\boxed{\textbf{Maximum ambition; minimum unearned authority.}}
\]

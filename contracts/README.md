# Scientific Contracts

Experiments in this program begin with a **prospective scientific contract**, not code.

The contract must define what would count before observing whether it happens.

Contract work is governed by:

- [`../methodology/RESEARCH_STATE_MACHINE.md`](../methodology/RESEARCH_STATE_MACHINE.md)
- [`../research_state.json`](../research_state.json)
- [`EXPERIMENT_RECORD_TEMPLATE.md`](EXPERIMENT_RECORD_TEMPLATE.md)

A contract may freeze only after the relevant scientific object has reached `MEASUREMENT_VALID`.

## Required order

```text
1. scientific object
2. causal path actually claimed
3. separable variables / transformations in that path
4. identification or validated-apparatus status of each required transformation
5. admissible intervention space
6. independent truth / warrant mapping where required
7. target and protected outcomes
8. admissible transformation class
9. prospective nulls and disconfirmation criteria
10. estimands and estimators
11. uncertainty and multiplicity
12. sample / randomization structure
13. authorization rule
14. implementation validation
15. execution
```

Statistical machinery may implement the scientific object. It may not define the object retroactively.

## CCA Causal Composition Principle

Every contract is subject to the canonical rule:

> **A downstream causal claim may not inherit authority from an upstream validated relation across a separable transformation unless that transformation is independently identified, prospectively specified and validated as an apparatus guarantee, or explicitly excluded from the claim.**

Thus:

\[
\boxed{\text{validated endpoints}\not\Rightarrow\text{validated pathway}.}
\]

A contract must make the causal path reconstructible. For each separable transformation the claim crosses, it must record one of:

```text
INDEPENDENTLY_IDENTIFIED
VALIDATED_APPARATUS_GUARANTEE
NOT_CROSSED_BY_CLAIM
```

`VALIDATED_APPARATUS_GUARANTEE` requires prospective specification plus independent validation or mechanical verification over the claimed domain. Merely declaring a deterministic mapping is insufficient.

If a transformation is `NOT_CROSSED_BY_CLAIM`, the claim must stop before that transformation. Exclusion narrows the claim; it does not validate the edge.

Canonical decision: [`../lineage/decisions/CCA_CAUSAL_COMPOSITION_PRINCIPLE.md`](../lineage/decisions/CCA_CAUSAL_COMPOSITION_PRINCIPLE.md).

## Contract lifecycle

A typical empirical object should move through:

```text
PROPOSED
→ ADVERSARIAL_REVIEW
→ MEASUREMENT_VALID
→ CONTRACT_FROZEN
→ AUTHORIZED
→ EXECUTED
→ ANALYZED
→ CLOSED
```

`CONTRACT_FROZEN` does not mean the hypothesis is supported. It means the experiment has a prospective identity stable enough to execute without outcome-dependent redefinition.

`AUTHORIZED` is a separate state. It requires both the frozen contract and satisfaction of the program's upstream dependencies.

## Contract template

Every future contract should state:

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

What object-level causal path does the claim assert? Which nodes/transformations are prospectively treated as separable?

For every separable transformation crossed by the claim, what warrants authority to propagate across it?

### Measurement structure

What observations constitute the object? What transformations preserve its identity?

### Intervention

What can vary under `do(·)` and what is matched?

### Estimand

What causal or descriptive quantity is to be recovered?

### Disconfirmation

What evidence would count against the proposed mechanism?

### Protected structure

What must remain unchanged, and within what prospectively fixed tolerance?

### Failure validity

Which implementation defects make the scientific object `UNOBSERVED/INVALID` rather than zero or failed?

### Authorization

What exact conjunction of results and path-validity conditions permits the next experimental claim?

## No compensatory scoring

Where several causal prerequisites are required, authorization is conjunctive.

For an end-to-end path \(\pi\), the generic form is:

\[
\mathrm{ADVANCE}_{\pi}
\iff
\left(\bigwedge_k G_k\right)
\land
\mathrm{PathValid}(\pi).
\]

A strong downstream score cannot compensate for failure of a required upstream mechanism or an unvalidated separable transformation.

## Implementation gate

Empirical implementation for execution is not authorized merely because a contract directory exists.

The relevant object must satisfy the machine-readable authorization requirements in `research_state.json`.

If the measurement object is unresolved, the contract remains unfrozen, or a claimed separable transformation lacks the required status, implementation work must not choose those scientific decisions implicitly through benchmark, model, prompt, data, or apparatus convenience.

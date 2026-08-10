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
2. admissible intervention space
3. independent truth / warrant mapping where required
4. target and protected outcomes
5. admissible transformation class
6. prospective nulls and disconfirmation criteria
7. estimands and estimators
8. uncertainty and multiplicity
9. sample / randomization structure
10. authorization rule
11. implementation validation
12. execution
```

Statistical machinery may implement the scientific object. It may not define the object retroactively.

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

What exact conjunction of results permits the next experimental gate?

## No compensatory scoring

Where several causal prerequisites are required, the default authorization form is conjunctive:

\[
\mathrm{ADVANCE}\iff G_1\land G_2\land\cdots\land G_k.
\]

A strong downstream score cannot compensate for failure of a required upstream mechanism.

## Implementation gate

Empirical implementation for execution is not authorized merely because a contract directory exists.

The relevant object must satisfy the machine-readable authorization requirements in `research_state.json`.

If the measurement object is unresolved or the contract remains unfrozen, implementation work must not choose those scientific decisions implicitly through benchmark, model, prompt, or data convenience.

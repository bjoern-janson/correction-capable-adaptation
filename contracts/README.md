# Scientific Contracts

Experiments in this program begin with a **prospective scientific contract**, not code.

The contract must define what would count before observing whether it happens.

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

## Contract template

Every future contract should state:

### Status

```text
DRAFT / FROZEN / CLOSED
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

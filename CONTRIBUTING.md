# Contributing

Contributions are welcome when they improve scientific clarity, falsifiability, measurement validity, provenance, or public reproducibility.

Before proposing empirical implementation, read:

- [`RESEARCH_STATE.md`](RESEARCH_STATE.md)
- [`research_state.json`](research_state.json)
- [`methodology/RESEARCH_STATE_MACHINE.md`](methodology/RESEARCH_STATE_MACHINE.md)
- [`lineage/EVIDENCE_LEDGER.md`](lineage/EVIDENCE_LEDGER.md)

## Highest-value contributions

Good contributions typically do one of the following:

- identify a hidden confound or non-identifiability problem;
- construct a counterexample to a proposed measurement or mechanism;
- improve a prospective contract before outcomes are observed;
- provide independent validation of an already frozen object;
- improve public explanations without strengthening the scientific claim;
- add provenance that makes a result easier to reconstruct;
- make the research authority state harder to violate accidentally.

## Scientific discipline

Please preserve these rules:

```text
negative result ≠ failed project
surprise ≠ identified mechanism
selection variation ≠ warranted evidence use
non-significance ≠ preservation
capability improvement ≠ justified adaptation
ASI-0 ≠ ASI evidence
```

Do not rescue a closed experiment by altering its estimand, gate, model, or interpretation after the outcome.

A new idea motivated by a failure should normally be proposed as a **new prospective object**.

## Research maturity and lifecycle

Every empirical proposal must declare both:

1. its **maturity level** in the program ladder; and
2. its **lifecycle state**.

Maturity levels:

```text
0 measurement validity
1 evidence-controlled selection
2 isolated modification
3 evidence → justified modification
4 repeated correction
5 justified transformability
6 adaptive viability / capability
7 extreme adaptive systems
```

Lifecycle:

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

Downstream work is blocked by unresolved upstream prerequisites.

## Implementation authorization

The existence of an idea, issue, benchmark, directory, model, or available compute does **not** authorize empirical implementation.

For an empirical experiment to be implemented for execution, its machine-readable state must satisfy the authorization requirements in `research_state.json`.

At minimum:

```text
measurement_state = MEASUREMENT_VALID or later
contract_state    = CONTRACT_FROZEN or later
execution_state   = AUTHORIZED
implementation_authorized = true
```

If those conditions are not met, implementation contributions must be restricted to non-scientific scaffolding that cannot select the unresolved scientific object implicitly.

## Current frontier

The active unresolved question is measurement-level:

\[
G_1^{\mathrm{broad}}
\quad\text{vs.}\quad
G_1^{\mathrm{relational}}.
\]

Contributions that clarify this fork, produce impossibility/existence results, or sharpen the measurement object are more useful right now than model, prompt, or benchmark implementations.

## Pull requests

A pull request must state:

1. **Scientific object:** what object or communication problem does this address?
2. **Maturity level:** which program gate does it belong to?
3. **Lifecycle state:** what state is the object in before and after this PR?
4. **Authority change:** what authority, if any, does this PR claim to change?
5. **Nonclaims:** what remains explicitly unauthorized?
6. **Frozen-object impact:** does it alter a frozen or closed object? If yes, why is that scientifically legitimate?
7. **Validation:** how was the change checked?

A PR must not silently advance a lifecycle state. State transitions require evidence or contract completion appropriate to the transition.

Small, auditable changes are preferred to large narrative rewrites.

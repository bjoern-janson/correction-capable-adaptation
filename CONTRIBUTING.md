# Contributing

> **Maximum ambition; minimum unearned authority.**

Contributions are welcome when they improve scientific clarity, falsifiability, measurement validity, provenance, public reproducibility, or the program's ability to remain corrigible without rewriting its history.

CCA prefers **small, auditable scientific repairs** over large narrative rewrites that silently change object identity.

## Before contributing

Read the current authority surfaces first:

- [`README.md`](README.md) — program map.
- [`RESEARCH_STATE.md`](RESEARCH_STATE.md) — human-readable current state.
- [`research_state.json`](research_state.json) — machine-readable authority and implementation policy.
- [`CARS.md`](CARS.md) — localization, discrimination, minimal revision, stopping.
- [`methodology/README.md`](methodology/README.md) — methodology map.
- [`methodology/RESEARCH_STATE_MACHINE.md`](methodology/RESEARCH_STATE_MACHINE.md) — lifecycle and execution authority.
- [`methodology/RESEARCH_RETURNABILITY.md`](methodology/RESEARCH_RETURNABILITY.md) — reopening without historical rewriting.
- [`lineage/EVIDENCE_LEDGER.md`](lineage/EVIDENCE_LEDGER.md) — what has and has not actually been established.
- [`KINTSUGI.md`](KINTSUGI.md) — repository lineage discipline.

## Highest-value contributions

Good contributions typically do one of the following:

- identify a hidden confound, collapsed distinction, or non-identifiability problem;
- construct a counterexample to a proposed measurement, mechanism, or conceptual equivalence;
- improve a prospective scientific contract before outcomes are observed;
- provide independent validation of an already constituted relation;
- sharpen a scientific object without making it larger than the evidence permits;
- improve public explanation **without strengthening the scientific claim**;
- repair provenance or navigation so a result is easier to reconstruct;
- make accidental authority leakage or unauthorized implementation harder;
- identify stale documentation that no longer matches `research_state.json`.

## Scientific discipline

Preserve these non-substitutions:

```text
negative result                ≠ failed project
surprise                       ≠ identified mechanism
selection variation            ≠ warranted evidence use
non-significance               ≠ preservation
current performance            ≠ post-modification correctability
one realized correction        ≠ broad correction capacity
repeated correction            ≠ justified transformability
many reachable states          ≠ warranted transformation repertoire
capability improvement         ≠ justified adaptation
available compute              ≠ authorization
historical immutability        ≠ epistemic irreversibility
reopenability                  ≠ permission to rewrite a closed result
```

Do not rescue a closed experiment by altering its estimand, gate, model, intervention, measurement structure, or interpretation after seeing the outcome.

A new idea motivated by failure should normally become an explicit **descendant, amendment, or successor object** with preserved provenance.

\[
\boxed{\text{redescription}\neq\text{re-localization}}
\]

A deeper abstraction has no revision authority merely because it subsumes a successful local explanation.

## Research maturity

CCA's current evidence-ordering ladder is:

```text
0   measurement / scientific-object validity
1   evidence-controlled adaptive decision
2   isolated modification
3   evidence → justified modification
4A  post-modification correctability
4B  repeated correction
5   justified transformability
6   adaptive viability / capability
7   extreme adaptive-system stress tests
```

The ladder is an evidence-ordering discipline, not automatically a universal decomposition of adaptive systems.

## Lifecycle

Every empirical object moves through an explicit lifecycle:

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

These states are not interchangeable.

- `CONTRACT_FROZEN` preserves the identity of one prospective empirical object.
- `AUTHORIZED` permits execution; it does not imply truth.
- `CLOSED` preserves the historical result under its original identity.
- all current conceptual and methodological authority remains reopenable under new discriminating evidence through the research-returnability rule.

## Implementation authorization

The existence of an idea, issue, benchmark, directory, model, available compute, or attractive theory does **not** authorize empirical implementation.

Before execution work, check [`research_state.json`](research_state.json).

At minimum, the relevant empirical object must satisfy the machine-readable authorization requirements, including:

```text
measurement_state = MEASUREMENT_VALID or later
contract_state    = CONTRACT_FROZEN or later
execution_state   = AUTHORIZED
implementation_authorized = true
```

If those conditions are not met, implementation must not choose unresolved scientific decisions implicitly through benchmark, model, prompt, data, or apparatus convenience.

## Current frontier

### Empirical authority frontier

G1 remains **empirically untested** and contract-unfrozen:

\[
\boxed{G_1=\text{warranted evidence acquiring causal control over a separable adaptive decision}}
\]

No empirical G1 execution is authorized.

### Conceptual frontier

The active conceptual question is Justified Transformability:

> **Can the warrant, distinctness, repertoire, preservation, target-family, and counterfactual-availability semantics of JT be specified without retrospective approval, trivial-difference inflation, or benchmark-defined reachability?**

Contributions should treat this as a scientific-object problem. A compelling JT definition does not authorize a JT benchmark or implementation.

## Pull requests

A research PR should make its scientific effect auditable.

Include:

1. **Scientific object** — what object, distinction, or communication problem does this address?
2. **Maturity level** — where does it sit in the evidence-ordering ladder?
3. **Lifecycle state** — what is the object's state before and after the PR?
4. **Failure locus** — if this is a correction, what is the shallowest sufficient localization?
5. **Discriminating evidence** — what warrants the change rather than merely redescribing the problem?
6. **Authority change** — what authority is gained, withdrawn, narrowed, or transferred?
7. **Nonclaims** — what remains explicitly unsupported or unauthorized?
8. **Lineage impact** — what ancestor or previous decision remains preserved?
9. **Execution impact** — does anything become implementable or executable? If not, say so explicitly.
10. **Validation** — how was the change checked?

A PR must not silently advance a lifecycle state.

## Kintsugi rule

A good contribution leaves the repository easier to understand **because the repair is visible**.

```text
old state preserved
→ reason for reopening visible
→ repair explicit
→ new authority scoped
→ history still reconstructible
```

\[
\boxed{\textbf{Commit hard. Preserve lineage. Reopen on evidence.}}
\]

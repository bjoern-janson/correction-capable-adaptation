# Correction-Capable Adaptation

**A research program on whether adaptive systems can become appropriately different without losing their capacity for justified correction.**

> We study whether adaptive systems can incorporate justified correction, produce effective change, preserve protected structure, and retain the capacity for further correction—and whether this capacity helps explain increasingly viable adaptation and capability.

## Core rule

> **Never infer a downstream capability from an unvalidated upstream mechanism.**

The program is organized as a dependency graph rather than a collection of independent projects:

```text
MEASUREMENT
Can the scientific object be identified?
    ↓
SELECTION
Does evidence control warranted choice?
    ↓
MODIFICATION
Does the modification cause the intended effect
without unacceptable protected interference?
    ↓
REPEATED CORRECTION
Does correction remain possible across repeated changes?
    ↓
CORRECTION CAPACITY
Does that capacity persist or improve?
    ↓
JUSTIFIED TRANSFORMABILITY
Can the system remain open to warranted future change?
    ↓
ADAPTIVE VIABILITY
Does this preserve or expand viable futures?
    ↓
CAPABILITY
Does capability grow under those constraints?
    ↓
ASI STRESS TEST
What happens at an extreme-capability regime?
```

A failed upstream gate blocks authority downstream. Progress is therefore **not an average score**. The current frontier is the first unresolved causal prerequisite.

## Current frontier

The active scientific question is still at the **measurement layer**:

\[
G_1^{\mathrm{broad}}
\quad\text{vs.}\quad
G_1^{\mathrm{relational}}.
\]

Should evidence use mean any warranted information carried by evidence, or specifically dependence on the demonstrated input-output relation beyond licensed non-relational channels?

That decision must be made before selecting the descendant ontology or constructing the next intervention space.

## One lineage

```text
ancestral empirical work
        ↓
ASI-0
        ↓
negative primary result
        ↓
mechanism diagnosis
        ↓
ECIM-like descendant architecture
        ↓
measurement frontier
        ↓
future gates only when earned
```

ASI-0 remains an immutable ancestor. It is **not** an ASI experiment and is not repaired retrospectively.

## Current evidence snapshot

ASI-0 produced the frozen result:

\[
\boxed{C=0,\qquad A=0,\qquad \mathrm{STOP}}
\]

where

\[
C=E[Y_{\mathrm{aligned}}-Y_{\mathrm{base}}],
\qquad
A=E[Y_{\mathrm{aligned}}-Y_{\mathrm{misaligned}}].
\]

The post-outcome diagnosis found two scoped bottlenecks under that frozen setup:

1. **Inference:** assigned evidence had weak control over candidate identity.
2. **Modification isolation:** 15 of 16 frozen textual patches failed to preserve baseline protected behavior.

The acceptance gate functioned as designed and rejected all 28 valid selected patches. Those observations motivate a new prospective object; they do not alter ASI-0.

## Theory and method

- **[CARS](CARS.md)** — the evidence-handling and research-correction protocol: localize, discriminate, revise minimally, retest, preserve provenance, and stop when authority is exhausted.
- **[MAGIKARP](MAGIKARP.md)** — a provisional theory layer for asking what makes one adaptive transformation more justified than another. It is not yet an empirically validated construct.
- **[Scientific object](SCIENTIFIC_OBJECT.md)** — the program-level causal dependency graph and claim boundaries.
- **[Research state](RESEARCH_STATE.md)** — the current frontier and authorization state.
- **[Evidence ledger](lineage/EVIDENCE_LEDGER.md)** — one canonical record of what has and has not been established.

## Repository map

```text
.
├── README.md
├── MISSION.md
├── SCIENTIFIC_OBJECT.md
├── RESEARCH_STATE.md
├── CARS.md
├── MAGIKARP.md
├── contracts/
├── experiments/
│   ├── ASI-0/
│   └── ECIM/
├── measurement/
└── lineage/
```

This repository is the public research program. Detailed implementation archaeology and exploratory branch history are intentionally not reproduced here.

## Public-research standard

Every empirical claim should make reconstructible:

```text
scientific object
measurement structure
prospective contract
intervention / assignment process
estimator
uncertainty procedure
protocol deviations
result actually observed
claim actually earned
what remains unauthorized
```

Negative and null results remain first-class evidence.

## Ultimate question

\[
\boxed{\textbf{Can increasing adaptive power preserve the ability to be corrected?}}
\]

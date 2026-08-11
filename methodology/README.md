# Methodology

This directory contains the rules that let Correction-Capable Adaptation change without losing scientific identity.

> **Current authority may be revised. Historical provenance may not be silently rewritten.**

## Start here

| Document | Role |
| --- | --- |
| [`../CARS.md`](../CARS.md) | How contradictions are localized, discriminated, revised, and retested. |
| [`RESEARCH_RETURNABILITY.md`](RESEARCH_RETURNABILITY.md) | How current authority can reopen under new evidence while closed historical results remain intact. |
| [`RESEARCH_STATE_MACHINE.md`](RESEARCH_STATE_MACHINE.md) | The lifecycle from proposal through authorization, execution, analysis, and closure. |
| [`../contracts/README.md`](../contracts/README.md) | How prospective scientific contracts are constituted before execution. |
| [`../research_state.json`](../research_state.json) | Machine-readable current authority and implementation guardrails. |
| [`../KINTSUGI.md`](../KINTSUGI.md) | Repository-design interpretation: visible repairs, persistent lineage, global reopenability. |

## Operational flow

```text
OBSERVE
  ↓
LOCALIZE
  ↓
DISCRIMINATE
  ↓
REVISE THE SMALLEST SUFFICIENT BOUNDARY
  ↓
RETEST
  ↓
NO RESIDUAL? ── yes ─→ COMMIT CURRENT AUTHORITY
  │
  no
  ↓
REOPEN THE NEXT EVIDENCE-IMPLICATED BOUNDARY
```

The stopping rule matters as much as the reopening rule:

\[
\boxed{r=0\Rightarrow\text{no deeper opening is currently warranted}}
\]

## Authority states are not truth states

CCA uses words such as `CANONICAL`, `PROVISIONALLY_FIXED`, `MEASUREMENT_VALID`, `CONTRACT_FROZEN`, and `CLOSED` to record **what currently carries authority and under what identity**.

They do not all mean the same thing.

| State | What it protects | What remains reopenable |
| --- | --- | --- |
| **CANONICAL** | Current methodological/conceptual authority | The rule itself, under new discriminating evidence |
| **PROVISIONALLY_FIXED** | Current scientific role or boundary | The role, if evidence reaches it |
| **MEASUREMENT_VALID** | Current identification contract | Measurement theory through an explicit successor/amendment |
| **CONTRACT_FROZEN** | Prospective identity of one empirical object | The surrounding program; a successor contract |
| **CLOSED** | Historical result under its original identity | Interpretation, scope, descendants, theory—not the recorded result |

## Two hard asymmetries

### Local closure, global reopenability

A local inquiry ends when the discriminating residual is exhausted. The research program remains permanently open to later evidence.

### Mutable authority, persistent lineage

A rule may stop governing. That does not erase the fact that it governed.

```text
past      preserve
present   commit
future    reopen on evidence
```

## Before empirical implementation

No empirical implementation follows from conceptual coherence alone.

An automated or human implementation path must check [`../research_state.json`](../research_state.json) and verify that the relevant object has the required measurement, contract, authorization, and implementation states.

Available compute, a plausible benchmark, an open issue, or a compelling theory does not authorize execution.

## Methodological posture

\[
\boxed{\textbf{Maximum ambition; minimum unearned authority.}}
\]

CCA can ask very large questions while keeping every individual inference local, scoped, and provenance-preserving.
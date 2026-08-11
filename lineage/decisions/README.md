# Decision Lineage

This directory contains the program's current role-level and methodological decisions.

A decision record is not a declaration of permanent truth. It is a provenance-bearing statement of **what currently carries authority, why, and what remains outside that authority**.

\[
\boxed{\textbf{Current authority may change; the fact that it once governed remains inspectable.}}
\]

## Current decision spine

| Decision | Current role | Reopenability |
| --- | --- | --- |
| [`RESEARCH_RETURNABILITY_RULE.md`](RESEARCH_RETURNABILITY_RULE.md) | Canonical rule for local closure plus global reopenability without rewriting closed results or contracts | Reopenable under new discriminating evidence |
| [`G1_LEVEL0_ROLE.md`](G1_LEVEL0_ROLE.md) | Scoped role for warranted evidence acquiring causal control over a separable adaptive decision | Reopenable under new discriminating evidence |
| [`CCA_CAUSAL_COMPOSITION_PRINCIPLE.md`](CCA_CAUSAL_COMPOSITION_PRINCIPLE.md) | Current canonical causal-composition rule | Reopenable under research returnability |
| [`POST_MODIFICATION_CORRECTABILITY_ROLE.md`](POST_MODIFICATION_CORRECTABILITY_ROLE.md) | Provisional role for Post-Modification Correctability | Reopenable |
| [`PMC_REPEATED_CORRECTION_DISTINCTION.md`](PMC_REPEATED_CORRECTION_DISTINCTION.md) | Current conceptual distinction between latent availability and realized exercise | Reopenable |
| [`JUSTIFIED_TRANSFORMABILITY_ROLE.md`](JUSTIFIED_TRANSFORMABILITY_ROLE.md) | Provisional repertoire-level role for Justified Transformability | Reopenable; semantics under review |

## How a decision changes

A decision should not be silently edited so that its original authority state disappears from the lineage.

When new evidence genuinely reaches the decision:

```text
current decision
→ discriminating evidence / surviving residual
→ shallowest sufficient localization
→ explicit amendment or successor
→ changed current authority
→ preserved ancestor
```

The new record should state:

- what evidence triggered reopening;
- which part of the previous decision failed or became insufficient;
- what remains valid;
- what authority is withdrawn, narrowed, or added;
- which downstream claims require retesting.

Mere elegance, broader abstraction, or a desire for consistency does not justify reopening a stable decision.

## Related documents

- [`../EVIDENCE_LEDGER.md`](../EVIDENCE_LEDGER.md) — evidence and authority ledger.
- [`../../methodology/RESEARCH_RETURNABILITY.md`](../../methodology/RESEARCH_RETURNABILITY.md) — reopening discipline.
- [`../../KINTSUGI.md`](../../KINTSUGI.md) — repository lineage philosophy.
- [`../../research_state.json`](../../research_state.json) — machine-readable current authority.

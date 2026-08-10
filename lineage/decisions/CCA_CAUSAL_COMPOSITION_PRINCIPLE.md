# Decision: CCA Causal Composition Principle

## Status

**CANONICAL METHODOLOGICAL PRINCIPLE — NO NEW GATE — NO EMPIRICAL RESULT — NO EXECUTION AUTHORIZED**

## Decision

Correction-Capable Adaptation adopts the following causal-composition principle:

\[
\boxed{\textbf{CCA Causal Composition Principle}}
\]

> **A downstream causal claim may not inherit authority from an upstream validated relation across a separable transformation unless that transformation is independently identified, prospectively specified and validated as an apparatus guarantee, or explicitly excluded from the claim.**

Compactly:

\[
\boxed{\text{validated endpoints}\not\Rightarrow\text{validated pathway}.}
\]

And equivalently:

\[
\boxed{\text{No causal authority may be propagated across an unvalidated separable transformation.}}
\]

## Why this is a composition law rather than a new gate

The principle does not require every correction-capable architecture to contain the same intermediate variables.

A separable architecture may factor as:

\[
E\rightarrow C\rightarrow D\rightarrow M\rightarrow Y.
\]

A direct-update architecture may instead use:

\[
E\rightarrow M\rightarrow Y.
\]

An inseparable architecture may contain an atomic adaptive transition \(U\) for which selection and modification are not independently manipulable.

Therefore CCA does **not** introduce a universal `G1.5`, adoption variable, or selection-to-modification gate.

The identification obligation is conditional on the decomposition actually claimed.

## Path-validity rule

For a claimed causal path \(\pi\), let \(\mathrm{Sep}(\pi)\) denote the transformations represented as causally separable in the prospective scientific contract.

A path claim is authorized only when every separable transformation crossed by the claim has warranted status:

\[
\boxed{
\mathrm{PathValid}(\pi)
\Rightarrow
\bigwedge_{\ell\in\mathrm{Sep}(\pi)} W(\ell)
}
\]

where \(W(\ell)\) means either:

1. the transformation is independently causally identified; or
2. the transformation is fixed by a prospectively specified, independently validated/verified apparatus relation within the claim's scope.

If a separable transformation is left unvalidated, the scientific claim must stop before crossing it. "Explicitly excluded from the claim" narrows the claim; it does not validate the edge.

## Apparatus guarantees

A deterministic or externally controlled relation is not automatically warranted merely because it is called apparatus.

If an experiment relies on:

\[
M=\phi(C),
\]

as experimental plumbing, then \(\phi\) must be prospectively specified and validated or mechanically verified for the relevant domain.

An externally guaranteed bridge can support an end-to-end experimental claim about the apparatus-mediated pathway. It does **not** establish that the adaptive system itself possesses adoption, translation, or deployment competence.

Thus:

\[
\boxed{
\text{apparatus-mediated composition}
\neq
\text{system-internal bridge competence}.
}
\]

## Consequence for G1 and G2

CCA currently uses:

\[
\boxed{
G_1=
\text{warranted evidence acquiring causal control over a separable adaptive decision}
}
\]

and independently:

\[
\boxed{
G_2:\ do(M=m)\rightarrow(Y_T,Y_P).
}
\]

Neither gate supplies the missing causal relations between its own identified relation and the other gate.

Therefore:

\[
\boxed{
G_1>0\land G_2>0
\not\Rightarrow
\text{a connected evidence-to-modification pathway}.
}
\]

For the current candidate-selection decomposition, if the claim crosses a separable transition such as:

\[
C_{\mathrm{selected}}\rightarrow D_{\mathrm{adopt}}\rightarrow M,
\]

that transition must satisfy the composition principle before CCA may claim:

\[
E\rightarrow C^*(E)\rightarrow M\rightarrow Y.
\]

This does not make the bridge a universal CCA level.

## Level-3 consequence

The previous shorthand

\[
\mathrm{ADVANCE}\iff G_1\land G_{2T}\land G_{2P}
\]

is insufficient for an end-to-end claim whenever the chosen architecture contains additional separable transformations between the decision identified by `G1` and the modification identified by `G2`.

For a claimed end-to-end path \(\pi\), the correct authorization structure is:

\[
\boxed{
\mathrm{ADVANCE}_{\pi}
\iff
G_1
\land
\mathrm{PathValid}(\pi)
\land
G_{2T}
\land
G_{2P}
}
\]

where `PathValid` does not double-count the `G1` or `G2` relations themselves; it covers the additional separable transformations required to compose them into the claimed pathway.

No scalar bridge estimand or named bridge gate is fixed by this rule.

## Relation to CARS

CARS already requires that evidence increase authority only along dimensions it can identify and that failure not be mistaken for its cause.

The composition principle is the causal-architecture counterpart:

> **Endpoint validity does not validate an intervening pathway.**

This prevents authority laundering across hidden rejection, mistranslation, independent control, deployment, translation, or other unvalidated transformations.

## Provenance

The principle is supported by the attack sequence:

```text
PR #9   causal semantics of the G1-to-G2 bridge
PR #10  architecture-independent necessity of a bridge
```

PR #9 established that `G1 -> G2` is shorthand rather than a literal causal edge and that successful endpoint assays do not identify a missing middle relation.

PR #10 established that explicit bridge variables are architecture-conditional: necessary for some separable decompositions, unnecessary for direct-update decompositions, and potentially malformed for inseparable decompositions.

The attack artifacts remain provenance rather than canonical empirical results.

## Authority gained

CCA may now enforce the following methodological rule across the entire program:

> **Every separable transformation crossed by a causal claim must carry its own warranted authority or a prospectively validated apparatus guarantee; otherwise the claim must stop before that transformation.**

This rule applies beyond G1/G2 to any future decomposition used in correction, repeated correction, transformability, viability, or extreme-system stress tests.

## Authority not gained

This decision does not establish:

- a positive G1 result;
- a positive G2 result;
- a selection-to-modification bridge;
- a universal adoption or translation variable;
- a named intermediate gate;
- a valid ECIM experiment;
- repeated correction;
- preservation of correction capacity after modification;
- justified transformability;
- adaptive viability;
- implementation or execution authorization.

## Next scientific frontier

The next program-level conceptual frontier is no longer whether CCA must invent a universal intermediate gate.

It is:

> **What must be true for a system to remain capable of incorporating warranted correction after a consequential modification?**

This is a conceptual frontier only. Any empirical study of post-modification correctability remains blocked until the particular evidence-to-change pathway it relies on satisfies the upstream empirical gates and the CCA Causal Composition Principle.

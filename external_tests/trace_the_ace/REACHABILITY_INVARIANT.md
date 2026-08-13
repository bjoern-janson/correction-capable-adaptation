# Trace the Ace reachability invariant

## Status

**FROZEN BRANCH-WIDE METHODOLOGICAL INVARIANT**

This artifact is a companion to `GOVERNING_INTERFACE.md`. It adds no scientific authority, changes no experiment result, and authorizes no new model family. It formalizes the control-law consequence of the existing price/authority and recursive-method rules.

## Research state

Trace the Ace research state is represented schematically as:

\[
\boxed{
S_t=(\mathcal O_t,E_t,A_t,B_t,\mathcal T_t)
}
\]

where:

```text
O_t  current scientific and methodological objects
E_t  accumulated evidence
A_t  earned authority
B_t  open diagnostic / revision boundaries
T_t  currently licensed research transitions
```

Evidence therefore affects not only what propositions are supported, but which research transitions are reachable.

## Possibility space is not execution space

Let `H_t` denote the live hypothesis / explanation space and `T_t` the licensed transition set.

\[
\boxed{\mathcal H_t \neq \mathcal T_t}
\]

`H_t` describes what may still be scientifically possible. `T_t` describes what the project is currently authorized to execute.

A disciplined research state may therefore satisfy:

\[
|\mathcal H_t| \gg |\mathcal T_t|.
\]

Uncertainty does not itself create execution authority.

\[
\boxed{\text{uncertainty} \neq \text{permission to explore arbitrarily}}
\]

## Authorized state transition

CARS governs state transitions through diagnosed evidence and only along licensed edges:

\[
\boxed{
S_t
\xrightarrow[\text{authorized edge}]{\text{evidence + diagnosis}}
S_{t+1}
}
\]

A transition may occur only when the predecessor state contains an authorized edge for that revision class.

The invalid shortcut is:

\[
\boxed{
\text{uncertainty or inconvenience}
\not\Rightarrow
\text{arbitrary successor execution}
}
\]

## No consequence object, no evidence-bearing transition

If an experiment is authorized but execution produces no scientific consequence object `P_k`, then no result-bearing transition exists:

\[
\boxed{
P_k\ \text{absent}
\Rightarrow
D_R\ \text{unavailable}
\Rightarrow
D_H\ \text{unavailable}
\Rightarrow
\Delta W=0
}
\]

Engineering evidence may update the apparatus boundary, but cannot be relabeled as scientific evidence for or against the hypothesis.

Therefore:

\[
\boxed{\text{blocked execution} \neq \text{negative scientific evidence}}
\]

## Returnability

Research returnability is an authorized reopening property, not continuous editability:

\[
\boxed{
\text{new discriminating evidence}
\rightarrow
\text{implicated boundary}
\rightarrow
\text{authorized reopening}
\rightarrow
\text{successor state}
}
\]

It does not mean:

\[
\text{new uncertainty}\rightarrow\text{anything goes}.
\]

A boundary may remain closed while unresolved alternatives stay live.

## Recursive topology

Object-level transitions remain governed by the locally binding methodological protocol `Gamma_t`:

\[
M_k\rightarrow M_{k+1}
\quad\text{only under}\quad
\Gamma_t.
\]

Changes to the transition rules themselves remain governed by the recursive methodological-successor rule:

\[
\Gamma_t\rightarrow\Gamma_{t+1}
\quad\text{only after}\quad
\operatorname{AUTH}(\Gamma_{t+1})
\text{ is earned under }\Gamma_t.
\]

Thus:

\[
\boxed{\text{CARS controls scientific transitions}}
\]

while:

\[
\boxed{\Gamma_t\text{ controls admissible changes to CARS transition rules}.}
\]

Neither level may overwrite the other implicitly.

## Governing reachability principle

\[
\boxed{\textbf{Corrigibility is evidence-governed reachability, not continuous editability.}}
\]

A corrigible research system preserves the capacity to reopen scientific or methodological boundaries when discriminating evidence earns that transition. It does not grant itself standing permission to cross unopened boundaries.

Equivalently:

\[
\boxed{
\textbf{A corrigible research system preserves the ability to reopen boundaries without granting itself permission to cross them arbitrarily.}
}
\]

## Permanent pair

This invariant is to be read alongside the governing price/authority rule:

\[
\boxed{\textbf{Price is consequence. Authority is diagnosed consequence.}}
\]

\[
\boxed{\textbf{Corrigibility is evidence-governed reachability, not continuous editability.}}
\]

The first rule governs **what evidence means**. The second governs **what evidence is allowed to make the research process do**.

## Current Trace the Ace implication

At the state in which this invariant is frozen, the licensed transition set remains intentionally narrow. Existing unresolved hypotheses do not authorize arbitrary model search or CCA-derived feature execution. Any expansion of the reachable set must be earned through the governing interface and predecessor methodological protocol.

Any departure from this reachability invariant is itself a methodological revision and must enter through an authorized methodological successor.
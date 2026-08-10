# Level-0 Attack: Can Outcome-Level G1 Be Identified Independently of Channel Attribution?

## Status

**ADVERSARIAL SCIENTIFIC ANALYSIS — NO STATE TRANSITION — NO IMPLEMENTATION**

This document attacks the proposition motivated by PR #3:

> **Outcome-level evidence control and mechanism/channel attribution can be separated.**

The candidate decomposition is:

```text
LEVEL A — OUTCOME
Does evidence control selection toward C*(E)?

LEVEL B — MECHANISM
Which information structure in E carries that control?
```

This analysis does **not** select an ontology, freeze an evidence intervention, modify `research_state.json`, implement ECIM, select a model or prompt, or authorize execution.

The question is narrower:

> **Can the total causal effect of evidence on warranted selection be identified without identifying which information channel inside the evidence caused that effect?**

The attack deliberately looks for both directions of failure:

1. cases where outcome-level G1 is identifiable but channel attribution is not;
2. cases where apparent separation fails because the evidence treatment itself is not well defined.

---

# 1. Objects that must not be conflated

Let:

\[
E
\]

be the prospectively defined evidence treatment;

\[
C_{\mathrm{selected}}
\]

be the selected candidate;

and

\[
C^*(e)
\]

be the candidate independently warranted by evidence condition \(e\).

Define warranted-selection success:

\[
S(e)=\mathbf 1[C_{\mathrm{selected}}=C^*(e)].
\]

The outcome-level object is therefore not arbitrary selection sensitivity. It is **causal movement toward the independently warranted candidate**.

For two matched evidence conditions \(e_a,e_b\) with

\[
C^*(e_a)\neq C^*(e_b),
\]

a directional contrast can be written as:

\[
\delta_a
=
P(C_{\mathrm{selected}}=C^*(e_a)\mid do(E=e_a))
-
P(C_{\mathrm{selected}}=C^*(e_a)\mid do(E=e_b)).
\]

A symmetric pairwise responsiveness contrast is:

\[
\delta_{ab}^{\mathrm{sym}}
=
\frac12\Big[
P(C=C^*(e_a)\mid do(e_a))
-
P(C=C^*(e_a)\mid do(e_b))
\Big]
\]

\[
+\frac12\Big[
P(C=C^*(e_b)\mid do(e_b))
-
P(C=C^*(e_b)\mid do(e_a))
\Big].
\]

The exact future estimand is not frozen here. These expressions only make the logical distinction explicit:

\[
\boxed{
\text{G1 outcome}
=
\text{causal evidence control in the warranted direction}
}
\]

not merely:

\[
E\text{ changes }C.
\]

---

# 2. Candidate channel decomposition

Suppose the raw evidence representation supports several prospectively described information structures:

\[
\Phi(E)
=
(R(E),O(E),I(E),P(E),H(E),\ldots),
\]

where, schematically:

```text
R  relational / pairing information
O  output-marginal information
I  input-only information
P  presentation / position information
H  higher-order or other structured information
```

These are **not automatically independent causal variables**.

They may be:

- deterministic functions of the same evidence object;
- statistically dependent;
- logically overlapping;
- impossible to vary independently while preserving evidence semantics;
- jointly sufficient but individually insufficient;
- different descriptions of the same underlying distinction.

Therefore the notation

\[
E\rightarrow(R,O,I,P,\ldots)\rightarrow C
\]

must not be mistaken for an already identified mediation model.

The channel-attribution question is a separate burden:

\[
\boxed{
\text{Which manipulable or discriminable information structure carries the observed G1 control?}
}
\]

---

# 3. First destructive test: same G1 outcome, different mechanisms

Construct two hypothetical selectors over the same admissible evidence conditions.

## Selector A — relation-based

Selector A maps evidence to the warranted candidate using only a pairing relation:

\[
C_A(E)=g_R(R(E)).
\]

## Selector B — output-based

Selector B produces the **same candidate choice on every admissible evidence condition**, but uses only an output statistic:

\[
C_B(E)=g_O(O(E)).
\]

Assume:

\[
C_A(e)=C_B(e)=C^*(e)
\quad\forall e\in\mathcal E.
\]

Then every outcome-level G1 observation is identical:

\[
P(C_A=C^*(e)\mid do(e))
=
P(C_B=C^*(e)\mid do(e)).
\]

All pairwise warranted-selection contrasts are also identical.

Yet the internal information source differs by construction.

Therefore:

\[
\boxed{
\text{outcome-level G1 data do not identify channel mechanism}
}
\]

and, importantly:

\[
\boxed{
\text{failure to identify channel mechanism does not prevent identifying G1 total control}
}
\]

provided the evidence treatment and warranted endpoint are themselves valid.

This is the first existence witness for clean separation.

---

# 4. Stronger destructive test: channel attribution can be impossible while G1 remains identified

Suppose on the entire admissible evidence support:

\[
R(E)=h(O(E))
\]

for a one-to-one mapping \(h\).

Then relational and output information are perfectly coupled under every licensed evidence condition.

No observed intervention on \(E\) separates them.

Two causal accounts remain observationally equivalent:

```text
E -> R -> C
```

and

```text
E -> O -> C.
```

If no semantically valid intervention can vary \(R\) while preserving \(O\), or vice versa, the channel-specific mechanism is not causally identified under that design.

Nevertheless, if:

1. \(E\) is prospectively defined;
2. \(C^*(E)\) is unique and independent of tested-model behavior;
3. evidence assignment is experimentally controlled;
4. the comparison holds other selection opportunities fixed;
5. \(C_{\mathrm{selected}}\) is observed reliably;

then the total effect

\[
do(E)\rightarrow C_{\mathrm{selected}}
\]

in the warranted direction can still be identified.

Thus:

\[
\boxed{
\text{channel non-identifiability}
\not\Rightarrow
\text{G1 outcome non-identifiability}
}
\]

This is a stronger separation result than the first witness because mechanism attribution is not merely unknown; it is **underidentified in principle under the available channel support**.

---

# 5. Mediation ambiguity is real, but it attacks Level B rather than Level A

Suppose the true system admits several routes:

\[
E\rightarrow R\rightarrow C,
\]

\[
E\rightarrow O\rightarrow C,
\]

and perhaps

\[
E\rightarrow(R,O)\rightarrow C.
\]

Randomizing or otherwise validly intervening on \(E\) identifies the **total evidence effect** on the selected outcome under ordinary causal assumptions appropriate to that randomized treatment.

It does not automatically identify:

- a natural indirect effect through \(R\);
- a controlled direct effect of \(R\);
- necessity of \(R\);
- sufficiency of \(R\);
- the fraction of the total effect carried by \(R\);
- whether \(R\) and \(O\) interact.

Those require additional measurement and intervention assumptions.

Therefore:

\[
\boxed{
\text{total evidence control}
\neq
\text{channel-specific mechanism}
}
\]

This is not a defect in the total-effect estimand. It is an authority boundary.

---

# 6. But the separation is not unlimited: treatment constitution remains upstream

A naive version of the proposed hierarchy would say:

```text
first estimate broad G1 from raw E
then worry about representation later
```

That is too permissive.

Before G1 can be identified, the experiment must still specify what counts as the evidence treatment.

Consider an evidence realization containing:

```text
semantic examples
+ candidate ID token
+ systematically privileged candidate position
+ formatting bit correlated with C*(E)
```

A selector may choose the warranted candidate because of the candidate ID or formatting bit.

If those fields were introduced accidentally by benchmark construction and are not licensed as part of the intended evidence semantics, then a large total treatment effect would not justify the claim:

> valid evidence controlled warranted selection.

It would justify only:

> this raw treatment package controlled selection.

Therefore Level-A G1 still requires a **measurement constitution layer** distinguishing:

\[
\text{licensed evidence content}
\]

from

\[
\text{extrinsic construction artifact}.
\]

This does **not** require identifying whether the model used relation, output marginal, or another legitimate semantic channel.

It requires prospectively defining the treatment whose causal effect is being estimated.

The corrected hierarchy is therefore at least:

```text
LEVEL 0A — TREATMENT / OBJECT CONSTITUTION
What counts as admissible evidence E?
What is nuisance or construction artifact?
What uniquely warrants C*(E)?

LEVEL 0B — OUTCOME-LEVEL G1
Does do(E) control selection toward C*(E)?

LEVEL 0C — CHANNEL / MECHANISM ATTRIBUTION
Which information structure within admissible E carries that control?
```

This is an important caveat:

\[
\boxed{
\text{G1 can be independent of channel attribution}
\;
\text{but not independent of evidence-treatment definition}
}
\]

---

# 7. What counts as a legitimate shortcut under outcome-level G1?

The word “shortcut” becomes dangerous unless indexed to the scientific object.

Under a broad outcome-level G1, an information statistic may be legitimate if all of the following hold:

1. it is genuinely entailed by the admissible evidence semantics;
2. it is available under the prospectively declared evidence representation;
3. it is not an accidental candidate-name, position, formatting, or benchmark-construction leak;
4. using it can validly support the independently warranted \(C^*(E)\) under the declared scope.

Examples may include output marginals, input statistics, symbolic patterns, or compressed sufficient statistics.

The model need not reconstruct the evidence in the representation preferred by the experimenter.

Thus:

\[
\boxed{
\text{unexpected compression}
\neq
\text{invalid evidence use}
}
\]

provided the compression is epistemically licensed by the evidence object.

By contrast, a feature is disqualifying for broad G1 if its candidate-predictive authority comes from **experimental presentation machinery rather than the licensed evidence semantics**.

This boundary belongs to measurement validity, not channel mechanism attribution.

---

# 8. Failure modes for G1 that do not depend on channel attribution

Outcome-level G1 can fail or become invalid for reasons that have nothing to do with whether relational, output, or other channels are used.

## 8.1 Non-unique warrant

If:

\[
|C^*(e)|\neq1,
\]

then success is not uniquely defined.

This is measurement non-identifiability.

## 8.2 Treatment confounding

If changing \(E\) also changes target context, candidate pool, candidate count, resources, selection opportunity, or other causal inputs, then the total evidence contrast is not isolated.

## 8.3 No counterfactual support

If every candidate is only ever paired with one evidence regime and the design gives no matched counterfactual evidence reassignment, evidence control may be inseparable from stable candidate/context structure.

## 8.4 Extrinsic authority leakage

If presentation fields reveal \(C^*(E)\) for reasons unrelated to admissible evidence semantics, the treatment no longer cleanly represents the intended evidence object.

## 8.5 Measurement corruption

If assignment, candidate identity, or selected outcome cannot be reconstructed reliably, the affected contrast is invalid/unobserved rather than a scientific failure.

None of these requires answering:

> Did the model use relation or output marginals?

Therefore they support the separation rather than undermine it.

---

# 9. Failure modes for channel attribution that can coexist with successful G1

Conversely, G1 may be clean and positive while Level-0C remains unresolved.

Channel attribution can fail because:

- channels are perfectly correlated;
- candidate semantics make one channel constitutively imply another;
- proposed channel interventions destroy the evidence semantics;
- channel variables are not independently manipulable;
- channel definitions overlap;
- relation-destruction creates evidence with no unique \(C^*\);
- the tested contrast identifies sensitivity but not causal mediation;
- multiple channel models are observationally equivalent.

In such cases the valid claim ceiling is:

> Assigned admissible evidence causally controlled warranted selection under the tested conditions.

Not:

> The system used relational reasoning.

This is a clean authority boundary rather than a failed experiment.

---

# 10. Relation-destruction controls remain useful, but their role changes

A relation-destruction object such as

\[
\widetilde e_{\pi}
=
\{(x_i,y_{\pi(i)})\}
\]

may preserve input and output marginals while destroying the original pairing.

This can be extremely useful for channel discrimination.

But if \(\widetilde e_{\pi}\) has no unique warranted candidate, then it cannot silently become a primary G1 treatment.

Its role is diagnostic:

```text
PRIMARY G1
admissible E with unique C*(E)
-> estimate warranted total evidence control

CHANNEL AUDIT
relation-destroyed / marginal-preserving object
-> ask what behavior survives removal of pairing structure
```

Therefore:

\[
\boxed{
\text{diagnostic channel intervention}
\neq
\text{primary warranted-selection treatment}
}
\]

This preserves the original rule that an object without a unique \(C^*\) cannot enter the primary estimand by convenience.

---

# 11. Does successful G1 authorize mechanism attribution?

No.

A positive outcome-level G1 establishes at most that the admissible evidence treatment causally governs warranted selection under the frozen conditions.

It does not identify which channel carried that effect.

Thus:

\[
G_1>0
\not\Rightarrow
M_R
\]

where \(M_R\) is a relational mechanism claim.

A separate mechanism contract would be needed.

However, G1 success may make a mechanism study **scientifically relevant** because there is then an effect to explain.

That gives a useful distinction:

```text
AUTHORITY:
G1 success does not establish mechanism.

RESEARCH PRIORITY:
G1 success may authorize asking what mechanism produced the effect.
```

Mechanism work can also occur after G1 failure as diagnosis, but then its claim is diagnostic rather than explanatory of successful warranted control.

---

# 12. Does mechanism attribution authorize G1?

Also no.

A selector can be strongly relation-sensitive and systematically wrong:

\[
R_{\mathrm{dep}}>0
\quad\land\quad
P(C=C^*)\approx0.
\]

Or it can use an identified channel in a way that moves choices without increasing warranted fidelity.

Therefore:

\[
\boxed{
M_R
\not\Rightarrow
G_1
}
\]

This confirms that the two layers carry different authority.

---

# 13. The proposed architecture survives, but only in a refined form

The strongest version of the decomposition that survives the attack is:

```text
CCA
 |
 v
LEVEL 0A — measurement constitution
Define admissible evidence, warrant, and nuisance class
 |
 v
LEVEL 0B — G1 total warranted evidence control
Does do(E) move selection toward C*(E)?
 |
 +-----------------------------+
 |                             |
 v                             v
successful G1              failed G1
 |                             |
 v                             v
mechanism explanation      mechanism diagnosis
(optional separate object) (optional separate object)
 |
 v
channel attribution / mechanism discrimination
```

The mechanism layer is **not part of the definition of warranted selection**.

But measurement constitution remains logically prior to both.

This yields the central result of the attack:

\[
\boxed{
\textbf{Outcome-level G1 is separable from channel attribution in principle,}
}
\]

subject to:

\[
\boxed{
\textbf{the evidence treatment and independent warrant mapping being validly constituted first.}
}
\]

---

# 14. What this means for the broad-vs-relational fork

PR #3 showed that “relational G1” had been carrying two possible meanings:

1. warranted evidence control under a relationally identifying design;
2. sensitivity to the relational information channel.

The present attack sharpens the distinction.

The first can still be understood as a restricted **measurement design for outcome-level G1**.

The second is better understood as a **mechanism/channel-attribution object**.

Therefore the apparent fork may decompose into two orthogonal questions:

\[
\boxed{
G_1:
\text{Does admissible evidence causally control warranted selection?}
}
\]

and

\[
\boxed{
M_1:
\text{Which information structures within admissible evidence carry that control?}
}
\]

This decomposition is not made canonical by this document. It is the strongest candidate architecture surviving the current attack.

---

# 15. Relation to CCA

CCA ultimately asks whether valid correction can govern adaptive change across time.

That functional property should not depend definitionally on one representational route.

A system may extract warranted information through:

- relational structure;
- sufficient statistics;
- symbolic inference;
- latent representations;
- combinations of channels;
- mechanisms not anticipated by the experimenter.

If the system reliably converts admissible evidence into warranted selection, the program has evidence about correction-capable behavior at G1 even when the internal extraction mechanism remains unresolved.

Mechanism knowledge can still matter for:

- transport;
- robustness;
- adversarial failure prediction;
- engineering;
- repeated-correction stability;
- interpreting why G1 succeeds or fails.

But those are additional authorities.

Thus the CCA-level distinction is:

\[
\boxed{
\text{functional correction capacity}
\neq
\text{particular information-processing mechanism}
}
\]

---

# 16. Relation to C_improve

The provisional `C_improve` hypothesis concerns the pathway:

\[
\text{valid feedback}
\rightarrow
\text{warranted revision}
\rightarrow
\text{validated modification}
\rightarrow
\text{future viability}.
\]

Nothing in that hypothesis requires the evidence to be extracted through a privileged relational mechanism.

Therefore, at the current theoretical level:

\[
\boxed{
C_{\mathrm{improve}}
\text{ is mechanism-agnostic with respect to information channel}
}
\]

provided the evidence-to-warranted-revision link is causally established.

Mechanism attribution may later explain reliability or transport of `C_improve`, but it should not define the construct prematurely.

---

# 17. Known impossibility boundary retained

The constant-function witness remains important:

\[
f_0(x)=0,
\qquad
f_1(x)=1.
\]

It shows that relational channel attribution may be impossible because candidate identity lives entirely in output marginals.

Under the present decomposition, that no longer threatens broad G1.

If the output marginal is a legitimate semantic consequence of the evidence and uniquely warrants the candidate, the system may still exhibit valid outcome-level evidence control.

Therefore the witness now localizes more precisely:

\[
\boxed{
\text{constant-function ontology}
\Rightarrow
\text{relational mechanism attribution unavailable}
}
\]

but not:

\[
\boxed{
\text{constant-function ontology}
\Rightarrow
\text{warranted evidence control unavailable}.
}
\]

This is exactly the type of distinction the attack was intended to expose.

---

# 18. What would refute the separation thesis?

The proposed separation would fail if one could establish that **no scientifically defensible evidence treatment can be defined without simultaneously specifying the information channel whose use constitutes success**.

That would require showing something like:

> For every admissible evidence representation, the identity of “valid evidence use” changes with the model's internal channel decomposition, so no channel-agnostic total warranted-selection effect corresponds to a stable scientific object.

The current analysis does not establish such an impossibility.

Instead it finds a stable candidate object:

\[
\boxed{
\text{causal control of independently warranted selection by a prospectively constituted evidence treatment}
}
\]

whose total effect can be defined without knowing which legitimate semantic feature the selector internally exploits.

Therefore the attempted destruction does **not** currently kill the outcome/mechanism separation.

---

# 19. Current adversarial verdict

The strongest justified conclusion is:

\[
\boxed{
\text{OUTCOME / CHANNEL SEPARATION}
=
\text{FEASIBLE IN PRINCIPLE}
}
\]

with an essential qualification:

\[
\boxed{
\text{treatment constitution precedes outcome identification}
}
\]

and:

\[
\boxed{
\text{channel attribution remains a separate, often harder identification problem}
}
\]

The resulting candidate hierarchy is:

```text
0A  scientific-object / evidence-treatment constitution
    ↓
0B  total evidence-controlled warranted selection (G1)
    ↓
0C  information-channel / mechanism attribution (M1), when scientifically useful
```

This is an adversarial result, **not yet a canonical CCA state transition**.

---

# 20. Explicit nonchanges

This analysis does not authorize or change any of the following:

```text
research_state.json          UNCHANGED
G1 canonical definition      UNCHANGED
candidate ontology           UNFROZEN
evidence intervention space  UNFROZEN
ECIM contract                UNFROZEN
model / prompt               NOT SELECTED
benchmark                    NOT IMPLEMENTED
execution                    NOT AUTHORIZED
ASI-0                        CLOSED / IMMUTABLE
```

No implementation follows from this document.

---

# 21. Next legitimate destructive question

If this candidate decomposition is attacked again, the highest-value target is no longer “broad vs relational.”

It is:

> **Can a prospectively defined evidence treatment be made semantically stable enough that total warranted-selection control is invariant to licensed representation changes, while remaining agnostic about the selector's internal information channel?**

That attacks the remaining dependency directly:

\[
\text{treatment constitution}
\rightarrow
\text{outcome-level G1}.
\]

Until that survives, no ontology or empirical G1 experiment should be frozen.

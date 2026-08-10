# Level-0 Scientific-Object Analysis: Broad vs Relational Evidence Use

## Status

**ADVERSARIAL SCIENTIFIC ANALYSIS — NO FORMULATION SELECTED — NO STATE TRANSITION**

This document compares two candidate meanings of evidence use at the current Level-0 measurement frontier:

\[
G_1^{\mathrm{broad}}: E\rightarrow C_{\mathrm{selected}}
\]

and

\[
G_1^{\mathrm{relational}}:(X,Y,\mathrm{pairing})\rightarrow C_{\mathrm{selected}}.
\]

It does **not** choose an ontology, construct an intervention space, select a model, implement ECIM, modify `research_state.json`, or authorize execution.

The purpose is narrower:

> **What scientific claims become possible or impossible under each formulation, and how do those claims connect to the larger Correction-Capable Adaptation program?**

---

# 1. Shared upstream requirement: warranted selection

The CCA program is not interested in selection variation by itself. The relevant endpoint is selection of a candidate independently warranted by the assigned evidence.

For admissible evidence condition \(e\), let

\[
C^*(e)
\]

be the candidate warranted by the prospectively declared evidence semantics, independently of tested-model behavior.

A generic broad success variable is therefore

\[
S(e)=\mathbf 1[C_{\mathrm{selected}}=C^*(e)].
\]

The broad scientific object is not merely

\[
do(E=e_a)\neq do(E=e_b)\Rightarrow C_a\neq C_b.
\]

It is that intervention on evidence changes selection **in the warranted direction**.

This distinction matters for the fork analysis because a system can be sensitive to a relation while using it incorrectly. Relational responsiveness alone is therefore not automatically a stronger form of broad warranted selection.

---

# 2. Two different meanings of “relational G1” must be separated

The notation

\[
(X,Y,\mathrm{pairing})\rightarrow C_{\mathrm{selected}}
\]

admits two scientifically different readings.

## 2.1 Relational responsiveness

The weak reading asks:

> Does changing or destroying the pairing relation change candidate selection beyond licensed non-relational information channels?

Call this

\[
R_{\mathrm{dep}}.
\]

This is a **channel-dependence** claim. It does not imply correctness.

A selector could react strongly to the pairing relation while systematically selecting the wrong candidate:

\[
R_{\mathrm{dep}}>0
\quad\land\quad
P(C_{\mathrm{selected}}=C^*)\approx 0.
\]

Therefore:

\[
\boxed{R_{\mathrm{dep}}\not\Rightarrow G_1^{\mathrm{broad}}}
\]

when broad G1 means warranted selection.

## 2.2 Relational warranted selection

The stronger reading retains the same warranted-selection endpoint as broad G1 and adds a channel-identification restriction:

> Does evidence causally move selection toward \(C^*(E)\), under contrasts for which licensed non-relational channels cannot identify the warranted candidate and the discriminating information resides in the input-output relation?

Call this

\[
G_1^{\mathrm{rel\text{-}warrant}}.
\]

Under this definition, relational G1 is not a replacement endpoint. It is broad warranted selection under a more restrictive measurement design.

This yields the first major result of the fork analysis:

\[
\boxed{
G_1^{\mathrm{relational}}
\subset
G_1^{\mathrm{broad}}
}
\]

is valid **only if** “relational” includes the same independently warranted \(C^*(E)\) criterion.

If “relational” means relation dependence alone, the two objects are not nested.

---

# 3. A clean nested formulation is possible

Let \(Z(E)\) denote the prospectively licensed non-relational information available from evidence, such as declared output marginals, input marginals, formatting features, or presentation statistics.

For a pair of valid evidence conditions \((e_a,e_b)\), suppose:

\[
C^*(e_a)\neq C^*(e_b)
\]

while

\[
Z(e_a)=Z(e_b).
\]

If the only licensed distinction capable of warranting the different candidates is the pairing relation, then successful warranted selection across those conditions establishes something stronger than generic broad evidence control.

A relationally identifying contrast can therefore be represented as a restricted subset

\[
\mathcal E_{\mathrm{rel}}
\subseteq
\mathcal E_{\mathrm{broad}}
\]

such that, for admissible pairs,

\[
Z(e_a)=Z(e_b),
\qquad
C^*(e_a)\neq C^*(e_b),
\]

and the warrant-relevant difference is carried by the relation.

Under this construction:

\[
\boxed{
\text{relational success}
\Rightarrow
\text{broad warranted-selection success on those contrasts}
}
\]

plus an additional channel claim indexed to the licensed nuisance class \(\mathcal Z\).

The converse does not hold:

\[
\boxed{
G_1^{\mathrm{broad}}
\not\Rightarrow
G_1^{\mathrm{rel\text{-}warrant}}
}
\]

because broad warranted selection may legitimately use non-relational evidence.

This is a possible hierarchy, not yet a program decision.

---

# 4. Comparison matrix

| Dimension | Broad G1 | Relational warranted G1 |
| --- | --- | --- |
| Primary claim | Assigned evidence causally controls selection toward the independently warranted candidate. | Assigned evidence controls warranted selection under contrasts where the discriminating authority is specifically relational beyond licensed non-relational channels. |
| Scientific level | Outcome-level evidence-control property. | Outcome-level evidence control + channel/mechanism attribution. |
| Scope | Broadest evidence-bearing ontology class compatible with independent warrant. | Restricted to ontologies where relational authority is separately identifiable without semantic recoding. |
| Mechanistic specificity | Low to moderate. | High, relative to the licensed non-relational feature class. |
| Shortcut policy | Legitimate evidence-derived shortcuts may count if they genuinely warrant the candidate. | Licensed non-relational shortcuts cannot carry the identifying contrast if a relational claim is to be earned. |
| Main risk | A positive result may leave the internal evidence-use mechanism opaque. | A beautiful mechanism probe may become narrower than the CCA phenomenon the program ultimately cares about. |
| Main impossibility boundary | Failure to define unique independent \(C^*(E)\), or confounded evidence interventions. | All broad boundaries plus ontology-dependent impossibility of separating relational from non-relational authority. |
| Relation to CCA mission | Direct: CCA requires valid evidence to govern warranted change, regardless of representational route. | Indirectly stronger mechanistic evidence: explains one way warranted evidence control may be realized. |
| Relation to `C_improve` | Natural upstream precursor: valid feedback must control warranted change before future viability can be attributed to correction. | Potential mechanism discriminator, but not required by `C_improve` unless the theory specifically privileges relational extraction. |
| Downstream authorization if successful | Can support moving to the modification layer, subject to a frozen contract and all other gates. | Can support the same move and additionally license a scoped relational-mechanism claim. |
| External generality | Potentially higher. | Potentially lower because admissible ontologies are constrained by relational identifiability. |

---

# 5. Scientific claim supported by broad G1

A successful broad experiment could support a claim of the form:

> Under the frozen evidence intervention, candidate ontology, warrant mapping, and resource conditions, assigned evidence causally increased selection of the independently warranted modification.

This claim is already substantial for CCA. It establishes a causal link between evidence and warranted adaptive choice.

It does **not** establish:

- that the system inferred an input-output relation;
- that the system formed the intended internal representation;
- that candidate selection was free of all shortcuts;
- that the evidence-control mechanism transports to a new ontology;
- that the selected modification is effective;
- that protected behavior is preserved;
- that capability or viability improves.

Broad G1 is therefore a clean answer to:

\[
\boxed{
\text{Does valid evidence acquire causal authority over warranted selection?}
}
\]

It is deliberately agnostic about the representational route by which that authority is exercised.

---

# 6. Scientific claim supported by relational warranted G1

A successful relationally identifying experiment could support a claim of the form:

> Under the frozen ontology and licensed non-relational feature class, assigned evidence causally increased warranted candidate selection in contrasts where the discriminating information was carried by the demonstrated input-output relation.

This claim adds mechanistic resolution.

It can exclude explanations of the form:

\[
Z(E)\rightarrow C_{\mathrm{selected}}
\]

for the prospectively licensed \(Z\)-class when \(Z\) is held invariant across the identifying contrast.

It still does **not** establish:

- absence of every conceivable shortcut;
- a unique internal representation;
- general relational reasoning;
- transport to ontologies outside the relationally admissible class;
- target efficacy, protected preservation, capability, or viability.

The strongest justified wording is therefore indexed to the licensed channels:

> Candidate selection depended on warrant-relevant relational information beyond the declared non-relational channels.

Not:

> The model reasoned relationally in general.

---

# 7. Claims excluded by choosing each object

## If broad G1 is the only Level-1 object

A positive result cannot by itself distinguish:

```text
relation extraction
output-marginal recognition
input-marginal recognition
semantic feature recognition
memorized candidate cue
other legitimate evidence-derived route
```

provided the route is genuinely contained in the admissible evidence and remains consistent with the independent warrant mapping.

Thus broad G1 cannot support a strong mechanism claim about **how** evidence acquired authority.

## If relational G1 is made the only Level-1 object

The program would exclude ontologies where valid evidence is inherently carried by non-relational properties.

For example, in the constant-function ontology

\[
f_0(x)=0,
\qquad
f_1(x)=1,
\]

candidate identity is legitimately present in the output marginal. There is no separate relational authority to recover.

Rejecting that ontology for relational measurement is scientifically correct for a relational claim, but it would be incorrect to conclude that its evidence cannot control warranted selection.

Therefore making relational G1 the sole definition of evidence use would narrow the program from:

> Can evidence govern warranted adaptive change?

to:

> Can a specific class of relational evidence govern warranted adaptive change?

That narrowing may or may not be desirable; the present analysis does not decide it.

---

# 8. Admissible ontology classes

## Broad ontology class

A broad G1 ontology is admissible in principle when the contract can define:

\[
\mathcal C,
\qquad
\mathcal E,
\qquad
C^*:\mathcal E\rightarrow\mathcal C
\]

with an independently auditable warrant mapping and an interpretable intervention on evidence.

The ontology need not make relational information separately identifiable.

Conceptually:

\[
\mathfrak C_{\mathrm{broad}}
=
\{\mathcal C:\exists\ \text{valid independently auditable evidence-to-warrant contract}\}.
\]

## Relational ontology class

A relational warranted G1 ontology must satisfy the broad requirements **and** permit at least one family of contrasts where licensed non-relational information is matched while the warranted candidate differs because of the relation.

Conceptually:

\[
\mathfrak C_{\mathrm{rel}}
\subseteq
\mathfrak C_{\mathrm{broad}}.
\]

The existing destructive analysis already establishes that this subset is proper in at least one natural sense:

```text
constant-function ontology
→ broad identifiability possible
→ relational identifiability UNSAT
```

while the balanced three-candidate/two-region witness establishes that

```text
relational admissibility is nonempty in principle.
```

---

# 9. Measurement requirements

## Broad G1 requires

At minimum:

1. an admissible evidence intervention space \(\mathcal E\);
2. a unique, model-independent warrant mapping \(C^*(E)\);
3. controlled evidence assignment;
4. candidate-set and resource matching across causal contrasts;
5. protection against label leakage, candidate-position leakage, or other artifacts that are not part of the intended evidence semantics;
6. a prospective selection estimand that rewards movement toward \(C^*(E)\), not mere answer variation;
7. explicit invalidation rules for ambiguous or confounded evidence conditions.

## Relational warranted G1 additionally requires

1. a prospectively licensed non-relational feature/channel class \(\mathcal Z\);
2. ontology feasibility showing that relational authority can be separated without altering semantic validity;
3. identifying contrasts with matched licensed non-relational information;
4. presentation equivariance/invariance rules so ordering does not become a surrogate relation;
5. relation-destruction or surface-only audits as diagnostics where scientifically coherent;
6. bounded claims indexed to \(\mathcal Z\), rather than universal “no shortcut” language.

The relational object therefore has a heavier measurement burden.

That burden buys a stronger channel-attribution claim, not automatically a more important CCA claim.

---

# 10. Necessary controls

## Broad controls

Controls should distinguish evidence authority from generic experimental artifacts:

```text
same candidate ontology
same candidate availability
same evidence quantity where relevant
same resource budget
same target context
same evaluation rule
prospective assignment/randomization
independent C*(E)
```

A non-relational cue is not disqualifying merely because it is simple. It is disqualifying only if it is outside the intended evidence semantics, leaks the answer independently of the scientific intervention, or destroys causal interpretability.

## Relational controls

The relational claim adds a stronger burden:

```text
licensed non-relational channels matched or rendered non-identifying
pair relation remains semantically faithful
candidate presentation does not encode identity
relation-destruction audit preserves the declared marginals where possible
surface-only audit cannot trivially recover identity within the licensed adversary class
```

Importantly, nuisance balancing may never override semantic fidelity.

If relational isolation requires recoding candidate semantics, the construction is invalid rather than “balanced.”

---

# 11. Known impossibility boundaries

## Broad impossibility

Broad G1 is not identified when:

- evidence does not determine a unique warranted candidate;
- the evidence intervention changes other causal variables that independently alter selection;
- the truth/warrant mapping is derived from tested-model behavior;
- candidate identity is exposed by an unintended experimental label rather than by the declared evidence semantics.

## Relational impossibility

Relational G1 inherits all broad impossibility conditions and adds a structural one:

> Some candidate ontologies do not permit relational authority to be separated from legitimate non-relational evidence while preserving the semantics of the candidate functions.

The constant-function witness is the permanent regression case:

\[
f_0(x)=0,
\qquad
f_1(x)=1.
\]

Here output marginals fully identify the candidate. Pairing adds no separately identifiable authority.

Thus:

\[
\boxed{
\text{relational evidence use cannot be demanded independently of ontology}
}
\]

is an established measurement-layer boundary.

---

# 12. Failure interpretations

Failure semantics differ materially across the formulations.

## Broad failure

If a valid broad experiment finds no warranted evidence-control effect, the shallow interpretation is:

> Under the tested interface and ontology, assigned evidence did not causally control warranted candidate selection to the declared criterion.

Possible deeper causes remain open unless independently diagnosed:

```text
insufficient inference
weak/ambiguous evidence
representation failure
candidate ontology mismatch
measurement invalidity
implementation failure
```

A broad failure does not automatically identify which one caused the result.

## Relational failure with broad success

This is scientifically coherent.

It can mean:

1. the system uses legitimate non-relational evidence rather than the pairing relation;
2. the pairing relation is not separately identifiable in that ontology;
3. the licensed nuisance class is too expressive or too weakly controlled;
4. the system achieves warranted selection through a different mechanism.

Therefore:

\[
\boxed{
\text{relational failure}
\not\Rightarrow
\text{failure of evidence-controlled warranted selection}
}
\]

when broad G1 succeeds.

## Relational responsiveness with broad failure

This is possible under the weak relation-dependence reading:

```text
pairing changes selection
+
selection moves toward the wrong candidate
```

It is **not** possible if relational G1 is defined as relational warranted selection on the same contrasts, because the warranted criterion is then part of the relational success condition.

This distinction is why the current notation must not silently conflate relation dependence with warranted relational use.

---

# 13. Legitimate vs disqualifying shortcuts

The word “shortcut” is scientifically dangerous unless indexed to the object.

## Under broad G1

A simple feature is **legitimate** when:

- it is genuinely part of the admissible evidence;
- it carries valid warrant for the candidate under the frozen semantics;
- it is not an accidental artifact of assignment or presentation.

For example, an output marginal may legitimately identify a constant candidate function.

A shortcut is **disqualifying** when it derives candidate identity from something that is not part of the intended evidence authority, such as:

- literal candidate-name leakage;
- systematic answer position;
- hidden differences in candidate availability;
- evidence quantity confounded with candidate identity;
- experimenter metadata that bypasses the declared scientific contrast.

## Under relational warranted G1

A non-relational cue can be semantically legitimate yet still make the ontology unsuitable for the relational claim.

That is not evidence of cheating by the system.

It is a measurement-design fact:

\[
\boxed{
\text{legitimate broad evidence channel}
\neq
\text{admissible channel for isolating relational authority}
}
\]

This distinction prevents the relational benchmark from redefining ordinary valid evidence use as failure merely because it is not mechanistically interesting.

---

# 14. Relation to the CCA mission

The program-level question is:

> Can an adaptive system increase its future viability while remaining capable of incorporating justified correction?

The earliest mechanism in that chain is not “relational reasoning.” It is:

\[
\text{valid evidence}
\rightarrow
\text{authority}
\rightarrow
\text{warranted change}.
\]

Broad G1 maps directly onto that requirement.

Relational warranted G1 answers an additional mechanistic question:

> Can one particular evidence structure—the relation instantiated by paired observations—acquire that authority independently of licensed non-relational channels?

Therefore relational evidence use is potentially highly informative for mechanism discrimination, representation research, and challenge-channel design, but it is not obviously constitutive of CCA itself.

This gives a partial ordering of scientific roles:

```text
CCA phenomenon
    ↓
evidence controls warranted selection
    ↓
possible mechanism-discrimination questions
    ├── relational extraction
    ├── marginal/statistical extraction
    ├── symbolic rule extraction
    └── other evidence channels
```

This hierarchy is a result of the fork analysis, not yet an authorization decision.

---

# 15. Relation to C_improve

`C_improve` is the provisional hypothesis that adaptive quality depends on the capacity to convert valid feedback into justified, validated transformation that improves future viability without destroying future correctability.

Its upstream requirement is therefore:

\[
\boxed{
\text{valid feedback acquires warranted causal authority}
}
\]

Broad G1 is directly aligned with that requirement.

Relational G1 would add information about **how** one class of valid feedback is interpreted, but `C_improve` currently contains no commitment that relational extraction is necessary for correction-capable adaptation.

Thus:

\[
\boxed{
G_1^{\mathrm{relational}}
\text{ is not presently required by }C_{\mathrm{improve}}
}
\]

unless the theory is later revised prospectively to make relational structure constitutive.

A relational result may improve mechanism understanding without increasing the program-level claim about future viability.

---

# 16. Downstream authorization consequences

Neither formulation currently authorizes downstream execution because no Level-1 contract is frozen.

Conceptually, however, successful broad G1 could establish the selection prerequisite needed before combining selection with direct modification assays:

\[
E
\rightarrow
C^*(E)
\]

followed independently by

\[
do(M=m)\rightarrow(Y_T,Y_P).
\]

Successful relational warranted G1 could authorize the **same** downstream mechanism question while adding a scoped explanation of the evidence channel.

Relational success does not authorize a qualitatively different G2.

The direct-\(do(M)\) requirement remains unchanged.

Likewise, neither broad nor relational G1 success authorizes:

```text
repeated correction
justified transformability
viability
capability growth
AGI / recursive improvement / ASI
```

Those remain separate gates.

---

# 17. Is relational strictly stronger, different, or nested?

The answer depends on the definition.

## Case A — relation dependence only

If relational G1 means only:

> the pairing relation causally changes selection,

then:

\[
\boxed{
G_1^{\mathrm{relational}}
\text{ and }
G_1^{\mathrm{broad}}
\text{ are different, non-nested claims.}
}
\]

Relational dependence can exist with wrong selection; broad warranted selection can exist without relational dependence.

## Case B — relational warranted selection

If relational G1 means:

> evidence controls selection toward \(C^*(E)\) on contrasts where the warrant-relevant difference is relational beyond licensed non-relational channels,

then:

\[
\boxed{
G_1^{\mathrm{rel\text{-}warrant}}
\subset
G_1^{\mathrm{broad}}
}
\]

on the shared admissible domain.

It is a **stronger per-contrast claim but a narrower-domain claim**.

This produces an important non-total ordering:

```text
broad G1
→ greater scope / weaker mechanism attribution

relational warranted G1
→ narrower scope / stronger channel attribution
```

So “stronger” cannot be treated as a single scalar property.

---

# 18. The current fork may mix scientific levels

The analysis suggests that the apparent fork may partly arise because the two formulations live at different explanatory levels:

```text
BROAD G1
outcome-level causal property:
Does evidence govern warranted selection?

RELATIONAL G1
possible mechanism/channel restriction:
Does warranted selection specifically depend on pair relations
beyond licensed non-relational channels?
```

If that decomposition is accepted later, the architecture could become:

```text
CCA
 ↓
G1: evidence-controlled warranted selection
 ↓
mechanism-discrimination layer
 ├── relational evidence use
 ├── marginal/statistical evidence use
 └── other evidence channels
```

But this document does **not** promote that decomposition to canonical state.

It only establishes that the two current formulations should not be compared as if they were automatically symmetric alternatives.

---

# 19. Adversarial questions each formulation must survive

## Broad G1

1. Does “warranted” have an independent oracle, or does model behavior define correctness?
2. Can a positive result be generated by assignment leakage rather than evidence semantics?
3. Does broadness make the object so permissive that any candidate-correlated cue counts as evidence use?
4. What distinguishes legitimate evidence compression from accidental benchmark artifacts?
5. Is the resulting claim sufficiently informative to support the next CCA gate?
6. Does the object transport across evidence modalities or only within one frozen representation?

## Relational warranted G1

1. Why should relational extraction be privileged by the CCA scientific question?
2. Is the ontology selected because it permits the desired claim rather than because it represents an independently motivated adaptive problem?
3. Can relational authority actually be isolated without semantic recoding?
4. Is the licensed nuisance class scientifically justified or benchmark-engineered?
5. Could a relational benchmark reject a system that is using valid evidence perfectly well through a different channel?
6. Does stronger internal mechanism identification come at unacceptable loss of external relevance?
7. Can the relational claim be stated without implying a unique internal representation?

Neither side currently answers all of these questions prospectively.

---

# 20. What would falsify the value of each formulation as the Level-1 object?

This is a scientific-object question, not an empirical model result.

## Broad G1 would be a poor primary object if

- it cannot distinguish legitimate evidence authority from arbitrary candidate-correlated leakage under a principled intervention contract;
- its positive claim is too weak to constrain downstream mechanism explanations;
- different evidence channels produce nominally identical “success” while carrying incompatible scientific meanings that matter for CCA.

## Relational G1 would be a poor primary object if

- relational structure is not theoretically required by CCA or `C_improve`;
- the admissible ontology class becomes so engineered that success has little bearing on correction-capable adaptation outside the benchmark;
- the mechanism claim can be obtained more cleanly as a secondary discrimination layer after broad warranted selection is established;
- relational feasibility depends on representational choices that constitute a different scientific object than the evidence use CCA ultimately cares about.

These are criteria for future object selection. They are not yet resolved.

---

# 21. Provisional analytical result

The fork analysis supports four conclusions without selecting a formulation.

### Result 1 — broad and relational are not automatically peer alternatives

Broad G1 is naturally an outcome-level causal claim about warranted evidence control.

Relational G1 can denote either a different channel-dependence claim or a stricter restricted form of broad warranted selection.

### Result 2 — nesting requires preserving warrant

The proposed hierarchy

\[
G_1^{\mathrm{relational}}
\subset
G_1^{\mathrm{broad}}
\]

is scientifically valid only for **relational warranted selection**, not relation sensitivity alone.

### Result 3 — relational strength trades against scope

Relational warranted G1 can provide stronger channel attribution on each admissible contrast, but only over an ontology class that permits that attribution.

It is therefore stronger in mechanism resolution and narrower in scope.

### Result 4 — the CCA mission currently privileges neither internal channel

CCA requires valid evidence to acquire causal authority over warranted adaptive change.

Nothing in the current mission or `C_improve` hypothesis makes relational evidence extraction constitutive of correction-capable adaptation.

That does not make relational measurement unimportant. It locates it as a candidate mechanism-discrimination layer unless a future scientific-object decision gives it a stronger role.

---

# 22. Authority boundary after this analysis

This document changes **no empirical or execution authority**.

```text
G1 broad vs relational         STILL UNRESOLVED
Level-0 lifecycle              STILL ADVERSARIAL_REVIEW
candidate ontology             UNFROZEN
evidence intervention space    UNFROZEN
ECIM contract                  UNFROZEN
model / prompt                 NOT SELECTED
implementation                 NOT AUTHORIZED
execution                      NOT AUTHORIZED
research_state.json            UNCHANGED
```

The next legitimate scientific move is to adversarially evaluate the analytical decomposition itself:

> Are broad warranted selection and relational channel attribution genuinely different scientific levels, or does CCA require the relational restriction to be part of the primary definition of evidence use?

No implementation follows from this document.

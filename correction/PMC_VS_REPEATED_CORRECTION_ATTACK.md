# Attack: Is Post-Modification Correctability Distinct from Repeated Correction?

## Status

**ADVERSARIAL SCIENTIFIC ANALYSIS — NO STATE TRANSITION — NO METRIC — NO IMPLEMENTATION — NO EXECUTION**

This document attacks the conceptual distinction provisionally adopted by Correction-Capable Adaptation (CCA):

\[
\boxed{
\mathrm{PMC}\neq\mathrm{Repeated\ Correction}
}
\]

The question is:

> **Is Post-Modification Correctability (PMC) a scientifically distinct latent property of a changed system and its correction environment, or is it merely another name for the fact that a later correction actually occurs?**

This attack is deliberately upstream of measurement construction.

It does **not**:

- define a PMC metric;
- define \(C_{\mathrm{corr}}\);
- freeze \(\Omega\);
- freeze a system boundary or horizon;
- freeze a repeated-correction protocol;
- define a required number of correction episodes;
- choose a model, prompt, benchmark, ontology, estimator, or threshold;
- define `C_improve`;
- modify `research_state.json`;
- authorize implementation or execution.

---

# 1. Canonical starting point

CCA provisionally adopts PMC in role only:

> **After a consequential change, do the conditions required for future warranted correction remain available?**

The causal content is intentionally stronger than generic flexibility:

\[
\text{future admissible evidence}
\leadsto
\text{warranted causal authority}
\leadsto
\text{consequential correction}.
\]

PMC is not yet a frozen metric or state scalar.

Repeated correction is currently a downstream empirical object: another valid correction episode actually occurs after a prior consequential correction.

The provisional dependency is:

\[
\boxed{
\text{one valid correction}
\rightarrow
\text{preserved capacity for another}
\rightarrow
\text{actual repeated correction}.
}
\]

The present attack asks whether the middle object has independent scientific content.

---

# 2. First distinction: disposition versus realization

PMC is naturally a **dispositional / counterfactual availability claim**.

Repeated correction is a **realized trajectory claim**.

A schematic PMC statement might eventually have the form:

\[
\mathrm{CorrAvail}(S_{t+1};\Omega)=1,
\]

meaning that under a declared future-correction scope \(\Omega\), relevant admissible evidence can still acquire warranted authority and reach consequential change through a path-valid process.

A repeated-correction statement instead requires an actual later episode:

\[
S_{t+1}
\xrightarrow{E_{t+1}}
S_{t+2}
\]

that itself satisfies the scientific conditions for valid correction.

These are not logically identical.

A disposition can exist without being exercised.

An exercised pathway can reveal that some disposition existed, but it need not establish a broader disposition over unexercised opportunities.

This is the central asymmetry to attack.

---

# 3. Attack A — PMC without repeated correction

Construct a changed system \(S_{t+1}\) for which the relevant future correction machinery is intact:

- admissible future evidence can still enter;
- warrant can still be determined;
- authority can still update;
- a warranted adaptive decision/change remains possible;
- the path to consequential modification is valid within the declared scope.

Suppose, however, that no new correction-relevant evidence arrives during the observation window.

Then no second correction episode occurs.

Yet the system may still be correctable.

Therefore:

\[
\boxed{
\mathrm{PMC}>0
\not\Rightarrow
\text{observed repeated correction}.
}
\]

This counterexample succeeds unless PMC is defined behaviorally as “a second correction happened,” in which case PMC collapses into repeated correction by definition and loses its intended role.

## 3.1 Opportunity absence

Let \(O_{t+1}=0\) denote that no admissible future correction opportunity occurs in the observation window.

Then:

\[
\mathrm{CorrAvail}(S_{t+1};\Omega)=1,
\qquad
O_{t+1}=0,
\]

can coexist with:

\[
\mathrm{RepeatedCorrection}=0.
\]

The absence of a realized second correction cannot therefore identify absence of PMC unless the contract guarantees a discriminating future correction opportunity.

This is a measurement consequence, not yet a metric proposal.

## 3.2 Deferred opportunity

A system may remain correctable at \(t+1\) even if the next relevant evidence arrives only at \(t+k\).

Thus an observation horizon can truncate realization without destroying the latent capacity.

A future PMC contract must therefore avoid equating “not exercised within horizon \(H\)” with “not available,” unless the opportunity process is itself prospectively part of the object.

### Result of Attack A

\[
\boxed{
\text{PMC is not sufficient for realized repeated correction.}
}
\]

Additional opportunity and execution conditions are required.

---

# 4. Attack B — repeated correction as a local witness, not broad PMC

Now suppose a valid second correction actually occurs.

Does that establish PMC?

For the **specific realized correction opportunity**, some suitable correction path must have been available immediately before the episode, assuming:

1. the system boundary is fixed;
2. the episode itself is genuinely warranted correction rather than external overwrite or scripted replay;
3. the causal path satisfies the CCA Causal Composition Principle.

Therefore a valid repeated correction can witness a **localized realized availability**.

But it does not automatically establish broad PMC over a larger future-correction scope \(\Omega\).

## 4.1 Narrow-route witness

Suppose \(\Omega\) prospectively contains ten materially distinct future correction opportunities.

After modification, the system retains exactly one hard-coded correction route and loses the other nine.

The retained opportunity happens to occur next.

A valid second correction succeeds.

Then:

\[
\mathrm{RepeatedCorrection}=1
\]

while broad correctability over \(\Omega\) may be severely degraded.

Thus:

\[
\boxed{
\text{one repeated-correction episode}
\not\Rightarrow
\text{broad PMC over an untested correction scope}.
}
\]

## 4.2 Memorized-sequence witness

Suppose the system is modified to execute a known two-step sequence:

```text
if correction opportunity A occurs, apply update A
then if correction opportunity B occurs, apply update B
```

Both episodes occur and look like repeated correction.

But the system may have lost any ability to incorporate novel warranted evidence outside that pre-installed sequence.

Repeated execution of a scripted trajectory is not automatically evidence of general preserved correctability.

The scientific authority is local to the correction opportunities actually identified by the contract.

### Result of Attack B

A valid repeated correction may imply that **some episode-specific PMC-like path existed**, but it does not establish a broader latent correctability object without independent scope and measurement.

This supports distinction rather than equivalence.

---

# 5. Attack C — external apparatus can create repeated correction without system-internal PMC

Suppose the changed adaptive system has lost its own revision interface.

An external controller nevertheless observes future evidence and overwrites the system state:

\[
E_{t+1}
\rightarrow
H_{\mathrm{external}}
\rightarrow
M_{t+1}
\rightarrow
S_{t+2}.
\]

Operationally, a second correction occurs.

If the system boundary excludes the controller, this does not establish system-internal PMC.

If the system boundary includes the controller as part of the correction-capable system, the claim is different.

Therefore:

\[
\boxed{
\text{repeated correction}
\not\Rightarrow
\text{system-internal PMC}
}
\]

without a frozen system/apparatus boundary.

This reproduces the apparatus distinction already required by the CCA Causal Composition Principle.

### Result of Attack C

The PMC/repeated-correction relation is boundary-sensitive.

A realized episode alone cannot resolve which component retained correctability.

---

# 6. Attack D — repeated correction requires more than latent availability

Suppose PMC is present.

A second correction still requires at least some realization process:

```text
future opportunity occurs
→ evidence is delivered
→ warranted authority is acquired
→ required path is activated
→ modification is instantiated
→ consequences are validly assessed
```

Failure of repeated correction can therefore occur despite PMC-like latent availability if:

- no discriminating evidence arrives;
- the opportunity is outside the observation horizon;
- resources needed for execution are temporarily absent but not structurally lost;
- a stochastic adoption process does not activate on that episode;
- the scientific measurement fails to instantiate the correction opportunity validly.

These cases differ from structural loss of correctability.

Thus:

\[
\boxed{
\text{failure to observe repeated correction}
\neq
\text{identified loss of PMC}.
}
\]

A future repeated-correction experiment must distinguish opportunity failure, execution failure, and correctability failure.

---

# 7. Attack E — a trivial existential PMC would be too weak

One possible definition is:

> PMC exists if there is at least one future evidence condition under which the changed system can be corrected.

This existential object is scientifically weak.

A system that retains one trivial correction path while losing every consequentially relevant correction route would satisfy it.

Then a single repeated correction could nearly collapse PMC into a witnessed existence statement.

Therefore PMC needs a prospectively scoped correction opportunity set or distribution if it is to carry more information than “there exists one surviving path.”

This does **not** freeze how that scope should be represented.

It establishes only:

\[
\boxed{
\text{PMC scope cannot be supplied retrospectively by whichever correction happened to succeed.}
}
\]

---

# 8. Attack F — repeated correction count is not correction capacity

Suppose a system can repeat the same easy correction one hundred times but cannot incorporate a different warranted correction.

A count-based repeated-correction score would be high.

Yet the system's correction opportunity set may be extremely narrow.

Conversely, another system may undergo only two difficult, structurally distinct warranted corrections but preserve a much broader future correction repertoire.

Therefore:

\[
\boxed{
\text{number of correction episodes}
\neq
\text{post-modification correction capacity}.
}
\]

Repeated correction is a trajectory property. PMC is intended to concern the availability structure that makes future trajectory continuations possible.

Neither should be reduced to the other.

---

# 9. Attack G — broad PMC can become unfalsifiable if treated as pure possibility

The distinction has a danger in the opposite direction.

If PMC is defined only as:

> “the system could have been corrected under some unobserved future condition,”

then a negative PMC result may become impossible to establish.

Any failed correction could be explained away by claiming the wrong evidence, horizon, resource envelope, or realization was used.

Therefore a scientifically useful PMC object must eventually prospectively constrain its correction environment or opportunity scope.

Conceptually:

\[
\boxed{
\text{dispositional does not mean unconstrained counterfactual.}
}
\]

The role survives only if future operationalization makes the disposition falsifiable under a declared scope.

This is another reason not to freeze PMC as a vague statement that “the system can still be corrected somehow.”

---

# 10. A candidate causal decomposition

Without freezing a measurement contract, the attack suggests a useful logical decomposition:

\[
\boxed{
\mathrm{PMC}(S_{t+1};\Omega)
+
\mathrm{Opportunity}_{t+1}(e\in\Omega)
+
\mathrm{ValidActivation/Execution}
\leadsto
\mathrm{RepeatedCorrectionEpisode}_{t+1}
}
\]

This is schematic only.

It is not an estimand or structural model.

The important point is that the terms answer different questions:

### PMC

Was a warranted correction path available after the prior modification within the declared correction scope?

### Opportunity

Did a future evidence condition requiring correction actually arise?

### Activation / execution

Was the available correction process validly exercised rather than blocked by transient execution or measurement failure?

### Repeated correction

Did a subsequent valid correction episode actually occur?

This decomposition explains why PMC and repeated correction need not be identical.

---

# 11. Necessary versus sufficient relations

The attack supports an asymmetric relationship.

## 11.1 PMC is not sufficient for repeated correction

Because opportunity and realization may be absent:

\[
\boxed{
\mathrm{PMC}
\not\Rightarrow
\mathrm{RepeatedCorrection}.
}
\]

## 11.2 Repeated correction is not sufficient for broad PMC

Because one realized route does not establish the wider correction scope:

\[
\boxed{
\mathrm{RepeatedCorrectionEpisode}
\not\Rightarrow
\mathrm{PMC}(\Omega_{\mathrm{broad}}).
}
\]

## 11.3 Episode-specific necessity

For a genuine repeated correction episode under a fixed system boundary and valid causal path, an episode-specific correction pathway must have been available immediately before it.

Schematically:

\[
\boxed{
\mathrm{ValidRepeatedCorrection}(e)
\Rightarrow
\mathrm{LocalCorrAvail}(e)
}
\]

for the realized opportunity \(e\).

But:

\[
\mathrm{LocalCorrAvail}(e)
\not\Rightarrow
\mathrm{PMC}(\Omega)
\]

for a broader \(\Omega\) without additional evidence.

This is the strongest surviving connection found by the attack.

---

# 12. PMC as latent precondition is not a reason to delete it

The attack supports the statement:

> PMC is a latent precondition for repeated correction in the sense that an actual second valid correction requires some correction pathway to remain available beforehand.

But being a latent precondition does not make PMC scientifically redundant.

The distinction is useful because it separates:

```text
capacity survived
```

from:

```text
capacity happened to be exercised successfully
```

That separation matters whenever:

- future opportunities are stochastic;
- observation horizons are finite;
- correction opportunities vary in type;
- only some correction routes survive;
- apparatus/system boundaries differ;
- repeated episodes are too sparse to characterize the latent opportunity structure.

Thus the fact that PMC is a precondition is an argument for its placement immediately upstream of repeated correction, not necessarily for collapsing the two objects.

---

# 13. Relation to preservation and improvement

This attack still does not establish whether PMC was preserved relative to \(S_t\).

A level statement:

\[
\mathrm{PMC}(S_{t+1};\Omega)
\]

is distinct from a change statement:

\[
\Delta\mathrm{PMC}
=
\mathrm{PMC}(S_{t+1};\Omega)
-
\mathrm{PMC}(S_t;\Omega).
\]

Even this notation is illustrative only.

A valid preservation/degradation claim will eventually require comparability across states and a prospectively frozen correction scope.

Likewise:

\[
\boxed{
\text{PMC preserved}
\not\Rightarrow
\text{PMC improved}.
}
\]

and:

\[
\boxed{
\text{PMC improved}
\not\Rightarrow
\text{adaptive viability improved}.
}
\]

Therefore `C_improve` remains downstream.

---

# 14. Refuted propositions

The attack refutes the following strong claims.

## R1 — PMC equals a second successful correction

\[
\boxed{
\mathrm{PMC}
\equiv
\mathrm{RepeatedCorrection}.
}
\]

False: capacity may survive without being exercised.

## R2 — absence of repeated correction proves loss of PMC

\[
\boxed{
\neg\mathrm{RepeatedCorrection}
\Rightarrow
\neg\mathrm{PMC}.
}
\]

False without a prospectively guaranteed discriminating correction opportunity and valid execution.

## R3 — one second correction establishes broad future correctability

\[
\boxed{
\mathrm{RepeatedCorrectionEpisode}
\Rightarrow
\mathrm{PMC}(\Omega_{\mathrm{broad}}).
}
\]

False. It supports only the correction path and scope actually identified.

## R4 — repeated correction count measures correction capacity

\[
\boxed{
N_{\mathrm{corrections}}
= C_{\mathrm{corr}}.
}
\]

Not established and generally false without assumptions about opportunity breadth and difficulty.

## R5 — pure possibility is a sufficient PMC definition

\[
\boxed{
\exists e:\text{correction possible under }e
\Rightarrow
\text{scientifically adequate PMC}.
}
\]

Too weak unless the relevant correction scope is prospectively constrained.

---

# 15. Surviving propositions

## S1 — PMC and repeated correction are scientifically distinct in principle

PMC is a scoped latent availability property.

Repeated correction is a realized valid trajectory event.

## S2 — PMC is a plausible immediate precondition for repeated correction

A genuine subsequent correction requires some relevant correction pathway to have remained available beforehand.

## S3 — realized repeated correction provides only local authority by default

A successful second episode establishes that the realized correction path existed and worked under its identified conditions. It does not automatically establish broad latent correctability.

## S4 — opportunity and execution must be separated from correctability

Failure to realize a second correction may arise because no opportunity occurred or because execution failed, even when a correction path remained structurally available.

## S5 — PMC requires prospective scope to remain falsifiable

The future-correction environment cannot be defined retrospectively around whichever correction succeeded or failed.

---

# 16. Candidate result

The attack supports preserving the conceptual distinction:

\[
\boxed{
\mathrm{PMC}\neq\mathrm{RepeatedCorrection}.
}
\]

More precisely:

> **Post-Modification Correctability is a prospectively scoped latent availability property: after consequential change, relevant future admissible evidence can still acquire warranted causal authority over consequential correction through path-valid processes. Repeated correction is the realized event that such a pathway is actually exercised successfully for a subsequent correction opportunity.**

The relationship is asymmetric:

\[
\boxed{
\mathrm{PMC}
\not\Rightarrow
\mathrm{RepeatedCorrection}
}
\]

and:

\[
\boxed{
\mathrm{RepeatedCorrection}(e)
\Rightarrow
\mathrm{LocalCorrAvail}(e)
\not\Rightarrow
\mathrm{PMC}(\Omega_{\mathrm{broader}}).
}
\]

This is a candidate scientific conclusion only.

It is not a metric or empirical result.

---

# 17. Authority change

```text
EMPIRICAL AUTHORITY CHANGE             NONE
RESEARCH STATE TRANSITION              NONE
PMC METRIC                              NONE
PMC ENVIRONMENT / OMEGA                 NONE
REPEATED-CORRECTION CONTRACT            NONE
C_improve CANONICALIZATION              NONE
IMPLEMENTATION AUTHORIZATION            NONE
EXECUTION AUTHORIZATION                 NONE
```

The canonical PMC role remains provisionally fixed.

This attack does not modify that state.

---

# 18. Next decision boundary

If this attack survives review, the next program-level decision is whether CCA should preserve the explicit conceptual dependency:

\[
\boxed{
\text{one valid correction}
\rightarrow
\mathrm{PMC}
\rightarrow
\text{repeated correction}
}
\]

with PMC interpreted as a prospectively scoped latent availability object and repeated correction as a realized subsequent correction event.

Only after that decision should CCA attack what a future PMC contract must preserve or expose across \(S_t\rightarrow S_{t+1}\).

No empirical implementation follows from this analysis.

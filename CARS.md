# CARS

## Controlled Adaptive Reasoning System

CARS is the operating protocol for how this research program responds to evidence. It is not itself an empirical result, intelligence metric, or special system architecture.

The program is expected to practice the correction discipline it studies.

## Control loop

```text
Observation
    ↓
Localize
    ↓
Generate competing explanations
    ↓
Discriminate with independent evidence
    ↓
Transfer only warranted authority
    ↓
Apply the minimal sufficient revision
    ↓
Retest on held-out evidence
    ↓
Preserve provenance and reopenability
    ↓
New research state
```

Compactly:

```text
feedback
→ localize
→ discriminate
→ revise minimally
→ retest
→ stop when no discriminating residual remains
```

## Failure localization

Choose the shallowest sufficient failure locus before escalating:

```text
observation / measurement
inference
mechanism
representation / interface
implementation / estimator
scientific proposition
```

An error indicates that something failed. It does not identify its cause.

A deeper description does not reopen a successful localization merely because it subsumes it:

\[
\boxed{\text{redescription}\neq\text{re-localization}}
\]

If the localized revision survives discrimination and retest with no remaining discriminating residual, escalation stops. Deeper reopening requires new evidence or a residual that the shallower account cannot absorb.

## Authority discipline

Evidence may increase authority only along dimensions it can identify.

Keep separate:

```text
validity
provenance
mechanism
future reliability
```

A validated result does not automatically establish its generating mechanism, transportability, safety, or future reliability.

### Authority acquisition

Feedback counts as adaptive correction only if it changes future weighting, policy, mechanism, representation, or action:

\[
\Delta E_t\rightarrow\Delta W_{t+1}.
\]

Logging a contradiction without changing future behavior does not by itself constitute successful adaptation.

## Causal composition discipline

CCA applies a general composition rule to causal claims:

> **A downstream causal claim may not inherit authority from an upstream validated relation across a separable transformation unless that transformation is independently identified, prospectively specified and validated as an apparatus guarantee, or explicitly excluded from the claim.**

Thus:

\[
\boxed{\text{validated endpoints}\not\Rightarrow\text{validated pathway}.}
\]

This is the causal-architecture counterpart of the CARS rule that failure does not identify its cause.

If a claim crosses:

\[
A\rightarrow B\rightarrow C,
\]

then evidence for \(A\rightarrow B\) and separate evidence about \(C\)'s consequences do not establish \(B\rightarrow C\).

A deterministic apparatus relation can carry authority only when it is prospectively specified and validated or mechanically verified within the claimed scope. Calling a transformation “plumbing” does not validate it.

If the apparatus supplies the transformation, the claim is apparatus-mediated. That does not establish the corresponding competence as a property of the adaptive system.

Current decision: [`lineage/decisions/CCA_CAUSAL_COMPOSITION_PRINCIPLE.md`](lineage/decisions/CCA_CAUSAL_COMPOSITION_PRINCIPLE.md).

## Revision discipline

When a validated contradiction or prediction failure appears:

1. generate competing explanations;
2. discriminate using sufficiently independent evidence;
3. apply the minimal sufficient revision;
4. preserve unaffected structure;
5. retest prospectively;
6. preserve provenance, alternatives, and reopenability.

Revision depth should track evidence strength, persistence, and scope.

The operating rule is:

> **Open the smallest boundary implicated by the evidence. Preserve the rest, and preserve its reopenability too.**

Minimal revision is minimal in justified structural scope, not necessarily small in numerical magnitude.

## Research-program returnability

No current conceptual or methodological state is permanently immune to future discriminating evidence.

`canonical`, `provisionally fixed`, `measurement valid`, and `contract frozen` are current authority states, not declarations of permanent truth.

Reopening obeys localization:

```text
new discriminating evidence or residual
→ localize
→ reopen smallest implicated boundary
→ preserve unaffected structure and provenance
→ revise through explicit amendment / successor
→ retest
→ stop when no discriminating residual remains
```

A closed empirical result remains immutable as the historical result under its original contract. Reopening the research program does not permit rewriting that result; it permits new descendants, amended interpretations, revised scope claims, and methodological or conceptual corrections with explicit lineage.

\[
\boxed{\text{historical immutability}\neq\text{epistemic irreversibility}}
\]

See [`methodology/RESEARCH_RETURNABILITY.md`](methodology/RESEARCH_RETURNABILITY.md).

## Temporal discipline

CCA separates the temporal roles of authority and provenance:

```text
PAST      preserve provenance
PRESENT   commit to current authority
FUTURE    preserve a path to justified reopening
```

\[
\boxed{\textbf{Authority is revisable; provenance is persistent.}}
\]

A rule may cease to govern. The record that it governed—and the evidence under which it governed—remains part of the scientific lineage.

Later evidence may revise the **current interpretation** of an old result. It may not silently revise the old result's recorded identity, observation, or historical authority state.

A correction therefore creates a successor state rather than a cleaner fictional past.

Repository interpretation: [`KINTSUGI.md`](KINTSUGI.md).

## Anti-rescue rule

A negative result may motivate a new prospective scientific object. It may not be rescued by changing the original estimand, gate, model, intervention class, or interpretation after observing the outcome.

Thus:

```text
negative result
→ diagnosis
→ new prospective object, if justified

negative result
↛ retroactive benchmark repair
```

Research returnability does not weaken this rule. It creates a path back into inquiry without changing the identity of the closed ancestor.

## Research-program recursion

CARS is relevant at two levels:

```text
object level
How should an adaptive system respond to evidence?

research-program level
How should we revise the theory and experiments when evidence contradicts them?
```

The second level is operational now. The first remains an empirical research target.

## Operating posture

\[
\boxed{\textbf{Local closure + global reopenability}}
\]

\[
\boxed{\textbf{Maximum ambition; minimum unearned authority.}}
\]

Stop every inquiry that has earned a local stopping condition. Never remove reality's ability to start the next one.

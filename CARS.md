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

## Revision discipline

When a validated contradiction or prediction failure appears:

1. generate competing explanations;
2. discriminate using sufficiently independent evidence;
3. apply the minimal sufficient revision;
4. preserve unaffected structure;
5. retest prospectively;
6. preserve provenance, alternatives, and reopenability.

Revision depth should track evidence strength, persistence, and scope.

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

## Research-program recursion

CARS is relevant at two levels:

```text
object level
How should an adaptive system respond to evidence?

research-program level
How should we revise the theory and experiments when evidence contradicts them?
```

The second level is operational now. The first remains an empirical research target.

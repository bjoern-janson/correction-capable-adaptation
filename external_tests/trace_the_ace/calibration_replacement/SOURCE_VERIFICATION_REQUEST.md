# Source verification request — Trace the Ace calibration evidence

## Status

**PROSPECTIVE OUTBOUND VERIFICATION PACKET — NOT YET SENT**

This request is downstream of the source-admissibility diagnostic in PR #47. It does not request permission to alter the calibration construct, the 25% practical non-inferiority decision, the competition target, or the historical evidence. Its sole purpose is to determine whether a legitimately admissible, target-equivalent, independently sampled additional cohort can be constituted.

## Governing question

Does there exist a cohort `C` satisfying all source-admissibility requirements `S1`–`S7` below, and if so, what independent quantity is available after all admissibility filters?

A source is `VERIFIED_ADMISSIBLE` only if:

```text
S1 & S2 & S3 & S4 & S5 & S6 & S7
```

## Information quantity required by the predecessor diagnostic

The prior synthetic-oracle information-scaling result identified the first jointly passing tested multiplier at:

```text
m_min_joint = 4
responses-equivalent total = 140,288
independent session-clusters total = 91,284
```

Relative to the current Trace the Ace evidence base, this corresponds to approximately:

```text
additional response-equivalents = 105,216
additional independent session-clusters = 68,463
```

These values are a tested-grid information requirement under the synthetic oracle regime. They are **not** a claim that exactly this many real observations are necessary, nor permission to manufacture pseudo-replicates from existing data.

## Requested source packet

Please confirm, for any candidate cohort that could be made available or authorized:

### S1 — Independent information

1. Is the cohort composed of genuinely new tutoring sessions rather than duplicated/resampled existing competition sessions?
2. Can student/session identity be used to demonstrate independence from the Trace the Ace training data?
3. If students have repeated sessions, can the grouping structure be supplied so effective independent session/student units can be preserved?

### S2 — Tutoring precedes assessment

4. Does each observation contain a tutoring interaction followed by a distinct assessment event?
5. Can the temporal ordering `tutoring -> assessment` be verified from the source protocol or timestamps?

### S3 — Exact target equivalence

6. What is the post-tutoring outcome variable?
7. Is it the correctness of the student's next assessment question on the same topic / learning objective, or an operationally equivalent outcome?
8. If not identical, please provide the exact assessment protocol and target definition so transport / scientific-object equivalence can be evaluated explicitly rather than assumed.

### S4 — Competition-data separation / contamination control

9. Is the candidate cohort disjoint from all Trace the Ace train and hidden-test observations?
10. Can disjointness be verified at the provider, student, session, item / question, learning-objective, and collection-window levels to the extent those identifiers exist?
11. Was any part of the cohort used to construct, label, sample, tune, or evaluate the competition data?

### S5 — Transport / protocol comparability

12. Which tutoring provider(s), student population(s), subject/domain(s), grade bands, tutor types, and interaction protocols generated the cohort?
13. How closely do the tutoring protocol, assessment timing, learning-objective definition, and target construction match Trace the Ace?
14. Are there known selection, intervention, or platform differences that would require a separate transportability contract before pooling evidence?

### S6 — Legal / competition admissibility

15. What license, data-use agreement, or research-use terms govern the cohort?
16. Do those terms permit use in this competition and permit organizer verification of the external resource / derived submission?
17. Are there privacy, redistribution, commercial-use, or model-training restrictions that would block use?
18. Can the competition organizers explicitly confirm that use of this cohort is permitted under the external-data rules?

### S7 — Sufficient independent quantity

19. After all disjointness, target-equivalence, licensing, and quality filters, how many observations remain?
20. Please report at minimum:

```text
number of response / assessment observations
number of tutoring sessions
number of unique students, if available
number of learning objectives / topics
collection dates
```

21. If less than the predecessor tested-grid requirement is currently available, is there a larger existing cohort from the same protocol that could be authorized without changing the target object?

## Requested answer format

For each candidate source/cohort, please provide:

```text
source / cohort name:
provider / owner:
collection period:
S1 independent information: PASS / FAIL / UNVERIFIED — evidence:
S2 tutoring before assessment: PASS / FAIL / UNVERIFIED — evidence:
S3 target equivalence: PASS / FAIL / UNVERIFIED — evidence:
S4 contamination / separation: PASS / FAIL / UNVERIFIED — evidence:
S5 transport: PASS / FAIL / UNVERIFIED — evidence:
S6 legal / competition admissibility: PASS / FAIL / UNVERIFIED — evidence:
S7 independent quantity: PASS / FAIL / UNVERIFIED — evidence:
post-filter observations:
post-filter sessions:
post-filter students:
license / DUA:
organizer confirmation:
notes / unresolved items:
```

## Interpretation rule

The response will be classified prospectively as:

```text
VERIFIED_ADMISSIBLE
PLAUSIBLE_UNVERIFIED
REJECTED_AS_DIRECT_SOURCE
```

No source will be admitted merely because it is large, publicly described, or outcome-bearing. Missing proof of target equivalence, sample disjointness, rights, or post-filter quantity remains `UNVERIFIED` rather than being inferred.

## Authority ceiling

A successful response can establish only source availability/admissibility and permission to constitute an additional-evidence contract. It does not by itself authorize:

```text
replacement calibration measurement
historical calibration closure
AUTH(Gamma'_cal)
M_mature
Z_E / Z_D / Z_C / Z_P
```

The 25% practical decision object remains unchanged.
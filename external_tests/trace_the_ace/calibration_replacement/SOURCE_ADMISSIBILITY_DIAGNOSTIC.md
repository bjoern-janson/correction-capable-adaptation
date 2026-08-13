# Calibration source-admissibility diagnostic

## Status

**CANDIDATE-NEUTRAL SOURCE-CONSTITUTION DIAGNOSTIC — PUBLIC EVIDENCE SCAN RECORDED 2026-08-12**

This diagnostic opens only the evidence availability/admissibility boundary exposed by PR #46.

It does not alter the calibration construct, the 25% practical NI decision, the authorized decision gate, the information-scaling result, the competition target, or any historical M1-cal/M2-S vector. It does not synthesize new observations, duplicate existing sessions, pseudo-label hidden test cases, or select a replacement calibration operator.

Predecessor state:

```text
PR46:
D_additional_evidence = SUPPORTED_AS_INFORMATION_QUANTITY
m_min_decision_joint  = 4 on the frozen multiplier grid
n_min_decision_joint  = 140,288 response-equivalents
sessions_joint        = 91,284 independent session-clusters
scope                  = LOCAL_SYNTHETIC_ORACLE_INFORMATION_QUANTITY_ONLY
```

Relative to the canonical Trace-the-Ace training geometry, the tested joint threshold corresponds to an additional:

```text
105,216 response-equivalents
68,463 independent session-clusters
```

These quantities are information requirements from the synthetic oracle diagnostic, not permission to manufacture pseudo-replicates.

## Governing question

> Does a legitimately admissible source exist that can provide enough new independent, target-equivalent outcome-bearing evidence to support the unchanged Trace-the-Ace calibration decision?

The existence question is:

```text
exists source S such that S1 & S2 & S3 & S4 & S5 & S6 & S7
```

## Source gates

A source can be `VERIFIED_ADMISSIBLE` only if all seven gates are independently supported.

### S1 — independent information

The source must add genuinely new session-level outcome information. Duplicate rows, repeated resampling of the same sessions, additional utterances from the same informational unit, or synthetic copies do not count.

### S2 — tutoring precedes assessment

The source must instantiate a tutoring interaction followed by an assessment-bearing observation. Generic question-response logs without the relevant tutoring interaction fail this gate.

### S3 — target equivalence

The outcome must be scientifically compatible with the Trace-the-Ace target: correctness on the next assessment question on the same topic following the tutoring interaction.

"Learning labels", tutor-quality labels, dialogue-act annotations, historic correctness, broad pre/post scores, or progress measures do not acquire target authority merely because they concern learning.

### S4 — contamination / separation

The source must be demonstrably separable from the competition training and hidden test evidence. Hidden-test pooling, pseudo-labeling, or unknown overlap with the competition sample cannot count as independent evidence.

### S5 — transport

Population, tutoring protocol, assessment timing, subject/objective relation, and sampling process must be close enough to support the same calibration decision, or a separately authorized transport/scientific-object successor must be constituted first.

### S6 — legal and competition admissibility

Use must comply with the live Trace-the-Ace external-data rules. For prize eligibility, external data must support broad/commercial use, be legally usable, and be shareable/verifiable by organizers as required by the competition rules.

### S7 — sufficient independent quantity

The source must be capable of supplying enough independent target-bearing information to plausibly reach the tested information threshold. The frozen benchmark is the first joint passing point `m=4`; a smaller real source may still be scientifically useful, but it cannot directly satisfy the already-earned information-quantity diagnosis without a new quantitative successor.

## Classification states

```text
VERIFIED_ADMISSIBLE
  all S1-S7 supported by source-specific evidence

PLAUSIBLE_UNVERIFIED
  no decisive hard rejection has been established for the source family,
  but one or more required gates remain unverified

REJECTED_AS_DIRECT_SOURCE
  at least one required gate is decisively failed for the concrete release/object
```

A source family and a public release are separate objects. A public release may fail while a future/restricted cohort from the same source family remains plausible but unverified.

## Live competition constraints

Official Trace-the-Ace materials establish:

- competition data come from Third Space Learning (TSL) and Eedi;
- the target is whether the student answers the next assessment question on the same topic correctly after tutoring;
- external data are allowed subject to the stated rights/licensing and verification conditions;
- the default test-data rule prohibits pooling information across hidden test cases for training/pseudo-labeling and requires inference without test-dependent retraining.

Primary source:

```text
https://platform.k12-ai-infrastructure.org/competitions/3/tutoring-outcomes/page/4/
https://platform.k12-ai-infrastructure.org/competitions/3/tutoring-outcomes/
```

## Source ledger — public evidence available on 2026-08-12

### A. NTO / Million Tutoring Moves source family

**Classification: PLAUSIBLE_UNVERIFIED**

The National Tutoring Observatory states that it is building a large open-access tutoring repository and that the broader Million Tutor Moves (MTM) repository is intended to link educator moves to student outcomes. It also names multiple provider partners, including providers distinct from the Trace-the-Ace source providers.

Supported at source-family level:

```text
S1: PLAUSIBLE — multiple providers and large future repository can in principle add new cohorts
S2: PLAUSIBLE/SUPPORTED IN DESIGN — tutoring interactions are the core object
S3: PLAUSIBLE — NTO says broader MTM will link educator moves to student outcomes
S4: UNVERIFIED — a concrete disjoint cohort has not been identified
S5: UNVERIFIED — target/protocol transport has not been demonstrated
S6: UNVERIFIED — a concrete target-bearing release/license usable for the competition has not been identified
S7: PLAUSIBLE IN PROGRAM SCALE, UNVERIFIED AS AVAILABLE TARGET-BEARING DATA
```

Primary sources:

```text
https://nationaltutoringobservatory.org/
https://nationaltutoringobservatory.org/approach.html
```

No authority is granted from program aspirations alone.

### B. MTM v1 — 4,654 UPchieve math tutoring transcripts

**Classification: REJECTED_AS_DIRECT_SOURCE**

The MTM v1 paper identifies the concrete release as 4,654 authentic math tutoring transcripts from UPchieve. Its release scope is textual tutoring sessions for dialogue/instructional-process research; the paper does not expose a post-session next-question correctness outcome compatible with Trace the Ace.

Gate diagnosis:

```text
S1: SUPPORT AT PROVIDER LEVEL — UPchieve differs from the competition's stated TSL/Eedi providers
S2: PASS — authentic tutoring sessions
S3: FAIL — released object contains transcripts, not the required post-tutoring correctness outcome
S4: PLAUSIBLE BUT NOT PROVEN AT STUDENT LEVEL — provider source differs, exact sample overlap not established
S5: UNRESOLVED — provider/population/protocol transport not validated
S6: UNRESOLVED FOR DATASET — paper/open-access intent is not sufficient proof of the concrete dataset's competition license/shareability terms
S7: FAIL — 4,654 sessions is far below the 68,463 additional independent-session benchmark from PR46
```

Primary source:

```text
https://arxiv.org/abs/2605.08092
https://arxiv.org/html/2605.08092v1
```

This rejection applies to **MTM v1 as released**, not to all future NTO cohorts.

### C. Eedi Question-Anchored-Tutoring-Dialogues-2k (QATD-2k)

**Classification: REJECTED_AS_DIRECT_SOURCE**

The public Eedi release contains 1,971 tutoring interventions / 1,073 students and question metadata, but no post-tutoring next-question correctness target. Its dataset card states a noncommercial Creative Commons license. Because Trace the Ace itself includes Eedi data, independence/overlap would also require explicit proof even if the target and licensing defects were repaired.

Gate diagnosis:

```text
S1: UNRESOLVED — real interventions, but overlap with competition Eedi source cannot be excluded
S2: PASS — real tutoring dialogue anchored to a diagnostic question
S3: FAIL — no Trace-the-Ace-equivalent successor correctness label in the released object
S4: FAIL/UNRESOLVED AS DIRECT ADDITIONAL EVIDENCE — same provider as competition and no disjointness proof
S5: UNRESOLVED — same broad domain does not establish same target/sampling object
S6: FAIL FOR PRIZE-ELIGIBLE DIRECT USE — dataset card specifies CC BY-NC-SA / noncommercial use
S7: FAIL — 1,971 interventions is far below the required additional independent-session benchmark
```

Primary source:

```text
https://huggingface.co/datasets/Eedi/Question-Anchored-Tutoring-Dialogues-2k
```

### D. Public Eedi question-response competition datasets

**Classification: REJECTED_AS_DIRECT_SOURCE**

Eedi publicly releases large question-response datasets from prior education competitions. They can provide correctness information, but they do not instantiate the required tutoring-interaction -> next same-topic assessment outcome object.

Gate diagnosis:

```text
S1: potentially independent observations, exact overlap not established
S2: FAIL — tutoring interaction is not the defining precursor object
S3: FAIL — correctness logs are not the same post-tutoring target contrast
S4-S7: not reached for direct-source authority after S2/S3 failure
```

Primary source:

```text
https://www.eedi.com/research
```

### E. Third Space Learning internal tutoring/outcome corpus

**Classification: PLAUSIBLE_UNVERIFIED**

Third Space Learning publicly reports very large tutoring volumes and exit-ticket accuracy, including millions of human tutoring sessions. This makes TSL an empirically plausible holder of enough outcome-bearing observations. However, no public row-level external cohort has been verified that is simultaneously disjoint from the competition evidence, target-equivalent, permissively licensed/shareable for participant use, and available in sufficient form.

Gate diagnosis:

```text
S1: UNVERIFIED — competition itself already uses TSL; a disjoint additional cohort must be identified
S2: PLAUSIBLE/SUPPORTED IN PRODUCT PROCESS — tutoring sessions precede outcome reporting
S3: PLAUSIBLE BUT UNVERIFIED — public "exit ticket accuracy" is close in semantics but not sufficient proof of exact Trace-the-Ace target equivalence
S4: UNVERIFIED — no source-specific exclusion from competition train/test pools
S5: PLAUSIBLE BUT UNVERIFIED — same provider does not by itself establish identical sampling/protocol
S6: UNVERIFIED/NOT PUBLICLY CONSTITUTED — aggregate public claims are not a licensed/shareable row-level dataset
S7: PLAUSIBLE — reported session counts are numerically large enough, but usable independent target-bearing rows are not verified
```

Primary sources:

```text
https://thirdspacelearning.com/us/pricing/
https://thirdspacelearning.com/tutoring/ai-tutor/
```

### F. Eedi internal / RCT tutoring-outcome cohorts

**Classification: PLAUSIBLE_UNVERIFIED**

Eedi publicly describes tutoring efficacy studies and new data collection, but the public materials do not constitute a row-level external cohort satisfying exact target equivalence, disjointness from competition samples, competition-compatible rights, and the required independent quantity.

Primary sources:

```text
https://www.eedi.com/school
https://www.eedi.com/news/two-year-rct-earns-eedi-a-gold-efficacy-certificate-from-eduevidence
```

## Current diagnosis

No concrete public source currently earns:

```text
VERIFIED_ADMISSIBLE
```

The live state is therefore:

```text
D_source = POSSIBLE_BUT_UNVERIFIED
verified_admissible_sources = 0
```

This is not evidence that no admissible source exists.

The shallowest unresolved path is source-specific constitution/verification, especially through NTO / organizers / provider-held disjoint cohorts.

## What would close the source boundary

A source-specific evidence packet must provide enough information to adjudicate every gate without inference from reputation or aggregate scale. At minimum:

```text
1. cohort provenance and collection dates
2. tutoring-provider/source identity
3. unique session/student independence definition
4. assessment timing relative to tutoring
5. exact outcome schema and target mapping to Trace the Ace
6. overlap-exclusion procedure against competition train/test source pools
7. population/protocol/subject transport description
8. row/session counts after all admissibility filters
9. license / legal-use documentation
10. organizer-verifiability/shareability confirmation
```

If all S1-S7 pass, the source may become `VERIFIED_ADMISSIBLE` and an additional-evidence constitution contract can be opened.

If only nearby outcomes are available, a separate transport/scientific-object successor is required before those data may constrain the existing calibration object.

If concrete candidate sources repeatedly fail required gates and no plausible unverified family remains, only then may `D_availability = FAIL` become supportable.

## Authority ceiling

This diagnostic may establish only:

```text
publicly verifiable source-admissibility classifications
failure loci for concrete public releases
existence of plausible but unverified source families
```

It cannot establish:

```text
historical availability of undisclosed provider data
permission to use restricted/private data
transport equivalence from nearby outcomes
replacement-measurement authority
AUTH(Gamma'_cal)
historical calibration closure
M_mature
Z_E / Z_D / Z_C / Z_P
```

## Reachability

```text
PR46 D_additional_evidence support
-> D_source / evidence availability-admissibility
-> source-specific verification
-> if S1&...&S7: constitute additional legitimate evidence
-> otherwise preserve failure locus or open separately authorized transport successor
```

The decision object remains closed to revision at this stage.
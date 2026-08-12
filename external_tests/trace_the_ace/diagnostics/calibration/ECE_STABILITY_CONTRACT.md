# Calibration ECE-stability diagnostic

## Status

**PROSPECTIVE DIAGNOSTIC CONTRACT FROZEN — RESULT UNOBSERVED**

This diagnostic does not change the existing calibration gate and does not introduce another calibrator. It asks only whether the historical M2-S ECE-10 non-degradation failure relative to M1-cal is itself stable under the same session-cluster resampling principle used elsewhere in Trace the Ace.

The already-observed point values are fixed historical evidence:

```text
M1-cal ECE-10     0.015989848091338636
M2-S Platt ECE-10 0.016943779107667246
```

The diagnostic quantity is:

\[
\Delta ECE = ECE_{10}(M_{2,S}^{Platt}) - ECE_{10}(M_1^{cal}).
\]

## Frozen measurement

- ECE definition remains exactly 10 equal-width bins on `[0,1]`.
- Resampling unit is `session_id`.
- Paired session-cluster bootstrap, 2,000 replicates, seed `1723`.
- Both prediction vectors are evaluated on the same resampled session multiplicities in every replicate.
- No bin count, bin boundary, metric definition, or calibration map is changed after observing the diagnostic.

## Adjudication

```text
STABLE_DEGRADATION     iff point Delta ECE > 0 and CI95 lower > 0
STABLE_NONDEGRADATION  iff point Delta ECE <= 0 and CI95 upper <= 0
NOT_STABLY_IDENTIFIED  otherwise
```

This diagnostic cannot retroactively change the historical M2 or M2-S calibration verdict.

If `NOT_STABLY_IDENTIFIED`, the only authority gained is to open a methodological question about whether a deterministic ECE non-degradation gate should itself include uncertainty. Any such change would require an explicit methodological successor under the governing `Gamma_t`; it is not authorized by this diagnostic alone.

If `STABLE_DEGRADATION`, the existing calibration measurement failure is reinforced and the next move must remain inside the calibration apparatus/representation rather than changing the evidence rule merely because the result is inconvenient.

## Authority ceiling

No outcome earns mature-calibration authority, conditioning authority, CCA support, or authorization of `Z_E/Z_D/Z_C/Z_P` by itself.

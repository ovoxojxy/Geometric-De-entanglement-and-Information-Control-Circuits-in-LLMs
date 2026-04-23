# Hiccup #2 — LLM judge vs paraphrase (Phase 6)

**Date:** 2026-04-23  
**Severity:** lighter than Hiccup #1 — does not invalidate Tier-1 known-scheme recoverability; **does** block strong Tier-2 claims.

## Observation (stub-aligned)

`judge_paraphrase_stress_stub()` shows high AUROC on **canonical** covert phrasing and **~0.49** on **paraphrased** covert phrasing (illustrative). Same pattern echoed in `experiments/p6_illustrative_table.md` last row.

## Paper / protocol consequence

- Tier-2 blind judge metrics appear **only** with explicit caveat.  
- **Threats to validity** subsection appended to Google Doc #1 (scope / reading).  
- No hyperparameter search against judge until non-LLM detector path exists.

# Phase 6 — illustrative experiment table (stub / sim)

**Not empirical data.** Placeholder rows for joint schema QA before CUDA.

| run_id | shell_pool | cosine_sent_country | KL | delta_H | repeat | smear_flag | recover | judge_auroc_canonical | judge_auroc_paraphrase |
|--------|--------------|----------------------|-----|---------|--------|------------|---------|------------------------|-------------------------|
| v2_stub_a | v2_pool_v0 | 0.21 | 0.11 | -0.02 | 0.06 | false | 0.58 | 0.82 | 0.51 |
| v2_stub_b | v2_pool_v0 | 0.19 | 0.13 | -0.03 | 0.07 | false | 0.55 | 0.79 | 0.48 |
| hiccup2_row | v2_pool_v0 | 0.20 | 0.12 | -0.02 | 0.06 | false | 0.56 | 0.81 | **0.49** |

**Hiccup #2 narrative:** last column — judge AUROC **near chance** under paraphrased covert text while canonical wording stays high → judge not a validity instrument for Tier-2.

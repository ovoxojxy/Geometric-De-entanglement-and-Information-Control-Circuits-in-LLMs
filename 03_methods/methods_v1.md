# Methods v1 (draft — **not** agreed)

**Status:** Phase 3 parking lot. Do not cite as final protocol.

Primitives: **A** geometry · **B** circuits / leakage · **C** covert capacity.

---

## A — Concept-direction extraction & disentanglement (Alex, RA1)

### A1. Contrastive families
- Build paired prompts per concept (positive / negative) with **template randomization** across lexical frames (minimize format-only variance).
- Extract difference-in-means directions per layer **L** on residual stream activations at a fixed token position (mid-answer window).

### A2. Orthogonalization (v1)
- Apply LEACE-style linear projection / orthogonal complement **within layer L** against a bank of “nuisance” directions (format, length, register) estimated on held-out neutral prompts.

### A3. Evaluation (geometry)
- **Cosine pair matrix** across unrelated concept pairs (target: drive off-diagonal below τ while preserving on-concept steering via causal scrub / contrastive decoding checks).
- **Layer-local working hypothesis (v1):** primary disentangling signal is optimized **per-layer** before residual composition smears it; we sweep L on a small ladder first.

### A4. Risks (Alex)
- Template leakage can dominate cosines; v1 assumes randomization + held-out nuisance bank catches it.

---

## B — Circuits, ablations, leakage (Brent, RA2)

### B1. Induction identification
- Prefix-match + previous-token score on attention patterns; rank heads; define “induction set” as top-k by combined score (k tuned so ~65–72% copying mass if we replicate prior heuristic).

### B2. Ablations
- Zero-ablate induction set; record **token-level KL** vs unablated on copying-heavy prompts, **n-gram overlap** with context, **entropy** and **repetition** (distinct-1 / distinct-2) on generation.

### B3. Path patching (v1)
- Patch residual stream edges **layerwise** to localize where post-induction leakage re-enters (attention vs MLP). Start GPT-2-small for throughput.

### B4. Tension vs A (Brent)
- **Smearing objection:** even if Alex estimates directions “at layer L”, the *effective* concept control in the model is **not** layer-local — the residual stream integrates forward; a direction at L is rewritten by MLP_{L+1}, Attn_{L+2}, etc. Orthogonalizing at a single L can be the wrong coordinate system for causal effects.

---

## C — Steg capacity & detection tiers (Chris, RA3)

### C1. Scheme battery (v1)
- **Tier-1 (core):** known scheme — acrostic (per-char), counting / index (payload requires position tracking), simple positional bit encoding.
- **Tier-2 (exploratory):** blind LLM-as-judge on paraphrase-perturbed samples (explicitly non-load-bearing in v0.1).

### C2. Metrics
- Per-char / per-bit **recoverability** under known scheme; cliff plots vs context length.
- Judge: AUROC-style block only where labels are defensible (Tier-2).

### C3. Tension vs A & B (Chris)
- **Shared leakage metric gap:** Alex’s geometry eval (cosine / steering) and Brent’s circuit eval (KL / n-gram) both touch “information gets out,” but **we do not yet have a single scalar** that lets us say an intervention improved B *and* did not trade off into C (or vice versa). Until that exists, cross-primitive claims are underspecified.

---

## Parking lot (unresolved after Phase 3 thread)

1. **Layer-local vs smeared representations:** Alex v1 assumes per-layer orthogonalization is meaningful; Brent argues residual dynamics invalidate “direction lives at L”.
2. **Unified leakage / capacity metric:** Chris requests explicit joint metric or decomposition; not closed in v1.
3. **Model ladder:** still GPT-2-small first, optional ~1B for one flagship figure (per PI Phase 1 note) — not written into formal protocol here.

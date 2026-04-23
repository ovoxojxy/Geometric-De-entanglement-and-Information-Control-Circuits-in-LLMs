# Methods v2 (post–Hiccup #1 — **active design**)

**Replaces** v1 extraction claims for paper-facing text. **Hiccup #1 fix:** template/format leakage invalidated v1 cosines; v2 makes randomized contrast shells **first-class**.

Primitives: **A** geometry · **B** circuits / leakage · **C** covert capacity.

---

## A — Concept-direction extraction v2 (Alex, RA1)

### A1. Template-randomized contrastive shells
- Sample contrast **envelopes** from a finite pool: varied closings (`Answer:`, `Final:`, none), bracket styles, order of clauses, neutral filler length bins.
- **Counterbalance:** every concept pair appears under ≥3 independent surface forms; block designs so no single scaffold correlates with label.

### A2. Extraction + orthogonalize (unchanged machinery, new inputs)
- Difference-in-means directions per layer **L** on residual at fixed token window; LEACE-style projection against **nuisance bank** expanded with **format-only** probes estimated on label-shuffled prompts.

### A3. Acceptance gates (geometry)
- **Template ablation row** required in every table: cosine / KL after (i) raw shells (ii) shuffled-endings (iii) full v2 pool.
- Cosine pair matrix **not** reported until (ii) passes pre-registered threshold band (pilot-derived).

### A4. Risks (Alex)
- Pool too small → residual format coupling; monitor off-diagonal mass on held-out unseen shell families.

---

## B — Circuit ↔ direction linkage (Brent, RA2)

### B1. Linkage probe (new in v2)
- Given direction **d** at layer **L** (from v2 extraction), run **edge-local interventions** (attention head write / MLP neuron mask) that maximally move the projection of residual onto **d** while minimizing LM loss spike on control prompts.
- Report **which edges** co-move with **d** under patching — names a minimal circuit candidate set **S(d)**.

### B2. Leakage table (unchanged headline from Zoom 1)
- Primary **KL**; **Δentropy**; **repeat**; smear **L vs L+2**; tertiary recover / judge-flip from Chris.

### B3. Tension vs A (carried)
- Smearing still possible; v2 adds **obligation** to log whether **S(d)** intersects layers **L+1…L+k** when Alex claims “direction lives at L”.

---

## C — Steg battery v2 (Chris, RA3)

### C1. Counting isolated as sub-test
- Split **counting / index** schemes from acrostic tier: separate **payload length sweep** and **distance-to-supervision** axis; cliff plots per sub-test.

### C2. Judge tier (exploratory) — **Hiccup #2 caveat**
- Blind LLM-judge AUROC is **not** load-bearing when paraphrase stress-test shows collapse (see Threats to Validity in scope doc).
- Tier-1 known-scheme recoverability remains core.

### C3. Cross-primitive reporting
- Joint row schema locked with RA1/RA2; no standalone steg claims without KL column from same intervention family.

---

## Experiments (scaffold only)

Illustrative tables live in `experiments/p6_illustrative_table.md` on RA branches — **not** real runs.

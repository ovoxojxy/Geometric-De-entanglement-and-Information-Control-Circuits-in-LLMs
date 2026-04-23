# Current Context Pack — GeomDeent

**Active phase:** P6 — Zoom 2 + methods v2 + Hiccup #2 (**complete**). Next: P7 paper draft v0.1 (await PI go-ahead).

1. **Goal**  
   Same as `00_project_scope.md`.

2. **Primitives**  
   A geometry · B circuits/leakage · C covert capacity.

3. **Slack thread refs**  
   - Phase 2 parent: `1776917326.872159` (lit review / scoping).  
   - Phase 3 parent: `1776917863.943389` (methods v1 + parking lot).  
   - Phase 4 parent: `1776920017.706679` (Zoom 1).  
   - Phase 5 parent: `1776921561.477649` (pilot + Hiccup #1).  
   - **Phase 6 parent:** `1776924155.200649` (Zoom 2 + methods v2 + Hiccup #2).

4. **Phase 4 decisions (measurement spine)**  
   - Leakage table: KL primary; Δentropy + repeat; recover/judge tertiary.  
   - Smear check L vs L+2; pilot-derived thresholds.  
   - Toy model: Qwen2.5-0.5B-Instruct default; TinyLlama fallback; frozen templates.

5. **Phase 5 / Hiccup #1**  
   - v1 extraction **parked** for claims (template/format leakage).  
   - Doc #1: **Known failure modes** (2026-04-23).  
   - Local: `06_decisions/pilot_hiccup1_summary.md`.

6. **Methods v2 + Phase 6**  
   - **v2 (active):** `03_methods/methods_v2.md` on RA branches — template-randomized envelopes + template ablation gate row; Brent **linkage probe** `S(d)`; Chris **counting sub-test** + Tier-2 judge caveats.  
   - **Experiments (stub):** `experiments/p6_illustrative_table.md`.

7. **Hiccup #2**  
   LLM-judge **paraphrase collapse** in stubs → Tier-2 **non-load-bearing**; **Threats to validity** appended to Doc #1. Local: `06_decisions/hiccup2_summary.md`.

8. **Docs**  
   - Scope / reading + failure modes + threats: https://docs.google.com/document/d/1ozgzNjCtJUbjI2tr0ELjHW3pNAYMj8M0ihwd14F9Hs0/edit  
   - Zoom 1: https://docs.google.com/document/d/1tRN_QgL27Y_UcWrq_6RXN6sZlR3JMkFRhjoAysSXwds/edit  
   - Zoom 2: https://docs.google.com/document/d/1QJxXcdYCqI0FDiRJu_quv3r-pLXvePUXT_IJ94JkoAI/edit

9. **Git (export SHAs)**  
   - `RA1` `b4e90e7`, `RA2` `feb6d18`, `RA3` `89a0b95` — pull branches for tip.  
   - `main` — archive previews + this file; `git pull origin/main`.

10. **Next**  
    Phase 7 — paper draft v0.1 in Google Docs + Slack critique loop. **Do not start until PI says go.**

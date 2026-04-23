# Current Context Pack — GeomDeent

**Active phase:** P4 — Zoom 1 (**complete**). Next: P5 pilot + Hiccup #1 (await PI go-ahead).

1. **Goal**  
   Same as `00_project_scope.md`: geometry-aware directions + circuit interventions → less leakage / covert capacity without wrecking LM performance.

2. **Primitives**  
   A geometry · B circuits/leakage · C covert capacity (notation: report collateral across all three).

3. **Slack thread refs**  
   - Phase 2 parent: `1776917326.872159` (lit review / scoping).  
   - Phase 3 parent: `1776917863.943389` (methods v1 + parking lot).  
   - **Phase 4 parent:** `1776920017.706679` (Zoom 1 transcript + decisions).

4. **Phase 4 decisions (locked 2026-04-22)**  
   - **Leakage table:** **KL(clean ‖ intervened)** = primary headline column on a shared probe set; same row includes **Δentropy** and **repetition / bigram repeat**; **recover** + **LLM-judge flip** = **tertiary** diagnostics.  
   - **Layer / smear:** Alex keeps **ladder-at-L** extraction default; Brent **smear check** = semantic probe on residual at **L and L+2** after projection; **“smeared coordinate”** flags use **pilot-derived** tail thresholds (not fixed in-room).  
   - **Toy model:** **Qwen2.5-0.5B-Instruct** default; **TinyLlama-1.1B** if OOM; **freeze tokenizer + chat template** across RAs.

5. **Docs**  
   - Scope / reading (Phase 2): existing Google Doc #1 (see Phase 2 Slack).  
   - **Meeting notes Zoom 1:** https://docs.google.com/document/d/1tRN_QgL27Y_UcWrq_6RXN6sZlR3JMkFRhjoAysSXwds/edit  
   - Local mirror: `06_decisions/meeting_notes_2026-04-22_zoom1.md`.

6. **Git (post–Phase 4)**  
   - `main`: Phase 4 wrap commits include `05_slack_exports/phase_4_preview.md`, `06_decisions/meeting_notes_2026-04-22_zoom1.md`, this `cp_current.md` — pull `origin/main` for the current tip.  
   - `RA1` @ `ae984e6`, `RA2` @ `381a48d`, `RA3` @ `4b86a64`: `research-log/phase4_zoom1.md`.

7. **Next**  
   Phase 5 — pilot scaffolding + illustrative numbers + **HiccUP-1** (template-feature leakage) + append failure modes to Google Doc #1. **Do not start until PI says go.**

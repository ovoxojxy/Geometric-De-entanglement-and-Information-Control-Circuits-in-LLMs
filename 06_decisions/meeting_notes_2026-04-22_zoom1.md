# GeomDeent — Meeting notes (Zoom 1)

**Date:** 2026-04-22  
**Attendees:** Jarod (PI), Alex, Brent, Chris  
**Related Slack:** Phase 4 meeting thread in `#cognitive-foundations-for-reasoning-paper-extension`  
**Mirrors:** Google Doc #2 created for this meeting (URL in Slack).

## Agenda

1. Parking lot from methods v1: layer-local vs smeared directions  
2. Leakage metric: single headline vs small vector  
3. Toy model and layer grid for first implementation pass  

## Decisions

1. **Leakage metric (reporting):** The primary headline number is **KL(clean ‖ intervened)** on next-token distributions over a fixed probe sentence set (order 50–100 prompts, shared tokenizer). The leakage table also includes **Δentropy** on the same run and **repetition / bigram repeat rate** (circuit-facing columns). **Recover rate** and **LLM-judge flip rate** stay in the protocol as **tertiary** diagnostics; they are not the main scalar for main-text plots.

2. **Layer scope:** Alex keeps **per-layer ladder extraction at L** as the default v1 implementation. Brent adds a **smear check**: measure the same semantic linear probe on the residual stream at **L and L+2** after orthogonalization and **log cosine drift**. Runs with large drift are flagged **“smeared coordinate”** in appendix; exact numeric threshold is **set from pilot quantiles** (not fixed in this meeting).

3. **Toy model:** Default shared small model is **Qwen2.5-0.5B-Instruct**. **TinyLlama-1.1B** is the fallback if VRAM or env constraints block Qwen. All RAs **freeze tokenizer and chat template** across comparisons.

## Action items

- **Alex:** Wire KL-primary column plus Δentropy into `ra1_contrastive_stub.py` outputs; document probe set path before pilot.  
- **Brent:** Add smear-check hook (L vs L+2) and repetition metric to `ra2_circuits_stub.py` before pilot.  
- **Chris:** Align steg battery output schema with the leakage table (KL primary; recover/judge-flip tertiary).  
- **Jarod:** Confirm toy model after Alex reports a one-machine VRAM sanity check (async).  

## Open questions

- Dense vs sparse layer grid for the paper’s main figure — **deferred** to Phase 5 pilot cost curve.  
- Pre-registering a single L* for the headline figure — needs pilot data; **not closed** in Zoom 1.  

# Reading queue — Phase 2 (lit review + scoping)

**Repo:** Geometric-De-entanglement-and-Information-Control-Circuits-in-LLMs  
**Last updated:** Phase 2 kickoff (parallel RA picks + scoping debate in Slack).

How to read this file: each RA owns their bullets; cross-links to the three primitives (geometry / circuits / steg) are explicit so we do not talk past each other.

## Alex (RA1) — concept geometry & disentanglement

| Priority | Paper / artifact | Why now |
|----------|------------------|---------|
| P0 | Zou et al., *Representation Engineering* | Canonical contrastive-direction baseline; we need a crisp target to beat on cosine + steering. |
| P0 | Belrose et al., *LEACE* | Linear concept erasure / orthogonalization — closest off-the-shelf tool to “disentangle” without retraining. |
| P1 | Anthropic, *Scaling Monosemanticity* (SAE roadmap) | SAE features as alternative *axes* to raw contrastive diffs — Jarod said both are first-class; need to see failure modes. |
| P1 | Park et al., *Linear Representation Hypothesis* | Vocabulary for when “direction” claims are even well-posed. |
| P2 | Marks & Tegmark, *Geometry of Truth* | Quantitative entanglement stories — sanity-check our metrics section. |

**Open worry:** template leakage in contrastive prompts (called out in kickoff). Anything we cite on 0.98 cosines has to survive template randomization or it is not evidence.

## Brent (RA2) — circuits, induction, MLP leakage

| Priority | Paper / artifact | Why now |
|----------|------------------|---------|
| P0 | Olsson et al., *In-context Learning and Induction Heads* | Definition + scoring for induction; baseline for “what are we even ablating”. |
| P0 | Goldowsky-Dill et al., *Path patching* | Causal isolation — without this we do not get to claim *where* leakage reroutes post-ablation. |
| P1 | Wang et al., *IOI-style circuits* | Template for multi-layer attention + MLP stories (even if our task is not IOI). |
| P1 | Marks et al., *Sparse Feature Circuits* | Bridge from SAE-ish features to paths — ties to Alex’s stack without hand-waving. |
| P2 | Nanda et al., *Progress Measures* (tiny-model toolkit) | Cheap intuition when GPT-2-small is too thin for effect sizes. |

**Open worry:** post-induction ablation leakage is *diffuse* — risk we end up listing “induction + twelve friends” with no clean intervention story.

## Chris (RA3) — steg capacity, cliffs, detection

| Priority | Paper / artifact | Why now |
|----------|------------------|---------|
| P0 | Motwani et al., *Secret Collusion* | Threat model for covert coordination / encoding — frames what “capacity” even means. |
| P0 | Roger & Greenblatt, *Hiding Reasoning* | Undetectability vs recoverability tradeoffs — maps to our tiered claims. |
| P1 | ARC / Christiano-line notes on steganographic capacity | Capacity framing for the “steg cliff” (acrostic vs counting split). |
| P1 | Recent “steg cliff” empirical writeups (acrostic vs counting / position) | Primary empirical anchor for Chris’s eval battery. |
| P2 | LLM-as-judge red-team literature | Any detector story has to survive paraphrase — collect concrete failure modes. |

**Open worry:** blind LLM-judge detection collapses under paraphrase — anything we ship as “safety” has to name the adversary.

## Scoping notes (from lab thread, Phase 2)

- **Brent (initial push):** treat steg as *out of scope* for v0.1 — circuits + leakage already explode combinatorially; steg is a second paper.
- **Chris (pushback):** core question explicitly ties leakage interventions to *covert capacity* — if we drop steg we are answering a different grant line than the scope doc.
- **Jarod (ruling):** steg **stays in** for v0.1 but **tiered** — known-scheme recoverability is load-bearing; blind judge track is exploratory with heavy caveats (matches PI message in Phase 1 thread).

## Next actions

- [ ] Alex: template-randomization lit for contrastive / LEACE failure cases.
- [ ] Brent: lock model ladder (GPT-2-small plumbing → optional ~1B) into `03_methods/evaluation_design.md` once that file exists.
- [ ] Chris: draft eval tiers (known-scheme vs blind) in upcoming methods doc.
- [ ] Everyone: Google Doc **GeomDeent — Scope & Reading Queue v0.1** is canonical for prose; this file is the git-diffable mirror.

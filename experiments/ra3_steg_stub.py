"""RA3 (Chris): steg battery + judge harness — Phase 3 stub; Phase 5 schema alignment (illustrative)."""

from __future__ import annotations

from typing import Any

PILOT_NOTE = (
    "Illustrative schema only (Phase 5–6 sim). "
    "Tier-2 judge metrics are non-load-bearing (see Hiccup #2 / Threats)."
)


def known_scheme_recoverability_stub() -> None:
    raise NotImplementedError("phase 3 stub")


def blind_judge_tier_stub() -> None:
    """Exploratory tier — paraphrase robustness required before any claim."""
    raise NotImplementedError("phase 3 stub")


def leakage_vector_tertiary_stub() -> dict[str, Any]:
    """Tertiary diagnostics (recover, judge-flip) — slots aligned with Zoom-1 vector."""
    return {
        "pilot_meta": PILOT_NOTE,
        "recover_rate": 0.41,
        "llm_judge_flip_rate": 0.07,
    }


def combined_table_row_stub(layer: int = 12) -> dict[str, Any]:
    """Single dict shape if we merge RA stubs for tables (still dummy)."""
    return {
        "layer": layer,
        "primary_kl": 0.184,
        "delta_entropy": -0.041,
        "repeat_rate": 0.092,
        **leakage_vector_tertiary_stub(),
    }


def counting_subtest_stub(*, distance_to_supervision: int = 8) -> dict[str, Any]:
    """Phase 6 — isolated counting/index payload curve (illustrative)."""
    return {
        "pilot_meta": PILOT_NOTE,
        "subtest": "counting_index",
        "distance_to_supervision": distance_to_supervision,
        "recover_rate": 0.33,
    }


def judge_paraphrase_stress_stub() -> dict[str, Any]:
    """Hiccup #2 — judge AUROC collapses under paraphrased covert phrasing (illustrative)."""
    return {
        "pilot_meta": PILOT_NOTE,
        "judge_auroc_canonical_wording": 0.81,
        "judge_auroc_paraphrase_covert": 0.49,
        "hiccup2_tag": "judge_not_validity_instrument_for_tier2",
    }


if __name__ == "__main__":
    print(combined_table_row_stub())

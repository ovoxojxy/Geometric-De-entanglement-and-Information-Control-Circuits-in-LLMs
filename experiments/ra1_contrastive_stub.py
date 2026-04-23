"""RA1 (Alex): contrastive extraction + cosine matrix — Phase 3 stub; Phase 5 pilot scaffolding (illustrative only, no model)."""

from __future__ import annotations

from typing import Any

# Synthetic pilot row for lab narrative / table alignment — NOT real activations.
PILOT_NOTE = "Illustrative numbers only (Phase 5 sim). Do not cite as empirical results."


def extract_direction_stub(layer: int, concept: str) -> None:
    """Wire to activation hooks + DiM / LEACE pipeline."""
    raise NotImplementedError("phase 3 stub")


def cosine_pair_matrix_stub() -> None:
    raise NotImplementedError("phase 3 stub")


def illustrative_pilot_row(*, layer: int = 12) -> dict[str, Any]:
    """Return one JSON-serializable pilot row (dummy data).

    Hiccup #1 narrative: post-orthogonalization directions that should decouple
    still sit at ~0.97 cosine — consistent with **template / format leakage**
    across contrast pairs, not semantic disentanglement.
    """
    return {
        "pilot_meta": PILOT_NOTE,
        "toy_model": "Qwen2.5-0.5B-Instruct (planned)",
        "layer": layer,
        "pair": "sentiment_vs_country_control",
        "cosine_raw": 0.981,
        "cosine_after_orthogonalize_v1": 0.972,
        "template_surface_hypothesis": "shared Answer:/bracket scaffold across A/B contrast shells",
    }


def run_pilot_stub_print() -> None:
    """CLI hook for Slack screenshots / logs (still no forward pass)."""
    row = illustrative_pilot_row()
    print(row)


if __name__ == "__main__":
    run_pilot_stub_print()

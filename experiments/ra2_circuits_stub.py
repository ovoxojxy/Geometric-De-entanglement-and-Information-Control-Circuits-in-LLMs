"""RA2 (Brent): induction scoring, ablations, path patching — Phase 3 stub; Phase 5 pilot scaffolding (illustrative)."""

from __future__ import annotations

from typing import Any

PILOT_NOTE = "Illustrative numbers only (Phase 5 sim). Not measured on real forwards."


def induction_scores_stub() -> None:
    raise NotImplementedError("phase 3 stub")


def patch_path_stub() -> None:
    raise NotImplementedError("phase 3 stub")


def leakage_metrics_stub() -> None:
    """Token KL, n-gram overlap, entropy / repetition — to be implemented."""
    raise NotImplementedError("phase 3 stub")


def illustrative_leakage_row_stub(*, layer: int = 12) -> dict[str, Any]:
    """Dummy pilot row aligned with Zoom-1 table (KL primary, ΔH, repeat, smear)."""
    return {
        "pilot_meta": PILOT_NOTE,
        "layer": layer,
        "kl_clean_vs_intervened": 0.184,
        "delta_entropy": -0.041,
        "bigram_repeat_rate": 0.092,
        "smear_cos_L": 0.88,
        "smear_cos_L_plus_2": 0.86,
        "smear_flag_stub": False,
    }


def run_pilot_stub_print() -> None:
    print(illustrative_leakage_row_stub())


if __name__ == "__main__":
    run_pilot_stub_print()

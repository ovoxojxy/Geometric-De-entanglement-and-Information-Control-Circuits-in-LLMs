# Pilot — Hiccup #1 (template leakage)

**Date:** 2026-04-23  
**Status:** Methods v1 **extraction protocol parked** pending v2 (randomized / counterbalanced contrast shells).

## What broke

Illustrative pilot row from `experiments/ra1_contrastive_stub.py` (`illustrative_pilot_row`) shows **cosine_after_orthogonalize_v1 ≈ 0.97** for sentiment vs country-control — incompatible with a clean disentangled basis. Team consensus: **shared prompt scaffolding** across contrast pairs couples the directions (format feature, not semantics).

## Doc

Same content appended to Google Doc #1 under **Known failure modes**:
https://docs.google.com/document/d/1ozgzNjCtJUbjI2tr0ELjHW3pNAYMj8M0ihwd14F9Hs0/edit

## Downstream

Do not use v1 directions for smear plots, judge calibration, or paper-quality tables until v2 extraction lands.

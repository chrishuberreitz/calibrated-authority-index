# Contributing to the Calibrated Authority Index

Every score is an auditable, contestable claim. If an institution is mis-coded,
missing, or its policy has moved, open a pull request. A GitHub Action validates
each record against `data/schema.json` before review.

## The coding rubric
Read the institution's **public** generative-AI policy. Score each dimension
0–2, summing to the Calibrated Authority (CA) score (0–12):

**D1 — Traceability & inspectability.** `0` = absent · `1` = partial / implied · `2` = explicit.
**D2 — Human authorship & accountability.** `0` = absent · `1` = partial / implied · `2` = explicit.
**D3 — Disclosure & labeling.** `0` = absent · `1` = partial / implied · `2` = explicit.
**D4 — Synthetic-identity / fabrication prohibition.** `0` = absent · `1` = partial / implied · `2` = explicit.
**D5 — Human validation in loop.** `0` = absent · `1` = partial / implied · `2` = explicit.
**D6 — Evidential-trust emphasis.** `0` = absent · `1` = partial / implied · `2` = explicit.

Then set:
- `posture`: `Prohibitive` | `Balanced` | `Enabling`
- `c2_fit`: `fits` if the policy permits AI where verification is cheap and
  reserves humans where it is scarce; `deviates` if not.
- `c3` (trust-logic): `Evidential` | `Relational` | `Both-split` | `Neither`
- `twilight`: `true` if the policy uses precedent-collapse / feedback-delay /
  exponential-fog framing.

## The one rule: no claim without a source
Every record MUST carry `provenance.url` (the policy page) and SHOULD carry a
verbatim `quote` — the actual sentence the score rests on. A score with no
quotable line behind it will be sent back.

## Submitting
1. Add or edit `data/institutions/<id>.json` (copy an existing atom for shape).
2. The Action runs `python scripts/validate_records.py data` — make it pass.
3. In the PR, link the policy and paste the quote(s) you coded from.

Maintainer folds accepted records back into the source corpus; the next weekly
export regenerates every surface (site, CSV, HF, this repo) from it.

# The Calibrated Authority Index™

**51 knowledge institutions, coded on how they construct trust in AI.**
Version 2026-06-22 · mean Calibrated Authority 9.8/12 · CC-BY-4.0

Nature, JAMA, the BBC, Oxford, UNESCO and 46 more all wrote public rules for
generative AI. Read together, they reveal one pattern none of them named: **they
let AI do the work you can cheaply check, and reserve for a human the work you
can't.** This repo is that pattern as open data — every institution's policy
scored on six dimensions into a single 0–12 number, with the verbatim quote each
score rests on.

It is a *living* index: a weekly scan re-reads every policy and re-scores what
changed. (It has already caught one major society quietly dropping its
AI-disclosure rule.)

- **Live site:** https://calibrated-authority.chrishuberreitz.com
- **Methodology & how-to-cite:** https://calibrated-authority.chrishuberreitz.com/methodology
- **Hugging Face dataset:** https://huggingface.co/datasets/chrishuberreitz/calibrated-authority-index

## What's in `data/`
| file | what it is |
|---|---|
| `index.json` | the full dataset + dataset-level schema.org JSON-LD |
| `data.csv` | the same records as a flat table |
| `schema.json` | JSON Schema for one institution record (self-describing) |
| `institutions/<id>.json` | one citation atom per institution, each with a schema.org/Review whose rating IS the 0–12 score, anchored to the verbatim quote + source |

## The instrument (six dimensions, 0–2 each → CA score 0–12)
- **D1** — Traceability & inspectability
- **D2** — Human authorship & accountability
- **D3** — Disclosure & labeling
- **D4** — Synthetic-identity / fabrication prohibition
- **D5** — Human validation in loop
- **D6** — Evidential-trust emphasis

`posture` (Prohibitive / Balanced / Enabling), `c2_fit` (does the policy land
where the thesis predicts), `c3` (trust-logic), and `twilight` round out each
record. Full definitions live in the methodology page above.

## Use it
```python
import csv, urllib.request
rows = list(csv.DictReader(
    urllib.request.urlopen("https://calibrated-authority.chrishuberreitz.com/data.csv").read().decode().splitlines()))
print(len(rows), "institutions")
```
Or just `git clone` this repo and read `data/`.

## Cite it
Use the **"Cite this repository"** button (powered by `CITATION.cff`), or:

> Reitz, C.H. (2026). *The Calibrated Authority Index* (version 2026-06-22). https://calibrated-authority.chrishuberreitz.com

**Cite as:** Reitz, C. H. (2026). *The Calibrated Authority Index™* (v2026-06-22) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.21108694

`10.5281/zenodo.21108694` is the **concept DOI** — it always resolves to the latest version. Each GitHub release also mints a versioned DOI pinning that exact snapshot.

## Contribute / correct a score
Scores are auditable, so they're contestable. If your institution is mis-coded
or missing, open a PR — `CONTRIBUTING.md` carries the full coding rubric, and a
GitHub Action validates every submitted record against `schema.json`.

## License
Data and text: **CC-BY-4.0**. Use it, cite it.

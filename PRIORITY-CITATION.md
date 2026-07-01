# Priority, citation & trademark block — staged for launch

Purpose: convert the live webpage into a third-party-timestamped, attribution-licensed,
citable scholarly object with a defensible **first-published date**. Paste the blocks below
where indicated on launch day (week of 2026-07-06). Replace `[LAUNCH DATE]` with the exact
publication date and `[DOI]` with the Zenodo DOI once minted.

---

## 1. Canonical "Cite as / First published" block — for the README (Markdown)

```markdown
## Cite this dataset

> Reitz, C.H. (2026). *The Calibrated Authority Index™* (version 2026-06-22).
> Zenodo. https://doi.org/[DOI]
> Also available at https://calibrated-authority.chrishuberreitz.com · Licensed CC-BY-4.0.

**First published [LAUNCH DATE]** (week of 2026-07-06). Priority for the dataset, the
six-dimension Calibrated Authority instrument, and the verification-economics coding
frame is established by this date via (a) the Zenodo DOI deposit, (b) an OpenTimestamps
blockchain anchor of the corpus files, and (c) a Wayback Machine + Perma.cc capture of
the live site. The Index is original and agent-maintained; reuse under CC-BY-4.0 requires
attribution to the citation above.
```

> Before the DOI exists, ship the URL-only fallback (no `[DOI]` line):
> `Reitz, C.H. (2026). The Calibrated Authority Index™ (version 2026-06-22). https://calibrated-authority.chrishuberreitz.com`

---

## 2. Site-footer copy (compact, one line) — for index.html + methodology.html

Plain text (replace the existing `CC-BY-4.0 · v2026-06-22 · Chris Huber Reitz` span):

```
The Calibrated Authority Index™ · First published [LAUNCH DATE] · CC-BY-4.0 · DOI: [DOI] · © 2026 Chris Huber Reitz
```

HTML snippet for the `.foot` block:

```html
<span>The Calibrated Authority Index&trade; · First published [LAUNCH DATE] ·
<a href="https://creativecommons.org/licenses/by/4.0/">CC-BY-4.0</a> ·
DOI: <a href="https://doi.org/[DOI]">[DOI]</a> · © 2026 Chris Huber Reitz</span>
```

---

## 3. ™ placement guidance

Mark the **name** "The Calibrated Authority Index™" — not the generic phrase "calibrated
authority" when used descriptively. Place ™ on the **first prominent use** in each surface,
not on every occurrence:

| Surface | Where | Status |
|---|---|---|
| Site header (`index.html` `<h1>`) | first display of the title | snippet ready — [CHRIS] apply on launch deploy |
| Site footer (both pages) | the footer span above | snippet ready — [CHRIS] apply on launch deploy |
| README (GitHub + Zenodo + HF) | first mention in the title line | applied to GitHub README first mention; mirror to HF/Zenodo READMEs |
| Zenodo deposit title | `.zenodo.json` `"title"` | **applied** → "The Calibrated Authority Index™" |
| CITATION.cff `title` | leave plain (CFF titles are machine-parsed; ™ can break renderers) | intentionally plain |

**Trademark path (one paragraph).** Use ™ now — it is an unregistered common-law claim that
requires no filing and signals intent to own the name as a brand from day one. It costs
nothing and starts building common-law rights through use in commerce. **File later** only
if the Index becomes a durable brand (a product, a paid data feed, a recurring publication):
a USPTO application (~$250–$350/class, likely IC 042 for the online data service and/or IC 016
for the publication) converts ™ to ® and gives nationwide constructive priority. Do not use ®
until a registration actually issues — using ® pre-registration is itself a violation. Decision
gate: if the Index is still "a paper + a site" in 12 months, ™ is sufficient; if it has become
a named recurring product with traffic, file.
```

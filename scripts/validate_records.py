#!/usr/bin/env python3
"""Stdlib-only validator for Calibrated Authority Index records.

Usage: python scripts/validate_records.py data
Checks every data/institutions/*.json atom against the record schema's core
constraints (required fields, score ranges, ca range + ca == sum(scores)).
Exit 1 on any failure so the GitHub Action blocks a bad PR. No dependencies.
"""
import json
import sys
from pathlib import Path

DIMS = ["D1", "D2", "D3", "D4", "D5", "D6"]
REQUIRED = ["id", "name", "segment", "scores", "ca", "provenance"]


def validate_record(rec, where):
    errs = []
    for k in REQUIRED:
        if k not in rec or rec[k] in (None, ""):
            errs.append("%s: missing required field '%s'" % (where, k))
    scores = rec.get("scores") or {}
    total = 0
    have_all = True
    for d in DIMS:
        v = scores.get(d)
        if v is None:
            have_all = False
            continue
        if not isinstance(v, int) or v < 0 or v > 2:
            errs.append("%s: %s=%r out of range 0-2" % (where, d, v))
        else:
            total += v
    ca = rec.get("ca")
    if ca is not None:
        if not isinstance(ca, int) or ca < 0 or ca > 12:
            errs.append("%s: ca=%r out of range 0-12" % (where, ca))
        elif have_all and ca != total:
            errs.append("%s: ca=%d != sum(D1-D6)=%d" % (where, ca, total))
    prov = rec.get("provenance") or {}
    if not prov.get("url"):
        errs.append("%s: provenance.url is required (no claim without a source)" % where)
    return errs


def main(argv):
    root = Path(argv[1]) if len(argv) > 1 else Path("data")
    atoms = sorted((root / "institutions").glob("*.json"))
    if not atoms:
        print("no records found under %s/institutions" % root)
        return 1
    all_errs = []
    for a in atoms:
        try:
            rec = json.loads(a.read_text())
        except Exception as e:
            all_errs.append("%s: invalid JSON (%s)" % (a.name, e))
            continue
        all_errs.extend(validate_record(rec, a.name))
    if all_errs:
        print("VALIDATION FAILED (%d issue(s)):" % len(all_errs))
        for e in all_errs:
            print("  - " + e)
        return 1
    print("OK: %d records valid." % len(atoms))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

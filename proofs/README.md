# Blockchain timestamp proofs

Each subdirectory is one frozen version of the dataset: the exact bytes that were
published, and the OpenTimestamps proof anchoring those bytes to the Bitcoin
blockchain. Together with the Zenodo DOI and the Wayback capture, these establish
the first-publication date for the dataset and the six-dimension Calibrated
Authority instrument (see `../PRIORITY-CITATION.md`).

## The invariant

**A `.ots` proof always sits in the same directory as the exact bytes it attests.**

This is the whole design. Proofs used to live next to the *live* files at
`data/data.csv.ots` — which meant every corpus refresh silently invalidated them,
and `ots verify` reported `File does not match original!` to anyone who checked.
A proof that reports failure is worse than no proof: it reads as tampering rather
than as version skew. Freezing the bytes with the proof makes that impossible.

Live files at `data/` carry no proof. Look here instead.

## Verifying

Install the client (`pip install opentimestamps-client`), then:

    cd proofs/2026-06-22-n51
    ots verify data.csv.ots

A pass prints the Bitcoin block and the attested time. `File does not match
original!` means the bytes in that directory were altered after stamping — these
directories are append-only and must never be edited.

Without a local Bitcoin node the client cannot check the block header itself and
will say so; the proof is still complete, it just needs a node (or a block
explorer) to confirm the final link.

## Versions

| Version | N | Stamped | Attestation |
|---|---|---|---|
| `2026-06-22-n51` | 51 | 2026-07-01 | Bitcoin blocks 956255, 956294, 956297 |
| `2026-07-31-n59` | 59 | 2026-08-02 | pending — calendars submitted, awaiting confirmation |

A fresh stamp is *pending* for a few hours: the calendar servers hold the
commitment and fold it into a Bitcoin transaction on their next batch. Run
`ots upgrade <file>.ots` after a day to pull the confirmed block header into the
proof file, making it verifiable without contacting anyone.

**Upgrade the pending proofs.** The `2026-06-22-n51` set sat pending for a month
because nobody did — it depended on four third-party calendar servers staying
online to prove anything at all. It was upgraded on 2026-08-02 and is now
self-contained. Do not repeat that gap: upgrade, then commit the upgraded proof.

## Cutting a new version

`ca-index-timestamp.sh` (in `~/.local/bin/`) archives the current live bytes into
a new `proofs/<version>-n<N>/` and stamps them. Run it before `gh release create`,
so the release tarball Zenodo archives contains a proof that actually verifies.

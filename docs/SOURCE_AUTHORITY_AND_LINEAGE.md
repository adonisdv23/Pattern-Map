# Source authority and lineage

Status: **governing foundation record**
Verified: 2026-08-19, America/New_York

## Authority order

When sources conflict, use this order:

1. The owner's approved v16 handoff and any later explicit owner instruction.
2. `docs/OWNER_INTENT_V16.md` after its intent-freeze checkpoint.
3. Recovered v13 material for the historical idea, ambition, six families, and
   reader problem.
4. V14/v15 material for rigor, boundaries, terminology, implementation ideas,
   accessibility, prior art, and design lessons.
5. V15.2 for The Echo Problem and selectively reusable interface or research
   patterns.
6. Model or agent reviews as advisory work products only.

Historical model recommendations are not owner instructions. Detail, confidence,
or repetition does not raise a review's authority.

## Verified lineage anchors

| Source | Integrity anchor | Role in v16 | Verification |
| --- | --- | --- | --- |
| Pattern-Map repository baseline | Commit `5eea2381c86400bacc1bc2a6df0e3af78bd6330a`; `main` matched `origin/main` at preflight | Destination baseline | Clean and synchronized before branch creation |
| V14 complete transfer | Packaging commit `d0d26e28236e50d49e57bea9554e2a3a7b392198`; artifact baseline `261c516710f67998224a16c056bba0aefd5c26f4`; 430 files; 91,184 KiB on disk | Immutable historical transfer; source of v14 rigor, QA, accessibility, design, and prior-art lessons | All entries in `00_START_HERE/SHA256SUMS.txt` passed on 2026-08-19 |
| Recovered v13 diagram inside the transfer | SHA-256 `8a8204a05e993e84f2bd9037c59b7beb2ab6b4bca89304e299f66b3961f203ae` | Historical origin map and six-family continuity anchor; never current topology | Hash recorded and previously verified in the transfer manifest |
| Recovered v13 rendered DOM snapshot | SHA-256 `3c7a191ac44404828309cbfd8c58fa04eb9742bbbebe96879dd640a94e3645ec` | Supplementary rendered-state evidence; not original standalone HTML | Status remains explicit: original standalone HTML unavailable |
| V15.2 source checkout | Commit `36568cb6e8afce9544606c968319b063fc9b79ce`; branch `codex/discrimination-layer-v15-2-overnight` | Exact source checkpoint for The Echo Problem; selective pattern source only for v16 | Checkout clean; source repository has no configured remote |
| V15.2 owner archive | 41,436,496 bytes; SHA-256 `f8b71db0bda7f7564e5d3cec1f697bee38b3fcb17b56f47c79bf653f39b549b5`; 239 selected payload files; 48,717,432 uncompressed payload bytes | Immutable owner checkpoint to be preserved losslessly; accession source for Echo EP v0.1 | Hash and sidecar match; JSON manifest parses; `unzip -t` passes |
| Historical public site | <https://pattern-recognition-map.adonisdv23.chatgpt.site/> | Supplementary visual/reference check only | Mutable external surface; local archived v13 material takes precedence |

## Permanent interpretation boundaries

- V13 is the historical authority for the broad reader problem and six-family
  ambition, not proof that its mechanisms work.
- V14 and v15 may constrain overclaiming and provide implementation lessons,
  but may not redefine v16 around origin accounting.
- V15.2 remains exactly what it was: a local owner-review checkpoint and unrun
  research program. It is not retroactively renamed.
- The curated successor under `research/the-echo-problem/` begins its own
  version sequence at EP v0.1. EP v1.1 is an active design successor; it does
  not rewrite EP v0.1 or any preserved v15.2 byte.
- The Echo Problem is related to the broader Discrimination Layer as a worked
  mechanism and research track; it is not the broad framework's opening or
  definition.

## Archive mutation rule

Source packages and imported checkpoints are accessioned byte-for-byte. New
labels, explanations, and status corrections belong in adjacent lineage files
or curated successors. Never silently overwrite archive contents.

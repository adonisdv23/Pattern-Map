# Binary artifact policy

Status: **foundation policy**
Last checked: 2026-08-19

## Purpose

Pattern Map contains historical images, PDFs, and owner-review packages whose
exact bytes matter. It also needs to remain cloneable and reviewable. This
policy separates immutable accession artifacts from regenerated outputs and
prevents large opaque files from silently becoming ordinary source.

## Repository rules

1. Text and code are canonical whenever a semantic source exists. PDFs and
   standalone HTML exports are review companions unless explicitly recorded
   otherwise.
2. Historical binaries must have a recorded source, byte count, SHA-256, role,
   and status before accession.
3. A binary under `archive/` is immutable after accession. Replacement requires
   a new path and a new lineage record.
4. Do not commit dependencies, caches, temporary renders, browser profiles,
   credentials, or regenerated build products.
5. New opaque Git objects should not exceed 1,000,000 bytes without a recorded
   exception. Splitting one opaque artifact does not reduce total history or
   checkout weight and is not, by itself, a storage optimization.
6. Git LFS is not currently installed in this workstation checkout. Do not add
   LFS pointer rules until the owner deliberately adopts LFS and the complete
   clone/recovery workflow is tested.
7. GitHub Releases are not an authorized storage route during v16 development.

## Recorded v16 owner-review exceptions

- `assets/diagrams/historical-v13-pattern-recognition-diagram-v12.png` is a
  1,961,204-byte historical asset and therefore exceeds the ordinary 1 MB
  guidance. It is accepted because the exact recovered bytes are the lineage
  evidence being displayed, its SHA-256 is locked as
  `8a8204a05e993e84f2bd9037c59b7beb2ab6b4bca89304e299f66b3961f203ae`,
  and the active copy lets the standalone local review route work without
  mutating the immutable transfer. It is labeled historical, not current.
- Committed browser screenshots and six PDF page renders under `qa/visual/`
  are bounded review evidence. Each individual file is below 1 MB. They are
  not runtime dependencies, generated-image candidates, or research results.
- `site/exports/pattern-map-v16-owner-review.pdf` is a review companion whose
  Markdown/source artifacts remain canonical. Its current file is below 1 MB.

These exceptions do not authorize larger future binaries, deployment
artifacts, dependency directories, or an exact-ZIP import.

GitHub's current documentation warns for regular-Git files above 50 MiB,
blocks files above 100 MiB, recommends a 1 MB maximum object, and recommends
Git LFS for binary files. References:

- <https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github>
- <https://docs.github.com/en/repositories/creating-and-managing-repositories/repository-limits>

## V15.2 owner archive disposition

The exact source archive is:

- Name: `PATTERN_MAP_V15_2_OWNER_HANDOFF.zip`
- Bytes: `41,436,496`
- SHA-256: `f8b71db0bda7f7564e5d3cec1f697bee38b3fcb17b56f47c79bf653f39b549b5`
- Source commit: `36568cb6e8afce9544606c968319b063fc9b79ce`
- Integrity checks completed: source hash match, sidecar match, JSON manifest
  parse, and compressed-data test.

### Four-option comparison

| Option | Self-contained repository | Git hygiene | Recoverability | External dependency or cost | Disposition |
| --- | --- | --- | --- | --- | --- |
| One exact 39.5 MiB Git blob | Exact ZIP is in every clone | Poor: one opaque object adds the full compressed payload and cannot deduplicate against v14 | Excellent | None | Rejected for ordinary Git |
| Git LFS | Exact ZIP can be fetched through LFS | Good for the Git object database | Good only while LFS objects and bandwidth remain available | Git LFS is not installed; actual account usage/budget could not be read without a broader GitHub authorization scope; LFS is metered after included quota | Deferred pending explicit owner adoption and budget safeguards |
| Canonical extracted payload plus manifest and local exact ZIP | Every selected payload file and its provenance are in Git; exact distribution bytes remain at the verified local source | Best current balance: text remains diffable and exact duplicate blobs deduplicate against v14 | Strong for project contents; exact ZIP remains separately hash-anchored until an authorized binary channel exists | No new service, quota, or tooling dependency | **Accepted** |
| Deterministic chunks | Exact ZIP is reconstructable from every clone | Poor-to-moderate: avoids one large object but preserves the full 41.4 MiB opaque payload and adds part/reassembly burden | Excellent with automated verification | None | Rejected because it does not improve total storage |

The extracted package contains 239 files and 48,717,432 payload bytes. Comparing
its manifest hashes with the already-preserved v14 transfer shows that 102 files
and 30,298,057 bytes (62.19% of the payload) already exist byte-for-byte. Git can
reuse those blobs. Only 137 files and 18,419,375 raw bytes are new or changed
before normal Git compression and delta reuse. The exact ZIP, by contrast, is an
opaque 41,436,496-byte object with no content-level deduplication.

### Accepted accession procedure

1. Keep the original ZIP untouched at
   `/Users/gpt/Documents/Codex/worktrees/discrimination-layer-v15-2-overnight/output/PATTERN_MAP_V15_2_OWNER_HANDOFF.zip`.
2. Copy the original `.zip.sha256` and package manifest unchanged into
   `archive/transfers/v15.2-owner-handoff/`.
3. Extract the verified ZIP directly into an immutable payload directory. Do
   not substitute a hand-selected working-tree copy for the package payload.
4. Recompute every extracted file's byte count and SHA-256 against the original
   package manifest. Fail accession on a missing, extra, or mismatched file.
5. Add an accession record containing the source path, source commit, exact ZIP
   byte count and SHA-256, verification date, extraction root, and the explicit
   statement that the exact ZIP container is not yet stored in Git.
6. Add documentation and a local verifier showing how the package directory can
   be reconstructed from the accession. A newly created ZIP is a semantic
   repackage and must not be claimed byte-identical to the original distribution
   ZIP unless its SHA-256 actually matches.
7. Keep the exact ZIP at the verified source location until the owner explicitly
   authorizes Git LFS or a GitHub Release and any cost/budget controls are known.

This preserves every selected payload byte and its provenance in canonical Git,
without pretending that extracted files reproduce ZIP container metadata. The
original container's exact bytes remain separately preserved and hash-anchored.

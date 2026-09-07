# V15.2 owner handoff accession record

This record is accession metadata for the immutable extracted transfer. It is
not part of the 239-file manifest-listed payload.

## Source anchor

- Source checkout: `/Users/gpt/Documents/Codex/worktrees/discrimination-layer-v15-2-overnight`
- Source branch: `codex/discrimination-layer-v15-2-overnight`
- Source commit: `36568cb6e8afce9544606c968319b063fc9b79ce`
- Source ZIP: `output/PATTERN_MAP_V15_2_OWNER_HANDOFF.zip`
- Source ZIP bytes: `41,436,496`
- Source ZIP SHA-256: `f8b71db0bda7f7564e5d3cec1f697bee38b3fcb17b56f47c79bf653f39b549b5`
- Source ZIP sidecar SHA-256: `2eef19557580340df49cf95ad7d5ebe23c3bc2f350c29d7d992ad3bedc6b6870`
- Source manifest: `output/PATTERN_MAP_V15_2_OWNER_HANDOFF-manifest.json`
- Source manifest bytes: `69,680`
- Source manifest SHA-256: `05aedafc2f5cb3f589cfdc69d1eff5c854c3bef97071324f9845d63a7a1028eb`
- Accession date: `2026-08-19`, America/New_York

## Extracted payload

The canonical extracted source is rooted at this directory. Every file below
the six manifest payload directories is copied directly from the verified ZIP
member named by the external manifest's `archive_path`; no working-tree copy
was substituted.

- Payload file count: `239`
- Payload total bytes: `48,717,432`
- Extraction root: `archive/transfers/v15.2-owner-handoff/`
- Payload directories: `00_START_HERE/` through `06_REPRODUCTION/`
- Original sidecar: `PATTERN_MAP_V15_2_OWNER_HANDOFF.zip.sha256` (copied byte-for-byte)
- Original external manifest: `PATTERN_MAP_V15_2_OWNER_HANDOFF-manifest.json` (copied byte-for-byte)

The ZIP contains one additional embedded `00_START_HERE/PACKAGE_MANIFEST.json`
member generated as package metadata. It is not in the external manifest's
239-file payload list. The external manifest and sidecar are preserved at the
accession root instead; the embedded metadata is checked against the copied
external manifest by the accession verifier.

## Status boundary

The exact ZIP container is **not stored in Git**. It remains untouched at the
verified local source path above until a later explicit owner instruction
authorizes an exact storage route. The extracted payload preserves content
bytes and per-file provenance; it does not reproduce ZIP container metadata and
must not be described as a byte-identical re-zip.

The source package remains a local owner-review checkpoint with no empirical
results, no model/provider study calls, and no participant study. This
accession is preservation and verification work only.

## Verification entrypoint

Run the complete local check, including the external source ZIP, with:

```sh
python3 archive/transfers/v15.2-owner-handoff/verify_accession.py \
  --source-zip /Users/gpt/Documents/Codex/worktrees/discrimination-layer-v15-2-overnight/output/PATTERN_MAP_V15_2_OWNER_HANDOFF.zip
```

The verifier checks missing and extra payload files, per-file byte counts and
SHA-256 values, manifest totals and hash, sidecar identity, source ZIP bytes
and hash, ZIP member set and CRC, and the embedded package manifest.

# Reconstructing the v15.2 extracted package

The accession root itself is the canonical extracted package directory. Its
six payload directories retain the external manifest's `archive_path` values,
so a consumer can copy the payload tree without interpreting the historical
source checkout layout.

## Verify the accession first

From the repository root, the complete check is:

```sh
python3 archive/transfers/v15.2-owner-handoff/verify_accession.py \
  --source-zip /Users/gpt/Documents/Codex/worktrees/discrimination-layer-v15-2-overnight/output/PATTERN_MAP_V15_2_OWNER_HANDOFF.zip
```

For a clone where the original ZIP is unavailable, omit `--source-zip` to
verify the manifest-listed extracted payload, copied sidecar, and copied
manifest. The full check is stronger because the ZIP is intentionally kept
outside Git.

## Copy the extracted package

To make a working copy without changing the accession, copy only the six
payload directories and preserve the two root metadata files separately:

```sh
mkdir -p /private/tmp/pattern-map-v15.2-reconstructed
cp -R archive/transfers/v15.2-owner-handoff/00_START_HERE \
  archive/transfers/v15.2-owner-handoff/01_FINAL_OUTPUT \
  archive/transfers/v15.2-owner-handoff/02_CANONICAL_FRAMEWORK \
  archive/transfers/v15.2-owner-handoff/03_RESEARCH_PROGRAM_UNRUN \
  archive/transfers/v15.2-owner-handoff/04_REASONING_AND_QA \
  archive/transfers/v15.2-owner-handoff/05_HISTORY_AND_VISUALS \
  archive/transfers/v15.2-owner-handoff/06_REPRODUCTION \
  /private/tmp/pattern-map-v15.2-reconstructed/
cp archive/transfers/v15.2-owner-handoff/PATTERN_MAP_V15_2_OWNER_HANDOFF.zip.sha256 \
  archive/transfers/v15.2-owner-handoff/PATTERN_MAP_V15_2_OWNER_HANDOFF-manifest.json \
  /private/tmp/pattern-map-v15.2-reconstructed/
```

Run the verifier against the working copy with `--root` before using it. Do
not call the result a byte-identical ZIP reconstruction: the source container
has its own member ordering, compression records, timestamps, and metadata.
Only the extracted payload bytes and their manifest identities are preserved
here.

## Exact ZIP boundary

The original ZIP remains at the source path recorded in
`ACCESSION_RECORD.md`. It is not copied into Git, split, re-zipped, or modified.
The ZIP has 240 members: the 239 external-manifest payload members plus the
embedded `00_START_HERE/PACKAGE_MANIFEST.json` metadata member. The verifier
checks all 240 source members while the canonical extracted payload remains
exactly the 239 manifest-listed files.

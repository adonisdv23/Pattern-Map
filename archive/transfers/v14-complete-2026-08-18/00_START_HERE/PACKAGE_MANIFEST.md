# Package manifest

Package: `Discrimination-Layer-V14-Complete-Transfer-2026-08-18`

Created: 2026-08-18, America/New_York

Packaging source commit:
`d0d26e28236e50d49e57bea9554e2a3a7b392198`

Completed artifact-content baseline:
`261c516710f67998224a16c056bba0aefd5c26f4`

Branch: `codex/discrimination-layer-thought-piece-v14`

## Read order

1. `COMPLETE_TRANSFER_GUIDE.md`
2. `../01_FINAL_OUTPUTS/THOUGHT_PIECE_V14.pdf`
3. `../01_FINAL_OUTPUTS/THOUGHT_PIECE_V14.md`
4. `../01_FINAL_OUTPUTS/FINAL_MAX_THOUGHT_PIECE_AND_SITE_REPORT.md`
5. `../01_FINAL_OUTPUTS/RESEARCH_EXPANSION_AND_INTEGRATION_REPORT.md`
6. The research protocols under `../03_RESEARCH_PACKAGE/`
7. Supporting reviews and QA only as needed.

## Folder roles

| Folder | Role |
| --- | --- |
| `00_START_HERE` | GPT-oriented transfer guide, this manifest, and checksums. |
| `01_FINAL_OUTPUTS` | Small curated set of final owner-review outputs. This is the primary final-output folder. |
| `02_INTERACTIVE_SITE` | Complete source for the local visual reader, excluding regenerated dependencies and build caches. |
| `03_RESEARCH_PACKAGE` | Canonical research design plus all twelve advisory research-loop memos. |
| `04_VISUAL_ASSETS` | Image candidates, previews, selection ledger, and archived rejected hero. |
| `05_HISTORICAL_V13` | Exact historical diagram, rendered-DOM reference snapshot, and provenance records. |
| `06_REVIEWS_AND_DECISIONS` | External-review receipts, independent dispositions, owner logs, and the user-supplied checkpoint text. |
| `07_QA_EVIDENCE` | Site/PDF QA reports, responsive screenshots, PDF page renders, and publication-readiness gates. |
| `08_CASE_STUDIES` | Bounded Alpha Solver and Signal Foundry illustrations. |
| `09_TOOLS_AND_REPRODUCTION` | PDF generator, source-version records, package metadata, and install/run information. |
| `10_FULL_REPOSITORY_SNAPSHOT` | Complete tracked repository tree at the packaging source commit. |

## Intentional exclusions

- `.git/` object database and local Git configuration.
- `node_modules/`, `.next/`, `dist/`, `.wrangler/`, and other regenerated
  dependency/build/runtime caches.
- `.DS_Store` metadata.
- Credentials, cookies, tokens, environment secrets, authentication databases,
  password-manager material, and private keys.
- Any deployment or publication artifact, because nothing was deployed or
  published.

The exact tracked source state is recoverable from the repository commit
recorded above. Dependency versions are preserved by `package-lock.json`.

## Integrity anchors

- Final PDF SHA-256:
  `c96b5f062fec5dd9a09b7a592dc88c915839a872bb172f1a621bdbb53d0612f7`
- Exact v13 diagram SHA-256:
  `8a8204a05e993e84f2bd9037c59b7beb2ab6b4bca89304e299f66b3961f203ae`
- Final social card SHA-256:
  `26d87ad92d12edabebb829daabf7ca60681ac720ff15705c86bb677a99bf3b24`
- Selected E2 worked-example image SHA-256:
  `88222893a08a52bbca3f1d855aaa575827c829b09766d743a5db931930a3e325`

`SHA256SUMS.txt` contains a checksum for every packaged file other than itself.

## Status

The package is ready for owner review and transfer to another GPT. It is not a
publication, empirical result, validated framework, or authorization to deploy,
recruit, contact participants, or run live/paid providers.

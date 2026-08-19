# Migration inventory

Status values: `VERIFIED`, `MOVED_IMMUTABLY`, `PENDING_ACCESSION`,
`PENDING_CURATED_COPY`, `REFERENCE_ONLY`, `NOT_STARTED`, `NOT_AUTHORIZED`.

| Source | Destination | Source anchor | Role | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| Root `Discrimination-Layer-V14-Complete-Transfer-2026-08-18/` | `archive/transfers/v14-complete-2026-08-18/` | Package commit `d0d26e2`; artifact baseline `261c516`; complete checksum ledger | Immutable transfer | `MOVED_IMMUTABLY` | Moved with `git mv`; no content rewritten |
| V14 transfer checksum ledger | Same relative path under moved transfer | 430 packaged files | Transfer integrity | `VERIFIED` | Every recorded SHA-256 passed on 2026-08-19 |
| V13 diagram in v14/v15 sources | `archive/v13/` curated accession | SHA-256 `8a8204a0…f203ae` | Historical map | `PENDING_CURATED_COPY` | Preserve exact bytes and provenance; do not redraw or treat as current topology |
| V13 rendered DOM snapshot | `archive/v13/` curated accession | SHA-256 `3c7a191a…e3645ec` | Historical rendered-state evidence | `PENDING_CURATED_COPY` | Must remain labeled as a DOM snapshot, not original standalone source |
| V14 canonical outputs | `archive/v14/` curated checkpoint | Artifact baseline `261c516` | Version checkpoint | `PENDING_CURATED_COPY` | Transfer remains complete source until curated copy is verified |
| V15 materials inside v15.2 history | `archive/v15/` curated checkpoint | Preserved within v15.2 package | Version checkpoint | `PENDING_CURATED_COPY` | No retrospective edits |
| V15.1 materials inside v15.2 history | `archive/v15.1/` curated checkpoint | Baseline `22f232701184812489843731b6fe27592118eb29` | Version checkpoint | `PENDING_CURATED_COPY` | No retrospective edits |
| V15.2 package payload, sidecar, manifest, and exact-ZIP accession record | `archive/transfers/v15.2-owner-handoff/` | Commit `36568cb`; ZIP SHA-256 `f8b71db0…549b5`; 239 manifest-listed files | Immutable owner checkpoint payload | `PENDING_ACCESSION` | Extract directly from verified ZIP and verify every file; exact ZIP stays at source pending authorized LFS/Release; owned by Echo task |
| Curated v15.2 version checkpoint | `archive/v15.2/` | Exact owner package | Version checkpoint | `PENDING_CURATED_COPY` | Must preserve v15.2 name and no-results status |
| V15.2 origin-accounting work | `research/the-echo-problem/` | Exact owner package, selectively curated | Separate successor EP v0.1 | `NOT_STARTED` | Preserve protocol, harness, fixtures, prior art, and unfavorable-result classes; run nothing |
| Recovered v13 broad thesis and six families | v16 docs, manuscript, and framework | V13 recovery memo plus exact archive | Primary historical intent | `REFERENCE_ONLY` | Adapt with explicit provenance; do not copy unsupported claims as facts |
| V14/v15 design and accessibility lessons | v16 site and QA | Archived packages | Selective implementation guidance | `REFERENCE_ONLY` | Site work starts only after content-interface freeze |
| Existing public site | None | Mutable live URL | Supplementary visual reference | `REFERENCE_ONLY` | No deployment, replacement, or publication authorized |
| Empirical study, provider run, participants, or datasets | None | N/A | Future research only | `NOT_AUTHORIZED` | Do not execute or imply results |

## Migration invariants

- Nothing historical is deleted to make the active root cleaner.
- A curated copy does not replace its transfer source until hashes and lineage
  are recorded.
- Active v16 files cite their historical or research inputs where material.
- Archives are evidence of what existed; canonical active files state what the
  project currently believes or proposes.

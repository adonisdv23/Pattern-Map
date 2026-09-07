# Migration inventory

Status values: `VERIFIED`, `MOVED_IMMUTABLY`, `ACCESSED_IMMUTABLY`,
`CURATED_INDEX`, `PENDING_ACCESSION`, `PENDING_CURATED_COPY`, `REFERENCE_ONLY`,
`NOT_STARTED`, `NOT_AUTHORIZED`.

| Source | Destination | Source anchor | Role | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| Root `Discrimination-Layer-V14-Complete-Transfer-2026-08-18/` | `archive/transfers/v14-complete-2026-08-18/` | Package commit `d0d26e2`; artifact baseline `261c516`; complete checksum ledger | Immutable transfer | `MOVED_IMMUTABLY` | Moved with `git mv`; no content rewritten |
| V14 transfer checksum ledger | Same relative path under moved transfer | 430 packaged files | Transfer integrity | `VERIFIED` | Every recorded SHA-256 passed on 2026-08-19 |
| V13 diagram in v14/v15 sources | `archive/v13/` curated index | SHA-256 `8a8204a0…f203ae` | Historical map | `CURATED_INDEX` | Index points to verified transfer bytes; do not redraw or treat as current topology |
| V13 rendered DOM snapshot | `archive/v13/` curated index | SHA-256 `3c7a191a…e3645ec` | Historical rendered-state evidence | `CURATED_INDEX` | Indexed source remains labeled as a DOM snapshot, not original standalone source |
| V14 canonical outputs | `archive/v14/` curated index | Artifact baseline `261c516`; complete transfer checksum ledger | Version checkpoint | `CURATED_INDEX` | Principal anchors indexed; complete transfer remains the single byte authority |
| V15 materials inside v15.2 history | `archive/v15/` curated index | Source commit `82f87b1`; preserved within v15.2 package | Version checkpoint | `CURATED_INDEX` | Present accession surfaces indexed without retrospective edits or duplicate checkout bytes |
| V15.1 materials inside v15.2 history | `archive/v15.1/` curated index | Baseline `22f232701184812489843731b6fe27592118eb29` | Version checkpoint | `CURATED_INDEX` | Present accession surfaces indexed without retrospective edits or duplicate checkout bytes |
| V15.2 package payload, sidecar, manifest, and exact-ZIP accession record | `archive/transfers/v15.2-owner-handoff/` | Commit `36568cb`; ZIP SHA-256 `f8b71db0…549b5`; 239 manifest-listed files and 48,717,432 bytes | Immutable owner checkpoint payload | `ACCESSED_IMMUTABLY` | Extracted directly from verified ZIP; per-file verifier and complete source-container check pass; exact ZIP stays untouched at source pending authorized LFS/Release |
| Curated v15.2 version checkpoint | `archive/v15.2/` curated index | Exact owner package accession; source commit `36568cb` | Version checkpoint | `CURATED_INDEX` | Index preserves v15.2 name/no-results status and points to the complete accession; exact ZIP policy remains D-004 |
| V15.2 origin-accounting work | `research/the-echo-problem/` | Exact owner package, 82 byte-verified curated source files | Separate successor EP v0.1 | `VERIFIED` | EP v0.1 identity, status, preserved manuscript/site/protocol/harness/fixtures/prior art, no-results boundary, and low/no-cost future plan established; no study run |
| Owner-supplied Claude session package | `research/the-echo-problem/v1_1/`, `qa/research/ECHO_V1_1_DESIGN_CHECKPOINT_QA_2026-08-23.md` | ZIP SHA-256 `b544b734…a253`; selected source-file and frozen-render hashes recorded in the QA/design fixture | Advisory input to EP v1.1 only | `REFERENCE_ONLY` | Package instructions are not authority; claims were independently reproduced or narrowed where checkable; package code was not imported wholesale; no model/corpus/study run |
| Recovered v13 broad thesis and six families | v16 docs, manuscript, and framework | V13 recovery memo plus exact archive | Primary historical intent | `REFERENCE_ONLY` | Adapt with explicit provenance; do not copy unsupported claims as facts |
| V14/v15 design and accessibility lessons | v16 site and QA | Archived packages | Selective implementation guidance | `REFERENCE_ONLY` | Site work starts only after content-interface freeze |
| Existing public site | None | Mutable live URL | Supplementary visual reference | `REFERENCE_ONLY` | No deployment, replacement, or publication authorized |
| Empirical study, provider run, participants, or datasets | None | N/A | Future research only | `NOT_AUTHORIZED` | Do not execute or imply results |

## Migration invariants

- Nothing historical is deleted to make the active root cleaner.
- A curated copy does not replace its transfer source until hashes and lineage
  are recorded.
- A curated index may point to already accessioned immutable bytes instead of
  duplicating them; the machine-readable index must verify every selected
  anchor and identify the complete transfer authority.
- Active v16 files cite their historical or research inputs where material.
- Archives are evidence of what existed; canonical active files state what the
  project currently believes or proposes.

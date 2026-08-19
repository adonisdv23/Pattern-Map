# Preserved v15.2 source index

All files in `preserved/v15.2/` are byte-for-byte copies made from the
accessioned payload, not hand-selected rewrites. The external manifest at
`archive/transfers/v15.2-owner-handoff/PATTERN_MAP_V15_2_OWNER_HANDOFF-manifest.json`
is the per-file authority for source path, byte count, and SHA-256. The
preserved-source QA script compares each curated copy with its accessioned
source and reports the aggregate count and bytes.

## Curated source set

| Role | Curated path | Accession source path | Preservation boundary |
| --- | --- | --- | --- |
| Manuscript | `preserved/v15.2/manuscript/THOUGHT_PIECE_V15_2.md` | `01_FINAL_OUTPUT/canonical-manuscript/THOUGHT_PIECE_V15_2.md` | Historical v15.2 manuscript; not the EP v0.1 thesis and not edited here. |
| Editable site | `preserved/v15.2/site-source/` | `01_FINAL_OUTPUT/site-source/` | Complete curated site source, including its source tests and locked package metadata; no dependencies or build cache. |
| Standalone site | `preserved/v15.2/site-standalone/` | `01_FINAL_OUTPUT/standalone-site/` | Historical standalone review surface; not a publication or deployment. |
| Protocols | `preserved/v15.2/protocol/` | `03_RESEARCH_PROGRAM_UNRUN/research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V0.md`; `.../ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md`; `.../overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md` | V1 is the canonical v15.2 protocol; V0 is retained history; V1.1 is explicitly a draft amendment, not canonical. |
| Offline harness | `preserved/v15.2/harness/origin_accounting/` | `03_RESEARCH_PROGRAM_UNRUN/offline-implementation/origin_accounting/` | Deterministic implementation source only; no live provider adapter or model call. |
| Harness test | `preserved/v15.2/harness/tests/test_origin_accounting.py` | `03_RESEARCH_PROGRAM_UNRUN/tests/test_origin_accounting.py` | Offline test source; a passing test is not an empirical result. |
| Fixture contract | `preserved/v15.2/fixtures/` | `03_RESEARCH_PROGRAM_UNRUN/research/origin_accounting/fixtures/`, `.../config/`, and `.../schema/` | README, frozen configuration, and schemas are preserved. No empirical fixture dataset is claimed. |
| Prior art and evidence | `preserved/v15.2/prior-art/` | Selected files under `03_RESEARCH_PROGRAM_UNRUN/research/` and its prior-art overnight records | Prior-art maps, references, claim/evidence registers, counterargument register, readiness path, and literature audit records remain advisory/source material. |

## Exactness and exclusions

The curated set does not alter historical names, status language, no-results
state, or unfavorable-result classes. The package ZIP itself, dependencies,
caches, credentials, and build products are not copied into the successor. The
complete 239-file payload remains available in the immutable accession for
anything not included in this focused curated view.

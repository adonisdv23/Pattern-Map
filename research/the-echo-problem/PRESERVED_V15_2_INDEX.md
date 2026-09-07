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
| Offline harness | `preserved/v15.2/tools/origin_accounting/` | `03_RESEARCH_PROGRAM_UNRUN/offline-implementation/origin_accounting/` | Deterministic implementation source only; restored to its historical repository-relative `tools/` location so its unedited imports remain runnable. No live provider adapter or model call. |
| Harness test | `preserved/v15.2/tests/test_origin_accounting.py` | `03_RESEARCH_PROGRAM_UNRUN/tests/test_origin_accounting.py` | Offline test source at its historical repository-relative location; a passing test is not an empirical result. |
| Fixture contract | `preserved/v15.2/research/origin_accounting/` | `03_RESEARCH_PROGRAM_UNRUN/research/origin_accounting/fixtures/`, `.../config/`, and `.../schema/` | README, frozen configuration, and schemas retain the layout expected by the byte-preserved harness. No empirical fixture dataset is claimed. |
| Prior art and evidence | `preserved/v15.2/prior-art/` | Selected files under `03_RESEARCH_PROGRAM_UNRUN/research/` and its prior-art overnight records | Prior-art maps, references, claim/evidence registers, counterargument register, readiness path, and literature audit records remain advisory/source material. |

## Exactness and exclusions

The curated set does not alter historical names, status language, no-results
state, or unfavorable-result classes. The package ZIP itself, dependencies,
caches, credentials, and build products are not copied into the successor. The
complete 239-file payload remains available in the immutable accession for
anything not included in this focused curated view.

The harness, test, configuration, and schema files use their historical
repository-relative paths because the preserved test imports
`tools.origin_accounting` and the preserved configuration loader resolves
`research/origin_accounting/config/frozen_config.json`. Their bytes remain
unchanged; only the curated successor's placement supplies the original import
contract.

## Historical link context

This is a focused 82-file view of a 239-file accession, so a small number of
relative Markdown links inside the byte-preserved files do not resolve from the
curated placement. Those links described the layout of the historical source
repository. They are intentionally not rewritten: changing even a path would
make the curated copy cease to be byte-for-byte historical evidence.

Use the current local routes below when following those historical references:

| Historical reference | Current local route |
| --- | --- |
| `ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V0.md` | [Curated v0 protocol](preserved/v15.2/protocol/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V0.md) |
| `overnight/rounds/08_LOOP2_OPERATIONALIZATION_SPEC.md` | [Complete-accession operationalization specification](../../archive/transfers/v15.2-owner-handoff/03_RESEARCH_PROGRAM_UNRUN/research/overnight/rounds/08_LOOP2_OPERATIONALIZATION_SPEC.md) |
| `PAPER_PROSPECTUS_V0.md` | [Complete-accession paper prospectus](../../archive/transfers/v15.2-owner-handoff/03_RESEARCH_PROGRAM_UNRUN/research/PAPER_PROSPECTUS_V0.md) |
| `PRIOR_ART_AND_ADJACENT_FIELDS_MAP.md` | [Curated prior-art map](preserved/v15.2/prior-art/PRIOR_ART_AND_ADJACENT_FIELDS_MAP.md) |
| `source/THOUGHT_PIECE_V14.md` | [Complete-accession v14 thought piece](../../archive/transfers/v15.2-owner-handoff/05_HISTORY_AND_VISUALS/prior-version-surfaces/THOUGHT_PIECE_V14.md) |

Repository-wide active-document link checks must therefore treat
`preserved/v15.2/**` as immutable historical content and test this index's
current routes instead. This is a documented subset boundary, not a claim that
the historical relative links resolve in their new placement. The complete
accession remains the recovery authority.

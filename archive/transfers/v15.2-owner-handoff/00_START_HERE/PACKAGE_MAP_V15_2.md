# Pattern Map v15.2 owner handoff - package map

This file is the navigation and authority contract for
`PATTERN_MAP_V15_2_OWNER_HANDOFF.zip`. The archive is organized so a human
owner or another GPT can identify the final output, the unrun research program,
the reasoning behind the changes, and the historical artifacts without relying
on chat history.

## Start here

1. Open `00_START_HERE/OWNER_REVIEW_PACKET_V15_2.md`.
2. Read `00_START_HERE/REASONING_AND_LOGIC_V15_2.md` for the end-to-end logic.
3. Read `00_START_HERE/PACKAGE_MAP_V15_2.md` (this file).
4. Open `01_FINAL_OUTPUT/standalone-site/index.html` for the current reader.
5. Use the `explore.html`, `lab.html`, and `sources.html` links inside the
   standalone reader or open those files directly.

## Which folder is the final output?

**`01_FINAL_OUTPUT/` is the final v15.2 output folder.**

- `standalone-site/` contains four self-contained HTML pages. They inline their
  CSS and local images and do not require Node, a development server, or an
  internet connection for core rendering.
- `site-source/` contains the canonical editable Vinext/React site source.
- `canonical-manuscript/THOUGHT_PIECE_V15_2.md` contains the current long-form
  text.
- `pdf-review/PATTERN_MAP_V15_2_REVIEW_COMPANION.pdf` is the current 20-page
  visual/print companion.

The semantic HTML and Markdown are canonical. The PDF is untagged and exists
for fast visual review; it is not the most accessible or editable source.

## Folder structure

```text
Pattern-Map-v15.2/
|-- 00_START_HERE/
|   |-- README.md
|   |-- OWNER_REVIEW_PACKET_V15_2.md
|   |-- REASONING_AND_LOGIC_V15_2.md
|   |-- VERSION_HISTORY_V15_2.md
|   |-- PACKAGE_MAP_V15_2.md
|   |-- PACKAGE_MANIFEST.json
|   `-- SOURCE_VERSIONS_USED.json
|-- 01_FINAL_OUTPUT/
|   |-- standalone-site/
|   |   |-- index.html
|   |   |-- explore.html
|   |   |-- lab.html
|   |   |-- sources.html
|   |   `-- STANDALONE_ROUTES.json
|   |-- site-source/
|   |-- canonical-manuscript/
|   `-- pdf-review/
|-- 02_CANONICAL_FRAMEWORK/
|   |-- source/
|   `-- case-studies/
|-- 03_RESEARCH_PROGRAM_UNRUN/
|   |-- research/
|   |-- offline-implementation/
|   |-- experiments/
|   `-- tests/
|-- 04_REASONING_AND_QA/
|   |-- overnight-v15.2/
|   |-- model-review-records/
|   |-- current-and-sealed/
|   `-- handoff-records/
|-- 05_HISTORY_AND_VISUALS/
|   |-- v13-anchor/
|   |-- image-candidates/
|   |-- prior-version-surfaces/
|   |-- prior-standalone-html/
|   `-- prior-review-pdfs/
`-- 06_REPRODUCTION/
    `-- tools/
```

## Epistemic status by folder

| Folder | What it contains | What it does not establish |
| --- | --- | --- |
| `00_START_HERE` | Owner guidance, authority boundaries, and manifest | A research finding or permission to act externally |
| `01_FINAL_OUTPUT` | Current reader, manuscript, editable site, and review PDF | Publication, deployment, or completed reader study |
| `02_CANONICAL_FRAMEWORK` | Current concepts, v15.2 reader contract, map records, glossary, and bounded cases | A proven minimum architecture or universal system topology |
| `03_RESEARCH_PROGRAM_UNRUN` | Canonical v1.0 protocol, v1.1 amendment draft, fictional data generator, validators, metrics, tests, and planning simulations | A model result, participant result, preregistration, pilot, or primary run |
| `04_REASONING_AND_QA` | Research/editorial/design lanes, compact model-review text records, red teams, decision ledger, and validation receipts | Independent empirical validation |
| `05_HISTORY_AND_VISUALS` | Recovered v13 anchor, all generated candidates, complete use table, prior surfaces, and self-contained v14-v15.2 manuscript HTML | Evidence that the framework works or a pixel reconstruction of every historical site |
| `06_REPRODUCTION` | Local builders, renderers, checkers, and package scripts | Authorization to call providers, deploy, publish, or mutate GitHub |

## Authority order for another GPT

When files appear to conflict, use this order:

1. `00_START_HERE/OWNER_REVIEW_PACKET_V15_2.md` for current status and owner
   review intent.
2. `01_FINAL_OUTPUT/canonical-manuscript/THOUGHT_PIECE_V15_2.md` and
   `01_FINAL_OUTPUT/site-source/` for current editorial content.
3. `02_CANONICAL_FRAMEWORK/source/READER_OUTCOME_AND_READING_PATH_V15_2.md`
   for current timing/comprehension requirements, then the other stable
   component and terminology records in that folder.
4. `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md` for the current canonical
   study protocol.
5. `research/overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md`
   only as a proposed amendment until the owner explicitly accepts it.
6. `04_REASONING_AND_QA/overnight-v15.2/INTEGRATION_DECISION_LEDGER.md` for why
   v15.2 decisions were accepted, revised, deferred, or rejected.
7. Historical v13-v15.1 artifacts only for comparison and provenance; they do
   not override v15.2.

## Historical standalone HTML

`05_HISTORY_AND_VISUALS/prior-standalone-html/index.html` opens a comparison
menu for four complete, self-contained manuscript pages: v14, v15, v15.1, and
v15.2. Each page inlines its CSS and requires no server, script, font, or image.
They are honest manuscript renderings for editorial comparison, not invented
pixel reconstructions of historical site interfaces. The recovered v13
rendered DOM snapshot remains separately preserved under `v13-anchor/`.

## Rules for another GPT

- Preserve the no-results boundary.
- Do not describe benchmark-stipulated relation labels as discovered real-world
  provenance or independence.
- Do not silently promote protocol v1.1 from draft to canonical.
- Keep F0 descriptive, F1 rule-only, F2 supplied-cue, and T1 outside the
  confirmatory denominators.
- Preserve null, rule-only, invalidity-only, harmful, shortcut-driven, fragile,
  non-transfer, and stopped outcomes.
- Preserve the v13 diagram byte-for-byte and label it as historical.
- Treat generated images as illustrations or process evidence, never as
  findings or system topology.
- Do not infer external authority from this archive. A fresh exact instruction
  is required for model/provider use, dataset acquisition, preregistration,
  participants, study execution, GitHub writes, deployment, or publication.
- Run the included checks before proposing a new canonical package.

## Visual provenance

`05_HISTORY_AND_VISUALS/image-candidates/IMAGE_USE_TABLE_V15_2.md` accounts for
every clean generated candidate, UI preview, derivative, historical image, and
production raster. The current reader uses only:

- the E2 derivative in the deeper Explore worked example; and
- the byte-identical v13 map at the end of the full public route as history.

The opening uses no generated hero. Explanatory visuals for the receipt,
relation change, and study conditions are live HTML/CSS.

Raw historical browser screenshots, temporary PDF page renders, nested review
ZIPs, and superseded QA rasters are intentionally excluded. The compact
Markdown/JSON model-review records and all material dispositions are included
under `04_REASONING_AND_QA/model-review-records/`.

## Standalone HTML boundary

The four files under `01_FINAL_OUTPUT/standalone-site/` are generated review
exports. They contain no framework runtime and have no local stylesheet or
image dependencies. Edit the canonical site source, rebuild, retest, and then
regenerate the standalone files; do not maintain the exports by hand.

## PDF boundary

The current PDF was generated with ReportLab, rendered to PNG page images, and
inspected across all 20 pages. It visibly states that HTML is canonical and
that no empirical results exist. It is untagged and should not replace the
semantic reader for accessibility review.

## Repository and publication boundary

This package is a local owner-review checkpoint. It does not push to
`adonisdv23/Pattern-Map`, open a pull request, deploy a Site, change the current
public URL, or publish a paper. Those remain separate owner decisions.

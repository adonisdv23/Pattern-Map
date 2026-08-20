# Final integration and QA report - Pattern Map v15.2

**Status:** `FINAL RELEASE RECEIPT`  
**Final disposition:** `OWNER_READY_WITH_MANUAL_INTERACTION_QA_RESIDUALS`  
**Review date:** 2026-08-19  
**Baseline:** `22f232701184812489843731b6fe27592118eb29` (sealed v15.1)  
**Release branch:** `codex/discrimination-layer-v15-2-overnight`  
**Release source commit:** recorded in the embedded
`00_START_HERE/PACKAGE_MANIFEST.json` after this report is committed. A tracked
file cannot contain the hash of the commit that contains itself without
creating a false self-reference.

## Outcome

V15.2 is accepted as a local owner-review checkpoint. It is a material
editorial, comprehension, accessibility, design, methods-disclosure, and
handoff improvement over v15.1 without changing the project's core conceptual
claim or implying an empirical result.

The release is not accepted as a published site, completed research paper,
validated system, or authorized study. No current supported-browser and
assistive-technology pass was available for the final build, so the disposition
retains explicit manual interaction residuals.

## Canonical final surfaces

| Surface | Status | Role |
| --- | --- | --- |
| `source/THOUGHT_PIECE_V15_2.md` | PASS | Canonical v15.2 public argument |
| `site/` | PASS, manual interaction residuals | Canonical editable Essay / Explore / Lab / Sources reader |
| `output/v15_2/standalone/` | PASS | Four current self-contained route exports |
| `output/v15_2/history-html/` | PASS | Self-contained v14, v15, v15.1, and v15.2 manuscript comparison pages |
| `output/pdf/PATTERN_MAP_V15_2_REVIEW_COMPANION.pdf` | PASS | 20-page untagged visual/print companion; HTML remains canonical |
| `source/READER_OUTCOME_AND_READING_PATH_V15_2.md` | PASS | Current 60-90-second / four-minute / nine-minute reader contract |
| `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md` | CANONICAL, UNRUN | Current protocol authority |
| `research/overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md` | DRAFT, NON-AUTHORIZING | Proposed clarification; not silently promoted |
| `assets/imagegen/IMAGE_USE_TABLE_V15_2.md` | PASS | Used / unused / rejected / audit-only image accounting |

## Independent acceptance results

### Methods and evidence

Final disposition from
`POSTFIX_METHODS_EVIDENCE_ACCEPTANCE.md`:

`PASS WITH EXPLICIT RESIDUALS - P0/P1_METHODS_EVIDENCE_CLOSURE_VERIFIED`

Verified closures include:

- exact all-assigned `A=300` conservative-risk meaning and decomposition;
- fixed `M=75` membership/hash from the restricted pre-run manifest;
- no validity or post-run filtering of the safety subset;
- locked F2-minus-F1 one-sided lower-bound margin greater than `-0.05`;
- explicit open interval, coverage, and paired-invalidity gates;
- coherent F1/F2 parity language;
- selected-model/no-run/no-result wording;
- `DPND` / `INDP` / `UNKN` semantics;
- every material open gate and the separation of a gate receipt from owner
  authorization; and
- the complete unfavorable-result ladder, including null, rule-only,
  invalidity-driven, threshold-only, harmful, direct-code/field-only,
  surface/semantic-audit failure, unstable, noise-fragile, non-transfer, and
  stopped/quarantined outcomes.

One P2 maintainability residual remains: fictional receipt `ORIGIN-EX-01` has
aligned compact, detailed, presentation, and generated representations. It is
not an evidence-status blocker. A future typed shared object or consistency
test would reduce drift.

### Site and static accessibility

Final disposition from `POSTFIX_SITE_STATIC_ACCEPTANCE.md`:

`PASS WITH MANUAL QA RESIDUALS`

Static evidence covers current route content, single-H1 structure, unique and
resolvable identifiers, skip targets, current `aria-current`, term-explanation
structure, focus-return code paths, in-flow popover fallback, CSS focus states,
responsive/print definitions, current no-results wording, and standalone
self-containment.

## Exact final local checks

All tests were local and offline. They are software/release checks, not model
or empirical evidence.

| Check | Result |
| --- | --- |
| `cd site && npm run lint` | PASS |
| `cd site && npm test` | PASS: Vinext production build completed; 7/7 server-rendered route tests passed |
| `pytest -q tests/test_origin_accounting.py` | PASS: 15 tests |
| Python compile check over `tools/origin_accounting` and `tests` | PASS |
| `python -m tools.origin_accounting.cli parser-fixtures` | PASS: 18/18 fixtures |
| Offline harness smoke check | PASS as wiring/readiness only; no provider/model/network call; no primary split opened; not an empirical result |
| Standalone v15.2 route builder and current-state scan | PASS |
| Standalone Lab correction assertion | PASS: 10/10 required safety/open-gate/result-ladder strings |
| Historical HTML generator compile and regeneration | PASS |
| Historical HTML static parser scan | PASS: each page has one H1; no scripts, images, external stylesheets, or unexpected local dependencies |
| `SOURCE_VERSIONS_USED.json` parse | PASS |
| Python/Node builder syntax checks | PASS |
| `git diff --check` | PASS |

The Vinext build prints its normal note that automatic route classification is
incomplete for some routes. The four intended routes build and server-render;
the note did not produce a failed check.

## Standalone HTML verification

The current route bundle contains:

- `index.html` - public essay and three cumulative stops;
- `explore.html` - detailed framework, records, loops, visuals, and cases;
- `lab.html` - proposed study, exact measures, open gates, and no results;
- `sources.html` - source status, glossary, and history.

Each file inlines current CSS and every rendered local PNG/JPEG as data. It has
no dependency on a local stylesheet, Vinext/React runtime, development server,
or local image path. Inter-route links are rewritten to sibling HTML files.

The historical comparison contains v14, v15, v15.1, and v15.2 as four separate
self-contained manuscript pages plus an index and source/output hash manifest.
These pages are explicitly labeled as generated manuscript renderings, not
pixel reconstructions of historical site interfaces. The v15 source is
recovered from sealed commit `82f87b1d57414d4e7b1d2637a8fa53799d5ccf4d`;
the v15.1 source is not silently substituted for it.

## PDF verification

`PATTERN_MAP_V15_2_REVIEW_COMPANION.pdf` was generated through the established
ReportLab renderer, then inspected as rendered page images.

- 20 A4 pages;
- title and metadata identify v15.2;
- no JavaScript, form, encryption, rotation, or embedded runtime;
- untagged by design and visibly labeled as a visual/print companion;
- every page carries the no-empirical-results footer;
- all 20 pages were reviewed in contact sheets;
- methods/result pages were inspected individually after correction;
- the final source-reference page was re-rendered and inspected after changing
  the stale compatibility filename to
  `source/THOUGHT_PIECE_V15_2.md - canonical v15.2 content`;
- extracted text contains no stale v15.1 release label; and
- the Unicode-dash scan passes the PDF output contract.

The PDF ZIP contains versioned visual companions, not pixel captures of every
interactive route. The standalone HTML is the direct site/manuscript review
surface and the more accessible source.

## Image and provenance verification

Every eligible generated design candidate, image-generation UI preview,
historical anchor, and production raster is listed in
`IMAGE_USE_TABLE_V15_2.md`.

- E2 production derivative: used only in Explore as illustration;
- v13 map: used only as a historical anchor and preserved byte-identically;
- hero candidates: unused/rejected;
- social-card candidate and `og.png`: retained, not referenced in v15.2;
- image-generation UI previews: audit only;
- current semantic microvisuals: HTML/CSS, not generated rasters.

The earlier selection ledger was reconciled so it no longer says the social
card is used by the final local site. Raw historical QA screenshots, former
review-interface captures, and temporary PDF render pages are intentionally
excluded from the owner ZIP; their material findings and text records remain.

## Package completeness and integrity

The deterministic owner archive uses an explicit role-based allowlist. It
contains:

- a clear `01_FINAL_OUTPUT/` current-output folder;
- an archive-specific start README with valid archive-relative links;
- the owner packet, this report, end-to-end reasoning narrative, package map,
  source/version records, and version-history table;
- current site, manuscript, PDF, and standalone routes;
- all four historical standalone manuscript pages;
- research protocols, memos, experiments, offline implementation, and tests;
- all eligible image candidates and use ledger;
- compact Markdown/JSON model-review records and dispositions;
- sealed history and prior PDFs; and
- reproduction builders.

Dependencies, build products, caches, temporary render rasters, nested review
ZIPs, superseded screenshot packets, existing transfer archives, credentials,
and environment files are excluded.

**Pre-commit package dry-run:** PASS - 239 allowlisted files, approximately
48.7 MB before ZIP compression; no duplicate destinations or forbidden build,
cache, key, environment, or credential-like file types.

**Final archive creation and CRC/SHA-256 verification:** `PASS`. From a clean
committed payload, the deterministic builder created the owner archive (239
allowlisted payload files plus its embedded manifest) and the five-member PDF
review archive. Both ZIPs were reopened, every member passed CRC/byte
verification, required paths were asserted, forbidden build/credential paths
were absent, and independently recalculated SHA-256 values matched the
sidecars. The archive is rebuilt once more after this final receipt is committed;
the definitive source commit, member sizes, and per-member hashes are recorded
in its embedded and external package manifests.

## External-action and evidence boundary

- Empirical-study model/provider calls: 0.
- Pilot or primary runs: 0.
- Primary split opened: no.
- Participants: 0.
- External datasets acquired: no.
- Preregistration: no.
- Deployment/publication: no.
- GitHub push, PR, merge, tag, or repository-setting change: no.
- Production or Signal Foundry mutation: no.

Design-image generation and model-assisted editorial/research critique did
occur and are documented. They are not empirical evidence for the framework
and are not counted as study/provider calls.

## Claude message status

The owner authorized sending a prepared Claude course-correction and asked
that local work continue immediately afterward. The Claude tab entered an
elevated re-authentication screen before submission. The exact message is
preserved in `CLAUDE_MESSAGE_STATUS.md`; no credential handling or bypass was
attempted. Delivery remains pending and did not block the local release.

## Manual acceptance residuals

Before publication or a claim of fully operated accessibility, verify in a
supported browser and relevant assistive technology:

1. keyboard open/close, Escape, light dismiss, and trigger-focus return for
   term explanations;
2. screen-reader announcement of explanation triggers and expanded content;
3. mobile and tablet popover/bottom-sheet placement and collision behavior;
4. no-popover fallback in a browser without the native Popover API;
5. forced-color visibility and focus indicators;
6. desktop/mobile/tablet navigation and long-record close behavior; and
7. print preview, page breaks, expanded definitions, and hidden controls.

These checks are short and important, but they do not authorize publication,
deployment, or the proposed study.

## Final decision

`OWNER_READY_WITH_MANUAL_INTERACTION_QA_RESIDUALS`

V15.2 is ready for the owner's first serious read. The next evidence should
come from the owner and real cold readers, followed by one bounded voice and
comprehension revision. Another unconstrained design/research expansion should
not precede that checkpoint.

# V15.1 final validation

Recorded: 2026-08-19

Status: `PASS · LOCAL OWNER REVIEW · NO EMPIRICAL RESULTS · NOT PUBLISHED`

This receipt covers the v15.1 convergence work. It validates local execution,
reader behavior, packaging structure, and epistemic labels. It does not validate
the framework’s effectiveness, establish scientific novelty, or authorize an
empirical run.

## Release surface

- Branch: `codex/discrimination-layer-v15-1`
- Base checkpoint: sealed v15 commit `82f87b1`
- Canonical site: `site/`
- Canonical manuscript compatibility path: `source/THOUGHT_PIECE_V15.md`
- Visual companion: `output/pdf/PATTERN_MAP_V15_1_REVIEW_COMPANION.pdf`
- Owner package: `output/PATTERN_MAP_V15_1_OWNER_REVIEW.zip`
- PDF comparison package: `output/PATTERN_MAP_V15_1_PDF_REVIEW.zip`

The archive builder records the exact final source commit and file hashes in
its embedded and adjacent manifests after the payload is committed.

## Loop 1 — evidence and methods

### Commands

```sh
git diff --check
python3 -m compileall -q tools/origin_accounting tools/build_v15_1_package.py tests
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 -m tools.origin_accounting.cli parser-fixtures
python3 -m tools.origin_accounting.cli smoke --out <temporary>/smoke
python3 -m tools.origin_accounting.cli generate --out <temporary>/full
python3 -m tools.origin_accounting.cli power \
  --out <temporary>/power \
  --repetitions 1 \
  --bootstrap-repetitions 5 \
  --vor-bootstrap-repetitions 5 \
  --vor-n 10
```

### Result

- `git diff --check`: pass.
- Python compile: pass.
- Unit tests: **15 passed**.
- Parser fixtures: **18 passed**.
- Offline smoke: pass; `model_calls=0`, `provider_calls=0`,
  `network_calls=0`, `primary_opened=false`.
- Full deterministic generation: pass; **480 fictional bundles** and **1,440
  prompt instances** generated with no model/provider integration.
- Reduced power scaffold: pass; status
  `planning_only_no_pilot_or_model_outputs`.

The reduced power command is a wiring check. Its numbers are not a power
finding and cannot authorize a primary run.

### Construct correction

The first descriptive-diagnostics draft incorrectly risked penalizing neutral
or refuting reports merely because they were selected for assessment. The
integrated version measures support-origin recovery only among selected reports
whose benchmark stance is `supports`. Unknown and contested support-only sets
are unscored, and empty-set behavior is explicit. FC_cons, VOR, F0/F1/F2,
primary denominators, and confirmatory interpretation remain unchanged.

### Prior-art boundary

The targeted update adds correlation-aware data integration as a mature
precedent and blocks a broad dependence/correlation novelty claim. It does not
claim a systematic review and does not add a study arm. The remaining empirical
question stays narrow: supplied origin-relation labels versus a plain explicit
rule under matched fictional evidence.

## Loop 2 — editorial, information architecture, and accessibility

### Commands

```sh
cd site
npm run lint
npm test
```

### Result

- ESLint: pass.
- Production Vinext build: pass.
- Routes built: `/`, `/explore`, `/lab`, `/sources`.
- Rendered-HTML tests: **7 passed**.
- Unique IDs and same-page fragment targets: pass on all routes.
- Local-only/noindex metadata: pass.
- Print table behavior and focus styling: pass.
- No starter preview or loading placeholder remains.

### In-app browser checks

- Desktop first-fold inspection at the normal 1280×720 viewport: pass; the
  proposition is legible in plain language and the page does not overflow
  horizontally.
- Mobile inspection at 390×844: pass; the N=300 explanation behaves as a
  bottom sheet within the viewport and includes the compact 30-dot / 300-bundle
  visual.
- Escape closes the explanation and returns focus to its trigger: pass.
- Definition, example, and “what it does not mean” boundary are exposed to the
  accessibility tree: pass.
- Stable disclosure IDs are unique; no hydration mismatch is logged: pass.
- Final console inspection contains development connection and React DevTools
  information only; no warning or error: pass.

### Reader acceptance

The first fold no longer requires a reader to decode F0/F1/F2, T1, N=300, or
the negative-result commitment. The visible text gives ordinary-language
meaning first. The full glossary remains available under `/sources`; term
popups deepen rather than rescue the prose.

## Loop 3 — PDF, adversarial handoff, and packaging

### PDF checks

- Generator: `tools/render_v15_reader_pdf.py` using the bundled ReportLab
  runtime.
- Pages: **20**.
- Page size: A4.
- Text extraction: all 20 pages nonempty; 27,991 extracted characters.
- Minimum/maximum extracted characters per page: 623 / 2,065.
- Metadata title: `Pattern Recognition: The Discrimination Layer — v15.1`.
- Encryption: none.
- Embedded JavaScript: none.
- Visual inspection: all 20 latest page renders reviewed across five contact
  sheets; no clipping, overlap, missing image, stray page, or illegible table
  was found.

The PDF is deliberately untagged. Semantic HTML and Markdown remain the
canonical accessible surfaces.

### Browser-print limitation

An attempted exact browser-print export of the four site routes reached a
browser permission request that was declined. The permission was not bypassed
through another browser surface. The delivered v15.1 PDF is the existing
ReportLab visual-review companion, not a claim that the four routes were
printed exactly.

### Package checks

`tools/build_v15_1_package.py` is the release sealer. It:

- requires every selected payload file to be tracked, committed, and identical
  to `HEAD`;
- uses an explicit role-based allowlist;
- excludes dependencies, build output, caches, raw QA rasters, credentials,
  environment files, and nested owner ZIPs;
- writes a fixed ZIP timestamp and sorted member order;
- embeds source-to-archive paths, byte counts, and SHA-256 hashes;
- verifies member safety, timestamps, ordering, content, uniqueness, and CRC;
  and
- creates adjacent SHA-256 sidecars for the main and PDF-review archives.

The structured main archive opens with `00_START_HERE/` and identifies
`01_FINAL_OUTPUT/` as the final-output folder. It includes the site, manuscript,
current PDF, research program, reasoning/QA, v13 anchor, all current image
candidates and their selection ledger, prior v14/v15 PDFs, and reproduction
tools.

## External-action receipt

- Model selected: no.
- Model/provider call: no.
- Study or pilot run: no.
- External dataset acquired: no.
- Participant contacted: no.
- Preregistration: no.
- Site deployed or published: no.
- GitHub push, PR, tag, release, merge, default-branch change, or setting
  mutation: no.

## Remaining owner decisions

1. Does the 60–90 second path communicate the intended idea in the owner’s
   voice?
2. Does the name “The Discrimination Layer” create more clarity than social-
   classification ambiguity?
3. Which review/history materials belong in the future public GitHub root?
4. Is the reusable receipt valuable enough to test with practitioners?
5. Only later: should a model/tokenizer/budget be selected and the unrun study
   proceed through its gates?

# V15 final validation and release receipt

- **Validation date:** 2026-08-18 (America/New_York)
- **Target:** canonical local v15 owner-review package
- **Current verdict:** `PASS_FOR_LOCAL_OWNER_REVIEW`
- **Empirical status:** no pilot, primary run, model output, or research result
- **External status:** not published, deployed, pushed, preregistered, or sent

This report consolidates the final validation surface. The three mandatory
improvement loops retain their own defect and post-fix reports; this record does
not replace them.

## 1. Runtime receipt

| Runtime | Version used |
| --- | --- |
| Python | 3.12.13 at `/Users/gpt/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3` |
| Node.js | 22.23.2 for the final site commands |
| npm | 10.9.8 |

No dependency was installed from the network during the final validation pass.
The committed site lockfile and existing local dependencies were used.

## 2. Offline research scaffold

Commands:

```text
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 -m compileall -q \
  tools/origin_accounting tests \
  tools/build_v15_package.py tools/verify_v15_package.py
python3 -m tools.origin_accounting.cli parser-fixtures
python3 -m tools.origin_accounting.cli smoke --out <temporary>/oa-smoke
python3 -m tools.origin_accounting.cli generate --out <temporary>/oa-full
python3 -m tools.origin_accounting.cli power \
  --out <temporary>/oa-power \
  --repetitions 1 \
  --bootstrap-repetitions 5 \
  --vor-bootstrap-repetitions 5 \
  --vor-n 10
```

Result: **PASS**.

| Check | Final result |
| --- | --- |
| Unit tests | 12/12 pass |
| Compile check | pass |
| Parser fixtures | 18/18 pass |
| Smoke corpus | 16 bundles, 64 reports, 48 prompts |
| Smoke external calls | 0 model, 0 provider, 0 network |
| Smoke leakage receipt | `precheck_pass`; authoritative clearance remains `unresolved` |
| Full fictional generation | 480 bundles, 1,920 reports, 1,440 prompts |
| Protocol identity | `origin-accounting-protocol-v1.0` |
| Primary manifest | 300 unique ordered IDs |
| Safety manifest | 75 unique ordered IDs; exact subset of primary manifest |
| Model | `UNSELECTED` |
| Local tokenizer | `deterministic-regex-surrogate-v1`; explicitly not a model tokenizer |
| Unknown-origin stress | 15 F2 prompts, 60 relation rows, every visible code `UNKN` |
| Reduced FC planning grid | 1,440 cells, 0 skipped |
| Reduced VOR planning grid | 128 valid cells, 16 mathematically invalid cells explicitly skipped |
| VOR smoke sample | `n=10`; protocol expectation remains fixed `M=75` |

The power command is a bounded wiring smoke with one simulated repetition and
five bootstrap draws. It is not the full production planning simulation, a
pilot, or an empirical result.

### Orchestration readback note

The first composite validation wrapper successfully completed all substantive
Python commands but then exited 1 while its summarizer looked for the obsolete
path `oa-smoke/run_manifest.json`. The current CLI correctly emits
`oa-smoke/receipt.json` and `oa-full/release/manifest.json`. The readback path
was corrected and the complete command matrix was rerun from a fresh temporary
directory with exit 0 and the results above. This was a validation-wrapper typo,
not a product, generator, test, or receipt failure.

## 3. Interactive reader

Commands:

```text
cd site
npm run lint
npm test
```

Result: **PASS**.

- ESLint passed.
- The Vinext production build completed.
- Five of five rendered-HTML tests passed.
- The suite checked the single H1, unique identifiers, complete same-page
  fragment targets, eleven component disclosures, eleven visible summary
  statuses, keyboard-returning close controls, the typed receipt, `UNKNOWN`
  semantics, F0/F1/F2, descriptive T1, `No F3 exists`, no-results boundaries,
  local-only metadata, eager local images, serif typography, two-tone focus,
  and print-table rules.

The build reports the Vinext beta’s generic “some routes could not be
classified” informational notice for `/`; it does not fail the build or test.
No deployment was attempted.

Live geometry and responsive evidence remain in
`reports/V15_VISUAL_AND_ACCESSIBILITY_QA.md`: 1440×1000, 768×1024, 390×844,
320×800, and a 640×360 CSS-viewport reflow proxy all avoided page-level
horizontal overflow. The screenshot and live-zoom limitations remain explicit.

## 4. Cross-artifact structure and semantics

A standard-library/PyPDF assertion pass produced:

| Check | Result |
| --- | --- |
| Final repository JSON/config/schema files parsed | 28, including the generated package manifest |
| Canonical framework families | 6, exactly F1–F6 |
| Canonical framework components | 11, exactly C01–C11 |
| Judgment dimensions | 8, exactly D01–D08 |
| D04 | `origin_relation` |
| Prior-art source cards | 19, exactly S1–S19 |
| Required fields per source card | 19 each for sourced fact, exact finding, project inference, blocked claim, residual contribution, and disposition |
| Confirmatory family | F0/F1/F2 present and preserved |
| F3 | explicit absence preserved |
| T1 | descriptive and denominator-firewalled |
| Unknown semantics | `UNKN`/`UNKNOWN` preserved |
| No-results boundary | present across canonical surfaces |
| Fixed sets | `A=300`, `M=75` preserved |

The exact v13 archive and site copy remain byte-identical at SHA-256
`8a8204a05e993e84f2bd9037c59b7beb2ab6b4bca89304e299f66b3961f203ae`.

The compact package allowlist currently selects 101 files and all 27 relative
Markdown links among those files resolve to another packaged file. It excludes
dependencies, build products, caches, intermediate QA rasters, v0/v14 final
surfaces, old overnight memos, and unrelated review bundles.

A bounded release scan inspected 95 text-like payload files for private-key
headers and common OpenAI, Google, bearer-token, API-key, client-secret, and
password-assignment patterns. It found zero matches. This is a release hygiene
check, not a general secret-detection guarantee.

## 5. PDF

Structural recheck: **PASS**.

| Property | Final value |
| --- | --- |
| File | `exports/THOUGHT_PIECE_V15.pdf` |
| SHA-256 | `0542cdd14311fd07f7d9fa5e02c05584e83ed31d4d2cb07f305c5e3751254dca` |
| Pages | 20 |
| Page size | A4 on every page |
| Tagged | no |
| Encryption | none |
| Forms | none |
| JavaScript | none |
| Open action | none |
| Replacement glyphs in extracted text | none |
| No-results/untagged footer | exactly once on each page |
| Attribution correction | `Strittmatter et al. · 2024` and `Schelpe` present; erroneous `Schelpe et al. · 2024` absent |

The final PDF was previously rasterized at 120 dpi and all 20 pages were
inspected, including dense tables and high-consequence boundary pages. No
clipping, overlap, broken table, empty page, black square, missing illustration,
or unreadable glyph was observed. The PDF remains explicitly untagged; HTML and
Markdown are canonical.

## 6. External links and citation status

`reports/V15_EXTERNAL_LINK_AND_CITATION_VALIDATION.md` records the exact pass:

- 131 unique HTTP(S) targets;
- 110 direct 2xx responses;
- 16 working DOI resolver redirects whose publisher destination denied the
  bounded automated client;
- three official BMJ/HHS records independently confirmed after curl 403;
- two exact ETH records independently confirmed after curl 500;
- zero transport failures; and
- zero 404/410 responses.

The S1–S19 status ledger remains explicit: 12 published contributions, five
unreviewed working manuscripts/preprints, one qualified acceptance record, and
one current official handbook chapter. No preprint was promoted and no
unsupported priority claim was introduced.

## 7. Improvement loops

| Loop | Initial review | Post-fix validation | Result |
| --- | --- | --- | --- |
| Evidence / novelty | `reports/V15_LOOP1_EVIDENCE_NOVELTY_REVIEW.md` | `reports/V15_LOOP1_EVIDENCE_FIX_VALIDATION.md` | pass |
| Construct / method | `reports/V15_LOOP2_METHOD_ADVERSARIAL_REVIEW.md` | `reports/V15_LOOP2_METHOD_FIX_VALIDATION.md` | pass |
| Reader / accessibility | `reports/V15_LOOP3_READER_DESIGN_ACCESSIBILITY_REVIEW.md` | `reports/V15_LOOP3_READER_FIX_VALIDATION.md` plus root live QA | pass with disclosed tool limitations |

No loop produced a P0 defect that remains open. Loop 2’s P1 implementation
findings were repaired without changing the estimand or protocol. Loop 3’s P1
and P2 presentation defects were repaired and rechecked.

## 8. Release package

Status: **PASS**.

The deterministic builder and independent verifier are implemented at
`tools/build_v15_package.py` and `tools/verify_v15_package.py`. A committed
101-file payload was sealed and checked as follows:

| Package check | Result |
| --- | --- |
| Payload manifest entries | 101 |
| SHA-256 checksum entries | 102: every payload file plus the manifest |
| ZIP members | 103: payload plus manifest and checksum ledger |
| ZIP CRC | pass |
| Sorted member allowlist | exact match |
| Fixed timestamps and `0644` modes | pass |
| Two consecutive builds from one source commit | byte-identical ZIP hash |
| ZIP sidecar hash | pass |
| Filesystem-to-ZIP byte comparison | pass |
| Fresh extracted-copy verification | pass |
| Branch-wide whitespace/error-marker diff check | pass |
| Final integration-worktree status after seal | clean |

The archive is regenerated from the commit containing this completed receipt.
Its authoritative source commit and payload hashes live in
`handoff/V15_PACKAGE_MANIFEST.json`; its final container hash lives in
`exports/DISCRIMINATION_LAYER_V15_OWNER_PACKAGE.zip.sha256`. The sidecar is
outside the archive because a ZIP cannot contain its own final checksum.

## 9. Remaining limitations and authorization stops

The package is ready for owner review, not a live study or public release.
Remaining stops include:

1. no selected model/checkpoint/intended tokenizer or budget;
2. no intended-tokenizer/backend chat-template parity;
3. no authoritative exhaustive leakage/near-duplicate or independent semantic
   audit;
4. no independent JSON-Schema/RFC 8785 conformance pass;
5. no full planning-grid/coverage/interval-method freeze;
6. no T1 rights or annotation clearance;
7. no formal WCAG audit, screen-reader matrix, actual browser-zoom observation,
   or browser print-preview inspection;
8. an untagged PDF; and
9. unresolved owner choices on name, map freeze, paper priority, T1 roadmap,
   and any external action.

A new explicit authorization is required before a model/pilot/primary run,
provider spend, preregistration, participant contact, ethics/IRB decision,
external dataset acquisition or redistribution, publication, deployment, push,
PR, merge, message, permission change, or production mutation.

## 10. Final gate decision

**PASS FOR LOCAL OWNER REVIEW.** The required v15 artifacts are canonical,
reconciled, validated, visually inspected, and package-verifiable. The HTML and
Markdown remain canonical accessible surfaces; the PDF remains visibly
untagged; the research program remains unrun; descriptive T1 remains outside
the confirmatory/safety denominators; unfavorable-result handling remains
locked; and every external-action gate remains closed.

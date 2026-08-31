# Public-surface accessibility and navigation QA — 2026-08-30

## Status and scope

**Controlled disposition: Accepted with revision for this local implementation lane.** The verified contrast, document-navigation, review-indexing, and 90-second-entry defects were corrected from baseline `76ade6e2c255151e32ddd9cbb3d4650cf46570d1` on branch `codex/pattern-map-v16-ultra-finalization`. This is an automated and source-inspection record, not a publication decision or evidence of reader effectiveness.

The locked owner-intent checkpoint was verified before and after implementation with `shasum -a 256 -c OWNER_INTENT_V16.sha256`: `OWNER_INTENT_V16.md: OK`. No archive, Echo-source, Signal Foundry, release-gate, or PDF source was edited.

## Findings and controlled dispositions

| ID | Verified finding | Disposition | Implemented correction |
| --- | --- | --- | --- |
| PS-01 | The normal and hover links in the purple Echo callout failed normal-text contrast. | Accepted | Added an inverse-surface palette and explicit normal, visited, hover, and focus-visible states without weakening the focus indicator. |
| PS-02 | Contrast automation checked selected palette tokens against paper but did not validate the actual dark-callout state pairs; its PASS wording overstated scope. | Accepted with revision | Added selector-to-token assertions and computed foreground/background checks for navy and Echo callout text, links, and focus indication. Narrowed the PASS label to its tested scope. |
| PS-03 | Document-labeled links collapsed distinct rendered and non-rendered documents into coarse route, disclosure, or Echo section links. The Echo callout linked to its own section. | Accepted with revision | Added path-exact document destinations and stable rendered IDs. Non-rendered documents are now non-link owner-package references with exact repository paths. Removed the Echo self-link and targeted the rendered identity/no-results record. |
| PS-04 | Hash targets nested in closed disclosures were not explicitly revealable by the shared runtime. | Accepted with revision | Initial-load and hash-change handling opens every enclosing disclosure, scrolls only after a reveal, and never moves focus. A same-hash click fallback is compatibility hardening; it does not prevent native navigation. The mentor handoff now targets content inside its disclosure so native/no-script ancestor reveal also applies. |
| PS-05 | Review-mode output lacked a defense-in-depth crawler directive. | Accepted | Added `noindex,nofollow` to every routed review document and the review standalone. Public output remains fail-closed unless the existing release-metadata gate is satisfied. |
| PS-06 | The 90-second heading exposed the internal framework name before stating the human function. | Accepted with revision | Changed only the heading to “Improve the room before the answer.” The 250-word body, broad thesis, all six families, Echo separation, and no-results boundary remain covered by the reader-language contract. |
| PS-07 | Canonical standalone exports did not contain the corrected source navigation, heading, callout states, and review metadata. | Accepted | Rebuilt both standalone exports from `site/build.mjs`; routed build products remained untracked local outputs. |
| PS-08 | Physical-device, assistive-technology, and reader-effectiveness evidence was not produced by this lane. | Deferred | Retained as explicit manual/owner gates below. |

## Computed contrast evidence

Ratios use the same sRGB relative-luminance calculation enforced by `site/check.mjs`. They are computed state-pair checks, not a claim of visual testing in a real browser or assistive technology.

| State pair | Before | After | Threshold used |
| --- | ---: | ---: | ---: |
| Echo normal link on `#3b304c` | `#9d442d`, 1.93:1 | `#f1bd80`, 7.20:1 | 4.5:1 |
| Echo visited link on `#3b304c` | not explicitly controlled | `#f1bd80`, 7.20:1 | 4.5:1 |
| Echo hover link on `#3b304c` | `#152022`, 1.36:1 | `#fff6dd`, 11.37:1 | 4.5:1 |
| Echo focus text on focus fill | inherited link treatment | `#3b304c` on `#fff6dd`, 11.37:1 | 4.5:1 |
| Echo focus outer indicator on `#3b304c` | shared outline only | `#f1bd80`, 7.20:1 | 3:1 |
| Echo heading on `#3b304c` | not state-pair tested | `#f6f3e9`, 11.04:1 | 4.5:1 |
| Echo body on `#3b304c` | not state-pair tested | `#d7e1de`, 9.17:1 | 4.5:1 |
| Navy callout heading on `#162d36` | not state-pair tested | `#f6f3e9`, 12.93:1 | 4.5:1 |
| Navy callout body on `#162d36` | not state-pair tested | `#d7e1de`, 10.74:1 | 4.5:1 |
| Navy callout eyebrow on `#162d36` | not state-pair tested | `#f1bd80`, 8.43:1 | 4.5:1 |

## Affected files

- `manuscript/NINETY_SECOND_VERSION.md`
- `qa/content/reader-language-contract.spec.mjs`
- `qa/site/public-mode-contract.spec.mjs`
- `qa/site/source-navigation-disclosure-contract.spec.mjs`
- `qa/site/PUBLIC_SURFACE_ACCESSIBILITY_NAVIGATION_QA_2026-08-30_76ade6e.md`
- `site/build.mjs`
- `site/check.mjs`
- `site/src/site.css`
- `site/src/site.js`
- `site/exports/standalone/pattern-map-v16.html`
- `site/exports/standalone/pattern-map-v16-public.html`

## Validation record

| Command | Result |
| --- | --- |
| `npm run build` from `site/` | PASS — generated 10 review routes, review standalone, 10 public routes, and public standalone from the canonical generator. |
| `node qa/site/source-navigation-disclosure-contract.spec.mjs` | PASS — exact rendered destinations, all 11 stable document targets in both modes and standalones, owner-package path honesty, disclosure nesting, malformed-hash safety, and focus-neutral reveal behavior. |
| `node qa/content/reader-language-contract.spec.mjs` | PASS — 250 words, functional heading order, six-family coverage, and retained reader routes. |
| `npm run check` from `site/` | PASS — complete documented site/content/interaction suite, including the focused contract above. |
| `python3 qa/site/audit_site.py` | PASS — structural route, heading, no-script, progressive-disclosure, link, and standalone checks; the script explicitly states that this is not comprehension/effectiveness evidence. |
| `shasum -a 256 -c OWNER_INTENT_V16.sha256` from `docs/` | PASS — `OWNER_INTENT_V16.md: OK`. |
| Scoped `git diff --check` | PASS — no whitespace errors in lane-owned changes. |
| `qa/site/headless_print_contract.sh` | SKIP — `pdftotext` is unavailable; exit status was zero, but this is not counted as a print PASS. |

## Limitations and manual gates

This lane did **not** establish physical-keyboard behavior, screen-reader announcements or reading order, real 200% browser zoom, real forced-colors rendering, native print output, hardware touch behavior, reader comprehension, reader effectiveness, or publication readiness. Those remain manual/owner-review gates. No PDF was regenerated, no public surface was deployed or published, no paid provider was selected, and no model, participant, pilot, or empirical study was run.

The source resolver intentionally guarantees document-level destinations for the current canonical corpus. No current rendered source link requests a mapped file plus a subheading fragment or query string; a future subdocument-fragment policy is deferred rather than inferred here.

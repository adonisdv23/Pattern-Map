# ChatGPT Pro Round 2 correction QA

Status: **IMPLEMENTATION PASS — FINAL DRAFT-PR READBACK REQUIRED AFTER THE EVIDENCE PUSH**

Reviewed advisory target:
`4d2505e7f3d325fe7b8ef5e2e5c3a634a11aa9fe`.

Coherent correction implementation checkpoint:
`c88926034cd75773dcc42d3842983c879dda5b58`.

The complete advisory output is preserved at
`qa/site/advisory/CHATGPT_PRO_INDEPENDENT_REVIEW_ROUND_2_2026-08-22_4d2505e.md`.
It is model feedback, not evidence, owner acceptance, accessibility
certification, or authorization. This note distinguishes source assertions,
executable checks, current live-browser observations, and manual residuals.

## Outcome first

All five bounded Round 2 P1 implementation findings are corrected at
`c889260`. No locked thesis, headline, six-family, three-door, human-authority,
Echo, Signal Foundry, no-results, or external-action boundary changed.

The remaining external metadata step is deliberately performed after the
final evidence commit is pushed: refresh draft PR #1, then read it back and
confirm that it is still open, draft, unmerged, and accurately describes the
current head. A repository checkpoint cannot prove a later GitHub metadata
readback about itself; the orchestrator must report that readback separately.

## Round 2 P1 closure matrix

| Finding | Source correction | Direct or executable evidence | Status |
| --- | --- | --- | --- |
| `PM16-R2-01` — Apply omitted Stage 0 | Apply now begins with `evidenceSelection = none | needed`. `none` stays ordinary; `needed` can never be ordinary; restricted permission still yields `CLARIFY`; a named human gate still yields `HOLD`. | `qa/interaction/apply-state-contract.spec.mjs` exhausts the full 2×2×3×3×3 matrix: 108 combinations. Every result is planning-only and the immutable observed-state object remains `NOT_RUN / NOT_TRIGGERED / NOT_OBSERVED / NOT_AVAILABLE / NOT_RECORDED`. | **PASS** |
| `PM16-R2-02` — stale draft PR body | A replacement PR description is prepared around the 250-word entry, ten routes, Guided, line-free relationship map, four limited relationship bands, planning-only Apply, immutable unrun/unobserved state, superseded screenshots, and current evidence. | Final completion requires post-push `gh pr view` readback. Base/head, draft/open state, and prohibited old language must be checked after the last evidence push. | **PENDING EXTERNAL READBACK** |
| `PM16-R2-03` — Home preview implied completed records/events | The aria-hidden Apply preview now reads `TASK CONDITIONS`, `recommendation → gate`, `planned boundary`, and `choose → recommend → review`. Receipt-prefixed classes were renamed to plan-prefixed classes. | `site/check.mjs` extracts the preview and rejects the old `DECISION BRIEF` and `human disposition` strings. A 390-pixel live inspection shows the new four-part sequence and no overflow. | **PASS** |
| `PM16-R2-04` — term-help accessible name, no-script, and medium containment | Each compact `See it` control has a concept-specific accessible name such as `Explain baseline`. No-script hides inert term buttons and progress widgets while preserving inline meaning. Term panels are flow-native from 601 through 1100 pixels. | Site and reader-language checks require descriptive names, at least six distinct concepts, no-script selectors, print suppression, and the medium in-flow rule. Live computed-style checks pass at 601, 768, 821, 1024, and 1100 pixels with `position: static`, `width: 100%`, and no document overflow. | **PASS WITH MANUAL KEYBOARD/SCREEN-READER RESIDUAL** |
| `PM16-R2-05` — compressed mobile route brief and undersized route controls | The conflicting late three-column mobile override is removed. The existing one-column route brief governs at ≤820 pixels. Primary/secondary navigation, orientation links, and the mobile orientation summary now share the 2.75rem minimum target contract. | Source checks reject a ≤600 three-column override. Live checks at 320, 390, 480, and 600 pixels show one full-width column, all three principal links visible, 44-pixel minimum visible route targets, and `scrollWidth === innerWidth`. | **PASS WITH MANUAL TOUCH/KEYBOARD RESIDUAL** |

## Direct source assertions

- `site/src/recommendation.js` validates five independent planning axes. Stage
  0 is not inferred from reversibility, consequence, uncertainty, or budget.
- `site/src/site.js` passes the explicit Stage 0 value to the pure recommender
  and still redraws the immutable observed-state baseline after every plan.
- `site/build.mjs` renders five fieldsets and a complete static no-script
  equivalent. The static guide states that Stage 0 `no` creates no evidence
  records, while Stage 0 `yes` chooses at least lightweight.
- The Map keeps only one polite focus announcement. The detailed focus status
  remains visible ordinary text, reducing duplicate-announcement risk without
  hiding information.
- The all-routes export now describes itself as direct-open within the
  repository package and explicitly identifies its one repository-relative
  historical image. It no longer calls itself a fully detached single file.
- The historical Round 1 QA report remains unchanged. Its phrase saying the
  old 54 combinations covered “repeatability” was inaccurate: the fourth
  axis was **budget**. This transparent correction supersedes that wording for
  current evidence; it does not rewrite the old exact-checkpoint report.

## Executable verification at the correction checkpoint

Focused commands:

```text
(cd site && npm run build)
PASS built 10 routed pages and refreshed the committed all-routes export

(cd site && npm run check)
PASS routes: 10
PASS Stage 0, descriptive term controls, mobile route brief, and medium-popover contracts
PASS Apply Stage 0 and planning-state contract across 108 combinations
PASS line-free map semantics and wide/medium/narrow layout contracts
PASS reader-language contract (249 words, six families, guided and accessible term-help routes)

python3 qa/site/audit_site.py
PASS semantic landmarks/headings/names on all 10 routes
PASS descriptive term controls, no-script suppression, and responsive route-help contracts
PASS Apply recommendation separates plans, simulations, and unobserved state
PASS direct-open all-routes HTML has embedded runtime, one h1, unique IDs,
     named sections, and its documented repository-local image
```

The complete repository command remains
`qa/run_owner_review_checks.sh`; its final replay belongs to the evidence
commit that follows this implementation checkpoint.

## Current live-browser observations

These are computed DOM/layout observations from the local deterministic build,
not screenshots, reader tests, or accessibility certification.

### Home at 390×844

- `scrollWidth = innerWidth = 390`;
- Read, Explore, Apply, and More are visible;
- each principal route and More is 44 pixels high;
- the three doors are full-width and distinct;
- the Apply preview shows only the new planning sequence;
- no element extends beyond the document viewport.

### Apply at 320 / 390 / 480 / 600 pixels

- the route brief resolves to one column at every width;
- each of its three entries occupies the full available width;
- all five planning fieldsets are present;
- visible route controls have a minimum computed height of 44 pixels;
- all three principal route names remain visible;
- document scroll width exactly matches viewport width.

### Term help at 601 / 768 / 821 / 1024 / 1100 pixels

- every contextual trigger exposes a descriptive concept name;
- the panel computes to `position: static` and `width: 100%`;
- document scroll width exactly matches viewport width;
- the mobile guide is used at 601 and 768; the editorial rail is used from
  821 upward;
- visible route controls remain at least 44 pixels high.

### Default desktop Apply

The default plan remains `ordinary / ANSWER` with Stage 0 set to `none`.
Observed execution, stop, outcome, learning, and human-decision fields remain
unchanged. No provider or external request is made.

## P2 disposition and containment

- Duplicate Map live announcements: **corrected** by retaining one live region.
- No-script 0% reading progress: **corrected** by hiding the optional widget
  until enhancement initializes.
- Round 1 “repeatability” wording: **corrected transparently here**; historical
  evidence remains intact.
- Legacy overridden Map CSS: **deferred**. It does not target the current
  line-free markup, and deleting an older visual system is unnecessary scope
  for this P1 correction. The current layout contracts remain binding.
- Standalone portability wording: **corrected** to direct-open within the
  repository package.

## Claims and authority recheck

- The broad headline remains the owner-approved conceptual proposition; no
  prevalence or causality result was added.
- All six families remain visible and origin accounting remains subordinate.
- Peripheral material remains a candidate, not truth.
- Provenance remains separate from correctness; recurrence remains separate
  from independent support.
- Apply recommends; it does not run, observe, stop, learn, or decide for a
  person.
- Echo remains separate, unrun, and without results.
- Signal Foundry remains an illustration, not validation.
- No merge, deployment, publication, Release, study, provider selection,
  spend, external dataset acquisition, preregistration, or outreach occurred.

## Manual and owner-only residuals

Automated or model review cannot close these gates:

1. physical end-to-end keyboard traversal;
2. supported VoiceOver or NVDA review;
3. real 200% browser/OS zoom;
4. real forced-colors inspection;
5. browser print preview;
6. hardware-touch inspection;
7. owner judgment of voice, pacing, public name, late visual density, and
   whether the publication feels personally memorable enough;
8. publication-time external-link, metadata, and package-path checks, only if
   publication is later separately authorized.

No result beyond the stated source, executable, and live-layout evidence is
inferred.

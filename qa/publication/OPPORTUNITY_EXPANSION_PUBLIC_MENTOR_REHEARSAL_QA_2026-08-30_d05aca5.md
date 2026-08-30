# Public / mentor / visual opportunity-expansion QA

Status: **LOCAL FEATURE-BRANCH EVIDENCE — UNPUBLISHED, UNSENT, UNDEPLOYED**

This report audits the public/mentor gap from the exact lane baseline and records
the smallest additions that earned a place. It is implementation and review
evidence, not a reader study, mentor response, publication result, social
response, or effectiveness result.

## Review identity and scope

| Item | Value |
| --- | --- |
| Worktree | `/Users/gpt/Documents/Codex/worktrees/pattern-map-v16-loop-public` |
| Branch | `codex/pattern-map-v16-loop-public` |
| Exact starting baseline | `d05aca58910b4463e5afb69b10558b662a446278` |
| Owner-intent checkpoint | `docs/OWNER_INTENT_V16.md` — SHA-256 verification passed before edits |
| Exclusive lane | `publication/**`; `site/**`; `assets/diagrams/publication/**`; `assets/generated-candidates/**`; `assets/IMAGE_USE_LEDGER.md`; `qa/publication/**`; `qa/site/**`; `qa/visual/**` |
| External actions | None: no post, mentor outreach, publication, deployment, merge, Release, study, provider/model call, dataset acquisition, or spend |

Only the assigned paths were changed. The locked owner intent, six-family
identity, human-first opening, permanent Echo separation, no-results boundary,
and unresolved publication metadata remain intact.

## Exact baseline audit

The baseline was a clean checkout on the named branch. The current site already
had a shared-source `review | public` adapter, ten route IDs, a prose-first
public Read route, a deterministic code-native Home teaching reveal, a current
six-family Map, a planning-only Apply route, a semantic public standalone, a
secondary visual PDF, and a fail-closed `LOCAL_PREVIEW_UNSET` publication
configuration. Existing owner-review material already covered the substantive
review path, claims, source routes, Echo no-results status, and manual residuals.

That baseline made a new publication page, a second six-family map, a new social
image, and a generic adoption layer poor additions. The gap was narrower: the
owner had no compact, unsent way to facilitate a mentor conversation, rehearse
public copy, or inspect the human gates that would precede any later release.

The live public baseline also exposed one real composition issue. At 1280×720,
the three principal header links had a computed `gap` of only `4.8px`:

| Link | Baseline left–right (px) |
| --- | ---: |
| Read the idea | 829.945–938.242 |
| Explore the map | 943.039–1067.586 |
| Apply it | 1072.383–1144.227 |

At 390×844, the public header’s computed gap was `0px` and the link rectangles
met exactly, even though the document did not overflow. This was a public-mode
navigation clarity defect, not a thesis or route-architecture problem.

## Opportunity inventory and controlled dispositions

| ID | Opportunity considered | Disposition | Reason, removal test, and affected files |
| --- | --- | --- | --- |
| PUB-01 | One unpublished publication-rehearsal entry point | **Accepted with revision** | A small index earns its place because the existing owner packet is comprehensive but not a quick private/public rehearsal handoff. Removing the index leaves the three focused notes usable, but loses the safe order, source map, and unresolved-field warning. Built as `publication/README.md`; it composes canonical artifacts and adds no second content authority. |
| PUB-02 | Private mentor review sequence | **Accepted** | Existing packet guidance is a technical owner-review path, not a conversation-sized invitation with observation-versus-interpretation prompts. Removing this note loses the only compact sequence that starts with the human problem, delays the Map, tests proportionality, and ends with a challenge rather than sign-off. Built as `publication/MENTOR_REVIEW_SEQUENCE_V16.md`. It records no mentor contact or comprehension result. |
| PUB-03 | Unsent X/public copy variants | **Accepted with revision** | A few short variants reduce future copy-compression friction while keeping the broad thesis, all-six-family breadth, human authority, and no-results boundary. Removing them has no effect on the site but removes the only platform-facing rehearsal. Built as `publication/X_COPY_VARIANTS_V16.md`; variants omit links, handles, byline, image, and call to action, and are not posted. |
| PUB-04 | Human release-decision checklist | **Accepted with revision** | The site’s machine gate and acceptance matrix exist, but no compact human decision surface joined identity, source/link recheck, manual accessibility, claims, and action boundaries. Removing it leaves machine checks but makes the later owner decision easier to misread as a build command. Built as `publication/RELEASE_DECISION_CHECKLIST_V16.md`; every field is unresolved and the current choice is `HOLD / NOT AUTHORIZED`. |
| PUB-05 | Add a dedicated “Publication” route or release machinery to the public site | **Rejected** | It would put release mechanics in the reader’s path, duplicate the existing ten-route surface, and conflict with the first-screen human-problem rule. Removal changes nothing substantive because the current public adapter already teaches the idea and separates review chrome. No site route was added. |
| PUB-06 | Add a one-page/share visual candidate | **Rejected** | The current Home reveal, Map, public standalone, and print-aware code-native treatments already provide the needed visual explanation and text equivalents. Conceptual removal leaves the public candidate equally teachable; a new visual would duplicate the six-family movement and create another export/alt-text/provenance burden. No file was created under `assets/diagrams/publication/`. |
| PUB-07 | Generate a bitmap/social card | **Rejected for current need; social-image decision Deferred** | `qa/visual/VISUAL_NEEDS.md` still finds no bitmap need: semantic HTML/CSS and the preserved historical v13 image cover teaching needs. The local preview has no authorized destination, and identity, canonical URL, social image, and alternative text remain unset. No ImageGen call or candidate was made; `assets/IMAGE_USE_LEDGER.md` remains at zero generated candidates. A later owner-authorized publication may separately decide whether a social image is needed. |
| PUB-08 | Increase public header separation | **Accepted with revision** | The live baseline reproduced a real 4.8px/0px public-only spacing defect. A public-only CSS rule raises the wide gap to `9.6px` and preserves a fit-safe `2.88px` mobile gap; review-mode density remains unchanged. The removal test is direct: reverting the rule restores the concatenation. Built in `site/src/site.css`, regenerated in both standalone exports, and guarded by `qa/site/public-nav-spacing-contract.spec.mjs`. |
| PUB-09 | Generic adoption/conformance artifact for future projects | **Deferred** | Existing D-031/D-042 decisions defer this until Signal Foundry and a materially different second project expose repeated transfer friction. It is outside this public/mentor lane and would add framework bureaucracy before the evidence exists. No file was added. |

The resulting kit is four small files—an index plus three focused notes—not a
new canonical publication. Each note passes the removal test for a distinct
friction; the site remains useful without all four and the core content remains
in its canonical manuscript/framework/site paths.

## Built artifacts

### Unpublished rehearsal kit

- [`publication/README.md`](../../publication/README.md) — safe entry point,
  canonical source map, unresolved identity fields, and evidence boundary.
- [`publication/MENTOR_REVIEW_SEQUENCE_V16.md`](../../publication/MENTOR_REVIEW_SEQUENCE_V16.md)
  — six-pass private sequence, observation sheet, stop conditions, and no-result
  boundary.
- [`publication/X_COPY_VARIANTS_V16.md`](../../publication/X_COPY_VARIANTS_V16.md)
  — three short variants plus a four-post thread rehearsal. Local copy sizes
  are 279, 269, and 277 characters; every thread post is under 240 characters.
  These are unsent drafts, not posts or social evidence.
- [`publication/RELEASE_DECISION_CHECKLIST_V16.md`](../../publication/RELEASE_DECISION_CHECKLIST_V16.md)
  — fail-closed owner identity, content, provenance/link, accessibility, claim,
  and action gates. It does not edit `site/publication.config.json` or authorize
  a release.

### Site correction and focused contracts

- [`site/src/site.css`](../../site/src/site.css) — public-mode-only header gaps:
  `0.6rem` at wide widths and `0.18rem` at the narrow breakpoint.
- [`site/package.json`](../../site/package.json) — runs the new navigation
  regression as part of `npm run check`.
- [`qa/site/public-nav-spacing-contract.spec.mjs`](../../qa/site/public-nav-spacing-contract.spec.mjs)
  — checks public-only declarations, review-mode non-inheritance, generated
  route markers, and all three principal links.
- [`qa/publication/publication-kit-contract.spec.mjs`](publication-kit-contract.spec.mjs)
  — checks required artifacts, source links, unresolved fields, exact local copy
  sizes, no invented URL/handle, null release configuration, and zero bitmap
  candidates.
- [`site/exports/standalone/pattern-map-v16-public.html`](../../site/exports/standalone/pattern-map-v16-public.html)
  and [`site/exports/standalone/pattern-map-v16.html`](../../site/exports/standalone/pattern-map-v16.html)
  — regenerated local exports after the CSS correction; no publication metadata
  was added.

No file under `assets/generated-candidates/` was added. The existing
`assets/IMAGE_USE_LEDGER.md` remains unchanged because no generated candidate
or derivative exists to ledger.

## Claims and boundary audit

- The rehearsal kit describes a human-governed design proposal and testable
  agenda. It does not claim novelty, validation, effectiveness, prevalence,
  reader comprehension, mentor agreement, or social response.
- The six families remain the public map. The mentor sequence and X variants
  explicitly keep peripheral material as a candidate, recurrence distinct from
  independent support, and human authority separate from technical access.
- The Echo Problem remains a separate unrun project with no results. Common
  origin is a bounded example, not the definition of v16.
- Apply remains planning-only. The kit never treats a recommendation as a run,
  stop event, outcome, learning review, or human disposition.
- `site/publication.config.json` remains `LOCAL_PREVIEW_UNSET` with null
  `author_name`, `author_handle`, `canonical_url`, `social_image_url`, and
  `social_image_alt`. No final byline, canonical URL, handle, publication
  destination, or social metadata was selected.
- The public preview remains `noindex,nofollow`; no public release build was
  attempted with real metadata.
- The preserved v13 diagram remains historical and is not redrawn as current
  topology. No new bitmap was necessary.

## Browser, responsive, source, and print evidence

The local public preview was served from the feature worktree with
`SITE_PORT=47893 npm run dev:public` and inspected through the Codex in-app
Browser. The live screenshots were captured at the named viewports during the
pass; no screenshot was added as a new visual candidate because the image-need
gate remains closed.

### Header geometry after the correction

| Mode / viewport | Computed gap | Item rectangles (left–right, px) | Document width | Result |
| --- | ---: | --- | ---: | --- |
| Public, 1280×720 | `9.6px` | Read `815.555–923.852`; Explore `933.445–1057.992`; Apply `1067.586–1139.430`; More `1149.023–1216.000` | 1280 | Links visibly separated; no overflow |
| Public, 390×844 | `2.88px` | Read `10.000–118.297`; Explore `121.172–245.719`; Apply `248.594–320.438`; More `323.313–379.742` | 390 | One row; links separated; no overflow |
| Review, 1280×720 | `4.8px` | Read `829.945–938.242`; Explore `943.039–1067.586`; Apply `1072.383–1144.227` | 1280 | Review density unchanged |

The public 390px capture retained the stacked wordmark/header, one-row
principal controls, human-first headline, and first door without horizontal
overflow. At 1280px the corrected header remains compact while each route has a
clear visual gap.

### Public source state

Browser DOM/source inspection after the correction reported:

```text
data-presentation-mode = public
data-publication-status = LOCAL_PREVIEW_UNSET
robots = noindex,nofollow
canonical = null
author = null
main h1 count = 1
principal links = Read the idea | Explore the map | Apply it
```

The direct-open standalone was source-checked from the generated file and by
the existing site/check contracts. A direct `file://` browser navigation was
blocked by the browser’s local-file policy; no workaround or alternate browser
surface was attempted. This does not affect the repository source/build checks.

### Print proxy

At public 1280px, print-media emulation reported `matchMedia("print") = true`,
document width 1280px, the site header hidden, the interactive reveal summary
hidden, and the reveal ledger displayed as a grid. Native OS print preview is
still a manual owner gate; this proxy does not claim physical print or PDF
accessibility.

## Checks run and results

| Command | Result |
| --- | --- |
| `(cd docs && shasum -a 256 -c OWNER_INTENT_V16.sha256)` | **PASS** — `OWNER_INTENT_V16.md: OK` before implementation |
| `npm run build` from `site/` | **PASS** — 10 review routes, review standalone, 10 public routes, and public standalone rebuilt |
| `node qa/publication/publication-kit-contract.spec.mjs` | **PASS** — kit files, links, fields, copy sizes, and no-bitmap gate |
| `node qa/site/public-nav-spacing-contract.spec.mjs` | **PASS** — public-only wide/narrow spacing contract and review non-inheritance |
| `npm run check` from `site/` | **PASS** — all existing site/interaction/content checks plus the new nav contract |
| `python3 qa/visual/verify_image_formats.py` | **PASS** — current image extensions match byte signatures; 40 immutable archive mismatches retained by policy |
| `node qa/publication/publication-kit-contract.spec.mjs` | **PASS** — rerun after the final build |
| `git diff --check` | **PASS** |
| `(cd docs && shasum -a 256 -c OWNER_INTENT_V16.sha256)` after edits | **PASS** — `OWNER_INTENT_V16.md: OK` |

The final handoff records the full commit hash after the final checks and scoped
commit. No generated `site/dist/`,
`site/public-dist/`, cache, dependency, or other prohibited build directory is
included in the commit.

## Residual owner/manual gates

The following remain intentionally open and are not closed by this lane:

- owner/mentor judgment about voice, comprehension, taste, and whether the
  invitation feels like a continuation of the coffee conversation;
- physical keyboard traversal, supported screen-reader review, real 200% zoom
  and reflow, real forced-colors inspection, native browser print preview, and
  hardware-touch behavior;
- publication-time verification of external links, dates, route paths, host
  reachability/authorization, analytics/cookies if any, and final artifact
  selection;
- explicit owner choices for final byline, canonical URL, author handle,
  publication destination, social image/alternative text, and release action;
- any later downstream-repository authority or project-transfer decision; and
- all empirical, model-comparison, participant, live-product, and outcome
  questions, which remain unrun.

The stop condition for this lane is therefore satisfied at the artifact level:
the added surfaces have no reproduced P0/P1/P2 defect in their checked scope,
the existing site remains the primary review experience, and remaining work is
limited to owner/manual or separately authorized publication/research gates.

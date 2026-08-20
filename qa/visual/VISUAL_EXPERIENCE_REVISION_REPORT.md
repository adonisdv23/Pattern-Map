# Pattern Map v16 visual-experience revision

Status: **final local owner-review evidence captured from the polished source
tree; no deployment or publication**

Base: `4b5fc809e84a1d6c32c7565808821332421fa42e`

Final implementation/evidence checkpoint:
`a319794f5cf2d395c34e5af4935c9299f12dfd5c`

Branch: `codex/pattern-map-v16-site-polish`

Final evidence folder: `qa/visual/screenshots-final-v16-polish/`

Current-evidence index and stale-capture warning: [`README.md`](README.md)

Plan: [`POLISH_PLAN.md`](POLISH_PLAN.md)

This report records the material site-polish revision requested by the owner.
It compares the revised experience with the preserved v14/v15.2 qualities as
design references, not as content authority. It is visual/interaction QA, not
reader testing, comprehension evidence, effectiveness evidence, screen-reader
certification, or research evidence.

## Design rationale

The revision keeps the frozen v16 headline and standfirst, warm paper palette,
serif/mono/sans hierarchy, semantic route structure, ordinary-language family
bridges, progressive disclosures, historical labeling, and separate Echo
boundary. It changes the experience from a handsome documentation surface into
one authored publication with a visible reading rhythm:

- Home now opens with a human problem and three distinct teaching modes: a
  reading-ribbon preview, a current-map preview, and a route/receipt preview.
  The first mobile viewport reaches the first principal door without using a
  fixed-height hero.
- A wide-screen chapter rail keeps the current location, principal doors,
  secondary routes, and next-route cue visible. Narrow screens receive a
  normal-flow route-guide disclosure with `aria-current="location"` rather than
  a squeezed horizontal navigation.
- Explore's current relationship view is now the first visual teaching object.
  It has a visible six-family node row, code-native relationship structure,
  baseline-to-absence/memory logic, route/generation/human-authority framing,
  and a visibly looped F6 learning path. The text equivalent remains nearby and
  essential meaning is not dependent on JavaScript or color.
- Read has a cumulative route index, progress treatment, pull quote, section
  rhythm, complete canonical essay, and distinct optional mentor handoff.
- Apply is a bounded local decision surface: four route levels are informed by
  consequence, uncertainty, budget, and permission, then become a visible
  receipt with separate route, stop, learning, and human-disposition fields.
  HOLD, ESCALATE, and STOPPED_BUDGET are reversible local states; no provider,
  network, dataset, or external action is involved.
- Examples use three full-width teaching narratives rather than repeated card
  grammar: specialist/peripheral candidate -> weigh/challenge; velocity and
  expected absence -> explicit baseline; and nine recurring reports -> one
  common origin with `independence: UNKNOWN`. Signal Foundry remains
  `ILLUSTRATION ONLY / READ-ONLY / NOT VALIDATION`; Echo remains late, separate,
  unrun, and no-results.

The v14/v15.2 references influenced chapter rhythm, persistent orientation,
visual teaching objects, and layered reading. Their provenance-first opening,
thesis wording, provider/research posture, decorative bitmap language, and
Echo-centered framing were intentionally not restored.

## P0 mobile-capture diagnosis

The pre-existing file `qa/visual/screenshots/home-mobile-390x844.png` contains a
solid black lower region. It was not overwritten. A fresh 390x844 capture from
the exact starting build at `4b5fc809e84a1d6c32c7565808821332421fa42e` showed
paper paint through the viewport, `scrollWidth == 390`, and no clipped or
overflowing boundary. Pixel checks reinforce the diagnosis:

**The pre-existing image is retained as stale QA history and must not be used
to judge the current site.** The active mobile review image is
[`screenshots-final-v16-polish/home-390x844.png`](screenshots-final-v16-polish/home-390x844.png).

| Capture | Bottom-center sample | Near-black centerline rows |
| --- | --- | ---: |
| Stale pre-existing screenshot | `(0, 0, 0)` | 141 |
| Fresh exact-base baseline | `(234, 234, 224)` | 17 |
| Fresh final polished capture | `(246, 245, 240)` | 17 |

The small number of near-black rows in the fresh captures is text/border detail,
not a contiguous black lower region. The body background and document metrics
were normal in the fresh browser render. Root cause is therefore classified as
a stale/incomplete screenshot capture artifact, not a site CSS, document-height,
overflow, or paint defect. The final capture was regenerated from the polished
build and visually inspected at both 390x844 and 360x800; neither has the black
region.

## Route-by-route visual evidence

All files below are fresh viewport captures after the final site build. The
desktop route set covers every route; the core viewport set covers Home, Map,
and Apply at every required viewport, with Read and Examples also captured on
390x844.

| Route | Desktop evidence | Mobile evidence | Teaching/QA focus |
| --- | --- | --- | --- |
| Home / Start here | [`home-1440x900.png`](screenshots-final-v16-polish/home-1440x900.png) | [`home-390x844.png`](screenshots-final-v16-polish/home-390x844.png), [`home-360x800.png`](screenshots-final-v16-polish/home-360x800.png) | Exact human-problem opening, three distinct doors, first-door pacing, no black capture region |
| Read the idea | [`read-1440x900.png`](screenshots-final-v16-polish/read-1440x900.png) | [`read-390x844.png`](screenshots-final-v16-polish/read-390x844.png) | Index/progress, pull quote, cumulative and complete reading layers |
| Explore the map | [`map-1440x900.png`](screenshots-final-v16-polish/map-1440x900.png) | [`map-390x844.png`](screenshots-final-v16-polish/map-390x844.png), [`map-360x800.png`](screenshots-final-v16-polish/map-360x800.png) | Current relationship view before family index; F1-F6 visual order; text-equivalent adjacency |
| Apply it | [`apply-1440x900.png`](screenshots-final-v16-polish/apply-1440x900.png) | [`apply-390x844.png`](screenshots-final-v16-polish/apply-390x844.png), [`apply-360x800.png`](screenshots-final-v16-polish/apply-360x800.png) | Route brief, proportionate choice surface, local receipt/stop path |
| Examples | [`examples-1440x900.png`](screenshots-final-v16-polish/examples-1440x900.png) | [`examples-390x844.png`](screenshots-final-v16-polish/examples-390x844.png) | Case/narrative mode and three required teaching patterns |
| Boundaries | [`boundaries-1440x900.png`](screenshots-final-v16-polish/boundaries-1440x900.png) | Core mobile layout checked at 390x844 and 360x800 | Claim and authority limits remain late and attached |
| Sources | [`sources-1440x900.png`](screenshots-final-v16-polish/sources-1440x900.png) | Core mobile layout checked at 390x844 and 360x800 | Targeted, not exhaustive; no newly reverified-source implication |
| Research | [`research-1440x900.png`](screenshots-final-v16-polish/research-1440x900.png) | Core mobile layout checked at 390x844 and 360x800 | `UNRUN · NO RESULTS · NO PROVIDER OR MODEL SELECTED` remains subordinate |
| History | [`history-1440x900.png`](screenshots-final-v16-polish/history-1440x900.png) | Core mobile layout checked at 390x844 and 360x800 | Historical v13 lineage stays separate from current topology |

### Core viewport matrix

| Viewport | Home | Map | Apply | Scroll width equals viewport |
| --- | --- | --- | --- | --- |
| 1440x900 | [`home-1440x900.png`](screenshots-final-v16-polish/home-1440x900.png) | [`map-1440x900.png`](screenshots-final-v16-polish/map-1440x900.png) | [`apply-1440x900.png`](screenshots-final-v16-polish/apply-1440x900.png) | yes |
| 1280x720 | [`home-1280x720.png`](screenshots-final-v16-polish/home-1280x720.png) | [`map-1280x720.png`](screenshots-final-v16-polish/map-1280x720.png) | [`apply-1280x720.png`](screenshots-final-v16-polish/apply-1280x720.png) | yes |
| 1024x768 | [`home-1024x768.png`](screenshots-final-v16-polish/home-1024x768.png) | [`map-1024x768.png`](screenshots-final-v16-polish/map-1024x768.png) | [`apply-1024x768.png`](screenshots-final-v16-polish/apply-1024x768.png) | yes |
| 768x1024 | [`home-768x1024.png`](screenshots-final-v16-polish/home-768x1024.png) | [`map-768x1024.png`](screenshots-final-v16-polish/map-768x1024.png) | [`apply-768x1024.png`](screenshots-final-v16-polish/apply-768x1024.png) | yes |
| 390x844 | [`home-390x844.png`](screenshots-final-v16-polish/home-390x844.png) | [`map-390x844.png`](screenshots-final-v16-polish/map-390x844.png) | [`apply-390x844.png`](screenshots-final-v16-polish/apply-390x844.png) | yes |
| 360x800 | [`home-360x800.png`](screenshots-final-v16-polish/home-360x800.png) | [`map-360x800.png`](screenshots-final-v16-polish/map-360x800.png) | [`apply-360x800.png`](screenshots-final-v16-polish/apply-360x800.png) | yes |

At 200%-friendly widths, fixed-height hero treatment is absent; the static
audit and 768px reflow check found no horizontal overflow. The in-app Browser
does not expose a reliable OS-level zoom simulation in this task, so this is
reported as a reflow-oriented implementation check, not a claim of actual
200%-zoom certification.

## Interaction evidence

Visible state captures:

- [`map-f1-focused-1280x720.jpg`](screenshots-final-v16-polish/interaction-states/map-f1-focused-1280x720.jpg)
  — F1 focused while all six families remain available;
- [`apply-advanced-hold-1280x720.jpg`](screenshots-final-v16-polish/interaction-states/apply-advanced-hold-1280x720.jpg)
  — advanced route with a recorded human HOLD and separate route/stop/learning/
  authority fields; and
- [`standalone-all-routes-1280x720.jpg`](screenshots-final-v16-polish/interaction-states/standalone-all-routes-1280x720.jpg)
  — corrected standalone orientation with one `All routes` publication rail.

- F1 family focus updated the current map state, `aria-pressed`, live status,
  text panel, and focused family card without dimming other content below usable
  contrast. Show all restored the full comparison state.
- The visible text equivalent contains all six questions in exact F1-F6 order,
  plus the baseline dependency for absence + memory, the `UNKNOWN` recurrence
  boundary, and the F6 learning loop.
- The local Apply receipt accepted a consequential/high/substantial/human-gate
  combination as `ADVANCED`, showed `CLARIFY`, `STOPPED_DEADLINE`,
  `LEARNING_PLANNED`, and `HUMAN_DISPOSITION_REQUIRED`, then recorded each
  reversible HOLD, ESCALATE, and STOPPED_BUDGET state and reset to ordinary.
- More opened into secondary links and closed on Escape with focus returned.
  The mobile route guide opened in normal flow and closed on Escape with focus
  returned to its summary.
- Read progress moved from 0% to 12% after a supported PageDown scroll and
  updated the active reading link.
- Native button semantics were preserved. Pointer activation was tested through
  repeated focus/clear/focus transitions with no duplicate toggle. The browser
  adapter moved focus for synthetic Enter/Space on the custom map buttons but
  did not dispatch their click path; no production fallback was added because
  it could double-activate in a conforming browser. Sequential synthetic Tab
  also did not advance in the adapter. These remain manual residuals, not
  passing keyboard-traversal claims.

## PDF visual companion

The regenerated PDF is under `site/exports/pattern-map-v16-owner-review.pdf`.
Rendered inspection pages are under
`qa/visual/pdf-renders-final-v16-polish/`:

- [`page-1.png`](pdf-renders-final-v16-polish/page-1.png) — frozen opening and
  three doors
- [`page-2.png`](pdf-renders-final-v16-polish/page-2.png) — Read route and
  boundaries
- [`page-3.png`](pdf-renders-final-v16-polish/page-3.png) — F1-F6 map summary
- [`page-4.png`](pdf-renders-final-v16-polish/page-4.png) — bounded examples,
  Signal Foundry, and Echo separation
- [`page-5.png`](pdf-renders-final-v16-polish/page-5.png) — Apply levels and
  operator path
- [`page-6.png`](pdf-renders-final-v16-polish/page-6.png) — history, QA limits,
  and local handoff

All six pages were rendered at 144 DPI and inspected for clipping, overlap,
black-square artifacts, and unreadable glyphs. The PDF is intentionally a
secondary, untagged visual companion; the semantic standalone HTML is primary.

## Residuals and boundary statement

- No static or browser QA here establishes reader comprehension, persuasion,
  behavioral effectiveness, model quality, screen-reader certification, or
  empirical research results.
- The in-app Browser adapter did not provide reliable sequential-Tab or custom
  map-button Enter/Space activation evidence; manual physical-keyboard and
  assistive-technology review remain owner follow-up if desired.
- Forced-colors, reduced-motion, print, and 200%-friendly behavior were
  verified through static hooks and reflow-oriented checks; no OS-level forced
  colors or real assistive technology session was claimed.
- Claude Code/Cowork review was unavailable because the existing OAuth token was
  revoked. Credentials were not inspected or repaired, no paid API was used,
  and no claim that Claude reviewed this revision is made.
- No deployment, hosting call, public URL, publication, Release, merge to main,
  study/provider/model/participant run, dataset acquisition, preregistration,
  outreach, or spend occurred.

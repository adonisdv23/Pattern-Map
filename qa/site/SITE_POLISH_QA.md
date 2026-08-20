# Pattern Map v16 site-polish QA

Status: **local owner-review build complete; no deployment performed**

This record covers the material visual and interaction revision from
`4b5fc809e84a1d6c32c7565808821332421fa42e` on branch
`codex/pattern-map-v16-site-polish`. It is implementation and artifact evidence;
it is not reader-comprehension, persuasion, effectiveness, screen-reader
certification, model-quality, or empirical evidence.

Final implementation/evidence checkpoint:
`a319794f5cf2d395c34e5af4935c9299f12dfd5c`. The first site-polish delivery was
`5a37aacccd26d407acf65cea9b33393899514851`; the final checkpoint adds exact
interaction-state captures and corrects the standalone export to one `All
routes` orientation system instead of nested route frames or a false Home
current state.

## Scope and ownership

- Site implementation, standalone export, PDF companion, screenshots, and QA
  evidence stay within the assigned `site/**`, `qa/site/**`, and `qa/visual/**`
  paths.
- No manuscript, framework, case, research, archive, canonical contract, root
  guidance, or integrator-owned image-ledger source was edited.
- The code-native visual-needs reassessment remains closed to generated bitmap
  imagery. No ImageGen call, bitmap candidate, social card, or public-sharing
  target was created.

## Automated checks

The following checks were rerun after the final CSS and keyboard-handler pass:

```text
cd site && npm run build
PASS: built 9 routes and refreshed site/exports/standalone/pattern-map-v16.html

cd site && npm run check
PASS: route/link checks, frozen first-screen framing, exact F1-F6 order,
      boundaries, standalone fragments, semantic landmarks/headings/names,
      no-script essentials, Apply vocabulary, reduced-motion/forced-colors/
      200%-friendly/print hooks, Echo removal, and historical/current labels

python3 qa/site/audit_site.py
PASS: structural site audit, 9 route landmarks/headings/names, no-script,
      Apply vocabulary, standalone integrity, and boundary checks

python3 qa/editorial/validate_content_interface.py
PASS: immutable owner-intent checkpoint, content-interface JSON, door and
      secondary-route manifests, F1-F6 invariants, first-screen framing,
      examples, late Echo placement, and claim/output obligations

git diff --check
PASS: no whitespace errors
```

The locked owner-intent checksum was verified before implementation and is
required again immediately before handoff:

```text
(cd docs && shasum -a 256 -c OWNER_INTENT_V16.sha256)
OWNER_INTENT_V16.md: OK
```

## Browser and interaction evidence

Rendered QA used the local-only server at `http://127.0.0.1:4173/` and the
in-app Browser. No credentials, cookies, browser storage, hosting API, or
production URL were accessed.

- Home: the exact frozen headline and standfirst lead; a clear first Read door
  appears at the bottom edge of both 390x844 and 360x800 captures. Read, Map,
  and Apply use distinct reading-ribbon, relationship-map, and route/receipt
  previews.
- Wide orientation: a sticky chapter rail exposes the current route,
  `aria-current="location"`, all principal doors, secondary routes, and the
  next-route cue. It follows normal DOM order and uses anchor scroll margins.
- Narrow orientation: the rail becomes a normal-flow `<details>` route guide;
  it does not become a horizontal keyboard or touch trap. Opening it and
  pressing Escape closes it and returns focus to its summary.
- Map: pointer focus on F1 updates `aria-pressed`, the relationship-stage
  state, the visible question/input/comparison/record/boundary/connection
  panel, and the live status while keeping every family reachable. Show all
  resets the state. The open text-equivalent disclosure contains all six
  families and the baseline/absence/UNKNOWN/learning-loop boundary text.
- Map keyboard: family inspection controls remain native `<button>` elements,
  so conforming browsers retain their built-in Enter/Space activation semantics.
  Pointer activation was exercised repeatedly (F1 focused, cleared, focused)
  with no duplicate toggle. In this in-app Browser adapter, synthetic
  `press("Enter")` and `press("Space")` moved focus but did not dispatch the
  custom-button click path; no adapter-only keydown fallback was added because
  it could double-activate in a conforming browser.
- Read: the reading progress bar updates on scroll; the active reading index
  moves to the section in view. The cumulative 60-90-second route, complete
  essay, and distinct optional mentor handoff remain separate.
- Apply: the local provider-free form maps consequence, uncertainty, budget,
  and permission to ordinary/lightweight/moderate/advanced. A consequential,
  high-uncertainty, substantial-budget, human-gate selection produced an
  `ADVANCED` receipt with separate route, stop, learning, and human-disposition
  fields. `HOLD for human`, `ESCALATE`, and `STOPPED_BUDGET` each produced a
  visible reversible status; Reset returned to `ORDINARY`. Submit also worked
  through keyboard activation.
- Exact visible-state evidence is preserved under
  `qa/visual/screenshots-final-v16-polish/interaction-states/`: focused F1,
  advanced/HOLD, and standalone `All routes` states. The captures supplement
  the DOM/status record; they do not replace the manual keyboard gate.
- Disclosure and menu controls: the Map text-equivalent summary activated with
  Enter; the More menu opened, moved focus into its links, and closed on Escape
  with focus returned to More.
- Sequential Tab limitation: the in-app Browser adapter's synthetic
  `body.press("Tab")` did not advance focus in this session. This is recorded
  as a manual residual, not presented as a passing physical-keyboard or
  screen-reader traversal certification. The site uses semantic links,
  native buttons, summaries, fieldsets, visible focus styles, and predictable
  DOM order.

## Responsive and non-script checks

Final captures and DOM measurements cover all required viewport sizes:

| Viewport | Home | Read | Map | Apply | Horizontal overflow |
| --- | --- | --- | --- | --- | --- |
| 1440x900 | yes | yes | yes | yes | none |
| 1280x720 | yes | yes | yes | yes | none |
| 1024x768 | yes | yes | yes | yes | none |
| 768x1024 | yes | yes | yes | yes | none |
| 390x844 | yes | yes | yes | yes | none |
| 360x800 | yes | yes | yes | yes | none |

The static checker confirms one `main` and one `h1` per route, no-script
essential meaning, unique standalone IDs, and print/reduced-motion/
forced-colors/200%-friendly hooks. A real assistive-technology audit and a
reader study were not authorized and were not claimed.

The older `qa/visual/screenshots/home-mobile-390x844.png` is retained as a
stale pre-polish QA artifact and is not current evidence. The warning and
replacement path are explicit in `qa/visual/README.md`.

## Standalone export

The committed export is under the owned, non-ignored path:

`site/exports/standalone/pattern-map-v16.html`

The in-app Browser blocks direct `file://` navigation by policy, so the export
was served only through a loopback static server at
`http://127.0.0.1:4174/pattern-map-v16.html`. The final served audit found one
`main`, one `h1`, 292 unique IDs, one publication rail, one mobile route guide,
one page frame, one inline script, one inline stylesheet, the three principal
doors, and local fragment links. The orientation says `All routes` and does not
falsely mark one section as the current route. No workaround around the
`file://` policy was attempted.

## PDF companion

The owner-review PDF was regenerated with the bundled PDF runtime, reopened
with `pdfinfo`, and rendered with Poppler at 144 DPI. It is six letter-size
pages, unencrypted, with no form fields or JavaScript. All six rendered pages
were inspected for clipping, overlap, black-square artifacts, and unreadable
glyphs. It is a secondary visual review companion; the interactive site and
standalone HTML remain the primary deliverables.

## External-action boundary

No Sites hosting or deployment API, production URL, publication, GitHub
Release, merge to `main`, PR opening, model/provider/participant run, study,
dataset acquisition, preregistration, outreach, spend, credential repair, or
Claude/Cowork review occurred. Claude Code/Cowork review was unavailable
because the existing OAuth token was revoked; credentials were not inspected
or repaired, and no claim that Claude reviewed this revision is made.

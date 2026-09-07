# Site visual-experience post-polish acceptance review

Review date: 2026-08-19

Initial review target: `5a37aacccd26d407acf65cea9b33393899514851`

Disposition checkpoint: `a319794f5cf2d395c34e5af4935c9299f12dfd5c`

Scope: bounded visual, interaction, source, and artifact review; no human study,
screen-reader certification, physical-keyboard certification, provider call,
deployment, or publication.

## Verdict

**PASS FOR OWNER REVIEW WITH MANUAL RESIDUALS.**

The initial exact-commit review returned **PASS WITH REVISIONS**. The site had
already cleared the substantive owner requirement: it was no longer a text or
PDF shell. The follow-up checkpoint resolves the remaining artifact-level
orientation and evidence issues. Owner taste and manual accessibility/print
gates remain deliberately open.

The polished site now has:

- a persistent desktop publication rail and a normal-flow mobile route guide;
- a current six-family relationship object at the start of Map;
- a provider-free local Apply studio with route, stop, learning, and authority
  receipts plus reversible HOLD, ESCALATE, and STOPPED_BUDGET states;
- a Read route with layered entry, index, progress treatment, pull quote, and
  full essay;
- full-width teaching narratives on Examples; and
- a PDF that is explicitly secondary to the interactive routed site and the
  semantic standalone HTML.

## Prior P0/P1 findings

| Finding | Final disposition | Evidence / boundary |
| --- | --- | --- |
| P0 — old mobile capture has a black lower region | **Resolved; stale artifact retained and labeled** | Fresh final Home captures are fully painted. `qa/visual/README.md` names the older image as stale QA history and points to the current 390x844 capture. |
| P1 — missing persistent route orientation | **Resolved** | Routed pages have a current-route rail and mobile guide. The standalone follow-up removes nested per-route frames, exposes one `All routes` rail and one mobile guide, and does not falsely mark Home current. |
| P1 — Map did not teach topology early | **Resolved** | Map opens with the relationship view, exact F1–F6 order/questions, baseline dependency, supporting records, human authority, F6 loop, focus state, and visible text equivalent. |
| P1 — Apply was descriptive rather than interactive | **Resolved** | The local studio builds ordinary/lightweight/moderate/advanced receipts and separates route, stop, learning, and authority. The final evidence set includes a visible advanced/HOLD state. |
| P1 — document-like pacing and weak route beats | **Resolved for implementation; owner taste remains** | Home, Read, Map, Apply, and Examples now use different teaching modes. Whether the Examples first viewport should expose more of its first visual is an owner pacing choice, not a failed implementation gate. |
| P1 — site felt like a PDF/document handoff | **Resolved** | The routed site is the primary interactive artifact. Standalone HTML is the semantic all-routes companion; the untagged PDF remains clearly secondary. |

## Exact follow-up evidence

- `qa/visual/screenshots-final-v16-polish/interaction-states/map-f1-focused-1280x720.jpg`
  shows the focused F1 relationship state while every family remains visible.
- `qa/visual/screenshots-final-v16-polish/interaction-states/apply-advanced-hold-1280x720.jpg`
  shows an advanced route with `HOLD`, `STOPPED_OTHER`, `LEARNING_PLANNED`, and
  `HUMAN_DISPOSITION_REQUIRED` as separate visible fields.
- `qa/visual/screenshots-final-v16-polish/interaction-states/standalone-all-routes-1280x720.jpg`
  shows the standalone export with one persistent `All routes` orientation
  system.
- The standalone export at the disposition checkpoint has one `main`, one
  `h1`, 292 unique IDs, one publication rail, one mobile route guide, one page
  frame, and no false `aria-current="location"` state.

## Checks rerun

- `cd site && npm run build` — PASS.
- `cd site && npm run check` — PASS.
- `python3 qa/site/audit_site.py` — PASS.
- `python3 qa/editorial/validate_content_interface.py` — PASS.
- `python3 qa/applied/validate_framework.py` — PASS.
- owner-intent SHA-256 checkpoint — PASS.
- `git diff --check` — PASS.

These are source, structure, browser-state, and rendered-artifact checks. They
are not evidence that a reader understood the framework or that it improves
AI work.

## Manual owner residuals

- Physical-keyboard traversal through the skip link, navigation, route guide,
  Map controls, disclosures, Apply form/actions, and Escape/focus-return paths.
- A supported screen-reader pass over routed and standalone HTML.
- Real browser print-preview inspection.
- Real 200% browser/OS zoom inspection; existing evidence is reflow-oriented.
- Owner judgment of first-screen pacing, voice, name, and 60–90-second
  comprehension.

The browser adapter's synthetic Tab and custom-button Enter/Space behavior was
not reliable enough to close those manual gates. No adapter-only key handler
was added because native buttons already provide conforming activation and an
extra fallback could double-toggle.

Claude Code/Cowork did not review this checkpoint because its existing OAuth
token was revoked. Credentials were not inspected or repaired, no paid API was
used, and no Claude-review claim is made.

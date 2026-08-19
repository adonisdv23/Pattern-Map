# Cold-reader post-revision verification — Pattern Map v16

**Verdict: PASS WITH REVISIONS**

**Reviewed tree:** exact commit `2a54b24ec01707bb2a73032ab3f662cd995669ae`
(`2a54b24`), reviewed as an owner-review candidate on 2026-08-19.

**Reviewer role:** bounded proxy cold reader with no machine-learning,
software-architecture, or research-methodology expertise. This is a model
proxy review, not the owner's mentor, a public-reader sample, measured reader
comprehension, persuasion evidence, participant evidence, or research
evidence. “Reader” statements below describe inspection friction in this
review, not a population result.

The source revisions resolve the two substantive copy problems in the prior
review and repair the blank glossary fields. One committed reviewer-facing
Map screenshot was not regenerated: it still shows the old technical card
copy even though the current rendered route and standalone export show the
revised plain-language copy. That stale artifact keeps the package at
**PASS WITH REVISIONS** until it is refreshed or explicitly marked as a
historical capture.

No external browsing, provider, model, study, participant activity, canonical
file edit, deployment, publication, or push was used. The only file written by
this review is this report.

## Scope and evidence read

I read the repository instructions and the required v16 governing contracts
in order, including the owner-intent, thesis/audience, artifact-boundary,
source-lineage, acceptance-criteria, decision-log, and review/disposition
documents. I also verified the locked owner-intent checkpoint:

```text
OWNER_INTENT_V16.md: OK
```

The exact-commit material reviewed was:

- `manuscript/NINETY_SECOND_VERSION.md`
- `manuscript/MENTOR_COVER_NOTE.md`
- `manuscript/PUBLIC_ABSTRACT.md`
- `manuscript/PATTERN_RECOGNITION_V16.md`
- `framework/GLOSSARY.md`
- `site/build.mjs`, `site/src/site.css`, and `site/src/site.js`
- the exact route-renderer logic from `site/build.mjs`, cross-checked against
  the committed standalone export; the shared checkout's generated route
  output was used only as supplementary implementation context
- `site/exports/standalone/pattern-map-v16.html`
- committed Home, mobile Home, and Map screenshots under
  `qa/visual/screenshots/`
- `site/exports/pattern-map-v16-owner-review.pdf`
- all six committed PDF renders under `qa/visual/pdf-renders/`

The following route checks passed on the available generated output in the
shared checkout. Because sibling work advanced that checkout during this
review, these command results are supplementary structural checks, not
standalone proof of an unpinned working-tree build's exact-commit identity.
The exact-commit content claims and visual findings below are pinned to
`git show 2a54b24:<path>` and the committed artifacts listed above:

```text
cd site && npm run check
PASS routes: 9
PASS exact first-screen framing, non-result boundary, and principal-door presence
PASS six-family order/names, implementation levels, teaching patterns
PASS Signal Foundry, Echo, and historical/current topology boundaries
PASS local route/assets link integrity
PASS exact underscore-bearing state vocabulary and standalone fragments
PASS responsive/no-script navigation and active-route semantics
PASS standalone export exists

python3 qa/site/audit_site.py
PASS semantic landmarks/headings/names for all 9 routes
PASS no-script essential meaning is present in static HTML
PASS standalone HTML is self-contained with one h1, unique IDs, and named route sections
NOTE structural QA is not reader comprehension or effectiveness evidence
```

These checks establish implementation and artifact invariants only. They do
not establish that a person understood, liked, trusted, or acted on the work.

## Gate readout

| Gate | Proxy verdict | Evidence-backed reading |
| --- | --- | --- |
| **A01 — broad idea in 90 seconds** | **PASS** | The revised short version starts with upstream causes, defines the Discrimination Layer as an inspectable/correctable responsibility, names all six families, says peripheral material is only a candidate, keeps human consequential authority explicit, and says the proposal is broader than origin counting. Remaining specialist terms are contextualized rather than blocking the short stop. |
| **A04 — thoughtful conversation, not committee document** | **PASS** | The coffee-conversation frame, direct invitation to challenge the center, and authored opening/close survive. The late essay still becomes more review-like in places, but that is an optional taste concern after the idea is clear, not an opening or thesis defect. |
| **A05 — approximately 10–15 minutes** | **PASS** | The exact short source is 303 raw words including its heading, and the full essay is 3,289 raw words. Those counts support the existing approximate 60–90-second entry and 10–15-minute essay framing; no timing was observed or measured here. |
| **A06 — progressive disclosure** | **PASS WITH REVISIONS** | The actual Home/Read/Map routes and standalone export now put plain-language meaning before technical detail, and the glossary no longer renders empty technical or boundary fields. The committed Map screenshot still exposes the old technical front copy, so the reviewer-facing evidence package is not fully in sync with the current renderer. |

## Verification of prior findings

### CNR-A01-01 — P1 — human authority and entry-point jargon

**Status: RESOLVED in the canonical short version and its current route
renderings.**

**Evidence:**

- `manuscript/NINETY_SECOND_VERSION.md:9–15` defines the responsibility and
  says the choices are visible enough to correct. The technical/social and
  architecture boundaries remain adjacent to the definition.
- `manuscript/NINETY_SECOND_VERSION.md:23–33` now says that peripheral material
  is a candidate for inspection, repeated reports are not automatically
  separate confirmation, knowing where something came from does not prove it
  correct, and “People still make the judgment and keep authority for
  consequential action.” The earlier “provenance,” “independent corroboration,”
  and “human disposition is not a fact” cluster is no longer required to carry
  the short version's human-authority boundary.
- The Home short entry in the committed standalone export repeats that exact
  sequence at `site/exports/standalone/pattern-map-v16.html:556–561`, and the
  Read route repeats it at `:587–592`. The route renderer reads the canonical
  short source for both surfaces (`site/build.mjs:483–500` and `:518–530`), so
  this is not a hand-maintained alternate summary.
- `manuscript/PUBLIC_ABSTRACT.md:18–23` independently states that human
  judgment and consequential authority remain essential.

**Gate:** A01 and A06.

**Cold-reader assessment:** The first stop now gives me the stronger answer to
“who is still responsible?” rather than merely pointing to a person who can
correct a route. “Velocity,” “baseline,” and “versioned memory” remain terms a
general reader may not use spontaneously, but the six-family sentence gives
their immediate action-oriented context and the full essay explains them. I do
not see a required entry-point jargon defect remaining.

**Recommendation:** No required corrective action for this finding. Preserve
the explicit human-authority sentence in future short-version rebuilds. An
owner may optionally simplify “consequential action” for an even more
conversational register, but that is taste, not a gate failure.

### CNR-A06-01 — P1 — visible Map cards used builder vocabulary too early

**Status: PARTIALLY RESOLVED at the package level.** The current renderer and
standalone export resolve the reader-facing defect; one committed screenshot
still shows the pre-revision defect.

**Evidence that the current route is fixed:**

- `site/build.mjs:337–362` introduces a separate `familyPublicCopy` object with
  ordinary-language purpose and mechanism text for all F1–F6 families.
- `site/build.mjs:442–454` renders that public copy first and places the source
  specification, technical mechanism, implementation levels, and “when not to
  use” material inside the expandable `Implementation detail` disclosure.
- The committed standalone Map route contains the revised front copy and
  keeps the technical language behind disclosure:
  `site/exports/standalone/pattern-map-v16.html:683–730`. Examples include:
  “Look beyond the obvious path, but treat what you find as something to
  inspect—not a shortcut to truth,” “Ask what each source can and cannot tell
  us about this exact claim,” and “Notice a change against a stated baseline
  before calling it meaningful.” The old “task-scoped information aperture”
  and “claim-scoped authority” phrases occur only in the expanded
  implementation details.
- The exact renderer logic and committed standalone export match on the six
  plain-language bridges. The available local `npm run check` also reported
  all six bridges, but that supplementary check is not used as the sole
  exact-commit evidence because the shared checkout advanced during review.

**Evidence of the remaining package defect:**

- The committed `qa/visual/screenshots/map-desktop-1440x1000.png` still shows
  the old visible F1/F2 purpose copy: “Widen a task-scoped information
  aperture...” and “Keep source role, claim-scoped authority...” in the first
  cards a reviewer sees.
- The screenshot blob is unchanged between `2a54b24^` and `2a54b24`, while
  `site/build.mjs` and `site/exports/standalone/pattern-map-v16.html` changed
  to the new public copy. The current visual QA report describes that image as
  the “current relationship view and F1/F2 opening composition,” so it cannot
  be treated as an intentionally historical capture without relabeling.

**Reader risk:** A reader opening the current route gets the improved bridge,
but an owner reviewing the committed Map screenshot is shown exactly the
committee-like language that the revision was meant to remove. This is a
review-package fidelity problem, not a remaining defect in the current Map
renderer.

**Gates:** A04 and A06.

**Recommendation:** **Required before a clean package-level pass:** regenerate
`qa/visual/screenshots/map-desktop-1440x1000.png` from commit `2a54b24` and
recheck that its visible F1/F2 cards match the standalone/current route. If
the old capture must be retained for comparison, move or label it as a
pre-revision artifact and add a current capture beside it. No source wording
change is needed for this finding.

### CNR-A06-02 — P2 — five optional glossary entries rendered empty fields

**Status: RESOLVED for the original blank-field defect, with one optional
plain-language quality residue noted below.**

**Evidence:**

- `framework/GLOSSARY.md:6–53` now has working-meaning and boundary rows for
  all seven terms promised by the Map route, including Typed relationship,
  Influence receipt, Cost-bounded route, Versioned memory, and Human
  disposition.
- `site/build.mjs:322–325` reads the canonical tables, and
  `:364–381` now fails the build if a promised term lacks a working meaning or
  boundary. It renders the plain translation first, followed by the technical
  meaning and boundary.
- The committed standalone export at
  `site/exports/standalone/pattern-map-v16.html:752–760` contains populated
  technical and boundary paragraphs for every promised term. There are no
  `<p></p>` technical fields and no empty `Boundary:` labels. `site/check.mjs`
  explicitly checks both conditions (`:107–108`), and the check passed.

**Gate:** A06 and site-to-source fidelity.

**Reader assessment:** Opening the optional glossary now gives a complete
technical explanation and a boundary instead of an unfinished-looking blank
row. The visible family questions and boundaries still make the Map useful
without opening the glossary, as required by the progressive-disclosure copy
at the standalone export's `:752–757`.

**Recommendation:** No required action for the prior CNR-A06-02 defect. The
optional residual is recorded separately as `CNR-GLOSSARY-OPT-01`: the
“Common origin” entry has the generic fallback plain translation “A bounded
record that keeps the route inspectable” at
`site/exports/standalone/pattern-map-v16.html:759`, rather than a plain
translation that says it is a shared upstream report, event, release, dataset,
or information path. Its technical meaning and boundary are correct, so this
does not recreate the blank-field defect or block the Map's essential meaning.

## What the first 90 seconds communicate after revision

The short stop and the current Home/Read route communicate the intended broad
proposition in this order:

1. **Generic output can begin upstream.** The search can follow the obvious
   path, familiar sources can crowd out a specialist perspective, comparison
   or baseline can be skipped, an expected piece can be missing, and prior
   memory can be absent (`NINETY_SECOND_VERSION.md:3–7`; standalone
   `:557–558`). The answer inherits those choices before generation.
2. **The Discrimination Layer is a responsibility, not a magic component.**
   It decides what the system should notice, acquire, compare, preserve,
   question, and allow to influence an answer, and makes those choices visible
   enough to correct (`NINETY_SECOND_VERSION.md:9–15`; standalone `:558`). The
   same passage explicitly distinguishes technical differentiation from
   classifying people and defines “layer” as a responsibility rather than a
   mandatory architecture.
3. **All six families are present and the scope is broad.** The short sentence
   at `NINETY_SECOND_VERSION.md:17–21` names peripheral signal, source
   weighing, velocity/motion, absence/memory, structured patterns, and the
   learning loop. The closing sentence says the proposal is broader than
   origin counting and narrower than replacing expertise (`:29–34`). The
   standalone Home and Read entries preserve that exact sequence
   (`:559–561` and `:590–592`).
4. **Peripheral is a candidate, not truth.** The short version says this
   directly at `:23–24`; the full essay gives the same boundary in the first
   family's specialist example (`PATTERN_RECOGNITION_V16.md:56–85`).
5. **Human judgment remains.** The revised short stop says people still make
   the judgment and keep authority for consequential action
   (`NINETY_SECOND_VERSION.md:25–27`). The full essay later makes the broader
   limit explicit: the framework can scaffold disciplined attention but cannot
   replace taste, accountability, permission, contextual judgment, or novel-
   situation judgment (`PATTERN_RECOGNITION_V16.md:351–355`).
6. **Origin accounting is one later example, not the definition.** The full
   essay places the nine-report/common-origin case after all six families at
   `PATTERN_RECOGNITION_V16.md:201–229` and says it belongs inside the broader
   picture. The Home places examples, the separate unrun Echo project, and
   history in a later context section (`standalone:574–580`). The Map boundary
   likewise says common-origin recurrence is one mechanism inside source
   weighing and structured patterns, not the map's definition
   (`standalone:761–763`).

My bounded proxy restatement after the revision is: *AI answers inherit what
entered the room before generation. We can make those upstream choices visible
and correctable, using six broad ways to look for what was missed, weigh what
entered, notice change and gaps, compare carefully, and learn without
rewriting history. A peripheral signal is only a candidate, people retain
judgment and consequential authority, and the nine-report origin case is one
later illustration rather than the whole project.* That restatement does not
require opening the glossary or knowing the implementation vocabulary.

## Site, standalone export, and PDF alignment

### Home route

The current Home route begins with the human problem and the upstream framing,
then gives the three principal doors in the required order. In the committed
standalone export, `:530–551` contains the headline, standfirst, broad bridge,
and `Read the idea` / `Explore the map` / `Apply it`; `:554–567` follows with
the short version and six-family preview. The later section at `:574–580`
defers examples, boundaries, sources, research, and history. The committed
desktop and mobile Home captures visually show the human-first opening; the
mobile capture keeps the headline and standfirst legible with the doors below
the fold rather than replacing the opening with metadata.

### Read route

The Read route is cumulative: the short version appears first at
`site/exports/standalone/pattern-map-v16.html:585–592`, the full canonical essay
follows at `:593` onward, and the mentor cover note and public abstract remain
optional handoff/metadata sections after the essay. The cover note itself is
still a direct invitation to challenge the upstream-choice center, six-family
map, name, and voice (`manuscript/MENTOR_COVER_NOTE.md:3–31`), not a substitute
for the public entry. The full essay preserves the human problem, all six
families, the candidate-not-truth boundary, human authority, and late Echo
subordination.

### Map route

The exact post-revision Map renderer has all six family cards in locked F1–F6 order,
plain-language purpose and “How it works” text, boundaries, expandable
technical detail, the current relationship view, the complete optional
glossary, and a human-correction note. The standalone output at
`:681–763` is the committed evidence for that route. The only Map drift is the
stale committed desktop screenshot described under CNR-A06-01.

### Standalone export

The standalone export is self-contained and has separate Home, Read, Map, and
other route sections with prefixed fragments. The exact post-revision file
contains the revised short copy, plain Map bridges, and populated glossary.
The route check passed its unique-ID, heading, fragment, no-script, and link
integrity assertions. This supports the conclusion that the source-to-renderer
fix is present; it does not excuse the stale reviewer screenshot.

### PDF companion and committed renders

The committed PDF is a six-page owner-review companion, not the canonical
10–15-minute essay or the semantic standalone route. All six committed PDF
renders were inspected:

- Page 1 leads with the human problem and three doors.
- Page 2 presents the reading path, a short opening, and the boundary that the
  package is a review companion rather than a result.
- Page 3 presents all six family names and reader questions, the relationship
  view, and the candidate/not-truth boundary.
- Page 4 presents the bounded specialist, motion/absence, common-origin, and
  Signal Foundry examples, with Echo explicitly separate, unrun, and late.
- Page 5 presents ordinary through advanced proportion and an explicit human
  owner/disposition in the operator path.
- Page 6 presents historical/current topology separation, QA limits, and the
  no-deployment/no-publication boundary.

The PDF has no visible clipping or broken glyphs in these committed renders,
and it does not introduce a competing thesis. Its owner-review metadata is
appropriate for this package. It should not be mistaken for measured reader
evidence or for a public handout without a separate presentation decision.

## Required defect versus optional taste

### Required defect remaining before a clean package pass

**CNR-A06-01 / P1 inherited, package-level residual — stale Map screenshot.**
Refresh the committed Map desktop capture, or explicitly mark the old image as
pre-revision and provide a current capture. This is the only required defect I
found after the source and standalone fixes. It affects the reliability of the
owner-review evidence package, not the current Map renderer's front copy.

### Optional taste and presentation notes

These are bounded proxy-reader impressions, not required defects and not
measured evidence:

- **CNR-A04-01 — P2 — late essay register.** The opening, coffee-conversation
  anchor, cover note, and invitation are thoughtful and personal. The “hard
  parts” and future-test section later in
  `PATTERN_RECOGNITION_V16.md:272–337` still accumulates fields, protocols,
  fixtures, validators, and no-results language in a review-memo register.
  The material is honest and correctly placed after the idea. If the owner
  wants a warmer sustained conversation, some inventory could move to the
  Research/Sources route; no removal or boundary weakening is required for
  this review.
- **CNR-NAME-01 — P2 — “Discrimination Layer” remains a loaded first label.**
  The Home eyebrow/title presents the name before the short definition, so a
  general reader may briefly hear social classification. The short version
  immediately defines the intended technical meaning and rejects classifying
  people (`NINETY_SECOND_VERSION.md:9–15`), and the cover note explicitly asks
  for challenge to the name (`MENTOR_COVER_NOTE.md:18–27`). Keep this as an
  owner naming decision, not an automatic copy change.
- **CNR-DENSITY-OPT-01 — P3 — the six-family sentence is compact but dense.**
  The one-sentence inventory at `NINETY_SECOND_VERSION.md:17–21` is efficient
  and preserves broad scope, but a cold reader may retain the overall movement
  more readily than all six labels on a first pass. The following full essay,
  Map cards, and family questions provide a sensible second layer. Splitting
  the inventory into two shorter sentences is optional and would trade some
  compression for ease; it is not required for A01 after the other revisions.
- **CNR-GLOSSARY-OPT-01 — P3 — Common origin's plain translation is generic.**
  The technical meaning and boundary are correct, and the glossary is
  optional; replacing the fallback with “A shared upstream report, event,
  release, dataset, or information path” would make the first line teach the
  term more directly.
- **CNR-VIS-01 — P3 — review metadata is not public-reader prose.** Labels such
  as “local owner review,” “content contract checkpoint,” and “not a research
  result” are useful in the committed companion and PDF. If either artifact
  later becomes the primary public/general-reader handout, a separate export
  could move the QA metadata later or omit it. This is not a defect in the
  current owner-review package.

## Disposition-oriented handoff

This report does not assign the repository's controlled integration
dispositions. For the primary orchestrator's ledger, the practical handoff is:

1. Treat CNR-A01-01 as verified resolved at `2a54b24`.
2. Treat the original blank-field portion of CNR-A06-02 as verified resolved;
   decide separately whether to polish `CNR-GLOSSARY-OPT-01`.
3. Refresh or relabel the Map screenshot for CNR-A06-01, then rerun the narrow
   visual/package check. A current capture should allow A06 and the overall
   verdict to move to PASS on this proxy rubric.
4. Keep the late-register, name, generic glossary translation, and owner-
   metadata observations separate from required defects.

No finding here claims measured understanding, public reception, mentor
agreement, framework effectiveness, or research validity.

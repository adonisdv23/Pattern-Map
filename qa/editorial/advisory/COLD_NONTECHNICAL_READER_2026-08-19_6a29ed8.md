# Cold nontechnical reader review — Pattern Map v16

**Verdict: PASS WITH REVISIONS**

**Reviewed tree:** exact commit `6a29ed834bffa405942b8636a8a6b8e7b48cbf4f`
(`6a29ed8`), reviewed as an owner-review candidate on 2026-08-19.

**Reviewer role:** bounded proxy cold reader with no machine-learning,
software-architecture, or research-methodology expertise. This is a model
proxy review, not the author's mentor, a public-reader sample, measured reader
comprehension, persuasion evidence, or research evidence. Severity below is
review priority, not one of the controlled integration dispositions.

The shared checkout advanced while this review was in progress. To preserve the
requested evidence boundary, the final checks and locators below are pinned to
the `6a29ed8` tree with `git show 6a29ed8:<path>`; later work is outside scope.
No canonical file was edited, and no browser, external source, model, provider,
study, or participant activity was used.

## Files and evidence read

I read the repository instructions and governing contracts in the required
order, then reviewed the exact-commit versions of:

- `manuscript/NINETY_SECOND_VERSION.md`
- `manuscript/MENTOR_COVER_NOTE.md`
- `manuscript/PUBLIC_ABSTRACT.md`
- `manuscript/PATTERN_RECOGNITION_V16.md`
- `site/build.mjs`, `site/src/site.css`, and `site/src/site.js`
- `site/exports/standalone/pattern-map-v16.html`
- committed Home, Map, Apply, and History screenshots under
  `qa/visual/screenshots/`
- the six rendered pages under `qa/visual/pdf-renders/` and
  `site/exports/pattern-map-v16-owner-review.pdf`

The editorial, site, and visual QA records were useful context but were not
treated as evidence of reader understanding. The owner-intent hash check
passed: `docs/OWNER_INTENT_V16.md: OK`.

## Gate readout

| Gate | Proxy verdict | Evidence-backed reading |
| --- | --- | --- |
| A01 — broad idea in 90 seconds | **PASS WITH REVISIONS** | The short version clearly starts upstream, defines an inspectable/correctable responsibility, names all six families, says peripheral material is only a candidate, and says the proposal is broader than origin counting. Human authority is present through “a person who can correct the route” and “narrower than a claim to replace expertise,” but it is indirect and surrounded by specialist boundary words. |
| A04 — thoughtful conversation, not committee document | **PASS WITH REVISIONS** | The opening and ending feel authored, the coffee-conversation frame is real, and the cover note asks for disagreement. The later limitations/research passage and some Map/Apply labels still sound like a requirements document. This is a bounded voice risk, not a thesis or intent failure. |
| A05 — approximately 10–15 minutes | **PASS** | Exact-commit word counts are 3,289 for the essay and 288 for the short version; the recorded editorial estimates of approximately 13.7–14.3 minutes and 74–77 seconds are plausible proxies, not observed timings. The site Read route keeps the full essay intact after the short entry. |
| A06 — progressive disclosure | **PASS WITH REVISIONS** | Home and Read lead with the human problem, short version, and full essay; Map/Apply defer some details behind controls; the static export and PDF retain the main meaning. However, visible Map card copy is jargon-heavy for a general reader, and five glossary entries render empty technical/boundary fields when opened. |

## What the first 90 seconds communicate

The short version is unusually disciplined about not making the Echo example the
thesis. The sequence works as follows:

1. **Generic output can begin upstream — PASS.** Lines 3–7 identify the
   obvious search path, familiar sources, missing specialist perspective,
   absent comparison/baseline, missing information, and missing memory before
   generation. The Home standfirst uses the same broad framing in the exact
   first-screen composition (`site/exports/standalone/pattern-map-v16.html:523–528`;
   `qa/visual/screenshots/home-desktop-1440x1000.png`).
2. **The Discrimination Layer is an inspectable/correctable responsibility —
   PASS WITH A PLAIN-LANGUAGE CAVEAT.** Lines 9–15 say it decides what the
   system should notice, acquire, compare, preserve, question, and allow to
   influence an answer, and makes those choices “visible enough to correct.”
   That is the right substance. The social/architecture defense is long for a
   288-word stop and contains terms a cold reader may not own yet.
3. **All six families and broad scope — PASS.** Lines 17–21 name peripheral
   signal, source weighing, velocity, absence + memory, structured patterns,
   and the learning loop in one sentence. Lines 28–33 add proportion and say
   explicitly that the proposal is broader than origin counting.
4. **Peripheral is a candidate, not truth — PASS.** Lines 23–24 state this
   directly. The full essay reinforces it in the first worked example
   (`manuscript/PATTERN_RECOGNITION_V16.md:56–85`).
5. **Human judgment remains — PARTIAL/PASS WITH REVISIONS.** The short stop
   says higher-stakes work may include “a person who can correct the route” and
   that the proposal is narrower than replacing expertise (`NINETY_SECOND_VERSION.md:28–32`).
   A reader can infer the boundary, and the public abstract states it directly
   (`PUBLIC_ABSTRACT.md:21–23`), but the cumulative short stop would be safer
   with one ordinary sentence that people retain final judgment and
   consequential authority.
6. **Origin accounting is one later example — PASS.** The nine-report case
   does not appear until after all six families (`PATTERN_RECOGNITION_V16.md:201–229`).
   The Home places examples and Echo in a later section, and the Map boundary
   says common-origin recurrence is one mechanism inside source weighing and
   structured patterns (`site/exports/standalone/pattern-map-v16.html:569–575,
   757–758`). The PDF also puts “Echo is separate and late” on page 4 rather
   than opening with it.

The broad message survived my first stop as: *AI answers inherit what entered
the room; the upstream choices can be made visible and corrected; the map is
broader than repeated-source counting; and the amount of structure should fit
the stakes.* That is a successful cold-reader outcome, with the wording fixes
below needed to make the restatement less dependent on inference.

## Required revisions before a clean reader-gate sign-off

### CNR-A01-01 — P1 — Human authority is implied, while the 90-second stop uses specialist boundary words

**Gates:** A01, A06

**Evidence:** `manuscript/NINETY_SECOND_VERSION.md:9–15,23–33` says “human
disposition is not a fact,” “provenance is not correctness,” “inspectable
evidence packet,” “cost and stopping rules,” and “a person who can correct the
route.” The explicit plain-language statement that human judgment and
consequential authority remain essential is instead in the abstract at
`manuscript/PUBLIC_ABSTRACT.md:21–23` and much later in the essay at
`PATTERN_RECOGNITION_V16.md:351–355`.

**Reader risk:** The short version gets the proposition right, but “human
disposition,” “provenance,” and “independent corroboration” are not ordinary
entry-point words. “A person who can correct the route” signals a checkpoint,
not quite the stronger boundary that people retain judgment and authority. A
reader may repeat the framework's vocabulary without being able to say who is
still accountable for the decision.

**Recommendation:** Keep the six-family and origin boundaries, but replace the
most technical phrases with ordinary equivalents in the short version. For
example, say that where something came from is not proof that it is right, and
that repeated reports are not automatically independent confirmation. Add one
sentence such as “People still make the judgment and keep authority for
consequential action.” Preserve the technical terms in the Map glossary and
Apply route, where they have room to be defined. This is a wording repair, not
a change to owner intent or the name of the layer.

### CNR-A06-01 — P1 — The visible Map cards use builder vocabulary before a plain-language bridge

**Gates:** A04, A06

**Evidence:** The exact static Map route exposes the family cards at
`site/exports/standalone/pattern-map-v16.html:677–720`. The first visible
purpose lines include “task-scoped information aperture” (F1), “claim-scoped
authority” and “typed relationships” (F2), “typed gaps” and “source-bound
memory” (F4), and a “dispositioned update proposal” (F6). The desktop Map
capture (`qa/visual/screenshots/map-desktop-1440x1000.png`) shows this register
on the first F1/F2 cards, before a reader reaches examples or the optional
glossary.

**Reader risk:** The questions and family names are clear enough to orient me,
but the explanatory sentence underneath asks a nontechnical reader to decode a
schema. “What might the default path have overlooked?” is a human question;
“widen a task-scoped information aperture” is a committee phrase. This makes
the Map door feel like a framework specification even though the essay has a
more accessible explanation of the same six ideas.

**Recommendation:** Make each card's first purpose sentence ordinary language
and move the current purpose/mechanism vocabulary into the expandable “How it
works” or “Implementation detail” treatment. Examples of the needed register:
“Look beyond the obvious path, but treat what you find as something to inspect,”
“Ask what each source can and cannot tell us about this claim,” and “Notice a
change against a baseline before calling it meaningful.” Keep the locked names,
reader questions, order, and boundaries unchanged.

### CNR-A06-02 — P2 — Five optional glossary entries render visibly empty fields

**Gates:** A06; site-to-source fidelity

**Evidence:** `site/build.mjs:303–325` asks for seven glossary terms and always
renders a technical-meaning paragraph and a boundary paragraph. In the exact
source `framework/GLOSSARY.md:6–48`, the main glossary table contains rows for
“Evidence spine” and “Common origin,” but not “Typed relationship,” “Influence
receipt,” “Cost-bounded route,” “Versioned memory,” or “Human disposition”; the
plain-language table at `framework/GLOSSARY.md:72–81` supplies only their plain
translations. The committed standalone export therefore contains empty
`<p></p>` elements and blank `Boundary:` labels for those five terms
(`site/exports/standalone/pattern-map-v16.html:747–755`).

**Reader risk:** A reader who opens the promised optional glossary sees a
partially broken explanation, not progressive disclosure. The blank fields
also make the site look like an unfinished committee interface and weaken the
boundary language precisely where the technical term is being introduced.

**Recommendation:** Either add the missing technical meanings and boundaries
to the canonical framework glossary, or make the renderer omit empty paragraphs
and labels. The preferred result is a complete, concise row for each promised
term, with the plain translation first and one clear boundary second. Rebuild
the standalone export and recheck the Map route after the fix.

## Optional taste and presentation notes

These are real cold-reader impressions, but they are not required defects in
the broad thesis and should not be mistaken for measured evidence.

### CNR-A04-01 — P2 — The late essay changes genre from conversation to review memo

**Gate:** A04 (bounded residual; not an opening failure)

The opening and close are human and specific: the “coffee conversation” anchor
at `PATTERN_RECOGNITION_V16.md:23–28` and the invitation at `:339–361` made the
piece feel authored. The cover note is especially successful: it starts
personally, asks whether the center is right, asks whether the six families are
a useful map, and invites challenge to the name and voice
(`MENTOR_COVER_NOTE.md:3–31`). At 247 words it is concise enough to be a real
handoff rather than a second abstract.

After the idea is clear, however, `PATTERN_RECOGNITION_V16.md:272–337` rolls
through established fields, value-of-information-style stopping, matched-budget
future-study language, model/provider selection, fixtures, validators, and
unrun-result boundaries. All of it is honest and correctly placed after
comprehension; the accumulation still sounds more like an academic committee
memo than a person continuing a conversation.

**Optional recommendation:** Keep the plain challenge and the statement that
the framework proposes questions rather than results in the essay. Move the
metric/protocol inventory to the Sources or Research route, or shorten it to
one paragraph. Do not remove the limitations or loosen the no-results boundary.

### CNR-NAME-01 — P2 — “Discrimination Layer” remains a high-friction name

**Gates:** A01, A04 (name usability, not an intent defect)

The essay and short version do the responsible thing by defining the term as
information differentiation rather than social classification
(`PATTERN_RECOGNITION_V16.md:35–39`; `NINETY_SECOND_VERSION.md:9–15`). The
cover note also explicitly asks whether the name creates more noise than
precision (`MENTOR_COVER_NOTE.md:18–27`). Even so, the Home eyebrow and
standalone title present the loaded label before a general reader has the plain
definition. The first reaction may be to wonder about social discrimination
rather than attend to the upstream-choice idea.

**Optional recommendation:** Keep the locked name for now, but put a short
descriptor next to it wherever it first appears: “the responsibility for what
enters, matters, and can be corrected.” A future owner decision can revisit the
name; this review does not propose changing locked intent.

### CNR-VIS-01 — P3 — Owner-review metadata is appropriate for the package but not for a public reading copy

**Gates:** A04/A06 only if the companion is handed to a general reader as the
primary entry

The local Home screenshots begin with the human problem and show the three
doors. The PDF is also readable and unclipped: page 1 moves from the owner-
review title to the human problem, pages 2–5 summarize Read/Map/Examples/Apply,
and page 6 records lineage, QA status, and residual boundaries. The standalone
HTML and PDF nevertheless foreground labels such as “STANDALONE REVIEW EXPORT,”
“LOCAL OWNER REVIEW ONLY,” “CONTENT CONTRACT CHECKPOINT,” “OWNER-REVIEW QA
COMPLETED,” and “LOCAL HANDOFF.” Those are useful owner-review metadata, not
human-facing prose.

**Optional recommendation:** Preserve these labels in the owner-review
companion. If the PDF or standalone file is later used as a public/general
reader handout, make a separate print/export variant whose first visible move
is the human problem and whose QA/contract metadata is at the end or omitted.

## Site-to-manuscript alignment

There is no material thesis drift at the reviewed commit:

- **Home:** The exact approved headline/standfirst matches the broad opening;
  the human problem precedes protocol, research status, Echo, and source
  defense. The desktop/tablet/mobile captures show the three principal doors;
  the mobile cards begin directly after the hero rather than being displaced by
  decorative media.
- **Read:** The route presents the short version first, then the complete
  canonical essay, then the cover note and abstract as optional details
  (`site/exports/standalone/pattern-map-v16.html:577–671`). The essay is not
  silently abridged or interleaved with builder protocol.
- **Map:** F1–F6 are present in the locked order with the correct names and
  reader questions. The current code-native relationship view is explicitly
  distinguished from the recovered v13 image. The issue is register and the
  broken optional glossary, not a change in family meaning.
- **Origin/Echo boundary:** The nine-report example is late in the essay and
  in the Examples route; the site repeatedly calls Echo a separate, unrun,
  no-results project. The broad routes remain intelligible without making
  origin accounting the definition.
- **PDF:** The companion preserves the headline, broad idea, six-family table,
  bounded examples, application spectrum, historical label, and no-results
  boundary. It is a compact review summary, not a substitute for the full
  10–15-minute essay, which is appropriate as long as it is labeled a
  companion.

The only concrete site-to-source drift found in this lane is the glossary
rendering defect (CNR-A06-02), plus the visible Map register becoming more
technical than the human essay. Neither silently changes owner intent, family
scope, Echo separation, or the evidence boundary.

## Recommended order of action

1. Add the explicit human-judgment/authority sentence and plain equivalents to
   the 60–90-second version (CNR-A01-01).
2. Rewrite the first visible Map card sentences in ordinary language while
   keeping technical details available behind progressive disclosure
   (CNR-A06-01).
3. Complete or safely suppress the five empty glossary fields, rebuild the
   standalone export, and recheck the Map route (CNR-A06-02).
4. If the owner wants a warmer mentor/public reading experience, thin the late
   research/QA register and place the high-friction name beside a plain
   descriptor (CNR-A04-01, CNR-NAME-01).

After items 1–3, I would reclassify A01 and A06 as **PASS** on this proxy rubric;
A04 would remain **PASS WITH REVISIONS** only if the owner considers the late
committee-tone concern material, otherwise **PASS**. A05 is already **PASS**.

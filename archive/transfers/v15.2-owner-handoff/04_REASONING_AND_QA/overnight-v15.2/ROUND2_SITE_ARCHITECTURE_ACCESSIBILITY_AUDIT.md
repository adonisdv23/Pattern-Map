# Round 2 site architecture / accessibility audit

## Pattern Recognition / The Discrimination Layer v15.1 → v15.2

**Lane:** site information architecture, progressive disclosure, accessibility,
CSS-native explanatory visuals, responsive/print behavior, and
manuscript/site agreement  
**Status:** audit-only recommendation for the parent integrator  
**Date:** 2026-08-19  
**Verification boundary:** the prior-round reports, charter, reader contract,
current manuscript/candidate, current site source, package metadata, and
rendered-HTML test source were read. No canonical source/site file was edited;
no browser, screen reader, print preview, deployment, publication, external
search, live provider, or study run was used in this lane.

## Executive verdict

The current reader has the right foundation: an authored paper-and-ink visual
voice, a concrete nine-report receipt, real semantic tables, explicit status
labels, a no-results Lab, and an unchanged historical v13 image with a text
transcript. Preserve those decisions.

The v15.2 site is not yet owner-ready in two material respects:

1. The reading-time labels do not point to truthful, explicit stop markers. The
   current `60–90 seconds` card points to a three-item takeaway before the
   receipt; `Continue · about 5 minutes` points to the beginning of a long
   section with no five-minute boundary; and there is no `12–15 minutes` stop
   marker. The page therefore makes a route promise the DOM does not fulfill.
2. `Term` is neither a valid modal dialog nor a complete nonmodal disclosure.
   It renders `role="dialog"`, leaves focus on the trigger, does not make the
   page inert or trap focus, omits `aria-describedby`, points
   `aria-controls` at an element that does not exist while closed, and lets
   multiple document-level Escape handlers compete when terms are open. The
   desktop panel can also run past the viewport edge. These are semantic and
   interaction bugs, not merely polish items.

The smallest coherent v15.2 repair is a bounded convergence pass:

- adopt one explicit route contract: first stop = scene + `09 / 01 / 00 / HOLD`,
  five-minute stop = three questions + correction invariant + no-results
  boundary, 12–15-minute stop = loops + use boundary + objections + narrow
  research bridge;
- make `Term` a native, nonmodal disclosure (details-first, with optional JS
  enhancement) because these explanations are optional and must remain useful
  without JavaScript, in print, and in the reading flow;
- integrate at most three CSS-native microvisuals, each with a figure/text
  equivalent and one conceptual job; defer the dense sample-size/negative-result
  visual and retire the generic flow visual from the first pass;
- keep full C01–C11 records, protocol gates, source-status detail, and relation
  codes behind Explore/Lab/Sources; and
- update the rendered tests so they enforce the chosen semantics instead of
  currently blessing `role="dialog"` without testing dialog behavior.

This is an architecture and accessibility repair, not a new framework or a
new image program.

## Evidence and boundaries carried forward

The recommendations below preserve the following settled boundaries from the
charter and the two rounds of prior review:

- The receipt is fictional. `09` observations, `01` known shared path, `00`
  counted supporting paths, and `HOLD` are an illustration, not a result,
  provenance discovery, or product evaluation.
- A supplied relation in the planned benchmark is stipulated, not inferred
  real-world provenance or universal independence. `UNKNOWN` must remain
  unresolved.
- `N=300` is provisional fictional test-case planning, not a participant count,
  confidence value, quality score, or completed run. No model has been selected
  and no study has run.
- The warm paper, ink, serif reading type, compact mono labels, thin rules,
  and restrained teal/coral/violet/ochre/blue accents are part of the authored
  voice. New visuals should clarify a decision, not turn the reader into a
  dashboard user.
- `site/public/images/v13-six-families-origin-map.png` remains byte-identical
  and historical. Its caption, boundary label, alt text, and text transcript
  must continue to say that it is v13, not the v15.2 topology or evidence.
  The existing `nine-mentions-one-origin.jpg` remains an explanatory
  illustration with an explicit “not a result” boundary; it is not a substitute
  for the proposed CSS-native microvisuals.

## Current architecture: what is working

Several current choices should be protected rather than redesigned:

- The home masthead states the conceptual/no-results status and leads with the
  nine-report failure (`site/app/page.tsx:75–87`).
- The receipt is text-first and already carries the decision frame, count
  snapshot, nine-row observation ledger, relation key, contrast roots, and
  `HOLD · VERIFY ANOTHER ORIGIN RELATION` (`site/app/page.tsx:143–217`).
- Wide data is placed in labelled, keyboard-focusable contained-scroll regions,
  with a mobile summary for the receipt (`page.tsx:175–190`,
  `globals.css:189–197, 684–690`). This is the correct pattern for a table;
  do not replace it with a CSS-only grid.
- Explore keeps the six-family map and all eleven component records separate
  from the home route (`page.tsx:309–401`). Lab keeps the proposed conditions,
  gates, T1 boundary, and negative-result commitment separate from the essay
  (`page.tsx:559–651`). Sources carries the expanded glossary and source list
  (`page.tsx:653–687`).
- Focus styling, reduced-motion rules, table print rules, and the v13 text
  transcript are already present (`globals.css:26–30, 660–663, 665–711`).
  They need targeted extension, not replacement.

The main issue is proportion and interaction semantics: the right information
exists, but too much of it is on the wrong stop, and the optional explanations
are implemented with an ambiguous role.

## 1. Truthful reading paths and stop markers

### Confirmed current timing problem

The current home route contains the masthead status, title definition, hero
scene, thesis callout, four route cards, and then the `60–90 second takeaway`
(`site/app/page.tsx:75–120`). The `Start here · 60–90 seconds` link targets
`#takeaway`, but that target contains only the general proposition and three
bullets. It does not contain the four receipt values or the “zero is not
rejection” consequence required by the charter. The reader can stop there and
miss the project’s actual behavior change.

The `Continue · about 5 minutes` link targets `#essay` (`page.tsx:94–98`).
That section immediately includes the full receipt, nine-row ledger, relation
codes, contrast roots, six-question grid, distinction block, v13 continuity
note, and use boundary (`page.tsx:130–307`). There is no element marking where
the essential argument ends. The current site also does not render the loops,
objections, or research bridge on the home route; those are on `/explore` and
`/lab`, while the manuscript and route copy describe a longer continuous path.

The current v15.1 manuscript says `15–20 minutes` for conceptual exploration
and `30–45 minutes or more` for research/technical review. Round 2’s selected
editorial direction narrows the public promise to `12–15 minutes` for loops,
use boundary, objections, and the narrow research bridge. The site must choose
one contract and expose its actual boundaries; it cannot keep all of these
labels simultaneously.

### Required route contract

Use the following contract in both the selected manuscript/candidate and the
home route. The wording can be punctuated differently, but the contents and
stop order should not change.

| Stop | Target content | Current failure | Required marker and budget |
| --- | --- | --- | --- |
| **60–90 seconds** | The fictional nine-report scene; the fact that repetition did not create new roots; compact `09 / 01 / 00 / HOLD`; one sentence that `00` is a hold on the broad claim, not rejection or missing source. | `#takeaway` has the time label but not the receipt consequence. The first route can end before the reader knows what is preserved or what happens next. | Add a visible, focusable target such as `id="stop-60-90"`, labelled “60–90-second stop.” Keep the visible prose to roughly 300–350 words including the compact receipt context, with no F-codes, N/T labels, or methods shorthand. |
| **About five minutes** | The three plain questions: where the report came from; what exact claim it supports; what may happen now. Include the human next step, correction invariant, and one plain “no study has run” status sentence. | `#essay` is a section start, not a stop. Its detailed ledger and 12-item distinction grid make the route longer and more technical than promised. | Add `id="stop-5"` after the correction invariant, with a visible “About five minutes” marker and an explicit “deeper records continue below/on Explore” sentence. Keep the public route to at most ~1,250 visible prose words before this marker, excluding compact chrome and the small receipt table. |
| **12–15 minutes** | The current-decision loop, outcome loop, use boundary, strongest objections/retirement tests, and the narrow proposed research bridge. | No marker exists. The home route stops before loops and objections; Explore/Lab are not labelled as a continuous 12–15-minute path. | Add `id="stop-12-15"` after this public bridge, or add a clearly labelled “12–15-minute full argument” on the home route that points to the exact start and end. Target approximately 2,700–3,300 visible words at the project’s 220–260 wpm reading assumption. |
| **Optional deeper routes** | Full C01–C11 records and cases; exact Lab gates; prior-art status and historical record. | Explore/Lab/Sources exist, but their optional role is not tied to an explicit stop contract. | Keep `/explore`, `/lab`, and `/sources` as optional routes. Their labels must say what they contain, not imply that the reader must traverse them to complete the argument. |

The first stop should not be a second full receipt. Use a compact four-field
receipt at `#stop-60-90`, then keep the detailed receipt as a progressively
disclosed block or immediately after the five-minute stop. The full nine-row
ledger, B1/C1 contrast roots, exact relation codes, and table remain valuable;
they do not belong in the timed first stop.

The exact first-stop sentence should be close to:

> One path is known; zero paths are counted as support for this broad claim
> yet. That is a hold, not a rejection: inspect one separately authored
> relation before changing the claim.

Use “reports” rather than “tabs.” A browser tab is a UI container, not the
evidence unit. Restore the manuscript’s sharper reversal: “The summary has not
merely shortened the evidence. It has changed its structure.”

### Stop-marker implementation contract

Each marker should be a real semantic element, not only a route-card label:

```tsx
<section id="stop-60-90" className="route-stop" aria-labelledby="stop-60-90-title">
  <p className="route-stop-label">60–90-second stop</p>
  <h2 id="stop-60-90-title">Nine reports can still follow one path.</h2>
  {/* scene, compact receipt, and zero-is-not-rejection consequence */}
</section>
```

The implementation may use a `data-route-stop` attribute for the offline test,
but the `id`, visible label, heading, and route link must agree. The route cards
and `ReadingNav` (`site/app/ReadingNav.tsx:5–16`) should link to these exact
markers. A route card is not a stop merely because its text says “five
minutes.”

The marker should be the last meaningful content in the promised stop. Do not
place it before a required explanation or put essential status in a collapsed
block that a cold reader is not expected to open. Conversely, do not include a
full C01–C11 inventory, Lab gate names, or prior-art parade before the five-
minute marker.

## 2. Progressive disclosure and manuscript/site agreement

### Public order

The visible sentence must stand if every explanation is closed, JavaScript is
blocked, images fail, or the document is printed. The recommended order is:

1. **Plain scene:** nine reports, one announcement, no technical noun needed.
2. **Compact receipt:** observations, known shared path, counted support, and
   human next step. State that zero is not rejection in the same block.
3. **Three plain questions:** where it came from; what it supports; what may
   happen now.
4. **One correction invariant:** changing a relation changes the count/route
   while preserving the original observation.
5. **Optional records:** typed labels, C01–C11, B1/C1, exact protocol gates,
   prior-art statuses, and the extended glossary.

Current `page.tsx` reverses some of this order. It introduces a full relation
key with `DEPENDENT`, `INDEPENDENT-AS-STIPULATED`, and `UNKNOWN` at
`page.tsx:193–200` before a reader has received the three ordinary-language
states. Keep the exact key in the detailed receipt/Explore, but lead the first
route with “shared path / separate only in this test / unresolved.” The codes
are useful record labels, not first-route prose.

### Trigger inventory and repeated-trigger risk

The current page repeats interactive explanations for the same concepts:

- “Recorded human decision” appears in the receipt header and footer, with the
  same definition (`page.tsx:147, 216`), and again as the technical glossary
  entry (`content.ts:316–321`).
- `N=300` appears in both the Lab method note and metric (`page.tsx:590,
  595`), plus the technical glossary (`content.ts:294–300`).
- `Provenance audit`, `System runtime`, `F0 / F1 / F2`, T1, and the negative-
  result commitment each have a first-use explanation and a deeper glossary
  occurrence.

Repeated static definitions are acceptable; repeated popover triggers are not
the best hierarchy. Keep one interactive explanation at the first/highest-
value occurrence on each route. Later occurrences should be plain text, a
short sentence, or a normal link to the relevant glossary anchor. In
particular:

- keep the first receipt explanation for the recorded human next step;
- remove the footer’s duplicate trigger and retain its plain status sentence;
- keep one `N=300` trigger in Lab and make the metric a plain “300 planned
  bundles” label;
- keep the F0/F1/F2 trigger at the Lab condition heading and use a normal
  glossary link later; and
- keep technical glossary cards readable as static text even if their trigger
  is never activated.

The runtime should also enforce one open explanation per route (or use a
documented, collision-safe multi-panel pattern). Two overlapping panels with
the same concept are not useful progressive disclosure. Unique IDs must be
checked across every `Term` instance, not only the closed server-rendered DOM.

## 3. `Term` semantic and accessibility audit

### Confirmed current bugs

These are observed from `site/app/Term.tsx` and `site/app/globals.css`, not
hypothetical future concerns.

| Finding | Evidence | Why it is a bug | Required disposition |
| --- | --- | --- | --- |
| **Modal/nonmodal mismatch** | `Term.tsx:51–73` renders `role="dialog"`; no `aria-modal`; page is not inert; focus is not moved into or trapped in the panel. | A dialog role gives assistive technology a dialog expectation, while the implementation behaves like an inline nonmodal disclosure. A mobile fixed bottom sheet can visually read as modal while allowing focus behind it. | Reject the current hybrid. Choose one pattern. The recommendation here is a nonmodal disclosure because the explanation is optional and the reader should retain the reading flow. Do not retain `role="dialog"` unless the full modal contract is implemented. |
| **Focus does not enter on open** | `Term.tsx:20–36, 40–47`; opening only toggles state. Focus remains on the trigger. | This is not automatically wrong for a nonmodal disclosure, but it is wrong for the current dialog role and gives no reliable announcement/reading transition for screen-reader users. | With native disclosure, keep focus on the summary/trigger and expose the expanded state; do not call the panel a dialog. On close, return focus to the summary. If the integrator chooses a dialog instead, focus must move to the heading/close control and be trapped. |
| **`aria-controls` points to no element while closed** | The panel is conditionally rendered at `Term.tsx:51`; the trigger always emits `aria-controls={popoverId}` at `:45`. | The accessibility relation references a target that is absent in the server-rendered and closed DOM. Existing tests only inspect source text and do not catch this. | Render the disclosure content in the DOM in a native `<details>` or always-rendered hidden region. Native `<summary>` removes the need for a fragile `aria-controls`; otherwise keep a stable target and test it. |
| **No description association** | Panel has `aria-labelledby={headingId}` but no `aria-describedby` (`Term.tsx:52–61`). | The definition, example, and boundary are not explicitly associated with the named explanation for announcement. | Add one stable description container (`definition + example + boundary`) and associate it with the region. With details, use a labelled `aside`/`div` region; do not rely on a generic span’s reading order. |
| **Global Escape listener races** | Every open instance adds a `document` keydown listener (`Term.tsx:26–36`). | If two terms are open, one Escape event closes every instance and each handler calls its own trigger’s `.focus()`. Final focus is order-dependent and may jump away from the panel the reader was using. | Remove the per-instance document listener in favor of a scoped details enhancement or one active-instance controller. Escape closes only the open instance and restores its own trigger focus. |
| **Multiple panels can remain open** | Trigger toggles local state (`Term.tsx:47`); no outside/light-dismiss or one-open policy exists. | Repeated terms can stack/clash, especially when an earlier absolute panel remains open while another opens. | Use one-open-per-route enhancement or an explicit nonoverlapping policy. Test opening a second trigger, closing it, and restoring focus to the correct summary. |
| **Desktop collision/clipping** | `.term-popover` is `left:50%`/`translateX(-50%)` with a 360px width (`globals.css:496–515`). | A trigger near either viewport edge can place the panel outside the viewport; ancestor overflow and 200% reflow are not accounted for. | Use collision-safe placement: native top-layer/anchor positioning with fallback, or a measured fixed panel clamped to viewport insets and placed above when below space is insufficient. Test left-edge, center, right-edge, 320px, and 200% reflow cases. |
| **No-JavaScript path is not actually a disclosure** | The comment promises readable prose (`Term.tsx:15–17`), but the trigger is a button and the panel does not exist until client state opens it. | A user without JS receives a button-like technical label with no expandable definition. The route may still be broadly understandable, but the explanation is not available as promised. | Make the server-rendered content a native `<details>/<summary>` disclosure. Keep the surrounding sentence independently intelligible, and treat the optional panel/visual as enhancement. |
| **Touch target is only text-sized** | `.term-trigger` has `padding: 0 1px` (`globals.css:484–494`). | Inline prose can make this difficult to activate accurately on touch and at magnification. | Preserve the dotted underline/voice but add a tested inline hit area and touch behavior; use the WCAG inline exception only if a larger target would damage prose layout. Verify at 320/390px and with touch emulation. |
| **Visual `aria-label` is on generic spans** | `Term.tsx:62–70` puts `aria-label` on `<span>` and hides the dots/arrows. | A generic span is not a reliably announced image/widget; some screen readers ignore the label, while visible caption text can be duplicated or disconnected. | Use `<figure>`/`<figcaption>` or a labelled region with visible text. The CSS arrangement is never the sole semantic carrier. |
| **Print has no Term fallback** | Print rules cover tables/details but not `.term-popover` (`globals.css:665–716`). | Closed client panels are absent; an open absolute/fixed panel can be clipped or printed out of context. | Print the definition/example/boundary as normal static content, hide close controls and decoration, and verify definitions appear once whether the disclosure was opened or not. |

`aria-labelledby` pointing to the visible heading is a sound association in
the current component. The problem is not the heading ID itself; it is the
missing description, absent closed target, role mismatch, and focus contract.

### Chosen interaction contract: native nonmodal disclosure

Use a details-first structure for `Term`:

```tsx
<details className="term-wrap" id={`term-${id}`}>
  <summary className="term-trigger" aria-label={`Explain ${visibleLabel}`}>
    {children}
  </summary>
  <aside
    className="term-popover"
    aria-labelledby={`${id}-heading`}
    aria-describedby={`${id}-description`}
  >
    <div className="term-popover-head">
      <strong id={`${id}-heading`}>{visibleLabel}</strong>
      {/* optional JS-enhanced close button; summary closes without JS */}
    </div>
    <div id={`${id}-description`}>definition, example, and boundary</div>
  </aside>
</details>
```

This is a semantic sketch, not a request to copy the markup verbatim. The
implementation must satisfy these behaviors:

- The page remains nonmodal: no `aria-modal`, no inert page, and no backdrop
  that implies the reader cannot interact with the document. The mobile panel
  may be fixed for legibility, but it must be visually and semantically
  nonmodal.
- The summary/trigger is keyboard and touch operable and exposes native
  expanded/collapsed state. Its accessible name identifies the action as an
  explanation without hiding the visible term’s meaning.
- The panel is present in server HTML when closed, with a stable heading and
  description association. The definition, example, and “does not mean”
  boundary are ordinary text; no critical meaning is in `aria-label` alone.
- JavaScript enhancement may add an explicit close button, one-open-per-route
  behavior, collision-safe placement, and Escape-to-close. Escape is scoped to
  the nearest open disclosure and returns focus to its summary. Without
  JavaScript, clicking the summary opens/closes the content and the page
  remains understandable.
- A second open term either closes the first deterministically or is placed so
  both are fully visible and independently labelled. The recommended default
  is one open term per route because the terms are short explanations, not a
  comparison workspace.
- In print, every closed disclosure’s substantive text is displayed in flow;
  close buttons, shadows, dotted trigger decoration, and connector decoration
  are hidden. The print result does not require a reader to activate anything.

If the parent integrator instead selects a true modal dialog, the minimum
acceptable alternative is materially larger: use a real dialog element or
equivalent with `aria-modal="true"`, move focus to a labelled heading or close
control on open, contain Tab/Shift+Tab within the panel, close on Escape and an
explicit button, restore focus to the initiating trigger, prevent background
interaction, handle outside dismissal intentionally, and provide a no-JS
static definition. The current component does none of those modal-specific
steps, so leaving `role="dialog"` in place is not an acceptable compromise.

## 4. CSS-native microvisual placements (maximum three)

The site should add no hero image, framework-map bitmap, generated SVG
topology, or visual gallery. The existing receipt already does the main visual
work. Use at most these three compact, deterministic placements:

| Placement | Route / insertion point | One conceptual job | Required semantic/text treatment | Boundary |
| --- | --- | --- | --- | --- |
| **1. Origin vs report count** | Home `#stop-60-90` compact receipt or the first “where a report’s information came from” explanation. Do not add a second full-width card after the receipt. | Show that nine observations can sit on one known shared path without becoming nine origins. | Use an ordered list or labelled figure: `O01–O09` → `Origin A`; live caption/text repeats `09 observations`, `01 known shared path`, `00 counted supporting paths`. Keep B1/C1 out of the first stop or label their support unassessed. A connector is a trace, not a causal/confidence arrow. | Not a provenance discovery, truth signal, or claim-support score. Reports remain useful observations. |
| **2. Trace → unresolved → hold** | Inside the receipt’s relation/decision explanation, preferably the first high-value explanation for the recorded human next step or origin relation. | Separate lineage, claim support, and human action so `UNKNOWN` does not visually become a conclusion. | Three stacked/side-by-side state cards or an ordered list: trace (`Origin A → observations`), claim state (`INSUFFICIENT`), human action (`HOLD · VERIFY`). Put `UNKNOWN` beside the relation state. Use visible labels and a caption; no color-only or arrow implying causation. | A trace does not prove the claim; a hold is not external truth; an unresolved relation is not independent. |
| **3. Three versions of one task** | `/lab`, immediately before or alongside the existing condition table. The table remains the authoritative text/data surface. | Isolate the one planned difference among ordinary, rule-only, and rule-plus-supplied-label conditions. | Three semantic cards or an ordered list with the same evidence repeated and only the prompt-visible difference highlighted. Keep ordinary names first and F0/F1/F2 second. The table and a short prose summary remain available to screen readers/print. | No winner/result arrow, effect size, or product-version implication. F2 vs F1 is a proposed comparison, not evidence that the framework improves decisions. |

The current generic `evidence → judgment → human action` flow (`Term.tsx:68–71`)
does not earn a separate placement; fold its useful words into placement 2 or
remove it. Defer the dense `30 dots shown · each dot stands for 10 bundles`
sample-size visual (`Term.tsx:62–66`) and the four-outcome sample/negative-result
prototype from the public pass. If the owner later insists on retaining it,
it belongs only in Lab, and it counts as a replacement for one of the three,
not a fourth addition. Dots must never resemble participants, model calls,
observed successes, or a favorable result.

Every visual must have a prose sentence before it, a real heading/caption, and
an equivalent `ol`, `dl`, table, or paragraph. If borders, arrows, dots, color,
or images disappear, the reader must still recover the counts, relation state,
claim state, and action. CSS-native means semantic HTML plus CSS; it does not
mean hiding a diagram in an ARIA label.

## 5. Responsive, motion, contrast, and print behavior

### Current strengths and current gaps

The current CSS already moves the rail to a sticky horizontal nav, collapses
multi-column content, converts loop tracks to one column, and keeps wide data
inside labelled scroll regions (`globals.css:550–638`). It also disables smooth
scroll and transitions under reduced motion (`globals.css:660–663`). Keep this
voice and behavior.

The Term mobile rule uses a fixed bottom sheet with `max-height: min(70vh,
460px)` (`globals.css:640–652`). That protects against the desktop centering
collision, but the panel can cover the sentence that motivated it, has no
explicit safe-area inset, and still inherits the dialog/nonmodal mismatch. A
nonmodal panel must not look like a blocking modal; a long explanation needs an
obvious heading, close affordance, internal scroll, and enough bottom padding
for touch/keyboard focus.

### Required responsive checks and implementation constraints

Test at 320px, 390px, 720px, and 1440px CSS widths, plus 200% text reflow and
touch emulation. The following must hold:

- no horizontal page scroll; only the receipt, state, and Lab comparison data
  regions may scroll horizontally, and each region has a visible/plain-language
  scroll hint and accessible label;
- the three microvisuals become a one-column stack at narrow widths, with
  labels wrapping rather than clipping; use `min-inline-size: 0` and
  `overflow-wrap: anywhere` for long relation/status labels;
- the Term panel stays inside the viewport, respects `env(safe-area-inset-*)`
  on mobile, has a readable close target, and does not hide the only copy of
  the sentence it explains;
- the trigger remains visibly focused after keyboard use; its inline target is
  comfortable to tap without turning the prose into a row of oversized cards;
- all state names (`UNKNOWN`, `HOLD`, `INSUFFICIENT`, “shared path”, and
  “separate only in this test”) remain written in text in grayscale, forced
  colors, images-disabled mode, and high-contrast settings; and
- reduced motion removes smooth scrolling/transitions but does not remove
  disclosure content or alter the route’s meaning.

The receipt table’s current contained-scroll fallback and mobile summary should
remain. Do not make the nine-row ledger a CSS visual or replace it with cards
that lose table headers and row relationships.

### Print contract

The current print stylesheet correctly opens long `details` records and makes
tables printable (`globals.css:680–711`), but it has no Term rule. Add a print
contract for the chosen disclosure:

- show each closed Term definition/example/boundary in normal flow;
- hide the close button, trigger dotted decoration, shadows, and nonsemantic
  arrows/dots;
- keep the figure caption and visible text equivalents for all three
  microvisuals;
- keep table captions, headers, and the receipt’s count/status labels together
  where possible; allow the intentionally wide data table to fit the page using
  the existing `min-width: 0`/fixed-layout rules; and
- retain the v13 image only with its historical boundary/caption/transcript,
  never as a current topology.

Print acceptance is not “the panel happens to print if it was open.” A closed
browser session must produce the definitions and status needed to understand
the document.

## 6. Manuscript/site agreement ledger

The current manuscript, v15.2 candidate, and site contain strong overlapping
material but are not yet one reading contract. Use this ledger when integrating:

| Topic | Canonical agreement to make | Current site/manuscript issue | Required repair |
| --- | --- | --- | --- |
| Opening unit | “Nine reports, one origin/announcement,” not “nine tabs.” | The v15.2 candidate says “Nine tabs”; the current site and v15.1 manuscript say reports. | Keep “reports” and restore “The summary has not merely shortened the evidence. It has changed its structure.” |
| First stop | Scene + `09 / 01 / 00 / HOLD` + zero-is-not-rejection. | Site’s `#takeaway` lacks the receipt; candidate’s first route is too long. | Make compact receipt and consequence the actual `#stop-60-90` target. |
| Five-minute explanation | Three questions, correction invariant, human next step, no-results status. | Site `#essay` starts with a long receipt and full distinction inventory; no marker. | Collapse first route, move codes/records deeper, and place `#stop-5` after the invariant. |
| Longer public route | Loops, use boundary, objections, narrow research bridge, `12–15 minutes`. | Current home does not render loops/challenges/Lab; v15.1 manuscript says 15–20 plus 30–45 technical routes. | Choose the Round 2 `12–15` contract and either render the compact bridge on home or label the cross-route sequence explicitly. |
| Count language | “09 observations / 01 known shared path / 00 counted support / HOLD.” | Site says “Known common-origin clusters for those records” and uses “supporting origins” before plain explanation (`page.tsx:167–172`); candidate wording is clearer. | Use plain terms first; retain exact cluster/origin schema labels only in detailed receipt/Explore. |
| Relation states | Shared path / separate only in this test / unresolved before codes. | Site exposes `DEPENDENT`, `INDEPENDENT-AS-STIPULATED`, `UNKNOWN` in the home receipt key. | Lead with the plain three-state key; retain codes in deep records. |
| Research status | “This is a proposed comparison, not a result. No model has been selected and no study has run.” | Lab is close (`page.tsx:562–570`), but candidate/manuscript methods phrasing can sound prepared/validated. | Use one exact status sentence before the research question; call `N=300` provisional fictional cases. |
| Prior art | Selected precedents with heterogeneous publication/review statuses. | Sources says “Selected primary and official references” (`page.tsx:653–658`) while `content.ts:339–359` includes standards, published papers, datasets, and unreviewed arXiv records. | Change heading to “Selected precedents and status notes” (or equivalent), link the ledger, and do not flatten authority classes. |
| Product cases | Translation, not independent validation. | Explore already carries explicit boundaries (`page.tsx:532–555`). | Keep cases optional and out of first five-minute route. |
| Historical v13 | Historical anchor only; unchanged image and transcript. | Current page’s caption/alt/transcript are aligned (`page.tsx:241–273`). | Preserve byte identity, caption, alt, transcript, and “not the v15.1/v15.2 system map” boundary. |
| Version/status chrome | One version and one owner-review/no-results status. | Current page/footer/layout use v15.1 (`page.tsx:68, 77–80, 698`; `layout.tsx:7`), while the overnight package is a v15.2 candidate. | Do not relabel the site v15.2 until the selected manuscript/content/site patch is integrated; then update all visible metadata and tests in one patch. |

No site surface should imply that the manuscript is complete while its actual
stop markers and route contents disagree. The public copy can be shorter than
the detailed receipt; it cannot change the meaning of the receipt.

## 7. Smallest coherent file-level patch sequence

The parent integrator should apply the following sequence after choosing the
editorial candidate as the canonical content base. This list is a recommendation
only; no file in this lane was edited.

### Patch 1 — lock the content and route contract

Update the selected manuscript path (`source/candidates/THOUGHT_PIECE_V15_2_EDITORIAL_CANDIDATE.md`
until the owner promotes it, then the canonical manuscript) and the route copy
in `site/app/page.tsx` together. Add the three explicit stop markers, exact
receipt wording, zero-is-not-rejection sentence, plain relation states, and one
research status sentence. Remove “tabs,” “primary and official” authority
wording, and unexplained first-route method shorthand.

Do not start by adding visuals. If the text route is not truthful, a visual
will only make the timing/genre problem harder to see.

### Patch 2 — replace the ambiguous Term contract

Update `site/app/Term.tsx` to the details-first nonmodal disclosure described
above. Keep deterministic IDs, but render the content in server HTML. Scope
Escape/close behavior to the active disclosure, restore focus to its summary,
and avoid the current all-document listener race. Remove `role="dialog"` unless
the integrator deliberately implements the full modal alternative.

Update `site/app/content.ts` only as needed to separate first-use visible
wording from technical labels and to remove/defer the generic `flow` and
`sample-size` visual flags. Do not duplicate definitions to compensate for a
broken interaction; the static card prose should remain the source of truth.

### Patch 3 — add the maximum-three visual package

Either add one small `site/app/MicroVisual.tsx` semantic component with three
named variants, or keep three auditable `<figure>` blocks in `page.tsx` if a
new component would add more abstraction than value. Do not create a visual
framework or bitmap assets. Implement only:

1. origin/report count;
2. trace/unknown/hold; and
3. F0/F1/F2 planned-condition comparison.

Each variant must include live text, a heading/caption, and a boundary. Keep the
existing receipt table and Lab table as authoritative text surfaces.

### Patch 4 — integrate route and hierarchy changes

Update `site/app/page.tsx` to:

- place the compact receipt at `#stop-60-90`;
- move the detailed ledger/codes/contrast roots behind the five-minute/deeper
  boundary or an explicit disclosure;
- place `#stop-5` after the three questions and correction invariant;
- add the compact 12–15-minute bridge (or an honest cross-route marker);
- keep full C01–C11/loops/cases on Explore, exact gates on Lab, and source
  statuses/glossary on Sources; and
- remove duplicate interactive triggers after first use.

Update `site/app/ReadingNav.tsx` so its labels and fragments target the same
stop IDs. If the site version is promoted to v15.2, update `site/app/layout.tsx`
metadata, visible page/footer labels, and tests in the same patch; otherwise
leave the current v15.1 labels rather than creating a mixed version.

### Patch 5 — CSS and print behavior

Update `site/app/globals.css` for the chosen details disclosure, collision-safe
placement, mobile safe-area/scroll behavior, touch target, microvisual grids,
forced-color-safe labels, and print expansion. Preserve the current paper/ink
system, serif/mono type roles, contained table scroll, reduced-motion rule,
and unchanged historical image treatment.

### Patch 6 — make the release tests enforce the contract

Update `site/tests/rendered-html.test.mjs` (and add a focused browser/manual
checklist if the repository’s test harness supports it) to test the actual
chosen pattern. The current test at lines 98–109 explicitly requires
`role="dialog"` but does not test `aria-modal`, focus entry, focus containment,
description association, no-JS rendering, collision, or repeated triggers. It
therefore codifies the current mismatch and must be changed, not merely made
green.

Update `site/README.md` only if its route/test description changes; it should
say that the glossary is a native disclosure enhancement and that browser/
screen-reader/print checks are separate from the offline rendered suite.

### Patch 7 — offline validation and handoff

Run the focused local checks only after the above files agree:

```sh
cd site
npm run lint
npm test
```

For any site/deployment-surface change, run the repository smoke check from the
project instructions as appropriate. These checks must remain offline. No
deployment, hosting update, provider call, or publication is part of this
patch sequence.

## 8. Acceptance tests

These are proposed acceptance tests, not tests run by this audit.

### A. Route truth and cold comprehension

1. Render `/` and assert that route links target unique existing IDs
   `#stop-60-90`, `#stop-5`, and `#stop-12-15` (or an explicitly documented
   cross-route target). Assert each marker has a visible label, heading, and
   `aria-labelledby` relationship.
2. Extract visible text for the first stop, excluding rail, status chrome, and
   compact table numerals. It must contain the nine-report failure, `09`, `01`,
   `00`, `HOLD`, and the sentence-level meaning that zero is not rejection. It
   must not require a glossary activation and must not contain F0/F1/F2, T1,
   N=300, tokenizer, denominator, leakage, or construct-validity shorthand.
3. Time five owner-proxy readers at normal attentive reading speed with no
   glossary or project context. After the first stop, at least 4/5 must say
   that repeated reports may share one path, the reports/relationship record
   should be preserved, and the broad claim is held rather than accepted or
   rejected. Automatic failures include “the articles are false,” “the tool is
   rejected,” “the model discovered independence,” or “nine sources prove
   validation.”
4. At `#stop-5`, at least 4/5 readers must answer the five reader-contract
   questions: the problem is false corroboration; nine reports may share one
   path; the responsibility makes the pre-answer route inspectable; a person
   can hold/correct it; and no empirical validation exists.
5. At `#stop-12-15`, time the public route at 220–260 wpm and confirm the
   visible content, not optional deeper records, falls within the advertised
   12–15-minute range. The marker must follow loops, use boundary, objections,
   and the proposed-comparison bridge, not merely precede them.

### B. Progressive disclosure, no-JS, and print

1. With JavaScript disabled or hydration blocked, the first route still exposes
   the plain scene, compact receipt, count meaning, relation states, and human
   next action. Clicking a native summary opens the definition/example/boundary.
2. With all disclosures closed, the page remains understandable. The full
   technical glossary is supplemental; no critical meaning lives only in an
   `aria-label`, color, CSS arrangement, image, or client-created node.
3. In print preview from a fresh, all-closed page, all Term definitions,
   examples, and boundaries appear in flow; close controls and shadows do not.
   The three visual captions/text equivalents, receipt counts, `UNKNOWN`,
   `INSUFFICIENT`, and `HOLD` remain legible.
4. Print the home, Explore, Lab, and Sources routes. Receipt/condition/state
   tables retain headers/captions and fit the print content area; only the
   intentionally contained screen-scroll behavior changes to visible print.

### C. Keyboard, screen-reader, and touch semantics

1. Keyboard only: Tab reaches each summary in source order; Enter/Space opens
   and closes it; the expanded/collapsed state is announced; the panel heading,
   definition, example, boundary, and close control are reachable; Escape
   closes only the active panel and restores focus to its summary.
2. Screen reader: the explanation is announced/navigable as an optional
   nonmodal disclosure, not a dialog. There is no `aria-modal` and no claim of
   focus containment. The panel’s labelled heading and description are
   associated once, and the close button has a useful name. No content is
   announced twice because an `aria-label` suppresses visible children.
3. Touch: at 320px and 390px, trigger and close targets are reliably activatable
   without hover; the fixed panel respects safe-area insets, scrolls internally
   when long, and does not make the page or only copy of the sentence
   unreachable.
4. Focus regression: open a term, open a second term, press Escape, activate a
   close button, and navigate to the next route link. Focus must never jump to
   an unrelated earlier/later trigger, and no two panels may have ambiguous
   duplicate IDs.
5. Inspect the DOM with every panel closed. Every `aria-controls`/labelledby/
   describedby reference must resolve, or the native details pattern must make
   the relationship unnecessary. Term IDs must be unique across all rendered
   instances, not just the closed server snapshot.

### D. Collision, responsive, motion, and visual integrity

1. Open terms whose triggers are at the left, center, and right edges of a
   1440px route, then resize/scroll. The panel remains fully within viewport
   insets and does not clip under an ancestor. Repeat at 720px and 200% zoom.
2. Check 320px, 390px, 720px, and 1440px widths. `document.documentElement`
   has no horizontal page overflow; only labelled data regions scroll.
3. Enable `prefers-reduced-motion: reduce`, forced colors, grayscale, and
   images disabled. No meaning, status, or focus visibility depends on motion,
   color, border shape, image, or arrow.
4. Check that the three microvisuals are one-column and text-complete on narrow
   screens, retain headings/captions in print, and do not add an unbounded
   visual gallery or alter the v13 historical image.
5. Verify the existing visual voice: warm paper/ink, serif body, mono labels,
   restrained accents, and thin rules remain; the receipt stays the primary
   explanatory object rather than being replaced by a dashboard-like map.

### E. Content, status, and manuscript/site agreement

1. Compare the selected manuscript and rendered site for exact first-route
   values, route labels, plain relation-state wording, status sentence, and
   stop order. A source-only pass or site-only pass fails this test.
2. Search the public route for unsupported implications. It must not say or
   imply that the framework improves decisions, discovers provenance,
   establishes independence, validates a product, or reports a study result.
3. Confirm `N=300` is labelled provisional fictional planning wherever shown;
   F0/F1/F2 are introduced as three versions of one task; T1 is optional and
   descriptive; and the negative/harmful/shortcut commitment remains visible.
4. Confirm Sources uses a heterogeneous-status phrase such as “Selected
   precedents and status notes,” links the full ledger, and does not call all
   standards, published works, datasets, and unreviewed preprints “primary and
   official.”
5. Confirm the v13 image hash/byte identity and historical caption/alt/text
   transcript remain unchanged. Confirm the E2 image remains explanatory only.

## Accept / revise / reject / defer matrix

| Surface or recommendation | Decision | Reason and acceptance condition |
| --- | --- | --- |
| Receipt-first architecture; preserve observations while changing the route | **ACCEPT** | It is the clearest mechanism and strongest visual voice. Keep `09 / 01 / 00 / HOLD`, `UNKNOWN`, the human next step, and the text receipt. |
| Current `Start here · 60–90 seconds` target `#takeaway` | **REVISE** | It does not contain the receipt consequence. Replace with the explicit first stop and cold-reader/timing tests above. |
| Current `Continue · about 5 minutes` target `#essay` | **REVISE** | It has no stop boundary and starts with too much ledger/detail. End the public essential route at the three-question correction invariant. |
| Add a truthful `12–15 minutes` public stop | **ACCEPT** | Required by the Round 2 convergence direction, provided loops/use boundary/objections/research bridge actually occur before the marker and the timed budget passes. |
| Current `Term` as `role="dialog"` without modal behavior | **REJECT** | It is a modal/nonmodal mismatch with missing focus, description, and target semantics. Do not ship this hybrid. |
| Native details-first nonmodal glossary disclosure | **ACCEPT** | Best fit for optional explanations, no-JS, print, touch, and reading-flow preservation. Must implement scoped Escape, stable associations, unique IDs, and collision-safe enhancement. |
| A true modal dialog alternative | **DEFER** | Possible only if the owner wants an interruptive interaction and the full modal focus/inert/ARIA/no-JS contract is implemented and tested. |
| Three CSS-native visuals: origin count, trace/unknown/hold, F0/F1/F2 | **ACCEPT** | Each has one conceptual job, live text equivalence, a caption, and no result/provenance implication. Use at most three total. |
| Generic `evidence → judgment → human action` flow visual | **REJECT** for v15.2 integration | It adds little beyond prose and risks generic visual cadence. Fold its words into the trace/unknown/hold visual if useful. |
| 300-dot/sample-size/negative-result visual | **DEFER** to Lab-only replacement choice | It can resemble observed participants/results and is the densest prototype. Keep the plain sentence and outcome rails first. |
| Existing E2 `nine-mentions-one-origin.jpg` | **ACCEPT** with current boundary | Keep as an explanatory figure after the receipt, never as a count/status surface or evidence. |
| Historical v13 map and transcript | **ACCEPT unchanged** | Preserve bytes, hash, caption, alt, transcript, and historical-only boundary; do not redraw it as v15.2 topology. |
| Full C01–C11, B1/C1, exact relation codes, Lab gates, and source-status ledger | **ACCEPT in deeper routes** | These remain inspectable in Explore/Lab/Sources but must not inflate the first-minute or five-minute route. |
| Sources heading “Selected primary and official references” | **REVISE** | Current source inventory is heterogeneous. Use a status-aware phrase and keep the detailed ledger. |
| Current rendered test that requires `role="dialog"` | **REJECT/REWRITE** | It codifies the broken contract and does not exercise runtime focus, no-JS, collision, or print behavior. Replace with tests for the selected disclosure semantics. |
| Version promotion from v15.1 to v15.2 | **DEFER until integration** | Do not mix v15.1 chrome with v15.2 manuscript/site copy. Promote metadata, visible labels, and tests together after owner selection. |
| Final owner-ready sign-off | **DEFER** | It requires offline lint/build/render checks plus browser keyboard/touch/screen-reader/print verification and manuscript/site comparison. |

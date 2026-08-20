# Loop 2 — opportunity and interface specification

**Status:** research/design memo · 2026-08-18
**Scope:** one bounded reader-facing specimen for v14/v15; no core-file edit, image generation, publication, or deployment
**Target artifact:** `research/overnight/rounds/09_LOOP2_OPPORTUNITY_AND_INTERFACE_SPEC.md`

> **Loop 3 implementation reconciliation (2026-08-18).** This memo is preserved as the proposal record. Its pre-implementation observations about masthead order, a five-versus-nine contradiction, and the absence of a receipt are superseded. The canonical implementation is receipt `ORIGIN-EX-01` version `0.2` in `site/app/page.tsx`: all example counts are nine; the deterministic receipt precedes the questions; H1 was removed from the final handoff surface after the last reader/design review; and the human disposition is `HOLD · VERIFY ANOTHER ORIGIN RELATION`. The historical specimen below is not the implementation receipt.

## Answer first

The best new opportunity is a small, deterministic **origin-accounting route receipt**: a semantic HTML specimen that makes one evidence packet inspectable as *nine observations, one known common origin, and no independently supporting origin established in this packet*. It should sit near the existing “nine positive articles. One launch announcement.” example and carry the exact count, relation type, claim state, unknown rule, and human disposition in live text.

This is a useful addition without enlarging the first-paper claim because it does not pretend to discover provenance, establish real-world independence, route a live request, or improve a human decision. It is an interface contract for the same narrow distinction that the proposed study tests under an oracle cue: `dependent`, `independent-as-stipulated`, or `unknown`. The first paper remains a frozen, fictional-bundle model-use benchmark comparing citation-only, an explicit origin-counting rule, and that rule plus typed relation cues. The receipt is a comprehension specimen and a testable design hypothesis, not a study result.

The specimen should be deterministic HTML with a table/list and explicit labels. It should not be a raster, a graph with arrowheads, a funnel, a central gate, a ranked “confidence” display, or a route animation. A receipt records what is known about a packet and what a person may do next; it does not depict a mandatory sequence.

**H1 disposition after Loop 3: omit from the final handoff surface.** The H1 image remains preserved in the candidate/selection archive, but its wide lanes, central aperture, and calmer right-hand field continued to invite a one-way filtering interpretation. H2 and H3 retain similar topology/status risks. The deterministic receipt is the first exact visual object explaining the nine/one distinction; E2 remains the worked-example illustration.

## Epistemic labels and reading boundary

This memo uses the following labels so that a persuasive interface proposal is not mistaken for evidence of performance:

- **[S] Sourced/observed:** directly read from the current repository, the archived v13 manifest, the visual-asset plan/ledger, the first-paper protocol, or a cited standard/paper.
- **[I] Inference:** a reasoned implication of those materials; useful, but not directly measured here.
- **[H] Hypothesis:** a claim the proposed reader test could falsify.
- **[DJ] Design judgment:** a recommendation about hierarchy, wording, topology, or implementation.

Nothing in this memo establishes that a receipt improves model accuracy, human decisions, trust, retrieval quality, provenance discovery, or organizational outcomes.

## 1. What I re-read and what is materially current

### Current v14 source

**[S · superseded observation]** At the time of this Loop 2 memo, `site/app/page.tsx` had this relevant order in the masthead:

1. title, dek, and technical definition;
2. the working proposition (“Make the judgment before generation visible”);
3. the full-width H1 editorial figure;
4. the two reading-path cards.

The Loop 1 memo warned about a hero appearing before the proposition. That exact DOM-order warning is now stale, but its anchoring concern remains: the H1 is still the first large visual object after the proposition and before the five-minute example. Its colored lanes and aperture can supply an implicit “what the system does” answer before the reader encounters the exact origin-accounting example.

**[S]** The current H1 alt says, in substance, that it is an illustrative field of evidence fragments, provenance trails, inspection frames, and a bounded context area, and that paths/colors do not encode a required route, family, status, correctness, or result. Its visible caption similarly says that it is a material metaphor and that paths/colors do not encode sequence, family, status, truth, or an empirical result. This is materially safer than the earlier ledger wording that described fragments “passing through” an aperture. It does not, however, change the visual topology a sighted reader may infer.

**[S]** The current map, loop figure, component records, worked-example six-step sequence, legend, and first-paper panel remain live HTML/text. The current architecture therefore already provides the right semantic division: exact relations and claims in HTML; editorial imagery only as optional atmosphere or a low-stakes entry cue.

**[S · resolved in Loop 3]** The Loop 2 page had a five-versus-nine contradiction. The canonical source, deterministic receipt, illustration caption, worked-example steps, and final result now all use a self-consistent **fictional nine-row bundle**. Fresh PDF and responsive artifacts—not this memo—must verify the rendered correction.

### Visual asset plan and ledger

**[S]** `reports/V14_VISUAL_ASSET_EXPERIMENT_PLAN.md` explicitly makes HTML authoritative for labels, sequence, component count, evidence status, citations, and causal relationships. It permits at most one hero and one worked-example image, allows using none, and requires captions/alt text to say that retained images are illustrations rather than evidence or system specifications. `assets/imagegen/IMAGE_SELECTION_LEDGER.md` records the local editorial decision, not reader evidence.

**[S]** The production H1 derivative is `site/public/images/context-before-answer.jpg` (1672 × 941; SHA-256 `59e0f6908e48e0c4cce2d5e247ce344cf41c77aca8b9d87a6c4fad04a1119ad7`). The ledger scores it 27/28, but the Loop 1 independent red-team reading scores its non-misleading structure lower because the visible lane/aperture grammar resembles a filter. The production worked image is `site/public/images/nine-mentions-one-origin.jpg` (1536 × 1024; SHA-256 `88222893a08a52bbca3f1d855aaa575827c829b09766d743a5db931930a3e325`), and is the strongest current editorial image for the concrete example, subject to count/crop checks. The exact v13 image remains a separate historical role.

### v13 anchor

**[S]** `archive/v13/LIVE_SITE_REFERENCE_MANIFEST.json` records the recovered v13 diagram as the exact hash-verified asset `archive/v13/pattern-recognition-diagram-v12.png`, 1024 × 1536, SHA-256 `8a8204a05e993e84f2bd9037c59b7beb2ab6b4bca89304e299f66b3961f203ae`. It also records that the original standalone HTML is unavailable and that the rendered DOM snapshot is a reference capture, not the original source. The current v14 page labels the image “Historical reference · v13 · not the v14 system map,” links the full-resolution copy, and offers a text summary.

The manifest and current boundary treatment are strong. The remaining risk is visual authority: a large portrait with a central hub and seven-step strip can still be remembered as the current system after the caption is forgotten. The route receipt should therefore establish v14’s relation grammar before the reader encounters the archival image. It must not use the v13 hub or its seven-step strip as a visual template for the receipt.

### First-paper boundary

**[S]** `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V0.md` defines the narrowest current study as an oracle-cue use test. It asks whether a frozen model, given the same evidence and explicit relation cues (`dependent`, `independent_as_stipulated`, `unknown`), reduces false corroboration beyond a rule-only condition while retaining valid-origin recall. It explicitly does not test provenance discovery, real-world independence, retrieval, human decisions, routing, memory, enterprise use, or the complete framework. The permitted positive claim is limited to newly authored fictional bundles with stipulated provenance graphs.

**[I]** The route receipt is the best interface bridge because it exposes exactly the relation distinction the protocol can test, while keeping all untested capabilities visibly outside the boundary. It should not introduce an additional “confidence score,” source-quality ranking, automatic gate, or real-world provenance claim.

## 2. The bounded opportunity: make origin accounting inspectable

### The insight

**[I]** The site currently explains “repetition is not independence” as prose, an editorial image, and a six-step example. The missing bridge is a small object that lets a reader point to the same packet and answer four different questions without conflating them:

1. How many observation records are present?
2. How many documented origin clusters do those records represent?
3. How many independently supporting origins have actually been established for the claim?
4. What remains unknown, and what may a person do next?

The route receipt makes those quantities co-present but not visually causal. This is the opportunity: **replace an implied path with a typed record of relationships and a reversible human disposition.**

### Why this does not broaden the first paper

The receipt may show a fictional bundle with a stipulated relation, but it must carry a boundary note:

> This specimen shows how a typed relation can be recorded and read. It does not discover provenance, prove independence, establish truth, or report a benchmark result.

The receipt can be described as the *reader-facing rendering of the typed-cue condition in miniature*, not as evidence that the cue works. The first-paper study remains the only proposed efficacy test and remains model- and corpus-specific if run. A reader study of the receipt is a separate formative comprehension test.

### Proposed placement

**[DJ]** Add the receipt in the five-minute overview immediately after the concrete preview and before the six-question grid. This is where a reader has just read “Nine positive articles can still trace to one launch announcement,” but has not yet been asked to absorb the full family map or historical v13 anchor.

Recommended reading order:

1. title/definition and working proposition;
2. route cards;
3. five-minute problem statement and concrete preview;
4. **route receipt: exact nine/one relation specimen**;
5. question grid and distinction contract;
6. v13 historical continuity anchor;
7. current six-family map and loops;
8. worked example with E2 image and six ordered steps.

Demote the H1 figure out of the role immediately preceding the route cards. If retained, place it after the receipt as a short “material metaphor” interlude with the current non-evidence caption. If the site’s information architecture requires the figure to stay in the masthead, reduce its visual weight and keep the route receipt as the first exact artifact in the five-minute path. The no-image option remains valid.

## 3. Specimen design: a receipt, not a pipeline

### Topology rule

**[DJ]** The receipt should use grouped records, field labels, and a count summary. It should contain no arrowheads, no left-to-right lane, no central gate, no “admitted/withheld” output columns, no color gradient from bad to good, and no bright right-hand “context” field. A thin border or brace may visually group rows under one origin, but the relation must be stated in text. If a connector is used for editorial polish, it is decorative (`aria-hidden="true"`) and cannot be the only indication of a relation.

Suggested visual grammar:

```text
ILLUSTRATIVE ROUTE RECEIPT · ORIGIN ACCOUNTING · NO VERDICT
Receipt ORIGIN-EX-01 · fictional bundle · version 0.1

Decision in view       sandbox pilot · 90 minutes · no production data
Claim under review     “The tool is broadly validated.”
Packet state            INSUFFICIENT · repetition is not independent support

COUNT SNAPSHOT
Observations under review                         09
Known common-origin clusters for those records    01
Independent supporting origins established        00
Separate roots shown for comparison              02 · support not assessed

OBSERVATION LEDGER · unordered records
┌ O01  report observation  · Origin A · dependent · repeats launch announcement
├ O02  report observation  · Origin A · dependent · repeats launch announcement
├ O03  report observation  · Origin A · dependent · repeats launch announcement
│ ...
└ O09  report observation  · Origin A · dependent · repeats launch announcement

SEPARATE ROOTS SHOWN FOR CONTRAST
B1  separate root · illustrative · claim support not assessed
C1  separate root · illustrative · claim support not assessed

HUMAN DISPOSITION
HOLD · inspect independently authored evidence before changing the claim state
No automatic admission, rejection, or truth verdict.
```

The vertical brace is only a visual grouping cue; in the implementation, the row’s `Origin A · dependent` text and the count summary carry the relation. There is no order among O01–O09. The “receipt” metaphor means “record of the current packet,” not “a sequence through which evidence must pass.”

### Exact visible hierarchy and microcopy

The following is the proposed content contract. Punctuation and capitalization are intentional: labels should be short enough to survive mobile and print, while the boundary sentences remain ordinary prose.

#### 1. Receipt header

- Eyebrow: `ILLUSTRATIVE ROUTE RECEIPT · ORIGIN ACCOUNTING · NO VERDICT`
- Title: `Nine observations can still represent one origin.`
- Boundary note: `A receipt records relationships and a human disposition. It does not depict a required workflow, discover provenance, or establish truth.`
- Metadata line: `Receipt ORIGIN-EX-01 · fictional bundle · version 0.1 · no live data`

#### 2. Decision frame

- `Decision in view` — `Sandbox pilot of a data-migration tool`
- `Permission and budget` — `Sandbox only · 90 minutes of research · no production data`
- `Packet state` — `HOLD · inspect independent evidence`
- `State meaning` — `The packet is insufficient for a broad validation claim. No automatic action is taken.`

The words “HOLD” and “INSUFFICIENT” must appear as text, not only as a colored pill. “HOLD” is a human disposition in this fictional packet, not a gate that every evidence item must pass.

#### 3. Claim under review

- Label: `Claim under review`
- Claim: `“The tool is broadly validated.”`
- State: `INSUFFICIENT · nine mentions do not become nine independent confirmations.`

The claim is illustrative. Do not cite the image, the receipt, or the current page as evidence for it.

#### 4. Count snapshot

- `Observations under review` — `09`
- `Known common-origin clusters for those records` — `01`
- `Independent supporting origins established for this claim` — `00`
- `Separate roots shown for comparison` — `02 · illustrative; claim support not assessed`
- Note: `If an origin relation is unknown, preserve UNKNOWN. Do not move it into the independent total.`

This wording deliberately separates “known common-origin clusters for those records” from “independent supporting origins established for this claim.” A source can be separately rooted and still fail to support the claim; a common origin can be credible and still not provide independent corroboration.

#### 5. Observation ledger

- Section label: `OBSERVATION LEDGER · NINE UNORDERED RECORDS`
- Note: `These rows preserve nine observations. Their order is not a workflow or a confidence ranking.`
- Each row: `O## · Report observation · Origin A · DEPENDENT · repeats the launch announcement; not independent support`

The nine rows are `O01` through `O09`. The fictional bundle must keep them visibly countable; do not collapse them into one “source” card or replace them with nine decorative dots.

#### 6. Relation key

- `DEPENDENT` — `Traceable to an existing artifact. Preserve the observation; do not count it as an independent supporting origin.`
- `INDEPENDENT-AS-STIPULATED` — `Separate root declared by this illustration/benchmark. This is a supplied relation, not provenance discovery.`
- `UNKNOWN` — `The relation is not established. Preserve the unknown; do not treat it as dependent or independent.`

The public-facing copy may use “separate root” alongside the benchmark token `INDEPENDENT-AS-STIPULATED`; it should not use unqualified “independent” as a factual finding.

#### 7. Separate roots shown for comparison

- Section label: `SEPARATE ROOTS SHOWN FOR CONTRAST`
- `B1 · Separate root · illustrative · claim support not assessed`
- `C1 · Separate root · illustrative · claim support not assessed`
- Note: `These two roots show what a separate origin record looks like. They are not a measured result and are not counted as support for the claim in this packet.`

Keeping B1/C1 outside the nine-row ledger prevents a reader from adding them to the “nine positive articles” count. It also avoids the visual implication that every separate root automatically corroborates the claim.

#### 8. Human disposition

- Heading: `HUMAN DISPOSITION`
- Historical proposal state: `HOLD · SEEK INDEPENDENT TEST`  
  Canonical Loop 3 state: `HOLD · VERIFY ANOTHER ORIGIN RELATION`
- Body: `Inspect the originating announcement, look for a separately authored benchmark, and preserve the current claim state until a reviewer records a reasoned change.`
- Guardrail: `No automatic admission, rejection, or truth verdict. A reviewer may correct this receipt; the fictional observations remain preserved.`

#### 9. Receipt footer

- `Illustrative only · not a reported dataset · not a provenance audit · not a system runtime`
- `No image is required to interpret the counts, relation types, or disposition.`

### What the specimen must not say

**[DJ]** Avoid the following microcopy because each one smuggles in a larger claim:

- `9 sources became 1 source` — observations and origins are not interchangeable, and “became” implies transformation.
- `9 articles collapsed into 1` — suggests deletion or devaluation of observations.
- `The gate admits only trusted evidence` — conflates authority, support, permission, and truth.
- `Independent evidence` for B1/C1 without the qualifier `as stipulated` or `illustrative` — implies a real-world provenance finding.
- `Confidence: 0` — turns origin accounting into a truth probability.
- `Validated`, `safe`, `approved`, or `rejected` as a decorative color state — exceeds the fictional packet.
- `Next step` in a numbered route — makes the receipt a pipeline. Use `Human disposition` and a reversible action note.

## 4. Exact semantic HTML and ARIA behavior

The route receipt is a data-bearing explanatory object, not a picture. Use native HTML first; add ARIA only to name regions and describe a scroll container. The following is a specimen DOM contract, not a request to edit `site/app/page.tsx` in this loop.

```html
<section
  class="route-receipt"
  id="origin-receipt"
  aria-labelledby="origin-receipt-title"
  aria-describedby="origin-receipt-boundary"
>
  <header class="route-receipt__header">
    <p class="kicker">Illustrative route receipt · origin accounting · no verdict</p>
    <h2 id="origin-receipt-title">Nine observations can still represent one origin.</h2>
    <p id="origin-receipt-boundary">
      A receipt records relationships and a human disposition. It does not depict a
      required workflow, discover provenance, or establish truth.
    </p>
    <p class="route-receipt__meta">Receipt ORIGIN-EX-01 · fictional bundle · version 0.1 · no live data</p>
  </header>

  <dl class="route-receipt__frame" aria-label="Decision frame">
    <div><dt>Decision in view</dt><dd>Sandbox pilot of a data-migration tool</dd></div>
    <div><dt>Permission and budget</dt><dd>Sandbox only · 90 minutes of research · no production data</dd></div>
    <div><dt>Packet state</dt><dd>HOLD · inspect independent evidence</dd></div>
    <div><dt>State meaning</dt><dd>The packet is insufficient for a broad validation claim. No automatic action is taken.</dd></div>
  </dl>

  <section aria-labelledby="origin-receipt-claim-title">
    <h3 id="origin-receipt-claim-title">Claim under review</h3>
    <p class="route-receipt__claim">“The tool is broadly validated.”</p>
    <p><strong>Packet state:</strong> INSUFFICIENT · nine mentions do not become nine independent confirmations.</p>
  </section>

  <section aria-labelledby="origin-receipt-count-title">
    <h3 id="origin-receipt-count-title">Count snapshot</h3>
    <dl class="route-receipt__counts">
      <div><dt>Observations under review</dt><dd>09</dd></div>
      <div><dt>Known common-origin clusters for those records</dt><dd>01</dd></div>
      <div><dt>Independent supporting origins established for this claim</dt><dd>00</dd></div>
      <div><dt>Separate roots shown for comparison</dt><dd>02 · illustrative; support not assessed</dd></div>
    </dl>
    <p class="route-receipt__unknown-note">
      If an origin relation is unknown, preserve UNKNOWN. Do not move it into the independent total.
    </p>
  </section>

  <section aria-labelledby="origin-receipt-ledger-title" aria-describedby="origin-receipt-ledger-note">
    <h3 id="origin-receipt-ledger-title">Observation ledger · nine unordered records</h3>
    <p id="origin-receipt-ledger-note">
      These rows preserve nine observations. Their order is not a workflow or a confidence ranking.
    </p>
    <div
      class="route-receipt__table-scroll"
      role="region"
      aria-labelledby="origin-receipt-ledger-title"
      aria-describedby="origin-receipt-scroll-note"
      tabindex="0"
    >
      <p id="origin-receipt-scroll-note" class="scroll-hint">
        On narrow screens, scroll this data table horizontally; the page itself does not scroll sideways.
      </p>
      <table>
        <caption>Typed relation ledger for the nine illustrative observations</caption>
        <thead>
          <tr>
            <th scope="col">Record</th>
            <th scope="col">Record kind</th>
            <th scope="col">Origin relation</th>
            <th scope="col">What this counts as</th>
          </tr>
        </thead>
        <tbody>
          <tr><th scope="row">O01</th><td>Report observation</td><td>Origin A · DEPENDENT</td><td>Repeats the launch announcement; not independent support.</td></tr>
          <tr><th scope="row">O02</th><td>Report observation</td><td>Origin A · DEPENDENT</td><td>Repeats the launch announcement; not independent support.</td></tr>
          <tr><th scope="row">O03</th><td>Report observation</td><td>Origin A · DEPENDENT</td><td>Repeats the launch announcement; not independent support.</td></tr>
          <tr><th scope="row">O04</th><td>Report observation</td><td>Origin A · DEPENDENT</td><td>Repeats the launch announcement; not independent support.</td></tr>
          <tr><th scope="row">O05</th><td>Report observation</td><td>Origin A · DEPENDENT</td><td>Repeats the launch announcement; not independent support.</td></tr>
          <tr><th scope="row">O06</th><td>Report observation</td><td>Origin A · DEPENDENT</td><td>Repeats the launch announcement; not independent support.</td></tr>
          <tr><th scope="row">O07</th><td>Report observation</td><td>Origin A · DEPENDENT</td><td>Repeats the launch announcement; not independent support.</td></tr>
          <tr><th scope="row">O08</th><td>Report observation</td><td>Origin A · DEPENDENT</td><td>Repeats the launch announcement; not independent support.</td></tr>
          <tr><th scope="row">O09</th><td>Report observation</td><td>Origin A · DEPENDENT</td><td>Repeats the launch announcement; not independent support.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section aria-labelledby="origin-receipt-key-title">
    <h3 id="origin-receipt-key-title">Origin relation key</h3>
    <dl class="route-receipt__key">
      <div><dt>DEPENDENT</dt><dd>Traceable to an existing artifact. Preserve the observation; do not count it as an independent supporting origin.</dd></div>
      <div><dt>INDEPENDENT-AS-STIPULATED</dt><dd>Separate root declared by this illustration or benchmark. This is a supplied relation, not provenance discovery.</dd></div>
      <div><dt>UNKNOWN</dt><dd>The relation is not established. Preserve the unknown; do not treat it as dependent or independent.</dd></div>
    </dl>
  </section>

  <section aria-labelledby="origin-receipt-contrast-title">
    <h3 id="origin-receipt-contrast-title">Separate roots shown for contrast</h3>
    <ul>
      <li><strong>B1 · Separate root · illustrative</strong> — claim support not assessed.</li>
      <li><strong>C1 · Separate root · illustrative</strong> — claim support not assessed.</li>
    </ul>
    <p>These roots are not a measured result and are not counted as support for the claim in this packet.</p>
  </section>

  <section aria-labelledby="origin-receipt-disposition-title">
    <h3 id="origin-receipt-disposition-title">Human disposition</h3>
    <p><strong>HOLD · VERIFY ANOTHER ORIGIN RELATION</strong></p>
    <p>Inspect the originating announcement, look for a separately authored benchmark, and preserve the current claim state until a reviewer records a reasoned change.</p>
    <p>No automatic admission, rejection, or truth verdict. A reviewer may correct this receipt; the fictional observations remain preserved.</p>
  </section>

  <footer class="route-receipt__footer">
    Illustrative only · not a reported dataset · not a provenance audit · not a system runtime.
    No image is required to interpret the counts, relation types, or disposition.
  </footer>
</section>
```

### DOM and ARIA requirements

1. **Use one page-level H1 only.** The receipt begins with an `h2` when inserted under the five-minute section. Its internal blocks use `h3`; do not create a second H1 for “route receipt.”
2. **Use native structure for relationships.** The frame and count snapshot are definition lists. The nine records are a real data table with a caption, column headers, row headers, and visible text. This keeps “record ↔ relation ↔ interpretation” programmatically available when layout changes. This follows the intent of WCAG 2.2 SC 1.3.1 and the HTML table model, not a custom `div` graph.
3. **Keep count-bearing content outside disclosure.** Do not hide O01–O09, the count snapshot, or the relation key inside collapsed cards. If later audit fields need progressive disclosure, use native `<details><summary>` and keep the summary and `aria-expanded` behavior native. The WAI-ARIA APG disclosure pattern specifies a keyboard-operable button with expanded/collapsed state; no custom disclosure is needed for this static specimen.
4. **Do not use `role="status"` or `aria-live` for a static receipt.** `HOLD`, `INSUFFICIENT`, and `UNKNOWN` are content, not asynchronous updates. Announcing them as live status could make a reader think the page is actively routing evidence. If a future product changes the state, update a clearly labelled record with an explicit user action and a separately evaluated interaction model.
5. **Do not rely on color, position, or border weight.** The words `DEPENDENT`, `INDEPENDENT-AS-STIPULATED`, `UNKNOWN`, `HOLD`, and `INSUFFICIENT` must be present. Color/pattern may support scanning but cannot carry status or relation. Use the visible relation key on the same page.
6. **Keep focus order equal to reading order.** The only extra focus target in the static specimen is the horizontally scrollable table region. Its focusable region should have a visible focus ring, a short scroll hint, and no keyboard trap. There are no draggable nodes, hover-only details, or hidden controls.
7. **No image alternative is needed for the receipt itself.** If the H1 or E2 image remains adjacent, keep its `img` alt and visible caption separate from the receipt. Do not make the image’s alt the only explanation of the table. If a future SVG adds grouping lines, mark decorative lines `aria-hidden="true"` and retain the same row/definition-list text.
8. **Preserve the fictional boundary in the accessible name/description.** The receipt heading, boundary paragraph, table caption, and footer should be read in ordinary order. Do not put “illustrative” only in a visual badge that a screen-reader user might skip.
9. **Do not make the table a pseudo-sequence.** Use `<tbody>` and unordered row semantics; the records are deliberately `O01`–`O09` identifiers, not steps. If a later implementation needs chronological order, add an explicit date column and state that order separately; do not infer it from row position.

### Why a table instead of a graph

**[E]** WCAG’s information-and-relationships guidance identifies table markup, captions, and scoped headers as ways to preserve relationships when presentation changes ([W3C WCAG 2.2, SC 1.3.1](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html)). The HTML standard provides the native table semantics ([WHATWG HTML, tables](https://html.spec.whatwg.org/multipage/tables.html)).

**[E]** Ghoniem, Fekete, and Castagliola’s controlled graph-readability study found that visual graph size/crossing decisions affect readability and task performance, which supports keeping a nine-record relation ledger sparse and giving it a text/table alternative rather than adding a dense provenance graph ([Ghoniem, Fekete & Castagliola 2005, DOI 10.1057/palgrave.ivs.9500092](https://doi.org/10.1057/palgrave.ivs.9500092)). This does not prove that a table is superior for this audience; it motivates testing a low-decoding representation.

## 5. Responsive and print behavior

### Desktop (approximately 1440 px)

**[DJ]** Use a single outer receipt frame with a modest two-column grid only for the non-ordered decision frame and count snapshot. Keep the claim, ledger, relation key, separate roots, and disposition full-width so the visual hierarchy remains vertical and inspectable. The count snapshot should be a four-cell grid with explicit labels, not four color bars or a single “score.”

The table may use four columns at desktop. Keep the first column narrow, the relation column stable, and allow the “what this counts as” column to wrap. The nine rows must remain visibly countable in one glance. Do not add curved lines from rows to an origin card; repeated `Origin A · DEPENDENT` text is the robust relation.

### 390 px mobile and narrow reflow

- Collapse the outer grid to one column; retain the same DOM order.
- Stack the count snapshot as labelled cards or a one-column `<dl>`. Preserve the leading zero (`09`) so the count reads as a record, not a rating.
- Keep the table as a semantic table inside the labelled `.route-receipt__table-scroll` region. The region may scroll horizontally; the page must not. Do not CSS-rewrite the table as unrelated visual cards unless the same header/row relationships remain programmatically available.
- Use short row copy: `Report observation`, `Origin A · dependent`, `Not independent support`. The full explanation remains in the relation key and boundary note.
- Keep the table caption and scroll hint above the table. A user should not have to discover a hidden gesture to find O01–O09.
- Do not hide B1/C1 or the unknown rule below a viewport-only accordion. If progressive disclosure is added for audit fields, the summary must state that it is optional detail and the count/disposition must remain visible.
- Preserve at least 44 CSS pixels of touch target for any future `<details>` or link; the static receipt has no required controls.

**[H]** The receipt will be more robust on mobile than a graph/image because the critical relation is repeated as text and the record count is explicit. This must be checked at 390 × 844 and at 200% text zoom; it is not established by the current desktop source.

### Print/A4

- Keep the receipt’s header, boundary note, count snapshot, and first ledger rows together; avoid a page break between the receipt title and its count.
- Print all nine rows. Do not rely on a scroll container in print: set overflow visible and width 100% in the print stylesheet.
- Keep `caption`, relation key, separate-root note, and disposition on the same page as the table when practical. If pagination forces a split, repeat the table header and place the boundary/footer on the final page.
- Use black/white-safe text labels and borders; do not make the teal/coral/violet palette the only distinction. The “illustrative,” “not a result,” and “no image required” boundaries must print.
- Keep any retained H1/E2 images separate from the receipt’s semantics. Current CSS has moved toward `object-fit: contain` for print, which reduces silent cropping risk; a fresh PDF still needs inspection because pagination and caption adjacency are not verified by source alone.
- The v13 portrait remains an archival figure with its pre-image label and text summary. Do not place it beside the receipt in a way that makes the historical seven-step strip look like the receipt’s next step.

## 6. Image/no-image/text-only reader test

This is a formative interface test, not an efficacy experiment. It should extend the Loop 1 protocol after the current integrated page has fresh captures at 1440 × 900, 720 × 900, 390 × 844, and A4/print. It should not be reported as evidence for the first-paper F2-versus-F1 contrast.

### Conditions

Use a counterbalanced, between-/within-reader protocol with 6–8 independent readers who did not author the page or memos. Include at least one screen-reader or low-vision reader if feasible; record the assistive technology and do not treat one participant as a prevalence estimate.

1. **Current-image condition:** current H1 in its present position after the working proposition, current E2 image, v13 anchor, and the proposed receipt.
2. **Demoted-H1 condition:** receipt and live proposition appear before the H1; the H1 is a smaller editorial transition after the exact specimen; E2/v13 remain bounded.
3. **No-H1 condition:** remove the H1 entirely; retain the receipt, live map, E2 worked example, and v13 historical boundary.
4. **Text-only condition:** hide all production images, preserve headings, captions, alt-equivalent/live prose, the receipt, the v13 text summary, and the worked-example text. This condition tests whether image removal deletes any meaning that HTML is supposed to carry.

Do not show alternate candidate images, image-generation previews, or black UI chrome. Do not explain the intended interpretation before the first response. Counterbalance condition order so that a learned answer does not contaminate the H1 decision.

### Tasks

Ask the reader to answer aloud or in writing before correction. Use the exact prompts below.

#### Receipt comprehension

1. “What does the number 09 count?” Expected: nine observation records, not nine sources, nine origins, or a confidence score.
2. “What does the number 01 count?” Expected: one known common-origin cluster for those nine records.
3. “How many independently supporting origins are established for the claim in this packet?” Expected: zero; B1/C1 are comparison roots whose claim support is not assessed.
4. “What should happen to an origin relation marked UNKNOWN?” Expected: preserve unknown; do not count it as dependent or independent.
5. “Does this receipt show a mandatory pipeline?” Expected: no; it records relationships and a human disposition, not a required sequence.
6. “What is the current claim state and who can change it?” Expected: insufficient/hold; a reviewer can record a reasoned correction, with no automatic truth or approval verdict.
7. “What would you inspect next?” Acceptable: originating announcement, separately authored benchmark, or another bounded evidence check; not “the gate will admit it” or “the system approves it.”

#### Cross-surface comprehension

8. “What is the role of the H1, if present?” Expected: optional editorial/material metaphor; not the v14 topology or an empirical result.
9. “What is the role of the v13 image?” Expected: historical reference, not the current v14 system map; the diagram’s exact bytes are preserved, while the original standalone HTML is unavailable.
10. “What does the worked-example image add, and what does it not prove?” Expected: an intuitive common-origin cue; it does not prove a reported dataset, real provenance audit, or that the reports are false.

### Surfaces and measures

For each assigned viewport, record:

- correct/incorrect response for the ten propositions;
- first spontaneous metaphor (`grouped records`, `receipt`, `pipeline`, `funnel`, `gatekeeper`, `graph`, or other);
- confidence (1–5), response time, and perceived effort (1–5);
- whether a crop or table scroll hid O01–O09, B1/C1, the unknown rule, the historical boundary, or the disposition;
- whether a screen-reader/keyboard reader hears “illustrative/no verdict” before relation labels;
- whether any color, border, node, or image position is treated as status, truth, authority, or approval.

### Formative gates

Reuse the Loop 1 thresholds, narrowed to the new specimen:

- At least 6 of 8 readers should answer at least 8 of 10 propositions correctly in the image condition; record the exact denominator if fewer than eight participate.
- No more than 1 of 8 readers should make a critical topology error on any one item: `09 = nine origins`, `01 = one source record`, `H1 = pipeline`, `v13 = current map`, or `HOLD = automatic rejection`.
- The current-image condition should not reduce critical-item accuracy by more than 10 percentage points versus the no-H1 condition.
- The text-only condition should preserve the 09/01/00 distinction, the unknown rule, the no-pipeline boundary, the claim state, and the human disposition. If it fails, repair live semantics before adding visual detail.
- At least 6 of 8 readers should spontaneously identify a human correction/hold/clarify possibility without prompting.
- At 390 px and print, no more than 1 of 8 readers should lose the nine-row count, one-origin grouping, or separate-root boundary because of crop, scroll, pagination, or caption separation.

These are decision gates for a local design iteration, not statistical claims about readers or evidence-system performance. A confident but wrong `nine origins` answer is more concerning than an explicit “I do not know.”

### Stop and revision rules

- **If readers count origins instead of observations:** shorten the count labels and put the typed relation in every row; do not add a bigger image.
- **If readers treat Origin A as proof that reports are false:** add/retain “common origin does not make a report false” beside the ledger and distinguish observation preservation from support counting.
- **If readers treat B1/C1 as claim support:** move them farther from the count snapshot and repeat “support not assessed”; do not use a green/positive color.
- **If readers call the receipt a pipeline:** remove any remaining line/arrow, reorder, or “next step” phrasing; keep grouped fields and a human disposition.
- **If H1 increases pipeline/gatekeeper errors:** demote it further or remove it. Do not attempt to repair a topology error with a longer caption.
- **If the text-only condition fails:** treat the HTML contract as incomplete; the image is not allowed to compensate.
- **If the current example’s five/nine contradiction remains:** stop implementation and freeze one fictional bundle count before testing.

## 7. Prioritized implementation/specification corrections

### P0 — before owner approval

1. **Freeze the example count.** Resolve the direct source inconsistency between “nine” in the heading/caption/Step 3 and “five” in Step 2/result. The receipt must use one self-consistent fictional bundle. No image or CSS change can repair a count contradiction.
2. **Add the deterministic receipt before another raster experiment.** Put the count snapshot and typed ledger in live HTML, with the no-verdict boundary and human disposition. Do not make an editorial image the first explanation of the relation.
3. **Demote H1.** Move it below the route receipt/proposition as an optional material metaphor, or run the current-image/no-H1 test before retaining it. Keep the current alt/caption boundary, but do not let that boundary carry the full semantic burden.
4. **Keep the exact first-paper boundary visible.** State that relation cues are supplied/stipulated in the specimen and study; do not say that the receipt discovers provenance or proves independence.

### P1 — next interface pass

1. **Implement native semantic structure.** Use a heading-labelled section, definition lists, a captioned table with scoped headers, visible row IDs, and a typed relation key. Keep all count-bearing content outside disclosure.
2. **Remove directional grammar.** No arrows, funnels, gates, “admission” lanes, status gradients, or right-hand “clean context” output in the receipt. Any decorative grouping line must be redundant with text.
3. **Preserve unknown as a first-class state.** The receipt’s key must say “UNKNOWN — preserve; do not count.” If a future fictional bundle includes unknown rows, include them in the table and in a separate count, not as zero or as independent support.
4. **Test table reflow and print.** The page may scroll the table region, not the whole page. Print must show all rows and the boundary. Capture 1440, 720, 390, 200% text zoom, keyboard, screen-reader spot check, and A4.
5. **Keep v13 archival.** Retain the verified PNG and full-resolution link, but do not reuse its hub/strip topology. Keep the text summary visible or easy to open, and ensure the receipt appears before the historical anchor.

### P2 — only after comprehension passes

1. Add optional per-record audit fields (source/artifact ID, date, derivation note) behind native disclosure, while leaving count/relation/state visible in the summary.
2. Consider a small deterministic SVG brace or repeated-origin marker only if it adds grouping without adding a route. It must have a text-equivalent and cannot become a new source of truth.
3. Optimize retained raster assets or provide responsive derivatives only with hash/provenance updates. No new image generation is needed for this opportunity.
4. If H1 and no-H1 are comprehension-equivalent, prefer the lower-weight/no-ambiguity composition. Emotional entry is not a reason to retain a misleading topology.

## 8. Evidence, inference, hypothesis, and design-judgment ledger

| Item | Label | Basis and implication |
| --- | --- | --- |
| The current source keeps exact map/loop/example semantics in live HTML. | **[S]** | Direct inspection of `site/app/page.tsx`; supports making the receipt HTML-first. |
| Current H1 alt/caption explicitly disclaim route/status/truth semantics. | **[S]** | Direct inspection; improves accessibility boundary but does not erase visible geometry. |
| H1’s aperture/lanes can be read as a one-way filter. | **[S] + [DJ]** | Direct visual inspection and Loop 1 red-team observation; design risk, not user-study evidence. |
| The current example mixes nine and five in different copy blocks. | **[S]** | Direct inspection; P0 content-integrity issue before implementation. |
| A route receipt is the best bounded addition. | **[I]** | It maps the current conceptual hinge to the exact typed-cue boundary without adding routing, discovery, or efficacy claims. |
| A text/table receipt will reduce nine-as-nine-origins errors. | **[H]** | Test with the proposed reader protocol; not yet demonstrated. |
| H1 should be demoted and tested against no-H1. | **[DJ] + [H]** | Recommendation based on topology risk, asset plan, and Loop 1 gates; the reader test decides retention. |
| The table/definition-list structure is preferable to a dense graph. | **[DJ] informed by [E]** | WCAG/HTML semantics and graph-readability literature support preserving relationships in text; no direct comparison study of this receipt exists. |
| B1/C1 are independent evidence. | **Not claimed** | They are separate roots only as stipulated by this fictional illustration; claim support is not assessed. |
| The receipt proves typed cues work. | **Not claimed** | Only the first-paper experiment could address the model-use claim, and only within its stated synthetic/oracle boundary. |

## 9. Primary/authoritative references

The visual/HCI references below are used for design rationale, not as direct evidence that this specific page or receipt will work.

- Ziemkiewicz, C. & Kosara, R. (2008). “The Shaping of Information by Visual Metaphors.” *IEEE Transactions on Visualization and Computer Graphics*, 14(6), 1269–1276. DOI: [10.1109/TVCG.2008.171](https://doi.org/10.1109/TVCG.2008.171). The study supports treating a funnel/aperture/gate as an interpretive metaphor with consequences, not neutral decoration.
- Hullman, J. & Diakopoulos, N. (2011). “Visualization Rhetoric: Framing Effects in Narrative Visualization.” *IEEE Transactions on Visualization and Computer Graphics*, 17(12), 2231–2240. DOI: [10.1109/TVCG.2011.255](https://doi.org/10.1109/TVCG.2011.255). It motivates testing framing, omission, visible structure, and annotation rather than assuming a disclaimer cancels a visual frame.
- Ghoniem, M., Fekete, J.-D. & Castagliola, P. (2005). “A Comparison of the Readability of Graphs Using Node-Link and Matrix-Based Representations.” *Information Visualization*, 4(2), 114–127. DOI: [10.1057/palgrave.ivs.9500092](https://doi.org/10.1057/palgrave.ivs.9500092). It motivates a sparse, text/table representation when relation detail can otherwise become a decoding burden.
- MacEachren, A. M., Roth, R. E., O’Brien, J., Li, B., Swingley, D. & Gahegan, M. (2012). “Visual Semiotics & Uncertainty Visualization: An Empirical Study.” *IEEE Transactions on Visualization and Computer Graphics*, 18(12), 2496–2505. DOI: [10.1109/TVCG.2012.279](https://doi.org/10.1109/TVCG.2012.279). The relevant design lesson is to make the type of uncertainty explicit; do not reuse one color or one visual cue for unknown, low support, and low confidence.
- Hullman, J., Qiao, X., Correll, M., Kale, A. & Kay, M. (2018 online / 2019 issue). “In Pursuit of Error: A Survey of Uncertainty Visualization Evaluation.” *IEEE Transactions on Visualization and Computer Graphics*, 25(1), 903–913. DOI: [10.1109/TVCG.2018.2864889](https://doi.org/10.1109/TVCG.2018.2864889). The survey motivates measuring interpretation, workload, and correction in addition to accuracy; it does not validate this receipt.
- W3C. [WCAG 2.2, SC 1.3.1: Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html), [SC 1.4.1: Use of Color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html), and [WCAG 2.2 Recommendation](https://www.w3.org/TR/WCAG22/). These are authoritative accessibility requirements/guidance for preserving structure in code and not relying on color alone.
- WHATWG. [HTML Living Standard: Tables](https://html.spec.whatwg.org/multipage/tables.html). Native table semantics support row/column relationships, captions, and scoped headers for the typed ledger.
- W3C WAI-ARIA Authoring Practices Guide. [Disclosure pattern](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/) and [WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria/). Use native `<details>/<summary>` for optional audit disclosure; do not hide the receipt’s count-bearing fields behind a custom widget.
- Zhang, Y., Ives, Z. & Roth, D. (2020). “Who said it, and Why? Provenance for Natural Language Claims.” *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics*, 4416–4426. DOI: [10.18653/v1/2020.acl-main.406](https://doi.org/10.18653/v1/2020.acl-main.406) and [ACL Anthology record](https://aclanthology.org/2020.acl-main.406/). The first-paper protocol cites this as a natural-language claim-provenance anchor; it motivates distinguishing article/report identity from common source origin, not the efficacy of this receipt.
- W3C. [PROV-O: The PROV Ontology](https://www.w3.org/TR/prov-o/). A provenance vocabulary is not a correctness or independence guarantee; the receipt borrows the typed-relation idea only within the project’s explicitly stipulated fictional boundary.

## Handoff

The bounded addition is the **origin-accounting route receipt**: nine explicit observation rows, one known common-origin cluster, zero independently supporting origins established for the claim, two separate comparison roots not assessed for support, preserved unknown semantics, and a human hold. Its topology is a labelled record/grouping, not a pipeline. Build it as semantic HTML first, test it image/no-image/text-only at desktop/mobile/print, and keep its copy explicitly illustrative.

The H1 should be **demoted and tested**, not trusted solely because the asset ledger scores it highly or because its caption disclaims a process diagram. The current source’s safer alt/caption and print `contain` behavior are improvements, but they do not establish reader comprehension. If H1 raises pipeline/gatekeeper errors or the image condition loses more than the formative threshold, remove it; the deterministic receipt, map, and worked text are sufficient.

Only the requested memo was written. No core files, images, deployments, or publications were changed.

# Round 1 editorial / owner-proxy audit

## Pattern Recognition / The Discrimination Layer v15.1 → v15.2

**Lane:** editorial voice, cold comprehension, and public-argument architecture
**Status:** provisional owner-proxy audit for the overnight convergence pass
**Date:** 2026-08-19
**Scope:** read-only review; no canonical production files edited

This audit simulates the owner described in the handoff: a high-agency systems
builder and exacting editor who can follow a difficult idea when it is introduced
in plain language, wants rigor through progressive disclosure, and has little
tolerance for inflated abstraction, generic manifesto prose, or plans presented
as evidence.

The proxy is not the owner. It is a test instrument for finding first-reader
friction before the owner spends time on a deep review.

## Executive verdict

### Gate

**Ready after one bounded editorial repair pass; not yet the strongest form for
deep owner review.** The underlying idea is coherent enough to review now, and
the release is substantially more honest and usable than v14. The next pass
should be editorial rather than conceptual: shorten the public argument, put the
decision consequence earlier, and move the record inventory and research
protocol behind the existing Explore and Lab routes. This does not justify a
new conceptual version.

### Strongest current form

An authored contemporary thought piece with a concrete evidence receipt and a
separate practitioner design dossier. It is not yet best presented as a single
all-in-one manuscript, academic paper, product manifesto, or validated
framework.

### Promise beyond a personal piece

**Conditional.** The strongest defensible seed is not “a new provenance system”
or “a universal discrimination layer.” It is:

> In evidence-sensitive AI work, treat the pre-answer context decision as a
> typed, reviewable, correctable record; test whether supplied information about
> shared origins reduces false corroboration beyond a plain counting rule.

That seed could support a practitioner template, open design project, and narrow
paper if other people can use the receipt consistently and the study survives
its baselines and shortcut checks.

### The dominant weakness

The manuscript asks a reader to remember a large taxonomy before showing enough
of the practical decision that taxonomy is supposed to improve. The reader can
understand the receipt, but the long middle gradually turns a distinctive essay
into a well-labelled inventory.

### Decisions

| Question | Provisional answer | Reason |
| --- | --- | --- |
| One thing to cut | The C01–C11 schema parade from the main reading path | It is useful implementation material, but its eight-field anatomy repeats the core claim eleven times and changes the genre from essay to dossier. Keep it in Explore / the framework record. |
| One thing to protect | The fictional receipt’s 09 observations / 01 common-origin cluster / 00 supporting origins / HOLD consequence, especially UNKNOWN stays unknown | This is the project’s clearest decision delta. It demonstrates preservation without corroboration and makes the human correction point visible. |
| Title | Keep provisionally for historical continuity, but run the rename test | The definition is careful, yet the social/legal reading of “discrimination” remains a high-severity first-impression risk. A subtitle such as “What an AI system should preserve before it answers” does useful work; it cannot replace reader testing. |
| Version | v15.2 editorial candidate, not a conceptual reset | The strongest material and the residual research question are already present. The repair is about sequence, load, and voice. |
| Next step | One bounded agent editorial pass, then owner review | Further agent expansion before a first owner reaction risks adding more explanation to a problem of proportion. |

## Evidence inspected

The following sources were inspected in the order required for this lane. Line
numbers refer to the current v15.1 checkout and are included so a later editor
can reproduce each finding.

| Evidence | Role in this audit | Material locations |
| --- | --- | --- |
| README.md | Release status, canonical surfaces, claim boundary, routes, and authorization limits | “Start here,” “Canonical v15.1 surfaces,” “Current status and claim boundary,” “Interactive explanations,” “History and future repository” |
| source/THOUGHT_PIECE_V15.md | Primary manuscript and line-level voice evidence | Opening and receipt 1–127; judgment and distinctions 129–174; C01–C11 175–252; loops and use boundary 254–312; prior art 314–390; objections 391–446; cases and lab 468–624; close 625–660 |
| source/THESIS_AND_TERMINOLOGY_CONTRACT.md | Owner intent, progressive-disclosure contract, title test, terminology boundaries | Thesis 9–24; title/term decision 46–64; term table 68–100; settled/provisional/testable boundary 104–134 |
| source/READER_OUTCOME_AND_READING_PATH_V15_1.md | Required reader outcome and route time budgets | North-star 9–25; paths 27–42; plain-language rule 44–67; interactive contract 69–88; acceptance test 90–105 |
| handoff/OWNER_REVIEW_PACKET_V15_1.md | Existing owner-facing recommendation and status | Recommendation 8–20; reader takeaway 22–43; change log 59–96; value ladder 112–129; next owner decisions 151–163 |
| site/app/page.tsx | Canonical route structure and first-fold/receipt implementation evidence | Masthead and route cards 77–126; receipt 137–217; proposition and historical transition 230–305; Explore map and C01–C11 surface 309–465; example 469–498; Lab 559–700; Sources/glossary 653–680; closing 689–694 |
| site/app/content.ts | Component, glossary, counterargument, research-path, and source arrays | Families/components 25–234; glossary 259–337; sources 339–359 |
| reports/V15_EDITORIAL_AND_SITE_SYNTHESIS_BLUEPRINT.md | Intended information architecture and release acceptance | Editorial spine, route separation, and acceptance sections |
| reports/VISUAL_READER_QA_REPORT.md | What is validated visually and what remains manual | Build/SSR and route checks; responsive behavior; keyboard/screen-reader limitation; print/PDF limits |
| reports/V15_1_FINAL_VALIDATION.md | Release receipt and evidence-status boundary | Loop 2 reader acceptance; Loop 3 package/status; remaining owner decisions |
| archive/v13/live-v13-rendered-dom-snapshot.html | Historical voice and original map logic | Intro around 852–894; mechanism cards 895–1359; footer 1454–1458 |
| reports/V13_RECOVERY_AND_INTENT_MEMO.md | Reconciled historical intent, what to preserve, and what not to re-import | Historical thesis and settled ideas; universal-looking claim corrections; wording worth preserving; structure not to repeat |
| source/THOUGHT_PIECE_V14.md and handoff/COMPLETE_TRANSFER_GUIDE.md | v14 progression and regression context | v14 origin/architecture around 124–157; component expansion; visual and mobile history |

No external account, live model, study, deployment, or publication was used.
The package itself says no empirical result exists; this audit preserves that
boundary.

## Cold first-read log

### 60–90 seconds: what lands

The manuscript’s intended route is “Nine reports, one origin” followed by the
receipt consequence. On a cold read, the first memorable event is excellent:
nine articles look like nine confirmations until the reader learns that all
trace to one launch announcement (source/THOUGHT_PIECE_V15.md:24–37). The
sentence “The summary has not merely shortened the evidence. It has changed its
structure” gives the error a shape instead of merely calling it bias.

The reader can restate the central point without technical vocabulary:

> A system can make an answer look better supported simply by treating repeated
> reports as separate evidence. Keep the reports, but check how they relate
> before deciding what they support.

That is a pass for the core comprehension contract. The opening list of earlier
choices (source/THOUGHT_PIECE_V15.md:39–52) also helps: the reader sees that
the problem is not only the final generated paragraph.

The first friction arrives immediately after the good example:

- “origin” has not yet been distinguished from source, article, or claim;
- “discrimination layer” appears as the proposed name before the reader has
  seen the name’s social/legal ambiguity in context (1:1–9, 60–64);
- “boundary-preserving” and “context is allowed to influence” are accurate but
  abstract compared with the concrete nine-article scene;
- the status block and reading-route instructions are useful for handoff but
  read like project metadata if placed in the public first screen.

**Provisional first-minute result:** pass on problem recognition; borderline on
name and genre. A reader understands the error before understanding the
framework, which is the correct order. The route should capitalize on that by
reaching the receipt’s changed action quickly.

### About five minutes: what becomes clear

The receipt makes the argument operational. The most important numbers are
09, 01, and 00: nine observations, one known common-origin cluster, and zero
counted supporting origins for the broad claim (source/THOUGHT_PIECE_V15.md:98–113;
the live route renders the same fields at site/app/page.tsx:151–172). The
zero is initially surprising, but the explanation is sound: a vendor launch is
not automatically evidence that a broad validation claim has independent
support. The HOLD · VERIFY ANOTHER ORIGIN RELATION disposition changes what a
team does next without pretending to reject the tool.

The three relation states also pass conceptually:

- known shared path: preserve the report but do not count it as a new root;
- separate only as stipulated by this fictional test;
- unresolved: do not guess.

The reader can now answer the five required questions from the contract:

1. **Problem:** report-level repetition can become false corroboration.
2. **Why nine can fail:** URLs and wording do not guarantee distinct origin
   paths.
3. **What is proposed:** make the choices before generation visible and
   reviewable.
4. **Who can correct it:** an accountable human can hold, verify, or correct
   the relation and route.
5. **Has it been validated?** No; the receipt is fictional and the study is
   unrun.

The friction is not conceptual impossibility but accumulation. The table at
source/THOUGHT_PIECE_V15.md:153–168 lists thirteen separations in one burst.
It is intellectually correct, but a non-specialist must hold source identity,
provenance, recurrence, origin relation, claim support, authority, relevance,
authorization, enrichment, action priority, disposition, and outcome at once.
The line “The table is not a claim that every distinction needs its own model or
database column” (170–173) arrives after the load rather than preventing it.

**Provisional five-minute result:** the essential argument passes if the reader
stops after the receipt and first distinction section. The current manuscript’s
advertised five-minute path is therefore defensible, but its stop point should
be more explicit and the public prose should use three plain questions before
the thirteen-term inventory.

### Full read: where the genre changes

The full manuscript is disciplined about uncertainty. It repeatedly says that
the framework is not a truth oracle, that prior art is extensive, that the
receipt is fictional, and that the proposed experiment has no result. Those are
major strengths. The full read also reveals a coherent systems idea: intent and
authorization, evidence identity, typed relationships and claims, routing,
human disposition/memory, and outcome feedback.

The cost is editorial proportion. Starting at
source/THOUGHT_PIECE_V15.md:175, each C01–C11 record uses a similar “what it is
/ why / consumes / produces / interacts / risks / evidence / speculative”
anatomy. That is excellent implementation documentation and weak main-essay
pacing. By C06–C08 the reader’s question shifts from “What should change in an
AI workflow?” to “How many fields are in this map?”

The prior-art section (314–390) is honest but reads like a source ledger in
the middle of the argument. It should remain available and cited; it should be
compressed in the public route to one paragraph that names the claim the prior
art removes. The objections (391–446) are among the best writing in the
manuscript, especially “Perfect lineage for a false claim is still perfect
lineage for a false claim” and the cost/ceremony concern. They are weakened by
parallel card-like headings and by arriving after a long taxonomy.

The lab note (491–595) correctly refuses to call a harness an experiment,
but its detailed endpoint, safety set, tokenizer parity, stress structures, and
shortcut diagnostics belong on /lab and in the protocol. In the thought piece
the reader needs only the one question, the comparison, the no-results status,
and the possible null/harm outcomes. The current inventory paragraph
(584–590) is especially dossier-like: “ten closed JSON Schemas,” generators,
parsers, scorers, and diagnostics communicate effort more than meaning.

**Provisional full-read result:** high epistemic trust; declining attention and
voice. The reader finishes knowing the project is careful, but may not remember
the one changed decision that made the care worthwhile.

## Sequential confusion log

This log follows the primary manuscript route, then cross-checks the site’s
rendered route and progressive-disclosure contract. “Popup” means the site’s
Term interaction; the Markdown manuscript has no popup, so a reader of the
canonical source cannot rely on one.

| Step / location | First interpretation | Later resolution | Popup/glossary effect | Severity | Editorial action |
| --- | --- | --- | --- | --- | --- |
| Title and subtitle 1–3 | “Discrimination” may concern protected-class classification, fairness, or a classifier; “origin” sounds like publishing history | Line 8–9 excludes social classification and the example later defines origin relation | Definition helps, but the first emotional/semantic association arrives before the argument | Trust loss for some readers | Keep historical title provisionally, add a plain subtitle and test alternatives with real readers; do not repeat the technical noun in every section heading |
| Reading instructions 11–22 | This is a handoff packet or product documentation rather than an essay | The route eventually becomes a clear thought piece | No popup needed; metadata cannot fix genre signal | Momentary friction | Move status/route metadata into a compact note or site chrome; begin the public manuscript with the scene |
| “Nine reports” 26–37 | Nine different URLs may equal nine pieces of evidence | All trace to one announcement; reports remain useful as records of circulation | No glossary needed | Pass | Protect nearly verbatim; this is the strongest opening |
| “Origin paths” 32–37 | Origin may mean source, publisher, artifact, or causal explanation | Receipt later distinguishes report, origin, and claim support | Glossary helps only after the reader has already formed a model | Comprehension loss if read quickly | Say “where the information came from” once before introducing “origin” |
| “Boundary-preserving” 60–64 | A broad systems abstraction with no visible action | Receipt later shows the boundary as a hold/verify decision | No glossary can make an abstraction concrete | Momentary friction | Replace or follow immediately with “keep the reports; change the next decision” |
| “Supporting origins counted: 0” 79–84, receipt 110 | If there is one known origin, why is the count zero? Is the framework discarding evidence? | Support for the broad claim was never assessed; origin relation is not claim support | Popup for claim support/origin relation would help on site; plain prose must carry it | Trust/comprehension risk | Put “one origin is known; zero origins support this claim yet” in the same sentence as the count |
| DEPENDENT, INDEPENDENT-AS-STIPULATED, UNKNOWN 115–127 | Experimental codes or statistical categories | The states are narrow relation labels; UNKNOWN blocks invented corroboration | The site glossary improves this; the manuscript needs a three-row plain table | Momentary friction | Lead with “shared / separate only in this test / unresolved”; expose codes second |
| “Judgment before the answer” 129–151 | Generic AI-safety preamble about context quality | The manual/community-post contrast shows why one score fails | No popup needed | Pass with load | Retain the contrast, trim one list of adjectives, and tie it to the receipt sooner |
| Thirteen-row separation table 153–168 | A database/schema design review | It is a set of error boundaries, not a requirement for thirteen columns | Glossary cannot reduce simultaneous load | Comprehension loss | Replace main-route table with three reader questions; preserve full table in Explore/Sources |
| Six families / C01–C11 175–252 | A required architecture or product specification | The manuscript says it is a reviewable map, not a minimum | Details are inspectable but not progressive enough | Route abandonment risk | Keep compact six-question map in essay; move field anatomy to framework route |
| Two loops 254–275 | A second conceptual framework after the first one | Fast current-decision loop and slower outcome update become clear | No popup needed | Momentary friction | Keep, but place immediately after the receipt/application and use one worked correction |
| Prior-art names 318–390 | A literature review and novelty defense | The claim is narrowed to synthesis + supplied-cue test | Links are useful; list density interrupts public reading | Attention loss | Compress to “what this removes” with a linked source ledger |
| Objection “old work under a new label” 393–400 | Defensive novelty argument | The project is honest about synthesis | No popup needed | Pass | Protect; make it the bridge into the narrow contribution |
| “Where the responsibility can live” 277–296 | A product architecture taxonomy | Practice, coordinating system, and model behavior are placements, not maturity levels | No popup needed | Pass | Retain in shorter form; strong practitioner value |
| Alpha Solver / Signal Foundry 468–489 | These products may validate the framework | Boundaries say they are translations, not votes | Boundary text repairs implication after the name has done its work | Trust risk | Keep at most one bounded case in the essay; link the case-study boundary; never use the names as support |
| Lab labels F0/F1/F2, N=300, T1 501–584 | A live study or a result report | It is a frozen, unrun protocol with a narrow comparison | Site popups help; manuscript route is too dense | Route abandonment / status confusion | Move mechanics to Lab; public essay keeps one paragraph and a no-results callout |
| “Sixteen boundaries” 595–624 | A defensive disclaimer wall | The project is trying not to overclaim | Repetition lowers salience of the strongest limits | Attention loss | Collapse to five decisive limits and link the full list |
| Closing 625–646 | The thesis returns, but much has already been said | The last sentence preserves a meaningful research question | No popup needed | Pass but repetitive | Protect the “count the right unit / preserve unknown” cadence; remove one duplicated prior paragraph |

## Cold-read answers without project vocabulary

### One-sentence thesis retained

Before an AI writes an answer, someone—or some workflow—has already decided what
to look at, what to treat as separate, what to include, and when to stop. Those
choices should leave a record that a person can challenge. Repeated reports can
remain useful without becoming repeated proof.

### Three distinctions retained

1. Nine reports are nine observations; they are not automatically nine separate
   paths to information.
2. Where a report came from is different from whether it supports the claim in
   question.
3. A human’s “hold,” “verify,” or “proceed” is a decision about what to do next,
   not a fact about the world.

### Behavior that should change

When a summary says “many sources agree,” inspect the relationship among the
reports before counting corroboration. Preserve the reports, mark unresolved
relationships as unresolved, narrow the claim if needed, and record the next
permitted action.

### Strongest unanswered question

Does the added record and review step improve a consequential decision enough to
justify its cost compared with a strong, simpler retrieval-plus-citation
workflow? The proposed study tests only one narrow cue-use behavior, not that
whole question.

### What makes it worth finishing

The receipt changes a vague quality complaint into a visible decision: zero
supporting origins for the broad claim, a hold, and a bounded verification step.
The project also earns trust by naming how it could lose and by keeping a null,
harmful, unstable, or shortcut-driven result in the record.

## Terminology and progressive-disclosure audit

The current contract is right that a popup cannot rescue opaque visible prose.
The following disposition is for the public thought piece. The technical
records may retain stable IDs and exact codes.

| Term | Current risk | v15.2 public treatment | Reserve / retain |
| --- | --- | --- | --- |
| discrimination layer | Social/legal ambiguity; can sound like one ranking classifier | Define once as “the responsibility for deciding what context may influence an answer,” then use “the layer” or “the pre-answer check” sparingly | Retain exact title only while the rename test is open |
| origin | Readers conflate source, publisher, document, and causal root | First say “where a report’s information came from”; introduce “origin” in the receipt | Retain as schema term |
| dependent / independent | Sounds like statistical independence or a discovered fact | Use “shared path,” “separate only in this test,” and “unresolved” first | Codes in Lab/protocol |
| provenance | Commonly heard as correctness or authenticity | Use “a trace of where material came from and how it changed”; define provenance second | Technical records / Sources |
| disposition | Internal workflow jargon | Use “recorded human decision (hold, verify, proceed, defer)” | Stable schema term |
| F0/F1/F2 | Product versions or grades | “Three versions of the same planned test” before codes | Lab/protocol only in essay |
| N=300 | A result, confidence, or people count | “300 planned fictional test cases; no study has run” | Lab/protocol |
| T1 | Opaque arm label | “Optional descriptive real-world transfer check” | Lab/protocol |
| calibration | Often means general model confidence | If needed, say “whether stated confidence matches outcomes”; otherwise reserve | Research appendix |
| endpoint | Sounds like API/network endpoint | “The predeclared measure the study will count” | Lab/protocol |
| denominator | Mathematical detail with no first-route value | “What set of assigned cases the measure counts” | Lab/protocol |
| construct validity | Methods jargon | “Whether the test actually represents the behavior we claim to test” | Research note |
| locked negative-result commitment | Long self-describing label | “A promise made before the test to report failure or harm” | Full label in Lab |

The term inventory supports progressive disclosure only if the visible sentence
can stand without the term. A technical glossary is an invitation to go deeper,
not a permit to write in a private dialect.

## AI-slop, voice, and deletion audit

“AI slop” here does not mean any polished sentence. It means language whose
cadence, abstraction, or repeated caveat creates the appearance of thought
without carrying a new decision, image, or boundary.

### Lines to change, with exact reasons

| Location | Passage / pattern | Diagnosis | Keep / change |
| --- | --- | --- | --- |
| source/THOUGHT_PIECE_V15.md:54–64 | “The proposal in this essay is modest… boundary-preserving way…” | Good restraint, but abstract nouns arrive directly after the strongest concrete scene. “Modest” also signals a familiar model-written hedge. | Change to a plain consequence: “keep a record of the relation and let it change the next decision.” |
| 39–52 | Eight parallel bullets beginning with “two…” / “an…” | A useful diagnostic list, but a long list of symmetrical substitutions can feel generated. | Keep six; group them under “counting, permission, stopping” and attach each group to an example. |
| 129–151 | “AI interfaces emphasize the answer because the answer is what people see…” | Strong setup, but the first two paragraphs use generalized system language before the next concrete example. | Keep the manual/community contrast; shorten the opening to one paragraph. |
| 153–173 | Thirteen-row distinction table | Correct but taxonomy-heavy; the table supplies breadth instead of an image or action. | Replace in essay with three questions and link the full table. |
| 177–180 | “The current framework decomposes the responsibility into six families and eleven named records…” | This is a framework handoff sentence, not a thought-piece turn. | Move to Explore introduction. In essay say “The full map breaks that check into a few reviewable records.” |
| 184–252 | Repeated C01–C11 “what/why/consumes/produces/interacts/risks/evidence/speculative” anatomy | High information value for implementers, low narrative value; repeated template cadence is the clearest AI-generated feel. | Keep as canonical framework data; remove from public essay. |
| 254–275 | “fast loop,” “slower loop,” “one preserved history” | Distinctive systems insight and memorable temporal distinction. | Protect, but place after a concrete correction and avoid introducing it as another abstract map. |
| 300–312 | “The full framework is most plausible when… It is probably unnecessary when…” | Useful negative space, but list syntax resembles a product requirements memo. | Keep as a short “Use it when / leave it out when” box. |
| 318–390 | Dense sequence of named papers and cautious comparator paragraphs | Evidence discipline is excellent; public argument loses rhythm and asks readers to audit novelty before they understand value. | Compress to the claim boundary; keep links and full ledger in Sources/research. |
| 393–446 | Repeated headings “The layer can… / Provenance can… / The framework may…” | Honest objections, but the repeated template produces a predictable machine cadence. | Keep the six objections; rewrite three as direct questions from a skeptical reader. |
| 468–489 | Two product cases | Names create an impression of validation before the boundary denial arrives. | Use one case as a bounded translation or move both to the case-study route. |
| 491–590 | Lab terminology, counts, and harness inventory | Methods-heavy detail shifts genre and repeats “no result” in several forms. | Keep one no-results paragraph and link Lab for protocol mechanics. |
| 595–624 | Sixteen limitation items | The list is responsible but overcomplete in the public route; repeated “No…” statements flatten the hierarchy of risk. | Keep five dominant limits; retain full list in audit/protocol. |
| 625–646 | Closing repeats origins/support/truth/decision distinctions | The cadence “A… A… A… A…” is effective once, then becomes a recitation. | Protect the final “count the right unit / preserve unknown” sentence; cut one earlier repetition. |
| archive/v13/live-v13-rendered-dom-snapshot.html:852–894 | “This started as a conversation about why so much AI output feels stale…” and the decomposable-floor distinction | Specific, human, and historically important; some universal claims about GPT and “the actual answer” are too broad. | Recover the origin story and cadence, not the unsupported universals. |

### Voice to protect

The project has a credible authorial voice when it is concrete, slightly
contrarian, and willing to state a limit without apologizing for the idea:

- “The summary has not merely shortened the evidence. It has changed its
  structure.” (source/THOUGHT_PIECE_V15.md:32–37)
- “Unknown is the state most likely to disappear in a polished summary.”
  (115–127)
- “A framework that cannot say when it is not worth using becomes a demand for
  ceremony.” (298–312)
- “Perfect lineage for a false claim is still perfect lineage for a false
  claim.” (411–416)
- “Underweighted is a starting condition, not a conclusion.” (historical
  wording recovered in reports/V13_RECOVERY_AND_INTENT_MEMO.md; echoed in the
  v15.1 continuity material)
- The “decomposable part of expertise is not the ceiling” idea from v13,
  retained only with the explicit boundary that output is not expertise.

These lines work because each contains a reversal, a picture, or a test. The
candidate manuscript uses that cadence but reduces slogans and status labels.

## Intended one-week takeaway

One week later, the reader should remember one habit, not eleven components:

> Before saying “many sources agree,” ask: how many observations, how many
> distinct information paths, and what exact claim does each path support? If
> the relation is unresolved, leave it unresolved and record what a person will
> do next.

If a reader remembers only the title, the project has failed. If a reader
remembers the receipt and applies the three questions to a real evidence packet,
the thought piece has done its job even if the framework name disappears.

## Stronger editorial architecture for v15.2

The repository already has the right route separation; the manuscript should
match it.

### Public thought piece: five movements

1. **Nine tabs, one announcement.** Start with the fictional scene and state
   the false-corroboration problem without project vocabulary.
2. **The receipt changes the decision.** Show 09 / 01 / 00, the three plain
   relation states, and HOLD · VERIFY. Explain why zero support is not a
   rejection.
3. **Three questions before the answer.** Collapse the taxonomy into: what did
   we see and where did it come from; what does it support; what may we do now?
   Mention the full six-family map as a deeper route, not as the essay’s spine.
4. **Make correction possible.** Explain the current-decision loop, later
   outcome loop, human disposition, and when the overhead is not worth it.
5. **Name the boundary.** State prior art, objections, the one unrun study
   question, historical continuity with v13, and the one-week takeaway.

### Deep routes

- **Explore:** six families, C01–C11, component failure modes, two loops, and
  bounded cases. Keep exact IDs and evidence labels here.
- **Lab:** F0/F1/F2, planned N=300, parity, fixed denominator, shortcut gates,
  T1, and null/harm dispositions. Make “no model/no run/no result” the first
  line.
- **Sources:** prior-art ledger, full glossary, historical v13 archive, and
  public/private boundary.

The thought piece must not make a reader walk through Explore and Lab to reach
the conclusion. Those routes should deepen trust after interest exists.

## Cut / keep / change ledger

| Decision | Material | Destination / transformation | Acceptance condition |
| --- | --- | --- | --- |
| CUT from main essay | 13-row “what must remain separate” table | Replace with three plain questions; retain full table in Explore/Sources | A non-specialist can state the problem without naming provenance, disposition, or origin accounting |
| CUT from main essay | Full C01–C11 eight-field records | Keep canonical data in site/app/content.ts and Explore | The essay can be read in 10–15 minutes without schema fatigue |
| CUT from main essay | Paper-by-paper prior-art parade | Replace with one paragraph + linked ledger | The novelty boundary remains exact; no broad novelty claim is lost |
| CUT from main essay | Full limitations list (16 items) | Keep five dominant limits + full Lab/Sources list | The reader can identify the one risk that governs the next decision |
| COLLAPSE | Multiple “no result / not evidence / not runtime” disclaimers | One status block at the start of Lab and one sentence at the receipt | No status boundary is weakened; the same caveat is not repeated in every section |
| KEEP | Nine reports / one origin narrative | Opening, nearly intact | At 90 seconds reader can explain why recurrence is not corroboration |
| KEEP | 09 / 01 / 00 receipt and HOLD | Core public artifact | Reader can state what changes after the receipt |
| KEEP | UNKNOWN rule | Plain-language three-state explanation | No reader moves unresolved relation into “independent” without being corrected |
| KEEP | Objection that lineage can be rigor theater | Skeptical midpoint | Reader understands more fields are not automatically more useful |
| KEEP | Negative/neutral/harmful study commitment | One short research boundary | Reader knows a null or harmful result would shrink the claim |
| CHANGE | Title treatment | Retain with subtitle and immediate definition; run 5-reader rename test | Social-classification misread is measured, not assumed away |
| CHANGE | discrimination layer repetition | Use title once, then “the pre-answer responsibility” / “the check” sparingly | Technical noun appears only where it adds meaning |
| CHANGE | V13 continuity | One paragraph and historical figure caption | Historical map is preserved without implying current topology or proof |
| CHANGE | Product cases | One bounded translation, or route-only | No case is read as independent validation |

## Acceptance tests for the candidate

These are tests of the editorial candidate, not of the framework’s effectiveness.

### First-minute comprehension

Use five readers matching the owner proxy, with no glossary, source files, or
prior context. After reading only the first 350–450 words, each reader must
answer in plain language:

1. What went wrong in the nine-report example?
2. What should be preserved?
3. What should not be claimed yet?

**Pass:** at least 4/5 answer all three materially correctly; no answer needs
the phrase “discrimination layer,” “provenance,” or “origin accounting.”

**Fail examples:** “the reports are false,” “the tool is rejected,” “the model
discovered real independence,” or “nine sources prove the claim.”

### Five-minute completeness

Stop readers after the receipt and three-questions section, before prior art or
the research note. Ask the five reader-contract questions from
source/READER_OUTCOME_AND_READING_PATH_V15_1.md:90–105.

**Pass:** at least 4/5 readers give materially equivalent answers, correctly
state that 09 observations do not equal 09 roots, and identify HOLD · VERIFY as
a human next step rather than a truth verdict. No glossary lookup is allowed
for the first attempt.

### Voice and anti-slop

Have two independent editors mark sentences that feel authored, generic, or
machine-templated.

**Pass:**

- at least five passages are judged specific and worth protecting;
- no section contains more than three consecutive abstract sentences without a
  concrete object, action, or example;
- no paragraph repeats the same “not a truth oracle / no empirical result”
  caveat after the status boundary has been made once;
- the candidate contains no unsupported market-size, model-capability, or
  universality claims;
- at least one skeptical reader can identify a sentence they disagree with,
  not only praise the polish.

### Status and evidence integrity

Run a local text check for:

- no model selected, no study has run, fictional, and not a result near every
  research surface;
- no sentence claiming that the framework improves decisions, discovers
  provenance, or establishes independence;
- no use of F0/F1/F2, N=300, T1, endpoint, or construct validity in the
  first-minute route;
- no heading in the public candidate that begins with C01–C11;
- duplicate phrase scan for “before generation,” “preserve,” “inspectable,” and
  “unknown” to ensure the concepts remain present without becoming a chorus.

## Handoff recommendation

The parent convergence task should treat this lane as a bounded editorial
repair, not a request for another framework expansion. The candidate at
source/candidates/THOUGHT_PIECE_V15_2_EDITORIAL_CANDIDATE.md is a complete
public-argument alternative. It intentionally leaves exact component records,
research denominators, and source-by-source prior-art disposition in their
canonical deeper routes.

After this pass, the owner’s most valuable decisions are narrow:

1. Does the receipt feel like a reusable artifact or only a teaching example?
2. Does the title’s historical continuity justify the first-impression risk?
3. Which sentence in the candidate sounds most like the owner’s actual voice?
4. Is the three-question version enough for the main route, with the full map
   behind Explore?

Do not answer these by adding more technical detail. They require a human
reaction to the proportion and voice of the revised argument.

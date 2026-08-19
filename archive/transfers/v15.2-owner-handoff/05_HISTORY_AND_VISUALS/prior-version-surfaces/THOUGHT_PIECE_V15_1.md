# Pattern Recognition: The Discrimination Layer

## Why repeated reports can still amount to one origin—and what an AI system should preserve before it generates

- **Status:** v15.1 thought piece for local owner review
- **Empirical status:** conceptual synthesis and research program; no model
  study, participant study, transfer run, field evaluation, or published result
- **Term boundary:** *discrimination* means technical differentiation among
  information and possible actions, not social classification

### How to read this

- **60–90 seconds:** read “Nine reports, one origin” and the closing paragraph
  of “The counting error in full.”
- **About five minutes:** continue through “What must remain separate.” That is
  the complete essential argument.
- **15–20 minutes:** add the framework, loops, objections, and bounded cases.
- **30–45 minutes or more:** add the research note, prior art, and linked
  technical records.

The shorter path is not a preview that withholds the conclusion. The longer
paths expose the machinery, objections, and research boundary behind it.

## Nine reports, one origin

Nine favorable articles arrive through nine sites. They use different
headlines, different layouts, and slightly different words. A summary says:
“Nine sources agree that the new tool is broadly validated.”

All nine articles trace to one launch announcement.

The summary has not merely shortened the evidence. It has changed its
structure. It has turned nine report observations into nine apparent origin
paths, then turned that apparent plurality into corroboration. The claim may
still be true. The announcement may still be accurate. The reports may still
be useful records of reach, timing, or framing. But repetition alone did not
create eight new roots.

This is a small failure with a large family resemblance. It appears whenever a
system gathers, groups, weights, compresses, and selects material before an AI
model answers. The final prose may be where the error becomes visible, but the
decisive judgment often happened earlier:

- two URLs were treated as two sources;
- two sources were treated as two origins;
- an official statement was treated as support for every claim about the
  product;
- an unknown relationship was silently treated as independence;
- retrieval rank became attention priority;
- technical access became permission;
- a long context became a reason to stop looking;
- a fluent synthesis hid which evidence actually influenced it.

The proposal in this essay is modest: make those judgments inspectable before
generation. Preserve the difference between a report, where it came from and
how it changed, the claim it bears on, its authority for that claim, its
relevance to the current decision, the permission to use it, the cost of
learning more, and the accountable person’s recorded next step.

Call that responsibility a **discrimination layer** if the name helps. Rename
it if the name misleads. It is not a truth oracle, a universal ranking model,
or necessarily a new service in a stack. It is a boundary-preserving way to
ask what context is allowed to influence an answer—and to leave a receipt that
another person can correct.

## The counting error in full

The nine-report example is fictional, but its accounting is exact. A technical
team is deciding whether a sandbox pilot of a data-migration tool is warranted.
No production data are allowed. The research budget is 90 minutes. The claim
under review is broad: “The tool is broadly validated.”

The receipt contains nine unordered observations, `O01` through `O09`. Each
report derives from `Origin A`, the launch announcement. Under the declared
relation rule, the nine observations form one known common-origin cluster and
each is marked `DEPENDENT`. The observations are preserved; none is deleted or
called false.

The number of counted supporting origins for the broad-validation claim is
**zero**, not one. That is intentional. The launch announcement is a known
origin, but its stance toward the broader claim has not been established. A
vendor announcing a product is not automatically evidence that the product is
validated in independent use. Origin accounting cannot be allowed to launder
claim support.

Two other roots, `B1` and `C1`, appear only as contrast. They are separately
rooted *in this illustration*; their support for the claim has not been
assessed, so they are not counted either. The packet state is `INSUFFICIENT`.
The accountable person’s recorded decision—called a *disposition* in the
technical records—is:

> **HOLD · VERIFY ANOTHER ORIGIN RELATION**

The next step is not “reject the tool.” It is to inspect the announcement, find
a separately authored benchmark or failure report, document its origin
relation, and then assess the exact claim it supports or refutes.

### Origin-accounting receipt `ORIGIN-EX-01`

| Field | Recorded value |
| --- | --- |
| Evidence status | Fictional illustration; no live data; no result |
| Decision | Sandbox-pilot warrant |
| Permission | Sandbox only; no production data |
| Research budget | 90 minutes |
| Claim | “The tool is broadly validated.” |
| Observations | `O01`–`O09`, nine unordered report records |
| Known relationship | All derive from `Origin A`, one launch announcement |
| Known common-origin clusters | `1` |
| Supporting origins counted for this claim | `0` |
| Contrast roots | `B1`, `C1`; separately rooted as illustrated, support unassessed |
| Claim state | `INSUFFICIENT` |
| Disposition | `HOLD · VERIFY ANOTHER ORIGIN RELATION` |

Three relation states do most of the work:

- **Known shared path (`DEPENDENT`):** traceable to an existing artifact or
  path. Preserve the report, but do not count it as a new root under this rule.
- **Separate in this test only (`INDEPENDENT-AS-STIPULATED`):** a separate root
  declared by an illustration or synthetic benchmark. This is not provenance
  discovery or a claim about the real world.
- **Not established (`UNKNOWN`):** the relationship is not established. Preserve the uncertainty;
  do not guess in either direction.

Unknown is the state most likely to disappear in a polished summary. It is
also the state that keeps incomplete lineage from turning into invented
corroboration.

## The judgment before the answer

AI interfaces emphasize the answer because the answer is what people see. But
the answer inherits a sequence of earlier choices: what could be acquired,
which artifacts were treated as versions of one another, which passages were
selected, which claims were considered supported, what was omitted, when
search stopped, and who could challenge the route.

“Use better context” is not a sufficient instruction. Better for what? More
authoritative, more relevant, more current, more diverse, more independently
rooted, cheaper to inspect, safer to disclose, or more likely to change the
decision? These properties can align, but they often do not.

An official manual may be authoritative about a documented command, share an
origin with ten derivative tutorials, remain silent about failure under load,
be highly relevant to an implementation question, and still be insufficient
for a reliability claim. A community post may be low-authority for product
policy, separately rooted for a reproduced failure, sensitive to disclose, and
the most decision-relevant artifact in the packet. One score cannot explain
both cases without burying the reason.

The layer proposed here is therefore not “quality ranking.” It is a place to
keep unlike judgments unlike long enough to inspect their consequences.

## What must remain separate

| Judgment | The tempting substitution | Why the substitution fails |
| --- | --- | --- |
| Source identity | Artifact identity | One source can publish many artifacts; one artifact can move through many sources. |
| Provenance | Correctness | A false claim can have perfect lineage. |
| Recurrence | Independent corroboration | Copies, quotations, and common-source reports can recur without adding a new root. |
| Origin relation | Claim support | A separately rooted report may not bear on the claim; a dependent report may contain a useful exact span. |
| Source authority | Universal trust | Authority is domain-, role-, time-, and claim-scoped. |
| Claim support | Citation presence | A cited document can be irrelevant, contradictory, or too broad for the proposition. |
| Relevance | General importance | Relevance belongs to the current decision and scope. |
| Technical access | Authorization | A system can reach material it is not allowed to collect, expose, transform, or retain. |
| Enrichment value | Action priority | Learning more may be useful without being the best permitted next step. |
| Action priority | Truth | “Run a sandbox test” is a decision, not a factual verdict. |
| Owner disposition | External fact | Acceptance, deferral, and override are accountable choices, not evidence about the world. |
| Outcome | Retroactive truth | A later result can update policy without rewriting what was known at the time. |

The table is not a claim that every distinction needs its own model or database
column. It is a claim about error visibility. When the distinctions collapse,
the system loses the ability to say whether a bad answer began with identity,
lineage, claim scope, selection, permission, or action.

## A systems responsibility, not another oracle

The current framework decomposes the responsibility into six families and
eleven named records. Eleven is not a proven minimum, and six families are not
a maturity model. They are a reviewable map: enough structure to show the
boundaries, compact enough to argue with.

### 1. Intent and authorization

**C01 · Decision brief and authorization envelope.** Record the question,
intended use, owner, stakes, expected baselines, allowed operations, sensitive-
source rules, and time/money/token/attention budget. Relevance, meaningful
absence, stopping, and disclosure are task-relative; without a versioned
brief, they become retrospective stories.

### 2. Evidence spine

**C02 · Acquisition controller.** Propose, authorize, record, and stop
retrieval or collection. “One more search” consumes resources and can cross a
permission boundary. A failed capture is a failure receipt, not evidence that
the material does not exist.

**C03 · Source, artifact, normalization, and lineage spine.** Keep a source,
an artifact, a capture, a normalized representation, and a summary linked but
distinct. Retain where each item came from, who or what handled it, when it
changed, and what remains ambiguous. The technical term for that trace is
*provenance*. A summary should not gain authority by losing its origin.

### 3. Relationships and claims

**C04 · Relationship, recurrence, common-origin, and gap graph.** Record typed
relationships among reports, origins, events, observations, time points,
copies, derivations, comparison sets, and expected-but-missing perspectives.
Similarity can propose a relation; it cannot certify one. Meaningful absence
requires a named expectation.

**C05 · Claim, evidence, comparison, and contradiction graph.** Link atomic,
scoped claims to exact spans and to support, refutation, qualification,
insufficiency, alternatives, and unresolved questions. One document can carry
several claims with different evidence states.

### 4. Discrimination policy

**C06 · Multidimensional assessment.** Keep attention priority, domain source
authority, claim support, origin relation, relevance, enrichment value, action
priority, owner disposition, uncertainty, and possible consequence separate.
A scalar may summarize one declared decision, but it must not become a
universal trust score.

**C07 · Enrichment, stopping, and action router.** Compare permitted next
actions: acquire, inspect, compare, clarify, answer, answer provisionally,
hold, defer, escalate, or refuse. Record expected benefit, cost range,
uncertainty, and the reason to stop. A route is a choice, not a factual state.

**C08 · Bounded context packet.** Assemble the exact material allowed to
influence generation, together with provenance, claim links, inclusions,
material exclusions, unknowns, budgets, and generation constraints. A long
prompt is not automatically a reviewable packet.

### 5. Human disposition and memory

**C09 · Owner disposition, review, and override.** Give an accountable person a
consequential way to accept, reject, defer, hold, override, request more work,
correct a relation, or revise a constraint. A human placed after an opaque
route is not meaningful oversight.

**C10 · Versioned evidence, decision, and memory ledger.** Preserve raw
observations, interpretations, packets, decisions, outputs, corrections, and
supersession as append-only history. Build current views over the history; do
not overwrite the evidence that produced the original decision.

### 6. Outcome feedback

**C11 · Outcome feedback and revisable policy update.** Compare a predefined
expected outcome with a later observation, state confounders and attribution
limits, and propose a policy update for approval. The feedback record may
change a future rule. It may not silently alter the old evidence, target, or
decision.

## Two loops, one preserved history

The map contains two different loops.

The fast loop is about the current decision. A gap can send the system back to
acquisition. A contradiction can trigger comparison. A permission boundary can
stop a route. A packet can be revised before it reaches a generator. A human
can correct an origin relation and ask the system to recalculate without
deleting either report.

The slower loop begins only after a defined outcome exists. It compares what
was expected with what was later observed and proposes a policy change. It is
slower because outcomes are often delayed, confounded, selectively observed,
or attached to a different policy version. Treating every click or owner
preference as immediate learning would optimize the system toward convenience,
not necessarily better evidence judgment.

Both loops write into one preserved history. Observations, interpretations,
decisions, and outcomes remain different record types. A correction supersedes
an interpretation; it does not erase the artifact. A later result can revise a
pilot rule; it does not travel backward in time to make the original packet
omniscient.

## Where the responsibility can live

The layer describes a responsibility, not a deployment hierarchy. It can live
in three places, often at once.

**Practice.** A researcher can define the decision, distinguish reports from
origins, record material exclusions, preserve unknowns, and state why search
stopped without building a new product.

**Coordinating system.** A workflow can maintain identities, provenance,
claims, permissions, routes, packets, review, and receipts across retrieval and
generation.

**Model behavior.** Training or prompting may encourage a model to seek
information, use typed cues, abstain, or expose uncertainty. Model behavior
cannot replace external artifact identity, legal/organizational permission,
append-only receipts, or human authority.

None of these placements is inherently more mature. The useful question is
where a particular failure can be observed and corrected at acceptable cost.

## When the overhead earns its place

The full framework is most plausible when the work is consequential,
contested, dependence-heavy, temporally changing, expensive to acquire,
sensitive to disclose, or likely to be revisited. A due-diligence synthesis, a
research evidence packet, a production-change decision, or a source-sensitive
investigation can justify explicit lineage and disposition.

It is probably unnecessary for a supplied-input calculation, a straightforward
format conversion, low-stakes creative rewriting, or a bounded extraction with
an obvious source. In those cases, the layer should collapse to a brief,
permissions, exact inputs, and a simple receipt—or disappear.

This negative space is part of the design. A framework that cannot say when it
is not worth using becomes a demand for ceremony.

## What the prior art removes from the claim

The component ideas are not blank territory.

[Dong, Berti-Équille, and Srivastava (2009)](https://www.vldb.org/pvldb/vol2/vldb09-pvldb47.pdf)
modeled copying and source dependence in truth discovery and warned that common
values alone do not prove copying. [Senn (2009)](https://doi.org/10.1186/1471-2288-9-10)
showed how double counting and dependence can overstate evidence in
meta-analysis. [Greenberg (2009)](https://pubmed.ncbi.nlm.nih.gov/19622839/)
traced how citation practices in one biomedical network amplified an
unsupported claim into apparent authority. The
[Cochrane Handbook](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04)
explicitly distinguishes multiple reports from the underlying study while
preserving useful secondary reports.

[Pochampally et al. (SIGMOD 2014)](https://doi.org/10.1145/2588555.2593674)
extends the dependence warning beyond literal copying: sources can be
positively correlated because they share extraction rules, or negatively
correlated because they cover complementary domains or extract different
features. That makes a binary dependent/independent vocabulary too coarse for
a general source model. The current diagnostic keeps `DPND`, `INDP`, and
`UNKN` as narrow, benchmark-stipulated accounting states; it does not claim
to infer common processes, establish real-world independence, or provide a
complete dependence taxonomy. A later policy would need typed relation,
scope, direction, uncertainty, and relation provenance.

Retrieval research already has exact deduplication, noisy duplicate detection,
diversity-aware reranking, and set-wise selection. [NEWS-COPY](https://arxiv.org/abs/2210.04261)
defines duplicates as articles from the same original source article despite
abridgement or OCR noise. [Newswire](https://papers.nips.cc/paper/2024/hash/58f52a01a516609336da78ff17e6f81f-Abstract-Datasets_and_Benchmarks_Track.html)
reconstructs large historical reproduction clusters. MMR and
[SetR](https://aclanthology.org/2025.acl-long.861/) address diversity and joint
retrieval-set value. These are not the same task as origin certification, but
they block any claim that redundancy or set structure was ignored before this
project.

The closest direct natural-language provenance comparator is [Zhang, Ives, and
Roth (ACL 2020)](https://aclanthology.org/2020.acl-main.406/), a published paper
that defines claim-provenance graphs and infers provenance with information
extraction and textual entailment. That is an inferred provenance graph, not the
supplied relation field in the current benchmark proposal. The full source and
status ledger is [research/PRIOR_ART_DELTA_V1.md](../research/PRIOR_ART_DELTA_V1.md),
entries S1–S20.

Current RAG work comes closer still. [RAMDocs](https://arxiv.org/abs/2504.13079)
is a COLM 2025 conflict benchmark. [Li, Padman, and Krishnan](https://arxiv.org/abs/2605.29084)
is an arXiv v1 manuscript submitted 2026-05-27; no venue acceptance is shown in
the checked record, and its source-dependence labels describe cross-source
answers rather than derivation. [EvidentialRAG](https://arxiv.org/abs/2607.10491)
is an arXiv v1 manuscript submitted 2026-07-11; no venue or acceptance is shown,
and it proposes conflict/uncertainty fusion rather than origin inference.
[Naphade](https://arxiv.org/abs/2601.06189) is an arXiv v1 manuscript submitted
2026-01-08 whose record notes an ACL ARR submission but shows no acceptance; it
reports paraphrased-opposing-evidence behavior, but its documents are not
verified origins. [Ross and colleagues](https://arxiv.org/abs/2608.13956) is an
arXiv v1 manuscript submitted 2026-08-14 with no venue or acceptance shown; it
directly compares duplicate, paraphrased, and diverse retrieved evidence on a
fictional benchmark. The full status labels and task boundaries remain in the
delta rather than being inferred from a headline.

The adjacent retrieval records are also explicit: [MMR](https://doi.org/10.1145/290941.291025)
is a published SIGIR 1998 diversity-reranking paper; [NEST](https://aclanthology.org/2026.acl-industry.35/)
is published in the ACL 2026 Industry Track; [RARE](https://arxiv.org/abs/2604.19047)
is arXiv v2 and says accepted to ACL 2026 Main Conference, but an ACL venue page
was not located; and [Schelpe](https://arxiv.org/abs/2605.09611) is an arXiv v1
preprint. These are adjacent or future comparators, not required arms of the
locked F0/F1/F2 study.

The plausible contribution that survives is not a new copying detector, a new
RAG architecture, or a universal pre-generation mechanism. It is a
boundary-preserving synthesis and one narrow experimental question: does a
supplied typed origin cue change origin counting beyond an explicit rule when
evidence, prompt budget, model, and output contract are held fixed?

That contribution may still be too small, too obvious, or too brittle to
matter. The study is designed to find out.

## The strongest objections

### This is old work under a new label

Much of it is. Provenance, lineage, claim-evidence graphs, evidence synthesis,
truth discovery, copying detection, information foraging, value of information,
RAG, mixed initiative, human review, and organizational learning all have
mature literatures. The framework is defensible only as a synthesis with
explicit boundaries and as a source of narrow tests. If a closer integrated
framework is found, the novelty claim must shrink again.

### The layer can become a gatekeeper

Any system that selects context can erase peripheral sources, encode
institutional preferences, and call the result quality control. The answer is
not to hide selection. Exclusions, unknowns, reasons, permissions, appeal, and
source coverage must remain inspectable. If the system cannot show what it
withheld and who may reverse it, “discrimination” is the wrong word and
possibly the wrong design.

### Provenance can become rigor theater

Perfect lineage for a false claim is still perfect lineage for a false claim.
More fields can create an aesthetic of control without improving a decision.
The receipt must point to a consequential distinction and a correctable route;
otherwise it is ceremony.

### The framework may cost more than it saves

Eleven responsibilities can become an expensive bureaucracy. The proposal has
to beat strong simple baselines under matched time, tokens, retrieval, and
review effort. A retrieval-plus-citation workflow that performs equally well
at lower cost should win.

### Human review can be decorative

A reviewer shown a polished recommendation and a hidden evidence path is
likely to approve the recommendation. Real review exposes the exact relation,
span, exclusion, uncertainty, and route and makes correction change the packet.
If people cannot use that opportunity reliably, the control has failed.

### Feedback can optimize the wrong thing

Clicks, acceptance, short-term completion, and owner preference are not
automatically good outcomes. A policy update needs a predefined target,
horizon, exposure record, confounders, and approval. Otherwise the system will
learn the easiest measurable proxy and call it judgment.

### The name may do harm

An explicit technical definition may not overcome the social and legal meaning
of discrimination or the ML meaning of discriminator. If representative
readers still infer a social-classification or classifier thesis after the
definition, rename it. **Context judgment layer** is the cleanest current
alternative. Historical continuity does not outrank comprehension.

## Retirement tests

For a named task class, materially weaken or retire the framework if:

- a strong simple retrieval-plus-citation baseline performs equivalently at
  lower cost;
- raters cannot reliably distinguish authority, support, origin relation,
  relevance, enrichment value, action priority, and disposition;
- origin grouping hides valid convergence as often as it prevents false
  corroboration;
- the interface increases overload, delay, or overreliance enough to erase the
  correction benefit;
- permissions and review become ceremonial rather than consequential;
- outcome updates encode local preference or contaminated proxies;
- the eleven-part decomposition adds no explanatory or implementation value;
- the name continues to misstate the thesis.

Retirement is task-scoped. A failed typed-origin cue does not prove that
authorization, claim scope, or append-only correction are useless. Conversely,
a successful cue does not validate the rest of the map.

## Two bounded product cases

### Alpha Solver

The inspected Alpha Solver documents illustrate a reasoning posture: define a
problem, expose assumptions, consider alternatives, control tool use, and keep
the path reviewable. That resemblance can help explain C01, C07, C08, and C09.
Repository structure and product intent do not show that this framework
improves reasoning quality, safety, or outcomes.

### Signal Foundry

Signal Foundry illustrates several evidence responsibilities in a concrete
pipeline: immutable raw acquisition, a documented success/exclusion boundary,
source-aware transcript evidence, staged imports that are not auto-applied,
and separation of visual evidence from transcript-backed claims. Those are
bounded design choices. They are not independent empirical validation of the
eleven responsibilities or the origin-accounting hypothesis.

The case studies are translations, not votes for the framework. Reusing the
same design intuitions in several repositories does not create independent
support.

## Lab note: one question, no results

The conceptual site can be complete before an experiment. The empirical
surface cannot.

The current scientific program asks:

> For one frozen model, does a supplied origin-relation field reduce false
> corroboration relative to the same evidence and the same origin-counting
> rule without populated relation values?

### Three versions of the same evidence task

The experiment does not compare three different products. It gives one frozen
model the same fictional evidence in three carefully matched versions:

- **Ordinary baseline (`F0`):** assess the evidence and identify what was used,
  without an origin-counting rule or populated relation labels.
- **Rule only (`F1`):** add an explicit instruction to count distinct origin
  pathways, avoid treating repeated or derived reports as independent support,
  and preserve unknown; relation slots remain `NONE`.
- **Rule plus supplied labels (`F2`):** keep the F1 rule and add short labels
  that say whether each report follows a known shared path, is separate only as
  the benchmark stipulates, or remains unresolved. The implementation codes
  are `DPND`, `INDP`, and `UNKN`.

The headline comparison is the third version against the second. That isolates
whether the supplied relation labels add anything beyond merely stating the
rule. The two inputs must use exactly the same byte and token budget under the
eventual frozen model tokenizer. The current local approximation is development
machinery, not the final check.

### Corpus and endpoint

The planned corpus contains 80 development cases, 40 feasibility-only pilot
cases, **300 primary test cases (`N=300`)**, and 60 descriptive stress cases.
Here, `N` simply means the number of primary cases; it is not a result or a
confidence score. The four structures are one-origin repetition,
multiple-origin convergence, unknown-origin agreement, and conflict. The
primary endpoint counts a valid
assertion of two or more supporting origins as false corroboration when the
manifest certifies none/single or withholds certification as unknown. Invalid
outputs are conservatively counted as risk events in the fixed set of all 300
assigned bundles.

The safety set is fixed before any run: primary bundles with multiple
stipulated supporting origins. A valid output must retain at least two such
origins. Invalid outputs count as safety failures. The set never shrinks to
parseable outputs.

### What success and failure mean

A bounded positive result requires a beneficial F2-minus-F1 paired effect, a
two-sided exact test and paired interval in the declared direction, and passage
of the fixed-set recall margin. It would show behavior under a supplied cue on
one model. It would not show provenance discovery or general transfer.

Before any run, the project makes a **locked negative-result commitment**. In
plain English: whatever the test finds stays in the record. A null, harmful,
unstable, or shortcut-driven result will not be hidden merely because it makes
the idea less impressive.

If F1 and F2 improve over F0 but tie, credit the rule. If F2 reduces apparent
false corroboration by ignoring real stipulated convergence, reject it. If the
effect is matched by a metadata-only counter, survives without report text, or
disappears under label, position, style, parity, or relation-noise controls,
report a direct-code, formatting, or oracle-only result. If F2 is worse, report
harm. If it is null or unstable, preserve the null or instability.

### Optional real-world transfer check (`T1`)

The transfer audit recommends an optional descriptive check called **T1**. It
would ask whether the pattern appears in naturally repeated news articles, but
it would remain outside the main experiment because those datasets do not
supply all the ground truth the primary question requires.

NEWS-COPY can support a bounded same-original/dependent fixture because its
duplicate relation is defined as the same original source article. Its
nonduplicates cannot be called independent: shared quotations, same-story
articles, and breaking-news updates can be nonduplicates. Newswire records
large reproduction clusters, but its released row represents a cluster and
`cluster_size` is recurrence, not origin count.

Neither dataset supplies the claim, stance, exact evidence spans, support and
refute origin sets, real-world independence, or multiple-origin ground truth
needed by the primary protocol. NEWS-COPY rights remain unresolved; Newswire
version and field-level licensing must be pinned. Any future T1 has its own
rights and annotation manifest, remains descriptive, and stays outside all
primary and safety denominators, confidence intervals, tests, and effect
estimates.

### Current readiness

The local repository now contains ten closed JSON Schemas, a deterministic
fictional generator, strict parser, immutable raw-output receipts, fixed-
denominator scorer, prompt-parity scaffolding, leakage/shortcut diagnostics,
planning simulations, and seven passing focused offline tests. It contains no
selected model, intended-tokenizer lock, primary corpus lock, cleared blocked
surface classifier, completed semantic audit, pilot output, result,
preregistration, or publication authorization.

The small surface-only smoke corpus is trivially separable. That is a warning,
not a pass. The blocked leakage probe and semantic audit remain stop gates.

## Limitations that cannot be smoothed away

1. **No empirical evaluation.** No model or participant result exists.
2. **No broad novelty finding.** The mechanisms have extensive precedents; the
   residual contribution is narrow and search-dependent.
3. **No proven minimum.** Eleven responsibilities are a decomposition, not a
   universal implementation requirement.
4. **No validated constructs.** People and models may not reliably distinguish
   the proposed fields.
5. **No provenance discovery.** The study supplies synthetic relation values.
6. **No real-world independence.** `INDP` is benchmark-stipulated only.
7. **No truth result.** Provenance, support, authority, and truth remain
   separate.
8. **Open-world evidence remains incomplete.** Sources change, origins are
   obscured, and important material can remain inaccessible.
9. **Costs are unknown.** A legible process can still be too slow or expensive.
10. **Human control is unproven.** Review can become rubber-stamping.
11. **Memory can amplify error.** Retention can preserve stale, biased, or
    sensitive content.
12. **Transfer is unresolved.** Public syndication data do not supply the
    required ground truth, and rights gates remain.
13. **The historical web artifact is incomplete.** The v13 image is preserved
    with its supplied hash; the expected original standalone HTML is not
    available. The rendered DOM snapshot is not a substitute.
14. **The product cases are circular if treated as evidence.** They illustrate
    design boundaries only.
15. **The name may fail.** Reader comprehension can require renaming.
16. **No publication or deployment authorization.** This is a local owner-
    review package.

## Closing

The important move is not to count less. It is to count the right unit under a
stated rule and to preserve what remains unknown.

Nine repeated reports may matter as nine observations of circulation, framing,
or timing. They may amount to one origin for a corroboration claim. One
official source may be authoritative about a command and insufficient about
field reliability. A separate root may be independent only inside a synthetic
graph and irrelevant to the claim. A human may approve a sandbox step without
endorsing the underlying proposition. A later outcome may update policy
without rewriting history.

An AI system will make context judgments whether or not it names them. The
case for a discrimination layer is the case for making those judgments visible
early enough to contest: before recurrence becomes corroboration, before
access becomes permission, before selection becomes truth, and before a fluent
answer makes the path disappear.

Whether that visibility improves anything enough to justify its cost is not a
conclusion. It is the next question—and the program is committed to keeping a
negative answer.

## Evidence and status note

The verified source-by-source novelty boundary is in
`research/PRIOR_ART_DELTA_V1.md`. Natural-syndication feasibility and rights
limits are in `research/REAL_SYNDICATION_TRANSFER_FEASIBILITY_V1.md`. The
canonical scientific design is in `research/PAPER_PROSPECTUS_V1.md` and
`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md`. Offline implementation
status is in `research/F0_F1_F2_IMPLEMENTATION_READINESS_V1.md`.

The recovered v13 map remains an unchanged historical origin artifact, not the
current topology. The E2 nine-mentions image remains a labeled illustration,
not a dataset or result. H1 remains archived because its one-way aperture can
imply a gatekeeper the framework does not claim.

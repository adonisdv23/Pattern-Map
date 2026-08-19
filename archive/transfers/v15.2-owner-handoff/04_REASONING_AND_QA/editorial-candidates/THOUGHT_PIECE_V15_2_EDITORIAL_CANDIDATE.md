# Pattern Recognition: The Discrimination Layer

## What an AI system should preserve before it answers

**Candidate status:** v15.2 editorial candidate for local owner review
**Empirical status:** conceptual synthesis and an unrun research program. No model
has been selected for the study. No participant, field, transfer, deployment, or
published result is reported here.
**Term boundary:** in this essay, “discrimination” means technical
differentiation among information and possible actions. It does not mean social
classification or discriminatory treatment.

### How to read this

- **First impression, 60–90 seconds:** read “Nine tabs, one announcement” and
  “The first decision.”
- **Essential argument, about five minutes:** continue through “Three questions
  before the answer.”
- **Deeper design, 15–20 minutes:** add “Make correction possible,” the use
  boundary, and the objections.
- **Research and history, another 10–15 minutes:** read the final sections and
  follow the linked technical records.

The short route contains the conclusion. The longer routes explain what the
idea would have to survive.

## Nine tabs, one announcement

*Fictional illustration. No live data or result is being reported.*

A team is deciding whether a sandbox pilot of a data-migration tool is worth
ninety minutes of investigation. Production data are off limits. The claim on
the table is broad: “The tool is broadly validated.”

Nine favorable articles arrive through nine different sites. The headlines,
layouts, and wording differ. A summary says:

> Nine sources agree that the new tool is broadly validated.

Then someone traces the articles backward. All nine came from the same launch
announcement.

The articles have not become false. They may still tell us something about
reach, timing, or how the announcement travelled. But the summary has changed
what the reports mean as evidence. It has treated nine observations as nine
separate paths to information, then treated that apparent plurality as
corroboration.

That is the error this essay starts with. It is small enough to see in a
receipt and common enough to hide inside an ordinary answer.

## The first decision: what are we counting?

The illustrative receipt records four different things:

| Question | Recorded value |
| --- | --- |
| How many report observations arrived? | 09 |
| How many known common-origin clusters do they form? | 01 |
| How many origins currently support the broad validation claim? | 00 |
| What may the team do next? | HOLD · VERIFY ANOTHER ORIGIN RELATION |

The last number is the one that usually gets lost. One origin is known: the
launch announcement. But the receipt has not established that the announcement
supports the broad claim that the tool is validated in independent use. A
vendor can be the right source for what it announced and the wrong source for
whether the product works in the field.

So the supporting-origin count is zero. That does not mean the tool is
rejected. It means the broad claim is not ready to carry the weight the summary
gave it.

The next action is narrower: inspect the announcement, look for a separately
authored benchmark or failure report, record how that material relates to the
earlier report, and only then reconsider the claim. If a permitted synthetic
rollback check is useful, authorize that check separately. Its result would
change a pilot rule; it would not retroactively prove the broad claim.

This is the point of a decision receipt. It makes a hidden change in route
visible.

### Three plain relation states

The receipt uses technical labels in its deeper records, but the reader needs
three ordinary-language states first:

- **Shared path:** the report can be traced to an earlier artifact. Keep the
  report; do not count it as a new support path under this rule.
- **Separate only in this test:** the illustration or benchmark stipulates a
  separate origin. That is a property of the test, not a discovery about the
  real web.
- **Unresolved:** the relation has not been established. Do not turn missing
  knowledge into either dependence or independence.

The third state matters most. Unknown is the place a polished summary is
tempted to erase. Leaving it unresolved is not indecision for its own sake. It
is how an incomplete trail stays incomplete instead of becoming invented
corroboration.

### Receipt ORIGIN-EX-01

| Field | Value |
| --- | --- |
| Evidence status | Fictional illustration; no live data; no result |
| Decision in view | Whether a sandbox pilot is warranted |
| Permission | Sandbox only; no production data |
| Research budget | 90 minutes |
| Claim under review | “The tool is broadly validated.” |
| Observations | O01–O09, nine unordered report records |
| Known relationship | All trace to Origin A, one launch announcement |
| Counted supporting origins | 00 under the stated relation rule |
| Claim state | INSUFFICIENT |
| Recorded human decision | HOLD · VERIFY ANOTHER ORIGIN RELATION |

The rows are not a ranking. The receipt does not discover real provenance,
prove truth, or make a pilot decision on its own. It records a supplied
illustration so another person can inspect the counting rule and correct it.

## The judgment before the answer

An AI answer is the visible end of a route. Before a model writes, someone has
already decided:

- what was possible to acquire;
- which items count as the same report, version, or upstream artifact;
- which passages bear on the claim;
- what was omitted;
- when search stopped;
- what the system was allowed to use or disclose; and
- who could challenge the route.

A fluent answer can hide all of those choices. “Use better context” does not
say what better means. More authoritative, more relevant, more current, more
independent, cheaper to inspect, safer to disclose, and more likely to change a
decision are different properties. They can point in different directions.

Consider two ordinary pieces of material. An official manual may be the best
authority for a documented command, share an upstream source with ten
tutorials, say nothing about failure under load, and still be exactly relevant
to an implementation question. A community post may be a poor authority for
product policy, yet contain a separately reproduced failure that matters more
to a reliability decision. A single “quality” score would hide why each item
earned attention.

The proposal here is not to install a grander ranking function. It is to make
the pre-answer judgment inspectable long enough for a person to see what
entered the packet, what stayed out, and why.

## Three questions before the answer

The full project map breaks this responsibility into six families and eleven
records. That map is useful for implementation. A reader can understand the
public argument through three questions.

### 1. What did we actually see, and where did it come from?

Keep a report distinct from the thing it reports, the copy captured from a
mutable page, the normalized extract, and the summary written later. Record
which transformation happened, when, and by whom or what.

The technical word for that trace is provenance. It means a record of origin,
custody, transformation, and time. It does not mean that the material is true,
authoritative, independent, or permitted to use.

This first question prevents a URL count from silently becoming an origin count.
It also prevents a summary from gaining authority simply because its source
disappeared during compression.

### 2. What exact claim does this material support?

A report can be relevant without supporting the claim in view. A source can be
authoritative for one narrow question and silent about another. A citation can
be present while the cited passage contradicts, qualifies, or fails to reach the
proposition being made.

Keep at least these judgments apart:

- where the report came from;
- whether it follows a shared or unresolved path;
- what claim its evidence supports, refutes, or does not settle;
- how authoritative it is for that claim; and
- how relevant it is to the current decision.

This is why one known origin does not become one supporting origin in the
receipt. Relation and support are connected, but they are not interchangeable.

### 3. What may happen now?

The next action is not the same thing as the truth of the claim. A team may be
allowed to inspect a source but not retain it. It may have enough evidence to
run a bounded sandbox check but not to touch production data. It may decide to
hold, ask for clarification, acquire one missing perspective, answer
provisionally, defer, escalate, or refuse.

Record the permission, cost, uncertainty, and accountable person’s decision.
That decision is sometimes called a disposition in the technical records. In
plain language, it is the recorded next step.

A receipt should make a correction consequential. If a person changes a shared
path to unresolved, the count and route should change while the original report
remains in history. If nothing downstream changes, the review control is
decorative.

### What not to collapse into one score

The project does not claim that every judgment needs a separate machine or
database column. It claims that collapsing them too early hides the source of
an error.

Recurrence is not independent support. Provenance is not correctness. Technical
access is not permission. Relevance is not general importance. A human decision
is not an external fact. A later outcome can change a future rule without
rewriting what was known when the earlier decision was made.

The full distinction table, component IDs, and field-level records belong in the
Explore route and the technical package. The public essay needs the reason for
the separations and one receipt that makes the reason tangible.

## Make correction possible

The responsibility has two different time horizons.

The **current-decision loop** runs while a question is open. A missing expected
perspective may justify one targeted search. A contradiction may justify
comparison. A permission boundary may stop the route. A corrected relation may
change which support is counted. A budget may end the work.

The **outcome loop** begins later, if a defined outcome exists. It compares what
was expected with what was observed and proposes a change to a future policy.
The proposal needs an owner and a version. It cannot silently rewrite the old
packet to make the earlier decision look wiser than it was.

Both loops need preserved history. Keep observations, interpretations,
decisions, outputs, corrections, and outcomes as different record types. A
correction supersedes an interpretation; it does not erase the report. A later
result can revise a pilot rule; it does not travel backward and make the
original evidence omniscient.

This can be done at several levels:

- **Practice:** a researcher states the question, permission, evidence
  relations, material exclusions, stopping reason, and next decision.
- **Workflow:** a coordinating system carries identity, claims, relations,
  permissions, context, review, and receipts through retrieval and generation.
- **Model behavior:** prompts or training may encourage information seeking,
  abstention, and uncertainty, but cannot replace external identity,
  authorization, append-only records, or human authority.

These are placements, not maturity levels. A careful team practice can be more
useful than an elaborate service. A new product box does not become a
responsibility merely because it is named.

## When the overhead earns its place

The full treatment is plausible when a decision is consequential, contested,
dependence-heavy, time-sensitive, expensive to investigate, sensitive to
disclose, or likely to be revisited. Due diligence, a research evidence packet,
a production-change decision, and a source-sensitive investigation are the kinds
of work where a receipt can repay its cost.

It is probably unnecessary for a low-stakes rewrite, a direct format
conversion, a supplied-input calculation, or a bounded extraction with an
obvious source. In those cases, use a short brief, permission check, exact
inputs, and a simple note—or skip the layer altogether.

This negative space is part of the proposal. A framework that cannot say when
it is not worth using becomes a demand for ceremony.

## What earlier work removes from the claim

The component ideas are established territory. Work on copying and source
dependence, double counting in evidence synthesis, citation amplification,
reports versus underlying studies, provenance standards, duplicate detection,
retrieval diversity, claim-provenance graphs, and source-dependent RAG all
remove the easy version of the novelty claim.

The project therefore does not claim to invent provenance, deduplication,
truth discovery, retrieval diversity, claim graphs, evidence synthesis,
context engineering, or human review. The residual claim is narrower: a
boundary-preserving synthesis that keeps these judgments visible across the
pre-answer route, plus a test of one supplied origin cue against an explicit
rule.

Relevant primary and official precedents are linked in
research/PRIOR_ART_DELTA_V1.md and the Sources route, including:

- Dong, Berti-Équille, and Srivastava on copying and source dependence;
- Senn on dependence and double counting in meta-analysis;
- Greenberg on citation-network amplification;
- the Cochrane Handbook on several reports of one underlying study;
- W3C PROV-O on entities, activities, agents, and derivation;
- NEWS-COPY and Newswire on repeated news articles and reproduction clusters;
- Zhang, Ives, and Roth on natural-language claim provenance;
- MMR and SetR on diversity-aware retrieval and set-wise selection; and
- recent conflict, redundancy, and source-dependent RAG benchmarks.

A future literature review may narrow the claim further. If it finds a closer
integrated responsibility, the project should say so. Historical continuity
does not make a synthesis new, and a plausible interface does not make it
effective.

## How this could lose

A serious proposal should make its retirement tests visible.

**“Is this old work under a new label?”** Much of it is. If a strong,
matched-budget retrieval-plus-citation baseline performs as well at lower cost,
the extra structure should lose for that task.

**“Could the layer become a gatekeeper?”** Yes. Selection can erase peripheral
sources, encode institutional preferences, or make an exclusion look like
quality control. The remedy is not to hide selection. Show exclusions,
unknowns, reasons, permissions, source coverage, and appeal. If nobody can see
what was withheld or reverse the route, the design has failed.

**“Could the receipt become rigor theater?”** Yes. Perfect lineage for a false
claim is still perfect lineage for a false claim. A receipt earns its place only
if a recorded distinction changes a consequential decision or makes a correction
possible.

**“Will the overhead cost more than it saves?”** It may. Eleven responsibilities
are a map open to argument, not a required ceremony. The framework should
collapse for simple tasks and should lose whenever a simpler workflow delivers
the same decision quality for less cost.

**“Will human review be decorative?”** It will be if a reviewer sees a polished
recommendation but cannot inspect the relation, claim, exclusion, uncertainty,
or route—or if changing one of those does not change the packet. Oversight
should be a real control, not a signature at the bottom.

**“Could feedback optimize the wrong thing?”** Yes. Clicks, acceptance, speed,
and local preference are not automatically good outcomes. A future update
needs a predefined target, a measurement window, confounders, and approval.

These are not disclaimers added after the idea. They are conditions under which
the idea should shrink or retire.

## One narrow test, no result

The conceptual argument can be complete before an experiment. The empirical
surface cannot.

The current research question is:

> For one frozen model, does a supplied origin-relation field reduce false
> corroboration beyond the same evidence and an explicit rule that repeated or
> derived reports should not count as independent support?

No model has been selected. No study has run. The offline harness creates
fictional bundles, checks schemas, validates parsing, and exercises scoring
wiring. It does not produce a model finding.

### Three versions of one planned task

The test would give one model the same fictional evidence under three versions:

| Plain name | What changes | Role |
| --- | --- | --- |
| Ordinary task | Evidence assessment without an origin-counting rule or supplied relation labels | Secondary baseline |
| Rule-only task | The same evidence plus an explicit rule to preserve unknown and avoid counting repeated paths as independent | Primary comparator |
| Rule-plus-label task | The same rule and evidence plus benchmark-supplied labels for shared, separate-in-this-test, or unresolved relations | Primary intervention |

The important comparison is rule-plus-label against rule-only. It asks whether the
supplied cue adds anything beyond saying the rule out loud. The labels would be
stipulated properties of fictional test bundles. They would not discover real
provenance or establish universal independence.

The current plan names 300 primary fictional test cases. That is a design input,
not a result, confidence score, or count of people. The final tokenizer,
denominator, leakage checks, safety checks, and other pre-run gates remain
unresolved until a separate authorization and methods review. A transfer check
using real repetition patterns would be optional and descriptive; it would not
enter the main test’s evidence or safety denominator.

The project has made a useful promise in advance: if the cue is null, harmful,
unstable, or merely exploits formatting or a direct label, that result stays in
the record. A result that helps one narrow behavior would not validate the
whole framework. A negative result would shrink the mechanism claim, not be
spun into success.

## The map that came before

The earlier v13 map began with a different but related frustration: AI-assisted
work can feel competent and still feel stale. Its proposed leverage was
pattern recognition before generation—looking beyond the most visible material
for specialist comments, unanswered questions, unusual changes, and prior
observations that alter what a current one means.

The original map remains a historical anchor, preserved unchanged in the
repository. Its important caution also survives:

> Underweighted is a starting condition, not a conclusion.

The current version changes the center of gravity. Peripheral material is a
candidate acquisition strategy, not a truth signal. A velocity anomaly deserves
attention, not belief. A learning loop requires a defined outcome. The old
center-and-sequence picture is not being passed off as the current system map;
the current map keeps typed relations, terminal decisions, correction, and
separately versioned outcomes visible.

## What to remember

One week later, the framework name may be gone. The useful habit should remain:

> Before saying “many sources agree,” count the observations, check how many
> distinct information paths they represent, ask what exact claim each path
> supports, and leave unresolved relations unresolved. Record what a person will
> do next.

The aim is not to count less. It is to count the declared unit, keep unlike
judgments from laundering one another, and preserve the route early enough for
someone else to contest it.

That is a design proposition, not a result. The framework may be too costly,
too easy to game, too difficult to use consistently, or too close to existing
practice to deserve its own name. The next honest step is to let readers test
the receipt, let practitioners try the smaller version, and let the narrow
study succeed, fail, or show that the cue is only a shortcut.

## Canonical deep routes and boundaries

- **Explore:** six families, eleven responsibilities, loops, component records,
  and bounded cases.
- **Lab:** the unrun protocol, planned sample, parity and shortcut gates, and
  possible null/harm outcomes.
- **Sources:** prior-art ledger, glossary, and historical v13 record.
- **Canonical research files:** research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md,
  research/F0_F1_F2_IMPLEMENTATION_READINESS_V1.md, and
  research/REAL_SYNDICATION_TRANSFER_FEASIBILITY_V1.md.
- **Status:** local owner review; conceptual synthesis; unrun research program;
  not published.

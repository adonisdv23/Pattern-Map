# DL narrow-wedge research decision memo v0.1

Status: **DESIGN COMPARISON ONLY / UNRUN / NO RESULTS / NOT A PROTOCOL OR
PREREGISTRATION / NO PROVIDER, MODEL, CORPUS, DATASET, PARTICIPANT, SAMPLE SIZE,
REGISTRY, OR SPEND SELECTED**

Checked against targeted public primary/official sources: **2026-08-30**.

This memo compares two possible mechanism-isolated research directions before
the broader DL-PLAYBOOK-01 matched-budget study. It does not choose a first
paper, authorize a run, acquire material, call a model, recruit a person, or
claim an empirical contribution. Any of those steps requires a later exact
owner instruction and a separately frozen execution packet.

## 1. Decision this memo can support

The current decision is only which construct deserves additional specification
and prior-art review first:

- **Candidate A — claim-scoped influence receipt:** compare a compact record of
  which authorized material influenced which claims with an ordinary source
  list; or
- **Candidate B — typed observation-boundary missingness:** compare explicit
  classifications such as `NOT_OBSERVED`, `NOT_CHECKED`, `UNAVAILABLE`, and
  `NOT_AUTHORIZED` with ordinary narrative uncertainty or untyped gap language.

The decision is not whether Pattern Map works. It is not whether either
candidate is novel. It is not a choice of provider, model, corpus, participants,
sample size, or statistical test.

## 2. Contribution ceiling and adjacent-work warning

Both candidates overlap active fields. Document- and citation-attribution work
already asks which retrieved material contributes to an answer. Iterative RAG
work already represents evidence sufficiency and structured gaps. Memory and
deep-research benchmarks already test retrieval, revision, citation accuracy,
implicit criteria, and long-horizon state. A credible study therefore cannot be
premised on “nobody has done this.”

At most, a later study could test whether one precisely frozen, human-governed
interface or record changes a defined decision artifact under defined
conditions and costs. It could not establish a new general mechanism, an
exhaustive framework, or the value of all six families.

## 3. Side-by-side decision surface

| Dimension | Candidate A — influence receipt | Candidate B — typed missingness |
| --- | --- | --- |
| Intended mechanism | Make claim-scoped influence and authorization inspectable | Prevent observation limits, failed checks, unavailability, and lack of permission from collapsing into “absent” |
| Strongest potential value | A reviewer can focus correction on material that actually shaped a consequential claim | A reviewer can distinguish “not found within this boundary” from “does not exist” and can see when checking never occurred |
| Strongest case against | It may be citation theater: more formatting and reviewer burden without better decisions, and “influence” may be a post-hoc self-report rather than faithful attribution | It may be label-following theater: a model can emit the right status vocabulary without observing the boundary correctly, and the expected/observable ground truth may be impossible to freeze |
| Principal novelty uncertainty | Source/citation attribution, evidence ledgers, provenance interfaces, and rationale records are established | Gap judging, sufficiency control, uncertainty taxonomies, missing-data reasoning, and observation-boundary practices are established |
| Smallest isolatable question | Does the claim-to-source mapping change accepted-error or correction behavior beyond a source list with the same sources? | Does the typed distinction reduce false absence and decision errors beyond an equally explicit untyped boundary statement? |
| Main cue-leak risk | Receipt vocabulary, visible length, claim IDs, and structured formatting expose condition | Upper-case status labels, field count, and explicit “missingness” terminology expose condition |
| Human-work dependency | High if correction effort or acceptability is measured | Potentially lower for purpose-built known-state tasks; still high for real expectedness or domain judgment |
| Current sequencing recommendation | Wait until the receipt contract is semantically repaired and independently inspectable | Specify first as a construct-isolation exercise, but do not select it as the first empirical paper yet |

## 4. Candidate A — claim-scoped influence receipt

### 4.1 Frozen treatment concept required before review

The smallest candidate treatment would map each material decision claim to:

- one or more resolvable evidence records;
- source/artifact identity and exact support span where available;
- claim-scoped role and support;
- authorization state for influence;
- whether the item was selected, withheld, or left unknown; and
- the operator's bounded reason for influence.

It must not claim causal faithfulness merely because the generating system
self-reports influence. “Selected for the answer” is an inspectable workflow
record; it is not an explanation of model internals.

### 4.2 Strongest case against

The ordinary source list may already give reviewers enough information. Adding
claim IDs, spans, roles, and reasons can increase output length, expose the
treatment, and shift reviewer attention without changing the underlying
decision. A structured receipt can also create false confidence: an item may be
listed as influential because the prompt demanded a record, not because it
actually changed generation. If the comparison rewards receipt completeness,
the study would measure obedience to a format it supplied.

This candidate should be abandoned if its only defensible outcome is “the
treatment produced more structured fields.”

### 4.3 Adjacent work and novelty uncertainty

Relevant work includes document-level source attribution in RAG, sentence-level
citation and verification interfaces, provenance records, attribution-bias
evaluation, and auditable correction workflows. A targeted review would need
to distinguish:

- model-internal or counterfactual attribution;
- generated citation correctness;
- provenance and lineage;
- human-facing rationale or decision records; and
- the narrower claim-to-authorized-influence workflow proposed here.

Until that mapping is complete, a novelty claim is **UNRESOLVED** and must not
appear in a prospectus or abstract.

### 4.4 Construct-validity risks

- Self-reported influence may not be faithful to generation.
- Claim segmentation may be unstable or condition-dependent.
- Exact support can be complementary across sources rather than attributable to
  one span.
- A receipt can reward verbosity or provide a checklist cue.
- Reviewers may treat a source mapping as correctness.
- “Ordinary source list” can be a deliberately weak straw baseline.
- Correction time confounds reading length, interface familiarity, and domain
  expertise.
- Authorization and evidentiary support can be mistakenly fused.

### 4.5 Credible comparators

Before any omnibus playbook comparison, a mechanism-isolated design would need
at least:

1. **A0 — ordinary source list:** the same answer and available sources with an
   ordinary citation/source list, no claim-scoped mapping;
2. **A1 — generic diligence mapping:** the same answer requirement plus a
   concise request to say which source supports each important claim, without
   Pattern Map vocabulary; and
3. **A2 — typed influence receipt:** the smallest frozen treatment above.

An optional diagnostic arm could retain claim-to-source mapping while removing
authorization or influence-reason fields. It should exist only if the added
arm answers a predeclared mechanism question and its multiplicity/resource cost
is justified.

### 4.6 Candidate outcomes and guardrails

**Primary candidates, subject to later construct review:**

- decision accuracy or accepted-error rate on tasks with a frozen decision key;
- rate of unsupported or contradicted claims that remain influential; and
- proportion of artifacts reaching a predeclared acceptable state without an
  evidence or permission correction.

**Secondary only:**

- reviewer correction actions and elapsed review time;
- claim/evidence-link precision and recall against a frozen key;
- appropriate withholding of unauthorized material; and
- reviewer ability to locate the source of a seeded error.

**Guardrails:** answer quality cannot compensate for unauthorized influence,
false source support, fabricated spans, unresolved IDs, or a materially greater
review burden. Satisfaction and perceived professionalism are not primary
outcomes.

### 4.7 Resource estimands

Any later design must report two separately labeled comparisons:

- **fixed-total-resource:** instructions, context, output, tool calls, time, and
  review all count inside the same total budget; and
- **equal-operating-overhead:** each condition receives enough budget to
  produce its required interface, with the added operating cost reported rather
  than hidden.

The second cannot replace the first. Receipt length and reviewer reading time
are treatment costs.

### 4.8 Blinding and cue leakage

Outputs would need neutral rendering that removes framework names, status
tokens, table styling, headings, and nonessential length differences while
preserving the actual information being compared. The evaluator rubric cannot
reward fields unique to A2. If neutralization removes the proposed mechanism,
blinded outcome scoring and a separate interface-utility evaluation must be
treated as different studies.

### 4.9 Permission and participant gates

A model-only artifact comparison cannot measure real human correction effort.
Any reviewer-time, comprehension, or acceptance outcome requires separate
participant or expert-review authorization, ethics/privacy handling,
recruitment and compensation decisions, accessibility planning, and retention
rules. No private source material may be used merely because it is accessible.

### 4.10 Unfavorable outcomes and no-go conditions

Retain null, harmful, shortcut-driven, fragile, non-transfer, stopped, invalid,
and indeterminate outcomes. Stop or do not proceed if:

- no defensible distinction from established attribution or citation
  interfaces survives targeted review;
- receipt correctness cannot be scored independently of receipt format;
- claim segmentation or evidence identity cannot be frozen;
- the baseline omits a generic-diligence mapping;
- authorization cannot be separated from support;
- blinding is impossible for the primary outcome;
- human effort is called “measured” without authorized human work; or
- the semantically repaired receipt contract is not complete.

## 5. Candidate B — typed observation-boundary missingness

### 5.1 Frozen treatment concept required before review

The smallest candidate treatment would require every material gap statement to
name:

- the expected item or field and why it was expected;
- the observation boundary: sources, period, scope, and allowed operations;
- the check state;
- the typed status (`NOT_OBSERVED`, `NOT_CHECKED`, `UNAVAILABLE`,
  `NOT_AUTHORIZED`, `FAILED_CAPTURE`, `STALE`, or `SUPERSEDED` as applicable);
- the decision consequence; and
- what additional observation, permission, or evidence would change the state.

The vocabulary itself is provisional. A later design must justify every state
and avoid pretending that all domains share one complete missingness taxonomy.

### 5.2 Strongest case against

The candidate may measure nothing beyond forced label production. If a prompt
contains the exact categories and the task surface cues reveal the answer, a
model can fill the schema without better observation or judgment. Expectedness
is also domain- and decision-dependent: a supposed “known” absence can encode
the task author's assumptions rather than an external truth. In open-web work,
the complete observation universe is unknowable, making false-absence labels
difficult to adjudicate.

Structured gap judging and evidence-sufficiency control are already active
research areas. If the only distinction is a renamed set of status labels, this
candidate is not a defensible research wedge.

### 5.3 Adjacent work and novelty uncertainty

A targeted review must cover iterative gap/sufficiency controllers, selective
retrieval and stopping, missing-data and open-world reasoning, information
foraging/metareasoning, dataset annotation of unavailable or unanswerable
questions, versioned memory, and abstention/calibration. The candidate's only
possible distinct emphasis is the combined human-governed record of expected
item, observation boundary, permission/check state, and decision consequence.

That distinction is a **DESIGN HYPOTHESIS**, not a novelty finding.

### 5.4 Construct-validity risks

- “Expected” may reflect author bias or leakage.
- The observation boundary can be incompletely or inconsistently applied.
- Surface tokens may reveal the correct status.
- `NOT_OBSERVED` can be mistaken for nonexistence.
- `NOT_CHECKED`, failed capture, and unavailable access may be observationally
  indistinguishable without tool traces.
- Correct status classification may not change the downstream decision.
- A schema can increase calibrated language while reducing useful action.
- Closed synthetic tasks may not transfer to open-world research.

### 5.5 Credible comparators

A mechanism-isolated design would need at least:

1. **B0 — ordinary uncertainty:** answer the decision task and state material
   uncertainties in ordinary prose;
2. **B1 — generic boundary diligence:** explicitly state what was searched,
   what could not be checked, and why, without a supplied status taxonomy; and
3. **B2 — typed observation boundary:** the smallest frozen treatment above.

An optional diagnostic arm could provide the status vocabulary without the
expected-item rationale or decision consequence. It is justified only if it
isolates whether labels or boundary reasoning drive any difference.

### 5.6 Candidate outcomes and guardrails

**Primary candidates, subject to later construct review:**

- decision accuracy or accepted-error rate when a gap changes the correct
  action;
- false-absence rate: claims of nonexistence when the correct state is a
  bounded observation or failed/unperformed check; and
- correct consequential classification of check, access, and observation state
  against a frozen known-state key.

**Secondary only:**

- appropriate hold, qualify, or request-more-information behavior;
- unnecessary abstention or over-refusal;
- status calibration across paraphrase and evidence order; and
- resource and review burden.

**Guardrails:** a higher typed-status score cannot offset worse decision
accuracy, permission violations, manufactured expectedness, or harmful
over-refusal. Schema completion is never the primary outcome.

### 5.7 Resource estimands

As with Candidate A, report both fixed-total-resource and
equal-operating-overhead comparisons. The typed schema's tokens, additional
tool checks, delay, and reviewer burden are costs. Budget exhaustion is a stop
state and remains in the denominator under a predeclared policy.

### 5.8 Blinding and cue leakage

Task construction must remove direct lexical mapping from evidence to status
labels. Surface features such as “access denied,” missing cells, or explicit
timestamps cannot make the treatment answer trivial. Neutral evaluator views
should hide condition names and normalize style. Purpose-built items require a
separate leakage audit and held-out perturbations before they can support a
construct claim.

### 5.9 Permission and participant gates

No real private, inaccessible, or licensed system should be probed to create a
`NOT_AUTHORIZED` case. Purpose-built material may represent the state without
accessing a real restricted source. Any real-domain expectedness key requires
authorized subject-matter review; any human correction/comprehension measure
requires the separate participant gates described for Candidate A.

### 5.10 Unfavorable outcomes and no-go conditions

Retain null, harmful, shortcut-driven, fragile, non-transfer, stopped, invalid,
and indeterminate outcomes. Stop or do not proceed if:

- targeted review reduces the contribution to renamed gap labels;
- expectedness or observation boundaries cannot be independently frozen;
- a label can be solved from surface wording rather than observation;
- a generic boundary-diligence comparator is absent;
- the outcome rewards status completion instead of decision quality;
- false absence and harmful over-refusal are not separate guardrails;
- permission states would require real unauthorized access; or
- the design cannot separate a model-only artifact test from human outcomes.

## 6. Recommended sequencing—without selecting a study

1. **Repair the applied contracts first.** Candidate A cannot be evaluated
   while the influence receipt permits unresolved IDs, collapsed permission
   states, or post-hoc structure without substantive references.
2. **Specify Candidate B first as a construct-isolation exercise.** Its state
   distinctions can be mapped and adversarially tested without the complete
   receipt system or a participant study. This is a recommendation for design
   work, not a selection of the first empirical paper.
3. **Run a targeted novelty/construct review of both candidates.** Include the
   strongest adjacent interfaces and direct attempts to reduce each candidate
   to existing terminology.
4. **Choose at most one narrow wedge only after that review.** Selection would
   require a later owner decision and a versioned execution packet.
5. **Require O0/B0, generic-diligence, and mechanism-isolated conditions before
   the omnibus playbook.** If the isolated mechanism has no meaningful signal
   or adds unacceptable cost, do not proceed to DL-PLAYBOOK-01.
6. **Leave human correction for a separate authorization stage.** First decide
   whether a model-only, known-state artifact design can establish a useful
   construct without implying participant evidence.

## 7. Relationship to DL-PLAYBOOK-01

The omnibus playbook remains a future Research Track 02 candidate, not the
first automatic study. Before it is interpretable, the research program needs:

- an ordinary baseline;
- a credible generic-diligence comparator;
- one or more mechanism-isolated arms;
- fixed-total-resource and equal-operating-overhead estimands;
- decision accuracy or accepted-error as the primary decision-facing outcome;
- safety, permission, support, over-refusal, and burden guardrails; and
- evidence that the treatment is more than framework vocabulary or receipt
  formatting.

A failed or costly narrow mechanism is a reason to narrow or stop the omnibus
plan, not a reason to hide the mechanism result inside a composite.

## 8. Relationship to The Echo Problem

The Echo Problem remains separate Research Track 01. Its origin-accounting
protocol can inform dependence-related task construction, but it cannot define
Candidate A, Candidate B, or the six-family playbook. No Echo protocol, fixture,
power calculation, or implementation check is imported here as a result.

## 9. Decisions and actions explicitly deferred

The following remain **UNSELECTED AND UNAUTHORIZED**:

- first paper or empirical wedge;
- provider, model, version, configuration, or credentials;
- corpus, dataset, task packet, source material, or rights basis;
- participants, experts, recruitment, compensation, or ethics route;
- sample size, power target, primary analysis model, or registry;
- monetary budget;
- model call, pilot, dry run that produces study observations, or study run;
- preregistration, publication, deployment, or outreach.

This memo may guide further design review only. It contains no research result.

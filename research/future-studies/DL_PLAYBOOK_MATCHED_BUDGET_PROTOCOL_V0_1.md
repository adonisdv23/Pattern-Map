# DL-PLAYBOOK-01 matched-budget protocol candidate v0.1

Status: **SPECIFICATION ONLY / UNRUN / NO RESULTS / NOT PREREGISTERED / NO MODEL, PROVIDER, DATASET, OR PARTICIPANT SELECTED**

This document specifies a future controlled comparison. It does not authorize
or report a study. Every empirical, provider, participant, dataset, spending,
preregistration, publication, and deployment action requires a later exact
owner instruction.

## 1. Bounded research question

Under matched resource and evidence-access budgets, does an operational
Discrimination Layer playbook change the quality and correction burden of
evidence-sensitive decision artifacts relative to ordinary prompting?

The proposed primary estimand is the average condition difference, over a
predeclared task population, in a blinded composite or prespecified family of
outcomes covering:

1. decision usefulness;
2. supported novelty;
3. evidence diversity;
4. missing-perspective detection; and
5. human correction effort.

The final design must choose whether there is one primary outcome, a hierarchical
testing sequence, or multiplicity-controlled co-primary outcomes. V0.1 does
not make that statistical choice and therefore is not analysis-ready.

## 2. Study unit and task boundary

One unit is a versioned task packet plus one condition assignment, its complete
input/output/tool trace, and a blinded review record. A packet must define:

- the actual decision, audience, consequence, and reversibility;
- allowed source material and acquisition operations;
- expected perspectives, fields, comparisons, and relevant baselines;
- a claim/evidence key and intentionally unresolved states;
- permission, privacy, disclosure, and no-external-action boundaries;
- a task-specific usefulness rubric;
- an admissible time and resource envelope; and
- known leakage, ambiguity, and adjudication risks.

Initial packets should be controlled and rights-cleared or purpose-built. No
external corpus is named or acquired here. Synthetic material may isolate
constructs but cannot by itself establish real-world transfer.

## 3. Candidate conditions

### O0 — Ordinary prompting

The model receives the task, allowed materials, ordinary tool permissions, and
the same output requirement an informed user would normally provide. It does
not receive the six-family playbook or required receipt schema.

### D1 — Operational Discrimination Layer

The same model receives the same task, materials, permissions, and maximum
resource envelope plus the frozen operational playbook. It must leave the
defined compact decision/evidence receipt.

### Optional diagnostic conditions

These may be useful later but are not automatically part of the primary study:

- **O1 — Ordinary plus generic diligence:** a concise instruction to check
  sources and uncertainty, separating playbook structure from simply asking
  for care.
- **D1-L — Lightweight playbook:** the minimum decision, comparison,
  disconfirmation, influence, and stop record.
- **D1-Ablations:** remove one family or mechanism at a time only when the
  added multiplicity and sample requirements are justified.

The primary comparison must be chosen before any run. Adding weak baselines
after seeing results is not acceptable.

## 4. Matched-budget rule

O0 and D1 must use the same:

- model/provider/version and decoding configuration;
- task packet and allowed information boundary;
- maximum elapsed time;
- total context plus output token budget, with playbook instructions counted;
- tool-call and retry limit;
- permission and external-action envelope;
- paid-retrieval ceiling, normally zero unless separately authorized;
- human clarification and review budget; and
- stopping and failure rules.

Two costs must be reported, not hidden: the maximum assigned budget and the
actual resources consumed. If the playbook's instructions consume more of the
fixed context budget, that is part of the treatment cost. If an alternate
estimand gives both conditions enough overhead to operate, it must be labeled
separately and cannot replace the fixed-total-budget result.

Budget exhaustion is a stop status, not evidence sufficiency. A stopped unit
remains in the denominator according to a predeclared policy; it is not silently
dropped because an answer was incomplete.

## 5. Task-family coverage

A future task set should vary the reason upstream judgment matters:

- overlooked specialist or peripheral perspective;
- source-role and claim-support mismatch;
- recurrence with known, unknown, or distinct origin;
- motion with denominator or collection changes;
- expected absence mixed with failed capture or unavailable access;
- peer/period/structure comparison with intentionally incomparable fields;
- memory with stale, corrected, or superseded records;
- permission or disclosure boundaries;
- a low-stakes ordinary-path task where extra procedure should not help; and
- a defined future-outcome scenario for bounded learning.

Task families, difficulty, source count, answer length, and surface cues should
be balanced or modeled. At least one family should be held out from development
before any transfer claim.

## 6. Outcome definitions requiring freeze

### 6.1 Decision usefulness

A task-specific blinded rubric should ask whether the artifact supports the
named decision, distinguishes observation from interpretation, communicates
material uncertainty, and avoids irrelevant ceremony. Reviewers should not
reward length, format, or use of framework vocabulary.

### 6.2 Supported novelty

Count a non-obvious claim, option, comparison, or missing perspective only if
it is decision-relevant and adequately supported under the packet key. Report
unsupported novelty separately as a harm or error, never as creativity.

### 6.3 Evidence diversity

Measure coverage across predeclared source roles, perspectives, origins or
information paths, and comparison positions. Raw URL, publisher, or citation
counts are insufficient. Common-origin recurrence may be informative while
contributing no independent-support count.

### 6.4 Missing-perspective detection

Score correct identification of predeclared expected material and correct
classification of not searched, failed capture, unavailable, unauthorized,
stale, superseded, or genuinely not observed within the boundary. Measure
false gap and manufactured-absence calls separately.

### 6.5 Human correction effort

Potential measures include blinded reviewer time, number and type of edits,
claim/evidence corrections, permission corrections, clarification turns, and
whether the artifact reaches a prespecified acceptable state. Reading a longer
receipt is part of the cost. Satisfaction alone is not the outcome.

## 7. Guardrails

- unsupported or contradicted influential claims;
- false independence, absence, motion, or provenance-as-correctness errors;
- unauthorized acquisition, retention, disclosure, or proposed action;
- inappropriate certainty and failure to hold or qualify;
- harmful over-refusal and missed useful answers;
- answer length, latency, token/tool cost, and reviewer burden;
- exact evidence-span and source/artifact identity errors;
- leakage of condition labels or rubric language into judged outputs;
- disagreement and adjudication burden; and
- privacy, security, or sensitive-content incidents.

No favorable primary score overrides a material authorization, privacy, safety,
or invalidity failure.

## 8. Assignment, blinding, and evaluation

The future frozen design should:

1. assign conditions at the task-instance level using a recorded seed or
   balanced schedule;
2. prevent paired-condition contamination or explicitly model it;
3. render outputs into a neutral evaluation format that removes condition
   names and nonessential style cues;
4. train reviewers on a separate calibration set;
5. keep primary reviewers blind to condition and hypothesis where practical;
6. double-score a predeclared subset or all primary units;
7. record agreement and adjudication without treating agreement as truth;
8. preserve every raw output, parse failure, exclusion, correction, and
   denominator decision; and
9. distinguish model-generated receipts from independently verified ground
   truth.

A model stating that it followed the playbook is not compliance evidence. The
required artifacts and observable actions must be scored.

## 9. Analysis choices still open

Before a run, a statistical plan must fix:

- unit of analysis and clustering;
- primary outcome or multiplicity procedure;
- minimum practically meaningful effects;
- sample-size or precision rationale;
- handling of invalid, stopped, refused, and missing units;
- ordinal, binary, count, time, and cost models as appropriate;
- paired or blocked comparisons;
- task-family and reviewer effects;
- robust uncertainty intervals and sensitivity analyses;
- contamination, order, prompt, seed, and model-version checks; and
- criteria for any noninferiority claim on safety or support guardrails.

No sample size appears in v0.1 because the outcome scale, variance, clustering,
and decision threshold are not frozen. Choosing a round number would create
false readiness.

## 10. Unfavorable and invalid outcomes

The analysis must retain and explicitly classify:

- null;
- harmful;
- shortcut-driven;
- fragile;
- non-transfer;
- stopped by budget, deadline, permission, safety, or infrastructure;
- invalid because of parse/schema/identity failure, contamination, leakage,
  unblinding, or missing denominator; and
- indeterminate because uncertainty is too large for the predeclared decision.

A unit may be retained for some outcomes and invalid for another only under a
predeclared rule. Repairs after outcome inspection require a versioned
amendment and sensitivity analysis.

## 11. Hard stops and quarantine

Stop or quarantine the relevant route on:

- absent, revoked, or ambiguous authorization;
- any external action beyond the frozen envelope;
- secret, personal, licensed, or sensitive material outside the approved plan;
- unbounded or unapproved spend;
- model/provider/version drift that breaks the estimand;
- corrupted task or evidence identity;
- condition leakage that makes blinded scoring unreliable;
- material safety or privacy harm;
- implementation behavior that changes the task or evidence budget by
  condition; or
- inability to preserve raw outputs, costs, failures, and exclusions.

Resume requires a documented cause, bounded repair, new version, and the
authority named in the future execution packet. A stop is reportable, not a
reason to erase the unit.

## 12. Participant work is separate

Human correction effort could eventually require participant or expert-review
work. That stage needs its own owner authorization, ethics or exemption review,
consent, recruitment, compensation, accessibility, privacy, retention, and
safety plan. A model-only benchmark cannot claim real human correction effort
unless actual human work is authorized and measured. A future human study does
not authorize model/provider spending by implication.

## 13. Interpretation limits

Even a favorable, valid result would support only the frozen task population,
conditions, model/version, evidence boundary, budgets, reviewers, outcomes,
and analysis. It would not show that:

- the six families are newly invented or universally complete;
- the playbook replaces expertise or human accountability;
- peripheral material is true;
- provenance establishes correctness;
- recurrence establishes independence;
- Signal Foundry or another product implements or validates the framework;
- a controlled gain transfers to field decisions; or
- the Discrimination Layer should be mandatory for ordinary tasks.

## 14. Required future execution packet

Before any empirical run, create and obtain explicit owner approval for a
versioned packet containing:

- frozen protocol and analysis plan;
- task provenance, rights, leakage, and contamination audit;
- selected model/provider/configuration and reproducible environment;
- maximum cost and stop controls;
- permissions, privacy, retention, disclosure, and incident plan;
- evaluator rubric, training, blinding, agreement, and adjudication plan;
- deterministic dry-run and parser/schema QA that is clearly not a result;
- preregistration text and destination, only if separately authorized;
- participant materials and review, only if separately authorized; and
- an explicit instruction authorizing the exact run.

Until that packet and instruction exist, DL-PLAYBOOK-01 remains an unrun design
candidate with no results.

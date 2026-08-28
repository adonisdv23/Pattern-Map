# The six families

Status: v16 applied-framework specification. This document is a stable
reader-facing map for builders and operators. It is a design framework, not a
claim that the mechanisms below have been validated or that the families are
newly invented.

The Discrimination Layer names a responsibility: deciding what an AI-assisted
workflow should notice, compare, preserve, question, and allow to influence
generation. It may be a checklist, a set of tables, a workflow, a service, or
a combination of tools. No family requires a particular model, database,
graph, vendor, or user interface.

The six families are the public map. Mechanisms such as permission envelopes,
provenance, claim ledgers, routing, receipts, and versioned memory support the
families; they do not replace them.

## Compact map

| ID | Family | Reader question | Primary output | Non-negotiable boundary |
| --- | --- | --- | --- | --- |
| F1 | Peripheral signal | What might the default path have overlooked? | Candidate signal and acquisition receipt | Less-visible or unusual material is a reason to inspect, not a reason to believe |
| F2 | Source weighing | What role does each source play for this exact claim? | Source-role and claim-support record | Recurrence, authority, support, origin, relevance, and permission remain distinct |
| F3 | Velocity / motion | What is changing unusually relative to a relevant baseline? | Time-stamped motion observation | Change is an attention prompt, not a conclusion or forecast |
| F4 | Absence + memory | What should be present but is not, and what prior context changes the meaning of now? | Baseline-linked gap and versioned memory link | A gap needs an expected baseline; memory does not silently rewrite history |
| F5 | Structured patterns | What becomes visible through explicit comparison? | Comparison matrix and typed relationships | Similarity is not equivalence, causation, or independent corroboration |
| F6 | Learning loop | What did we expect, what happened, and what bounded update is justified? | Outcome review and proposed update | Outcomes preserve the original record and do not automatically change policy |

The order is useful for a first pass, but it is not a compulsory sequence. A
motion question may reveal a missing baseline; a source review may reveal a
common origin; a later outcome may require correcting the original comparison.
Receipts should show which families were used, skipped, or revisited and why.

## F1 — Peripheral signal

### What it does

Peripheral signal deliberately widens the information aperture beyond the
obvious query, dominant source, familiar vocabulary, or default retrieval
route. “Peripheral” is relative to this task and the observed information
boundary. It can include specialist material, dissenting descriptions,
low-prominence fields, adjacent disciplines, minority interpretations, or
sources that the default path would not have surfaced.

The operator records why a candidate was outside the default path and what
inspection it earned. The candidate remains a candidate until a separate
assessment establishes what, if anything, it supports.

### Observable procedure

1. Write the default path: the query, sources, vocabulary, time window, or
   product route that would otherwise be used.
2. Name one to three bounded expansion routes, such as a specialist source,
   counter-vocabulary, adjacent peer group, or dissenting perspective.
3. Acquire only within the permission and cost envelope.
4. Record candidate identity, acquisition result, and why it deserves
   inspection.
5. Send the candidate through source weighing, comparison, and disconfirmation
   before allowing influence.

### Inputs and outputs

- Inputs: decision brief, default-path record, expected perspectives, allowed
  sources, and remaining budget.
- Outputs: expansion query or route, candidate records, capture/failure
  receipts, and a reasoned disposition such as inspect, hold, exclude, or
  escalate.

### Boundaries and failure signals

- Peripheral does not mean true, valuable, independent, or safe.
- Novelty is not evidence of relevance.
- A failed capture is a retrieval failure, not evidence that the source or
  event does not exist.
- “The model did not see it before” is not an observable claim unless the
  information boundary is known.

### Implementation levels

- Lightweight: add one bounded alternate route and list candidates in the
  evidence register.
- Moderate: maintain route coverage, source identities, exclusion reasons, and
  an explicit missing-perspective check.
- Advanced: use a task-scoped route planner or corpus-coverage view, with
  human review and a hard enrichment budget.

## F2 — Source weighing

### What it does

Source weighing asks what a source or artifact can establish for a particular
claim and use. It keeps separate fields for source role, evidence of track
record in the relevant domain and time window, domain or claim-scoped
authority, directness, support, contradiction, relevance, independence,
recurrence, provenance, and operational permission.

A filing may be authoritative for what it filed, weak support for why an event
occurred, highly relevant to one decision, and unavailable for another use.
The framework does not produce a universal trust score.

### Observable procedure

1. Split the answer into claims small enough to be checked.
2. Identify the exact artifact and passage associated with each claim.
3. Record source role, relevant track-record evidence (or `UNKNOWN`), and
   claim-scoped authority as separate judgments.
4. Assess support, contradiction, qualification, or insufficiency separately.
5. Record origin and recurrence state; do not count copies as independent
   support.
6. Record whether acquisition, retention, disclosure, and action are
   permitted.

### Inputs and outputs

- Inputs: source and artifact identity, exact spans, claim, domain standard,
  relevant track-record evidence, origin relations, task relevance, and
  permission policy.
- Outputs: source-role record, claim/evidence relationship, uncertainty,
  contradiction or qualification links, and an influence recommendation.

### Boundaries and failure signals

- Provenance is not correctness.
- Authority is not universal trust.
- Technical access is not permission.
- A citation is not proof of entailment.
- Recurrence is not corroboration when reports share an origin or pathway.

### Implementation levels

- Lightweight: use a four-column note: source role, relevant track-record
  evidence, what it supports, and what remains unknown.
- Moderate: use a claim-level evidence register with typed relationship states.
- Advanced: preserve source, artifact, version, derivation, and claim graphs
  with domain-specific review.

## F3 — Velocity / motion

### What it does

Velocity or motion notices a rate, direction, or change that deserves
inspection relative to a relevant history or comparison set. It can concern
frequency, timing, language, behavior, availability, or another observable
attribute. The operator must define the measure, time points, comparison set,
and baseline before interpreting a movement.

### Observable procedure

1. Define the measured attribute and event-time rule.
2. Collect at least two comparable time-stamped observations when making a
   motion claim.
3. State the baseline: prior period, peer set, seasonal pattern, or expected
   rate.
4. Check for measurement, collection, policy, or denominator changes.
5. Label the result as motion observed, motion uncertain, or no supported
   motion.
6. Route the attention prompt to comparison or acquisition; do not turn it
   directly into belief or action.

### Inputs and outputs

- Inputs: time-stamped observations, denominator, baseline, comparison set,
  measurement method, and known collection changes.
- Outputs: motion observation, assumptions, anomaly or no-anomaly state,
  uncertainty, and a bounded next action.

### Boundaries and failure signals

- One timestamp is not velocity.
- A rate change may reflect measurement drift, seasonality, manipulation, or
  noise.
- An unusual movement is not a forecast.
- A pattern seen after the outcome window is not a prospective expectation.

### Implementation levels

- Lightweight: compare current and prior values with a written baseline and
  one alternative explanation.
- Moderate: preserve the series, denominator, time window, and collection
  changes in a table.
- Advanced: use versioned time-series and anomaly tooling, with domain review
  of thresholds and false-alert costs.

## F4 — Absence + memory

### What it does

This family combines two disciplines that prevent the present from being
interpreted in a vacuum:

- Absence: identify something expected but not observed against a named
  baseline, and classify the gap as not searched, unavailable, failed capture,
  unauthorized, stale, or genuinely not observed within the boundary.
- Memory: retrieve relevant prior observations, decisions, corrections, and
  outcomes with their version, provenance, and scope intact.

### Observable procedure

1. State what was expected and why: a perspective, field, period, document,
   measurement, or prior decision.
2. Test whether the observation boundary was complete enough to call it a gap.
3. Distinguish missing, inaccessible, unauthorized, failed, stale, and
   superseded states.
4. Retrieve prior records by task, time, and source scope.
5. Link the current interpretation to prior records without overwriting them.
6. If memory conflicts with current evidence, preserve both and escalate or
   reconcile explicitly.

### Inputs and outputs

- Inputs: expected baseline, observation boundary, retrieval result, prior
  records, retention policy, and version links.
- Outputs: typed gap record, memory citations, staleness or supersession
  flags, and a route such as acquire, hold, answer with caveat, or escalate.

### Boundaries and failure signals

- An absence flag is not proof of nonexistence.
- Private, deleted, unavailable, or unauthorized material is a typed gap, not
  factual absence.
- Memory is not a timeless fact store.
- A summary may not silently replace the underlying observation or decision.

### Implementation levels

- Lightweight: write an “expected / observed / unknown” table and cite one
  prior decision or state “no relevant memory found.”
- Moderate: retain append-only observations, corrections, and supersession
  links.
- Advanced: use versioned memory retrieval with source-bound filters, stale
  flags, access controls, and correction workflows.

## F5 — Structured patterns

### What it does

Structured patterns make comparison explicit. The operator chooses the objects,
attributes, periods, relationships, and comparison rule before treating a
recurrence or difference as meaningful. The framework supports peer, period,
attribute, structural, and origin comparisons.

Comparison is where common-origin accounting belongs as one useful mechanism.
Nine reports can be nine observations and one known upstream announcement.
The common-origin relation changes the interpretation of recurrence; it does
not erase the observations or prove that the upstream announcement is correct.

### Observable procedure

1. Define the comparison question and unit of comparison.
2. Choose a matched set or explain why the set is intentionally asymmetric.
3. Align definitions, time windows, denominators, and missing fields.
4. Mark exact matches, differences, unknowns, and incomparable fields.
5. Trace origin, derivation, and shared pathways where recurrence matters.
6. State what the comparison makes visible and what it cannot establish.

### Inputs and outputs

- Inputs: comparable records, attributes, time windows, relationship evidence,
  origin links, and gap baseline.
- Outputs: comparison matrix, typed relationship edges, origin clusters or
  unknowns, and candidate interpretations for review.

### Boundaries and failure signals

- Different URLs, publishers, or wording do not establish independence.
- Similarity is not equivalence or causation.
- A peer set may encode the operator’s selection bias.
- Unknown origin must remain unknown.

### Implementation levels

- Lightweight: a two- or three-row comparison table with one explicit
  “not comparable” cell.
- Moderate: versioned comparison matrices and origin notes.
- Advanced: typed relationship graphs and queryable cohort definitions, with
  human review of entity resolution.

## F6 — Learning loop

### What it does

The learning loop compares a recorded expectation, route, decision, cost, and
defined outcome with what later happened. It proposes a bounded update to a
query, baseline, source policy, threshold, or review rule while preserving the
old record and the reason for the update.

### Observable procedure

1. Record the expectation and success, abstention, or escalation condition
   before the outcome window closes.
2. Define the outcome, measurement window, attribution boundary, and missing
   outcome state.
3. Capture observed outcome, actual cost, corrections, and confounders.
4. Compare expected and observed without rewriting the original receipt.
5. Separate a proposed policy update from a factual update.
6. Request authorized human disposition before applying any policy or memory
   change.

### Inputs and outputs

- Inputs: original decision and influence receipts, expected outcome, outcome
  window, observed result, cost, missingness, and relevant context changes.
- Outputs: outcome review, calibration or mismatch notes, bounded update
  proposal, and disposition record.

### Boundaries and failure signals

- A later outcome does not prove the earlier reasoning was right or wrong.
- Correlation is not causal attribution.
- User satisfaction alone is not a defined decision outcome.
- Policy updates must not erase prior evidence, uncertainty, or dissent.

### Implementation levels

- Lightweight: maintain an expectation/outcome table and propose one change.
- Moderate: append outcome reviews and link them to prior receipts and
  versions.
- Advanced: evaluate policy variants under approved matched-budget tests;
  preserve null, harmful, shortcut, fragility, and non-transfer outcomes.

## Cross-family invariants

These statements should appear in an operator receipt whenever the relevant
family was used:

1. Peripheral is a candidate status, not a truth status.
2. Recurrence is not independent corroboration.
3. Provenance is not correctness.
4. Technical access is not operational permission.
5. Motion and absence are baseline-dependent.
6. Unknown relations stay unknown.
7. Human disposition is a decision record, not a fact.
8. Outcome learning proposes bounded updates and preserves history.

## Minimum evidence of use

A reviewer should be able to inspect the decision brief, the acquisition or
failure receipt, the comparison or gap record, the disconfirmation attempt,
the uncertainty and permission fields, the stop/escalation reason, the
influence receipt, and—when applicable—the later outcome review. A fluent
answer without those artifacts is not evidence that the procedure was followed.

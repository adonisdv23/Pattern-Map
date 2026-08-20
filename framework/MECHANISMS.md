# Cross-family mechanisms

Status: v16 implementation guidance. These mechanisms are reusable supports
for the six families; they are not a replacement map and they do not imply
that one technical architecture is required.

## Families versus mechanisms

| Families answer | Mechanisms make observable |
| --- | --- |
| What the workflow should notice and compare | The decision frame and route |
| Which historical practices remain visible | The source, artifact, and claim records |
| How to treat motion, gaps, memory, and recurrence | Baselines, typed relationships, and versions |
| What may influence generation | Selection, withholding, and an influence receipt |
| How the workflow should stop and learn | Cost, stop, disposition, and outcome records |

The same mechanism can serve more than one family. For example, a source and
artifact identity supports both peripheral acquisition and source weighing;
an expected baseline supports both motion and absence; a versioned receipt
supports both human correction and the learning loop.

## M01. Decision brief and permission envelope

### Purpose

Name the real decision before collecting material. A brief makes the
consequence, audience, intended use, owner, expected baseline, permitted
operations, and resource limits visible. The permission envelope distinguishes
what a tool can technically reach from what the operator is allowed to acquire,
process, retain, disclose, or act upon.

### Required fields

- decision ID and version;
- question, intended use, audience, and decision owner;
- consequence level and time window;
- allowed and prohibited actions;
- technical access, operational permission, retention, and disclosure state;
- expected perspectives, fields, periods, or comparison set;
- time, money, latency, token, compute, privacy, and reviewer-attention budget;
- answer, provisional, abstain, hold, and escalation conditions;
- outcome definition and measurement window, when a learning loop is intended.

### Failure and recovery

If the question is vague, ask one clarifying question or record a provisional
interpretation. If permission is absent or ambiguous, stop acquisition and
escalate. If the brief changes materially, version it and re-check downstream
receipts; do not silently reuse a packet produced for the earlier brief.

## M02. Bounded acquisition and capture receipt

### Purpose

Acquire candidates because they could reduce a named uncertainty or fill a
baseline-linked gap, not merely because more material is available. Every
attempt creates either a capture receipt or a failure receipt.

### Required fields

- route or query and why the default path was insufficient;
- source and artifact identity, if available;
- permission decision and permitted use;
- expected information benefit;
- time, monetary, latency, and attention estimate;
- capture result, failure type, or partial result;
- transformation and tool version, if transformed;
- next action and remaining budget.

### Failure and recovery

Scope creep returns to the brief. A paid, private, sensitive, or externally
consequential operation without permission is a hard stop. A timeout, parser
error, robots denial, missing field, or unavailable source remains a failure
state; it is not negative evidence about the world.

## M03. Evidence spine

### Purpose

Keep source, artifact, capture, version, exact span, observation time,
transformation, and derivation distinct enough that a reviewer can reconstruct
what was available and how it changed.

### Minimum record

| Field | Why it matters |
| --- | --- |
| Source identity | Who or what issued or made the artifact available |
| Artifact identity | Which bounded object was observed |
| Version or digest | Which state was observed |
| Capture time and event time | When it was seen versus when it concerns |
| Exact span or pointer | What supports the claim |
| Transformation | How extraction, normalization, or summary changed it |
| Relationship state | Support, contradiction, recurrence, common origin, or unknown |
| Access and retention state | Whether use is permitted and how long it may be held |

Provenance makes inspection possible. It does not establish correctness,
authority, independence, relevance, or permission to act.

## M04. Typed comparison and relationship record

### Purpose

Make recurrence, common origin, similarity, contradiction, and comparison
explicit. A relationship is an assertion with evidence and uncertainty, not a
decorative label.

### Relationship vocabulary

- SUPPORTS: the exact evidence supports the narrow claim under the stated
  standard;
- CONTRADICTS: the exact evidence conflicts with the narrow claim;
- QUALIFIES: the evidence limits scope, condition, or interpretation;
- RECURRENCE: the claim or pattern appears again;
- COMMON_ORIGIN: evidence suggests shared upstream material or pathway;
- COMPARES_WITH: the records are in the declared comparison set;
- INDEPENDENT: a justified distinct origin or pathway;
- RELATED: a relation exists but independence is not established;
- UNKNOWN: available evidence cannot distinguish the relation;
- INCOMPARABLE: the records cannot be aligned for the stated question.

The most conservative state that preserves the evidence is preferred. Unknown
origin is not independent. Recurrence is not corroboration. Similarity is not
causation.

## M05. Disconfirmation and uncertainty review

### Purpose

Challenge the emerging interpretation before generation or action. The
procedure must seek a strongest contrary item, a missing perspective, an
alternative explanation, and a common-origin or measurement-change explanation
where applicable.

### Required disconfirmation record

1. Leading interpretation or candidate claim.
2. What would weaken or falsify it.
3. Search or comparison route used.
4. Contrary, limiting, missing, or differently rooted material found.
5. What remains unresolved and why.
6. Whether the unresolved state changes the route, wording, or permission.

### Uncertainty vocabulary

Use a typed note such as UNKNOWN, AMBIGUOUS_IDENTITY, INSUFFICIENT_SUPPORT,
CONTESTED, STALE, MISSING_BASELINE, FAILED_CAPTURE, UNAUTHORIZED,
INCOMPARABLE, or OUTCOME_MISSING. Do not collapse these into a single
confidence number.

## M06. Bounded route, cost, and stop policy

### Purpose

Choose whether the next permitted action is worth its expected benefit and
risk. The route is a recommendation or approved workflow step; it is not
automatic authority to act outside the envelope.

### Route choices

| Route | Use when | Required record |
| --- | --- | --- |
| ACQUIRE | A named gap or uncertainty may be reduced within permission and budget | Acquisition proposal and result |
| COMPARE | The claim needs peers, periods, structures, or origins | Comparison frame and result |
| CLARIFY | The question, audience, or authority is underspecified | Clarifying question and answer |
| ANSWER | Evidence and permission are sufficient for the bounded use | Influence receipt and caveats |
| ANSWER_PROVISIONALLY | The task can proceed while named uncertainty remains | Uncertainty and abstention wording |
| HOLD | A consequential uncertainty or permission issue blocks influence | Hold reason and owner |
| DEFER | A later time or missing input is required | Trigger and re-entry condition |
| ESCALATE | Human or domain authority must decide | Destination, question, and no-action boundary |
| REFUSE | The requested action is prohibited or unsafe within the envelope | Reason and safe alternative |

Route and stop are separate fields. Use exactly one route value from the table
above. Record the current stop state as `CONTINUE`, `COMPLETE`,
`STOPPED_BUDGET`, `STOPPED_DEADLINE`, or `STOPPED_OTHER`, with a reason and a
resume condition when one exists. Budget or deadline exhaustion therefore does
not become a route; for example, an operator may `ANSWER_PROVISIONALLY` with
`STOPPED_BUDGET`, or `HOLD` with `STOPPED_DEADLINE`. Plain-language
“abstention” maps to `HOLD`, `DEFER`, or `REFUSE` according to why no answer or
action is allowed.

Learning has its own state: `LEARNING_PLANNED`, `LEARNING_PENDING_OUTCOME`,
`LEARNING_REVIEWED`, or `LEARNING_NOT_APPLICABLE`. Do not use a learning state
as a route or treat a missing future outcome as a failed present answer.

### Cost dimensions

Record at least the dimensions that can bind the task:

- elapsed time and deadline risk;
- money or paid retrieval;
- model tokens and compute;
- reviewer attention and correction time;
- privacy, retention, disclosure, and security exposure;
- latency or opportunity cost;
- risk of misleading influence or external action.

Do not report budget exhaustion as evidence sufficiency. Record stop status
`STOPPED_BUDGET` with the remaining uncertainty and a permitted route.

## M07. Context packet and influence receipt

### Purpose

Give generation or human decision-making a bounded, reviewable context. The
packet carries selected evidence and its reasons, exclusions, unresolved gaps,
permission state, and constraints. The receipt records what was allowed to
influence the answer and what was withheld.

### Minimum packet contents

- packet ID, decision brief version, and evidence snapshot;
- selected item IDs and exact spans or pointers;
- claim/evidence links and source roles;
- common-origin, recurrence, comparison, or gap notes;
- exclusions and their reasons;
- unresolved uncertainty and abstention instructions;
- disclosure and retention constraints;
- expected output and human review boundary.

### Influence fields

For each influential item, record:

- item and claim ID;
- influence role: supports, qualifies, contradicts, frames, or routes;
- why it was admitted;
- what it cannot establish;
- permission and disclosure status;
- reviewer or policy disposition.

Withholding is not deletion. A withheld item remains inspectable unless a
separate retention or deletion policy says otherwise.

## M08. Human disposition and escalation

### Purpose

Keep accountable judgment visible. A person or authorized role may accept,
reject, defer, hold, override, request enrichment, correct a relationship,
revise the brief, or revoke permission. The record should show the scope of the
decision and its reason.

### Escalate when

- the action could materially affect people, money, access, safety, rights, or
  reputation;
- identity, provenance, permission, or source relation is unresolved;
- a critical gap cannot be filled within the budget;
- the evidence conflicts on a decision-critical claim;
- a policy or memory update would affect future tasks;
- the operator is being asked to treat a candidate or model confidence as a
  fact.

Escalation does not mean “the human will agree.” It means the unresolved
question and no-action boundary are made explicit.

## M09. Versioned memory and outcome review

### Purpose

Preserve prior observations, decisions, corrections, packets, outcomes, and
updates. A current view can be convenient, but it must link back to the prior
state and explain supersession.

### Outcome review fields

- original expectation, route, and influence receipt;
- outcome definition and measurement window;
- observed result, actual cost, and missingness;
- context changes, corrections, and plausible confounders;
- what was learned, what was not learned, and what remains unknown;
- one bounded update proposal;
- authorized disposition and new version, if applied.

An outcome can motivate a question or bounded proposal. It does not prove
causality, prove that an earlier interpretation was correct, or permit silent
policy rewriting.

## Cross-family state transition

~~~mermaid
stateDiagram-v2
    [*] --> PROPOSED
    PROPOSED --> NOT_AUTHORIZED: permission absent or revoked
    PROPOSED --> AUTHORIZED: permission and budget recorded
    AUTHORIZED --> OBSERVED: capture succeeds
    AUTHORIZED --> FAILED: capture or transformation fails
    OBSERVED --> RELATED: relationship assessed
    RELATED --> ASSESSED: source, comparison, and uncertainty reviewed
    ASSESSED --> HELD: critical gap, conflict, or cost block
    ASSESSED --> SELECTED: allowed to influence with reason
    ASSESSED --> EXCLUDED: withheld with reason
    HELD --> ESCALATED: human or domain decision required
    SELECTED --> VERSIONED: packet and influence receipt saved
    VERSIONED --> SUPERSEDED: later correction or newer evidence
    FAILED --> HELD: failure affects the decision
    SUPERSEDED --> VERSIONED: current view links history
~~~

This state sketch is a record vocabulary, not a promise that every
implementation needs a state machine.

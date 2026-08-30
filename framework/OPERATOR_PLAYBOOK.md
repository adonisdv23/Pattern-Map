# Practical operator playbook

This playbook is for a person or agent preparing an evidence-sensitive answer
or decision. It is deliberately stack-neutral. The operator can implement it
with a notebook, Markdown files, a spreadsheet, or software.

## Start with the smallest useful route

First apply Stage 0. Ordinary is valid only for a reversible transformation of
user-supplied material that requires no material claim judgment, comparison,
selection or withholding, permission resolution, memory reuse, new
acquisition, externally consequential influence, or a separate human action
gate. That path returns only its four-field terminal record; it is not an `ANSWER` route or an influence
receipt.

For every other task, ask four questions to choose the smallest layered route:

1. Is the task consequential, hard to reverse, sensitive, or likely to be
   reused as memory?
2. Is new acquisition, comparison, or permission judgment required?
3. Can a person correct a wrong answer quickly?
4. Is there a later outcome worth comparing with an expectation?

If the answers are mostly no, use the lightweight route. If any answer is yes,
create a decision brief and choose a cost boundary before searching. These
questions select a layered level; they do not override Stage 0 or grant human
authority for externally consequential action.

## The operating sequence

### 1. Frame the decision

Write one sentence for the decision and one for the intended use. Record the
owner, audience, consequence, deadline, and what would count as a useful
answer. Do not substitute “find information” for the actual decision.

Output: decision brief, version 1.

### 2. Set permission and cost

List what is technically reachable and separately what is authorized. Name
allowed acquisition, processing, retention, disclosure, and action. Set the
time, money, token, compute, privacy, latency, and reviewer-attention limits.
Include a no-action boundary.

Output: permission envelope and budget.

### 3. Write the default path

Record the query, familiar sources, vocabulary, time window, or product route
that would be used without deliberate discrimination. This is a comparison
point, not an admission that the default path is wrong.

Output: default-path note.

### 4. Add one bounded peripheral route

Choose one route the default path is likely to underrepresent: a specialist
source, alternative vocabulary, dissenting view, adjacent peer set, or lower
prominence field. State why it is relevant and stop after the route’s stated
budget. Record every failed capture as a failure, not as absence.

Output: acquisition proposal and capture/failure receipt.

### 5. Build the evidence register

For each candidate, record source, artifact, version or time, exact span,
observed metadata, claim, source role, relevant track-record evidence,
claim-scoped authority, support state, origin/recurrence state,
relevance, permission, uncertainty, and disposition. Keep the raw item
separate from interpretation.

Output: evidence register.

### 6. Compare before concluding

Choose the comparison that can change the decision:

- a peer or alternative;
- a prior period or baseline;
- a different source role;
- a structural or attribute comparison;
- an origin or pathway comparison.

Align definitions and mark incomparable cells. Do not call multiple copies
independent. Preserve UNKNOWN when origin or support cannot be established.

Output: comparison matrix, baseline record, or gap/memory record.

### 7. Inspect motion and absence

For motion, require repeated comparable observations and a baseline. For
absence, write what was expected and classify why it was not observed. Retrieve
relevant prior decisions and corrections without overwriting them. A gap may
mean not searched, inaccessible, unauthorized, failed, stale, or superseded.

Output: motion observation, typed gap, and memory links where applicable.

### 8. Disconfirm the leading interpretation

Write what would weaken the emerging answer. Search for the strongest contrary
source, missing perspective, alternative explanation, measurement change, or
shared origin. Record what was searched, what was found, and what remains
unresolved.

Output: disconfirmation log.

### 9. Route, stop, or escalate

Choose ACQUIRE, COMPARE, CLARIFY, ANSWER, ANSWER_PROVISIONALLY, HOLD, DEFER,
ESCALATE, or REFUSE. A route must name its reason, expected benefit, cost,
permission, uncertainty, and stop condition. Separately record stop status
CONTINUE, COMPLETE, STOPPED_BUDGET, STOPPED_DEADLINE, or STOPPED_OTHER; never
use that status in place of the route.

Hard stop and escalate if permission is absent, a critical identity or
provenance check fails, a high-consequence claim remains materially
unsupported, the no-action boundary is reached, or an external action would
require authority the operator does not hold.

Output: route and stop/escalation receipt.

### 10. Record influence

Create a bounded context packet or answer plan. List selected material,
excluded material, claim links, source roles, uncertainty, disclosure limits,
and the reason each selected item may influence the answer. A withheld item is
not deleted. If the answer is provisional, state the missing evidence and what
would change the conclusion.

Output: context packet and influence receipt.

### 11. Generate and preserve the boundary

Generate only within the packet and brief. Separate observation, interpretation,
recommendation, and human decision. Do not turn a disposition into a fact.
Leave externally consequential action to the named authority.

Output: versioned answer or decision brief with caveats.

### 12. Close the loop

Before the outcome window closes, record the expectation, success or abstention
criterion, and measurement. Later, compare the observed outcome, actual cost,
missingness, corrections, and confounders. Propose one bounded update, request
disposition, and keep the original receipt unchanged.

Output: outcome review and update proposal.

## Decision table

| Situation | Route | What the operator must say |
| --- | --- | --- |
| Exact reversible transformation of all named supplied material; no Stage 0 disqualifier | — (terminal ordinary record, not a route) | Supplied scope, material assumptions, unchecked boundaries, and output |
| Low consequence, supplied evidence, easy correction, but material judgment or selection is required | ANSWER on the lightweight route | What was judged, selected or withheld, assumed, and not checked |
| One material gap, reversible decision, authorized low-cost search | ACQUIRE | Which gap, expected benefit, cost limit, and stop rule |
| Repeated reports with unclear relation | COMPARE or HOLD | Recurrence observed; independence UNKNOWN until supported |
| High-consequence claim with missing baseline | HOLD or ESCALATE | Baseline missing; no factual absence or motion conclusion |
| Technical access exists but permission is absent | REFUSE acquisition or ESCALATE | Access is not authorization; no retrieval or disclosure |
| More search would mostly duplicate current material | ANSWER_PROVISIONALLY, HOLD, or DEFER; stop status `STOPPED_BUDGET` or `STOPPED_OTHER` | What remains uncertain and why more work is not worth the current cost |
| Evidence supports a narrow statement but not its explanation | ANSWER_PROVISIONALLY | State the supported observation and withhold the causal claim |
| Later outcome conflicts with expectation | — (outcome-learning review, not a route) | Preserve the original receipt; use the outcome-review record, request human disposition, and propose—never silently apply—an update |

## Receipt minimum

The reviewer should be able to answer:

- What was the decision?
- What was allowed and what was merely technically possible?
- What did the operator acquire, compare, and fail to acquire?
- Which family or mechanism produced each record?
- What is observed versus interpreted?
- What is the strongest unresolved uncertainty?
- Why did the operator stop, hold, or escalate?
- What influenced the answer and what was withheld?
- Who may authorize the external consequence?
- What later outcome would update the practice?

If the answer to one of these is unavailable, mark the field UNKNOWN or
NOT_RECORDED. Do not fill it with a plausible story.

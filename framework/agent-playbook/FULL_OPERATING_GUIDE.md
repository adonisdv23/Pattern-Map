# Full operating guide for agents

Status: v16 applied procedure. This guide defines observable agent behavior.
An agent that follows it leaves records; it does not merely claim that it
“thought differently.” The guide does not grant permission to spend, contact,
publish, deploy, or act externally.

## 0. Decide whether evidence-selection work exists

Before choosing a level, ask: **Does the task require any material claim
judgment, comparison, selection or withholding, permission resolution, memory
reuse, new acquisition, or externally consequential influence, rather than
only a reversible transformation of user-supplied material?**

Ordinary is valid only for a reversible transformation of user-supplied
material that requires no material claim judgment, comparison, selection or
withholding, permission resolution, memory reuse, new acquisition, or
externally consequential influence.

- If no, use the ordinary path: perform the reversible supplied-material
  transformation, save only the supplied scope, material assumptions,
  unchecked boundaries, and output, and stop. Do not manufacture evidence,
  route, stop, outcome, learning, or six-family records. Use the repository
  template `framework/templates/ORDINARY_RECORD.md`, not the layered decision
  receipt.
- If yes, continue to the operating levels below. Choose only the records and
  checks justified by consequence, uncertainty, repetition, and cost.

The four-field ordinary record is terminal; it is not an ANSWER, route, stop,
learning, or influence receipt. Stage 0 grants no external-action authority;
externally consequential action remains with an explicitly authorized human.

Exact, reversible formatting that preserves every supplied item may stay
ordinary. Translation, extraction, summarization, classification, and creative
transformation can require material claim judgment or selection and
withholding even when every input was supplied; they do not qualify
automatically. This gate prevents the playbook from turning routine work into
ceremony without excusing a consequential judgment inside supplied material.

## 1. Choose the operating level

Select LIGHTWEIGHT, MODERATE, or ADVANCED using the consequence, reversibility,
evidence volume, sensitivity, reuse, and expected outcome. Record the choice.

- LIGHTWEIGHT: decision brief, evidence table, a substantive comparison and
  disconfirmation or one bounded typed reason for each inactive check, and an
  influence receipt.
- MODERATE: stable IDs, acquisition/failure receipts, typed relationships,
  packet, human disposition, outcome review.
- ADVANCED: only when consequence is high, uncertainty is high, and
  substantial capacity is separately approved; add queryable lineage, access
  and retention policy, relationship/time views, route policy, replay, and
  approved evaluation.

Record why the selected level is proportionate. Do not escalate an ordinary
task merely because more infrastructure is available. A layered task also needs
not activate all six families: record one concise reason for an inactive family
and create no placeholder artifact for it. A budget records capacity and
constraint; it cannot independently justify advanced machinery.
Advanced is justified only when consequence is high, uncertainty is high, and
substantial capacity has been separately approved; volume, reuse, or longevity
may shape capabilities inside the chosen level but do not independently select
it.

## 2. Define the real decision

Create a versioned decision brief before nontrivial acquisition.

Required fields:

- question and intended use;
- audience and consequence;
- decision owner and required reviewer;
- deadline and reversibility;
- expected sources, perspectives, fields, or periods;
- answer, abstention, hold, and escalation conditions;
- budget for time, money, tokens, compute, privacy, latency, and reviewer
  attention;
- outcome definition and measurement window if a learning loop is intended.

Do not let “find information” stand in for the decision. If the question is
underspecified, ask a clarifying question or label the interpretation
PROVISIONAL.

## 3. Separate technical access from permission

For each operation, record:

1. Can the tool technically reach the material?
2. Is the agent authorized to retrieve and inspect it for this purpose?
3. May it be transformed, retained, disclosed, or reused?
4. Does an external action require a human authority?

An accessible source may still be private, paid, sensitive, out of scope,
restricted by purpose, or forbidden to retain. If permission is UNKNOWN for a
consequential operation, route to HOLD or ESCALATE. Do not infer authorization
from credentials, a successful request, or a visible link.

Preserve the exact operation state as `AUTHORIZED`, `UNKNOWN`,
`NOT_AUTHORIZED`, or `REVOKED`. `UNKNOWN` means permission has not been
established; `NOT_AUTHORIZED` means it is absent or denied; `REVOKED` means a
previous authorization no longer applies. Each unresolved or blocked state
needs its own reason and condition for resuming. None may influence the output.

An executable permission record uses only these fields: `technical_access`,
`state`, `scope`, `reason_code`, `reason`, and `resume_condition`. Do not carry
an extra boolean such as `authorized`, `permission_granted`, or
`is_authorized` inside the permission object or at receipt top level; it can
contradict the typed state. In the current
single-global-permission receipt, `UNKNOWN`, `NOT_AUTHORIZED`, or `REVOKED`
means evidence, baseline, comparison, disconfirmation, memory, and influence
collections remain empty, and memory is `NOT_USED`. A more granular
per-operation design would need a separate, explicit contract; do not infer it
from this fixture.

## 4. Set the cost and stop envelope

Before searching, state:

- maximum elapsed time and deadline;
- paid-retrieval and spending limit;
- model-call, token, and compute limit;
- reviewer-attention limit;
- privacy, retention, and disclosure limit;
- maximum number of expansion routes or retries;
- hard stops and soft stops;
- what condition would justify one more action.

A qualitative benefit label is sufficient: HIGH, MEDIUM, LOW, or UNKNOWN.
Avoid false precision. The fact that a budget exists does not make the
remaining material sufficient.

## 5. Map the default and peripheral routes

Write the default route so a reviewer can see what would have happened without
the playbook:

- query and vocabulary;
- familiar source set;
- time window;
- ranking or product route;
- expected perspective and known blind spot.

Choose one to three bounded alternate routes. Examples include:

- a specialist or less-prominent source;
- a different vocabulary or adjacent discipline;
- a dissenting or minority interpretation;
- a peer group not represented in the default set;
- a low-prominence field or earlier time period.

For each route, state why it may change the decision and stop after the route’s
budget. Peripheral material is a candidate signal, not a truth signal.

## 6. Acquire and register every attempt

For each acquisition:

1. Write the gap or uncertainty it could reduce.
2. Record route, query, source, artifact, time, permission, and expected
   benefit.
3. Capture the result or create a failure receipt.
4. Preserve source identity, artifact identity, version or digest, event time,
   capture time, exact span, and transformation.
5. Record whether the result is usable, partial, withheld, or unresolved.
6. Update remaining budget and the next stop condition.

Capture and failure classes include NOT_FOUND, FAILED_CAPTURE, PARSER_ERROR,
UNAVAILABLE, STALE, NOT_AUTHORIZED, and OUT_OF_SCOPE. Budget or deadline
termination belongs in the separate stop-status field. A failed capture is not
evidence that the source, event, or perspective does not exist.

## 7. Weigh sources at claim level

Split the intended answer into narrow claims. For each claim and evidence item,
record:

- source role, relevant track-record evidence (or `UNKNOWN`), and claim-scoped
  authority as separate fields;
- exact support, contradiction, qualification, or insufficiency;
- relevance to this decision;
- origin, recurrence, and independence state;
- provenance and version;
- permission to use and disclose;
- uncertainty and disposition.

Never use one universal trust or relevance score. Authority for what a source
filed is not authority for why it happened. Provenance is not correctness.
Technical access is not permission.

## 8. Compare explicitly

Choose a comparison unit before interpreting a pattern:

- peer;
- period;
- attribute;
- structure;
- source role;
- origin or information pathway.

Align terms, time windows, denominators, and collection rules. Mark
INCOMPARABLE, UNKNOWN, and MISSING rather than substituting a convenient
proxy. When several reports repeat a statement, trace common origin if
possible. If origin cannot be established, preserve UNKNOWN; do not promote
the reports to independent corroboration.

## 9. Inspect motion and expected absence

For motion:

- define the measured attribute and event-time rule;
- name at least two distinct, authorized evidence IDs whose timestamps parse as
  real UTC-Z instants, include at least two distinct instants, and share one
  alignment key; never substitute a self-reported count of time points;
- state the baseline or peer comparison;
- check seasonality, denominator, collection, policy, and measurement changes;
- label the result OBSERVED_MOTION, UNCERTAIN_MOTION, or NO_SUPPORTED_MOTION.

For absence:

- state what was expected and why;
- define the observation boundary;
- distinguish not searched, failed, unavailable, unauthorized, stale, and
  superseded;
- say only “not observed within this boundary” when that is all the record
  supports.

For memory:

- retrieve by task, time, source, and permission scope;
- give each retained version a stable ID, canonical payload, and digest of the
  canonical payload bytes;
- preserve earlier observations, decisions, and corrections;
- append a corrected version with `supersedes`, `corrects`, prior-digest,
  reason, and scoped-reuse links instead of overwriting;
- bind the lineage root to a separately frozen initial anchor and reject a
  coordinated rewrite that merely recomputes the in-record links;
- keep the bounded contract linear: one successor per version and exactly one
  `CURRENT` record. A fork requires a separately represented and authorized
  branching contract; this template does not provide one;
- admit a correction into this current lineage only with an `ACCEPTED` human
  disposition; other disposition states require a separate proposal/status
  record and do not become current here;
- allow only `CURRENT`, `AUTHORIZED` memory within its recorded reuse scope to
  be used or selected for influence;
- preserve `SUPERSEDED` memory as withheld history; never select it as current
  influence;
- treat stale or unscoped memory as uncertainty.

Use repository template `framework/templates/MEMORY_RECORD.md` only when
scoped memory is material. A link proves which record was corrected; it does
not prove that the correction is true.

## 10. Disconfirm the leading interpretation

Before answering a consequential question, create a disconfirmation log:

1. State the leading interpretation.
2. State what would weaken, limit, or falsify it.
3. Search for the strongest contrary or limiting source.
4. Search for a missing expected perspective or field.
5. Check an alternative explanation, measurement change, or shared origin.
6. Record the result and remaining uncertainty.
7. Change the route or wording if the challenge matters.

“No contrary item found” is a search result, not proof of correctness.

Every `ANSWER` or `ANSWER_PROVISIONALLY` receipt records both checks. Each
check is either `PERFORMED` with linked substantive records, or explicitly
inactive: comparison uses `NOT_APPLICABLE`; disconfirmation uses `SKIPPED`.
An inactive check carries exactly one bounded task-specific reason and no
placeholder records. Non-answer routes keep the same proportional form rather
than manufacturing work.

## 11. Represent uncertainty

Use typed uncertainty:

- UNKNOWN;
- INSUFFICIENT_SUPPORT;
- CONTESTED;
- AMBIGUOUS_IDENTITY;
- UNKNOWN_ORIGIN;
- MISSING_BASELINE;
- FAILED_CAPTURE;
- NOT_AUTHORIZED;
- REVOKED;
- STALE;
- INCOMPARABLE;
- OUTCOME_MISSING.

State the source of the uncertainty and the action that could reduce it. Do
not convert an unavailable source into a negative observation or model
confidence into evidence support.

## 12. Choose the route and stop

The agent may recommend or perform only a route allowed by the brief.

Record three separate fields:

- **Route:** `ACQUIRE`, `COMPARE`, `CLARIFY`, `ANSWER`,
  `ANSWER_PROVISIONALLY`, `HOLD`, `DEFER`, `ESCALATE`, or `REFUSE`.
- **Stop status:** `CONTINUE`, `COMPLETE`, `STOPPED_BUDGET`,
  `STOPPED_DEADLINE`, or `STOPPED_OTHER`.
- **Learning status:** `LEARNING_PLANNED`, `LEARNING_PENDING_OUTCOME`,
  `LEARNING_REVIEWED`, or `LEARNING_NOT_APPLICABLE`.

Do not substitute a stop or learning status for the route. If the agent
abstains, record why as `HOLD`, `DEFER`, or `REFUSE` rather than creating an
untyped `ABSTAIN` route.

| Condition | Required route | Stop status example |
| --- | --- | --- |
| Low consequence, narrow supported claim | ANSWER | COMPLETE |
| Evidence sufficient for a bounded answer but material uncertainty remains | ANSWER_PROVISIONALLY | COMPLETE or a named stop state |
| One low-cost authorized action may reduce a named gap | ACQUIRE or COMPARE | CONTINUE |
| Question or authority is unclear | CLARIFY | CONTINUE or STOPPED_OTHER |
| Critical gap, conflict, or permission issue blocks influence | HOLD | STOPPED_OTHER |
| A later time or missing input is required | DEFER | STOPPED_DEADLINE or STOPPED_OTHER |
| Human or domain authority must decide | ESCALATE | STOPPED_OTHER |
| Requested action is prohibited | REFUSE | COMPLETE or STOPPED_OTHER |
| More work is not worth the remaining budget | ANSWER_PROVISIONALLY, HOLD, or DEFER | STOPPED_BUDGET |

Every route receipt includes route, stop status, reason, expected benefit,
cost, permission, uncertainty, and stop or resume condition. Budget exhaustion
is not evidence sufficiency.

A planning surface may recommend a route, gate, or stopping condition before a
run. That recommendation is not an observed route receipt. Record `COMPLETE`, a
`STOPPED_*` status, a human disposition, or an outcome-learning state only
after the corresponding event has actually occurred.

## 13. Build the context and influence receipt

The packet contains only material permitted for this bounded output. For each
selected item, state:

- item and claim ID;
- exact span or pointer;
- source role and relationship;
- influence role: supports, qualifies, contradicts, frames, or routes;
- why admitted;
- what it cannot establish;
- disclosure permission and reviewer disposition.

List withheld material and its reason: duplicate, insufficient, not authorized,
sensitive, stale, out of scope, or unknown. Withholding is not deletion.
Every selected ID must resolve to a preserved evidence or memory record, and
that record must be `AUTHORIZED` for the named use. A plausible but dangling
ID is not an influence receipt. If the selected item is memory, it must also
be `CURRENT`; a `SUPERSEDED` version remains inspectable only as withheld
history.

The generated answer must separate:

- observations;
- interpretations;
- recommendations;
- unknowns;
- human decision or action requiring authority.

## 14. Escalate without pretending the human has answered

Escalation is a record, not a rhetorical handoff. Include:

- the question for the human or domain reviewer;
- the exact evidence and uncertainty;
- what the agent has and has not done;
- the cost already spent and remaining;
- the no-action boundary;
- the decision needed to resume.

Do not use a human disposition as evidence of truth. A reviewer can accept a
route, reject an item, defer, override, correct a relation, request enrichment,
or revoke permission.

## 15. Record outcome learning

Before the outcome window closes, save:

- expectation and success or abstention condition;
- outcome definition, timing, and attribution boundary;
- expected cost and route;
- what would count as missing outcome.

After the window:

- record observed outcome, actual cost, corrections, context changes, and
  confounders;
- compare expectation with observation;
- state what the outcome cannot establish;
- propose one bounded update;
- request authorized disposition;
- preserve the original brief, packet, and receipt unchanged.

Learning proposes a bounded update. It does not silently change a policy,
rewrite a fact, or turn correlation into causation.

Record `LEARNING_NOT_APPLICABLE` when no defined later outcome exists. Use
`LEARNING_PLANNED` while a future outcome route is proposed but its expectation
and window are not yet locked. Once those pre-outcome fields are recorded, use
`LEARNING_PENDING_OUTCOME`. Use `LEARNING_REVIEWED` only after the outcome
review and human disposition are recorded.

## 16. Completion checklist

The agent may call the work complete only when:

- the decision and authority are explicit;
- the route stayed within permission and budget;
- source, artifact, and claim distinctions are recorded where needed;
- peripheral candidates were not promoted by status;
- recurrence and origin were not conflated;
- any motion claim resolves to at least two authorized, time-bearing records
  sharing one alignment key, and any absence claim has its required baseline;
- any memory influence resolves to a `CURRENT`, authorized, scoped, versioned
  record whose payload digest and frozen lineage anchor validate;
- comparison and disconfirmation are substantive or carry their typed bounded
  inactive reason, and uncertainty is visible;
- stop or escalation is reasoned;
- influence and withholding are recorded;
- external action remains with the authorized human;
- a later outcome plan exists or is marked NOT_APPLICABLE.

If any required item is missing, stop with the missing field named.

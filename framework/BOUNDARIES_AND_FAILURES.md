# Boundaries, failure modes, stopping rules, and cost

The framework is a set of inspectable practices, not a guarantee of correct
answers. These controls make errors easier to see and correct; they do not
remove domain judgment, privacy obligations, or human accountability.

## Common failure modes

| Failure | Observable symptom | Recovery |
| --- | --- | --- |
| Default-path tunnel | Only familiar sources or vocabulary appear | Record the default path and add one bounded alternate route |
| Peripheral romanticism | An obscure item is admitted because it is obscure | Re-label it CANDIDATE and apply source weighing and comparison |
| Recurrence inflation | Copies or citations are counted as independent support | Trace common origin; keep relation UNKNOWN when unresolved |
| Authority leakage | A source’s standing for one claim is used for a different claim | Split the claim and record claim-scoped authority |
| Provenance laundering | A clean citation or summary is treated as proof | Inspect exact span, transformation, and support state |
| Access/permission collapse | A reachable private, paid, or sensitive source is acquired | Stop, record NOT_AUTHORIZED, and escalate |
| Motion from one point | One timestamp is called a trend or velocity | Require repeated observations and a baseline |
| Manufactured absence | A missing field is treated as nonexistence | Write the expected baseline and classify the gap |
| Memory overwrite | A correction replaces the original record | Append a correction and link supersession |
| Comparison by appearance | Unlike items are compared because they look similar | Declare comparison unit and mark incomparable fields |
| Confidence collapse | Model confidence becomes the evidence assessment | Use typed uncertainty and exact support links |
| Search without a stop | More acquisition continues without a decision rule | Compare expected benefit with cost and stop or escalate |
| Budget-as-sufficiency | A time or token limit is described as proof | Record stop status STOPPED_BUDGET and the remaining uncertainty separately from the route |
| Influence opacity | The answer cites sources but not what shaped which claim | Create a claim-level influence receipt |
| Rubber-stamp review | Human approval has no role, reason, or scope | Record disposition, authority, reason, and any override |
| Hindsight learning | The later outcome rewrites the earlier story | Freeze the original receipt and write an outcome review |
| Over-discrimination | The workflow refuses or delays easy, reversible tasks | Use the lightweight or ordinary path and measure reviewer cost |
| Under-discrimination | Fluent answer proceeds despite a critical gap or permission issue | Use HOLD, DEFER, ESCALATE, or REFUSE with the missing condition visible |

## Stop rules

### Hard stops

Stop the current route and do not allow the blocked material to influence
generation when:

1. permission is absent, revoked, or materially ambiguous;
2. the action would disclose, publish, spend, or affect an external system or
   person beyond the operator’s authority;
3. a critical source, artifact, identity, or provenance check fails;
4. a high-consequence claim has no support and no approved provisional wording;
5. the observed boundary cannot distinguish failed capture from absence;
6. retention, privacy, security, or safety constraints are violated;
7. the decision owner or required domain reviewer is unavailable for an action
   that cannot be reversed safely.

Record the route as `ESCALATE` where required and use a canonical
`STOPPED_*` status such as `STOPPED_OTHER`, together with the no-action
boundary and the condition needed to resume. Do not hide a hard stop behind a
polished answer.

### Soft stops

Stop acquisition and answer provisionally, hold, or defer when:

- the next action is expected to add mostly duplicates;
- the remaining budget cannot buy enough information to change the route;
- the answer is supported for a narrow claim but broader interpretation remains
  unresolved;
- comparison coverage is sufficient for the stated decision;
- the deadline makes additional work less valuable than an explicit caveat;
- the task is low consequence and a full record would cost more than a
  correction.

Soft stopping preserves uncertainty. It does not announce certainty.

### Resume conditions

Every hold or defer record should name one resume condition, such as a
clarified question, authorized source, new time point, corrected identity,
domain review, or defined outcome. Without a resume condition, the record is
closed with `STOPPED_OTHER` rather than left in an invisible queue.

## Cost boundary

Before the first nontrivial acquisition or enrichment, record:

| Dimension | Example boundary |
| --- | --- |
| Time | 20 minutes or one research pass |
| Money | No paid source; or a named authorized amount |
| Tokens/compute | One model call, fixed context size, or local processing only |
| Human attention | One reviewer pass and one correction request |
| Privacy | No new sensitive content; pointers instead of copied material |
| Disclosure | Internal use only; no external sharing |
| Latency | Answer by a stated deadline |
| Consequence | No automatic external action; human decision required |

The operator may use qualitative benefit bands such as HIGH, MEDIUM, LOW, or
UNKNOWN. Do not invent precise value-of-information numbers unless the task
has a defensible measurement model. A plausible cost/benefit story is not an
empirical result.

## Permission boundary

| Capability | Technical ability | Permission question |
| --- | --- | --- |
| Read | Can a tool reach it? | Is this operator allowed to retrieve and inspect it for this purpose? |
| Transform | Can it be parsed, summarized, or embedded? | Is transformation allowed, and may the result retain sensitive content? |
| Retain | Can it be stored or remembered? | What retention, deletion, legal, or minimization rule applies? |
| Disclose | Can it be placed in a packet or answer? | Who may receive it, in what form, and for what purpose? |
| Act | Can a tool execute the action? | Who authorizes it, and what human gate or rollback exists? |

Any unknown permission field routes to HOLD or ESCALATE for consequential work.

## When not to use the full framework

Do not add the complete framework when:

- the task only rewrites, translates, formats, or brainstorms from supplied
  content and adds no factual claim;
- the work is ephemeral, reversible, low consequence, and a person will inspect
  it immediately;
- the user explicitly wants a creative variation rather than a factual answer;
- there is no acquisition, comparison, memory reuse, or influence choice to
  govern;
- recording a full packet would expose more sensitive material than the task
  requires;
- the answer must be produced inside a trivial latency budget and the safe
  response is an explicit limitation.

Use a one-paragraph ordinary answer with assumptions, or the lightweight route,
instead. The framework should improve proportion, not become mandatory
bureaucracy.

## Non-negotiable language

Every implementation, case, and receipt should preserve these boundaries:

- peripheral is a candidate, not truth;
- recurrence is not independent corroboration;
- provenance is not correctness;
- technical access is not permission;
- a disposition is not a fact;
- an outcome proposes a bounded update and preserves history;
- a protocol, case, fixture, or planning simulation is not a result;
- Signal Foundry is a bounded illustration, not validation;
- no artifact grants authority to deploy, publish, spend, contact, or act.

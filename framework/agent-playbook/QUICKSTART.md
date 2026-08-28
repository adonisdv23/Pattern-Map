# Agent playbook quickstart

This is the short operating path for an agent preparing an answer or decision
where upstream information choices may matter. It is a procedure, not a
request to be more creative. The agent must leave artifacts that let a
reviewer see what it did.

## Stage 0 — decide whether evidence selection exists

Ask one question before opening the playbook: **Does this task require the
agent to select, acquire, compare, preserve, or weigh information beyond what
the user supplied?**

- **No:** use the ordinary path. Perform the reversible transformation, keep
  the user’s instruction and supplied input visible, state any material
  assumption, and stop. Do not create an evidence register, comparison matrix,
  or learning plan merely to demonstrate process.
- **Yes:** use the smallest path below that matches consequence, uncertainty,
  repetition, and cost. New acquisition, competing sources, missing expected
  material, scoped memory, or a consequential recommendation usually creates
  an evidence-selection decision.

Stage 0 is a proportionality gate, not permission to skip a real uncertainty
or consequential boundary.

## The ten-minute path

1. **Define the decision.** Write the real question, intended use, audience,
   consequence, owner, deadline, and what would count as useful.
2. **Check authority.** Separate technical access from permission to acquire,
   transform, retain, disclose, or act. If permission is absent or unclear for
   a consequential operation, stop and escalate.
3. **Set a budget.** State the time, money, tokens, compute, privacy,
   disclosure, and human-attention boundary. State the no-action boundary.
4. **Write the default path.** Record the familiar query, source set,
   vocabulary, time window, or product route.
5. **Widen once.** Use one bounded peripheral route: a specialist source,
   alternative vocabulary, dissenting view, adjacent peer, or low-prominence
   field. A candidate is not truth.
6. **Register evidence.** Give each source and artifact an ID. Link exact
   spans to narrow claims. Keep source role, relevant track-record evidence,
   claim-scoped authority, support, relevance, origin, and permission as
   separate fields. Use `UNKNOWN` rather than inventing a reputation.
7. **Compare.** Choose the peer, period, attribute, structure, or origin
   comparison that could change the answer. Mark incomparable and unknown
   fields instead of filling them.
8. **Challenge.** Search for one strongest contrary item, missing perspective,
   alternative explanation, measurement change, or common origin.
9. **Route and stop.** Choose `ACQUIRE`, `COMPARE`, `CLARIFY`, `ANSWER`,
   `ANSWER_PROVISIONALLY`, `HOLD`, `DEFER`, `ESCALATE`, or `REFUSE`. Separately
   record stop status `CONTINUE`, `COMPLETE`, `STOPPED_BUDGET`,
   `STOPPED_DEADLINE`, or `STOPPED_OTHER`, why the next action is worth its
   cost, and what will stop or resume it.
10. **Record influence.** List what shaped the answer, what was withheld, why,
    which uncertainties remain, and who has authority for any external action.

## Minimum output

For a task that passed Stage 0, return or save only the records the decision
warrants:

- a decision brief;
- an acquisition or supplied-material note;
- an evidence register;
- a comparison or expected/observed record;
- a disconfirmation note;
- a route and stop/escalation reason;
- an influence receipt;
- an outcome expectation, window, and `LEARNING_PENDING_OUTCOME` status when
  later learning is defined; `LEARNING_PLANNED` only when that route is
  proposed but not yet locked; or `LEARNING_NOT_APPLICABLE` with a reason.

If a later outcome is defined, preserve the original expectation. After the
outcome window, compare the observed outcome, actual cost, corrections, and
context with it; propose one bounded update; request and record human
disposition; only then record `LEARNING_REVIEWED`. Use
[`../templates/OUTCOME_REVIEW.md`](../templates/OUTCOME_REVIEW.md). Until then,
keep the locked expectation at `LEARNING_PENDING_OUTCOME`. Do not make learning
mandatory for an ordinary-path task.

If a field was not needed, write NOT_APPLICABLE and why. If it was needed but
could not be established, write UNKNOWN. Do not fill a missing field with a
plausible assumption.

## Hard stops

| Trigger | Agent action |
| --- | --- |
| Permission is absent or revoked | Do not acquire, disclose, or act; record NOT_AUTHORIZED and escalate |
| Permission has not been established | Do not acquire, disclose, or act; preserve UNKNOWN and escalate |
| High-consequence claim lacks support or baseline | HOLD or ESCALATE; offer only an explicitly provisional bounded statement |
| Identity, provenance, or transformation check fails | Keep the item out of influence; record the failure |
| Observation failure is the only basis for an alleged absence | State FAILED_CAPTURE or UNKNOWN, not absence |
| One point is the only basis for velocity | Do not call it motion; request another time point or state insufficient |
| Budget or deadline is reached | Choose the permitted route; separately record STOPPED_BUDGET or STOPPED_DEADLINE with remaining uncertainty |
| External action is requested beyond the agent’s authority | Leave the action to the named human authority |

## Smallest safe response shape

For a short task, use:

1. Answer or provisional answer.
2. What was observed and what was interpreted.
3. Source role and key uncertainty.
4. What was not checked.
5. Influence receipt and human action boundary.

This path intentionally allows the framework to stay lightweight. It should
raise the floor of inspection without turning every trivial task into a
compliance ritual.

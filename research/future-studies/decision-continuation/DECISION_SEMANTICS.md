# What a changed reason can change

Status: **AUTHORED DEVELOPMENT / NO STUDY RUN / NO RESULTS / NO NOVELTY CLAIM**.
Prepared 2026-09-07 from `61f530c39aa30be67c310116c460b8adabdc79e8`.
Governing requirements: [owner intent](../../../docs/OWNER_INTENT_V16.md),
A07–A08/A11/A15–A17, proportionality, and the
[public continuation scope](../../../docs/PUBLIC_CONTINUATION_SCOPE_2026-09-07.md). This optional research note does not change a runtime or frozen pilot.

**Reconsider the part of a decision whose justification has changed.** A newer
source, a failed check, or an uncertain historical link is not a reason to
discard everything already supported. Equally, an intact historical record does
not make its recommendation applicable now. The useful question is whether a
short procedure helps people make those distinctions at acceptable total cost
compared with careful ordinary reasoning.

## Keep the objects distinct

| Object | What it establishes, if adequately supported | What it does not establish |
| --- | --- | --- |
| Source identity and integrity | These are the identified version's bytes; a pointer or digest matches its stated reference | Truth, completeness, applicability, independent origin, or current action authority |
| Applicability | The material addresses this subject, operation, time, conditions and intended use | That its claim is true or its recommended action authorized |
| Observation | A stated event or capture result within a described observation boundary | An explanation, an unobserved event, or completeness outside that boundary |
| Reason | An explicit consideration supporting, qualifying or defeating a particular conclusion under stated conditions | A universally necessary condition or sufficient argument merely because the author called it important |
| Conclusion | A bounded factual assertion or recommendation warranted by the available evidence and governing decision criteria | Permission to perform an external action |
| Decision/action authority | The named authority permits or directs the exact operation within scope | World truth, retrospective correctness, or permission for adjacent operations |

Time has several roles. A record can be current as a file and concern a past
event; an old immutable record can be good evidence of that event. A later
capture time does not move the event forward in time. A current policy can
settle today's permitted scope while saying nothing about why last month's
policy changed. Keep those claims separate rather than treating `CURRENT` as a
universal truth label.

## Necessary, sufficient, and merely contributing reasons

These are elementary reasoning distinctions, not a proposed decision calculus.
Fix the subject, goal, evidence cutoff and decision rule before using them.
A condition is **necessary** for a specified route when that route cannot meet
the rule without it. A set of reasons is **sufficient** when, together with the
explicit background conditions, it meets that rule. A contributing reason can
change the balance without being either necessary or sufficient. If the source
does not establish which role a reason plays, preserve that uncertainty.

For an authored local example, an owner permits a repair only when it is
reversible **and** the exact file is in scope. Finding reversibility alone
cannot justify the repair. A different owner rule says to keep an optional
integration parked while either its required license is unavailable **or** no
maintenance owner is assigned. Either obstacle is sufficient to keep it parked.
Resolving the license warrants revising that reason; the unassigned maintenance
role still supports the same decision. Neither resolving one obstacle nor
resolving both is proof that the integration is beneficial.

In compact notation, `(R1 OR R2) => keep parked` does not license
`NOT R1 => reopen`. Even `NOT R1 AND NOT R2` removes only these sufficient
reasons; unless the governing rule is an explicit equivalence, it does not
establish the opposite decision. A direct prohibition can independently prevent
action after every technical objection disappears. Conversely, discovering
that one cited reason was mistaken need not defeat a conclusion independently
supported by another sufficient argument. Preserve the error and the surviving
argument instead of silently substituting a better history.

A claim can lose support without becoming false. Suppose an inventory with
no matching row was used to conclude that the collection contains no X.
Learning that the inventory covered only part of the collection removes the
basis for that collection-wide absence claim. The captured portion still
contains no matching row; X elsewhere remains unknown. Conversely, a captured
matching X remains positive evidence for its stated subject and observation
boundary even when the inventory is partial. Correct the affected coverage
claim without erasing what was actually observed.

## One proportionate continuation procedure

Use the existing decision brief and receipt, in prose where sufficient:

1. Resolve the current question, subject and applicable authority. Recover the
   earlier decision and reasons only to the extent needed for this question.
2. State the new observation separately from its interpretation. Identify its
   source/version, event and observation times, and coverage where material.
3. Identify the particular reason, condition or support relation affected.
   Ask whether an independently sufficient reason survives; do not infer one
   from a missing record.
4. Preserve supported conclusions. For each unresolved part, name an available
   check whose possible answers could alter the recommendation, its scope or a
   required permission decision. Compare its cost with using the current answer
   or stopping. A small sequence may be worthwhile even when one check alone
   cannot settle the matter.
5. Recommend continuing, inspecting, proposing a scoped reconsideration, or
   stopping. These are ordinary descriptions mapped to existing route/stop
   fields, not new enum values. Preserve the earlier record and cite the new
   basis. A recommendation to reconsider does not perform the action.

Do not demand formal Boolean expressions, probabilities, all six family
records, or an exhaustive dependency graph. An honest sentence can suffice:
“The new export changes identifier reuse, so recheck the pointer binding;
the ban on a second writable authority still applies.” The family questions
remain available according to decision value, not as six compulsory checks.

## Counterexamples the procedure must survive

The cases below are authored reasoning examples. They reuse distinctions in
the [earlier discovery cases](../development/DISCOVERY_CASES.json) and
[eight development families](../ultra/development/README.md), especially F4–F7;
they are not additional pilot tasks or observed outcomes.

| Available history | Justified consequence and error to avoid |
| --- | --- |
| Relevant facts, goal and authority are unchanged | Continue the supported decision or stop reviewing. A new timestamp alone earns no retrieval. |
| A newer source changes a different product's identifier behavior | Record irrelevance if necessary. Matching vocabulary cannot establish subject identity or changed applicability. |
| A target operation now duplicates side effects on retry | Recheck the retry transfer, preserving the historical evidence that applied to the earlier operation. A good source analogy cannot repair a defeated target condition. |
| One of two independently sufficient reasons for parking is defeated | Correct that reason; keep parked if the second still applies. Do not count two reasons as independent evidence merely because they are written twice. |
| The original rationale is missing | Do not claim the old decision was irrational, or that its exact failure has been resolved. Retrieve the rationale if that historical claim or governing reopening rule requires it. An independently supported new assessment is possible under current scope. |
| Current authority explicitly parks the named project; an old supersession link is unavailable | Answer that the inspected current authority parks it. Leave the historical transition unresolved. This cannot support a detailed history or waive a gate that actually requires that history. |
| A capture returns an empty payload and reports failure | Event presence is unknown from this attempt. Inspect coverage if worthwhile; do not call failure a complete negative observation. |
| A complete journal for a defined sequence/window contains no matching event, and its coverage/matching rule is established | The scoped absence is supported. Extend it to world absence only if the event would necessarily have appeared there. Observation reliability remains a premise. |
| A matching event was previously captured; a later attempt fails | Preserve the positive observation for its original subject/window. Later failure does not erase it or prove continuing presence now. |
| An explicit later owner instruction changes the goal or permits a named exception | Reassess the named scope under the new instruction. Changed preference is a new decision criterion, not new evidence of demand, feasibility or prior error. |
| Two different worlds yield exactly the same available source and capture history | Permit the same epistemically justified answers and next-action policies. Hidden event truth cannot make one identical answer justified and the other unjustified. |

The final row assumes the same goals, costs, available checks and permissions.
Changing any of these changes the decision problem even if event observations
match. If the values needed to rank actions are unstated, there may be several
defensible choices; do not invent a unique optimum.

## Partial answers and mandatory gates

Localize uncertainty **within** the applicable contract. The current
[memory template](../../../framework/templates/MEMORY_RECORD.md) admits only a
`CURRENT`, `AUTHORIZED`, in-scope record in its verified linear lineage.
A missing required target or integrity failure blocks that memory's influence.
Do not relabel the same blocked memory as “direct evidence” to evade the rule.
Separately obtained authorized current-source evidence can support an independent
claim through its own valid route. Superseded memory remains preserved and
withheld; preservation alone supplies no current influence.

Likewise, the current single-global-permission receipt requires empty downstream
collections when global permission is blocked. Claim-level uncertainty is no
exception to that rule, and unknown consequence still prevents an answer route.
Where the overall operation is permitted and consequence known, an unknown
historical relation need not contaminate a separately supported present-state
claim. The ordinary research comparator can make that judgment; it is not
canonical Stage 0 `ORDINARY`, which excludes material judgment and memory reuse.

More information can be useless for this decision without being worthless in
general. If every affordable observation leaves the same permitted action and
acceptable answer scope, and no separate authorized information objective is
served, stop. If a check could justify a better bounded recommendation even
though execution remains prohibited, it may still have value. Do not equate
“cannot act today” with “cannot usefully know anything.”

## Existing representations before new fields

| Existing artifact | Representation already available |
| --- | --- |
| [Decision brief](../../../framework/templates/DECISION_BRIEF.md) | Real question, intended use, owner, permission envelope, expected coverage, useful answer, cost and resume condition; change log for changed goal |
| [Influence receipt](../../../framework/templates/INFLUENCE_RECEIPT.md) | Exact pointer, decision role, support and limits, withheld material, re-entry condition; observations separate from interpretations and recommendations |
| [Scoped memory](../../../framework/templates/MEMORY_RECORD.md) | Preserved statement/scope, source/time/reuse scope, current/superseded relationship and correction reason |
| [Outcome review](../../../framework/templates/OUTCOME_REVIEW.md) | Preserved expectation/window, observed or missing outcome, context changes, attribution limits and bounded update proposal |

The minimal candidate refinement is explanatory guidance within those existing
reason/scope fields: which condition matters and what a change could affect.
No new record stack, mandatory reason schema, universal gate or trust score is
justified here. An authored continuation is not `LEARNING_REVIEWED`; the actual
linked review and accountable disposition requirements remain unchanged.

## Primary methods and the remaining question

Inspected 2026-09-07; targeted, not exhaustive. These comparisons constrain the
contribution, not establish Pattern Map effectiveness.

**Competing hypotheses.** Heuer's Chapter 8 asks for alternatives, expected
evidence and explanations of missing evidence, diagnostic comparison,
sensitivity to critical assumptions, and future milestones. It also distinguishes
unproven from disproved hypotheses. A compact adaptation is a serious comparator:
state plausible explanations, identify discriminating observations, and revise
the conclusion only as far as evidence warrants. Its matrix remains an aid to
judgment. Our inference is that scoped continuation organizes these familiar
operations around an existing decision, not that it invents them. Inspected
steps 1–8, printed pp. 95–107; the book's effectiveness assertions are not adopted
as evidence here. [Heuer, 1999](https://www.cia.gov/resources/csi/static/9a5f1162fd0932c29bfed1c030edf4ae/Pyschology-of-Intelligence-Analysis.pdf).

**Assumption-based planning.** An accessible official primary application
identifies assumptions in planning documents, connects them to planned actions,
develops signs of vulnerability, and distinguishes actions that protect an
assumption from those preparing for its failure. It is directly relevant to
recording why a plan remains appropriate. Inspected methods pp. 16–19 and
Appendix A pp. 59–63. This supports the comparison, not transfer of military
investment judgments or utility machinery. This comparison is limited to
MG532; it does not claim inspection of RAND R-4216 or Dewar's complete book.
[Peters et al., 2007, RAND MG532](https://www.rand.org/content/dam/rand/pubs/monographs/2007/RAND_MG532.pdf).

**Cost-sensitive metareasoning.** Hay and colleagues formulate selecting
computations as a decision problem with computation cost and a terminal choice.
Their myopic policy can stop before a useful sequence of computations. Inspected
§2, Definitions 1–6 and the stopping discussion. The practical inference is to
allow a justified affordable check sequence rather than requiring each check
to settle the decision alone. Their probabilities, utilities and observation
model cannot be assumed for heterogeneous project records; no optimal-policy
claim follows. [Hay et al., 2012](https://arxiv.org/html/1207.5879).

The [existing transfer/check proposal](../ultra/MECHANISM_AND_COMPARATORS.md)
already grants strong ordinary practice normal search, comparison, notes,
reconsideration and stopping. Preserve those rights here. Selection, mandatory
reads, instructions, retrieval, review, correction and maintenance all count.
The proposed increment can lose: keep ordinary prose if it produces equally
supported decisions with less work, or if apparent gains require author-selected
answer cues. The question is practical incremental usefulness, not terminology,
adherence or another completed form.

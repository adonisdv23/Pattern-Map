# Advisory review — grounded discovery pilot

Reviewed commit: **`d02f58ac81fcacee77e0c128ad16cd92b454b1cf`**, branch
`codex/pattern-map-ultra-mechanism-2026-09-07`, on 2026-09-07. Scope:
`research/future-studies/ultra/MECHANISM_AND_COMPARATORS.md` and
`research/future-studies/ultra/PILOT_DECISION_SPEC.md` only. Repository source and
Council were not changed. This is same-model adversarial design review, not
empirical validation, an independent scientific source, or a formal Council
Auditor verdict. Referenced literature was not independently re-audited here.

**Recommendation: Accepted with revision.** The primary R-versus-O/M contrast is
coherent as a bounded instruction-policy package comparison. Resolve the budget
scoring ambiguity below before freezing the adapter and rubric together. The
other findings require small specification edits, not another research platform.
Fresh task packets, private world keys and strict offline adapter are being
authored elsewhere; their previously declared absence is not a new finding.

## P2 — Over-budget intermediate attempts have ambiguous acceptance consequences

**Evidence:** Pilot decision specification lines 104–115 and 173–194. An
unaffordable paid action releases nothing and “records effort failure.” The
analysis later says benign rejected intermediate attempts remain charged
diagnostics; terminal/ceiling failures score zero, and a hard-constraint violation
fails acceptance. It does not classify an unaffordable intermediate request among
those alternatives.

**Concrete argument:** Set B=1 and K=3, with all actions within their step
deadlines. Attempt 1 inspects one item successfully and consumes B. Attempt 2
requests another listed inspection, releases nothing and charges zero remaining
units. Attempt 3 returns a justified STOP. This terminates within K and never
spends more than B. One implementation can accept the decision with a diagnostic;
another can assign zero because the request is an effort failure or hard-budget
violation. The same ambiguity affects the harmful-error counts used for
advancement even if both implementations accept the terminal decision. This is
a specification counterexample, not an executed model episode.

**Disposition recommendation: Accepted with revision.** Define an explicit
attempt-level/episode-level table for unaffordable requests, unavailable actions,
deadline rejection and terminal exhaustion. State Y and advancement-error coding
for the three-step trace. Add this exact trace to deterministic adapter/rubric
cross-checks. Do not change K or grant extra terminal capacity to repair it.
Governing requirement: fixed cost/stopping rules, comparable denominators and
honest unfavorable-result classes.

**Suggested replacement wording, consistent with the root's stated intended
adapter policy:**

> Intermediate rejected requests (including malformed, unavailable and
> unaffordable requests) and permitted duplicate inspections retain their
> attempt-level diagnostic class and prescribed cost. They do not, by themselves,
> produce terminal EFFORT_FAILURE or automatic episode-zero. An unaffordable
> inspection records REJECTED_BUDGET, releases no evidence, and charges at most
> remaining B. A valid terminal decision within K and the token/time ceilings is
> graded semantically. Any action meeting the frozen task's definition of a
> scope/permission violation independently fails acceptance; needless acquisition
> is classified separately under the frozen rubric. Invalid terminal output,
> token/time exhaustion, or reaching K without a valid terminal decision scores
> zero. Attempt-level budget rejection is not an episode-level effort failure.

For the B=1/K=3 trace, the justified STOP can therefore receive Y=1, with a
REJECTED_BUDGET diagnostic and its charged cost retained. Any needless-acquisition
classification comes from the frozen rubric. Clarify whether each task's scope
rule prohibits requesting an action or performing its effect; parser denial
alone must not choose that semantic rule. This is proposed precedence for the
source amendment, not a claim that the current adapter was verified here.

## P2 — The interval's inferential target and construction are unspecified

**Evidence:** Pilot lines 143–159 and 189–199 prescribe twelve authored tasks in a
3-domain by 4-regime grid, four episodes per task/arm, equally weighted task
contrasts and “exploratory task-cluster intervals.” Randomization concerns run
order; it does not randomly sample tasks from a declared task population.

The point estimate is clear for this fixed instrument. The proposed interval
could instead describe repeat-episode randomness, variation under hypothetical
task replacement, or uncertainty over a larger task population. Those are
different targets. Calling an interval exploratory does not choose among them.
In particular, an ordinary task bootstrap would not preserve the authored
domain/regime grid and should not imply coverage for an unspecified population.

**Disposition recommendation: Accepted with revision.** Either omit intervals
for this diagnostic pilot and report all twelve paired task differences, or
state the exact estimand, resampling scheme and interpretation before calls.
If resampling tasks is retained, label it sensitivity to this instrument's task
composition unless a sampling model is explicitly justified. Do not count forms,
counterfactual worlds or repeated outputs as independent tasks. No larger sample
or new study is required to resolve this specification issue.

## P3 — Clarify unlisted implementations within the finite catalogue

**Evidence:** Pilot lines 13–18, 95–106, 122–126 and 166–170. SELECT is bound to
allowed candidate IDs, while feasible alternatives absent from the author's
list can receive credit. “Author's list” could mean the frozen rubric's named
implementations or the public candidate catalogue.

**Disposition recommendation: Accepted with revision.** Say explicitly whether
an unlisted implementation must instantiate/combine listed candidates. That fits
the stated finite-catalogue estimand and avoids a new action type. If entirely
new candidates are intended, their representation and admissibility would need
an explicit contract before any episode; do not let graders improvise this after
seeing outputs. The present text does not establish a demonstrated leakage bug.

## P3 — One controlled disposition reverses its apparent decision

**Evidence:** Mechanism document line 111 labels “Stop a mechanism claim when it
reduces to existing operations” as Rejected, although its explanation rejects
novelty by renaming familiar operations.

**Disposition recommendation: Accepted with revision.** Either mark the stopping
decision Accepted, or rename the row “Claim a new mechanism by renaming existing
operations” and retain Rejected. The surrounding novelty ceiling is otherwise
appropriately explicit.

## Boundaries that survived this review

O and M are substantial comparators and remain free to use R-like reasoning.
R receives no extra facts or capacity; acquired evidence can differ as a policy
outcome. The docs explicitly avoid isolating a timing or formatting mechanism.
Hidden-world grading, case-family/preferred-route labels, task dependence,
assigned failures and unfavorable outcomes have appropriate stated boundaries.
The conservative advancement rules earn only a larger design review, require
both baselines, retain harm/cost limits, and forbid post-output relaxation.

These strengths are specification observations, not proof that forthcoming
packets or the adapter satisfy them. Before execution review, inspect their exact
public projections and release traces against these documents, and resolve the
four findings through the existing controlled disposition process. No new
execution authority follows from this report.

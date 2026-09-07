# Advisory review — offline pilot adapter

Reviewed baseline: **`af6d6018575096fdcca818908e6b11f48b3e2dfa`** in
`/Users/gpt/Documents/Codex/worktrees/pattern-map-ultra-integration-2026-09-07`,
2026-09-07. Scope: the amended mechanism/pilot documents,
`research/future-studies/ultra/pilot/adapter.py`, and `test_adapter.py`.
No source edits were made by this reviewer. The worktree already contained
integrator-owned generated-site changes, which were left untouched.

This is same-model advisory implementation review, not empirical validation,
production-security certification, or a formal Council Auditor verdict. All
executed examples were synthetic in-memory contract checks with no network,
model or provider operation.

**Recommendation: Accepted with revision.** Two initial reproducible adapter
defects remain at the reviewed baseline. A completeness finding and a candidate
binding loophole were raised by the integrator and are assessed separately below.
The previously
reported four pilot-document issues are resolved in this baseline: explicit
intermediate budget-rejection precedence, leave-one-task-out composition
sensitivity instead of population intervals, supported instantiations/combinations
for unlisted implementations, and corrected novelty-disposition wording.

## P2 — Unchecked action descriptions admit nested records into the public view

**Evidence:** `adapter.py:113–128` checks action keys, kind, costs, deadlines and
identity, but does not require `description` to be a string. `view()` at lines
170–175 copies the action record directly into the model-facing projection.

**Executed reproduction:** Starting from `test_adapter.specimen()`, replace the
first action's description with
`{"text": "Compare", "private_answer": "SYNTHETIC_UNOPENED_KEY_CANARY"}`.
`Episode(task, releases)` succeeds and the canary appears in
`json.dumps(episode.view())`. This is a misplaced synthetic-key leak through an
unchecked field, not evidence that a real key was exposed.

**Disposition recommendation: Accepted.** Require every action description to be
nonempty text before copying it. Add a negative test for an object/list nested in
this field, alongside existing candidate/constraint/priority private-field tests.
Use schema validation rather than a blacklist of secret-looking words: approved
public text still requires semantic source review. Governing requirement: exact
public projection, nested-record closure and no unopened key exposure.

## P2 — Public availability contradicts irreversible rejection

**Evidence:** `view()` at lines 172–174 derives availability only from terminal
state, deadline and remaining acquisition units. `_request_error()` at lines
228–229 separately rejects every REOPEN when `reversible` is false.

**Executed reproduction:** Set the specimen's rejection policy to irreversible;
submit REJECT with C1. The next public view marks REOPEN `available: true`.
Submitting REOPEN with C1 then returns `REJECTED_IRREVERSIBLE` and charges one
unit. A model following the displayed availability can therefore lose scarce
budget on an action that the same frozen contract already forbids.

**Disposition recommendation: Accepted.** Make public REOPEN availability false
under the irreversible policy. Add a test covering the displayed availability,
rejected direct attempt, retained evidence/history and charged attempted request.
Do not relax the existing rejection rule or grant a free retry. Governing
requirement: truthful public action availability and matched action costs.

## P2 — Missing public request/terminal contract: accepted integrator finding

The integrator reported that the Shared instruction refers to a supplied action
contract, but baseline `view()` contains action descriptions without the exact
request/terminal schema and typing rules. Source inspection confirms no public
`contract` field at this baseline. The new parser rejects unknown fields, imposes
candidate-count and citation rules, and applies length limits that a prospective
model needs to see identically in every arm.

**Disposition recommendation: Accepted.** The integrator is adding one shared
public contract covering exact fields/types, candidate and unlisted-implementation
rules, charging, attempts/deadlines, termination and raw-record limits, plus a
test. This report records the accepted correction plan; it does not certify a
successor commit that has not yet been reviewed. O/M/R variable wording should
remain unchanged.

## P2 — Empty SELECT bindings bypass syntactic irreversible rejection

**Evidence and executed reproduction:** The baseline permits SELECT with empty
candidate IDs for an unlisted implementation (`adapter.py:217–219` and its
unforeseen-implementation test). Using the exact baseline adapter loaded from
Git, set irreversible rejection, REJECT C1, then SELECT with empty IDs and
implementation text “Instantiate the C1 mechanism with a renamed wrapper.”
The result is terminal SELECT while C1 remains rejected and selected IDs remain
empty. No semantic acceptance/score is emitted; this is a syntactic binding
loophole, not proof that the rubric would award credit.

**Disposition recommendation: Accepted with revision.** Support the integrator's
proposed tightening: SELECT must supply nonempty IDs naming every listed mechanism
materially instantiated/combined by the implementation, and cannot intersect the
rejected set. Implementation names remain unrestricted, and semantic reviewers
still assess truthful binding and feasibility rather than lexical agreement.
Revise the pilot's empty-ID exception and test accordingly. This fits the already
selected finite-catalogue scope and applies equally to O/M/R; it needs no new
candidate registry. It does not make all described implementations automatically
valid. The separate permissive development helper retains its stated scope.

## Checks performed and bounded conclusions

Executed:

```sh
python3 -B -m unittest discover -s research/future-studies/ultra/pilot -p 'test_*.py' -v
```

Result: **9 tests run; 8 passed, 1 skipped**. The skip is
`test_loaded_packets_match_strict_contract`, explicitly because TASKS authoring
has not yet been integrated. Frozen TASKS, PRIVATE_KEYS and SURFACES are being
authored elsewhere; their absence is not a new defect. The skip must disappear
when those artifacts are integrated. Both additional reproductions above were
executed separately against the reviewed source.

The inspected parser rejects duplicate JSON keys, nonfinite numbers, malformed
request shapes, unknown action/candidate IDs, unseen source citations and invalid
terminal fields. The tested B/K behavior permits a valid final choice after
acquisition exhaustion, counts zero-unit actions as attempts, and rejects actions
after termination. Release IDs are checked against their listed inspections;
unopened release payloads do not enter the normal public view. Duplicate
inspection preserves earlier found evidence even with FAILED_CAPTURE. Terminal
acceptance remains syntactic: the adapter produces no semantic grade, score or
efficacy claim.

These conclusions apply to the inspected contract and synthetic checks only.
They do not establish semantic cue-freedom, correctness of forthcoming task keys,
independent surface equivalence, model-specific transport isolation, enforced
provider token/time budgets or actual decision benefit. Final readback should
inspect the bounded successor diff, rerun the adapter suite with the packet skip
closed, and repeat the concrete reproductions after their fixes.

## Successor readback — findings corrected at 7c74e55

Exact successor reviewed: **`7c74e5509957ecac52ba696d28b730aee42c4698`**,
including parent `c9e28cd`'s shared public contract. This section supersedes the
baseline's unresolved implementation status; the original findings and evidence
above remain historical. Reviewed source files matched this commit during the
readback. Integrator-owned generated-site edits remained untouched.

**Final scoped disposition: Accepted.** All four findings are corrected in the
inspected successor:

| Baseline finding | Observed successor result |
| --- | --- |
| Nested action-description object enters public view | Both object and list canary descriptions raise ValueError during construction; accepted descriptions require nonempty text |
| Irreversible REOPEN advertised as available | Public availability is false; a direct prohibited request still records REJECTED_IRREVERSIBLE and charges one unit |
| No public request/terminal schema | Every view supplies an identical copied contract with fields, types, candidate bindings, charging, deadlines, termination and limits; mutating a returned contract does not affect later views |
| Empty SELECT binding bypasses pruning | The exact renamed-C1/empty-ID reproduction records REJECTED_SELECTION without terminating; a novel implementation bound to unrejected C2 can still terminate SELECT, with no automatic semantic grade |

The pilot text now requires nonempty SELECT IDs for all supplied mechanisms
materially instantiated/combined and explicitly preserves semantic assessment of
unforeseen implementation names. The adapter, public contract and document agree
on this boundary. No O/M/R variable instruction wording changed in the reviewed
successor diff.

Re-ran the same focused unittest command: **10 tests run; 9 passed, 1 skipped**
in 0.021 seconds. The sole skip remains the explicitly pending loaded-packet
integration test. It is not a pass and must disappear after packet integration.
Also executed the four targeted reproductions above and the exact B=1/K=3 trace:
successful INSPECT, denied second INSPECT, valid STOP. It records REJECTED_BUDGET
for the middle attempt, spends one total acquisition unit, counts three attempts,
and ends STOP rather than EFFORT_FAILURE. No semantic acceptance was computed.

No additional actionable defect was found in this narrow successor readback.
Fresh packet release-map/surface inspection, the loaded-packet check and the
144-slot assignment manifest remain separate integration checks for the root;
they were not performed or certified here. This conclusion remains advisory
local contract review, not study authorization or empirical/model validation.

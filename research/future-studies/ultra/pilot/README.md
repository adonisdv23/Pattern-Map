# Authored pilot instrument

This directory prepares a finite synthetic comparison for review. It contains
no provider integration, empirical run, measured model behavior or effectiveness
result. Native Codex agents authored and reviewed these materials; the zero-call
fields refer to the proposed study, not to the authors' use of Codex.

The governing [pilot decision specification](../PILOT_DECISION_SPEC.md) defines
the question, exact Shared/O/M/R instructions and interpretation. The
[mechanism assessment](../MECHANISM_AND_COMPARATORS.md) explains why the question
is worth testing and why a simpler comparator may be sufficient.

## Material boundaries

| File | Responsibility |
| --- | --- |
| `TASKS.json` | Twelve fictional public tasks, first narrative, candidates, initial evidence, constraints, decision priorities, actions and limits |
| `PRIVATE_KEYS.json` | Frozen inspection releases and provisional semantic rubrics; these answer keys are excluded from the tested model's input |
| `SURFACES.json` | Separately authored second narrative, bound to exact public-task bytes; shared structured facts do not change |
| `AUTHORING_NOTES.md`, `SURFACE_REVIEW.md` | Source assumptions, author judgments, public-first review sequence, ambiguities and dispositions |
| `adapter.py`, `test_adapter.py` | Offline action parser/state transition and adversarial checks; no semantic scoring or model connection |
| `prepare.py`, `INSTRUMENT_MANIFEST.json` | Exact material/instruction hashes and reproducible 144-slot proposed assignment; every slot is planned and unlaunched |

These tasks are fresh relative to the separate eight-family development set.
They remain purposively authored examples, with repeated regimes and one task
per domain/regime cell. They are not a population sample, independently validated
benchmark, independent set of twelve domains, or evidence of transfer.

## What the offline adapter establishes

`Episode(public_task, private_releases, surface=...)` copies the supplied
objects. `view()` returns an explicit public projection, including the complete
common action contract, current evidence, action availability, candidate state,
remaining limits and attempted-action history. It receives no answer rubric,
domain or regime classification. Each inspection releases only its frozen
observation after affordability and deadline checks. Capture state cannot erase
previous positive evidence.

`submit(original_request_text)` checks strict JSON, exact fields, IDs, source
availability and terminal structure. Rejected and malformed attempts are logged
and charged under the same B/K rules as successful ones. A denied intermediate
inspection does not automatically invalidate a later justified decision. Reaching
K without a valid terminal response produces `EFFORT_FAILURE`. The adapter never
assigns semantic acceptance or an effectiveness score. An implementation can
have a new name while remaining bound to its supplied candidate mechanisms;
renaming cannot bypass a rejected candidate.

This is an in-process authoring helper, not a security sandbox. The full owner
package includes answer keys and must not be mounted for a tested model.
Separately authorized execution must restrict the model to serialized public
views, isolate episodes, retain raw wire records, and enforce/report actual
model tokens, calls and elapsed time. Invalid raw requests are bound here by a
SHA-256 digest; the helper does not replace raw-wire retention. Toy acquisition
units are not seconds, dollars or model tokens.

## Local preparation and verification

From the repository root, run only the deterministic checks:

```sh
python3 -B -m unittest discover -s research/future-studies/ultra/pilot -p 'test_*.py' -v
python3 -B research/future-studies/ultra/pilot/prepare.py
```

The preparation check verifies exact current material bytes, strict adapter
compatibility, shared information across narrative forms, the authored 3-by-4
coverage and the deterministic assignment. It does not grade rubric quality or
prove semantic equality. After a deliberate authoring revision, the primary
integrator can refresh the proposed instrument seal with:

```sh
python3 -B research/future-studies/ultra/pilot/prepare.py --write --confirm AUTHORING_ONLY_NO_STUDY
```

Review the resulting diff and commit it with the source revision. No source
change may be silently incorporated into a later running study. A revised
instrument would need a new frozen identity and exact execution authorization.

The assignment uses seed `20260907`: 12 tasks × two narratives × two repeats
× O/M/R = 144 planned slots, grouped into 48 matched blocks. Each block uses the
same candidate display order across its three arms; block order, arm order and
candidate display order are shuffled deterministically. `prepare.make_episode` applies that exact candidate permutation and narrative.
`prepare.public_prompt` composes the frozen arm instructions with only the
episode public view; neither helper calls a model. No slot has been
attempted. Preparation checks do not populate an outcome ledger or simulated
performance table.

## Remaining execution decisions

Before a model run, approve the synthetic task values and a positive minimum
useful effect, set separate practical cost margins, accept the final semantic
instrument/reviewer allocation, select one exact provider/model/configuration
and data-handling scope, and bind enforceable token/time/call limits plus a
priced maximum. The model-facing transport must then be verified against this
offline contract in its authorized environment, without exposing keys. The
launch instruction must identify exact hashes, assignment, retention location,
stop owner and expiry. Neither this directory nor a passing test supplies that
authorization.

A favorable comparison would support only the frozen package on these tasks.
A null, harmful, ambiguous, excessive-cost or shortcut-driven comparison must
remain visible and can justify narrowing or stopping this route. It cannot
rewrite the six-family human thesis or borrow results from The Echo Problem.

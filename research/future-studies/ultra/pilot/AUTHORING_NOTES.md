# Synthetic pilot instrument: authoring record

Status: **AUTHORING CANDIDATE / NO STUDY RUN / NO RESULTS / EXECUTION BLOCKED**.
Date: 2026-09-07. Governing instruction checkpoint:
`d02f58ac81fcacee77e0c128ad16cd92b454b1cf`.

This successor supplies the twelve locally authored task packets and separate
grading keys requested by the [pilot decision specification](../PILOT_DECISION_SPEC.md).
It preserves that specification and [mechanism argument](../MECHANISM_AND_COMPARATORS.md)
unchanged. These are fictional decision premises, not an acquired dataset,
observed performance measurements, validated task quality, representative
sampling, or permission to execute a study. “Private keys” here means withheld
synthetic grading records; they contain no credentials or personal information.

## Files and authority

- `TASKS.json` contains a `tasks` mapping keyed by opaque task IDs. Each object
  contains one prose narrative (`surface1`) plus structured public purpose,
  candidates, initial evidence, constraints, ordered decision priorities,
  limits, rejection policy, and the action catalogue. Public objects contain no
  regime, preferred-route field or private grading label. The facts and priorities
  must still allow the decision to be inferred; obscurity is not the intervention.
- `PRIVATE_KEYS.json` contains a separate `keys` mapping. Each key holds private
  domain/regime labels, per-action releases, worked acceptable routes, semantic
  alternatives, support conditions, partial-evidence judgments and possible harms.
  Its global `rubric_contract` governs interpretation of every key.
- This record supplies lineage and review limits. Neither it nor the private
  rubric is model input. Root is the sole integrator of these files, the separate
  surface authoring, and the offline adapter.

The public revision supplied to the independent surface author has SHA-256
`fb4faaeff2aaa0527a66743a24c310724bae7d7871a16cab19fba8d91c407204`.
The author was instructed to inspect only public task data, author surface two
and record ambiguities before reading the private keys, and bind the public
revision by hash. Any later public correction requires a corresponding surface
review and a new frozen version. Independent advisory review is recorded below;
neither its completion nor this record approves a study.

Advisory dispositions before the final public freeze are **Accepted with
revision**. Root identified concentration of useful routes at C3 and no worked
C2 selections: candidate IDs were relabeled consistently in both JSON files so
each non-HOLD regime uses C1, C2 and C3 once. Inspection IDs were also permuted
with local seed `2026090701`; public catalogues are sorted by the resulting IDs.
No acceptance fact changed merely to balance labels. The independent public-only
reader identified T007's outcome-cueing “counterexample” action descriptions,
T009's ambiguous advance-kit stock allocation, and T012's “both candidates”
wording. Public descriptions are now neutral, T009 explicitly allocates one set
of common parts, and T012 distinguishes two designs from the hybrid proposal.
These revisions serve the governing requirement for equal, reviewable information
and explicit task acceptance. The previous public hash
`f74742ad3cd37e0f61e8c75c8b405282efd7d707c8792b3d37b6889f5992478a`
is superseded; the surface author was asked to re-freeze against the new public
revision before private-key access. Strong affordance cueing in two-record tasks
is **Deferred** to semantic instrument review: it reflects deliberately supplied
metadata, and is not evidence of task quality or general discovery ability.

## Intended coverage, visible premises and costs

The private coverage matrix is the proposed three-domain, four-regime cross.
These labels describe author intent; they do not establish that a mechanism is
unfamiliar to a tested model or that it constitutes a novel contribution.

| Private domain | Useful transfer | Invalid transfer | Ordinary route adequate | Gap within available effort |
| --- | --- | --- | --- | --- |
| Local software workflows | T001: deferred help initialization | T007: order-dependent edits | T010: complete existing checker | T004: unavailable peak-memory record |
| Document handoffs | T005: tiled table with preserved associations | T011: visible removal versus required export channels | T002: approved exact-copy glossary | T008: uncertified current roster |
| Small inventory operations | T009: common kit core and late assignment | T003: mixed-unit mass versus exact count | T006: verified nearby sealed pack | T012: three required records, two acquisitions |

All narratives, names, numeric bounds, observations and alternative-world
illustrations were authored locally. They do not reuse the development case
packets as future observations. Their conceptual obligations intentionally
overlap with development coverage: an unrelated scenario is not evidence that a
mechanism generalizes. Each task is a new base decision; surface forms and repeats
remain dependent observations within that task.

Each public task binds acquisition budget `B = 2`, attempt limit `K = 8`, and
reversible rejection. Each inspection costs one unit and has step deadline six;
successful bookkeeping and terminal actions cost zero and have deadline eight.
Every request consumes an attempt. These are toy decision resources, distinct
from the narrative's stipulated milliseconds, seconds, page counts or acceptance
dimensions and from actual model tokens, elapsed time or money. Current keys
exercise acquisition and adequate stopping, including jointly useful checks;
they do not provide an empirical comparison of irreversible versus revisable
pruning. Task T009 also requires transfer across late location assignment rather
than assuming one bracket fits every target.

Candidates supply purpose and mechanism metadata equally to all arms. The
intervention therefore concerns use of supplied affordances and obligations,
not discovery or authorship of those metadata. Some decisions are deliberately
easy once their premises are respected. Floor/ceiling difficulty, surface cueing,
position cues and semantic ambiguity remain review concerns; no model outcomes
were obtained to tune them. Match candidate-order permutations across arms when
freezing assignment as specified in the governing proposal.

## Evidence release and semantic grading

An `INSPECT:<ID>` entry targets its same-named evidence ID. The private release
map returns a `process_state` plus zero or one evidence record. A stipulated
failed capture returns `FAILED_CAPTURE` and an empty evidence list; it supplies
no negative world fact and no citable target evidence. Budget or deadline
rejection releases neither the private process state nor its evidence. Initial
facts and acquired facts retain their IDs and text across arms and narratives.

For review, `required_evidence_ids` identifies support for a worked route, not
a demand to repeat every ID in the response. Lists of acceptable routes are
non-exhaustive. Judge a supported implementation or compatible combination on
its meaning and constraints, rather than its resemblance to the author's name.
The finite candidate catalogue and action contract still apply: a new label
does not manufacture evidence or authorize a new candidate ID.

The global rubric contract covers every acquired subset. A partial rule's
`all_visible_evidence_ids` requires all listed facts; a nonempty
`any_missing_evidence_ids` requires at least one absent fact, and an empty list
adds no missing condition. Compatible rules may overlap. Unlisted partial
states require semantic review using only visible facts. Preferred actions
must be filtered for already acquired records, remaining budget, step deadlines
and attempts needed to finish. Their value is judged from the public evidence
description and current uncertainty, without treating the eventual hidden
outcome as known in advance.

Record factual support separately from action quality and terminal acceptance.
For example, a single coverage check does not establish timing; a single timing
check does not establish coverage. The primary Y is operational supported-task
attainment: the nine prospectively classified `SUPPORTED_SELECTION_ATTAINABLE`
tasks require a valid supported compliant SELECT for Y = 1. An accurate HOLD
after a plausible unsuccessful inspection has Y = 0 for nonattainment, while
retaining its epistemic justification; that score does not establish avoidable
effort or an inherently needless hold. The three `INITIAL_GAP_CONTROL` tasks
permit a valid bounded HOLD/STOP to attain Y = 1. Classification is frozen from
the initial capabilities, limits and authored release universe before any
episode. It cannot be reassigned because a particular trace ended in HOLD.
A qualified prospective route may appear in HOLD's next step; it
does not become an accepted SELECT before required support exists. Conversely,
a complete initially supplied record does not require ritual rechecking.

The independent key review's S-K01 finding is **Accepted with revision**: earlier
wording left Y discretionary after a plausible failed check. The global
`rubric_contract.primary_Y`, `precedence` and each task's
`rubric.primary_terminal_acceptance` now supply the binary rule. For example,
T001 can inspect the eager-revision record, observe its failure, and lack enough
remaining acquisitions for both manifest obligations. A truthful bounded HOLD
then retains epistemic justification but attains Y = 0. Ex ante policy blame
cannot be inferred from the eventual hidden result or that score. Identical
observational traces in indistinguishable worlds retain the same epistemic
assessment. Benign rejected intermediate attempts remain charged diagnostics
unless they cause terminal invalidity, a hard-ceiling termination failure or a
hard task-constraint violation. This rule is an authored operational value
choice awaiting owner approval, not a universal definition of good judgment.
The independent reviewer confirmed the exact key readback at SHA-256
`a50190d82c44dc5b359cf1804d24be3049834474ae2fa0652b052f36ef574109`
and closed S-K01 for this authoring review. The public surface revision was
frozen before that private read and remained unchanged afterward. This is
preparatory advisory review, not validated task quality or future study approval.

T004 and T008 give indistinguishable-world examples: failed capture is compatible
with different unobserved states and supports the same bounded uncertainty.
T012's withheld records stipulate passes, but three records cannot be acquired
under the two-unit cap. Its hidden passing world must not be used to certify a
selection from two or fewer observations. Harm examples remain separate error
classes rather than summed utility weights; unnecessary checking is not by
itself fabrication or a scope violation.

## Adapter boundary and remaining work

The exact Shared/O/M/R strings and terminal/action fields remain those in the
committed pilot specification. Root's separately authored `adapter.py` is a
deterministic offline contract adapter, with `test_adapter.py` for adversarial
checks. It consumes one public task and only that task's `releases`; domain,
regime and rubric fields are excluded. The separate `SURFACES.json` supplies only
the alternate narrative string while all structured public fields and released
evidence remain identical. This tests a limited narrative paraphrase, not a
complete independent rewording of every payload field.

These paths do not imply a provider transport, configured model, real-time or
token enforcement, empirical isolation, or study execution. Before execution
approval, integration must complete the independent narrative/key review,
resolve ambiguities with fresh versions, verify the actual allowlisted adapter
and citations/charging/failure behavior, and bind task, key, prompt, surface and
adapter hashes plus the balanced assignment seed. Authoring checks establish
internal consistency only; independent preparation is not approval to run.

Owner decisions remain explicit: acceptance of the proposed task priorities;
positive advancement margin and separate resource margins; reviewer allocation;
exact provider/model/version/configuration and data handling; enforceable token,
time and call ceilings; current priced money cap; and a bounded execution
authorization binding the reviewed version, retention, stop owner and expiry.
No model call, external acquisition, participant activity, outreach or spending
was performed in authoring these three files.

Local authoring checks passed: strict JSON parsing with duplicate-key and
nonfinite-number rejection; exactly twelve matching public/private task IDs and
one task per three-by-four coverage cell; all 43 inspection/release mappings;
two failed captures with empty evidence; unique candidate/evidence/action IDs;
budget, attempt and deadline bounds; route-support and partial-rule references;
absence of private fields from the public object tree; and one C1/C2/C3 worked
selection per non-HOLD regime. The 109 successful-evidence subsets reachable
within the acquisition cap were enumerated for reference checking, without
claiming complete semantic validation. The two governing documents have no diff
from `d02f58ac81fcacee77e0c128ad16cd92b454b1cf`. No unchanged repository-wide
test suite was run for this bounded authoring change.

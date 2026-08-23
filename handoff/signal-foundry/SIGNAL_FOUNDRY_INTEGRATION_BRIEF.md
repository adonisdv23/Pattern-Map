# Signal Foundry integration brief

## Start here

Read this brief together with:

```text
handoff/signal-foundry/PATTERN_MAP_V16_CANONICAL_HANDOFF.md
```

Then inspect the two repositories at their exact stated checkpoints:

```text
Pattern Map:
  https://github.com/adonisdv23/Pattern-Map
  codex/pattern-map-v16-foundation @ d4b7b9e481165b3f692986cdda1b8a0da8b4388b
  content/site checkpoint @ c88926034cd75773dcc42d3842983c879dda5b58

Signal Foundry:
  https://github.com/adonisdv23/Signal-Foundry
  main == origin/main @ f9bf3775ca3d5b52ea5083cea52306c025727e23
  product name: Signal Foundry
```

This is an integration brief, not a Signal Foundry code change or authorization
to run anything live. Signal Foundry remains the authority for its own records,
transcripts, Visual Evidence, receipts, deployments, and production data.
Pattern Map supplies a way to ask better questions about what may influence a
decision; it does not replace Signal Foundry’s source-specific contracts.

## The recommended transfer in one paragraph

Use the Pattern Map as a small, proportionate decision-context layer around
existing Signal Foundry evidence. Start with the existing question/permission,
source identity, transcript lifecycle, Visual Evidence, graph, gap, and
decision-memory boundaries. Record only what a named question was allowed to
see, what was withheld or missing, why, and what next action is permitted. Keep
unknown relations unknown, keep visual material separate from transcript
evidence, and reuse existing receipts instead of copying their contents into a
new universal ledger. If a proposed field cannot change evidence inclusion,
permitted action, gap/hold state, or correction path, do not add it.

## Current Signal Foundry structures to preserve

| Need | Current authoritative or bounded structure | How v16 should connect |
| --- | --- | --- |
| Product and operator orientation | `README.md`, `docs/OPERATOR_RUNBOOK.md`, current admin routes in `app.py` | Use plain operator language; never expose “Discrimination Layer” as a mandatory product architecture. |
| Source identity and acquisition | `source_foundation.py`, source-specific records, `personal_corpus_source_resolution.py`, `docs/source_role_boundary_matrix.md` | Ask what source role and identity can support the named question. Never turn a display name or availability into authority. |
| Attention and next action | `daily_intelligence.py`, `docs/SIGNAL_OPERATING_SYSTEM.md`, existing `/triage` and review surfaces | Treat priority, triage, and deterministic Signals v0 as routing/attention hints, not evidence quality, truth, independence, or recommendations. |
| Cross-source comparison | `cross_source_intelligence.py`, `docs/cross_source_intelligence_v1_contract.md` | Preserve typed `source_ref`/`record_ref`, exact operator grouping bases, and non-causality boundaries. Similarity, title overlap, or rank is not a grouping basis. |
| Evidence classes and graph | `evidence_discrimination.py`, `evidence_graph.py`, `docs/evidence_discrimination_v1_contract.md`, `docs/evidence_graph_v1.md` | Use fact classes, typed relationships, contradictions, gap states, time cutoffs, and pointer/digest bindings. Do not create a master score. |
| Evidence review surface | `evidence_workbench.py`, `docs/evidence_workbench_v1.md`, `tools/evidence_workbench_offline_fixture.py` | Show a decision delta through the existing read model; do not add another queue, ranking surface, or canonical store. |
| Transcript evidence | `transcript_durable.py`, `docs/transcript_durable_stage_apply_v1.md`, `docs/SITE_NATIVE_TRANSCRIPT_WORKFLOW.md` | Only receipt-bound applied transcript pointers enter transcript-backed evidence/exports. Preview, stage, failed, unavailable, and reconciliation states remain distinct. |
| Visual Evidence | `workers/visual_evidence_cloud/**`, `docs/visual_evidence_app_workflow.md`, video-detail Visual Evidence route | Keep uploaded video/frame/OCR pointers in the Visual Evidence class. They do not become transcript text or transcript-backed exports. |
| Decision memory | `decision_memory.py`, `docs/decision_memory_retrospective_v1.md`, `docs/schemas/decision_memory_v1/decision_memory.schema.json` | Reuse append-only episode events, sequence/head protection, receipts, correction/supersession, and cutoff binding. |
| Research/context packets | `research_context.py`, `question_scoped_evidence_brief.py`, `evidence_evaluation.py` | Bind question, evidence boundary, cutoff, limitations, and evaluation scope. A replay or fixture is not a live result. |
| Safety boundary | `AGENTS.md`, `docs/pattern_recognition_evidence_boundary.md`, `docs/post_mvp_contract_index.md` | Keep all new work read-only/offline until separately authorized. |

### Important existing statuses

- `Signal Foundry` is the product name. “Sigma Foundry” is not supported by
  repository evidence.
- `AI_ANALYSIS_ENABLED` defaults to `false`; the app is standalone and has no
  automatic AI review flow.
- `docs/deterministic_signals_v0.md` describes a completed bounded read-only
  heuristic envelope, not a “Codex classifier.” It uses fixed rules, returns
  unknown where inputs are unavailable, does not persist a new classifier field,
  and does not trigger enrichment.
- The Evidence Discrimination and Workbench surfaces are bounded local/offline
  contracts and explicitly do not establish truth, usefulness, value, or
  product readiness.
- The current GitHub `main` checkout is clean relative to `origin/main`, but the
  owner’s local checkout has a pre-existing `.gitignore` modification and
  untracked `AGENTS.md`/`CLAUDE.md`. Do not clean, overwrite, stage, or delete
  those files.

## The smallest useful integration artifact

The prior Pattern Map → Signal Foundry transfer audit at local commit `4a6ed78`
identified one missing seam: Signal Foundry has evidence, provenance, graph,
Visual, transcript, and decision receipts, but not one small record that says
why a particular context was allowed to influence one named operator question.

The recommended design is an append-only **context-disposition event**, or the
smallest equivalent using existing `OPERATOR_DECISION` plus `RATIONALE` events.
It should reference existing records and receipts rather than duplicate them.

### Minimum conceptual shape

```json
{
  "event_type": "CONTEXT_DISPOSITION",
  "subject_ref": "canonical://signal-foundry/<source-specific-record>",
  "question_ref": "bounded operator question or packet reference",
  "decision_cutoff_at": "2026-08-19T14:00:00Z",
  "included_evidence_refs": ["existing transcript / visual / graph refs"],
  "excluded_or_missing": [
    {"ref": "existing gap or artifact ref", "reason_code": "VISUAL_NOT_REVIEWED"}
  ],
  "disposition": "HOLD_MANUAL_WATCH",
  "actor_ref": "trusted operator or system actor",
  "source_receipt_refs": ["existing operation / Visual / Apply receipt refs"],
  "next_allowed_action": "review_visual_evidence",
  "limitation": "This disposition does not establish truth or completeness."
}
```

This is a proposal only. A separately authorized implementation must decide
whether this is a new event type or an existing decision-memory pair, define
schema and migration rules, add offline validation, and prove a before/after
decision delta. It must:

- carry pointers, IDs, digests, and reason codes—not transcript bodies, image
  bytes, raw provider responses, credentials, or copied secrets;
- preserve `NOT_OBSERVED`, `NOT_REQUESTED`, `NOT_AUTHORIZED`, `NOT_TESTED`,
  `UNAVAILABLE`, `PRIVATE_OR_DELETED`, `PARTIAL`, `STALE`,
  `EXPECTED_BUT_MISSING`, `ABSENCE_CONFIRMED`, and `UNKNOWN` distinctly;
- bind the question, intended use, actor, decision cutoff, and exact evidence
  references;
- keep `RELATED` separate from `INDEPENDENT` and `UNKNOWN`;
- preserve contradictions instead of averaging or majority-voting them;
- keep human disposition separate from observed fact; and
- append corrections or supersessions without rewriting prior evidence.

It must not introduce:

- a universal truth score, confidence scalar, rank, source weight, or winner;
- a second Review Queue or Daily Intelligence projection;
- automatic provider/model calls, enrichment, export mutation, or deployment;
- a Pattern Map copy of Signal Foundry’s canonical records; or
- a claim that Signal Foundry validates Pattern Map v16.

## One honest worked example for the downstream app

Use the existing synthetic Evidence Workbench fixture, not live data:

1. Two synthetic exact claim occurrences are linked by an explicit syndication
   relation.
2. The raw occurrence count is `2`; the known-origin count is `1`.
3. A third synthetic claim contradicts the first claim.
4. A bounded inspection gap is `EXPECTED_BUT_MISSING`, not confirmed absence.
5. The operator records a hold pending an independently observed primary
   artifact.
6. A later synthetic outcome remains an outcome event and does not become
   independent support or proof of the earlier call.

Relevant fixture/read-model paths:

```text
tools/evidence_workbench_offline_fixture.py
tests/test_evidence_workbench.py
evidence_graph.py
evidence_workbench.py
docs/evidence_workbench_v1.md
```

This demonstrates contract behavior and a decision delta only. It is not a
real-source finding, live operator evaluation, model result, product result,
or validation study.

## Current integration plan (design-only until separately authorized)

### Phase 0 — recover the state

- Inspect Pattern Map at `d4b7b9e` and verify the owner-intent checksum.
- Inspect Signal Foundry at `main`/`f9bf377`, preserving local dirty files.
- Read the transfer audit from local branch `codex/pattern-map-signal-foundry-transfer-audit`
  at `4a6ed78`; treat it as a read-only report.
- Record which findings are already implemented, design-only, missing, or
  deferred. Do not combine branches in place.

### Phase 1 — offline contract proof

If the owner later authorizes a Signal Foundry implementation branch, start with
one fixture and tests for:

- bounded question, intended use, actor, cutoff, and permission;
- exact included/excluded evidence references and reason codes;
- attention-versus-support separation;
- identity-pending/record-only versus provider/task authorization;
- transcript lifecycle and Visual Evidence non-contamination;
- relatedness versus independent corroboration;
- missingness and expected-absence distinctions;
- late evidence and correction/supersession; and
- deterministic replay with unchanged existing bodies and receipts.

The fixture must fail closed on stale digests, unknown actors, missing reasons,
late evidence, unbound references, or unauthorized actions. A passing offline
fixture is a contract check, not an outcome claim.

### Phase 2 — bounded product review

Only after an authorized implementation exists should an agent inspect whether
one operator workflow actually changes in a useful, lower-ceremony way. The
review must remain local/offline unless a separate owner instruction authorizes
hosted access. It should ask:

- Did the record change what evidence was included or withheld?
- Did it prevent a false absence, false corroboration, or unauthorized action?
- Did it make the next safe action clearer?
- Did it preserve a correction path?
- Would the existing receipt/decision-memory path have been enough?

If the answer is no, stop and do not add the event.

### Phase 3 — future live work, not included here

Deployment, provider calls, source acquisition, model analysis, dataset
acquisition, participant work, production-data mutation, and publication each
need their own exact owner authorization. None is implied by this brief.

## Orphaned work recovery

“Orphaned” means **recoverable but disconnected**, not deleted. A thread can
end while its branch remains. A branch can exist locally without an upstream.
A commit can contain useful work without being part of `main`, a current PR, or
the current task.

Current verified example:

```text
Signal Foundry main: f9bf377 == origin/main
Local audit branch: codex/pattern-map-signal-foundry-transfer-audit
Audit commit:       4a6ed78
Upstream:            none
Change:             one read-only 533-line transfer audit
```

Recovery checklist, read-only first:

```sh
cd /Users/gpt/Documents/Codex/projects/Signal-Foundry
git status --short --branch
git show --stat 4a6ed78
git branch --contains 4a6ed78
git diff main..codex/pattern-map-signal-foundry-transfer-audit --stat
git log --oneline main..codex/pattern-map-signal-foundry-transfer-audit
```

If a later owner instruction authorizes integration:

1. Create a new isolated worktree from current `main`.
2. Inspect the exact diff and read the report.
3. Decide whether it is archival documentation, an app change, or a rejected
   recommendation. Do not infer an implementation from the report.
4. Commit only the selected, reviewed files on a named feature branch.
5. Push that branch only when authorized and verify the remote object.
6. Never reset the dirty main checkout, delete user files, or claim a push,
   merge, deployment, or result before Git/provider evidence confirms it.

## Copyable prompt for Claude Code

Copy the block below into the Claude Code task that is supposed to finish or
review Signal Foundry. It is intentionally explicit because the previous
session used “V14,” “Sigma Foundry,” “deep link,” “classifier,” and “orphaned”
loosely.

```text
You are reviewing the Pattern Map v16 → Signal Foundry handoff.

Read these first, in order:

1. handoff/signal-foundry/PATTERN_MAP_V16_CANONICAL_HANDOFF.md
2. handoff/signal-foundry/SIGNAL_FOUNDRY_INTEGRATION_BRIEF.md
3. Pattern Map docs/OWNER_INTENT_V16.md
4. Pattern Map docs/THESIS_AND_AUDIENCE_CONTRACT_V16.md
5. Pattern Map docs/ARTIFACT_BOUNDARIES.md
6. Signal Foundry AGENTS.md, CLAUDE.md, and README.md
7. Signal Foundry docs/evidence_discrimination_v1_contract.md
8. Signal Foundry docs/evidence_graph_v1.md
9. Signal Foundry docs/evidence_workbench_v1.md
10. Signal Foundry docs/transcript_durable_stage_apply_v1.md
11. Signal Foundry docs/visual_evidence_app_workflow.md
12. Signal Foundry docs/decision_memory_retrospective_v1.md
13. Signal Foundry docs/pattern_recognition_evidence_boundary.md

Use exact current source identities:

- Pattern Map v16 is the broad human-first Pattern Recognition / Discrimination
  Layer project at branch codex/pattern-map-v16-foundation, commit
  d4b7b9e481165b3f692986cdda1b8a0da8b4388b. Its content/site implementation
  checkpoint is c88926034cd75773dcc42d3842983c879dda5b58.
- Signal Foundry is the product name, not Sigma Foundry. Its current main and
  origin/main are f9bf3775ca3d5b52ea5083cea52306c025727e23.
- The local Pattern Map → Signal Foundry transfer audit is branch
  codex/pattern-map-signal-foundry-transfer-audit at 4a6ed78. It is read-only,
  one commit ahead of main, has no upstream, and is not an integrated app
  change. Do not push or merge it in this task.

Your job in this turn is to produce a source-grounded integration assessment
and, if useful, a separately scoped implementation plan. Do not mutate Signal
Foundry unless a new exact owner instruction authorizes a feature branch and
specific implementation paths. Preserve the existing local .gitignore change
and untracked AGENTS.md/CLAUDE.md; never clean them.

Map v16 onto existing Signal Foundry structures:

- evidence_discrimination.py / docs/evidence_discrimination_v1_contract.md
- evidence_graph.py / docs/evidence_graph_v1.md
- evidence_workbench.py / docs/evidence_workbench_v1.md
- decision_memory.py / docs/decision_memory_retrospective_v1.md
- cross_source_intelligence.py / docs/cross_source_intelligence_v1_contract.md
- daily_intelligence.py and existing triage/review routes
- transcript_durable.py / docs/transcript_durable_stage_apply_v1.md
- docs/visual_evidence_app_workflow.md and Visual Evidence code
- source_foundation.py and source identity resolution

Preserve these boundaries:

- Signal Foundry’s source-specific records remain authoritative.
- Pattern Map is a decision-context vocabulary, not a new canonical store,
  classifier, queue, score, or universal architecture.
- Existing deterministic Signals v0 are read-only heuristic markers, not a
  Codex classifier and not evidence of quality or truth.
- `RELATED`, `INDEPENDENT`, and `UNKNOWN` remain distinct; recurrence is not
  corroboration; provenance is not correctness; access is not permission.
- Visual Evidence never becomes transcript evidence or transcript export text.
- Preview/stage/apply and human authority remain explicit.
- A fixture, QA run, proxy review, or planning recommendation is not an
  empirical result or product validation.

Evaluate the smallest proposed seam: an append-only context-disposition event
(or existing OPERATOR_DECISION + RATIONALE pair) that binds a named question,
intended use, decision cutoff, included evidence pointers, excluded/missing
references with reason codes, disposition, actor, next allowed action, and
limitations. Reuse existing receipts and decision memory. Do not copy raw
transcripts, images, provider bodies, credentials, or secrets. Do not add a
score, rank, source weight, truth label, or automatic recommendation.

Return:

1. Exact repository/branch/head state and any dirty-file warning.
2. A table classifying each transfer finding as already implemented,
   design-only, a genuine current gap, deferred, or unsupported.
3. The smallest before/after operator decision delta, if one exists.
4. A no-change design plan for the next bounded offline fixture and tests.
5. Any true blocker to a future implementation, with exact paths.
6. The owner decisions actually required, keeping the list as short as possible.

Do not invent a V14 pass deep link, a Pattern Map classifier output, a Claude
thread status, a GitHub push, a deployment, a provider call, a model result, or
a research result. If you cannot verify it from Git or a file, say that it is
unverified.
```

## Machine-readable handoff checklist

The following JSON is intentionally small and mirrors the prose above. It is a
checklist, not an authorization receipt or a product result.

```json
{
  "schema_version": "pattern_map_signal_foundry_handoff_v1",
  "product_name": "Signal Foundry",
  "pattern_map": {
    "repository": "https://github.com/adonisdv23/Pattern-Map",
    "branch": "codex/pattern-map-v16-foundation",
    "head": "d4b7b9e481165b3f692986cdda1b8a0da8b4388b",
    "content_checkpoint": "c88926034cd75773dcc42d3842983c879dda5b58",
    "site_status": "local_owner_review_only",
    "research_status": "unrun_no_results"
  },
  "signal_foundry": {
    "repository": "https://github.com/adonisdv23/Signal-Foundry",
    "branch": "main",
    "head": "f9bf3775ca3d5b52ea5083cea52306c025727e23",
    "working_tree_status": "clean_relative_to_origin_with_preexisting_local_files",
    "ai_analysis_default": false,
    "integration_status": "not_implemented_on_main"
  },
  "orphaned_audit": {
    "branch": "codex/pattern-map-signal-foundry-transfer-audit",
    "commit": "4a6ed78",
    "upstream": null,
    "status": "recoverable_local_read_only_not_integrated"
  },
  "proposed_seam": {
    "name": "CONTEXT_DISPOSITION",
    "status": "design_only",
    "reuses": ["existing_evidence_refs", "existing_receipt_refs", "decision_memory"],
    "forbidden": ["score", "rank", "truth_label", "automatic_provider_call", "raw_body_copy"]
  },
  "required_checks": [
    "verify_pattern_map_owner_intent_checksum",
    "verify_exact_git_heads",
    "preserve_signal_foundry_dirty_user_files",
    "keep_related_independent_unknown_distinct",
    "keep_visual_separate_from_transcript",
    "keep_plan_event_outcome_human_decision_distinct",
    "no_deploy_no_publish_no_provider_no_model_no_study"
  ]
}
```

## Owner handoff in one sentence

Give Claude the two Markdown files named here and the exact Pattern Map commit;
ask it to assess or prepare the smallest offline, receipt-referencing
context-disposition seam inside existing Signal Foundry boundaries. Do not give
it a fictional deep link or classifier, and do not let an ended thread or
unupstreamed branch masquerade as current application state.

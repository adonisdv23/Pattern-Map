# Pattern Map v16 → Signal Foundry

## Canonical handoff for a tired owner or a new agent

Status: **ready to consume; owner-review development, not publication or
deployment**

## If you only read five lines

1. Give Claude exactly `handoff/signal-foundry/PATTERN_MAP_V16_CANONICAL_HANDOFF.md` and `handoff/signal-foundry/SIGNAL_FOUNDRY_INTEGRATION_BRIEF.md`.
2. Inspect `codex/pattern-map-v16-foundation` at canonical source checkpoint `bc7e7c5f95c85b8f6f969ed87ff7fa81cdb2ae91`; preserve `d4b7b9e`, `c889260`, and `ad964dd` only as audited predecessor anchors.
3. Use Signal Foundry `main` at audited checkpoint `f9bf3775ca3d5b52ea5083cea52306c025727e23`, preserving its existing local files.
4. The product is **Signal Foundry**; there is no verified V14 deep link, Pattern Map classifier output, or “Sigma Foundry” project to supply.
5. This is design/review only: test the existing `OPERATOR_DECISION` + `RATIONALE` seam first; do not mutate Signal Foundry or invent a new event type.

This is the one place to start when another task asks for the Pattern Map /
Discrimination Layer. It names the exact canonical source checkpoint, the
audited predecessor anchors, the artifacts that matter, what is historical,
and what a downstream Signal Foundry task may safely do.

The product is **Signal Foundry**, not “Sigma Foundry.” Signal Foundry’s own
README names the product explicitly. Legacy infrastructure slugs such as
`youtube-signal-monitor` may still appear in operational paths, but they are
not the user-facing product name.

## Start here

### Canonical Pattern Map source checkpoint

Repository: <https://github.com/adonisdv23/Pattern-Map>

Canonical source checkpoint after all content, site, Echo, and handoff lanes
converged:

```text
branch:  codex/pattern-map-v16-foundation
source:  bc7e7c5f95c85b8f6f969ed87ff7fa81cdb2ae91
content: bc7e7c5f95c85b8f6f969ed87ff7fa81cdb2ae91
PR:      https://github.com/adonisdv23/Pattern-Map/pull/1
state:   draft/open/unmerged; owner review and manual gates remain open
```

The independently audited predecessor head was
`d4b7b9e481165b3f692986cdda1b8a0da8b4388b`; the ChatGPT Pro Round 2 content
checkpoint was `c88926034cd75773dcc42d3842983c879dda5b58`, and the earlier
converged source before the owner visual/export repair was
`ad964dd91eff521b0442f613c55bc4e9e97c2f2a`. They remain audit anchors, not
the current source. The evidence/checksum commit that follows `bc7e7c5` may
advance the branch head without changing the canonical source
checkpoint. Resolve Git before editing and do not substitute an older
conversation, screenshot, or deep link for this source commit.

Canonical local checkout used by the orchestration work:

```text
/Users/gpt/Documents/Codex/projects/Pattern-Map
```

If your task is running in another checkout, resolve the branch and commit
with Git before editing. Do not infer currentness from a conversation title,
an old screenshot, a self-referential handoff paragraph, or a deep link that
is not present in the repository.

### The fastest useful review path

Read these in order:

1. `docs/OWNER_INTENT_V16.md`
2. `docs/THESIS_AND_AUDIENCE_CONTRACT_V16.md`
3. `docs/ARTIFACT_BOUNDARIES.md`
4. `manuscript/NINETY_SECOND_VERSION.md`
5. `manuscript/PATTERN_RECOGNITION_V16.md`
6. `framework/SIX_FAMILIES.md`
7. `framework/agent-playbook/QUICKSTART.md`
8. `cases/signal-foundry/README.md`
9. `research/the-echo-problem/README.md`
10. `research/the-echo-problem/STATUS_AND_BOUNDARIES.md`
11. `handoff/OWNER_REVIEW_PACKET_V16.md`

The locked intent must verify before integration:

```sh
cd /Users/gpt/Documents/Codex/projects/Pattern-Map
(cd docs && shasum -a 256 -c OWNER_INTENT_V16.sha256)
```

### The local site

The site is a real authored, dependency-free, interactive review surface. It
is not a text dump or a PDF substitute. The three principal doors are:

- **Read the idea** — `site/dist/read/index.html` after a local build;
- **Explore the map** — `site/dist/map/index.html` after a local build; and
- **Apply it** — `site/dist/apply/index.html` after a local build.

There is also a continuous **Guided read** at
`site/dist/guided/index.html`, plus Examples, Boundaries, Sources, Research,
and History routes. `site/dist/` is generated and should not be committed.

Build and serve it locally:

```sh
cd /Users/gpt/Documents/Codex/projects/Pattern-Map/site
npm ci
npm run build
npm run check
npm run dev
```

The current direct-open companion is:

```text
/Users/gpt/Documents/Codex/projects/Pattern-Map/site/exports/standalone/pattern-map-v16.html
```

The secondary visual review companion is:

```text
/Users/gpt/Documents/Codex/projects/Pattern-Map/site/exports/pattern-map-v16-owner-review.pdf
```

The semantic routed site and standalone HTML are the primary review surfaces;
the PDF is intentionally a visual companion. No public v16 URL has been
authorized or deployed. Do not invent a “V14 pass deep link.” V14 is a
historical source, not the current v16 site.

For transfer to another computer, send the committed standalone HTML together
with its repository-relative historical image, or use the verified portable
bundle. For PDF review, use the deliberately composed six-page companion above.
Do not substitute a browser extension's full-page capture or a custom jsPDF
export: those paths can combine routes, expand technical appendices, or impose
a non-print viewport. A receiving agent should rebuild locally and inspect the
routed site before attributing a visual defect to current source. The current
standalone build also verifies balanced main markup and requires every route to
remain inside the publication content column.

## What v16 is

Pattern Recognition / The Discrimination Layer v16 is the broad principal
project: a human-first thought piece, six-family framework, builder/operator
translation, observable AI-agent playbook, bounded examples, and interactive
local site.

Its central proposition is that AI-assisted work inherits decisions made before
generation. The Discrimination Layer is the explicit, inspectable,
cost-bounded, and correctable responsibility for deciding what the system
should notice, compare, preserve, question, and allow to influence an answer.

It is deliberately not a settled scientific result, a universal architecture,
a provenance-only system, a magic creativity prompt, or a replacement for
human judgment.

## Version hierarchy and supersession

| Version / project | Current role | What a downstream task may use |
| --- | --- | --- |
| v13 | Historical origin of the broad reader problem, ambition, six families, and original visual map | Continuity and intent; never current topology or proof of effectiveness |
| v14 | Immutable complete transfer | Rigor, accessibility, prior-art, implementation, and design lessons; do not rewrite the archive |
| v15 / v15.1 | Historical intermediate checkpoints | Historical context only; do not treat as current v16 source |
| v15.2 | Exact source checkpoint for **The Echo Problem / ECHO-01** | Preserve unchanged and use only for Echo or selectively reusable interface/research patterns |
| EP v0.1 | Curated successor under `research/the-echo-problem/` | Separate unrun research track with explicit no-results boundary |
| EP v1.1 | Active design-only successor under `research/the-echo-problem/v1_1/` | Narrowed protocol, provider-free checks, and prospective research order; never a result or v16 definition |
| v16 | Current broad Pattern Map project | Canonical standalone framework and site described in this handoff |

Nothing is deleted or silently renamed. Origin accounting is one worked
example and research track inside the history; it is not the definition of v16.

## Authority order

When documents disagree, use this order:

1. The owner’s approved v16 handoff and later exact owner instructions.
2. `docs/OWNER_INTENT_V16.md` and its checksum.
3. Recovered v13 material for historical idea, ambition, six families, and the
   reader problem.
4. V14/v15 material for rigor, limits, terminology, implementation patterns,
   accessibility, prior art, and design lessons.
5. V15.2 for The Echo Problem and selectively reusable interface/research
   patterns.
6. Agent, Claude, ChatGPT, and other model reviews as advisory work products
   only.

A detailed review does not outrank locked owner intent. Research may narrow a
claim; it may not silently redefine the thesis. A protocol, fixture, QA pass,
model review, or design illustration is not an empirical result.

## Six-family map

All six families must remain visible and meaningful. Supporting schemas and
implementation components must not replace this public map.

| Family | Reader question | Boundary |
| --- | --- | --- |
| **F1 — Peripheral signal** | What might the default path have overlooked? | Underweighted or less visible is a reason to inspect, not a reason to believe. |
| **F2 — Source weighing** | What role does each source and information path play for this exact claim? | Recurrence, authority, support, relevance, origin, and permission stay distinct. |
| **F3 — Velocity / motion** | What is changing unusually relative to a relevant baseline? | Change deserves examination, not automatic belief or action. |
| **F4 — Absence + memory** | What should be present but is not, and what prior context changes the meaning of now? | Absence needs an expected baseline; memory remains versioned and source-bound. |
| **F5 — Structured patterns** | What becomes visible through explicit comparison of peers, periods, attributes, and relationships? | Comparison must not force unlike cases into false equivalence. |
| **F6 — Learning loop** | What did we expect, what happened, and what bounded update should be proposed? | Outcomes do not rewrite history or automatically change policy. |

## Canonical v16 artifacts

### Human-facing

```text
manuscript/PATTERN_RECOGNITION_V16.md
manuscript/NINETY_SECOND_VERSION.md
manuscript/MENTOR_COVER_NOTE.md
manuscript/PUBLIC_ABSTRACT.md
manuscript/ORIGIN_NOTE.md
manuscript/SOURCES_AND_RESEARCH_ROUTE.md
```

### Builder and operator-facing

```text
framework/SIX_FAMILIES.md
framework/SIX_FAMILIES.json
framework/SIX_FAMILIES.schema.json
framework/RELATIONSHIP_MAP.md
framework/GLOSSARY.md
framework/OPERATOR_PLAYBOOK.md
framework/IMPLEMENTATION_CHOICES.md
framework/BOUNDARIES_AND_FAILURES.md
framework/mechanisms/**
framework/templates/**
cases/signal-foundry/README.md
cases/general-research/README.md
cases/product-and-process/README.md
```

### Agent-facing

```text
framework/agent-playbook/QUICKSTART.md
framework/agent-playbook/FULL_OPERATING_GUIDE.md
framework/agent-playbook/COPYABLE_AGENT_BRIEF.md
framework/agent-playbook/PREFLIGHT_CHECKLIST.md
framework/agent-playbook/DECISION_RECEIPT_TEMPLATE.md
framework/agent-playbook/ORDINARY_VS_DISCRIMINATION_LAYER.md
```

### Site and evidence

```text
site/build.mjs
site/check.mjs
site/src/site.js
site/src/site.css
site/src/recommendation.js
site/exports/standalone/pattern-map-v16.html
site/exports/pattern-map-v16-owner-review.pdf
qa/site/**
qa/interaction/**
qa/visual/**
assets/IMAGE_USE_LEDGER.md
```

### Research separation

```text
research/README.md
research/THE_DISCRIMINATION_LAYER_RESEARCH_AGENDA.md
research/future-studies/DL_PLAYBOOK_MATCHED_BUDGET_PROTOCOL_V0_1.md
research/the-echo-problem/README.md
research/the-echo-problem/STATUS_AND_BOUNDARIES.md
research/the-echo-problem/RELATION_TO_V16.md
research/the-echo-problem/FUTURE_EXECUTION_PLAN.md
research/the-echo-problem/VERSION_HISTORY.md
research/the-echo-problem/preserved/v15.2/**
archive/transfers/v15.2-owner-handoff/**
```

The Echo Problem is explicitly `unrun / no results`. The broader matched-budget
study is also a future protocol only. Do not select a model/provider/dataset,
run a study, spend, preregister, or present any fixture or QA output as a
result.

## How Signal Foundry should use v16

Use the framework as a decision-safety vocabulary and review discipline, not as
an 11-service architecture and not as a new canonical data store.

The existing Signal Foundry transfer surface is:

| Pattern Map responsibility | Existing Signal Foundry surface | Safe interpretation |
| --- | --- | --- |
| Define the decision and authority | `docs/evidence_discrimination_v1_contract.md`, `question_scoped_evidence_brief.py`, `decision_memory.py`, operator review routes | Bind a named question, intended use, actor, permission, and cutoff; technical access is not permission. |
| Acquire and stop proportionately | `docs/SITE_NATIVE_TRANSCRIPT_WORKFLOW.md`, `docs/transcript_durable_stage_apply_v1.md`, `transcript_durable.py` | Preserve Preview → Stage → Apply; no hidden retry, provider fallback, or automatic promotion. |
| Weigh source role and provenance | `source_foundation.py`, `sources.yaml`, source-specific records, `docs/source_role_boundary_matrix.md` | Preserve source identity, role, provenance, and availability without making a trust score. |
| Compare and trace relatedness | `cross_source_intelligence.py`, `docs/cross_source_intelligence_v1_contract.md`, `evidence_graph.py` | Exact operator grouping or typed relation is context; relatedness is not truth or independence. |
| Preserve contradictions and gaps | `evidence_discrimination.py`, `evidence_graph.py`, `evidence_workbench.py`, `docs/evidence_discrimination_v1_contract.md` | Keep `UNKNOWN`, `PARTIAL`, `UNAVAILABLE`, `EXPECTED_BUT_MISSING`, and contradiction states distinct. |
| Keep visual context separate | `docs/visual_evidence_app_workflow.md`, `workers/visual_evidence_cloud/**`, video-detail Visual Evidence route | Visual/OCR artifacts remain Visual Evidence; they never become transcript text or transcript-backed exports. |
| Record influence and human disposition | `decision_memory.py`, `docs/decision_memory_retrospective_v1.md`, existing Apply receipts | Reuse the existing append-only decision-memory path; do not add a duplicate universal receipt. |
| Learn without rewriting history | `decision_memory.py`, `evidence_evaluation.py`, `docs/evidence_workbench_v1.md` | Record expectations, later outcomes, corrections, and limitations; a later outcome is not automatic proof. |

The **default seam to test** is Signal Foundry's existing, valid append-only
decision-memory pair: `OPERATOR_DECISION` plus `RATIONALE`. Bind the pair to the
current subject and evidence snapshot using the schema's existing
`subject_binding` and the event pair's current `evidence_digest`,
`evidence_ref`, and `statement` fields where applicable. An authorized
offline fixture should first test whether that pair produces a useful decision
delta without changing the schema.

The following object is only a conceptual completeness worksheet. It is
**not valid** against the current closed
`decision_memory.schema.json`: `CONTEXT_DISPOSITION` is not an allowed
`event_type`, and the current event schema has `additionalProperties: false`.
`VISUAL_NOT_REVIEWED`, `HOLD_MANUAL_WATCH`, and any similar all-caps value here
are proposed local reason/disposition vocabulary, not existing Signal Foundry
enums.

```json
{
  "concept_name": "CONTEXT_DISPOSITION",
  "schema_status": "NOT_VALID_AGAINST_CURRENT_SIGNAL_FOUNDRY_DECISION_MEMORY_V1",
  "question_ref": "bounded operator question or packet reference",
  "subject_ref": "canonical Signal Foundry record pointer",
  "decision_cutoff_at": "UTC instant",
  "included_evidence_refs": ["existing transcript / visual / graph refs"],
  "excluded_or_missing": [{"ref": "existing gap or artifact ref", "proposed_local_reason_code": "VISUAL_NOT_REVIEWED"}],
  "disposition": "HOLD_MANUAL_WATCH",
  "actor_ref": "trusted operator or system actor",
  "source_receipt_refs": ["existing operation / Visual / Apply receipt refs"],
  "limitation": "This disposition does not establish truth or completeness."
}
```

Do not implement that conceptual object. Consider a new event type only if a
separately authorized offline fixture first proves that the valid
`OPERATOR_DECISION` + `RATIONALE` pair cannot express a material, useful
decision delta and records the exact insufficiency. Any later schema proposal
would require its own review, migration plan, write authority, and tests. No
option may copy transcript bodies, images, raw provider responses, credentials,
or secrets, or add a master score, rank, confidence scalar, source weight,
truth label, or automatic recommendation.

## What not to do

- Do not make Signal Foundry depend on a “Pattern Map classifier.” No such
  canonical v16 classifier output exists.
- Do not call Signal Foundry “Sigma Foundry.”
- Do not invent a public or hosted Pattern Map deep link. Use the local build and
  the repository/GitHub checkpoint above.
- Do not replace the six families with a provenance graph, classifier, score, or
  source-count dashboard.
- Do not turn `related`, recurrence, provenance, or source identity into truth or
  independent corroboration.
- Do not merge the Echo Problem into v16 or use its unrun protocol as product
  validation.
- Do not deploy, publish, merge to `main`, call a model/provider, acquire a
  dataset, spend, preregister, or contact people from this handoff.
- Do not copy Pattern Map files into Signal Foundry’s canonical data store.
  Signal Foundry remains the authority for its own records and receipts.

## The three Claude follow-ups, now resolved plainly

Claude’s preserved Pattern Map session ended with three owner-facing items. The
exact wording is preserved in its local session record and transcript; the
summary below is the current resolution.

| Claude item | What it meant | Current resolution |
| --- | --- | --- |
| **Push it yourself** | The Claude session’s stored GitHub token was invalid, so it could not push the Pattern Map branch. | Resolved by the primary orchestration path: canonical source is `bc7e7c5` on `codex/pattern-map-v16-foundation`; the authorized final evidence push and remote PR readback are recorded in the owner-review handoff. The separate Signal Foundry audit branch remains local-only. |
| **Look at the Map route** | Claude wanted the owner to judge whether the corrected current Map route matched the owner’s visual expectation. | The route exists and is locally buildable at `site/dist/map/index.html`; current source is `bc7e7c5`, with Pro correction history at `c889260` and earlier converged source `ad964dd`. Automated and proxy checks pass; physical keyboard, screen reader, real zoom, forced colors, print preview, touch, and owner taste remain human review gates. |
| **Decide if the evidence rule bites too hard** | Claude tightened guards around unreachable CSS, false file extensions, exact checkpoints, and planning-versus-event language. | The strictness is now the canonical safety posture recorded in the locked intent, D-025, the acceptance matrix, and the current QA. No new owner decision is needed to consume v16. If an owner later wants a guard relaxed, record an explicit decision and revise the affected contract; do not silently weaken it. |

## “Orphaned” work in plain language

Orphaned does not mean deleted. It means a conversation or branch stopped being
the active path, and its work is not yet connected to the current canonical
branch, an upstream remote, or an integrated pull request.

The concrete Signal Foundry example is:

```text
repository:  /Users/gpt/Documents/Codex/projects/Signal-Foundry
current:     main == origin/main == f9bf3775ca3d5b52ea5083cea52306c025727e23
orphan:      codex/pattern-map-signal-foundry-transfer-audit
commit:      4a6ed78 (one commit ahead of main)
upstream:    none
content:     one 533-line read-only Pattern Map v15.2 transfer audit
state:       recoverable locally, not integrated into main, not on GitHub
```

That audit is useful evidence and should be read, but it is not a current
Signal Foundry implementation. Do not push or merge it as part of this
handoff. If an owner later wants to preserve it remotely, the recovery sequence
is:

```sh
cd /Users/gpt/Documents/Codex/projects/Signal-Foundry
git status --short --branch                 # preserve existing user changes
git show --stat 4a6ed78                     # confirm the exact object
git branch --contains 4a6ed78
git diff main..codex/pattern-map-signal-foundry-transfer-audit --stat
git log --oneline main..codex/pattern-map-signal-foundry-transfer-audit
```

Then, only under a new exact owner instruction, create a named remote feature
branch or cherry-pick the single audit commit into an isolated worktree. Do not
use `git reset --hard`, overwrite the dirty main checkout, or describe the audit
as an app change. The local `.gitignore` modification and untracked
`AGENTS.md`/`CLAUDE.md` in Signal Foundry predate this handoff and must remain
untouched.

## Current Signal Foundry blockers and non-blockers

### Genuine blockers for a Pattern Map integration

1. **No Pattern Map integration fixture is currently on Signal Foundry
   `main`.** The valid `OPERATOR_DECISION` and `RATIONALE` event types already
   exist, but no authorized offline fixture has yet shown whether that pair is
   sufficient for the bounded transfer. The local transfer audit is a report,
   not an implementation, and no need for a new event type has been established.
2. **No current owner authorization exists for a Signal Foundry schema/write
   change, migration, provider/model call, deployment, or production data.**
   The integration must remain a design brief until separately authorized.
3. **The current Pattern Map handoff has no hosted deep link.** A Claude or
   Sigma/Signal Foundry task must build the local site or read the exact GitHub
   checkpoint rather than guessing a URL.
4. **Owner/manual v16 gates remain open.** That affects whether the owner calls
   Pattern Map ready for personal use, not whether the brief can guide a
   bounded design review.

### Not blockers

- The product-name question is settled: Signal Foundry.
- The six-family framework, agent playbook, and site source are present.
- Canonical Pattern Map source is frozen at `bc7e7c5`; a later evidence-only
  branch head does not replace that content checkpoint.
- The local Signal Foundry transfer audit is recoverable and its orphan status
  is understood.
- Signal Foundry’s existing deterministic Signals v0 is not a missing Pattern
  Map classifier; it is a read-only, no-LLM heuristic marker documented in
  `docs/deterministic_signals_v0.md` and surfaced under existing triage.

## What to give Claude

Give Claude these two repository artifacts:

1. `handoff/signal-foundry/PATTERN_MAP_V16_CANONICAL_HANDOFF.md`
2. `handoff/signal-foundry/SIGNAL_FOUNDRY_INTEGRATION_BRIEF.md`

If the Claude task cannot see the repository, provide the GitHub repository and
the exact audited v16 branch/commit above. If either handoff file is absent from
Claude's checkout, attach or copy the exact file, or stop and request that exact
file; never infer its contents from this summary or an older conversation. Do
not provide secrets, cookies, credentials, private transcripts, or a made-up
deep link.

## Governing boundary

This handoff is a navigation and design aid. It does not merge, deploy,
publish, run a model or study, acquire a corpus, select a provider, spend, or
change Signal Foundry. The primary orchestrator must inspect and disposition
this branch before any integration.

# V13 continuity and owner-intent fidelity audit

Status: **Advisory continuity review — no canonical change, study, provider
call, or external action**

Reviewed snapshot: commit `223d19069a3d61069c3eedec64e6ccdd38852dff`
(`Build v16 applied framework and agent playbook`), not the moving worktree.

Reviewed date: 2026-08-19

Reviewed scope:

- locked contracts: `docs/OWNER_INTENT_V16.md`,
  `docs/THESIS_AND_AUDIENCE_CONTRACT_V16.md`,
  `docs/V13_TO_V16_FIDELITY_MATRIX.md`, and the required foundation records;
- recovered v13 material under
  `archive/transfers/v14-complete-2026-08-18/05_HISTORICAL_V13/`, including
  the recovery memo, rendered DOM snapshot, and reference manifest;
- `manuscript/**`, `framework/**`, and `cases/**` at the reviewed snapshot.

The snapshot owner-intent bytes were checked directly: the SHA-256 recorded in
`223d190:docs/OWNER_INTENT_V16.sha256` matches the SHA-256 of
`223d190:docs/OWNER_INTENT_V16.md` (`3aea5eeb19302a0e6498f7bcfccb23535953dbb6807fb5a486e0279bfa72543b`).

## Evidence boundary and method

This report distinguishes repository evidence from model judgment. “Evidence”
below means text, structure, or status visible in the named snapshot file and
line range. “Model judgment” is the reviewer’s interpretation of whether that
evidence satisfies the locked continuity requirement; it is not a reader study,
empirical result, owner instruction, or proof that the framework works.

The historical v13 source is treated as recovered historical intent, not as
evidence that its mechanisms work. The recovery memo explicitly gives v13 the
historical reader problem, ambition, six-family structure, and implementation
paths while marking the practical promise unvalidated
(`archive/transfers/v14-complete-2026-08-18/05_HISTORICAL_V13/V13_RECOVERY_AND_INTENT_MEMO.md:15-28,30-51`).
The rendered DOM is a post-render reference snapshot rather than the unavailable
original standalone HTML; that limitation is recorded in the reference
manifest (`archive/transfers/v14-complete-2026-08-18/05_HISTORICAL_V13/LIVE_SITE_REFERENCE_MANIFEST.json:57-75`).

## Overall continuity gate verdict

**PASS WITH ONE LOW-SEVERITY FOLLOW-UP; no continuity blocker found.**

The reviewed snapshot preserves the original broad proposition: generic or
stale-feeling AI work can be shaped upstream by predictable search paths,
source choices, missing comparisons, absent information, and missing memory;
Pattern Recognition names the discipline of improving those choices before
generation. It also preserves the original practical ambition—raising the
floor of disciplined, decomposable practice for builders and agents—while
correctly narrowing unsupported v13 formulations and keeping human judgment,
permission, uncertainty, cost, and consequential authority visible.

All six historical families remain visible and meaningful. The Echo/common-origin
material is later, subordinate, and explicitly removable; it does not define
the opening, the 90-second version, the essay, or the current builder/agent map.
The human essay and mentor cover note retain the coffee-conversation frame,
while the framework, agent companion, and cases translate the idea into
inspectable procedures and bounded fixtures without presenting them as results.

The one follow-up is not a failure of owner intent. The applied framework
offers lightweight, moderate, and advanced choices, but it no longer explicitly
maps those choices to the three v13 implementation paths (process layer,
intermediary reasoning/workflow, and optional custom-model path). A single
stack-neutral sentence in the builder implementation guide would make that
continuity legible without reintroducing v13’s rejected hierarchy claims.

This is a continuity-lane verdict only. It is not a full v16 release or site,
accessibility, archive, Echo, research, or deployment acceptance verdict.

## Findings

### V13-01 — Informational / PASS — Broad reader problem, pre-generation leverage, and ambition survive

**Class:** Historical-intent continuity; no defect found.

**Evidence:**

- The recovered memo says v13 starts from the experiential problem that
  AI-assisted work can feel generic or stale, places leverage in judgment over
  what enters the model, and describes the discrimination layer as a
  pre-generation responsibility (`.../V13_RECOVERY_AND_INTENT_MEMO.md:15-18`).
  It records the practical promise as differentiated work from deliberately
  shaped evidence and context, while expressly marking that promise
  unvalidated (`.../V13_RECOVERY_AND_INTENT_MEMO.md:24-28`).
- The current essay opens with polished answers that feel “strangely familiar,”
  then identifies default search, familiar sources, missing comparison,
  expected gaps, and absent memory before introducing the framework
  (`manuscript/PATTERN_RECOGNITION_V16.md:5-21`). It then explicitly ties the
  proposition to the coffee conversation and to decisions before generation
  (`manuscript/PATTERN_RECOGNITION_V16.md:23-44`).
- The short version preserves the same broad sequence—upstream weakness,
  inspectable choices, human boundaries, and proportionality—without making
  origin accounting the definition (`manuscript/NINETY_SECOND_VERSION.md:3-15,28-33`).
- The essay retains practical ambition but uses proposal language: it calls
  the work a “useful working discipline” that needs comparison with simpler
  methods, and closes by describing the ambition as raising the floor without
  automating expert judgment (`manuscript/PATTERN_RECOGNITION_V16.md:272-280,339-361`).

**Model judgment (not evidence):** The snapshot is faithful to the original
reader problem and differentiated-work ambition. It corrects v13’s broadest
claims about model distributions and expert-grade output without weakening the
reason to build the framework. This matches the fidelity matrix’s reader,
pre-generation, decomposable-expertise, and differentiation requirements
(`docs/V13_TO_V16_FIDELITY_MATRIX.md:14-15,22-24,30-43`).

**Severity:** Pass; no corrective change required.

**Governing requirement:** Owner intent, “Why v16 exists,” “Human judgment
boundary,” and “Provisional editorial center” (`docs/OWNER_INTENT_V16.md:15-29,109-136`);
thesis/audience contract, plain-language 90-second and evidence-boundary
clauses (`docs/THESIS_AND_AUDIENCE_CONTRACT_V16.md:3-16,32-65`).

**Recommended bounded change:** None. Preserve the current human-first opening
and its careful distinction between an ambitious proposition and an unrun test.

### V13-02 — Informational / PASS — All six families remain visible, distinct, and operational

**Class:** Six-family continuity and family-drift check; no defect found.

**Evidence:**

- The recovered v13 memo names the six historical families and their roles:
  peripheral signal mining, source weighing, velocity/motion, absence + memory,
  structured patterns, and the learning loop (`.../V13_RECOVERY_AND_INTENT_MEMO.md:30-41`).
  The rendered historical legend independently lists the same six families and
  descriptions (`.../live-v13-rendered-dom-snapshot.html:1401-1450`).
- The current essay gives each family its own reader-facing section and
  operational boundary: peripheral candidate inspection
  (`manuscript/PATTERN_RECOGNITION_V16.md:46-85`), source/claim distinctions
  (`:87-109`), baseline-dependent motion (`:111-121`), expected absence and
  versioned memory (`:123-159`), explicit comparison (`:161-177`), and
  outcome-based learning with bounded updates (`:179-199`).
- The current short version names all six in one plain-language sentence
  (`manuscript/NINETY_SECOND_VERSION.md:17-21`). The stable builder map gives
  each family a reader question, output, and non-negotiable boundary
  (`framework/SIX_FAMILIES.md:18-32`), with full observable procedures and
  implementation levels for F1–F6 (`framework/SIX_FAMILIES.md:34-338`).
- The machine-readable map also contains exactly six public families, F1–F6,
  with aligned purposes, actions, outputs, boundaries, implementation levels,
  and “when not to use” guidance (`framework/SIX_FAMILIES.json:8-128`).
- The domain-neutral cases and Signal Foundry translation each route through
  all six families rather than collapsing the map into provenance
  (`cases/general-research/README.md:42-51`,
  `cases/product-and-process/README.md:41-50`,
  `cases/signal-foundry/README.md:82-91`).

**Model judgment (not evidence):** No historical family has drifted into a
mere label or disappeared beneath v14/v15 mechanisms. Absence and memory remain
paired as the locked family; motion remains separate; structured comparison and
learning remain visible; and supporting mechanisms are explicitly subordinate
to the public family map.

**Severity:** Pass; no family-restoration change required.

**Governing requirement:** Owner intent six-family lock
(`docs/OWNER_INTENT_V16.md:51-87`), fidelity matrix family rows
(`docs/V13_TO_V16_FIDELITY_MATRIX.md:16-21`), and acceptance gate A03.

**Recommended bounded change:** None. Preserve the current six-family names,
reader questions, and boundaries if later prose or site work is integrated.

### V13-03 — Informational / PASS — Research rigor constrains claims; origin accounting does not displace the thesis

**Class:** Echo/origin separation and research-containment check; no displacement
found.

**Evidence:**

- The historical v13 opening is broad but contains an origin-independent
  reader problem and six-family map before its cards
  (`.../live-v13-rendered-dom-snapshot.html:851-885`). The historical source
  does include origin-adjacent convergence language, but the six-family legend
  gives equal named roles to motion, absence/memory, structured patterns, and
  learning (`.../live-v13-rendered-dom-snapshot.html:1401-1450`).
- The current essay keeps the generic upstream-choice thesis at the opening
  (`manuscript/PATTERN_RECOGNITION_V16.md:5-44`) and places the nine-reports,
  one-announcement scenario only after all six families
  (`manuscript/PATTERN_RECOGNITION_V16.md:201-229`). It calls the example
  subordinate, identifies The Echo Problem as a separate unrun track, and
  states that removing it leaves the broad thesis, other families, learning
  loop, and human boundary intact (`:224-229`).
- The short version says repeated reports are not automatically independent,
  but then explicitly says the proposal is broader than origin counting
  (`manuscript/NINETY_SECOND_VERSION.md:23-33`).
- The current builder topology identifies common-origin analysis as one
  structured-pattern mechanism and includes an explicit removal test
  (`framework/SIX_FAMILIES.md:230-243`,
  `framework/RELATIONSHIP_MAP.md:113-118`). The agent companion likewise says
  the common-origin example can be removed while the six-family procedure
  remains coherent (`framework/agent-playbook/ORDINARY_VS_DISCRIMINATION_LAYER.md:109-114`).
- Research boundaries are explicit: the essay calls the project a framework
  and set of testable questions, says no study has run, and rejects protocol,
  fixture, or planning-simulation language as empirical result
  (`manuscript/PATTERN_RECOGNITION_V16.md:315-337`). Cases carry fixture and
  non-validation status (`cases/README.md:1-17`,
  `cases/signal-foundry/README.md:1-15,121-122`).

**Model judgment (not evidence):** The snapshot has absorbed rigor as a claim
boundary and operating safeguard rather than allowing it to redefine the
project as a provenance system. Origin vocabulary is intentionally frequent in
the source-weighing, structured-pattern, and disconfirmation procedures, but
the reader-facing order, six-family map, and removal tests keep origin
accounting subordinate. This satisfies the fidelity matrix’s explicit v15.2
drift guard (`docs/V13_TO_V16_FIDELITY_MATRIX.md:45-55`).

**Severity:** Pass; no Echo-subordination change required.

**Governing requirement:** Owner intent permanent separation and non-goals
(`docs/OWNER_INTENT_V16.md:165-190`), artifact firebreaks, and acceptance gates
A01, A10, A11, A15, and A16 (`docs/ARTIFACT_BOUNDARIES.md:1-55`,
`docs/V16_ACCEPTANCE_CRITERIA.md:3-22`).

**Recommended bounded change:** None for the reviewed manuscript/framework/case
set. Preserve the removal test whenever the Echo example is linked or adapted.

### V13-04 — Informational / PASS — Human voice and operational translation remain aligned

**Class:** Mentor-reader continuity, human-judgment boundary, and
builder/agent translation; no material misalignment found.

**Evidence:**

- The mentor note starts from the original coffee conversation, states the
  broad upstream-choice center, preserves the six families as ways of seeing,
  places the common-origin case later, and asks the mentor to challenge the
  center, map, terminology, and voice (`manuscript/MENTOR_COVER_NOTE.md:3-31`).
- The essay itself returns to the conversation at the opening and closes with
  an invitation to challenge the route rather than adopt a complete system
  (`manuscript/PATTERN_RECOGNITION_V16.md:23-44,339-361`). It also explicitly
  says when the layer should nearly disappear for simple or reversible tasks
  (`:258-270`).
- The framework turns the six-family idea into stack-neutral decisions,
  records, failure modes, costs, stop rules, and “when not to use” guidance
  (`framework/IMPLEMENTATION_CHOICES.md:1-13,15-34,73-112`,
  `framework/BOUNDARIES_AND_FAILURES.md:1-28,30-70,104-135`).
- The agent companion is observable rather than inspirational: it defines
  default and peripheral routes, acquisition receipts, claim-level weighing,
  comparison, motion/absence/memory, disconfirmation, routing/stopping,
  influence receipts, and outcome learning
  (`framework/agent-playbook/COPYABLE_AGENT_BRIEF.md:43-120`; see also the full
  guide’s decision, permission, cost, acquisition, and outcome sections at
  `framework/agent-playbook/FULL_OPERATING_GUIDE.md:24-73,75-112,114-186,208-286`).
- Cases preserve the intended operational boundary: they use invented or
  illustrative records, name human authority, keep permission separate from
  access, and do not claim runtime effectiveness
  (`cases/general-research/README.md:1-9,11-28,63-89`,
  `cases/product-and-process/README.md:1-8,62-89`,
  `cases/signal-foundry/README.md:43-68,124-147,159-179`).

**Model judgment (not evidence):** The human essay is appropriately less
procedural than the builder and agent artifacts, while the latter preserve the
essay’s central distinctions instead of introducing a competing thesis. The
current wording is direct enough to continue the mentor conversation and the
operational records are detailed enough to make behavior inspectable. The
framework’s formality is an artifact-boundary choice, not evidence that the
human thought piece has become a protocol.

**Severity:** Pass; no voice or translation blocker found.

**Governing requirement:** Owner intent north star, primary reader, builder and
agent requirements, and voice/reading experience (`docs/OWNER_INTENT_V16.md:15-29,31-50,89-108,141-164`);
thesis/audience human-voice and progressive-disclosure contract
(`docs/THESIS_AND_AUDIENCE_CONTRACT_V16.md:77-117`).

**Recommended bounded change:** None required for this snapshot. Keep future
technical additions behind the current essay/framework/agent firebreaks and
retain the “ordinary path” and “when not to use” escape hatches.

### V13-05 — Low — The implementation spectrum is preserved by level, but v13 path continuity is implicit

**Class:** Continuity opportunity; not an owner-intent violation, not an
architecture requirement, and not a research or evidence defect.

**Evidence:**

- The recovered v13 reference inventory explicitly records three implementation
  paths—“process layer,” “reasoning layer,” and “custom model”
  (`.../LIVE_SITE_REFERENCE_MANIFEST.json:36-41`). The recovery memo describes
  the same three paths, calls the process path the baseline, and says the paths
  can compound (`.../V13_RECOVERY_AND_INTENT_MEMO.md:43-49`).
- The current essay deliberately compresses implementation into lightweight,
  moderate, and advanced choices: a decision brief, a compact evidence packet,
  and software for consequential/repeated work
  (`manuscript/PATTERN_RECOGNITION_V16.md:231-265`).
- The current builder guide offers a useful three-level spectrum and explicitly
  rejects a mandatory stack, provider, model, graph, database, or service
  (`framework/IMPLEMENTATION_CHOICES.md:1-13`). Its advanced route describes
  structured data, policies, lineage, routing, review, and evaluation, but does
  not name the optional model-adaptation path
  (`framework/IMPLEMENTATION_CHOICES.md:54-71`).
- The fidelity matrix requires lightweight, moderate, and advanced choices
  without hierarchy, while also recording the historical process,
  intermediary-workflow, and custom-model paths as the continuity context
  (`docs/V13_TO_V16_FIDELITY_MATRIX.md:22-24`). The same matrix explicitly
  rejects the historical claim that a custom model is inherently “deepest” or
  “most defensible” (`:28-43`).

**Model judgment (not evidence):** The owner requirement is met at the level of
implementation choices: the current spectrum is stack-neutral, bounded, and
includes a genuine lightweight route. However, a builder reading only the
current framework may not immediately recognize that the v13 practical
ambition can compound from team process to an intermediary context/evidence
workflow and, only where justified, to model adaptation. This is a small
continuity legibility gap, not drift toward a different thesis.

**Severity:** Low; non-blocking follow-up.

**Governing requirement:** Fidelity matrix implementation-spectrum row and
intentional-departure guard (`docs/V13_TO_V16_FIDELITY_MATRIX.md:22-24,30-43`),
owner intent builder handoff and non-mandatory-architecture boundary
(`docs/OWNER_INTENT_V16.md:76-87`), and acceptance gate A07.

**Recommended bounded change:** In a future owner-reviewed revision, add one
sentence to `framework/IMPLEMENTATION_CHOICES.md` (or its reader-facing
introduction) making the mapping explicit: the lightweight/moderate/advanced
levels may be realized as team process, an intermediary reasoning/context or
evidence workflow, or—only with approved data, budget, governance, and
evaluation—as model adaptation. State in the same sentence that no path is
inherently deeper, more defensible, or required. Do not add a custom-model
requirement, resurrect the v13 hierarchy, or move this implementation detail
into the 90-second opening.

## Gate-oriented summary

This continuity audit supports the following lane conclusions for snapshot
`223d190`:

- **A01 / broad 60–90-second understanding:** Pass. The short version begins
  with upstream genericness and makes the proposal broader than origin
  counting (`manuscript/NINETY_SECOND_VERSION.md:3-33`).
- **A03 / six families:** Pass. All six are named in the short version, essay,
  Markdown map, JSON map, agent receipt, and cases
  (`manuscript/NINETY_SECOND_VERSION.md:17-21`,
  `framework/SIX_FAMILIES.md:20-27`,
  `framework/agent-playbook/DECISION_RECEIPT_TEMPLATE.md:48-57`).
- **A04 / conversation-like voice:** Pass for this lane. The mentor note and
  essay contain a coffee-conversation origin, a direct challenge invitation,
  and a closing question rather than an adoption demand
  (`manuscript/MENTOR_COVER_NOTE.md:3-31`,
  `manuscript/PATTERN_RECOGNITION_V16.md:339-361`).
- **A06 / progressive disclosure:** Pass on the reviewed artifacts’ separation.
  The essay states a human-readable core and the framework/playbook carry the
  records and vocabulary (`manuscript/PATTERN_RECOGNITION_V16.md:41-44,231-270`,
  `framework/README.md:3-21`). A full site/print inspection is outside this
  lane.
- **A07 / builder implementation paths:** Pass with the low-severity V13-05
  continuity opportunity. Three bounded levels, costs, stops, and “when not to
  use” guidance are present (`framework/IMPLEMENTATION_CHOICES.md:7-13,73-94`).
- **A08 / observable agent companion:** Pass. The copyable brief and full guide
  require artifacts for acquisition, comparison, disconfirmation, uncertainty,
  escalation, cost, stop, influence, and learning
  (`framework/agent-playbook/COPYABLE_AGENT_BRIEF.md:43-120`,
  `framework/agent-playbook/FULL_OPERATING_GUIDE.md:97-112,114-225,227-286`).
- **A10/A16 / Echo separation and research containment:** Pass for the reviewed
  manuscript/framework/case scope. The example is fictional, subordinate, and
  removable; no fixture or case is presented as validation
  (`manuscript/PATTERN_RECOGNITION_V16.md:201-229,315-337`,
  `framework/RELATIONSHIP_MAP.md:113-118`, `cases/README.md:1-17`).

No additional V13 continuity finding is warranted from this snapshot. The
recommended implementation-path sentence is bounded, owner-reviewable, and
should be treated as a follow-up to V13-05 rather than as permission to alter
the locked thesis or architecture boundary.

# Post-integration methods and evidence red team — Pattern Map v15.2

**Review mode:** read-only post-integration audit
**Worktree:** `/Users/gpt/Documents/Codex/worktrees/discrimination-layer-v15-2-overnight`
**Status:** `AUDIT_ONLY · NO STUDY RUN · NO MODEL/PROVIDER/NETWORK EXPERIMENT`
**Review date:** 2026-08-19
**Files reviewed:**

- `source/THOUGHT_PIECE_V15_2.md`
- `site/app/HomeEssay.tsx`
- `site/app/ReferenceRoutes.tsx`
- `site/app/DeepReceipt.tsx`
- `research/overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md`
- `reports/overnight/v15_2/INTEGRATION_DECISION_LEDGER.md`

No implementation file was edited by this review. No model, provider, network,
deployment, preregistration, external dataset, or empirical output was used.

## Executive decision

**Current release gate: REJECT / P0 OPEN.** The integration is honest about the
high-level truth boundary: the manuscript and site repeatedly say that no model
has been selected, no study has run, and no empirical result exists. The narrow
novelty boundary, stipulated-origin language, T1 firewall, and core
null/harm/shortcut commitment also survive.

The candidate is not yet owner-ready because the public Lab route does not
state the actual primary metric and safety guardrail precisely enough, and it
contains an internally misleading prompt-parity sentence. The integration
ledger explicitly requires Lab to retain the exact open gates (`INTEGRATION_DECISION_LEDGER.md:35,41,68-74`),
while the rendered research route currently exposes only a subset of them. A
reader could therefore understand the status correctly while still
misunderstanding what the future experiment would measure and what remains
open.

The minimum release condition is to close P0-01 through P0-03 below, then
re-run the post-integration methods/evidence review. P1 items should be closed
before a public research handoff; P2 items are maintainability and drift risks
that should be addressed before a durable release.

## What survived the attack

These are positive findings, not empirical validation:

- The manuscript’s front matter and research bridge state “no model selected,”
  “no study run,” and “no empirical result” (`source/THOUGHT_PIECE_V15_2.md:1-8,232-257`).
- The manuscript calls the comparison proposed, says the local harness is not a
  model finding, and explicitly names shortcut, invalid-output, noise, and
  instability explanations (`source/THOUGHT_PIECE_V15_2.md:232-263`).
- The site repeats the no-result status in the default essay, Lab, and detailed
  receipt (`site/app/HomeEssay.tsx:43-50,83,174,252`; `site/app/ReferenceRoutes.tsx:574-584`;
  `site/app/DeepReceipt.tsx:9,18-19,87`).
- Broad mechanism novelty is rejected rather than implied. The manuscript
  describes a boundary-preserving synthesis and a proposed supplied-cue
  comparison, while disavowing provenance discovery, real-world independence,
  truth, human benefit, and whole-framework validation
  (`source/THOUGHT_PIECE_V15_2.md:193-206`; `site/app/HomeEssay.tsx:229-234`).
- The amendment draft is explicitly non-authorizing, keeps v1.0 canonical until
  owner acceptance, preserves F0/F1/F2, and defers D-S/EvidentialRAG
  (`research/overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md:3-27,123-141,639-658`).
- The detailed receipt consistently marks the nine-report example as fictional,
  supplied, non-live, non-runtime, and not a model result
  (`site/app/DeepReceipt.tsx:9-19,80-87`).
- The site keeps T1 descriptive and outside the main comparison, and states that
  rights and annotation gates must pass before data use
  (`site/app/ReferenceRoutes.tsx:634-639`).

These strengths do not close the methods gates below; they establish that the
problems are correctable integration gaps rather than fabricated results.

## P0 findings — block owner-ready release

### P0-01 — The Lab collapses `FC_cons` into “invalid answers” and hides VOR

**Anchors:**

- `site/app/ReferenceRoutes.tsx:607-614` displays `N=300` and split counts but
  does not display the fixed `M=75` safety subset.
- `site/app/ReferenceRoutes.tsx:616-631` describes the “main measure” only as
  counting invalid answers as failures. It does not state that a valid emitted
  count of at least two on `none`, `single`, or `unknown` rows is also a
  conservative risk event, nor does it state the VOR threshold.
- `site/app/ReferenceRoutes.tsx:589-602` says the supplied-cue version should
  “beat” the rule-only version without naming the primary risk event or the
  fixed safety gate.
- The amendment explicitly defines the two formulas and their limits
  (`research/overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md:192-234,248-319`).
- The integration ledger requires the interpretation revision, provisional
  denominators, and exact open Lab gates (`reports/overnight/v15_2/INTEGRATION_DECISION_LEDGER.md:38-42,68-74`).

**Attack.** A reader can leave the Lab believing that the primary endpoint is
mostly or only parseability. That masks the central construct problem: a
condition can lower `FC_cons` through invalid-rate differences, valid asserted
count behavior, or both. Conversely, VOR is presented only as an unspecified
“safety check,” so the reader cannot see that it is a fixed-75 threshold guard
against blanket suppression, not exact origin accounting. This creates both a
metric-interpretation failure and an evidence-status failure: the amendment’s
P0-01/P0-02/P0-06 gates are not recoverable from the route that claims to hold
the exact open gates.

**Minimum corrective edit.** Add a short plain-language metric block to Lab:

1. `FC_cons` is the all-assigned conservative asserted-count-risk event:
   invalid output is risky, and a valid count `>=2` is risky on bundles whose
   stipulated supporting-origin certainty is `none`, `single`, or `unknown`.
2. The primary denominator is all 300 assigned bundles; invalid outputs remain
   in it. Invalid-rate and valid-only asserted-count components are reported
   separately before any semantic-cue wording is allowed.
3. VOR is evaluated on fixed `M=75` multiple-certainty bundles; it requires a
   valid output, count `>=2`, and at least two selected support-side stipulated
   origins. It is a threshold guardrail, not exact counting or assignment.
4. The final interval and paired-invalid-dependence operating-characteristic
   receipt remain **open**, not passed.

**Accept/reject gate.** **REJECT until fixed.** Accept only when the Lab text,
the amendment, and the integration ledger use the same endpoint names and
limits, and a static text check confirms that `FC_cons`, `VOR`, `M=75`,
invalidity decomposition, and open interval status are all present.

### P0-02 — The prompt-parity sentence is internally contradictory

**Anchors:**

- `site/app/ReferenceRoutes.tsx:623-625` says the two primary versions must
  have “exactly the same evidence and prompt bytes” while “only the supplied
  relationship field may differ.”
- The amendment requires equal selected-tokenizer counts and equal byte
  lengths, but records distinct prompt payload hashes and treats the relation
  cue as the intentional treatment difference
  (`research/overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md:395-433`).
- The manuscript correctly describes the comparison as a visible-field effect
  that may also reflect formatting, position, invalidity, or shortcuts
  (`source/THOUGHT_PIECE_V15_2.md:246-257`).

**Attack.** Literal “same prompt bytes” is impossible if F1 has `NONE` relation
slots and F2 has `DPND`/`INDP`/`UNKN` values. It also conflicts with the
amendment’s required per-condition hashes. A reviewer could read the sentence
as claiming byte-identical treatment prompts, or as treating relation content
as a non-treatment formatting detail. Either reading undermines the stated
causal contrast and the fail-closed parity gate.

**Minimum corrective edit.** Replace the sentence with language equivalent to:

> F1 and F2 must contain byte-identical report text, report order, metadata
> shape, rule instruction, output cap, retrieval/tool budget, and matched
> resource receipts. The relation-field values are the intentional visible
> input difference. Final prompt bytes and hashes may differ; input byte
> lengths and selected-tokenizer input counts must match exactly.

Keep “the current tokenizer is a development stand-in” and the no-run status.

**Accept/reject gate.** **REJECT until fixed.** Accept only when this wording
matches the v1.0/amendment parity receipt and the site no longer says that the
final prompt bytes are identical.

### P0-03 — The Lab does not enumerate the open P0 gate set it claims to carry

**Anchors:**

- The integration ledger says exact F0/F1/F2, tokenizer, interval, denominator,
  leakage, safety, and T1 mechanics live in Lab, and that listed controls are
  not passed until receipts exist (`reports/overnight/v15_2/INTEGRATION_DECISION_LEDGER.md:35,41,68-74`).
- The amendment enumerates P0-01 through P0-06 as open and separately requires
  owner phase authorization (`research/overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md:364-384`).
- The current Lab route states no model/no run and mentions parity, shortcut
  controls, semantic audit, and T1, but does not expose the final interval,
  paired invalid dependence, coherence, claim-language, or explicit owner-
  authorization gates (`site/app/ReferenceRoutes.tsx:574-638,653-666`).

**Attack.** The public route can be read as “the safeguards are listed and the
study is waiting for a model,” rather than “six material gates are open and
the current scaffold cannot authorize even a pilot.” In particular, the
sentence that controls “must pass” does not identify which receipts are absent,
and the route has no visible `COHERENT_PROTOCOL_NOT_EXECUTION_READY` or
`P0 GATES OPEN` status. That weakens the no-authorization boundary and makes
the release gate impossible for a cold reader to audit.

**Minimum corrective edit.** Add a compact, nontechnical “Open gates — none
passed yet” panel in Lab with these rows: `FC_cons` decomposition;
interval/paired-invalid operating characteristics; selected-model
tokenizer/chat-template parity; leakage/semantic audit; claim/status lint;
count/stance/evidence coherence; and separate owner phase authorization. State
that a listed control is not a passed control, and that the current route is
`COHERENT_PROTOCOL_NOT_EXECUTION_READY`.

**Accept/reject gate.** **REJECT until fixed.** Accept only when each P0 row is
explicitly marked open or linked to a receipt, with no “ready,” “frozen,”
“passed,” or “authorized” implication before owner acceptance.

## P1 findings — required before public research handoff

### P1-01 — “One Frozen Model” reads as though model selection already occurred

**Anchors:**

- `site/app/ReferenceRoutes.tsx:577-589` says “No model selected” and then
  presents the scientific title “Supplied Origin-Relation Cues in One Frozen
  Model” and “compare the same model and evidence.”
- The manuscript says no model is selected (`source/THOUGHT_PIECE_V15_2.md:232-236`),
  and the amendment says the selected model/tokenizer remain unknown
  (`research/overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md:388-393`).

**Attack.** The surrounding status prevents this from being an empirical-result
claim, but the title can still be read as a frozen-model receipt rather than a
candidate study title. That is especially risky beside `N=300` and the phrase
“the same model.”

**Minimum corrective edit.** Label it “Proposed study title — model not yet
selected” or use “One Model to Be Selected” until the owner freezes the exact
checkpoint/tokenizer. Keep “one frozen model” only as a future protocol
qualifier after the parity receipt exists.

**Accept/reject gate.** **CONDITIONAL ACCEPT after wording fix.** No model
selection or parity receipt may be implied by the title.

### P1-02 — The worked example contains an unqualified “authorize” action

**Anchors:**

- `site/app/ReferenceRoutes.tsx:472-499` labels the section “Illustrative
  example,” but ends with: “authorize only the bounded synthetic-data rollback
  check.”
- The integration ledger calls the Signal Foundry case a bounded translation,
  pending final copy, and says the proposed event must remain labeled a
  proposal (`reports/overnight/v15_2/INTEGRATION_DECISION_LEDGER.md:46`).
- The amendment requires separate owner phase authorization and states that a
  gate receipt is not authorization (`research/overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md:381-384`).

**Attack.** In context this is an illustrative human disposition, not an actual
  run. However, “authorize only” can be copied or read as a current permission
  to conduct a synthetic rollback check. It is the clearest accidental
  authorization verb in the inspected integration.

**Minimum corrective edit.** Change the sentence to “the illustrative route
  would propose a bounded synthetic-data rollback check, subject to separate
  owner authorization; it authorizes nothing now.” Add the same boundary to the
  expanded receipt if the case remains in the public route.

**Accept/reject gate.** **CONDITIONAL ACCEPT after wording fix.** The example
  may remain, but no current action, budget, data access, or run permission may
  be inferred from it.

### P1-03 — The public negative-result commitment is narrower than the locked contract

**Anchors:**

- `site/app/ReferenceRoutes.tsx:641-650` preserves null, rule-only tie, harmful,
  and shortcut/unstable outcomes.
- `site/app/HomeEssay.tsx:259-263` adds invalid-answer-only, noise, and
  instability language, and `source/THOUGHT_PIECE_V15_2.md:259-263` repeats it.
- The amendment’s locked result table also names invalidity-driven,
  threshold-only VOR, noise-fragile, surface/semantic-audit failure, T1
  non-transport, and stopped/quarantined outcomes
  (`research/overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md:660-681`).

**Attack.** The core commitment survives, so this is not a claim that the site
  is positive-only. The drift is that the public route collapses distinct
  failure classes into “shortcut or unstable” and does not expose the special
  interpretation rule for an invalidity-driven composite delta or a VOR pass
  that is only threshold behavior. A future favorable `FC_cons` result could
  therefore be narrated as cue value while the public promise technically
  mentions only “invalid answers.”

**Minimum corrective edit.** Add concise bullets or a linkable Lab disclosure
  for: invalidity-driven composite improvement; threshold-only VOR; direct-code
  or field-only behavior; noise-fragile behavior; semantic/stance audit
  failure; and stopped/quarantined runs. Keep null and harmful outcomes as
  first-class language, and do not merge direct-code with general instability.

**Accept/reject gate.** **CONDITIONAL ACCEPT after wording/link fix.** The
  complete locked table need not be in the essay, but Lab must expose the full
  interpretation ladder before any run.

### P1-04 — The Lab names supplied labels but not their critical semantics

**Anchors:**

- `site/app/ReferenceRoutes.tsx:595-602` calls F2 labels “the benchmark’s
  supplied relationship labels” without stating that `INDP` is
  independent-as-stipulated and `UNKN` is unresolved rather than independent.
- The essay explains ordinary shared/separate-in-this-test/unresolved states
  (`site/app/HomeEssay.tsx:115-121`), and the glossary provides the code boundary,
  but the Lab’s condition table is where a reader is asked to understand the
  experiment.
- The amendment makes the code semantics and unknown-origin conservative rule
  explicit (`research/overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md:50-55,147-190,346-357`).

**Attack.** A reader can interpret “relationship labels” as discovered
  provenance or treat an absent relation as a non-event. That would undermine
  both the oracle-cue boundary and the reason unknown-origin rows are
  conservatively risk-coded.

**Minimum corrective edit.** Add one sentence below the condition table:
  “F2 shows supplied `DPND`/`INDP`/`UNKN` values: dependent path,
  separate-origin-as-stipulated, and unresolved; `UNKN` is never silently
  counted as independent.” Link to the full amendment for technical details.

**Accept/reject gate.** **CONDITIONAL ACCEPT after wording fix.** The Lab need
  not reproduce the full schema, but it must not leave the treatment labels
  semantically unbounded.

## P2 findings — maintainability and drift risks

### P2-01 — ORIGIN-EX-01 is duplicated across three route implementations

**Anchors:**

- `site/app/HomeEssay.tsx:123-135` contains a compact five-field ORIGIN-EX-01
  record.
- `site/app/ReferenceRoutes.tsx:145-218` contains another home-mode receipt,
  version `0.2`, with the nine-row ledger and B1/C1 contrast roots.
- `site/app/DeepReceipt.tsx:14-87` contains a third detailed receipt, version
  `0.3`, with the same IDs and a slightly different field vocabulary.
- `site/app/page.tsx:1-16` routes the live home page to `HomeEssay`, while the
  `isHome` branch in `ReferenceRoutes.tsx:56-219,722-724` remains another copy.

**Attack.** The current values are broadly aligned and all copies are clearly
  illustrative, so this is not an evidence-status failure today. But duplicate
  receipt data, two versions without a visible changelog, and an unreachable
  home branch create a predictable future drift path: one route could acquire
  a changed count, relation label, or disposition while another remains the
  apparent canonical example.

**Minimum corrective edit.** Make ORIGIN-EX-01 a single typed content object
  (or delete the unreachable ReferenceRoutes home branch), document whether
  `0.2` and `0.3` are intentional presentation versions, and add a static
  consistency check for `09 / 01 / 00 / HOLD`, B1/C1, relation labels, and
  fictional/no-result status.

**Accept/reject gate.** **ACCEPT WITH P2 FOLLOW-UP.** This does not block the
  methods gate if the current copies remain aligned, but it should be resolved
  before durable publication or further route edits.

## Overall acceptance test and minimum corrective set

The integrated candidate should be marked **owner-ready only after**:

1. Lab states `FC_cons`, its valid asserted-count branch, all-assigned `A=300`,
   fixed `M=75`, VOR’s threshold interpretation, and the open interval/
   paired-invalidity status (P0-01).
2. The parity sentence distinguishes equal evidence/resource bytes and lengths
   from the intentional relation-field content difference (P0-02).
3. Lab exposes all P0 gates as open or receipt-backed and explicitly says that
   no listed gate, scaffold, or gate receipt authorizes a run (P0-03).
4. The planned title is not read as an already selected model (P1-01), and the
   illustrative “authorize” verb is made future/conditional (P1-02).
5. The public commitment links or states invalidity-driven, threshold-only,
   direct-code, noise-fragile, semantic-audit, and stopped-run dispositions
   without weakening the null/harm promise (P1-03).
6. The Lab defines `DPND`, `INDP`, and `UNKN` in ordinary language (P1-04).
7. Receipt duplication is tracked or consolidated before the next durable
   site revision (P2-01).

**Final disposition:** `REJECT_OWNER_READY_PENDING_P0_CORRECTIONS`.

This report finds no empirical result, no provider action, no authorization,
and no broad novelty claim in the current integration. Its rejection is a
release-quality decision about methods/evidence clarity, not a finding about
the proposed study’s eventual outcome.

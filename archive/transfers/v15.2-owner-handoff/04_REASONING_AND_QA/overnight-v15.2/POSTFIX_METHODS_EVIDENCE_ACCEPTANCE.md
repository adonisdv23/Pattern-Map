# Post-fix methods/evidence acceptance — Pattern Map v15.2

**Review mode:** read-only post-fix acceptance review  
**Worktree:** `/Users/gpt/Documents/Codex/worktrees/discrimination-layer-v15-2-overnight`  
**Review date:** 2026-08-19  
**Disposition (final post-correction):** **PASS WITH EXPLICIT RESIDUALS — P0/P1 closure verified; one non-blocking P2 remains.**

**First-pass audit trail:** The original `FAIL` review dated 2026-08-19 is
preserved below, including its original findings and final disposition. The
dated post-correction re-review appended at the end supersedes the top-level
disposition only; it does not rewrite the first-pass record.

## First-pass audit trail — 2026-08-19

This review read the complete post-integration methods red-team report, the
complete non-authorizing v1.1 amendment draft, `ReferenceRoutes.tsx`, the
rendered-route test, `THOUGHT_PIECE_V15_2.md`, and the canonical v1.0 protocol
plus the relevant v15.2 methods/decision records. No implementation or
research source was edited. The only file created by this review is this
report.

The failure is a release-quality finding about the public methods receipt, not
an empirical finding. No model, provider, network, pilot, primary run, or
result was used or authorized.

## Canonical-status boundary

The canonical authority remains `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md`
v1.0. It calls itself the canonical pre-run protocol, says that the primary
run is not authorized or opened, and records no selected model, tokenizer,
pilot/primary output, preregistration, or result
(`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:1-12`). It also expressly
does not authorize a model, provider, spending, preregistration, release, or
opening of the primary split (`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:28-30`).

`research/overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md`
is a proposed, non-authorizing amendment, not a replacement for v1.0. Its
status table preserves F0/F1/F2 and says that owner acceptance is required;
its notice says that v1.0 remains the source of truth until a versioned
amendment is explicitly accepted (`research/overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md:1-27`).
The draft therefore supplies the interpretation and future evidence contract,
but it does not close a gate or authorize a run. The Lab itself links the
canonical protocol and labels the amendment as a non-authorizing draft
(`site/app/ReferenceRoutes.tsx:443`).

## Acceptance matrix for the requested corrections

| Requirement | Disposition | Evidence and boundary |
| --- | --- | --- |
| Exact `FC_cons` definition and decomposition | **PASS, subject to the P0 VOR residual below** | The canonical formula is `FC_obs = valid ∧ count >= 2 ∧ certainty ∈ {none,single,unknown}` and `FC_cons = ¬valid ∨ FC_obs` (`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:300-320`). The v1.1 draft preserves the formula, names the event **conservative asserted-count risk**, and requires invalid-by-reason, valid-only, all-assigned, two-by-two, and narrative decomposition receipts (`research/overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md:192-234,264-290`). Lab prose says all `A=300` rows remain in the denominator, invalid output is risky, valid `>=2` on `none`/`single`/`unresolved` rows is risky, and invalidity versus valid-answer counting must be reported separately (`site/app/ReferenceRoutes.tsx:374-380`). It does not call this semantic understanding or claim-truth evidence. |
| `A=300` denominator | **PASS** | Lab says `FC_cons` keeps all `A=300` assigned bundles in the denominator and the sample-size note marks 300 as planned/provisional, not a result (`site/app/ReferenceRoutes.tsx:365,378-379`). The canonical all-assigned requirement is explicit (`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:381-396`); the draft retains `A=300` as a design input with operating adequacy open (`research/overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md:120-141`). |
| Fixed `M=75` VOR definition, margin, and membership freeze | **FAIL — P0-01 residual** | Lab states a fixed `M=75` multiple-certainty subset and correctly describes VOR as a threshold guardrail requiring a valid output, count `>=2`, and selected support from at least two supplied origins (`site/app/ReferenceRoutes.tsx:376-380`). But it does **not** state the locked one-sided lower-bound margin (`F2−F1 VOR lower bound > -0.05`), that membership comes from the pre-run restricted manifest, that the ordered membership/hash is frozen, or that `M` must not be intersected with valid outputs. Those requirements are canonical (`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:322-335,398-404`) and are retained by the draft (`research/overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md:192-234,528-544`). The Lab says interval work and paired invalid dependence remain open (`site/app/ReferenceRoutes.tsx:393-405`), but the missing margin and membership-freeze language leaves the safety gate underspecified on the public route. |
| F1/F2 parity language | **PASS** | The corrected Lab sentence explicitly separates byte-identical report text/order/metadata/rule/resource material from the intentional relation-field difference, then says final prompt bytes and hashes may differ while input byte lengths and selected-tokenizer input counts must match (`site/app/ReferenceRoutes.tsx:382-385`). This matches the canonical parity receipt, which requires equal report hashes/order, byte lengths, and intended-tokenizer counts while allowing F2 relation values to differ (`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:229-248`), and the v1.1 receipt requirements (`research/overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md:395-433`). The route also labels the current tokenizer development-only (`site/app/ReferenceRoutes.tsx:384`). |
| Every open gate and non-authorization boundary | **PASS** | The Lab visibly marks `COHERENT_PROTOCOL_NOT_EXECUTION_READY · all material gates open`, says a listed safeguard is not a passed safeguard, requires a dated receipt plus a separate owner decision, and enumerates FC decomposition, operating characteristics/paired invalidity, selected-model parity, leakage/meaning, claim/status lint, count/stance/evidence coherence, and owner phase authorization (`site/app/ReferenceRoutes.tsx:393-405`). The amendment carries six P0 gates as `OPEN` and separately states that a gate receipt is not authorization (`research/overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md:364-384`). The no-result and no-authorization wording is consistent with the v1.0 owner checklist (`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:474-512,597-612`). |
| Selected-model wording | **PASS** | The Lab labels the title “Proposed study title · model not yet selected” and names the future study “One Model to Be Selected” (`site/app/ReferenceRoutes.tsx:331-347`). The canonical protocol and amendment both keep model/checkpoint/tokenizer selection as future owner-gated work (`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:7-10,252-269`; `research/overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md:388-417`). No selection or parity receipt is implied. |
| `DPND` / `INDP` / `UNKN` semantics | **PASS** | The condition table defines `DPND` as shared/dependent path, `INDP` as a separate origin only as stipulated by the fictional test, and `UNKN` as unresolved; it explicitly says `UNKN` is never silently counted as independent (`site/app/ReferenceRoutes.tsx:351-363`). The detailed receipt repeats the plain-state/code boundary (`site/app/DeepReceipt.tsx:64-71`), and the canonical legend has the same semantics (`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:205-212`). |
| Comprehensive locked unfavorable-result interpretations | **FAIL — P1-03 residual** | Lab preserves null, rule-only tie, invalidity-driven, threshold-only, harmful, direct-code/field/coherence shortcut, relation-noise fragility, non-transfer, and stopped/quarantined language (`site/app/ReferenceRoutes.tsx:415-427`). However, the full locked contract also requires an explicit **unstable** class and an explicit **surface/semantic-audit failure** class, with their dispositions; the Lab currently folds these into “Shortcut or semantic failure” and “Fragile or non-transferable” without naming the result classes. The manuscript mentions instability but does not replace the Lab disclosure (`source/THOUGHT_PIECE_V15_2.md:265-269`); the complete amendment table names `Unstable`, `Surface/semantic audit failure`, `T1 non-transport`, `Noise-fragile`, `Shortcut/direct-code`, `Invalidity-driven`, `Threshold-only VOR`, and `Stopped/quarantined` separately (`research/overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md:660-681`). |
| No empirical-result implication | **PASS** | The manuscript says “proposed comparison, not a result,” no model selected, no study run, and local machinery is not a model finding (`source/THOUGHT_PIECE_V15_2.md:235-263`). The Lab says no model is chosen, the test is not run, the title is proposed, and the route is not execution-ready (`site/app/ReferenceRoutes.tsx:331-347,393-405`). The home essay repeats no model/no run/no result and says the research bridge is a proposed comparison (`site/app/HomeEssay.tsx:43-50,255-269`). The v1.1 draft explicitly separates design values from observed results and says no model/output/pilot/result exists (`research/overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md:106-121`). |

## Remaining findings

### P0 — still blocks owner-ready release

#### P0-01 — Public VOR safety receipt is incomplete

The primary `FC_cons` language and its all-assigned decomposition are now
aligned with the canonical formula and the proposed v1.1 interpretation. The
remaining blocker is the safety half of the same methods block: a reader of
Lab can see `M=75` and “threshold guardrail,” but cannot recover the locked
decision margin or the fail-closed membership rule from the route.

The canonical protocol requires fixed `M` membership, an ordered membership
hash in the run receipt, and a one-sided lower bound that must exceed `-0.05`
(`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:322-335,398-404`). The draft
keeps that margin and requires fixed-`M` planning/coverage evidence while
leaving the interval method open (`research/overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md:230-234,528-544`).
The public Lab currently stops at “fixed `M=75` multiple-certainty safety
subset” and “finalize the interval” (`site/app/ReferenceRoutes.tsx:378-379,393-405`).

Required closure: add to the Lab metric block that (a) `M` is the ordered,
pre-run restricted-manifest subset of exactly 75 multiple-certainty bundles,
with membership/hash frozen and never filtered by validity or post-run output;
(b) VOR is the F2-minus-F1 guardrail whose one-sided lower bound must be
greater than the locked `-0.05` margin; and (c) the final interval method,
coverage, and paired-invalid operating-characteristic receipt are still open.
This is a wording/inspectability correction only; it does not authorize a
run or change v1.0.

### P1 — required before public research handoff

#### P1-03 — Locked failure ladder is not fully named on Lab

The route does preserve an unfavorable-result promise and several newly
required classes. It should nevertheless expose the complete interpretation
ladder before a run, rather than require a reader to infer “unstable” from the
manuscript or “semantic-audit failure” from the open-gate list. Add explicit
rows (or a direct, clearly marked link to the full non-authorizing table) for:

- unstable across preregistered seeds/configurations;
- surface/semantic-audit, stance, transformation, or split-leakage failure;
- direct-code/field-only shortcut;
- invalidity-driven composite movement;
- threshold-only VOR;
- noise-fragile oracle behavior;
- T1 non-transport; and
- stopped/quarantined runs.

The existing null, rule-only tie, harmful, and stopped/quarantined language can
remain. The source contract must stay the interpretation authority: the
amendment’s table is comprehensive, but it is a draft and does not itself
authorize a result (`research/overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md:660-681,704-715`).

### P2 — maintainability/regression risks

#### P2-01 — Illustrative receipt remains represented in multiple components

The compact ORIGIN-EX-01 receipt is rendered in the home essay
(`site/app/HomeEssay.tsx:126-139`), while the detailed receipt carries the
same fictional identifiers and disposition in a separate component
(`site/app/DeepReceipt.tsx:14-87`); the Explore worked-example route also
references the receipt and its illustrative disposition
(`site/app/ReferenceRoutes.tsx:228-256`). These are currently aligned and
explicitly fictional, so this is not an evidence-status failure. A single
typed content object or a consistency test would reduce future drift.

#### P2-02 — Rendered tests do not lock the missing safety/ladder strings

The rendered Lab test checks presence of `FC_cons`, `A=300`, `M=75`, `VOR`, the
open-gate status, and non-authorization (`site/tests/rendered-html.test.mjs:98-120`),
but it does not assert the `-0.05` margin, membership/hash freeze, explicit
unstable class, or explicit surface/semantic-audit class. After the P0/P1
wording is closed, add static assertions so a future route edit cannot silently
reintroduce either omission.

## Checks run

All checks were local/offline and are not model or empirical evidence:

- `cd site && npm test` — build succeeded; all 7 rendered-route tests passed.
- `/Users/gpt/Documents/Codex/projects/Signal-Foundry/.venv/bin/python -m pytest -q tests/test_origin_accounting.py` — **15 passed**.

No model/provider/network invocation, external dataset access, deployment,
preregistration, production mutation, or authorization occurred. The local
test passes establish only render/code-path and offline contract behavior; the
canonical protocol explicitly says that the scaffold does not provide model
output, effect, semantic audit clearance, or release authorization
(`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:577-595`).

## Final disposition

**FAIL — `REJECT_OWNER_READY_PENDING_P0_VOR_RECEIPT_AND_P1_RESULT_LADDER`.**

Passed corrections are real: the route now uses conservative asserted-count
risk language, preserves `A=300`, distinguishes F1/F2 bytes/hashes from equal
lengths/token counts, exposes all material gates and no-authorization status,
labels the model as not yet selected, defines `DPND`/`INDP`/`UNKN`, and avoids
empirical-result implication. The release cannot be accepted until the Lab
also exposes the canonical VOR margin/membership freeze and the full locked
unfavorable-result ladder. This review does not authorize any study phase.

## Post-correction re-review — 2026-08-19

**Re-review disposition:** **PASS WITH EXPLICIT RESIDUALS.** The P0-01 VOR
receipt defect and P1-03 unfavorable-result-ladder defect are closed in the
current source route, rendered-test assertions, and standalone `/lab` export.
No execution, model/provider call, empirical output, or authorization was
inferred. No implementation or research source was edited by this re-review;
only this existing acceptance report was updated.

### P0-01 closure — VOR margin and membership freeze

The corrected Lab now states all of the previously missing safety boundaries
in one metric block:

- VOR is evaluated on fixed `M=75` multiple-certainty bundles and remains a
  threshold guardrail, not exact counting or assignment
  (`site/app/ReferenceRoutes.tsx:379`).
- The ordered membership and hash come from the restricted pre-run manifest,
  are frozen before execution, and are never filtered by validity or post-run
  output (`site/app/ReferenceRoutes.tsx:379`).
- The planned F2-minus-F1 one-sided 95% lower bound must be greater than the
  locked `-0.05` margin (`site/app/ReferenceRoutes.tsx:379`).
- The interval method, coverage simulation, and paired-invalid operating-
  characteristic receipt remain explicitly open (`site/app/ReferenceRoutes.tsx:379`).
- The open-gate panel repeats that the safety interval method, fixed `M=75`,
  locked `-0.05` margin, and paired invalid-output dependence still require
  evidence, while all gates remain open and no gate receipt authorizes a run
  (`site/app/ReferenceRoutes.tsx:393-405`).

These statements match the canonical v1.0 membership and safety decision
contract (`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:322-335,398-404`)
and the non-authorizing v1.1 draft’s fixed-`M` planning/coverage requirement
(`research/overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md:230-234,528-544`).
This is a wording/receipt closure, not evidence that the interval, coverage,
or operating-characteristic gate has passed.

### P1-03 closure — comprehensive unfavorable-result ladder

The corrected Lab now names the required locked dispositions separately:

- null and rule-only tie (`site/app/ReferenceRoutes.tsx:420-421`);
- invalidity-driven and threshold-only (`site/app/ReferenceRoutes.tsx:422`);
- harmful (`site/app/ReferenceRoutes.tsx:423`);
- direct-code/field-only shortcut (`site/app/ReferenceRoutes.tsx:424`);
- surface or semantic-audit failure, including stance,
  transformation, split-leakage, and count/claim/evidence-coherence failure
  (`site/app/ReferenceRoutes.tsx:425`);
- unstable across preregistered seeds/configurations
  (`site/app/ReferenceRoutes.tsx:426`);
- noise-fragile or non-transferable behavior
  (`site/app/ReferenceRoutes.tsx:427`), paired with the separate T1
  descriptive-transfer firewall (`site/app/ReferenceRoutes.tsx:408-412`); and
- stopped or quarantined runs (`site/app/ReferenceRoutes.tsx:428`).

The wording now covers the distinct classes in the v1.1 draft’s locked table,
including `Unstable`, `Surface/semantic audit failure`, `T1 non-transport`,
`Noise-fragile`, `Shortcut/direct-code`, `Invalidity-driven`, `Threshold-only
VOR`, and `Stopped/quarantined` (`research/overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md:660-681`).
It remains a pre-run commitment rather than a result.

### Rendered-route and standalone evidence

The Lab-specific rendered-route assertions now lock the closure strings for
the model/no-run status, `FC_cons`, `A=300`, `M=75`, VOR membership/hash,
`-0.05`, open interval status, non-authorization, and the result classes
(`site/tests/rendered-html.test.mjs:98-128`). The standalone Lab export carries
the same corrected server-rendered content in its body (`output/v15_2/standalone/lab.html:892`),
including the membership/hash, margin, open-gate, no-result, and unfavorable-
result strings. A direct standalone assertion found all 10 required strings
present in that export.

The route continues to state no chosen model, no run, and no result
(`site/app/ReferenceRoutes.tsx:331-347`), and the open-gate panel continues to
state `COHERENT_PROTOCOL_NOT_EXECUTION_READY` and that complete gate receipts
authorize nothing by themselves (`site/app/ReferenceRoutes.tsx:393-405`).
The standalone file’s route comment and rendered footer likewise retain the
no-study/no-empirical-results boundary (`output/v15_2/standalone/lab.html:1,892`).

### Checks performed in this re-review

All checks were local/offline and are not model or empirical evidence:

- `node --test tests/rendered-html.test.mjs` — **7 passed** after the updated
  assertions were present.
- Clean rerun of `cd site && npm test` — build succeeded; **7 rendered-route
  tests passed**. One earlier post-correction invocation hit a transient
  `dist/server/index.js` module-not-found during route imports immediately
  after build materialization; the direct rerun and clean `npm test` rerun
  passed without source changes.
- `/Users/gpt/Documents/Codex/projects/Signal-Foundry/.venv/bin/python -m pytest -q tests/test_origin_accounting.py` — **15 passed**.
- Standalone content assertion — **10/10** required VOR/open-gate/result-
  ladder/no-result strings present in `output/v15_2/standalone/lab.html`.

### Remaining findings after correction

**P0:** None identified in the requested P0-01/P0-03 methods/evidence
surface. The VOR margin, membership freeze, open interval status, and
non-authorization boundary are now explicit and regression-asserted.

**P1:** None identified in the requested P1-03 result-interpretation surface.
The full locked unfavorable-result ladder is now explicit in Lab and present
in the standalone export.

**P2-01 — illustrative receipt duplication remains (non-blocking).** The
fictional ORIGIN-EX-01 record still has compact/detail/presentation copies in
`site/app/HomeEssay.tsx:126-139`, `site/app/DeepReceipt.tsx:14-87`, and
`site/app/ReferenceRoutes.tsx:228-256`, with the standalone export as another
generated representation (`output/v15_2/standalone/lab.html:892`). The copies
are currently aligned and explicitly illustrative; consolidation into one
typed content object or a consistency test remains maintainability work, not
a methods/evidence acceptance blocker.

The prior P2 test-coverage gap is closed for the corrected surfaces:
`site/tests/rendered-html.test.mjs:111-128` now asserts the margin,
membership/hash, open interval status, and the newly named failure classes.

## Final post-correction disposition

**PASS WITH EXPLICIT RESIDUALS — `P0/P1_METHODS_EVIDENCE_CLOSURE_VERIFIED; P2-01_RECEIPT_DUPLICATION_NON_BLOCKING`.**

The corrected route, rendered tests, and standalone Lab export now close the
specific P0-01 and P1-03 findings from the first-pass audit. `A=300`, exact
`FC_cons` risk/decomposition language, F1/F2 parity caveats, all open gates,
selected-model wording, `DPND`/`INDP`/`UNKN` semantics, comprehensive
unfavorable-result interpretations, and the no-empirical-result boundary are
all preserved. This acceptance is not a study authorization and does not
convert any open scientific gate into a pass.

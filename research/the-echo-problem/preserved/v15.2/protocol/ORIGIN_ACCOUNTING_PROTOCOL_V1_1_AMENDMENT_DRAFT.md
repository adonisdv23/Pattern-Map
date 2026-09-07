# Origin Accounting Protocol v1.1 Amendment Draft

## Explicit status: NON-AUTHORIZING pre-run draft

| Field | Value |
| --- | --- |
| Study | `OA-TPC-001` |
| Baseline | `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md` v1.0 |
| Draft status | `DRAFT_NON_AUTHORIZING_PRE_RUN_AMENDMENT` |
| Empirical status | No model selected, no model output, no pilot, no primary run, no result |
| Authority | This draft does not authorize a model, provider, spending, preregistration, data access, publication, deployment, or release |
| Change scope | Research-document clarification and pre-run acceptance contract only |
| Conditions | F0, F1, and F2 remain unchanged |
| Owner action | Required before this draft can become a locked protocol amendment |

> **NON-AUTHORIZING NOTICE.** This file is a proposed amendment record, not a
> replacement for the canonical v1.0 protocol and not a run instruction. The
> v1.0 protocol remains the source of truth until the owner explicitly accepts
> a versioned amendment and records the remaining authorization decisions. No
> empirical phase may begin because this file exists.

This draft is intentionally limited to the bounded pre-run diagnostic. It does
not broaden the study into provenance discovery, real-world independence,
truth finding, human utility, deployment validation, a Dempster–Shafer arm, or
a reusable benchmark. It records what is already fixed, what follows from the
fixed definitions, what this draft proposes to clarify, what remains unknown,
and what evidence must exist before a separately owner-authorized run.

## 1. Reading the labels in this draft

The following labels keep source facts, logical consequences, decisions, open
questions, and future acceptance work separate.

| Label | Meaning |
| --- | --- |
| **[SOURCE FACT]** | Directly recorded in the charter, v1.0 protocol, readiness memo, local harness, or Round 1/2 audit artifacts. It is not a model result. |
| **[DERIVATION]** | Arithmetic or logical consequence of a source-defined formula or contract. It is not an experiment. |
| **[DRAFT DECISION]** | A proposed v1.1 interpretation or guard. It is not locked until the owner accepts it in a versioned protocol receipt. |
| **[UNKNOWN]** | Not established by the inspected artifacts. It must not be filled with a favorable assumption. |
| **[FUTURE GATE]** | Evidence that must be produced and reviewed before the relevant phase can be authorized. A listed gate is open until its receipt exists. |
| **[NON-ACTION]** | An explicit action that this draft does not take and does not authorize. |

## 2. Compact plain-language summary

**[SOURCE FACT]** Nine reports can still be one information pathway. The
synthetic graph in this study can stipulate which reports share an origin, but
the model is not discovering that graph and the graph does not prove truth,
authority, permission, or real-world independence.

**[SOURCE FACT]** F1 and F2 are deliberately close. F1 gives the model the
same reports and the same explicit counting rule with no relation cue. F2 gives
the same rule and the same reports plus visible relation codes supplied by the
benchmark. `INDP` means “separate origin in this benchmark,” not “independent
in the real world.” `UNKN` means unresolved; it is not a hidden zero or a
license to count a report as independent.

**[DERIVATION]** The primary `FC_cons` value is deliberately conservative: an
invalid answer is a risk event, and a valid answer that asserts at least two
supporting origins on a bundle whose supporting-origin certainty is `none`,
`single`, or `unknown` is also a risk event. Thus it is a safety-oriented
asserted-count-risk measure. It is not, by itself, proof that the model made a
false claim, understood provenance, or semantically integrated the reports.

**[DERIVATION]** VOR asks a narrower safety question on a fixed set of 75
multiple-origin bundles: was the output valid, did it assert at least two, and
did its selected supporting reports cover at least two stipulated support
origins? Passing VOR does not require the exact count, exact selected set,
coherent claim stance, or correct handling of a wrong-origin distractor.

**[DRAFT DECISION]** The safe pre-run description is therefore: “a
frozen-model diagnostic of whether a visible, benchmark-stipulated
origin-relation cue changes conservative asserted-count risk beyond the same
explicit rule, with a fixed selected-support-origin coverage guardrail.” The
phrase “origin accounting” must not be used to imply exact origin discovery or
assignment accuracy.

**[FUTURE GATE]** Before any owner-authorized model run, the team must close
the invalidity/coherence interpretation, validate operating characteristics
under paired invalid dependence, obtain exact selected-model tokenizer and
chat-template parity, complete leakage and semantic controls, and record the
owner’s model/budget/phase authorization. A null, harmful, unstable,
shortcut-driven, threshold-only, invalidity-driven, or stopped result remains
an outcome to preserve.

## 3. Source boundary and amendment basis

### 3.1 Source facts inspected

**[SOURCE FACT]** The following local artifacts define the basis of this draft.
The paths are included so a reviewer can distinguish an existing fact from a
proposed amendment.

| Source | Fact used in this draft |
| --- | --- |
| `reports/overnight/v15_2/PROGRAM_CHARTER.md` | The v15.2 pass is a bounded pre-run hardening pass. No model, effect, participant result, deployment result, preregistration, publication, or production action exists or is authorized by the program. |
| `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md` | v1.0 fixes F0/F1/F2, the bundle unit, `A=300`, the fixed `M` definition, the `FC_cons` and VOR formulas, the synthetic/stipulated truth boundary, the T1 firewall, and the negative-result contract. |
| `research/F0_F1_F2_IMPLEMENTATION_READINESS_V1.md` | The local scaffold is offline implementation evidence only. The selected model and intended tokenizer are unresolved; the deterministic regex tokenizer is a surrogate; smoke leakage status is unresolved. |
| `research/overnight/v15_2/ROUND1_RESEARCH_METHODS_AUDIT.md` | The residual contribution is a conditional supplied-field condition effect. P0 concerns include invalidity decomposition, interval/operating characteristics, actual tokenizer parity, leakage/semantic audit, terminology, and count/stance/evidence coherence. |
| `research/overnight/v15_2/ROUND1_RESEARCH_SOURCE_LEDGER.md` | Provenance graphs, source dependence, conflict-aware RAG, source attribution, metadata bias, and evidence-utilization diagnostics are adjacent prior art; the search is bounded and does not support a broad novelty or priority claim. |
| `research/overnight/v15_2/ROUND2_METHODS_NOVELTY_ADVERSARY.md` | `FC_cons` is a conservative asserted-count-risk composite; VOR is a threshold guardrail; the Dempster–Shafer/EvidentialRAG lead is adjacent, unverified, and deferred; current planning and control receipts do not authorize a run. |
| `research/overnight/v15_2/ROUND2_METHODS_DECISION_MATRIX.md` | Round 1 P0 recommendations are retained, revised, or accepted as open gates; no D-S/EvidentialRAG condition is added to F0/F1/F2. |
| `tools/origin_accounting/analysis.py` and `parser.py` | The current scorer uses validity/count/certainty for `FC_cons`, uses the fixed support-origin threshold for VOR, preserves parser reason codes, and does not use `claim_state` or `evidence_ids` in the primary event. |
| `tools/origin_accounting/generator.py` and `power.py` | Local prompt parity is surrogate-only; the current planning helper is planning-only and applies invalidity independently between F1 and F2. |
| `tests/test_origin_accounting.py` | Existing tests exercise offline generator/parser/scorer/manifest/planning invariants. They do not establish model behavior, provenance discovery, power, interval coverage, or generality. |

### 3.2 No invented results

**[SOURCE FACT]** No model has been selected. No checkpoint, tokenizer
revision, backend chat-template receipt, primary output, pilot output, effect,
confidence interval, p-value, safety result, transfer result, or human result
exists in the inspected package.

**[NON-ACTION]** This draft does not run a model, call a provider, access a
live or external corpus, use a D-S/EvidentialRAG implementation, change a
schema, modify the harness, generate primary outputs, deploy, preregister,
publish, or push.

**[DRAFT DECISION]** Any future numerical value in a run receipt must be
clearly separated from the design values in this draft. `N=300`, `|M|=75`,
`-0.08`, `-0.05`, `alpha=.05`, and the planning grids below are design inputs,
not observed results or evidence of adequacy.

## 4. Amendment disposition at a glance

**[DRAFT DECISION]** The proposed amendment is clarificatory and gate-focused.
It does not change the F0/F1/F2 prompts, experimental unit, primary set,
safety set, locked formulas, negative-result commitment, or T1 boundary.

| Area | v1.1 draft disposition | Change to locked v1.0 estimand/conditions? | Current status |
| --- | --- | --- | --- |
| F0/F1/F2 | Preserve exactly. F1 remains the rule-only comparator; F2 remains the same rule plus visible stipulated relation values; F0 remains secondary. | **No.** | Locked; no empirical run. |
| Primary unit and denominators | Preserve bundle unit, `A=300`, and fixed `M=75` multiple-certainty rows. | **No.** | Locked design; operating adequacy unknown. |
| `FC_cons` | Retain the formula, but name and interpret it as a conservative asserted-count-risk composite. Require an invalidity/valid-only decomposition before using a semantic cue narrative. | **No formula change; interpretation gate added.** | Gate open. |
| VOR | Retain the formula and fixed denominator; describe it as thresholded selected stipulated support-origin coverage, not exact accounting. | **No.** | Gate open pending interval/coverage evidence. |
| Coherence | Keep count/stance/evidence out of the primary formula; add offline fixtures and a descriptive coherence sidecar. | **No primary endpoint change.** | Fixtures and narrative rule must be locked. |
| Tokenizer/resource parity | Keep local surrogate as development-only; require selected-backend tokenizer/chat-template receipt and byte parity before a run. | **No.** | Hard gate open. |
| Operating characteristics | Extend planning to paired invalid dependence and condition-specific invalidity; validate the final interval at `N=300`, `|M|=75`. | **No observed result or automatic N change.** | Planning gate open. |
| Leakage/semantic controls | Treat listed controls as open until receipts pass; failures quarantine or narrow interpretation. | **No.** | Clearance unresolved. |
| T1 | Keep descriptive, rights/version/annotation gated, and outside all primary inference. | **No.** | Firewalled. |
| D-S/EvidentialRAG | Defer as adjacent, unverified future comparator; do not add an arm or use it as novelty evidence. | **No.** | Deferred. |
| Result commitment | Preserve null, negative/harmful, unstable, shortcut/direct-code, stopped, and non-transporting outcomes. Add explicit invalidity-driven and threshold-only language. | **No.** | Locked commitment retained. |

## 5. Locked items that this draft must not change

### 5.1 Conditions and prompt contrast

**[SOURCE FACT]** The v1.0 condition definitions remain exactly as follows:

| Condition | Prompt-visible material | Role |
| --- | --- | --- |
| **F0** | Claim, report text, opaque IDs, fictional dates, `NONE` relation placeholders, and the ordinary bounded evidence-assessment instruction. | Secondary ordinary baseline. |
| **F1** | The same report bytes, order, IDs, metadata shape, output contract, and explicit rule instruction; all relation slots are `NONE`. | Primary rule-only comparator. |
| **F2** | The byte-identical F1 rule instruction plus the same report bytes/order and visible `DPND`, `INDP`, or `UNKN` values from the stipulated graph. | Primary supplied-cue condition. |

The model must not receive the condition name, split, bundle ID, origin ID,
origin structure, gold count, gold stance, or evaluator-only graph fields.

The relation legend remains:

```text
DPND = dependent on another observed report or origin path
INDP = separate origin in this benchmark, stipulated rather than discovered
UNKN = relation unresolved; do not count it as independent
NONE = no relation value supplied in this slot
```

**[DRAFT DECISION]** No coherence fixture, control, or future comparator in
this amendment may turn F0, F1, or F2 into a different task. In particular,
the draft does not add a D-S/EvidentialRAG condition, a retrieval arm, a
different relation codebook, a claim-state instruction, or a human decision
endpoint to the confirmatory family.

### 5.2 Unit, sets, and truth boundary

**[SOURCE FACT]** The experimental unit remains one synthetic evidence bundle.
`A` is the fixed ordered list of all 300 assigned primary bundles. `M` is the
fixed ordered subset of the 75 primary bundles whose stipulated supporting-
origin certainty is `multiple`. `M` is defined from the pre-run restricted
manifest and is never intersected with valid outputs or post-run selections.

**[SOURCE FACT]** The generator may establish synthetic nodes and edges by
construction: report, artifact, transformation, origin family, stance, and
synthetic time. It cannot establish real-world honesty, truth, authority,
causal or epistemic independence, permission, authorization, consequence, or
prevalence.

**[DRAFT DECISION]** `INDP` must be expanded in scientific prose as
“independent-as-stipulated” or “separate origin as stipulated in this
benchmark.” `UNKN` must remain an unresolved state. Neither code may be
translated into a real-world claim.

### 5.3 Primary and safety formulas

**[SOURCE FACT]** For bundle `i` and condition `c`, v1.0 defines:

```text
FC_obs(i,c) = 1[valid(i,c)
                  AND hat_n(i,c) >= 2
                  AND certainty_i in {none,single,unknown}]

FC_cons(i,c) = 1[NOT valid(i,c) OR FC_obs(i,c)=1]
FC_lib(i,c)  = 1[valid(i,c) AND FC_obs(i,c)=1]
```

For each `i` in fixed `M`:

```text
VOR(i,c) = 1[valid(i,c)
               AND hat_n(i,c) >= 2
               AND |O_support(E(i,c))| >= 2]
```

Here `O_support(E)` is computed by the evaluator from selected evidence IDs
whose benchmark stance is `supports`; refuting, neutral, dependent-copy, and
unknown origins cannot inflate support-origin recall.

**[DERIVATION]** The primary contrast remains:

```text
Delta_FC_cons = mean_i_in_A[FC_cons(i,F2)]
                - mean_i_in_A[FC_cons(i,F1)]
```

Invalid outputs remain in the all-assigned denominator. The v1.0 primary
decision remains a beneficial delta, an exact two-sided paired McNemar/binomial
test with `p < .05`, and a declared 95% paired interval whose upper bound is
below zero. The planning benchmark `Delta=-0.08` remains a planning input,
not an additional undisclosed test and not a result.

**[DERIVATION]** The safety decision remains a fixed-`M` F2-minus-F1 VOR
contrast with invalid outputs coded as zero and a one-sided lower bound greater
than the locked `-0.05` margin. The exact interval method remains an open
pre-registration decision; the current local percentile-bootstrap helper is a
development scaffold and cannot be silently promoted by this draft.

### 5.4 Secondary measures and multiplicity

**[SOURCE FACT]** Absolute origin-count error, selected supporting-origin-set
precision/recall/exact match on certified non-contested rows, claim state,
invalid reason codes, confidence, resource use, and structure/domain/style/
order/noise slices remain descriptive. Unknown-origin and invalid rows remain
undefined for metrics whose gold values are not certified; they are not
imputed. The confirmatory family remains the primary FC decision plus the VOR
safety gate. F0 and other slices do not become a second p-value family.

## 6. Proposed v1.1 interpretation amendments

### 6.1 `FC_cons`: field-risk interpretation and invalidity gate

**[SOURCE FACT]** The implementation and v1.0 protocol calculate `FC_cons`
from validity, emitted count, and gold supporting-origin certainty. They do not
use `claim_state` or selected evidence IDs in the primary event.

**[DERIVATION]** A change in `FC_cons` can be caused by at least two distinct
components:

1. a change in parse validity or runtime/format compliance; or
2. a change in valid outputs that assert at least two supporting origins on a
   `none`, `single`, or `unknown` row.

The same primary delta can arise from different mixtures of those components.
The primary formula therefore cannot identify semantic relation use by itself.

**[DRAFT DECISION — REQUIRES OWNER ACCEPTANCE]** Retain the all-assigned
formula as the v1.1 primary safety event, but name it consistently:

> **Conservative asserted-count risk:** an all-assigned risk event that codes
> invalid output as risky and codes a valid asserted count of at least two as
> risky when the benchmark does not certify multiple supporting origins.

“False corroboration” may remain a historical shorthand for the formula only
where the full conservative coding is shown. It must not be presented as a
pure claim-truth, semantic-understanding, or internal-cue measure.

**[FUTURE GATE]** Every future primary receipt must include, for F1 and F2:

- valid and invalid counts/rates on all `A=300` rows;
- invalid counts by the closed parser/runtime reason code, with raw-byte
  receipt linkage and no-retry proof;
- the valid-only `FC_obs` counts/rates and their paired contrast;
- the all-assigned `FC_cons` counts/rates and their paired contrast;
- a two-by-two or equivalent decomposition showing validity and risk-event
  status together; and
- an owner-locked narrative rule for a result whose difference is primarily
  invalidity, primarily valid overcount, or mixed/opposing.

**[UNKNOWN]** No materiality threshold for calling an invalid-rate difference
“primarily” or “material” is locked in v1.0. The owner must choose and record
that threshold before any output is inspected for efficacy. Until then, a
favorable composite delta may be reported only as a composite risk result,
not as typed-cue or semantic-integration evidence.

### 6.2 VOR: threshold safety guardrail, not exact origin accounting

**[SOURCE FACT]** VOR requires validity, an emitted count of at least two, and
at least two distinct stipulated support-side origins among selected support
reports in fixed `M`. It does not require an exact count of three in the
multiple-origin fixtures, an exact selected support-origin set, coherent
`claim_state`, or a wrong-origin distractor test.

**[DERIVATION]** A rule that emits `2` on every multiple-origin bundle can pass
the VOR threshold when two stipulated support origins are selected, even if
the constructed gold count is three. A rule that emits `1` on all
one-origin/unknown rows can avoid the FC event without demonstrating origin
accounting. These are valid threshold-policy behaviors under the current
estimand, not evidence of exact counting.

**[DRAFT DECISION — REQUIRES OWNER ACCEPTANCE]** Use this interpretation in
the title, abstract, tables, and handoff:

> VOR is **selected stipulated support-origin coverage at a safety threshold**.
> It is a guardrail against blanket suppression of multiple-origin support,
> not exact origin-counting or origin-assignment accuracy.

The descriptive count-error and selected-origin-set panels may characterize
the threshold result but cannot replace `FC_cons`, change `VOR`, enlarge `M`,
or create a new confirmatory family. A future wrong-origin stress corpus is
outside this amendment and outside the first confirmatory family.

### 6.3 Count/stance/evidence coherence

**[SOURCE FACT]** The parser strictly validates the four-field JSON contract,
but a syntactically valid output can contain a count, claim stance, and
selected evidence set that do not agree. The v1.0 primary scorer intentionally
does not use those fields to calculate `FC_cons`.

**[DRAFT DECISION — REQUIRES OWNER ACCEPTANCE]** Adopt the minimal
field-risk interpretation for v1.1: do not change the primary formula; expose
coherence as a separately named descriptive diagnostic and make the result
narrative follow the field-risk boundary. Do not call an incoherent output
evidence of claim-level corroboration. A stronger claim-corroboration endpoint
would require a new protocol, not a silent v1.1 reinterpretation.

**[FUTURE GATE]** The coherence fixture pack in Section 7 must pass offline,
and the locked run receipt must report which outputs are valid but incoherent.
No post-hoc repair, count reconstruction, evidence-ID inference, or semantic
reinterpretation is allowed.

## 7. Offline coherence and invalid-output fixture pack

**[SOURCE FACT]** These fixtures are not model results. They are deterministic
contract tests for the parser, scorer, and receipt interpretation. They must
be added to the next authorized implementation/specification update by the
owner or implementation steward; this draft itself does not edit the harness.

| Fixture | Construct | Required contract behavior | Interpretation boundary |
| --- | --- | --- | --- |
| `C-01` | Syntactically valid object with `origin_count_supporting=4`, `claim_state=refuted`, and a valid evidence-ID list on a certified `single` row. | `FC_cons` follows validity/count/certainty and remains risk-coded; a separate coherence flag marks count/stance tension. | The primary event is an asserted-count field-risk event, not a claim-state truth judgment. |
| `C-02` | Syntactically valid object with `origin_count_supporting=0`, `claim_state=supported`, and valid evidence IDs. | `FC_obs` is not triggered by the count; a separate coherence flag marks the count/stance tension. | A non-risk `FC_cons` value cannot be narrated as a coherent supported claim. |
| `C-03` | Valid output whose count and selected evidence IDs disagree with the stipulated support-origin set. | Primary FC scoring remains formula-defined; VOR uses only the threshold and selected support-side origins; descriptive count/set fields expose the disagreement. | Do not infer a corrected count or silently credit omitted origins. |
| `C-04` | Valid `origin_count_supporting=2` on an `unknown`-origin bundle, with a valid numeric confidence and legal IDs. | `FC_cons=1`; the row is not in fixed `M`; certified support-origin metrics remain undefined. | The conservative event does not claim the latent world has one or zero origins. |
| `C-05` | Valid output selecting a neutral or refuting report alongside support reports. | Preserve the selection; support-origin metrics inspect only selected reports whose benchmark stance is `supports`; neutral/refuting selection is not automatically a support-selection error. | Evidence used for assessment is not identical to evidence credited as supporting the claim. |
| `C-06` | Empty output, invalid UTF-8, malformed JSON, duplicate key, unknown key, wrong type, non-finite confidence, too many IDs, unknown ID, and duplicate evidence ID. | Each receives its existing distinct parse status/error code; raw bytes, length, hash, and no-repair/no-retry receipt are retained. `FC_cons=1`; VOR is `0` when applicable. | Invalidity is visible and cannot be hidden as semantic overcount or repaired into a favorable answer. |
| `C-07` | Paired synthetic score vectors where only F1/F2 invalidity changes, only valid overcount changes, both change in the same direction, and components move in opposite directions. | Receipt reports invalid-only, valid-only, and composite contrasts separately and applies the predeclared narrative rule. | A composite improvement cannot be called a semantic cue effect without the locked interpretation gate. |
| `C-08` | Valid rows with count/evidence mismatch on certified non-contested rows, conflict rows, and unknown rows. | Certified non-conflict sidecars may report count error/set metrics; conflict and unknown scopes remain visibly separate per v1.0. | Undefined metrics remain undefined; no latent unknown truth is imputed. |
| `C-09` | A selected refuting `INDP` cue in a conflict fixture. | Refuting origin is excluded from support-side VOR coverage; support/refute origin sets remain separate. | A refuting independent-as-stipulated cue cannot inflate supporting-origin recall. |
| `C-10` | Attempted “wrong-origin” fixture without changing the corpus contract. | Reject the attempted fixture or label it out of scope; do not fabricate a v1 metric. | v1 does not test wrong-origin assignment; that is future stress work. |

**[FUTURE GATE]** Acceptance requires a fixture receipt naming the fixture
version, parser/scorer versions, expected statuses, expected field-risk values,
coherence flags, raw-output hash checks, and the exact set of tests run. A
passing fixture receipt still proves only local contract behavior.

## 8. P0 gates before any owner-authorized model phase

**[SOURCE FACT]** Round 1 and Round 2 identify six P0 areas that block a
useful scientific handoff or any pilot opening. The table below carries them
forward as explicit, fail-closed gates. “Open” means no accepted evidence
receipt is currently present; it is not a prediction about whether a future
gate will pass.

| Gate | Why it is P0 | Required acceptance evidence before authorization | Failure disposition | Current status |
| --- | --- | --- | --- | --- |
| **P0-01 — `FC_cons` decomposition** | The composite combines invalid output with valid asserted-count risk. | Offline decomposition fixtures; final locked materiality/narrative rule; run receipt with invalid reason counts, invalid-only delta, valid-only `FC_obs` delta, and composite delta. | Report as conservative asserted-count risk only; no semantic cue interpretation when the gate fails. Preserve all invalids. | **OPEN** |
| **P0-02 — interval and operating characteristics** | `N=300` and `|M|=75` are design inputs; the current helper does not model paired invalid dependence and the VOR interval/coverage method is not final. | Planning-only receipt using the final decision rule, exact final interval, paired invalid-dependence grid, type-I error, power at planning delta, interval coverage, discordance counts, and VOR gate probability/coverage at fixed `M=75`. | Downgrade to estimation/feasibility or create a new protocol if the design is inadequate; do not tune `N`, margin, or gate after outputs. | **OPEN** |
| **P0-03 — selected-model parity** | Surrogate token counts and byte equality do not establish selected-backend token/chat-template parity. | Owner-selected model/checkpoint/tokenizer/license receipt; exact chat-template and rendered F1/F2 hashes/counts; byte and intended-tokenizer parity for every paired input; output cap/truncation/retry lock. | Fail closed; no primary input is opened. | **OPEN** |
| **P0-04 — leakage and semantic validity** | Smoke diagnostics and listed controls are not clearance; template, codebook, position, style, or stance errors can create a false condition effect. | Frozen held-out-family character/token probe with ceiling and Wilson interval; exact/near-duplicate and family audit; codebook/position/field-only/overlap/noise controls; independent semantic/stance/transformation audit with adjudication/quarantine receipt. | Quarantine or repair corpus/prompt version; narrow the claim to the observed shortcut only. | **OPEN** |
| **P0-05 — claim and terminology boundary** | “Benchmark,” “origin accounting,” “metadata use,” and “discrimination layer” can imply unsupported mechanism or generality. | Claim-source lint over title/abstract/conclusion/handoff; one-model, synthetic, stipulated, supplied/oracle, and observable-output qualifiers; source-status reconciliation; no priority/exhaustive-review claim. | Revise language before any paper or handoff; no broad result claim. | **OPEN** |
| **P0-06 — count/stance/evidence coherence** | Valid but incoherent JSON can pass the primary event while being misnarrated as claim corroboration. | Fixture pack in Section 7; locked field-risk interpretation; valid-incoherent counts and reason labels in run receipt; no repairs or post-hoc reconstruction. | Keep only the field-risk result; do not claim semantic corroboration or exact origin accounting. | **OPEN** |

**[FUTURE GATE — owner authority]** In addition to P0 evidence, the owner must
separately record the exact phase authorization. A gate receipt is not an
authorization. An owner authorization without a closed applicable P0 gate is
invalid under this draft.

## 9. Selected-model parity and resource-control receipt

### 9.1 What remains unknown

**[UNKNOWN]** The selected model, checkpoint revision, tokenizer revision,
chat-template behavior, hardware/runtime, and exact output decoding are not
known. The local `deterministic-regex-surrogate-v1` is not the intended model
tokenizer and cannot satisfy this gate.

### 9.2 Required receipt contents

**[FUTURE GATE]** Before any pilot or primary prompt is opened, create a
versioned selected-model parity receipt containing, at minimum:

1. owner-approved model identifier, exact checkpoint revision, exact tokenizer
   revision, license/permitted-use record, and local model-file hashes;
2. runtime, dependency, hardware, memory, compute/time/storage budget, and
   deterministic-decoding or exactly-three-seed policy;
3. exact backend chat-template source/bytes, template hash, special-token
   settings, truncation policy, input/output token limits, and no-retry policy;
4. per-bundle F1/F2 system, user, final-input, instruction, report-text-map,
   and ordered-report-sequence hashes;
5. exact input-token counts under the selected tokenizer for every F1/F2 pair,
   with equality required before primary opening;
6. exact UTF-8 input-byte lengths recorded separately as a resource-control
   check, with equality required for every F1/F2 pair;
7. output-cap, retrieval-call, and tool-call receipts (`0` for the locked
   study), plus evidence-order and report-byte equality checks;
8. fail-closed mismatch tests that demonstrate a token, byte, template,
   order, hash, or cap mismatch prevents the pair from being admitted; and
9. a receipt status that distinguishes `selected_tokenizer_pass` from the
   development-only `surrogate_parity_pass`.

**[DRAFT DECISION]** F1/F2 selected-token equality is the inferential resource
parity requirement. Byte equality is a separate implementation/resource
check. Neither is evidence that the conditions are semantically equivalent;
the relation cue is intentionally the treatment difference.

**[DRAFT DECISION]** F0 may remain secondary, but its shared report bytes,
order, output cap, and resource receipt must remain visible. F0 parity cannot
be used to enlarge or replace the F1/F2 confirmatory contrast.

### 9.3 Acceptance and non-authorization

**[FUTURE GATE]** Acceptance requires every assigned F1/F2 pair to pass the
same receipt schema and a fail-closed replay of the parity checker. A local
surrogate receipt, a hand-counted token total, a byte-only match, or a smoke
fixture cannot satisfy this gate.

**[NON-ACTION]** This draft does not select a model, inspect model files,
render a backend template, or produce any parity receipt.

## 10. Paired invalid-dependence operating-characteristic plan

### 10.1 Purpose and status

**[SOURCE FACT]** v1.0 requires planning for FC baseline, discordance, effect,
sample size, invalid rates, and conservative/liberal coding. The current local
helper applies invalid draws independently to F1 and F2 and uses a named
development interval scaffold. That helper is not evidence of final power or
coverage.

**[DRAFT DECISION — REQUIRES OWNER ACCEPTANCE]** Before preregistration, run a
planning-only operating-characteristic simulation that preserves the paired
bundle unit and explicitly varies the joint invalidity pattern. This is a
design validation, not a pilot and not a model run.

### 10.2 Paired data-generating objects

**[DERIVATION]** For the latent valid endpoint, retain the v1.0 paired
Bernoulli parameterization:

```text
p10 = P(F1=1, F2=0)
p01 = P(F1=0, F2=1)
p10 + p01 = discordance
p01 - p10 = Delta_F2_minus_F1
p11 = baseline_F1 - p10
p00 = 1 - p10 - p01 - p11
```

For invalidity, define `I1` and `I2` as condition-specific invalid indicators,
with margins `r1=P(I1=1)` and `r2=P(I2=1)`. Define `q11=P(I1=1,I2=1)` and
derive:

```text
q10 = r1 - q11
q01 = r2 - q11
q00 = 1 - q11 - q10 - q01
max(0, r1+r2-1) <= q11 <= min(r1,r2)
```

**[DERIVATION]** The feasible lower and upper bounds expose the strongest
possible negative/positive pairing for the chosen margins. The independence
point is `q11=r1*r2` when it lies in the feasible interval. Using the bounds
and independence point prevents a single assumed invalid correlation from
being mistaken for the only plausible operating condition.

The planned conservative and liberal transformations remain:

```text
Xc_cons = 1 if Ic=1 else Yc
Xc_lib  = 0 if Ic=1 else Yc
Zc_vor  = 0 if Ic=1 else Wc
```

where `Yc` is the latent FC event and `Wc` is the latent VOR event. The
primary uses `X_cons`; liberal and valid-only variants remain sensitivities.

**[UNKNOWN]** The relationship between invalidity and the latent semantic
event is not identified by the offline scaffold. The primary planning overlay
must state whether invalidity is independent of `Y/W`, and a stress analysis
should include outcome-associated invalidity bounds if the owner intends to
make a robustness statement. No favorable independence assumption may be
silently treated as established behavior.

### 10.3 Minimum FC grid to freeze before preregistration

**[FUTURE GATE]** The planning receipt must include, at minimum, the following
design cells. The exact seed schedule, invalid-pair cells, interval algorithm,
and resampling count must be frozen in the receipt before any pilot efficacy
output is opened.

| Dimension | Required values or coverage |
| --- | --- |
| F1 baseline FC risk | `0.20`, `0.30`, `0.40` |
| Paired FC discordance | `0.10`, `0.20`, `0.30` |
| F2-minus-F1 delta | `0`, `-0.05`, `-0.08`, `-0.10` |
| Assigned primary size | `240`, `280`, `300`, `320`, `360` |
| F1 invalid margin | `0`, `0.02`, `0.05`, `0.10` |
| F2 invalid margin | `0`, `0.02`, `0.05`, `0.10`, including unequal F1/F2 pairs |
| Paired invalidity | Feasible lower bound, independence point, and feasible upper bound for `q11` for each selected `(r1,r2)` pair; any additional correlation points must be frozen before simulation |
| Invalid coding | Conservative primary coding plus liberal/valid-only sensitivity coding |
| Replications | At least `10,000` independent repetitions per valid cell, unless a new owner-accepted protocol states otherwise |

**[FUTURE GATE]** For each cell, retain the seed, parameter tuple, valid-cell
or skip reason, number of discordant pairs, invalid-pair counts, estimated
decision rate, and interval summaries. A skipped infeasible probability cell
must remain visible; it must not be silently removed from the grid.

### 10.4 Minimum VOR grid at fixed `M=75`

**[FUTURE GATE]** The VOR planning receipt must retain the fixed safety
denominator and cross:

| Dimension | Required values or coverage |
| --- | --- |
| Baseline VOR | `0.70`, `0.80`, `0.90` |
| Paired VOR discordance | `0.10`, `0.20`, `0.30` |
| F2-minus-F1 VOR delta | `0`, `-0.02`, `-0.05`, `-0.08` |
| Safety size | Exactly `|M|=75`; optional nearby sizes may be descriptive only and cannot replace 75 |
| Invalid margins/dependence | The same condition-specific margins and feasible paired-invalidity points used for FC |
| Invalid coding | Invalid output coded as zero, as locked for VOR |
| Replications | At least `10,000` per valid cell, with the exact final one-sided interval method |

The receipt must report one-sided interval coverage, probability of passing the
`-0.05` safety margin, false-gate behavior at delta zero, and the effect of
paired discordance and invalid dependence. It must not use the pilot effect to
choose a favorable `M`, margin, interval, or sample size.

### 10.5 Required planning outputs and decisions

**[FUTURE GATE]** The accepted planning packet must report:

- type-I error at delta zero under the exact primary decision;
- decision power at the planning delta `-0.08` and at the surrounding effect
  grid;
- paired percentile or alternative interval coverage under the final declared
  method, not only a p-value;
- the number and distribution of discordant pairs;
- sensitivity to invalid margins, invalid dependence, and invalid coding;
- fixed-`M` VOR coverage and safety-gate probability at delta zero, `-0.05`,
  and nearby deltas;
- the exact seed, grid, interval, resampling, and implementation receipt; and
- an explicit decision on whether `N=300` and `|M|=75` remain fit for a
  confirmatory interpretation.

**[DRAFT DECISION]** If the design cannot estimate the planning difference
with useful operating characteristics at `N=300`, the next permitted action
is to downgrade to estimation/feasibility or create a new protocol. It is not
permitted to enlarge `N`, change the margin, remove invalids, or choose a
favorable slice after model output is seen. If VOR is too imprecise at `M=75`,
it must be downgraded before preregistration rather than rescued by enlarging
`M` after inspection.

**[NON-ACTION]** No planning simulation is run by this document. Any future
planning output remains labeled `PLANNING_ONLY_NO_PILOT_OR_MODEL_OUTPUTS`.

## 11. Leakage, shortcut, contamination, and semantic controls

**[SOURCE FACT]** The protocol lists controls for IDs, formatting, overlap,
style, position, split family, codebook, metadata-only behavior, field-only
behavior, relation noise, unknown preservation, refuting-origin separation,
and independent semantic audit. The existing nearest-centroid smoke check is
explicitly not leakage clearance.

**[FUTURE GATE]** The following control matrix must be frozen before opening
the primary split. Listing a control is not passing it.

| Control | What it tests | Required receipt | Failure interpretation |
| --- | --- | --- | --- |
| Exact/near-duplicate and family blocking | Cross-split contamination from copied/paraphrased families | Exact normalized-text report; character/token near-duplicate candidates; proposition/origin-family membership; quarantine reasons; immutable split hash | Corpus/split failure; affected data do not enter efficacy evidence. |
| Held-out-family character/token probe | Whether structure or condition is recoverable from surface form | Frozen blocked TF-IDF/character classifier, held-out family split, ceiling, Wilson interval, seed, and threshold | Above-ceiling or trivially separable structure is a corpus failure, not a model discovery. |
| Style/domain/length/position/order balance | Surface and serial-position leakage | Balance table and cross-tab receipt for every split/condition | Repair/regenerate or narrow claim to shortcut behavior. |
| F1/F2 format and resource parity | Whether the treatment is merely bytes, tokens, delimiters, or padding | Selected-model parity receipt plus byte/hash/order equality | Fail primary lock; no causal interpretation. |
| Codebook permutation / neutral labels | Relation semantics versus token identity or salience | Predeclared permutation/neutral-code stress receipt with untouched gold and interpretation rule | Token-identity/label shortcut; do not call semantic relation use. |
| Metadata-only direct counter | Whether visible codes alone reproduce the count effect | Offline direct-code output and comparison receipt, clearly non-model if no model is authorized | A matching effect is direct-code behavior, not report integration. |
| Field-only / masked-report control | Whether report text is necessary for the observed behavior | Prespecified masked-report condition or offline control receipt under a separately authorized model phase | A surviving effect is not evidence of semantic report integration. |
| Relation-position/order swap | Cue location and attention/order sensitivity | Fixed swap/permutation receipt with output and interpretation lock | Position-fragile result is formatting/attention behavior. |
| Low-overlap dependent vs high-overlap stipulated-distinct | Similarity shortcut versus supplied relation cue | Crossed fixture inventory and outcome receipt | Similarity-only behavior cannot support relation-cue semantics. |
| Relation-noise stress | Dependence on perfect oracle cues | `0.05`, `0.10`, `0.20` visible-code noise; gold graph untouched; unknown rows remain `UNKN` | Noise-fragile result is an oracle upper bound, not robust origin reasoning. |
| Unknown preservation | Whether unknown is silently treated as independent/dependent | All-`UNKN` fixture and invariant receipt | Construct/prompt failure; conservative unknown policy must remain visible. |
| Refuting-origin separation | Whether refutation can inflate support recall | Conflict fixture and scorer assertion | Scoring failure; refuting origins cannot count toward supporting VOR. |
| Independent semantic/stance/transformation audit | Whether generated text matches its intended construction | Prespecified sample across structure/style/position/domain; independent labels; agreement, adjudication, quarantine, and signed receipt | Corpus validity unresolved; affected rows are quarantined before any run. |
| Prompt-control/privacy/secret scan | Whether hidden labels, private text, credentials, or control strings leak into prompts | Zero-failure scan receipt over generator outputs, prompts, manifests, and environment boundary | Stop affected phase; preserve receipt; no secret or private material may enter the corpus. |

**[DRAFT DECISION]** A control failure is itself a result about the test
design, not a favorable model slice. It must be reported and either repaired
under a new locked version or used to narrow the claim. No control may be
selected, removed, or reweighted after efficacy inspection.

**[UNKNOWN]** No complete blocked classifier receipt, selected-model control
run, or independent semantic audit receipt exists in the current package.

## 12. T1 firewall: natural-syndication transfer remains separate

**[SOURCE FACT]** v1.0 defines T1 as an optional descriptive transfer tier,
not a condition, and prohibits it from supplying `A`, `M`, primary confidence
intervals, McNemar rows, VOR, or confirmatory effects.

**[DRAFT DECISION]** The firewall is unchanged and is restated here to prevent
an amendment or later handoff from weakening it:

1. T1 can be designed only after primary prompt and analysis locks and only
   with separate owner authorization.
2. T1 requires a separate dataset/version/license/annotation manifest,
   provenance of each native relation label, rights receipt, and stance/
   version audit.
3. A documented same-original NEWS-COPY pair may receive an adapter `DPND`
   while retaining its native duplicate label. A nonduplicate remains `UNKN`
   absent a documented source-path audit.
4. Newswire recurrence, cluster size, URL count, publisher count, date, byline,
   wording, topic, and wire-city metadata never produce synthetic `INDP`.
5. T1 cannot tune the v1 endpoint, prompt, denominator, margin, sample size,
   model choice, or favorable narrative.
6. Unresolved rights, version labels, stance labels, or origin labels fail
   closed. T1 cannot rescue a null, harmful, invalidity-driven, or shortcut
   result in the synthetic primary study.

**[UNKNOWN]** No T1 data access, rights receipt, annotation, transfer output,
or real-world result exists. The safest current T1 status is
`DESCRIPTIVE_FUTURE_TRANSFER_ONLY`.

## 13. Dempster–Shafer/EvidentialRAG disposition

**[SOURCE FACT]** Round 2 identifies Dempster–Shafer/EvidentialRAG as adjacent
prior art and notes that the checked EvidentialRAG v1 preprint does not supply
a source-family, duplicate, syndication, or dependence receipt for retrieved
passages. The round’s duplicate-inflation and fold-order examples are
mathematical derivations from the displayed operator, not empirical results.

**[DRAFT DECISION]** The lead is **DEFERRED and unverified**. It is not added to
F0/F1/F2, not used as evidence that the Pattern Map is novel, and not treated
as evidence that retrieved passages are independent. The v1.1 draft does not
change the locked estimand to a fusion comparison.

**[FUTURE GATE]** A separately authorized D-S/EvidentialRAG comparison would
require a new protocol fixing source-family/duplicate labels; supplied versus
inferred relation status; exact mass construction, frame, discounting,
normalization, `lambda`, arity, and fold order; order/duplicate sensitivity;
dependence-aware and non-D-S baselines; conflict/calibration/abstention
endpoints; and a rights/annotation receipt. None of that is a v1.1 run gate or
current result.

## 14. Locked negative, null, harmful, and shortcut result commitment

**[SOURCE FACT]** v1.0 and the readiness memo already commit to preserving
unfavorable outcomes. This amendment carries that commitment forward without
softening it.

| Result class | Required interpretation | Required disposition |
| --- | --- | --- |
| **Null F2−F1** | No evidence of added supplied-cue value in this setting; not evidence that all origin-aware systems fail. | Stop escalation from this mechanism; retain the rule/baseline or redesign only under a versioned protocol; do not search for a favorable slice. |
| **Negative / harmful** | F2 increases conservative asserted-count risk or fails the primary direction; if VOR also falls below `-0.05`, the tested cue suppresses stipulated supporting-origin coverage on this task. | Quarantine, inspect invalids/noise/structure, and retire or reverse the tested cue; never market harm as “conservative behavior.” |
| **Unstable** | Direction or conclusion changes materially across preregistered seeds, locked stress cells, or an explicitly unpowered robustness configuration. | Report model/configuration-specific instability; do not pool favorable runs or generalize. |
| **Shortcut / direct-code** | Effect is reproduced by metadata-only counting, field-only text replacement, code identity, formatting, order, style, overlap, or another non-semantic cue. | Fail the semantic-integration interpretation; repair/regenerate or narrow the paper to the observed shortcut behavior. |
| **Invalidity-driven** | The composite delta is materially explained by condition-specific parser/runtime invalidity rather than valid asserted-count behavior. | Report the composite safety result and decomposition; do not call it typed-cue or semantic value unless the predeclared gate permits that wording. |
| **Threshold-only VOR** | VOR passes while exact count/set fidelity or coherence remains weak or undefined. | Report thresholded selected stipulated support-origin coverage, not origin accounting or assignment accuracy. |
| **Noise-fragile** | Relation-noise stress removes the effect or changes its direction. | Report an oracle-cue upper bound; do not generalize to noisy relation data. |
| **Surface/semantic audit failure** | Split leakage, prompt leakage, stance/transformation disagreement, or semantic invariant failure remains. | Quarantine affected material; no efficacy interpretation. |
| **T1 non-transport** | A future descriptive transfer tier fails, is unavailable, or cannot establish rights/labels. | Make no real-world transfer claim; do not treat T1 as a rescue arm. |
| **Stopped/quarantined run** | Secret/private material, unauthorized access, manifest corruption, prompt/evidence mismatch, parity failure, raw-output loss, or unrecoverable backend deviation occurs. | Stop affected run, preserve the receipt, quarantine data, and exclude it from efficacy evidence. |

**[DRAFT DECISION]** Raw outputs, invalids, diagnostic failures, stopped runs,
and unfavorable cells remain in the reproducibility record when a future run
is separately authorized. No positive-only report may be assembled by hiding
the rows named above.

## 15. Status language and claim ladder

### 15.1 Status now

**[SOURCE FACT]** The correct current status language is:

```text
COHERENT_PROTOCOL_NOT_EXECUTION_READY
OFFLINE_SCAFFOLD_ONLY_NOT_PRIMARY_READY
NO_MODEL/PROVIDER/NETWORK_RUN
DS/EvidentialRAG LEAD: DEFERRED, UNVERIFIED ADJACENT COMPARATOR
F2-versus-F1: CONDITIONAL CANDIDATE, P0 GATES OPEN
```

**[DRAFT DECISION]** Use “proposed,” “pre-run,” “offline scaffold,”
“planning-only,” “one frozen model to be selected later,” “supplied,”
“oracle/stipulated,” “fictional/synthetic,” and “observable output
difference.” Use “pass” only for a named offline contract test, never for an
empirical effect or an unresolved readiness gate.

### 15.2 Wording that is prohibited before results

**[DRAFT DECISION]** Before a separately authorized run, do not write that the
model or framework:

- discovered provenance, copying, or real-world independence;
- used, understood, attended to, or causally relied on origin metadata;
- improved truth, retrieval, human decisions, safety, utility, or deployment;
- validated the Discrimination Layer or an eleven-responsibility architecture;
- established a benchmark result, power, coverage, or generality;
- demonstrated an effect, even if the offline harness passes; or
- showed that a D-S/EvidentialRAG operator treats retrieved passages as
  independent or is formally valid/invalid.

### 15.3 Conditional maximum claim after a future passing run

**[SOURCE FACT]** The v1.0 permitted claim remains the ceiling, and only if the
primary decision and VOR gate pass with all controls and interpretation gates
closed:

> On newly authored fictional evidence bundles with stipulated provenance
> graphs, the supplied typed-metadata condition produced less conservative
> false corroboration than the byte-identical rule-only condition on the
> tested frozen model, while fixed-set recall of multiple stipulated
> supporting origins remained above the prespecified safety margin.

**[DRAFT DECISION]** Any future accepted wording should replace the broad
shorthand with the more exact phrase “lower conservative asserted-count risk”
unless the owner explicitly retains “false corroboration” with the full
composite definition displayed. It must retain “supplied” or “oracle,”
“fictional/synthetic,” “one frozen model,” and “stipulated.” It cannot claim
provenance discovery, real-world independence, source authority, truth,
human benefit, transfer, or full-layer validation.

## 16. Acceptance evidence packet required before authorization

**[FUTURE GATE]** No owner-authorized pilot or primary run may open until the
applicable evidence packet is complete, versioned, and reviewed. The following
checklist is deliberately blank in this draft; it records requirements, not
completed work.

### 16.1 Common pre-run packet

- [ ] Owner accepts or rejects this amendment in a new locked protocol version;
  the version receipt identifies every accepted, modified, deferred, and
  rejected item.
- [ ] The canonical v1.0 formulas, F0/F1/F2 condition bytes, `A=300`, `M=75`,
  negative-result contract, T1 firewall, and no-peeking rule are reproduced in
  the locked version with hashes.
- [ ] P0-01 decomposition and narrative gate is closed, including the
  materiality rule and invalid reason-code table.
- [ ] P0-02 final interval and paired invalid-dependence operating-characteristic
  receipt is complete and labeled planning-only.
- [ ] P0-03 selected-model tokenizer/chat-template parity receipt is complete;
  surrogate parity is separately labeled and cannot substitute.
- [ ] P0-04 split, leakage, shortcut, privacy/secret, and independent semantic/
  stance/transformation audit receipts are complete, with zero unresolved
  failures affecting the locked primary material; any quarantine has a new
  locked manifest, explicit owner acceptance, and excludes every affected row
  from `A` and `M`.
- [ ] P0-05 claim-source lint and status-language review is complete; no broad
  novelty, internal-use, real-independence, truth, utility, or transfer claim
  remains.
- [ ] P0-06 coherence fixtures and expected field-risk/coherence interpretation
  are complete; no parser/scorer repair or post-hoc reconstruction is allowed.
- [ ] Exact primary and safety manifests are frozen, ordered, hashed, and
  checked against the restricted gold contract before any output is stored.
- [ ] Raw-output write-once path, parser version, error codebook, no-retry
  proof, and per-run receipt fields are reviewed.
- [ ] No secrets, private records, credentials, cookies, provider tokens,
  control strings, real-person harmful labels, or externally licensed article
  text enter the synthetic corpus or prompt package.

### 16.2 Additional pilot gate

**[FUTURE GATE]** A separately authorized 40-bundle pilot may test feasibility,
replay, runtime, memory, storage, parseability, output caps, semantic audit
process, and shortcut probes only. It may not tune the endpoint, denominator,
margin, prompt, or claim from efficacy output. The pilot exit packet must
record parseability, runtime/resource behavior, schema/provenance invariants,
cross-split duplicate status, control results, and all invalid reasons. Pilot
efficacy estimates cannot open the primary split.

### 16.3 Additional primary gate

**[FUTURE GATE]** Before a 300-bundle primary run, require the final locked
protocol/manifest, completed pilot feasibility disposition, preregistration
authorization if applicable, exact primary prompt and tokenizer parity receipt,
fixed `A`/`M` membership hashes, final analysis/interval method, and a separate
owner authorization naming the model, budget, output handling, and primary
phase. A primary run cannot be inferred from pilot completion or scaffolding.

### 16.4 Evidence interpretation

**[DERIVATION]** A complete packet establishes that the study is ready to be
considered for an owner-authorized phase. It does not establish a model effect,
semantic understanding, provenance discovery, real-world independence, truth,
human benefit, or deployment value.

## 17. Open unknowns and future work not silently added to v1.1

**[UNKNOWN]** The following remain unresolved or outside the amendment:

- exact model/checkpoint/tokenizer/chat-template and model-resource receipt;
- final one-sided VOR interval method and its coverage at `|M|=75`;
- the owner-selected materiality threshold for invalidity-driven interpretation;
- the full blocked lexical/condition classifier outcome;
- independent semantic/stance/transformation agreement and quarantine outcome;
- a wrong-origin distractor corpus and true support-origin assignment metric;
- richer relation objects for direction, scope, time, uncertainty, and relation
  provenance;
- relation inference from noisy/partial/dynamic external evidence;
- human correction, reliance, workload, accessibility, action, or utility;
- origin-bound memory/security and provenance poisoning;
- T1 rights, annotation, and transfer evidence; and
- a reusable multi-model/multi-task benchmark or general quality score.

**[DRAFT DECISION]** None of these unknowns may be filled by analogy, a
scaffold receipt, a favorable pilot, an adjacent paper, or a D-S/EvidentialRAG
comparison. A future study of any item requires a separately scoped protocol
and owner authorization.

## 18. Amendment change boundary and handoff

**[NON-ACTION]** This draft changes only this research-document lane. It does
not edit:

- the canonical v1.0 protocol;
- the F0/F1/F2 harness, generator, parser, scorer, schemas, or tests;
- the manuscript, site, glossary, framework map, or package manifest;
- model/provider configuration, credentials, IAM, schedulers, alerts, or data;
- T1 data, D-S/EvidentialRAG code, preregistration, publication, or release.

**[DRAFT DECISION]** Parent integration may quote the bounded wording and
record the gate decisions, but the parent must preserve this status until an
owner accepts a new locked version:

```text
V1.1 AMENDMENT: DRAFT, NON-AUTHORIZING
PROTOCOL: V1.0 CANONICAL UNTIL OWNER ACCEPTANCE
STATUS: COHERENT_PROTOCOL_NOT_EXECUTION_READY
FC_cons: CONSERVATIVE ASSERTED-COUNT-RISK COMPOSITE
VOR: SELECTED STIPULATED SUPPORT-ORIGIN COVERAGE THRESHOLD
DS/EvidentialRAG: DEFERRED, UNVERIFIED ADJACENT COMPARATOR
P0 GATES: OPEN UNTIL RECEIPTS EXIST
RUN: NOT AUTHORIZED
```

The required next step is owner review of this amendment’s proposed
interpretation and evidence contract, not a model invocation.

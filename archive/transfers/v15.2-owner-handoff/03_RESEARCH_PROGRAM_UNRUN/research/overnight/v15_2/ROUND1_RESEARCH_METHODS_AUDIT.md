# Round 1 research and methods audit — Pattern Map v15.2

**Lane:** independent research/methods red team
**Prepared:** 2026-08-19
**Worktree:** `/Users/gpt/Documents/Codex/worktrees/discrimination-layer-v15-2-overnight`
**Branch:** `codex/discrimination-layer-v15-2-overnight`
**Status:** `AUDIT_ONLY · NO STUDY RUN · NO MODEL/PROVIDER/NETWORK EXPERIMENT`

## TL;DR

**[OBSERVATION]** The package is now an unusually careful pre-run design package,
not a paper with results. The canonical protocol explicitly says that no model,
tokenizer, pilot, primary output, preregistration, or result exists
(`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:1-30`). The offline generator,
parser, fixed-denominator scorer, and regression suite are useful implementation
receipts; they are not evidence that a model can account for origins or that the
larger framework works.

**[INFERENCE]** The broad contribution claim does not survive the current prior
art. Provenance graphs, copying/dependence-aware fusion, claim/evidence graphs,
conflict-aware RAG, source attribution, evidence-use diagnostics, and metadata
bias studies already occupy the neighboring responsibility surface. The only
defensible residual is narrower:

> On newly authored fictional bundles with a stipulated origin graph, does one
> frozen model produce a different, lower *thresholded corroboration-risk event*
> when the same explicit counting rule is accompanied by visible typed relation
> values, under matched input resources and a fixed recall guardrail?

That is a useful measurement question if it is presented as a supplied-field
condition effect. It is not provenance discovery, real-world independence,
truth finding, semantic origin reasoning, better human decisions, or validation
of a general “discrimination layer.”

**[RECOMMENDATION]** Keep the current F2-versus-F1 core as a candidate diagnostic,
but do not open a pilot or preregister until four gates are closed: (1) choose
and validate the final interval method at `|M|=75`; (2) obtain actual selected-
model tokenizer/chat-template parity; (3) complete the blocked leakage and
semantic/stance audit; and (4) pre-specify how invalid outputs and incoherent
`origin_count_supporting`/`claim_state` pairs affect interpretation. The most
important conceptual change is to call the endpoint a corroboration-risk event,
not a direct measure of “false corroboration” or internal cue use.

## Scope, truth boundary, and non-actions

This lane independently audited the conceptual/research program as of
2026-08-19. It did not edit canonical source, site, protocol, schemas, tools,
or tests. It created only this audit and the companion source ledger.

The following boundary is frozen and is treated as an observation, not a
negotiable interpretation:

- no model has been selected or run;
- no provider, paid service, live retrieval, network experiment, participant
  study, preregistration, publication, deployment, or external transfer has
  occurred;
- synthetic generator relations are construction labels only;
- `INDP` means separately rooted **as stipulated in this benchmark**, not causal,
  epistemic, editorial, or real-world independence;
- `UNKN` is unresolved and is not evidence of zero or one origin;
- an offline harness proves code-path behavior only.

No command in this lane contacted a model, provider, network service, Cloud Run,
paid API, or external corpus. Current web checks were limited to reading primary
records for the source ledger; they are not study data.

## Inspection receipt

The following local artifacts were actually inspected. Line references are to
the v15.2 overnight checkout at audit time.

| Local artifact | What was checked | Finding |
| --- | --- | --- |
| `README.md:1-149` | Project purpose, canonical surfaces, current status, offline commands, authorization boundary | Correctly labels v15.1 as conceptual synthesis/unrun program and says no publication or push occurred. |
| `reports/overnight/v15_2/PROGRAM_CHARTER.md:1-110` | Overnight objective, frozen truth boundary, reader outcome, editorial/design/research gates, and parent integration rule | Used as this lane’s integration contract; it forbids study execution/publication and requires exact status, reader, design, and reproducibility boundaries. |
| `source/THOUGHT_PIECE_V15.md:1-660` | Thesis, worked “nine reports, one origin” example, prior-art boundary, protocol handoff, null/negative limits | Strongest public argument is the example and the insistence that recurrence is not independent support. Several research terms still risk being read more broadly than the protocol supports. |
| `source/FRAMEWORK_COMPONENT_MAP.md:1-374` | C01–C11 decomposition, typed distinctions, layer boundary, evidence maturity, open questions | Explicitly calls the map a conceptual synthesis rather than a validated or novel mechanism. The decomposition is useful as a design contract but has no ablation or practitioner evidence. |
| `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:1-612` | F0/F1/F2, corpus, endpoints, denominators, parity, power, shortcut suite, stop gates, T1, negative-result contract | Coherent pre-run skeleton with clear truth boundary. Final interval method, actual tokenizer, exhaustive leakage audit, and semantic audit remain open. `FC_cons` and VOR have construct-validity limitations recorded below. |
| `research/PAPER_PROSPECTUS_V1.md:1-403` | Residual contribution, title, estimand, paper architecture, status | Narrower than the thought piece, but “benchmark” and “uses a supplied field” can still imply a broader behavioral or reusable benchmark claim. |
| `research/F0_F1_F2_IMPLEMENTATION_READINESS_V1.md:1-404` | Implementation receipt, tests, controls, remaining gates, result commitments | Good separation of implementation readiness from empirical readiness; expressly says surrogate tokenizer and smoke diagnostics are non-authorizing. |
| `research/PRIOR_ART_DELTA_V1.md:1-517` | Existing source cards and status labels | Strong local source boundary, including Pochampally and Zhang. This audit adds current primary records and emphasizes that source status must remain visible in the first paper. |
| `research/overnight/01_THEORY_AND_PRIOR_ART_LUNA_MAX.md` | Earlier theory/prior-art synthesis | Correctly narrows the broad layer novelty claim and separates lineage, credibility, support, and selection. Treated as historical advisory work, not as a substitute for this pass. |
| `research/overnight/02_EMPIRICAL_RESEARCH_DESIGN_LUNA_MAX.md` | Earlier estimand/design proposals | Useful origin-accounting direction; current v1 protocol supersedes earlier versions. |
| `research/overnight/03_NEW_INSIGHTS_AND_VISUAL_OPPORTUNITIES_LUNA_MAX.md` | Research/tool-design opportunities | Receipt/schema opportunity is stronger than an additional atmospheric visual; visual work should not imply a proven algorithm. |
| `research/overnight/rounds/05_LOOP1_EMPIRICAL_RED_TEAM.md` | Empirical threats and construct concerns | Earlier concerns about oracle cues, invalids, shortcuts, and safety are preserved in v1. |
| `research/overnight/rounds/07_LOOP2_CURRENT_LITERATURE_EXPANSION.md` | 2024–2026 current-literature comparison | Strong close-work matrix; its status labels and bounded search language are retained. |
| `research/overnight/rounds/08_LOOP2_OPERATIONALIZATION_SPEC.md` | Operational definitions, diagnostics, release contract | Useful implementation detail; not treated as evidence of execution. |
| `research/overnight/rounds/10_LOOP3_ML_NLP_REVIEW.md` | ML/NLP overlap and shortcut critique | Supports the direct-code, metadata-bias, long-context, and one-model limits in this audit. |
| `reports/V15_LOOP2_METHOD_ADVERSARIAL_REVIEW.md` | Prior implementation defects | Important historical failure receipt; it was superseded by the fix validation. |
| `reports/V15_LOOP2_METHOD_FIX_VALIDATION.md:1-112` | Repairs for P1-01 through P1-07 and P2 defects | Passes the focused re-review, while explicitly leaving actual tokenizer parity, exhaustive leakage, semantic audit, and owner authorization open. |
| `tests/test_origin_accounting.py:1-485` | Offline regression coverage | 15 focused tests pass; tests establish local invariants, not model behavior. |

## 1. Exact residual contribution after prior-art review

### What is observed

**[OBSERVATION]** The public framework names an explicit responsibility for
keeping task, evidence, relation, assessment, action, human disposition, and
memory judgments inspectable (`source/FRAMEWORK_COMPONENT_MAP.md:38-60`). It
also states that this is not a mechanism-novelty claim or validated
implementation (`source/FRAMEWORK_COMPONENT_MAP.md:9-11`).

**[OBSERVATION]** The prospectus already rejects broad novelty language and
describes the candidate paper as a single supplied-field contrast
(`research/PAPER_PROSPECTUS_V1.md:52-110`). The canonical protocol fixes the
primary unit, `A=300`, `M=75`, F1/F2, all-assigned invalid coding, and the
synthetic/stipulated boundary (`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:14-77`).

**[OBSERVATION]** Primary records reviewed in this pass establish close
precedents:

- PROV-O supplies entities, activities, agents, derivations, attribution, and
  specialization as a formal provenance vocabulary.
- Zhang, Ives, and Roth define and infer provenance graphs for natural-language
  claims and evaluate them for claim verification.
- Pochampally et al. show that source correlation is broader than literal
  copying: common extraction rules can create positive correlation, while
  complementary coverage can create negative correlation.
- CONFACT evaluates RAG under conflicting evidence and source-credibility
  differences.
- Nematov et al. study document influence with Shapley-style attribution and
  explicitly evaluate redundancy, complementarity, and synergy (preprint).
- Xia proposes a matched four-condition evidence-utilization diagnostic and
  explicitly distinguishes observable condition behavior from internal causal
  attention (preprint).
- Abolghasemi et al. show that authorship metadata can change attribution
  behavior and trust, making metadata salience a competing explanation for any
  visible relation-cue effect.
- Laitenberger et al. show that a simple source-faithful baseline can match or
  beat more elaborate RAG systems under scaled token budgets, so complexity
  must earn its cost.
- Hagström et al. report that synthetic context can exaggerate utilization
  characteristics relative to retrieved real-world context.
- Li et al. study authority bias and credibility-aware conflict handling; this
  is adjacent but not the same as origin dependence.
- FaithfulRAG, TROVE, and GenProve provide current precedents for fact-level
  conflict or fine-grained provenance relations, while leaving upstream origin
  family as a separate question.

Primary URLs and status labels are in
`research/overnight/v15_2/ROUND1_RESEARCH_SOURCE_LEDGER.md`.

### What follows by inference

**[INFERENCE]** “A discrimination layer before generation” is not a residual
mechanism claim. It is a synthesis label for multiple established
responsibilities. The paper cannot obtain novelty by renaming provenance,
source dependence, evidence selection, conflict handling, attribution, routing,
or memory.

**[INFERENCE]** The strongest bounded residual is a *cue-conditioned diagnostic*:
same synthetic reports, same explicit rule, same output contract, same model,
same resources, and a visible relation field as the focal treatment. Even this
is not a clean-sheet design pattern; the contribution would be the precise
measurement contract and its negative controls, not the general idea that
models may respond to structured context.

**[INFERENCE]** The paper’s narrow claim should avoid “the model used metadata.”
The estimand identifies an output difference between conditions. It cannot
identify internal representation, causal attention, semantic comprehension,
or a provenance-discovery process.

### Strongest counterarguments

1. **“This is old work under a new label.”** Mostly correct for the broad map.
   The response is to lead with a bounded design and an exact residual test,
   not to defend universal architectural novelty.
2. **“F2 may count a field, not understand reports.”** Directly plausible.
   The metadata-only and field-only diagnostics are therefore interpretation
   gates, not decorative extras.
3. **“The graph gives the model the answer.”** Correct in the limited sense that
   F2 receives oracle/stipulated relation values. That is the treatment, not a
   provenance-discovery result.
4. **“Synthetic reports are too clean.”** Plausible and supported by current
   context-utilization work. The synthetic study can establish a bounded
   diagnostic only; natural-news T1 is a separately authorized, rights-gated
   descriptive transfer, not a rescue arm.
5. **“Source dependence is not binary.”** Correct. Copying, common extraction,
   shared evidence, institutional coordination, complementary scope, and
   temporal drift are different relations. The three protocol codes are
   acceptable only as narrow benchmark states.
6. **“A model can lower false corroboration by suppressing all counts.”** The
   VOR gate blocks the most obvious zero-everything strategy, but it does not
   require exact count or support-origin-set fidelity. A positive result can
   still be a threshold policy rather than origin accounting.
7. **“An invalid output is not a false-corroboration claim.”** Correct. The
   all-assigned conservative coding is a legitimate safety-risk estimand, but
   it is a composite of semantic overcount risk and output validity. Any effect
   must be decomposed before being narrated as a cue effect.

## 2. Operationalization and construct validity

### 2.1 The relation field is intentionally narrow, but the public language is wider

**[OBSERVATION]** The protocol separates derivation, origin relation, claim
stance, and action (`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:152-166`).
It defines `DPND`, `INDP`, `UNKN`, and `NONE` and says the origin graph is
construction truth only (`:137-157`, `:208-231`). This is a strong boundary.

**[INFERENCE]** The field is not a general “provenance” field. It is a
report-level, visible cue encoding a benchmark relation. A positive effect
would not show that the model can infer origin, resolve partial copying,
recognize common extraction pipelines, or reason over relation direction,
scope, time, confidence, or relation evidence.

**[RECOMMENDATION]** Use “stipulated origin-relation cue” in all scientific
artifacts. Reserve “provenance” for the graph/lineage record and say “oracle”
whenever a prompt exposes the relation value. Keep the broader “discrimination
layer” phrase as historical thought-piece framing only until reader and
construct evidence justify more.

### 2.2 `FC_cons` is a safety-risk composite, not a pure false-corroboration measure

**[OBSERVATION]** The protocol defines `FC_cons=1` for every invalid output and
for a valid output with `origin_count_supporting >= 2` on `none`, `single`, or
`unknown` certainty (`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:300-320`).
The implementation matches this at `tools/origin_accounting/analysis.py:122-145`.
The protocol reports invalid rates and liberal/complete-case sensitivities but
does not make invalid-rate parity an interpretation gate (`:381-411`).

**[INFERENCE]** A favorable F2-minus-F1 delta can arise from any mixture of:

- fewer semantically over-large counts;
- fewer parser-invalid outputs;
- a condition-specific formatting or compliance change;
- a model learning to output a low safe count without using report content.

This does not make `FC_cons` wrong. It means the maximum claim is a composite
risk reduction unless the invalid component is separately bounded.

**[RECOMMENDATION]** Keep all-assigned `FC_cons` as the locked safety-oriented
primary if the owner wants it, but add a pre-registered interpretation gate:
report paired invalid-rate difference and a two-by-two decomposition of
`valid`, `FC_obs`, and `FC_cons`; do not call a result “typed origin-cue value”
if the FC delta is explained by a material parseability difference. Treat
`FC_lib` and complete-case results as declared sensitivities, not a choice after
results. Acceptance is a receipt with: (a) invalid counts by reason and
condition, (b) invalid-only delta, (c) valid-only overcount delta, and (d) a
locked narrative rule for discordant combinations.

### 2.3 Count and claim stance are syntactically separate but semantically coupled

**[OBSERVATION]** The required JSON has `origin_count_supporting`,
`claim_state`, `confidence`, and `evidence_ids` (`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:208-232`).
The parser checks types and allowed values, but `score_output` marks
`FC_obs` using only validity, the count, and gold certainty; it does not use
`claim_state` or selected evidence for the primary event
(`tools/origin_accounting/analysis.py:122-145`).

**[INFERENCE]** A formally valid output can say `claim_state="refuted"` while
asserting `origin_count_supporting=4`, and that output still triggers the
corroboration-risk event. This may be intentional if the endpoint is “asserted
count field,” but it is not the same construct as a model asserting supporting
corroboration. Likewise, a model can emit a count inconsistent with its
selected evidence IDs, and the primary endpoint will not notice.

**[RECOMMENDATION]** Before preregistration, choose one of two explicit
interpretations:

1. **Field-risk interpretation (minimal change):** rename the event in prose to
   `conservative asserted-count risk`, retain the current formula, and make
   count/stance/evidence coherence a descriptive diagnostic; or
2. **Claim-corroboration interpretation (stronger construct):** add a frozen
   secondary event requiring `claim_state="supported"` and selected support
   evidence consistent with the count, while keeping the all-assigned event as
   a safety sensitivity.

Do not silently use one interpretation in code and another in the abstract.
Add fixtures for contradictory count/stance/evidence combinations and assert
the chosen status. A result cannot support “the model recognized
corroboration” if the model never had to make a coherent claim/evidence
assertion.

### 2.4 VOR is a threshold safety gate, not exact origin accounting

**[OBSERVATION]** `VOR` passes when the output is valid, the count is at least
two, and selected support-side evidence contains at least two distinct
stipulated origins (`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:322-335`).
Absolute count error and support-origin set precision/recall/exact match are
descriptive only (`:337-373`).

**[INFERENCE]** A model can pass VOR by always emitting `2` for a multiple-origin
bundle, even when the stipulated count is `3`, and can avoid a false-corroboration
event on one-origin/unknown rows by emitting `1`. That policy may be a valid
conservative threshold strategy, but it does not demonstrate accurate origin
counting or relation integration. The present protocol can answer a narrower
question about risk/recall trade-off, not “did the model account for origins?”

**[RECOMMENDATION]** Retain VOR as a guardrail but state its threshold nature in
the title, abstract, and result table. Require a descriptive `count_error`,
selected-origin-set exact match, and a count-vs-stance coherence panel for all
valid certified rows. If the owner wants the phrase “origin accounting,” define
an additional, separately labeled fidelity endpoint in a future protocol; do
not promote the current VOR pass into that claim.

### 2.5 The corpus cannot test wrong origin assignments

**[OBSERVATION]** The protocol explicitly says that all supporting reports are
members of the restricted support set and therefore does not emit a
wrong-stipulated-origin metric (`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:370-373`).

**[INFERENCE]** Selected-support-origin recall measures omission and set coverage
only. It cannot distinguish a model that correctly selected the right origins
from one that selected a fabricated support report whose origin happens to be
in the gold support set, because the current generator does not include a
wrong-support-origin fixture. This is acceptable for the narrow threshold
diagnostic but blocks stronger claims about evidence selection or origin
assignment.

**[RECOMMENDATION]** Keep the current fixture contract for v1.0 if changing it
would reopen the study. Add a P1 diagnostic in the next protocol: include
certified distractor reports with non-supporting stance and/or deliberately
misassigned origin metadata in a separate stress corpus, score false-origin
credit and support-set precision, and keep it outside the first confirmatory
family. Until then, say “selected stipulated support-origin coverage,” not
“origin assignment accuracy.”

## 3. F0/F1/F2 design and estimand

### What is good and should remain

**[OBSERVATION]** F1 and F2 receive the same explicit rule bytes; F1 has `NONE`
slots and F2 has visible `DPND`/`INDP`/`UNKN` values. The model does not receive
gold structure, origin IDs, split labels, or gold counts
(`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:214-248`). The builder
recomputes local payload hashes and ordered report hashes
(`tools/origin_accounting/generator.py:629-749`).

**[INFERENCE]** This is the right causal contrast for the narrow question: the
relation field is the focal change. F0 is useful as a secondary ordinary
baseline, but it must not be used to make the F2-versus-F1 effect look larger.

**[RECOMMENDATION]** Preserve the F2-versus-F1 core, fixed all-assigned `A`,
fixed `M`, explicit `UNKN`, T1 firewall, and no-peeking rule. Keep F0, claim
state, confidence, structure, style, order, stress, and optional-model slices
descriptive as the protocol currently states (`:406-411`).

### Remaining design risks

1. **The treatment is highly visible.** Four-letter codes are intentionally
   exposed in a fixed metadata table. A model can count `INDP` tokens without
   reading the reports. This is not a flaw in the intervention; it bounds the
   interpretation to visible-code behavior.
2. **One model means one configuration.** Even a clean result is model-, prompt-,
   tokenizer-, decoding-, and generator-specific. A second model is a robustness
   check unless the study is re-powered and the inferential unit is redesigned.
3. **The relation field may be a general authority/status cue.** Abolghasemi
   and Li show that metadata can alter attribution or trust. Codebook permutation,
   neutral labels, relation position, and evidence masking are needed to
   separate relation semantics from metadata salience.
4. **Cross-structure differences are not counterfactual pairs.** The protocol
   correctly treats the four structures as balanced strata. Never describe them
   as matched pairs in a paper or handoff.
5. **Unknown-origin rows are deliberately conservative.** A valid output of two
   or more on `UNKN` is a risk event; this is a policy choice under unresolved
   information, not a claim that the latent bundle has at most one origin.

## 4. Denominators, N=300, and power logic

### Fixed denominators are a strength

**[OBSERVATION]** The repaired scorer requires a hash-locked ordered manifest of
exactly 300 primary rows and 75 multiple-certainty safety rows in confirmatory
mode (`tools/origin_accounting/analysis.py:364-423`; test coverage at
`tests/test_origin_accounting.py:415-433`). Invalid outputs remain in the
assigned denominator. The repair validation reports that smoke mode is now
separately named and cannot masquerade as confirmatory analysis
(`reports/V15_LOOP2_METHOD_FIX_VALIDATION.md:29-39`).

**[INFERENCE]** This closes the earlier denominator failure. It does not make
`N=300` intrinsically adequate: paired McNemar information is determined by the
number and dependence of discordant pairs, and VOR precision is determined by
`|M|=75` and the paired safety pattern. The protocol’s grid correctly treats
baseline risk, discordance, delta, invalid rate, and invalid coding as planning
inputs (`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:413-445`), but no final
operating-characteristic receipt is present in the package.

**[RECOMMENDATION]** Treat `N=300` as a candidate, not a result. Before
preregistration, produce a versioned simulation receipt that:

- uses the exact final primary decision (paired exact test plus the declared
  interval rule), not only a p-value;
- includes type-I error at delta zero, power at the candidate `-0.08`, and
  coverage at all planned invalid rates;
- varies paired invalid dependence, not only independent invalid draws;
- reports the number of discordant pairs and the operating range in which a
  nominal `N=300` can detect the effect;
- validates the fixed-`M` one-sided interval at `|M|=75`, especially at the
  `-0.05` boundary and under high/low baseline VOR; and
- freezes the interval method and interpretation before any model output is
  opened.

The current `tools/origin_accounting/power.py:44-115,150-250` is explicitly a
planning scaffold. The reduced smoke command in the fix validation used tiny
repetition/resample counts and `vor_n=10`, so it cannot be cited as power or
coverage (`reports/V15_LOOP2_METHOD_FIX_VALIDATION.md:64-68`).

### Composite invalid coding needs a second power axis

**[INFERENCE]** Independent invalid-rate perturbation in the planning helper is
useful for sensitivity, but real invalidity can be correlated within a bundle:
the same chat template, output cap, tokenizer, or model behavior may make both
conditions invalid. Correlation changes discordance and therefore McNemar
operating characteristics. A final grid should include paired invalid
correlation or explicit worst/best-case bounds.

**[RECOMMENDATION]** If invalid outputs remain `FC_cons=1`, pre-specify a
parseability adequacy rule: for example, no efficacy interpretation when the
condition invalid-rate difference exceeds a frozen threshold, while still
reporting the all-assigned risk result. The exact threshold is an owner/method
decision; what must not happen is deciding after seeing whether invalidity
helped F2.

## 5. Tokenizer parity and resource control

**[OBSERVATION]** The local builder proves only deterministic-regex surrogate
parity. The protocol requires exact equality under the selected model’s actual
tokenizer and exact backend chat-template rendering before opening the primary
split (`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:233-269`). The fix
validation explicitly leaves those gates open (`reports/V15_LOOP2_METHOD_FIX_VALIDATION.md:84-103`).

**[INFERENCE]** Equal UTF-8 bytes and equal surrogate token counts are necessary
but not sufficient. Relation codes may have different tokenization in a chosen
model; padding can change attention patterns; chat templates can add special
tokens; output length limits can interact with visible relation text; and
equal-input token counts do not remove semantic salience or position effects.

**[RECOMMENDATION]** Require a final parity receipt with exact model/checkpoint/
tokenizer revisions, chat-template bytes, rendered system/user/final-input
hashes, input-token counts, output cap, and no-retry policy. Add an invariance
test that swaps relation-code labels while preserving code length and confirms
the receipt still reports exact resource parity. Keep byte parity as a separate
resource check; never present it as evidence of semantic equivalence.

## 6. Shortcut, leakage, and contamination audit

### Existing controls to keep

**[OBSERVATION]** The protocol names opaque IDs, crossed style/length/position/
domain, low-overlap dependent versus high-overlap distinct-as-stipulated
reports, split blocking, codebook permutation, metadata-only and field-only
diagnostics, relation noise, and an independent semantic audit
(`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:447-464`). The repaired suite
also preserves an explicit non-authorizing leakage precheck
(`tools/origin_accounting/diagnostics.py:30-83`; `tests/test_origin_accounting.py:43-60`).

### Open controls that block the study

**[OBSERVATION]** No complete blocked character/token TF-IDF classifier with a
frozen ceiling and Wilson interval, no full independent semantic/stance/
transformation audit, no selected-model field-only run, and no actual
codebook-permutation/model diagnostic is present. The package says so directly
(`research/F0_F1_F2_IMPLEMENTATION_READINESS_V1.md:237-263,330-347`).

**[INFERENCE]** The deterministic smoke corpus can be trivially classified by
structure, as the protocol warns. That is not evidence of a broken primary
corpus yet, but it is evidence that the cheap smoke result cannot authorize a
primary run. Surface leakage is especially dangerous because `origin_structure`
is the latent label and the generator uses hand-authored templates.

**[RECOMMENDATION]** Freeze and publish a control matrix before the model is
selected:

| Control | What it distinguishes | Required interpretation |
| --- | --- | --- |
| Codebook permutation | Relation semantics versus token/label identity | If effect follows token identity, it is a label shortcut. |
| Field-only / masked reports | Direct code count versus report integration | If effect survives report masking, do not call it semantic integration. |
| Relation position/order swap | Cue location and serial-position effects | Position-fragile effect is a formatting/attention result. |
| Low-overlap dependent / high-overlap distinct | Similarity heuristic versus relation cue | A similarity-only model is not using the stipulated relation field. |
| Held-out-family TF-IDF/character probe | Split/template leakage | Above-frozen ceiling quarantines the corpus. |
| Relation noise | Oracle fragility | Noise-fragile result is an oracle upper bound, not robust origin accounting. |
| Independent semantic audit | Generator stance/transformation correctness | Disagreement requires quarantine/adjudication before any run. |

No one control proves semantic reasoning. Together they limit the claims that
can be made from a condition difference.

## 7. Feasible offline experiments and future authorized program

### Safe offline work now (no model/provider/network)

The following can advance without crossing the authorization boundary:

1. Regenerate the full 480-bundle corpus and verify all hashes, graph edges,
   support/refute sets, split membership, and exact primary manifest.
2. Complete an independent blocked character/token leakage precheck and label
   it `clearance_unresolved` until the pre-registered classifier and thresholds
   are implemented.
3. Build a human-readable semantic audit packet for a prespecified sample of
   bundle/structure/style/position cells, with transformation and stance
   decisions independently adjudicated.
4. Add offline fixtures for incoherent count/stance/evidence combinations and
   for invalid-output decomposition. These are parser/scorer tests, not model
   results.
5. Run planning simulations only after the final analysis rule is chosen. Keep
   outputs labeled planning-only and record the exact seed, grid, resampling,
   and interval method.
6. Reconcile the source ledger and bibliography statuses. Do not claim an
   exhaustive review or “first” result.

### Future authorized empirical sequence

This sequence requires explicit owner authorization at each gate:

| Stage | Authorized action | Exit evidence | What it still cannot establish |
| --- | --- | --- | --- |
| 0. Lock | Choose the bounded claim, endpoint language, interval method, model/checkpoint/tokenizer, and budget | Signed/dated protocol and manifest with no open P0 | Any model effect |
| 1. Feasibility | Run the 40-bundle pilot under frozen prompts and no primary IDs | Parseability, runtime, receipt, shortcut, and semantic-audit results; no efficacy estimate | Generality or efficacy |
| 2. Primary diagnostic | Run one frozen model on 300 fixed bundles, F1/F2, with all raw outputs | Complete paired result, invalids, safety gate, controls, and negative-result record | Provenance discovery, truth, human benefit, transfer |
| 3. Robustness | Only if pre-specified or separately authorized, test another model/configuration | Model-specific replication or instability receipt | Pooled generalization unless powered/redesigned |
| 4. Transfer | Only after primary lock and rights/annotation review, build T1 descriptive adapter | Rights receipt, relation-label provenance, transfer diagnostics | Real-world independence or primary efficacy |
| 5. Human/tool study | Separate reader/correction/routing study with its own task, outcomes, ethics, and power | Correction, reliance, workload, or decision-quality evidence | Automatic validation of the conceptual map |
| 6. Later relation inference | Study noisy/partial/dynamic origin discovery with external data only after authorization | Relation-inference accuracy and uncertainty | Safety or truth from lineage alone |

Do not jump from Stage 2 to product, deployment, human utility, or the eleven-
responsibility framework. A null or harmful Stage 2 result stops escalation from
this cue mechanism but does not invalidate unrelated conceptual distinctions.

## 8. Null, negative, harmful, and shortcut commitments

**[OBSERVATION]** The protocol’s retirement table is unusually strong: null,
harmful, VOR-failing, direct-code, surface, noise-fragile, unstable, and
non-transporting results each have a named disposition
(`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:535-552`). The readiness memo
also preserves the owner-approved interpretation (`research/F0_F1_F2_IMPLEMENTATION_READINESS_V1.md:353-371`).

**[INFERENCE]** The commitment is credible only if the paper preserves raw
outputs, invalids, failed controls, and stopped runs in the release receipt. A
positive-only table can still be created accidentally if invalid-rate effects,
count/stance incoherence, or unpowered model slices are relegated to a footnote.

**[RECOMMENDATION]** Add a result-class row for each newly identified failure:

- **Invalidity-driven delta:** if F2’s apparent improvement is mostly a
  parseability change, report a composite-risk result and do not call it a
  semantic cue effect.
- **Count/stance incoherence:** if the effect appears only in contradictory
  structured outputs, report field behavior and retire the stronger construct.
- **Threshold-only success:** if VOR passes but exact count/set fidelity does
  not, report a risk/recall threshold result, not origin accounting.
- **Synthetic-only success:** if T1 fails or is unavailable, keep the synthetic
  result bounded and do not write “works on news” or “real-world corroboration.”

## 9. Opportunities that improve both thought piece and tool design

### Keep

- The concrete “nine reports, one origin” example and the rule “preserve all
  observations; do not multiply their origins.”
- The explicit distinction among recurrence, authority, support, relevance,
  action priority, and owner disposition.
- `UNKN` as a visible state rather than a forced independent/dependent choice.
- The static receipt as an inspectable artifact, clearly labeled as an
  illustration/harness output rather than a workflow or empirical result.
- The historical v13 map as a historical anchor, not evidence of current
  mechanism validity.
- The negative-result and retirement contract.

### Cut or demote

- “Controlled false-corroboration benchmark” until the artifact is genuinely
  reusable across models/tasks; “frozen-model diagnostic” is more accurate now.
- Any phrase saying a model “used” or “understood” origin metadata. Use
  “produced a condition-sensitive output difference.”
- Any scientific title that presents “discrimination layer” as a universal
  architecture. Keep the historical title in the thought piece, and use
  “stipulated origin-relation cue” for the methods branch.
- Visual topology that looks like a one-way gatekeeper or truth filter. The
  current package already demotes the evidence-aperture visual; preserve that
  decision.
- Any claim that a provenance record itself proves truth, source authority,
  permission, or independence.

### Add

1. **Relation record, not master score.** For each relation, expose type
   (`derivation`, `origin`, `stance`, or `action`), direction, scope, capture
   time, confidence/uncertainty, evidence for the relation, and who/what
   supplied it. This directly answers Pochampally’s broader-correlation warning
   without changing the first diagnostic’s three codes.
2. **Decision delta panel.** Show what a rule-only system would do, what the
   typed-cue system would do, and what remains unknown. Do not present the
   difference as truth; present it as a traceable action/attention consequence.
3. **Coherence receipt.** Display count, claim stance, selected evidence, support
   origins, invalid status, and relation confidence together so a reviewer can
   see when a model’s fields disagree.
4. **Uncertainty affordance.** “Unknown origin” should be actionable: hold,
   seek a documented distinct-origin test, or answer with a caveat. It should
   never render as a hidden zero.
5. **Complexity budget.** Every added relation/graph/router field should state
   what decision it changes and what it costs in tokens, latency, reviewer
   minutes, or disclosure risk. Laitenberger’s simple-baseline result makes
   this a necessary design test.
6. **Provenance of the relation itself.** A relation supplied by a benchmark
   oracle, inferred by an algorithm, copied from a source, or corrected by a
   human should not share one visual style.

## 10. Readiness verdict and priority backlog

### Direct verdicts

| Question | Verdict |
| --- | --- |
| Broad “new discrimination layer” novelty | **Reject.** It is a synthesis/design framing with extensive prior art, not a demonstrated mechanism. |
| Narrow residual contribution | **Conditional.** A frozen-model, supplied-field cue-use/corroboration-risk diagnostic may be worthwhile if controls pass. |
| Current research status | **Coherent protocol, not execution-ready.** |
| Current thought-piece status | **Ready for owner review as a bounded conceptual synthesis**, subject to terminology and status honesty. |
| N=300 | **Candidate only.** Adequacy depends on paired discordance, invalid dependence, and fixed-M safety precision. |
| VOR | **Useful threshold guardrail, not exact origin-accounting evidence.** |
| T1 | **Descriptive future transfer only, rights and annotation gated.** |
| Should a model run occur now? | **No.** P0 gates remain open and no current user authorization for a study run exists. |

### P0 — blocks a useful scientific handoff or any model/pilot opening

| ID | Evidence/location | Failure caused | Concrete change | Acceptance test | Scope | Regression risk |
| --- | --- | --- | --- | --- | --- | --- |
| P0-01 | `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:300-320`; `tools/origin_accounting/analysis.py:122-145` | `FC_cons` combines invalidity and asserted overcount; a condition effect can be misnarrated as semantic cue use. | Freeze the event name as “conservative asserted-count risk” or add an explicit interpretation gate requiring invalid-rate decomposition and a valid-only sensitivity. | Synthetic fixtures where only invalidity changes, only count changes, and both change produce distinct receipt rows and locked interpretations. | Moderate | Medium: changing wording/receipt fields can create version drift. |
| P0-02 | `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:398-445`; `tools/origin_accounting/power.py:44-250` | `|M|=75` safety interval and `N=300` operating characteristics are not yet validated under the final decision rule. | Freeze the final one-sided VOR interval, simulate exact primary and safety decisions at 10,000 repetitions/cell, and include paired invalid dependence. | Versioned receipt reports type-I error, power, interval coverage, discordance, invalid correlation, and gate probability at `|M|=75`; no model output used. | Moderate | Low: analysis semantics should not change, but intervals may alter readiness. |
| P0-03 | `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:233-269`; `reports/V15_LOOP2_METHOD_FIX_VALIDATION.md:84-103` | Surrogate parity could be mistaken for model-resource parity; chat-template effects remain untested. | Select model/checkpoint/tokenizer only with owner authorization; render exact backend prompts and record all hashes/counts before opening `A`. | Every F1/F2 pair has identical selected-tokenizer input counts, byte receipt, chat-template receipt, report hashes/order, output cap, and fail-closed mismatch test. | Moderate | Medium: model choice can expose new token/format drift. |
| P0-04 | `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:175-189,447-464`; `research/F0_F1_F2_IMPLEMENTATION_READINESS_V1.md:330-347` | Smoke diagnostics do not establish leakage clearance or semantic validity. | Complete the blocked held-out-family lexical probe, codebook/position/field-only controls, and independent semantic/stance/transformation audit with frozen ceilings and adjudication. | Primary-lock receipt has no unresolved cross-split exact/near duplicates, classifier below frozen ceiling, zero semantic invariant failures, and signed audit/quarantine reasons. | Structural | Medium: fixture repair may require a new protocol version. |
| P0-05 | `research/PAPER_PROSPECTUS_V1.md:14-50,101-110` | “Benchmark,” “uses metadata,” and “origin accounting” invite claims beyond the actual oracle/threshold test. | Rename the scientific artifact to “frozen-model diagnostic” unless a reusable multi-model benchmark is released; use “observable condition effect” everywhere. | Claim-source lint finds no internal-use, discovery, real-independence, truth, human-benefit, or general-layer wording in title/abstract/conclusion. | Surgical | Low: improves rather than changes the estimand. |
| P0-06 | `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:208-232`; `tools/origin_accounting/analysis.py:122-145` | A valid but incoherent count/stance/evidence object can pass the primary event without specifying which construct is measured. | Freeze field-risk versus claim-corroboration interpretation; add contradictory-output fixtures and a coherence diagnostic. | Parser/scorer tests cover count=4 with `refuted`, count=0 with `supported`, and count/evidence mismatch; result narrative follows the frozen rule. | Moderate | Medium: adding a diagnostic can reveal that the current estimand is narrower than named. |

### P1 — required before public research handoff or a stronger paper claim

| ID | Evidence/location | Failure caused | Concrete change | Acceptance test | Scope | Regression risk |
| --- | --- | --- | --- | --- | --- | --- |
| P1-01 | `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:137-166`; Pochampally source card in ledger | Three relation codes flatten dependence type, direction, scope, time, and uncertainty. | Keep v1 codes narrow, but add a future relation-object contract and name all relation provenance/status fields. | Example records distinguish derivation, origin, stance, and action relations and visibly mark oracle/inferred/human status. | Moderate | Low if kept outside v1 confirmatory fields. |
| P1-02 | `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:337-373` | No wrong-origin assignment fixture; selected-origin metrics are omission/coverage only. | Add a separate stress corpus with certified distractor/misassigned-origin cases; keep outside the first confirmatory family. | Scorer reports false-origin credit and support-set precision without altering `FC_cons`, `VOR`, `A`, or `M`. | Structural | Medium: generator contract expansion. |
| P1-03 | `research/overnight/rounds/07_LOOP2_CURRENT_LITERATURE_EXPANSION.md`; `research/REFERENCES.md`; `research/references.bib` | Current close work can be status-confused or omitted at submission. | Add/verify Zhang, Pochampally, CONFACT, Xia, Nematov, Abolghasemi, Li, Laitenberger, Hagström, FaithfulRAG, TROVE, and GenProve with peer-reviewed/preprint labels. | Markdown/Bib/source ledger agree on title, authors, venue/status, URL, and exact supported/blocked claim. | Surgical | Low. |
| P1-04 | `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:519-533`; `research/REAL_SYNDICATION_TRANSFER_FEASIBILITY_V1.md` | T1 could be read as natural-world proof despite incomplete stance/origin labels and rights. | Keep T1 descriptive, require rights/version/annotation receipts, and never map nonduplicates or cluster size to `INDP`. | T1 manifest cannot enter `A`, `M`, McNemar rows, VOR, or primary effect; unresolved rights fail closed. | Moderate | Low. |
| P1-05 | `source/THOUGHT_PIECE_V15.md:320-389`; `source/FRAMEWORK_COMPONENT_MAP.md:289-359` | Public conceptual prose can drift from “relation under rule” into “independent support” or a master ranking. | Add visible first-use caveats and keep typed distinctions in the body, not only glossary/popups. | A cold reader can restate recurrence, origin relation, support, authority, and action as different judgments without reading research appendix. | Moderate | Medium: terminology change may require a new owner review pass. |
| P1-06 | `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:250-269`; readiness memo | One-model result can be overgeneralized to “models” or deployment. | Put one-model/task/prompt/synthetic qualifiers in title, abstract, result headings, and conclusion; treat second model as unpowered robustness unless redesigned. | Text audit has no unqualified plural model/transfer/utility claim; optional model cannot change confirmatory inference. | Surgical | Low. |
| P1-07 | `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:554-575` | Local receipts may be treated as release-grade canonicalization or provenance. | Run independent RFC 8785 conformance and external schema validation only before any authorized release; preserve `deterministic-json-v1` status now. | Unicode, nested-map, array, number, negative-zero, raw-byte/hash, and schema conformance fixtures pass in a release receipt. | Moderate | Low. |

### P2 — later expansion, not required to review the current thought piece

| ID | Future question | Proposed bounded work | Exit evidence |
| --- | --- | --- | --- |
| P2-01 | Can noisy/partial origin relations be inferred rather than supplied? | New study with relation uncertainty, direction, time, common extraction, and human adjudication; separate from F2/F1. | Relation precision/recall/calibration and error taxonomy on authorized corpus. |
| P2-02 | Does a receipt improve human correction or decisions? | Independent HCI/correction study with task outcomes, workload, reliance, accessibility, ethics, and power. | Pre-registered correction/decision outcomes; no inference from model-only F2. |
| P2-03 | Does typed context alter acquisition/stopping/action routing? | Separate action-policy study with value-of-information, cost, authorization, abstention, and human disposition endpoints. | Matched-budget action/utility/abstention result or null. |
| P2-04 | Does origin-bound memory prevent laundering across summaries? | Security/lineage study with authenticated relation provenance and memory poisoning controls. | Attack/defense evaluation; do not conflate with benign provenance logging. |
| P2-05 | Is “discrimination layer” the right public name? | Reader terminology test against “context judgment,” “evidence-selection,” and “origin accounting.” | Restatement/abandonment/error results with accessibility and social-sensitivity review. |
| P2-06 | Can this become a reusable benchmark? | Multi-model, multi-task dataset card, codebook, licensing, baseline, and contamination plan. | Reusable release with stable task semantics; until then call it a frozen-model diagnostic. |

## 11. Bounded integration brief for the parent

Merge the following points into the overnight convergence record; do not merge
canonical site or research-source edits from this lane:

1. **Status:** `COHERENT_PROTOCOL_NOT_EXECUTION_READY`. The code and tests are
   implementation evidence only; no study or model result exists.
2. **Residual claim:** “A visible, benchmark-stipulated origin-relation cue may
   change a frozen model’s thresholded corroboration-risk output beyond an
   explicit rule under matched resources.” This is a condition effect, not
   internal cue use, provenance discovery, real independence, truth, utility,
   or broad layer validation.
3. **Keep:** the nine-reports/one-origin example, explicit unknown state,
   relation/stance/authority/support/action distinctions, T1 firewall, fixed
   denominators, and negative/harm/shortcut commitments.
4. **Do not overclaim:** `FC_cons` is a conservative risk composite; VOR is a
   threshold guardrail; selected-origin metrics omit wrong-origin fixtures;
   `N=300` and `|M|=75` are candidates awaiting operating-characteristic proof;
   local surrogate parity is not model-tokenizer parity.
5. **Round-2 priority:** close P0-01 through P0-06 in a new lock receipt before
   any pilot authorization. The parent may improve thought-piece wording and
   design now, but should not launch a model run from this audit.
6. **Design opportunity:** make the receipt a visible “decision delta” and
   relation-status record, not a truth filter or one-way gate. Clearly mark
   oracle, inferred, human-corrected, and unresolved relations.

### Suggested one-paragraph handoff language

> The research branch is a pre-run, frozen-model diagnostic proposal. Its only
> residual question is whether supplied, benchmark-stipulated origin-relation
> codes alter a model’s conservative asserted-count risk beyond the same
> explicit counting rule. The package does not infer provenance or establish
> real-world independence, truth, human benefit, or framework validity. Before
> any authorized pilot, the team must freeze and validate the `|M|=75` safety
> interval, selected-model tokenizer/chat-template parity, blocked leakage and
> semantic audits, invalid-output interpretation, and count/stance/evidence
> coherence. A null, harmful, threshold-only, invalidity-driven, direct-code, or
> noise-fragile result remains a first-class outcome.

## 12. Local validation of this lane

Checks run after creating the two lane files:

```text
python3 -m unittest discover -s tests -p 'test_*.py' -v
PASS — 15 tests; no model/provider/network calls

python3 -m compileall -q tools/origin_accounting tests
PASS

git diff --check
PASS
```

The checks validate the pre-existing offline implementation and Markdown
patch cleanliness. They do not validate a model, power, provenance discovery,
or any empirical claim.

# V15 loop 2 method/adversarial review

- **Reviewed checkout:** `/Users/gpt/Documents/Codex/worktrees/discrimination-layer-v15-loop2`
- **Reviewed branch:** `codex/discrimination-layer-v15-loop2-review`
- **Reviewed base:** `6423a43e1a0f0d0b6b4dd021d5035a767426307c`
  (`Record v15 reader integration gate`)
- **Review date:** 2026-08-18
- **Scope:** frozen v15 protocol, prospectus, readiness memo, schemas,
  synthetic generator, prompt builder, parser, scorer, diagnostics, power
  scaffolding, tests, manuscript, reader, matrix, and decision ledger
- **External effects:** none. No model, provider, network, Cloud Run, paid
  service, external corpus, or site build dependency was called.

## Verdict

**FAIL for adversarial implementation readiness / pre-pilot opening.** The F2-minus-F1 estimand, conservative invalid-output coding, the intended F0/F1/F2 conceptual isolation, T1 firewall, and owner-approved negative-result commitment are present. However, the current implementation does not fail closed on several conditions that can change the analyzed set or the treatment contrast:

- unknown-origin relation-noise stress violates the explicit all-`UNKN` rule;
- the analysis accepts a smoke/non-primary set as the confirmatory `A` and derives `M` from whatever gold rows the caller supplies;
- prompt parity validation accepts mutated F1/F2 system or user text and treats an evidence-byte receipt as a hard-coded boolean;
- corpus validation accepts tampered report text/hash and report/gold cross-record links;
- the planning simulation does not implement the required VOR grid and does not simulate the declared FC bootstrap decision;
- raw-output receipts can be constructed with a hash from a different byte string; and
- the CLI/receipt version identity is stale or ambiguous relative to canonical protocol v1.0.

No P0 was found because no primary split or model run occurred and no external data were touched. The P1 defects below are nevertheless release-blocking before any pilot/primary opening. They do not require changing the F2-F1 estimand; they require implementation, receipt, and gate corrections. The review found two P2 documentation/diagnostic weaknesses and lists the remaining run gates separately.

## Commands and observed results

All commands below were run from the reviewed worktree with Python 3 and no network access.

| Check | Exact command | Result |
| --- | --- | --- |
| Focused offline tests | `python3 -m unittest discover -s tests -p 'test_*.py' -v` | **PASS** — 7 tests |
| Python compilation | `python3 -m compileall -q tools/origin_accounting` | **PASS** |
| Strict parser fixtures | `python3 -m tools.origin_accounting.cli parser-fixtures` | **PASS** — 18/18 fixtures |
| Offline smoke | `python3 -m tools.origin_accounting.cli smoke --out "$TMPDIR"` | **PASS as smoke only** — 16 bundles, 48 prompts, 0 model/provider/network calls; split leakage `pass`; surface probe accuracy 1.0, correctly not a clearance gate |
| Power smoke | `python3 -m tools.origin_accounting.cli power --out "$TMPDIR" --repetitions 1` | **PASS as execution smoke only** — 720 FC cells emitted; no VOR grid emitted. The default 10,000 repetitions were not run because this grid is computationally large; this is not a model/network limitation. |
| Full synthetic generation | Inline Python: `generate_corpus(FrozenConfig(), small=False)` followed by `build_prompt_instances` and `split_leakage_report` | **PASS for generation/precheck** — 480 bundles, 1,920 reports, 1,440 prompts; split leakage precheck passed; all 12 stress cells have 5 rows. The unknown-origin stress invariant found 6 violating bundles (P1-01). |
| Probability invariants | Inline Python over `baseline in (0.2,0.3,0.4)`, `discordance in (0.1,0.2,0.3)`, and `delta in (0,-.05,-.08,-.10)`, asserting `p10+p11=baseline` and `(p01+p11)-(p10+p11)=delta` | **PASS** |
| Direct-code counter | `metadata_only_counter(["DPND", "INDP", "INDP", "INDP", "UNKN"])` | **PASS** — returns 3 `INDP` rows; interpretation remains direct-code behavior only |
| Site dependency check | `test -d site/node_modules && echo present || echo absent` | `absent`; site `npm run build`/render tests were not run because installing dependencies would require an external package operation. |
| Independent JSON Schema check | `python3 -c 'import jsonschema'` | Dependency unavailable; no network install was attempted. Independent schema/RFC 8785 checks remain an open gate. |

The adversarial probes below were run as local inline Python scripts. They did not modify repository files.

```text
Prompt mutation probe:
  prompts = build_prompt_instances(generate_corpus(FrozenConfig(), small=True), FrozenConfig())
  mutate one F2 system_text, then call validate_prompt_parity(prompts)
  mutate one F2 user_text, then call validate_prompt_parity(prompts)
Observed: both mutations were accepted.

Receipt mismatch probe:
  result = parse_output(good_bytes, [])
  raw_output_record("RN-AAAAAAAAAA", b"other", result)
Observed: receipt byte_length is 5 and raw_output_sha256 is the hash of good_bytes,
          not b"other".

Corpus-integrity probe:
  deepcopy a small corpus; mutate one report's text, then validate_corpus;
  repeat for proposition_family_id and for stance/origin_id.
Observed: all three tampered corpora were accepted.

Denominator probe:
  score the 16-bundle small corpus in F1/F2 and call paired_analysis(...).
Observed: result reports primary_n=16 and |M|=4, with no rejection.
```

## P0 defects

**None observed.** This is not a readiness pass: P1 defects below prevent a safe pre-pilot/primary lock.

## P1 defects — required before a run gate can pass

### P1-01 — Unknown-origin stress rows expose non-`UNKN` relations

**Evidence:** `tools/origin_accounting/generator.py:340-343` correctly sets the latent relation to `unknown` for every report in an `unknown_origin` bundle. But `tools/origin_accounting/generator.py:534-546` applies relation noise to every F2 stress report and replaces the code with an alternative, including `DPND` or `INDP`. The full-generation probe found 6 stress unknown-origin bundles with non-`UNKN` visible codes; for example, `BD-A7A3Q5JCEO` / `STRESS-02` exposes one `DPND` and three `UNKN` values.

**Normative conflict:** `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:143-146` says every prompt-visible relation in unknown-origin bundles is `UNKN`, even when the latent graph contains transformations. The same rule is part of the unknown-origin shortcut control at lines 430-432.

**Impact:** a stress control can teach or expose a dependent/independent relation in precisely the fixture whose purpose is to preserve unknown. This can turn an unknown relation into a countable cue and invalidates the unknown-origin semantic audit. The problem is in descriptive stress, but the protocol makes the invariant explicit; a descriptive row that violates it cannot be a passing control receipt.

**Required fix:** exempt `unknown_origin` from relation-code noise so all visible codes remain `UNKN`, or explicitly amend the protocol to define noisy unknown rows as a different fixture while retaining a separately enforced all-`UNKN` unknown control. Add a full-corpus test, not only the current first-small-corpus unknown test.

### P1-02 — Confirmatory analysis does not enforce fixed `A` or fixed manifest `M`

**Evidence:** `tools/origin_accounting/analysis.py:147-168` accepts any complete `gold_by_bundle` mapping, does not call `assert_config_invariants`, does not require `len(A)==config.primary_n`, does not require `gold.split == "primary"`, and constructs `M` by selecting every supplied row whose certainty is `multiple`. `tools/origin_accounting/analysis.py:38-48` likewise marks VOR by the certainty value rather than by an explicit frozen membership list.

**Reproducer:** running the same scorer/analysis path on the deliberately small 16-bundle smoke corpus returns `primary_n=16` and `fixed_safety_set_M.n=4` without error. A caller that accidentally supplies dev, pilot, stress, or a mixed set can therefore obtain a plausible-looking analysis object with altered denominators.

**Normative conflict:** the protocol freezes `A` as 300 primary bundles and `M` as its fixed multiple-certainty subset (`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:80-94`, `:321-334`, `:355-364`). The readiness memo also says the fixed manifest set is never intersected with post-run validity (`research/F0_F1_F2_IMPLEMENTATION_READINESS_V1.md:30-35`).

**Impact:** this is a direct estimand/denominator failure if the API is used without an external caller guard. Invalid-output coding itself is correct, but a wrong bundle set changes the estimand while preserving the `invalid_outputs_in_primary_denominator` label.

**Required fix:** require an explicit ordered primary manifest and explicit ordered `M` membership/hash as analysis inputs; validate exact count 300, primary split membership, unique IDs, and `|M|=75` against the locked manifest. Reject smoke/dev/pilot/stress rows unless an explicitly named descriptive mode is used, and do not derive confirmatory membership solely from gold certainty.

### P1-03 — Prompt parity validator does not fail closed on exact F1/F2 bytes, rule, or order

**Evidence:** `tools/origin_accounting/generator.py:648-667` compares token/byte count fields, flags, and F1/F2 report-hash dictionaries. It does not recompute hashes from `system_text`/`user_text`, compare the F1/F2 instruction bytes, compare final prompt bytes, or compare report order as an ordered sequence. Dictionary equality also discards insertion order. At `tools/origin_accounting/generator.py:637-641`, `evidence_bytes_equal` is emitted as the literal `True` rather than derived from evidence bytes.

**Reproducer:** mutating one F2 `system_text` or one F2 `user_text` in a generated prompt list and then calling `validate_prompt_parity` prints `accepted`; all stored count/flag fields remain untouched. This is enough to show that the validator trusts receipt fields rather than the prompt payload.

**Normative conflict:** `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:232-247` requires identical ordered report hashes, exact byte equality, exact intended-tokenizer token equality, system/user/final-input hashes, and fail-closed behavior.

**Impact:** a later prompt-control or serialization edit could alter the F1/F2 rule or evidence while retaining a passing receipt. The current builder output is matched under the local surrogate, but the lock boundary does not protect against mutation or bad receipt construction.

**Required fix:** derive all parity fields from the stored prompt payload; store and compare ordered report hash sequences plus system/user/final-input hashes; compare exact F1/F2 instruction bytes and backend-rendered final bytes; make `evidence_bytes_equal` a computed assertion; enforce local surrogate limits separately from intended-tokenizer parity. Keep byte-length parity explicitly separate from intended-tokenizer token parity.

### P1-04 — Corpus validation accepts tampered evidence and cross-record gold links

**Evidence:** `tools/origin_accounting/generator.py:670-764` checks ID collisions, split-family consistency from `split_index`, bundle report permutations, graph edge/node shape, derivation cycles, and count/certainty consistency. It does not recompute `report.text_sha256` (created at `:338`), `bundle_text_sha256` (created at `:392-394`), or verify that each report's `proposition_family_id`, `origin_id`, `source_id`, `artifact_id`, stance, and transformation agree with its public bundle, graph, and gold row. It also does not verify that the split index and public/gold split fields agree.

**Reproducer:** after deep-copying a small corpus, each of these mutations is accepted by `validate_corpus`: append text to one report without updating `text_sha256`; change a report's `proposition_family_id`; change a report's stance and origin ID. The graph still has the expected report IDs, so the current checks do not notice the semantic mismatch.

**Impact:** evidence text, stance, and origin membership can diverge from their hashes/gold while all current graph and split receipts say pass. That can alter F2 cue semantics, VOR support-origin accounting, surface leakage, or claim-statement scoring without changing the visible record count.

**Required fix:** add an independent schema pass and cross-record validator that recomputes all content hashes, checks every report-to-bundle/proposition/graph/gold link, checks support/refute/relation key sets and disjointness, checks split membership, checks unique/complete bundle and manifest rows, and fails on any duplicate or orphaned record. Include these checks in the deterministic receipt rather than relying on generator construction being the only caller.

### P1-05 — Planning power output does not implement the declared decision/grid

**Evidence:** `tools/origin_accounting/power.py:44-87` counts a simulated FC pass when `delta_hat < 0` and exact `p < .05`, but does not require the primary 95% paired bootstrap upper bound below zero. `tools/origin_accounting/power.py:90-135` emits only the FC grid. The separate `simulate_vor_cell` at `:138-178` is not called by `run_power_simulation`, uses a provisional normal lower bound, has no invalid-rate dimension, and does not report interval coverage.

**Observed output:** `python3 -m tools.origin_accounting.cli power --out "$TMPDIR" --repetitions 1` emits 720 FC cells and no `vor_cells` (or equivalent VOR grid/coverage section).

**Normative conflict:** `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:351-376` declares the FC exact test plus bootstrap upper-bound decision, and `:398-417` requires power, type-I error, interval coverage, conservative/liberal invalid coding, and a separate `|M|=75` VOR grid crossing the specified VOR baselines/deltas with coverage and one-sided-gate probability.

**Impact:** the current planning number is not operating power for the actual primary decision, and there is no operating-characteristic evidence for the safety gate. The implementation receipt's “planning simulation” label is honest, but the required pre-pilot validation cannot pass from this output.

**Required fix:** make FC simulation use the exact declared decision (including the bootstrap criterion and its frozen method), report interval coverage and invalid-coding variants, and add a separate VOR grid fixed at `|M|=75` with the protocol's baseline/discordance/delta cells, invalid-as-zero behavior, coverage, and gate-pass probability. Freeze the final interval method before preregistration.

### P1-06 — Raw-output receipt integrity is caller-trust based, and run schemas cannot record the required audit

**Evidence:** `tools/origin_accounting/parser.py:132-142` copies `result.raw_sha256` into a receipt for an independently supplied `raw` argument instead of recomputing and checking the hash/length against that byte string. The mismatch probe produced a receipt for `b"other"` with the hash of the original `good_bytes`; no exception is raised. `research/origin_accounting/schema/raw_output.schema.json:7-14` only requires an unconstrained base64 string and a hash pattern; it cannot validate base64 decoding, byte length, or hash correspondence. `research/origin_accounting/schema/run_record.schema.json:7-26` does not require final input bytes/hash, system/user/final prompt hashes, chat-template/runtime/dependency/hardware receipts, seed/decoder fields beyond an unconstrained object, or a link to the raw-output bytes.

**Normative conflict:** the protocol requires model/checkpoint/tokenizer/chat-template/runtime/dependency/hardware/decoding/seeds, prompt hashes, input/output counts, timing/memory/errors, and raw bytes for every assigned run (`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:249-268` and `:526-541`).

**Impact:** a malformed writer can produce a self-inconsistent raw receipt, and the schemas cannot enforce the run provenance needed to demonstrate one-model, exact-prompt, no-retry execution. This is an audit-integrity gap even though no run is currently authorized.

**Required fix:** recompute `sha256(raw)` and `len(raw)` in `raw_output_record`, reject a mismatched `ParseResult`, and add a validator for base64/hash/length. Expand run receipts/schema with final input/system/user hashes and bytes/counts, chat template, model/checkpoint/tokenizer, decoder seed(s), runtime/dependency/hardware, and raw-output linkage; keep invalid/runtime reason codes distinct.

### P1-07 — CLI does not load the committed frozen config, and emitted version identity is stale/ambiguous

**Evidence:** `tools/origin_accounting/config.py:124-132` provides `load_frozen_config`, but `tools/origin_accounting/cli.py:70-74` and `:90-93` instantiate `FrozenConfig()` directly. Current defaults happen to equal the committed JSON, but a committed config edit would not affect CLI generation or the config hash in the smoke receipt. The config code and JSON identify `protocol_version="0.3"` and `specification_version="loop3-operationalization-0.3"` (`config.py:30-33`; `research/origin_accounting/config/frozen_config.json:2-4`), while canonical `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:1-11` identifies protocol v1.0 and says it supersedes v0. No compatibility mapping is recorded in the emitted manifest (`cli.py:95-113`).

**Impact:** a future receipt may silently use code defaults instead of the committed frozen file, and its manifest can be mistaken for the superseded v0.3 protocol rather than v1.0. This undermines reproducibility and lock identity even before model selection.

**Required fix:** make all CLI paths load and hash the committed config, record the config-file hash and the exact protocol/specification compatibility mapping, and either bump the emitted protocol identity to v1.0 or state explicitly why `0.3` is an implementation subversion of v1.0. Add a test that changes a temporary committed-config value and proves the CLI consumes it.

## P2 defects

### P2-01 — Readiness memo still names the superseded v0 protocol as its baseline

`research/F0_F1_F2_IMPLEMENTATION_READINESS_V1.md:3-7` labels the memo v1 but points its “Protocol baseline” to `ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V0.md` v0.3 and its operationalization baseline to the old loop2 file. The memo otherwise describes v1 concepts and the v1 ledger commitment. This is documentation drift that can misdirect an independent reviewer to the wrong lock; update the pointers or explicitly label them as historical compatibility inputs after the P1-07 version decision.

### P2-02 — The near-duplicate diagnostic can report `pass` for a precheck, not an exhaustive leakage clearance

`tools/origin_accounting/diagnostics.py:60-76` deliberately applies token-set blocking before the character-gram threshold and says the final lock needs an independently implemented exhaustive probe. Nevertheless, it returns `status="pass"` when the blocked precheck finds no candidates (`:70`). The protocol correctly says this is insufficient (`research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:174-189`), but a receipt consumer could treat the generic `pass` as clearance. Rename the result to `precheck_pass`/`clearance_unresolved` and reserve `pass` for the independent locked probe, or include an explicit non-authorizing status in every receipt.

## What passed and should be preserved

- The primary formula and direction are preserved: F2 minus F1 on all-assigned `FC_cons`; invalid outputs are coded as risk events. No evidence here requires changing the estimand, sample target, or F0/F1/F2 causal contrast.
- The shared relation legend, F0 ordinary instruction, and byte-identical F1/F2 rule match the v1 condition specification. The builder emits equal local-surrogate token/byte counts, and all relation codes occupy the same four ASCII bytes. The parity *validator* remains defective as described in P1-03.
- The parser is strict and write-once for the supplied bytes: fenced/prose output, duplicate keys, unknown keys/IDs, wrong types, non-finite numbers, duplicate evidence IDs, empty output, and malformed UTF-8 all have focused fixtures and distinct reason codes. No repair, extraction, or retry path was found in `parser.py`.
- The direct metadata counter correctly counts each `INDP` row rather than using a set, and its returned interpretation explicitly says it is a shortcut/direct-code diagnostic rather than semantic evidence integration.
- The local power probability correction is correct: the checked grid satisfies `P(F1=1)=baseline` and `P(F2=1)-P(F1=1)=delta` for every valid cell.
- The generator uses opaque HMAC/Base32 IDs, future-dated fictional records, separate support/refute stance fields, and split-family blocking. Multiple-origin and conflict tests prevent a refuting `INDP` from being laundered into supporting-origin recall. Root/original `UNKN` remains intentional; no `ORIGINAL` code was invented.
- T1 is firewalled. Static inspection found no T1 data adapter or F3 path in the origin-accounting tools. The manuscript and reader keep T1 descriptive and outside `A`, `M`, intervals, McNemar rows, VOR, and effect estimates (`source/THOUGHT_PIECE_V15.md:501-518`; `site/app/page.tsx:579-584`).
- The owner-approved null/negative/harmful/unstable/shortcut commitment is present as a locked commitment, not a proposed patch (`reports/V15_DECISION_LEDGER.md:62-84`; `research/F0_F1_F2_IMPLEMENTATION_READINESS_V1.md:316-334`).

## Unresolved run gates (not claims of results)

These remain stops even after the P1/P2 corrections:

1. **Model/tokenizer:** no owner-selected model, checkpoint, license, runtime, or intended tokenizer. Surrogate regex parity is explicitly non-authorizing. Backend chat-template rendering and final-input parity have not been run.
2. **Primary and safety manifests:** no separately frozen ordered `A`/`M` artifact with 300/75 membership and hash; the current analysis derives membership from caller-supplied gold.
3. **Leakage/shortcut:** no blocked held-out-family character/token TF-IDF classifier, frozen ceiling/Wilson interval, condition/structure/order/style/overlap control, codebook-permutation/neutral-label stress, or independent semantic/stance/transformation audit. The full nearest-centroid result is 0.5 accuracy and the 16-bundle smoke result is 1.0; neither is clearance.
4. **Schema/canonicalization:** no independent Draft 2020-12 validator was available in this offline environment, and the local JSON serializer expressly does not claim RFC 8785 conformance. The raw/run schema gaps in P1-06 remain.
5. **Power and interval:** the VOR interval method and coverage plan are not frozen/validated; FC interval coverage and the separate VOR operating-characteristic grid are absent.
6. **Privacy/control scans:** no completed prompt-control-string, secret/private-text, or independent release-boundary scan is recorded for this loop. The synthetic generator made no external calls, but a release gate still needs the scan receipt.
7. **Pilot/preregistration/authorization:** no pilot output, preregistration, primary authorization, or owner model/budget authorization exists.
8. **T1 transfer:** rights, dataset/version, field-level licensing, and annotation gates remain unresolved. The firewall must remain in place.

## Required disposition

1. Treat the current implementation as **offline scaffolding only**, not pre-pilot-ready.
2. Correct P1-01 through P1-07 and add focused regression tests for every reproducer above.
3. Correct or explicitly disposition P2-01/P2-02 in the next lock receipt.
4. Re-run the full offline validator and publish an explicit ordered primary/safety manifest before any pilot output is considered.
5. Preserve the current F2-F1 estimand and the locked negative-result table. None of the observed defects requires a protocol amendment to the estimand. The only possible protocol question is whether relation-noise is intended to override the all-`UNKN` unknown-origin fixture; absent an explicit amendment, the implementation must preserve all `UNKN`.

- **Final review status:** `FAIL_PREPILOT_IMPLEMENTATION_GATE`
- **Model/provider/network calls:** `0`
- **External data/results:** `none`

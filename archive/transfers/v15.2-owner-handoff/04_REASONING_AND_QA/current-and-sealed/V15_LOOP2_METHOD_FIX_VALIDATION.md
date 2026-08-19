# V15 loop-2 method-fix validation

**Checkout:** `/Users/gpt/Documents/Codex/worktrees/discrimination-layer-v15-method-fix`

**Branch:** `codex/discrimination-layer-v15-method-fix`

**Base reviewed:** `f6fea6b` (`Add v15 loop2 adversarial methods review`)

**Validation date:** 2026-08-18
**Scope:** offline implementation repairs for every P1-01 through P1-07 and both P2 findings in `reports/V15_LOOP2_METHOD_ADVERSARIAL_REVIEW.md`.

## Re-review verdict

**PASS for the loop-2 implementation-fix re-review.** Each original reproducer
now fails closed or is represented by a separately named non-confirmatory mode.
The F2-minus-F1 estimand, all-assigned `FC_cons` coding, fixed 300-row primary
definition, fixed 75-row safety definition, F0/F1/F2 causal core, T1 firewall,
and locked negative-result commitment are unchanged. No model, provider,
network, Cloud Run, paid service, external corpus, preregistration, push, PR,
or deployment was used.

This is **not** a primary/pilot authorization. The intended model tokenizer,
backend chat-template rendering, independent JSON-Schema/RFC 8785 validation,
the exhaustive near-duplicate lock, and owner run authorization remain open
gates as recorded below.

## Finding-by-finding disposition

| Finding | Repair and exact implementation anchor | Regression / validation | Re-review |
| --- | --- | --- | --- |
| **P1-01 unknown-origin stress exposes non-`UNKN`** | `tools/origin_accounting/generator.py:_relation_code_for_report` returns `UNKN` before relation-noise perturbation whenever `required_unknown_preservation` is true. Gold latent transformations remain unchanged. | `OriginAccountingReadinessTests.test_full_unknown_origin_stress_preserves_all_visible_unknown_codes`; full generation checked all 480 bundles and 1,920 reports, with zero unknown-origin F2 visible-code violations. | **PASS** |
| **P1-02 confirmatory analysis accepts smoke/non-primary denominators** | `tools/origin_accounting/generator.py:build_primary_manifest` emits ordered/hash-locked A and M membership. `tools/origin_accounting/analysis.py:_validate_confirmatory_manifest` requires protocol v1.0, exactly 300 primary IDs and exactly 75 multiple-certainty IDs, hashes, split membership, subset/equality rules, and exact score-key membership. `paired_analysis` defaults to `analysis_mode="confirmatory"`; only `analysis_mode="descriptive_smoke"` permits a small fixture. | `test_confirmatory_analysis_requires_ordered_300_75_manifest` rejects a missing/short manifest, while the small-corpus test explicitly uses `descriptive_smoke`. Full CLI generation emitted a standalone `release/primary_manifest.json` with 300/75 IDs. | **PASS** |
| **P1-03 prompt parity trusts mutable fields** | `tools/origin_accounting/generator.py:_validate_prompt_payload` recomputes system/user/instruction/final-input SHA-256 hashes, deterministic-surrogate token counts, UTF-8 byte lengths, final-input concatenation, relation-code coverage, and ordered report hash sequence. `validate_prompt_parity` compares all F0/F1/F2 condition receipts, F1/F2 rule bytes, shared system bytes, ordered evidence, and corpus report bytes. Intended-tokenizer status remains explicitly `not_run_model_tokenizer`. | `test_prompt_parity_recomputes_mutated_payload_and_instruction` rejects mutated F2 system/user/rule payloads. `test_prompt_has_exact_per_bundle_token_and_byte_parity` checks per-bundle parity. | **PASS** |
| **P1-04 corpus validator accepts tampered evidence/links** | `tools/origin_accounting/generator.py:validate_corpus` now recomputes report and bundle hashes; checks complete public/gold/split/graph membership; report-to-bundle/proposition links; gold stance/origin/relation sets; split-family consistency; graph node/edge/link/derivation invariants; graph certainty/origin metadata; cycles; and exact split/structure counts. | `test_corpus_validator_rejects_hash_and_cross_record_tampering` rejects report text/hash, proposition-family, stance/origin, and gold-relation mutations. Full `generate_corpus(..., small=False)` passes the validator. | **PASS** |
| **P1-05 power output omits the declared FC decision and VOR grid** | `tools/origin_accounting/power.py:simulate_fc_cell` applies the exact planning decision (`delta_hat < 0`, exact paired p `< alpha`, and paired-bootstrap upper bound `< 0`), reports coverage, and exposes conservative/liberal invalid-coding sensitivities. `run_power_simulation` emits a distinct VOR grid crossing baseline, discordance, delta, invalid-rate, and fixed-M size. `simulate_vor_cell` uses the declared one-sided lower-bootstrap development scaffold, invalid-as-zero coding, coverage, and gate probability. | Reduced smoke: `python3 -m tools.origin_accounting.cli power --out "$TMPDIR/oa-power" --repetitions 1 --bootstrap-repetitions 5 --vor-bootstrap-repetitions 5 --vor-n 10` emitted 1,440 FC cells plus explicit skipped-cell records and 128 valid VOR cells; each result carries decision/coverage or gate/coverage fields. Production grid declares `expected_protocol_n_fixed_M=75`; `vor_n=10` was used only for bounded smoke. | **PASS** |
| **P1-06 raw receipts trust caller hash and schemas lack audit fields** | `tools/origin_accounting/parser.py:raw_output_record` recomputes SHA-256/length and rejects a mismatched `ParseResult`. `validate_raw_output_record` strictly decodes canonical base64 and rechecks byte length/hash/status. `validate_run_record` requires prompt hashes, input bytes/tokens, chat template, runtime, dependency hashes, hardware, decoder, seed, timing/memory, error, and raw-output linkage. Raw/run JSON Schemas were expanded accordingly. | `test_parser_is_strict_and_preserves_raw_receipt` validates a good receipt and rejects the original `b"other"` mismatch reproducer; it also validates a complete run receipt. Parser fixtures remain 18/18. | **PASS** |
| **P1-07 CLI/config identity drift** | `tools/origin_accounting/config.py` sets canonical protocol identity to v1.0, fails closed on a missing frozen file, and exposes exact config-file hashing. `tools/origin_accounting/cli.py` loads/hashes the provided committed config for smoke/generate/power, records file and derived-config hashes, emits `origin-accounting-protocol-v1.0`, and writes the primary manifest. The old `loop3-operationalization-0.3` value is retained only as a historical specification input, not protocol identity. | `test_cli_consumes_hashed_frozen_config_file` changes a temporary frozen config seed and proves CLI output uses its file hash. Full CLI generation emitted protocol v1.0 and 300/75 manifest identity. | **PASS** |
| **P2-01 readiness memo points at superseded v0** | `research/F0_F1_F2_IMPLEMENTATION_READINESS_V1.md` now names `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md` v1.0 as the protocol baseline and labels V0/loop-2 operationalization as historical compatibility inputs. | Text audit with `rg` confirms no stale v0 baseline claim remains; the historical references are explicitly marked superseded. | **PASS** |
| **P2-02 near-duplicate precheck says generic pass** | `tools/origin_accounting/diagnostics.py:split_leakage_report` returns `precheck_pass`/`precheck_fail`, `clearance_status="unresolved"`, `authoritative=false`, and a named blocked-precheck probe. | `test_small_corpus_is_deterministic_and_split_blocked` checks the new non-authorizing receipt fields. Smoke receipt records `precheck_pass` plus unresolved clearance. | **PASS** |

## Exact offline checks

Commands were run from the checkout above. No command accessed a model,
provider, network, Cloud Run, paid service, or external data.

```text
python3 -m unittest discover -s tests -p 'test_*.py' -v
Ran 12 tests ... OK

python3 -m compileall -q tools/origin_accounting tests
PASS

python3 -m tools.origin_accounting.cli parser-fixtures
18 fixtures; pass=true

python3 -m tools.origin_accounting.cli smoke --out "$TMPDIR/oa-smoke"
PASS — 16 smoke bundles, 64 reports, 48 prompts; 0 model/provider/network calls;
       split status=precheck_pass, clearance_status=unresolved

python3 -m tools.origin_accounting.cli generate --out "$TMPDIR/oa-full"
PASS — 480 bundles, 1,920 reports, 1,440 prompts; protocol identity v1.0;
       standalone primary manifest A=300, M=75; 0 model/provider/network calls

python3 -m tools.origin_accounting.cli power --out "$TMPDIR/oa-power" \
  --repetitions 1 --bootstrap-repetitions 5 \
  --vor-bootstrap-repetitions 5 --vor-n 10
PASS as reduced planning smoke — FC decision/coverage fields and separate VOR
       gate/coverage fields emitted; VOR n=10 is smoke-only, expected protocol n=75

git diff --check
PASS

python3 -m pytest -q
NOT RUN — pytest is not installed in the offline interpreter

python3 -c 'import jsonschema'
NOT RUN — jsonschema is not installed; no network install attempted
```

The focused unittest suite is the authoritative executed regression check in
this environment. JSON parsing of every changed schema/config file also
passed with the standard-library `json` module.

## Remaining run gates and limitations

1. No owner-selected frozen model/checkpoint/tokenizer exists. The local
   regex tokenizer proves only deterministic development parity. Intended
   tokenizer token equality and backend chat-template final-input parity are
   still open and non-authorizing.
2. The FC bootstrap method and one-sided VOR bootstrap method are explicitly
   labelled development scaffolds. The reduced smoke uses five resamples; the
   protocol planning configuration remains 10,000 repetitions/resamples and
   must be coverage-simulated and frozen before preregistration.
3. The exhaustive blocked held-out-family near-duplicate/TF-IDF suite,
   semantic/stance/transformation audit, condition/order/style/overlap
   shortcut suite, privacy/control-string scan, and independent release scan
   remain required. `precheck_pass` is not leakage clearance.
4. An independent Draft 2020-12 JSON-Schema implementation and RFC 8785
   conformance suite were unavailable offline. The dependency-free validator
   is an additional cross-record guard, not a replacement for those gates.
5. No pilot, preregistration, primary authorization, or owner approval for a
   live run is present. All generated artifacts remain synthetic offline
   design scaffolding.

## Amendment disposition

No protocol amendment is required. The repairs make the implementation obey
the existing v1.0 specification: they do not alter the FC estimand, A/M
denominators, condition contrast, invalid-output policy, T1 boundary, or
negative-result commitment. The only version clarification is receipt-level:
the canonical protocol identity is v1.0, while the older operationalization
string is recorded as a historical compatibility input.

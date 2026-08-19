# Loop 3 consolidated operationalization specification

## Oracle Origin-Relation Metadata in One Frozen Model

Status: review-resolved design specification, version `loop3-operationalization-0.3`, paired with protocol `0.3`; no corpus has been generated, no model has been run, and no live, paid, human-participant, deployment, or publication activity is authorized by this document. “Review-resolved” means the Loop 3 audit findings are incorporated; it is not a preregistration or feasibility result.

This specification operationalizes `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V0.md` after the feasibility red team and the Loop 3 ML/NLP, HCI/ethics, reproducibility, and reader/design reviews. It also reconciles the revised `research/PAPER_PROSPECTUS_V0.md`. It is deliberately narrower than the thought piece: it estimates an observable F2-versus-F1 condition effect for one frozen model; it does not identify an internal reasoning mechanism or test provenance discovery, source authority, retrieval, routing, memory, human correction, or the full Pattern Recognition / Discrimination Layer.

## 1. Frozen decision summary

The study’s single confirmatory question is:

> On newly authored fictional evidence bundles with a stipulated provenance graph, does a condition containing a compact typed origin cue—`dependent`, `independent-as-stipulated`, or `unknown`—produce less false corroboration than the same evidence and explicit origin-counting rule without the cue, on one frozen model?

The intervention is an **oracle-cue representation/use condition**. The graph relation is supplied in F2; the model is not asked to infer it. The study therefore supports, at most, a bounded claim about using relation-typed provenance information under controlled conditions.

### Decisions made to remove remaining ambiguity

| Decision point | Consolidated choice for protocol/specification 0.3 | Why |
| --- | --- | --- |
| Primary sample size | Retain the protocol target of **300 primary bundles**: 75 in each origin structure. | It preserves the preregistered protocol target. Do not silently change to 320 for a cleaner secondary factorial balance; claim-state balance is removed from confirmatory analysis instead. |
| Primary endpoint | Paired false-corroboration event, F2 versus F1. | One binary endpoint with one bundle-level unit and one primary contrast. |
| Safety endpoint | Recall of stipulated supporting origins (`VOR` shorthand) on the fixed manifest set with multiple supporting origin pathways. | Prevents the intervention from winning by calling every bundle dependent or unknown; the denominator never changes with parse status. |
| Claim-state output | Keep `claim_state` in the output contract as a descriptive secondary field, but do not make it a powered claim or balance it across structures. | Claim-state semantics are orthogonal to origin accounting and would expand the estimand. |
| Confidence output | Keep a scalar selected-state `confidence` for logging; do **not** call its squared error a multiclass Brier score. | A proper multiclass Brier score requires a full probability vector. Add that only in a later protocol. |
| Public datasets | No public text in the primary statistical test. Optional 60-bundle public transfer set is descriptive after the primary lock. | Public datasets do not supply complete origin truth and may be memorized. |
| Model count | One frozen local open-weight instruction model for the confirmatory run. An optional second model is unpowered robustness only. | Avoid model-family multiplicity and provider drift. |
| Decode | Deterministic decoding if the selected local backend supports it. Otherwise three predeclared seeds, nested within bundle. | Seeds are uncertainty, not additional independent items. |
| Resource match | Exact per-bundle input-token parity for F1 versus F2; F0 is padded to the same target and is secondary. | The primary contrast must differ in relation information, not accidental prompt length. If exact parity is impossible, stop before opening the primary split. |
| Gold relation meaning | `independent_as_stipulated` means separate origin nodes in the synthetic graph; it does not mean real-world causal or epistemic independence. | Prevents synthetic bookkeeping from being overclaimed as truth. |
| Pilot | 40 pilot bundles, 10 per structure, for schema, parser, generator, leakage, and replay feasibility only. | Pilot effects are not efficacy evidence; this follows the pilot-design caution in [Leon, Davis, & Kraemer (2011)](https://doi.org/10.1016/j.jpsychires.2010.10.008). |

**Recommendation if any choice above becomes impossible:** downgrade to an estimation/benchmark feasibility paper. Do not add models, human participants, retrieval, or extra endpoints to rescue a failed first study.

### 1.1 Evidence status of this specification

- **Sourced evidence / standards:** JSON Lines and JSON Schema define machine-readable interchange contracts; W3C PROV-O supplies a provenance vocabulary; the cited pilot, power, construct-validity, and multiple-testing sources constrain how the protocol should be documented. These sources do not validate this benchmark or its synthetic labels.
- **Design inference:** because ordinary claim-verification corpora do not expose complete report-to-origin derivation truth, a deterministic fictional generator is the narrowest way to obtain a known graph for this mechanism test. The paired bundle unit, F2-versus-F1 estimand, and oracle-cue claim boundary are methodological recommendations inferred from the protocol’s stated question and the Loop 1 red-team constraints.
- **Speculative / falsifiable hypotheses:** F2 will reduce `FC` relative to F1; the candidate practically important effect is `-0.08`; and the five-point VOR margin is acceptable. These are planning hypotheses, not observed effects or sourced facts. A null, harmful, underpowered, or shortcut-contaminated result narrows or falsifies the corresponding claim.

## 2. Artifact layout and data-flow boundary

The benchmark is a set of UTF-8 JSON Lines files (`.jsonl`) plus JSON manifests. Each line is one complete JSON object; no pretty-printed multi-line records are permitted. The format follows the JSON Lines convention ([jsonlines.org](https://jsonlines.org/)) and uses JSON Schema Draft 2020-12 for validation ([official schema](https://json-schema.org/draft/2020-12/schema)).

```text
origin-accounting/
  schema/
    proposition.schema.json
    report.schema.json
    bundle_public.schema.json
    bundle_gold.schema.json
    provenance.schema.json
    prompt_instance.schema.json
    run_record.schema.json
    raw_output.schema.json
    parsed_output.schema.json
    qa_record.schema.json
  data/
    propositions.jsonl              # non-sensitive; no gold origin relation
    reports.jsonl                   # non-sensitive report text and public IDs
    bundles_public.jsonl            # prompt-visible bundle records
    bundles_gold.jsonl              # restricted evaluation truth
    provenance_graphs.jsonl         # restricted graph truth
    split_index.jsonl               # restricted until primary lock
    pilot_bundles.jsonl             # development/pilot only
    stress_bundles_public.jsonl     # prompt-visible stress items
    stress_bundles_gold.jsonl       # restricted stress truth
  prompts/
    F0.jsonl
    F1.jsonl
    F2.jsonl
  runs/
    run_records.jsonl
    raw_outputs.jsonl
    parsed_outputs.jsonl
    qa_records.jsonl
  analysis/
    power_simulation.json
    primary_analysis_plan.json
  release/
    manifest.json
```

### Trust boundary

`bundles_public.jsonl`, `reports.jsonl`, and prompt instances may be given to the model. `bundles_gold.jsonl`, `provenance_graphs.jsonl`, and `split_index.jsonl` must remain unavailable to the model and to any prompt-building process except through a keyed evaluator. The evaluator joins on `bundle_id` only after raw model output is immutable.

The model must never receive `proposition_family_id`, `origin_family_id`, `origin_id`, `gold_claim_state`, `gold_support_origin_count`, `split`, `condition`, or any generator field not explicitly listed in the prompt template.

## 3. Canonical identifiers and hashes

IDs are opaque and carry no relation, class, domain, split, or condition semantics. They are reproducible but not sequential.

| Object | Pattern | Example | Visibility |
| --- | --- | --- | --- |
| Study | `^OA-[A-Z0-9-]+$` | `OA-TPC-001` | public |
| Proposition family | `^PF-[A-Z2-7]{10}$` | `PF-K7M2Q9X4PT` | restricted until split lock; never prompt-visible |
| Origin | `^OR-[A-Z2-7]{10}$` | `OR-4QK8Z2M6JD` | gold only |
| Origin family | `^OF-[A-Z2-7]{10}$` | `OF-6P3M8Q2K7T` | gold/split index only |
| Provenance graph | `^PG-[A-Z2-7]{10}$` | `PG-2M7Q4K8XPD` | gold only |
| Report | `^RP-[A-Z2-7]{10}$` | `RP-P3V6N8Q1ZT` | prompt-visible as an opaque report ID |
| Source | `^SC-[A-Z2-7]{10}$` | `SC-9J2K4M7QXD` | prompt-visible as an opaque source ID |
| Artifact | `^AR-[A-Z2-7]{10}$` | `AR-T6P2K8V4QW` | prompt-visible as an opaque artifact ID |
| Bundle | `^BD-[A-Z2-7]{10}$` | `BD-N8Q2W6K4ZT` | prompt-visible |
| Prompt instance | `^PI-[A-Z2-7]{10}$` | `PI-4M8Q2V7KXD` | run metadata only |
| Run | `^RN-[A-Z2-7]{10}$` | `RN-7T2Q9K4MVP` | run metadata only |

Generate an ID as the first 10 **RFC 4648 Base32** characters (uppercase, no padding) of `HMAC-SHA256(master_seed, object_type + ":" + stable_namespace + ":" + local_index)`. The `[A-Z2-7]` patterns above therefore describe the actual alphabet; do not substitute Crockford Base32 without changing the schemas and examples. Do not expose `master_seed` until a later release is authorized. The public release may replace it with a release seed if exact regeneration is permitted.

`origin_family_id` is a blocked lineage unit, not a target class. It groups every latent origin node, artifact, report, and derived transformation that the generator could reuse within one candidate graph. The default generator assigns one origin family to one bundle graph and never reuses it. If an implementation intentionally reuses a source, template, origin, or derived artifact across bundles, all affected bundles inherit the same `origin_family_id` and must be assigned to one split; post-hoc ID relabeling is not allowed.

Every JSONL file must have:

- UTF-8 encoding and one final newline;
- unique primary ID within the file;
- RFC 8785 JSON Canonicalization Scheme serialization for hashing, with UTF-8 bytes, recursive lexicographic property ordering, ECMAScript-compatible number serialization, and array order preserved;
- no `NaN`, `Infinity`, comments, trailing commas, or duplicate JSON keys;
- SHA-256 recorded in the release manifest.

Publish RFC 8785 conformance fixtures, including Unicode, nested maps, arrays, negative zero, and boundary numeric representations. A record that cannot be represented within the interoperable JSON number domain fails closed before hashing; “pretty-printed then sorted” is not an accepted substitute.

## 4. JSON/JSONL schema contracts

The full machine validation should use the JSON Schema files named in Section 2. The tables below are normative: required fields, types, enumerations, and bounds are not suggestions. `additionalProperties` is `false` for every record except `metadata` objects explicitly marked as extension-safe.

### 4.1 `propositions.jsonl`

One line per underlying proposition family. No two split records may share `proposition_family_id`.

| Field | Type/constraint | Meaning |
| --- | --- | --- |
| `proposition_family_id` | string; opaque ID; required | Stable unit used for split blocking. Never prompt-visible. |
| `domain` | enum `technical`, `environmental`; required | Synthetic content domain only. |
| `subject` | string; 3–60 Unicode chars | Fictional entity/site name. |
| `predicate` | enum `reduced`, `increased`, `recorded`, `did_not_record`; required | Canonical machine predicate selected by the versioned rendering map. Every value has exactly one claim renderer and round-trip fixture. |
| `object` | string; 3–80 chars | Metric or observation. |
| `magnitude` | number; finite; bounded `-1000` to `1000` | Numeric value if predicate requires it. |
| `unit` | enum `percent`, `milliseconds`, `units`, `count`, `index_points`, `none` | Measurement unit. |
| `baseline` | string; 3–80 chars | Comparison condition. |
| `site` | string; 3–80 chars | Fictional lab, region, or test site. |
| `time_window` | object `{start_year:int,end_year:int}`; years 2030–2099; `start_year <= end_year` | Synthetic time only. |
| `truth_state` | enum `supported`, `refuted`, `insufficient`, `contested`; required | Gold claim state used only for descriptive claim-state scoring. |
| `lexical_seed` | integer 0–2^63−1 | Reproducible grammar choice; hidden from model. |

Canonical example:

```json
{"proposition_family_id":"PF-K7M2Q9X4PT","domain":"technical","subject":"Lumen cache","predicate":"reduced","object":"median sync latency","magnitude":18,"unit":"percent","baseline":"the baseline cache","site":"Northlake test bench","time_window":{"start_year":2042,"end_year":2042},"truth_state":"supported","lexical_seed":18402731}
```

### 4.2 `reports.jsonl`

One line per report artifact. This is prompt-visible except for fields marked restricted.

| Field | Type/constraint | Visibility/meaning |
| --- | --- | --- |
| `report_id` | opaque string; required | Prompt-visible identifier. |
| `source_id` | opaque string; required | Prompt-visible source identifier; no semantics. |
| `artifact_id` | opaque string; required | Prompt-visible artifact identifier. |
| `proposition_family_id` | opaque string; required | Restricted; split join only. |
| `origin_id` | opaque string; required | Restricted; gold graph only. |
| `style` | enum `lab_note`, `release_note`, `field_log`, `review_note`; required | Restricted generator field; prompt may show prose only. |
| `stance` | enum `supports`, `refutes`, `neutral`; required | Restricted gold label; evaluator only. |
| `transformation_type` | enum `original`, `dependent_copy`, `dependent_paraphrase`, `independent_observation`, `independent_contradiction`, `summary`; required | Restricted gold label; not prompt-visible. |
| `observed_at` | ISO date `YYYY-MM-DD`, synthetic years only; required | Prompt-visible date. |
| `text` | string 120–900 Unicode chars; no control characters except spaces/newline | Prompt-visible evidence text. |
| `text_sha256` | lowercase 64-hex string; required | Integrity; may be prompt-hidden. |

### 4.3 `bundles_public.jsonl`

One line per prompt-visible bundle; no gold fields.

| Field | Type/constraint | Meaning |
| --- | --- | --- |
| `bundle_id` | opaque string; required | Prompt/evaluator join key. |
| `proposition_family_id` | restricted string; required in storage, removed before prompt | Split blocking. |
| `claim_text` | string 40–300 chars; required | Exact target claim shown to model. |
| `report_ids` | array of 4–6 unique report IDs | Reports in the bundle. |
| `report_order` | array containing exactly `report_ids` once | Frozen order used in all F0/F1/F2 paired runs. |
| `domain` | enum technical/environmental; prompt-hidden or shown only if template requires | Do not let domain reveal structure. |
| `observed_date_range` | object; derived from reports | Prompt-visible only if included in all conditions. |
| `bundle_text_sha256` | lowercase 64-hex | Integrity. |

### 4.4 `bundles_gold.jsonl`

One line per bundle, unavailable to the model.

| Field | Type/constraint | Meaning |
| --- | --- | --- |
| `bundle_id` | required opaque string | Join key. |
| `split` | enum `dev`, `pilot`, `primary`, `stress` | Locked before model run. |
| `origin_structure` | enum `one_origin_repetition`, `multiple_origin_convergence`, `unknown_origin`, `conflict` | Confirmatory strata. |
| `gold_claim_state` | enum `supported`, `refuted`, `insufficient`, `contested` | Descriptive state only. |
| `gold_support_origin_count` | integer 0–6 or null | Count of supporting-side origin nodes when certified; null iff certification is `unknown`. This never counts refuting-only origins. |
| `gold_support_origin_certainty` | enum `none`, `single`, `multiple`, `unknown` | Certified supporting-path status visible to evaluator. `unknown` is not `multiple`. |
| `support_origin_ids` | array of opaque origin IDs; may be empty; restricted latent graph truth | Supporting-side origin IDs only; not used as a claim of real independence. |
| `refute_origin_ids` | array of opaque origin IDs; may be empty; restricted latent graph truth | Refuting-side origin IDs, kept separate so conflict bundles cannot inflate supporting-origin counts. |
| `origin_family_id` | opaque `OF-...` string; required | Blocked lineage family; never prompt-visible. |
| `supporting_report_ids` | array of report IDs | Reports with `stance=supports`. |
| `refuting_report_ids` | array of report IDs | Reports with `stance=refutes`. |
| `relation_by_report_id` | map `report_id → dependent / independent_as_stipulated / unknown` | Gold relation for evaluator and F2 builder. |
| `required_unknown_preservation` | boolean | True for unknown-origin bundles. |
| `provenance_graph_id` | opaque string | Join to restricted graph. |
| `stress_variant` | enum `order`, `overlap`, `relation_code_permutation`, `relation_noise`, or null | Required non-null only for the `stress` split. |
| `noise_rate` | number in `0`, `0.05`, `0.10`, `0.20` | `0` outside relation-noise stress; frozen before generation. |
| `noise_seed` | opaque string or null | Required iff `noise_rate > 0`; never prompt-visible. |
| `stress_cell_id` | opaque string or null | Required for `stress`; identifies the frozen balanced allocation. |

Cross-field invariants are normative: `gold_support_origin_count=null` iff `gold_support_origin_certainty=unknown`; counts 0, 1, and 2–6 map to `none`, `single`, and `multiple`; `support_origin_ids` length equals the certified count when non-null; and no ID may appear in both support and refute sets for one proposition stance. Conflict fixtures must cover one-support/one-refute, multiple-support/one-refute, and dependent-copy/refute combinations.

### 4.5 `provenance_graphs.jsonl`

The graph is a restricted audit object. It uses PROV-O-like vocabulary but does not assert correctness; the W3C recommendation is [PROV-O](https://www.w3.org/TR/prov-o/).

```json
{
  "provenance_graph_id": "PG-...",
  "origin_family_id": "OF-...",
  "nodes": [
    {"node_id":"OR-...","node_type":"origin"},
    {"node_id":"SC-...","node_type":"source"},
    {"node_id":"AR-...","node_type":"artifact","report_id":"RP-..."}
  ],
  "edges": [
    {"from":"AR-...","to":"SC-...","edge_type":"generated_from"},
    {"from":"AR-...","to":"OR-...","edge_type":"generated_from"},
    {"from":"AR-...","to":"AR-...","edge_type":"derives_from","derivation":"dependent_paraphrase"}
  ],
  "latent_origin_count": 3,
  "certified_relation_state": "multiple"
}
```

The graph record has this normative shape (all IDs must resolve within the same bundle):

| Field | Type/constraint | Meaning |
| --- | --- | --- |
| `provenance_graph_id` | opaque string; required and unique | Restricted graph identifier. |
| `origin_family_id` | opaque `OF-...` string; required | Split-blocking lineage family. |
| `nodes` | array of 1–24 objects; required | Node objects with `node_id`, `node_type` (`origin`, `source`, `artifact`), and `report_id` required only for artifact nodes. |
| `edges` | array of objects; required | Each edge has `from`, `to`, `edge_type` (`generated_from`, `derives_from`), and `derivation` required only for `derives_from`. |
| `latent_origin_count` | integer 1–6; required | Number of distinct origin nodes in the latent graph. |
| `certified_relation_state` | enum `single`, `multiple`, `unknown`, `none`; required | What the benchmark certifies to the evaluator; `unknown` is not a count. |

The graph validator must reject dangling IDs, duplicate node IDs, duplicate edges, artifact nodes without exactly one report ID, reports without exactly one artifact node, and derivation edges that create a cycle.

Normative graph rules:

- every report artifact has exactly one source, one artifact node, and one origin node in the latent graph;
- an original artifact has no `derives_from` parent;
- a dependent copy, paraphrase, or summary has exactly one or more derivation edges to its parent/origin path;
- independent-as-stipulated origins have no derivation edge to each other;
- unknown-origin bundles may have a latent graph with multiple origins, but `certified_relation_state` is `unknown` and the evaluator must not score the model as knowing those origins;
- no graph edge itself implies claim truth, authority, or authorization.

### 4.6 `prompt_instance.jsonl`

One line per bundle-condition input. It records exactly what the model receives and the resource parity checks.

| Field | Type/constraint | Meaning |
| --- | --- | --- |
| `prompt_instance_id` | opaque string | Run input ID. |
| `bundle_id` | opaque string | Join key. |
| `condition` | enum `F0`, `F1`, `F2` | Not included in prompt text. |
| `prompt_version` | string | Immutable template version. |
| `system_text` | string | Exact system message. |
| `user_text` | string | Exact user message. |
| `system_sha256`, `user_sha256` | lowercase 64-hex | Prompt integrity. |
| `input_token_count` | non-negative integer | Exact count from locked tokenizer. |
| `target_input_token_count` | positive integer | Per-bundle parity target. |
| `token_parity_pass` | boolean | Must be true for F1/F2 primary pair. |
| `max_new_tokens` | integer; fixed at 128 | Same in all conditions. |
| `retrieval_calls`, `tool_calls` | integer; fixed 0 | No retrieval/tool condition in this first study. |
| `metadata_slot_token_counts` | object | Per-slot counts for audit. |
| `report_text_sha256s` | map report ID → hash | Ensures identical evidence. |

### 4.7 `run_records.jsonl`

One line per model invocation, including failed calls.

| Field | Type/constraint | Meaning |
| --- | --- | --- |
| `run_id` | opaque string | Unique invocation. |
| `prompt_instance_id`, `bundle_id` | opaque strings | Joins. |
| `condition` | `F0`, `F1`, `F2` | Condition. |
| `model_id`, `model_revision`, `tokenizer_revision` | strings | Frozen local model details. |
| `decoder` | object `{temperature:0,top_p:1,do_sample:false,seed:0}` or preregistered seed variant | Exact decoding. |
| `started_at_utc` | ISO 8601 | Run log. |
| `status` | enum `completed`, `runtime_error`, `timeout`, `cancelled` | Runtime state. |
| `input_tokens`, `output_tokens` | non-negative integers | Actual usage. |
| `latency_ms` | non-negative number | Wall-clock latency. |
| `cpu_ms`, `gpu_ms`, `peak_memory_mb` | non-negative number or null | Local resource telemetry; null only with reason. |
| `raw_output_sha256` | lowercase 64-hex or null | Raw output integrity. |
| `error_code` | enum `TIMEOUT`, `CANCELLED`, `BACKEND_ERROR`, `EMPTY_OUTPUT`, `INVALID_UTF8`, `INVALID_JSON`, `DUPLICATE_KEY`, `SCHEMA_ERROR`, `SEMANTIC_ERROR`, `UNKNOWN_EVIDENCE_ID`, `NONE` | Closed run/parser vocabulary; no secrets or stack traces in release artifacts. `NONE` is required for a completed valid run. |

### 4.8 `parsed_outputs.jsonl`

Keep the raw model output unchanged in a separate record. Parsed output is either a valid object or a failure status; no repair or retry is allowed.

```json
{
  "run_id":"RN-...",
  "parse_status":"valid",
  "parsed":{
    "origin_count_supporting":1,
    "claim_state":"supported",
    "confidence":0.72,
    "evidence_ids":["RP-..."]
  },
  "parser_version":"parser-0.1.0",
  "semantic_validation":{
    "evidence_ids_in_bundle":true,
    "unique_evidence_ids":true,
    "count_within_bound":true,
    "confidence_finite":true
  }
}
```

Valid output JSON Schema:

```json
{
  "$schema":"https://json-schema.org/draft/2020-12/schema",
  "$id":"https://example.invalid/origin-accounting/parsed-output.schema.json",
  "type":"object",
  "additionalProperties":false,
  "required":["origin_count_supporting","claim_state","confidence","evidence_ids"],
  "properties":{
    "origin_count_supporting":{"type":"integer","minimum":0,"maximum":6},
    "claim_state":{"type":"string","enum":["supported","refuted","insufficient","contested"]},
    "confidence":{"type":"number","minimum":0,"maximum":1},
    "evidence_ids":{
      "type":"array","minItems":0,"maxItems":6,"uniqueItems":true,
      "items":{"type":"string","pattern":"^RP-[A-Z2-7]{10}$"}
    }
  }
}
```

### 4.8.1 `raw_outputs.jsonl`

Raw responses are write-once restricted records, never reconstructed from parsed fields:

```json
{"run_id":"RN-...","raw_output_b64":"eyJvcmlnaW5fY291bnRfc3VwcG9ydGluZyI6MX0=","byte_length":29,"raw_output_sha256":"680309c02480775ba41d8e211ff6a793c17b4971869fe8ba201571483483457b"}
```

`raw_output_b64` is the unmodified response byte string encoded with standard Base64 and no line wrapping; `byte_length` must equal the decoded length and the SHA-256 must match the decoded bytes. The parser reads these bytes, records the exact failure or success status, and never overwrites or repairs the raw record. Raw outputs, if later released, require the same privacy/secret review as run logs.

Normative `raw_output.schema.json` constraints:

- required keys are exactly `run_id`, `raw_output_b64`, `byte_length`, `raw_output_sha256`, `parse_status`, and `error_code`; `additionalProperties=false`;
- `parse_status` is one of `valid`, `invalid_utf8`, `invalid_json`, `schema_error`, `semantic_error`, `runtime_error`, `timeout`, or `empty_output`;
- `error_code` uses the closed vocabulary in §4.7 and must be `NONE` iff `parse_status=valid`;
- Base64 must use the RFC 4648 standard alphabet without whitespace; decoding must reproduce exactly `byte_length` bytes and the recorded SHA-256;
- one record exists for every assigned run, including timeout/runtime failure (which may encode the empty byte string); raw bytes are never reconstructed from parsed values.

Conformance fixtures include duplicate keys, non-finite numbers, Unicode and malformed UTF-8, code fences, leading/trailing prose, multiple objects, timeout, empty output, unknown evidence IDs, schema errors, and semantic errors.

Parser contract:

1. Decode UTF-8; strip only surrounding ASCII whitespace.
2. Require exactly one JSON object; leading/trailing prose and Markdown fences are invalid.
3. Reject duplicate JSON keys, unknown keys, wrong types, non-finite numbers, out-of-range integers, duplicate evidence IDs, unknown evidence IDs, or more than six evidence IDs.
4. Do not coerce strings to numbers, repair punctuation, select the first object, truncate arrays, or re-prompt.
5. Store `parse_status` using the closed schema vocabulary above and the matching closed `error_code`; never store a free-text reason in those fields.
6. Invalid output is a failed run in the primary denominator, not missing data to be silently removed.

### 4.9 `qa_records.jsonl`

One line per QA check or audited item.

| Field | Type/constraint | Meaning |
| --- | --- | --- |
| `qa_id` | opaque string | Unique check. |
| `object_id` | string | Bundle, report, graph, or prompt instance. |
| `qa_type` | enum `schema`, `semantic_stance`, `transformation`, `graph_invariant`, `surface_balance`, `split_leakage`, `prompt_parity`, `parser_fixture`, `privacy`, `replay` | Check category. |
| `auditor_id` | pseudonymous string | No personal data in public release. |
| `label` | enum `pass`, `fail`, `uncertain`, `not_applicable` | Outcome. |
| `code` | controlled string | Reason code. |
| `notes` | string ≤1000 chars | No sensitive content. |
| `created_at_utc` | ISO 8601 | Audit time. |

## 5. Proposition and origin-family split logic

### 5.1 Split inventory

Keep the protocol’s 300 primary bundles and add development/pilot material that cannot enter confirmatory analysis:

| Split | Count | Purpose | Can affect primary prompts/analysis? |
| --- | ---: | --- | --- |
| `dev` | 80 (20 per structure) | Grammar, templates, parser fixtures, initial leakage repair | No; may be used during implementation. |
| `pilot` | 40 (10 per structure) | End-to-end feasibility smoke run and power parameter calibration | No efficacy estimate; no test-tuned prompt changes after lock. |
| `primary` | 300 (75 per structure) | Confirmatory paired analysis | Locked before model invocation. |
| `stress` | 60 | Four structures × three nonzero relation-noise rates × five bundles; order, overlap, and code-position variants balanced within the frozen cell table | Secondary descriptive only. |

No `proposition_family_id` may occur in more than one split. No `origin_family_id` may occur in more than one split. A proposition family is the blocking unit even if two bundles use different wording or relation structures. A report artifact, paraphrase, summary, or transformation derived from a proposition family inherits its split. The split validator must also take the transitive closure of `origin_family_id`: if any origin, artifact, or derived report is reused by a bundle, all bundles sharing that lineage are assigned together or the generator fails.

### 5.2 Assignment algorithm

1. Generate a split-independent candidate pool with a fresh master seed.
2. Assign each candidate a unique `proposition_family_id`, one `origin_family_id`, and one or more latent `origin_id` values. Any deliberate reuse makes the affected candidates one blocked origin family rather than independent records.
3. Shuffle candidate families with a cryptographically seeded deterministic permutation.
4. Select exact counts by `origin_structure`: 20 each to `dev`, 10 each to `pilot`, 75 each to `primary`, and 15 each to `stress`. Allocate the 15 stress bundles per structure as five at each noise rate (`0.05`, `0.10`, `0.20`); assign order/overlap/code-position variants with the frozen balanced subcell rule and record `stress_cell_id`.
5. Write the split map once; compute its hash; do not resample after primary prompt generation.
6. Run exact-match, normalized-text, character 5-gram, and token 5-gram duplicate checks across all splits. Any duplicate/near-duplicate family crossing a split invalidates the map and requires regeneration before primary lock.
7. Keep all primary/stress labels and graph truth in restricted files. The public prompt-visible file contains no split or family IDs.

`origin_structure` is balanced in the primary set. `gold_claim_state` is not a confirmatory factor and need not be perfectly balanced; the generator records it for descriptive output-state checks only. Do not report a claim-state-by-structure inferential result from N=300.

Any later FEVER, SciFact, AVeriTeC, or other public-corpus exercise is a separately named `transfer` split with its own count, license review, and construct boundary. It cannot reuse `stress_n=60`, enter the FC/VOR power calculation, or establish real-world origin independence.

### 5.3 Primary/secondary transfer boundary

If a 60-bundle public transfer challenge is later included, create it after the primary prompt and analysis locks. Use FEVER, SciFact, or AVeriTeC only for claim/evidence text and document facts that are actually released by the dataset. Assign `origin_certainty=unknown` unless a documented derivation path exists. Do not use the transfer set in power, primary confidence intervals, or a real-world independence claim.

## 6. Fictional generator grammar

The generator must be deterministic, human-auditable, and independent of the model under test. Do not use the same model family to generate the evidence text and evaluate it. The recommended implementation is a slot grammar plus hand-authored templates and deterministic lexical substitutions; LLM paraphrasing is not used in the primary corpus because it creates provenance and contamination ambiguity.

### 6.1 Slot grammar

```ebnf
<claim> ::= <technical_claim> | <environmental_claim>

<technical_claim> ::= "During the " <site> " test in " <year> ", "
                     <subject> " " <technical_predicate_phrase> " " <object> " by "
                     <magnitude> <unit> " relative to " <baseline> "."

<environmental_claim> ::= "At " <site> " during " <season> " " <year> ", "
                          <subject> " " <environmental_predicate_phrase> "."

<report> ::= <lead> <claim_paraphrase> <method_clause> <caveat_clause>
<lead> ::= <lab_lead> | <release_lead> | <field_lead> | <review_lead>
<method_clause> ::= <measurement_sentence> | <comparison_sentence> | ""
<caveat_clause> ::= <uncertainty_sentence> | <scope_sentence> | ""
```

Slot lists must be versioned and contain only fictional names. Example slots:

```json
{
  "technical": {
    "subjects":["Lumen cache","Orchid relay","Kite index"],
    "objects":["median sync latency","batch completion time","lookup delay"],
    "predicates":["reduced","increased"],
    "units":["percent","milliseconds"],
    "baselines":["the baseline cache","the prior relay","the reference index"]
  },
  "environmental": {
    "subjects":["the Northlake reed plot","the Vesper inlet","the Halcyon ridge"],
    "objects":["salinity index","night-flight count","surface moisture"],
    "predicates":["recorded","did_not_record"],
    "units":["index_points","count","none"]
  }
}
```

The versioned predicate renderer is closed and fail-closed:

| Machine predicate | Allowed domain | Exact canonical phrase body |
| --- | --- | --- |
| `reduced` | technical | `{subject} reduced {object} by {magnitude} {unit} relative to {baseline}` |
| `increased` | technical | `{subject} increased {object} by {magnitude} {unit} relative to {baseline}` |
| `recorded` | environmental | `{subject} recorded {object} at {magnitude} {unit}, compared with {baseline}` |
| `did_not_record` | environmental | `{subject} did not record {object} above {magnitude} {unit}, compared with {baseline}` |

Every predicate has a positive or negative semantic fixture, an exact renderer snapshot, and a render→parse→gold round-trip test. Unsupported predicates and domain/predicate combinations fail generation; no generic fallback phrase is allowed. One hundred percent of dev/pilot claims must pass the render-to-gold truth-state suite before a pilot model call.

Numbers, names, dates, and wording must be sampled independently of `origin_structure` except where the structure requires a transformation. The proposition’s claim text is generated once; report texts are generated separately from the same proposition slots.

### 6.2 Report styles

Use four hand-authored styles, assigned independently of origin structure:

| Style | Required content | Prohibited shortcut |
| --- | --- | --- |
| `lab_note` | measurement, comparator, date, caveat | no fixed “independent” phrase |
| `release_note` | observed result, version, scope | no origin/count phrase |
| `field_log` | site observation, method, date | no structure-specific punctuation |
| `review_note` | summary of a result, limitation | no “copied from” language |

Each structure receives every style in approximately equal numbers. The report text may mention a source organization or artifact date, but those values are opaque and do not encode origin.

### 6.3 Origin structures and transformations

The generator creates a latent graph first, then renders text.

| Structure | Latent graph | Visible relation in F2 | Primary support-origin status |
| --- | --- | --- | --- |
| `one_origin_repetition` | One original supporting artifact; remaining supporting reports derive from it by exact copy, low-overlap paraphrase, or summary. | `DPND` for derived reports; the root/original receives `UNKN` because no parent relation is supplied. | `single` |
| `multiple_origin_convergence` | Three separately authored supporting origins with no derivation edges between them. | `INDP` for each support report as benchmark-stipulated. | `multiple` |
| `unknown_origin` | Reports agree; latent graph may contain one or multiple origins, but the relation is intentionally not certified. | `UNKN` for every relevant report. | `unknown` |
| `conflict` | One supporting origin plus one refuting origin; at least one side has a dependent copy. | `DPND`, `INDP`, or `UNKN` according to graph; relation state is not a truth cue. | `single` on the supporting side; claim state `contested` |

`INDP` means “separate origin in this synthetic graph; not a real-world independence claim.” `UNKN` means “the benchmark withholds certification”; it is not evidence of dependence or independence.

### 6.4 Transformation bands

To prevent copying from being the shortcut:

- `dependent_copy`: exact or near-exact text, but at least 25% of dependent reports must be low lexical overlap after deterministic paraphrase;
- `dependent_paraphrase`: semantic content preserved; paraphrase templates are hand-authored and audited;
- `independent_observation`: independently rendered text, with at least 25% of independent reports deliberately sharing high-overlap domain vocabulary;
- `independent_contradiction`: same topic and method style but opposite claim polarity or a value outside the support interval;
- `summary`: shorter derived text that preserves the relevant claim but drops at least one caveat.

The exact low/high overlap thresholds belong in the generator config and are tested empirically before lock. The specification must not claim successful matching until the leakage suite passes.

### 6.5 Seed derivation

For stable regeneration:

```text
proposition_seed = HMAC(master_seed, "proposition:" + proposition_family_id)
origin_seed       = HMAC(master_seed, "origin:" + proposition_family_id + ":" + origin_structure)
report_seed       = HMAC(master_seed, "report:" + report_id)
style_seed        = HMAC(master_seed, "style:" + report_id)
```

No seed may depend on condition `F0/F1/F2`; the evidence text, report order, and public IDs must be identical across conditions. The relation field is the only intended information difference in the primary F1/F2 contrast.

## 7. F0/F1/F2 prompt templates

The exact prompt strings are versioned and hashed. The templates below are normative in content; punctuation and padding may change only during development before prompt lock.

### 7.1 Shared system message

```text
You are a bounded evidence-counting evaluator.

Return exactly one JSON object with these four keys and no others:
origin_count_supporting, claim_state, confidence, evidence_ids.

origin_count_supporting must be an integer from 0 through 6.
claim_state must be one of supported, refuted, insufficient, contested.
confidence must be a number from 0 through 1.
evidence_ids must be a unique JSON array of report IDs from the bundle.

Do not include Markdown, code fences, explanations, or additional keys.
Use only the claim and reports supplied in this task. Do not infer a provenance relation that is not supplied.

Metadata relation-code legend, when a relation code is present:
DPND means the report is dependent on another observed report or origin path.
INDP means a separate origin in this benchmark; this is a stipulated graph label, not a claim about the real world.
UNKN means the origin relation is unknown and must not be counted as independent.
NONE means no relation cue is supplied in that slot.
```

The legend is present in all conditions. F0/F1 use `NONE` in the relation slot; F2 uses `DPND`, `INDP`, or `UNKN` according to the gold graph. This keeps format and codebook exposure constant while making the relation values the intended information manipulation.

### 7.2 Shared user-message skeleton

```text
Claim:
{{claim_text}}

Reports:
{{reports_block}}

Metadata slots:
{{metadata_block}}

{{condition_instruction}}

Return the required JSON object now.
{{neutral_padding}}
```

`reports_block` is identical across F0/F1/F2, including order. `metadata_block` has one fixed row per report:

```text
- report_id={{opaque_report_id}}; source_id={{opaque_source_id}}; artifact_id={{opaque_artifact_id}}; observed_at={{synthetic_date}}; relation_code={{relation_code}}
```

The model sees no `bundle_id`, `proposition_family_id`, `origin_id`, `origin_structure`, `condition`, or gold field.

### 7.3 Condition instructions

F0:

```text
Assess the claim using the reports. Preserve uncertainty when the supplied evidence does not resolve the claim. Select the report IDs used for your assessment. Do not infer a provenance relation from wording, source ID, artifact ID, date, or report order.
```

F1 and F2, byte-identical:

```text
Count distinct origin pathways when the supplied information permits it. Do not treat repeated or derived reports as independent support. Preserve an unknown origin relation as unknown, and do not infer a relation that is not supplied. Select the report IDs used for your assessment.
```

F2 relation slots use only `DPND`, `INDP`, or `UNKN`. A root/original artifact also receives `UNKN`: it has no supplied parent relation, and the benchmark does not add an `ORIGINAL` code. `NONE` is reserved for the no-cue placeholder in F0/F1. F0 receives neutral padding selected to match F1/F2 token count. F1/F2 use exactly the same instruction and differ only in relation-slot values. No condition name is rendered in the prompt.

### 7.4 Prompt resource accounting

After the model and tokenizer are selected but before the primary split is opened:

1. Render all F2 prompts from the locked evidence text and metadata skeleton.
2. Choose relation code strings and neutral padding from a versioned candidate pool.
3. Tokenize with the exact model tokenizer, with no chat-template mutation after this point.
4. Set each bundle’s `target_input_token_count` to the F2 count.
5. Render F1 and require exact equality to F2 for each bundle. F1/F2 primary parity is zero-token difference, not “within a few percent.”
6. Render F0 and pad to the same per-bundle target. If exact parity is impossible without changing evidence text, fail the prompt-parity gate and revise before primary lock.
7. Enforce `max_total_tokens=2048` and `max_new_tokens=128`. If a prompt exceeds 1920 input tokens, shorten the report grammar before split lock; never truncate a primary report at run time.
8. Record system/user/input/target token counts, slot token counts, output cap, retrieval calls (0), and tool calls (0).

The intended estimand is a benefit of typed relation information at equal model-context length. Runtime and memory costs remain measured secondary outcomes; no monetary cost is assigned to fictional local compute.

## 8. Output parser and semantic evaluator

### 8.1 Parser fixtures

Before primary lock, create at least 20 parser fixtures:

- five valid canonical objects;
- fenced JSON;
- leading prose;
- trailing prose;
- duplicate keys;
- unknown key;
- wrong type for integer/confidence/array;
- `NaN`, `Infinity`, and out-of-range numbers;
- duplicate or unknown evidence ID;
- seven evidence IDs;
- negative origin count;
- confidence as a string;
- multiple JSON objects;
- malformed UTF-8/runtime failure fixture.

The parser must produce the same status and reason code on replay. Do not repair any fixture.

### 8.2 Gold-derived quantities

For bundle (i), read or derive from restricted gold:

- `gold_support_origin_certainty_i ∈ {none, single, multiple, unknown}`;
- `gold_support_origin_count_i` only when certified `none`, `single`, or `multiple`;
- `supporting_report_ids_i`;
- `support_origin_ids_i` and `refute_origin_ids_i` as disjoint stance-specific sets;
- `gold_claim_state_i`;
- `origin_of_report_i` for audit only.

For a parsed output, derive:

```text
hat_n_i = parsed.origin_count_supporting
selected_support_origin_count_i
  = number of distinct latent origin IDs attached to selected evidence IDs
    whose report stance is supports
```

The evaluator uses latent origin IDs only after output storage. For `unknown_origin` bundles, `selected_support_origin_count` may be computed for descriptive audit but is not treated as knowledge available to the model.

### 8.3 Primary and safety formulas

Observed false-corroboration event and fixed-denominator risk codings:

```text
FC_obs(i,c) = 1[valid(i,c)
                  AND hat_n_i >= 2
                  AND gold_support_origin_certainty_i in {none,single,unknown}]

FC_cons(i,c) = 1[NOT valid(i,c) OR FC_obs(i,c)=1]
FC_lib(i,c)  = 1[valid(i,c) AND FC_obs(i,c)=1]
FC_valid(i,c)= FC_obs(i,c), reported only on the locked jointly valid sensitivity set
```

Interpretation: `FC_obs` names an observed model assertion; `FC_cons` is the prespecified risk coding for every assigned run. `unknown` is conservatively treated as not certified multiple. An invalid output is not described as an observed corroboration assertion, but it is a failure for the primary risk-control estimand. All 300 assigned bundle pairs stay in the primary denominator.

Primary contrast:

```text
Delta_FC_cons = mean_A[FC_cons(i,F2)] - mean_A[FC_cons(i,F1)]
```

Here `A` is the fixed set of all 300 assigned primary bundles. Lower is better; a beneficial effect is negative.

Safety denominator for recall of stipulated supporting origins (`VOR` shorthand):

```text
M = {i in A : gold_support_origin_certainty_i == multiple}
VOR(i,c) = 1 if:
  i ∈ M;
  parsed output is valid;
  hat_n_i >= 2;
  selected_support_origin_count_i >= 2;
VOR(i,c) = 0 otherwise.
```

Invalid outputs are `VOR=0`. The set `M` is never intersected with a post-run valid-output set; its exact membership list and hash are frozen in the restricted manifest. The safety contrast is `Delta_VOR = mean_M(VOR_F2) - mean_M(VOR_F1)`. F2 passes the candidate non-inferiority guardrail only when the one-sided 95% lower confidence bound is greater than `-0.05`. This margin is a frozen synthetic-task choice, not a universal claim.

Secondary claim-state accuracy is:

```text
CSA(i,c) = 1[parsed.claim_state == gold_claim_state_i]
```

It is descriptive only. `confidence` is logged; because the output does not contain a full four-class probability vector, report selected-state confidence and correctness descriptively, not as a multiclass Brier score. A future probability-calibration study must extend the schema rather than silently reinterpret this scalar.

### 8.4 Invalid-output policy

Every assigned run remains in the denominator for run completion and the primary `FC_cons` contrast:

- report the all-assigned conservative estimate with invalid outputs risk-coded as `FC_cons=1` as primary;
- report a liberal all-assigned estimate with invalid outputs coded as `FC_lib=0` as a sensitivity;
- report `FC_valid` only on bundles valid in both F1 and F2 as a complete-case sensitivity, with its conditional-on-parseability limitation;
- do not choose the favorable sensitivity after results;
- require at least 98% parseable outputs in each condition and no more than 10% primary-bundle invalidation for data-quality/runtime reasons; if either threshold fails, stop efficacy interpretation.

This is preferable to silently dropping failures or treating malformed output as refusal.

### 8.5 Secondary quality and resource measures

These measures are logged for audit and descriptive reporting; none can rescue a failed `FC` primary contrast.

- **Evidence selection:** for bundles where a gold support set is meaningful, let `S_i` be the supporting report IDs and `E_i` the parsed `evidence_ids`. Report `support_precision_i = |E_i ∩ S_i| / max(1, |E_i|)` and `support_recall_i = |E_i ∩ S_i| / |S_i|` when `|S_i|>0`; report conflict bundles separately because selecting refuting evidence can be appropriate and is not automatically an error.
- **Claim-state accuracy:** report `CSA` overall and by the four structures, with raw counts and intervals only as descriptive summaries. Do not report macro-F1 as a confirmatory endpoint.
- **Cross-field consistency:** derive `count_claim_state_consistent` and `count_selected_evidence_consistent` from frozen rules without changing any model-returned field. `origin_count_supporting` remains the sole count assertion used for FC; disagreements are reported descriptively and are never auto-repaired.
- **Confidence:** report the distribution of the scalar `confidence`, its association with `CSA`, and confidence bins only descriptively. It is not a full probability vector and therefore does not support a multiclass Brier or proper calibration claim in this protocol.
- **Time and context:** report median and 95th-percentile `latency_ms`, `input_tokens`, `output_tokens`, and peak memory by condition. Report paired F2−F1 differences for latency and tokens; do not convert local compute to dollars without a preregistered hardware/energy price model.
- **Decision utility:** no defensible consequence function exists for these fictional bundles, so decision utility is not estimable and must not be invented. A later study must define harms, benefits, and abstention costs before using utility as an endpoint.

## 9. Leakage and shortcut suite

The leakage suite runs before primary lock on `dev` and `pilot`, then once on the locked primary manifest without using model outcomes. Any failed hard test invalidates the affected split.

| Test | Procedure | Acceptance gate |
| --- | --- | --- |
| Exact duplicate | SHA-256 normalized text and report ID-independent serialization across splits | Zero cross-split duplicate proposition/report family. |
| Near duplicate | Character 5-gram and tokenizer 5-gram Jaccard; compare all report pairs across splits | No cross-split pair above the preregistered 0.80 Jaccard quarantine threshold. |
| Proposition leakage | Join on normalized semantic slots, not only text | Zero proposition-family overlap across splits. |
| Condition probe | Replace every relation value and condition-specific instruction with the same byte/token-position-preserving sentinel; use frozen character 3–5-gram TF-IDF, L2 logistic regression, blocked 80/20 proposition-family split, seed `20260818`, inner 5-fold tuning on the training set, and Wilson CI | Accuracy must be ≤0.55 and its 95% Wilson upper bound ≤0.60; otherwise repair formatting/grammar. Publish config and raw predictions. |
| Structure probe | Train a held-out surface classifier on report text, excluding IDs and metadata | Accuracy must not exceed 0.35 for four structures; otherwise inspect and regenerate. |
| Domain/style balance | Cross-tab domain, style, report position, transformation, and structure | No empty cells; maximum absolute proportion difference per style/position ≤0.05 where balance is intended. |
| Lexical overlap | Compute normalized overlap bands by structure and transformation | Mean absolute standardized difference between dependent and stipulated-distinct overlap distributions ≤0.10 on the locked audit sample. This is a hard primary-identification gate; if it fails, downgrade to a descriptive association under the observed surface distribution. |
| Metadata parity | Tokenize every condition with locked tokenizer | F1/F2 input-token difference exactly 0 per bundle; F0 difference exactly 0 after approved padding. |
| Report-order probe | Predict structure from position and formatting only, using the same blocked split/classifier/seed as the condition probe; stance is excluded because it is part of the intended conflict construction | Accuracy at chance + 0.05 maximum with the prespecified CI; otherwise rebalance order. |
| Generator determinism | Regenerate all records with same seed and canonical serializer | Byte-identical records and hashes. |
| Cross-condition text identity | Compare report hashes and order in F0/F1/F2 inputs | Exact equality of claim/reports/IDs/order. |
| Pretraining contamination | Use new fictional text; record creation date, authorship, and no public training corpus reuse | No claim of formal contamination proof; any reused text removes it from primary. |
| Prompt-injection contamination | Scan report text for instruction-like strings, JSON delimiters, control characters, and model-control tokens | Zero unreviewed instruction/control strings; escape or regenerate before lock. |
| Deterministic metadata-only counter | Apply the public relation-code rule without report text | Record its exact output. A model result that merely matches direct countability cannot be described as semantic integration. |
| Field-only model diagnostic | Give the frozen model the same metadata fields and output contract but replace report prose with a fixed sentinel; descriptive stress only | If the F2 effect persists without evidence text, classify it as direct-code/formatting behavior and retire the evidence-integration claim. |

The semantic relation signal in F2 is intentionally detectable through the relation field. The probe requirement applies to **non-semantic** formatting, position, style, and text shortcuts. A classifier that succeeds only by reading the intended relation field is not a leakage finding; it confirms the manipulation exists.

## 10. Annotation and QA codebook

The origin relation is stipulated by the graph. Human QA validates semantic construction and graph integrity; it does not ask annotators to infer real-world independence.

### 10.1 Normative labels

| Field | Values | Codebook rule |
| --- | --- | --- |
| `stance` | `supports`, `refutes`, `neutral` | `supports` if the report asserts the target proposition within scope/time; `refutes` if it asserts the opposite or a directly incompatible value; `neutral` if it only contextualizes or is insufficient. |
| `transformation_type` | `original`, `dependent_copy`, `dependent_paraphrase`, `independent_observation`, `independent_contradiction`, `summary` | Assigned by generator graph. Auditor checks whether the text transformation preserves the declared stance/content. |
| `origin_relation` | `dependent`, `independent_as_stipulated`, `unknown` | `dependent` only when a derivation path is present; `independent_as_stipulated` only when separate origin nodes are intentionally assigned; `unknown` when the relation is withheld. Unknown is not a negative relation. |
| `gold_claim_state` | `supported`, `refuted`, `insufficient`, `contested` | A separate bundle-level label derived from the proposition and report set. It does not determine origin dependence. |
| `surface_overlap_band` | `low`, `medium`, `high` | QA descriptor, not a target label; determined by frozen similarity code. |
| `relation_visibility` | `explicit`, `none` | F2 has explicit relation codes; F0/F1 have `NONE`. |

### 10.2 Audit allocation

- Automated generator tests cover 100% of graph invariants, IDs, split assignment, slot counts, and report hashes.
- Two independent human auditors review claim text and stance/transformation semantics for a stratified 25% sample: equal sampling across four structures, two domains, four styles, and overlap bands.
- A third adjudicator resolves disagreements without seeing model outputs or condition results.
- A second auditor checks all bundles that failed an automated semantic invariant and all 60 stress bundles.
- Human auditors do not label `independent_as_stipulated` from prose; they verify the graph manifest and that no text falsely states the relation as a fact.

Acceptance thresholds and agreement methods are frozen before pilot outputs are inspected:

- stance and transformation raw agreement ≥0.90;
- Cohen’s κ ≥0.80 for nominal stance/transformation labels, with raw agreement, label prevalence, and a bootstrap 95% interval. If the preregistered prevalence diagnostic makes κ unstable, report that fact and use the predeclared Krippendorff nominal alpha—not an outcome-selected statistic;
- every disagreement documented and adjudicated;
- no unresolved disagreement on a primary bundle’s claim polarity or transformation.

The audit sample and strata are frozen before the pilot: two blinded auditors review all 80 development and 40 pilot bundles plus a stratified 25% of primary candidates, balanced across structure, domain, style, and overlap band. `uncertain` is retained as disagreement/failure until adjudicated by the named third auditor; it is never silently removed from a denominator.

If agreement is lower, repair templates/codebook and regenerate affected bundles. Do not use adjudication to hide systematically ambiguous text.

### 10.3 QA reason codes

Use controlled reason codes, for example:

```text
STANCE_AMBIGUOUS
POLARITY_NOT_PRESERVED
CONTRADICTION_NOT_DIRECT
DERIVATION_EDGE_MISSING
ORIGIN_EDGE_EXTRA
UNKNOWN_RELATION_LEAKED
STYLE_STRUCTURE_SHORTCUT
TOKEN_PARITY_FAIL
ID_COLLISION
CROSS_SPLIT_DUPLICATE
PRIVATE_OR_SENSITIVE_TEXT
PROMPT_CONTROL_STRING
```

## 11. Paired analysis and power-simulation design

### 11.1 Analysis object

The primary dataset is a three-condition repeated-measures table with one row per `bundle_id × condition` and one parsed output. The bundle, not the report, is the unit because all reports in a bundle share the same proposition and the model makes one origin-count assertion.

For deterministic decoding, one row per bundle-condition is expected. If the backend is nondeterministic, use exactly three predeclared seeds per bundle-condition and aggregate within bundle-condition before the primary test:

- primary aggregation: majority/median rule fixed before lock;
- seed disagreement rate reported;
- nested bootstrap resamples bundles first, then seeds within bundle;
- no treating 3 seeds × 300 bundles as 900 independent items.

### 11.2 Primary test

Use the exact two-sided McNemar/binomial test over all 300 assigned bundle-level `FC_cons` pairs, with the sign and null fixed before results. Let `b = count(FC_cons_F1=1, FC_cons_F2=0)`, `c = count(FC_cons_F1=0, FC_cons_F2=1)`, and `n_d=b+c`; the primary p-value is `min(1, 2 × min{P[Binomial(n_d,.5)≤min(b,c)], P[Binomial(n_d,.5)≥max(b,c)]})`. Report:

- the fixed primary set `A` with `N=300`; parse status never changes this denominator;
- F1 and F2 `FC_cons` rates;
- absolute risk difference `Delta_FC_cons`;
- 95% paired percentile bootstrap confidence interval from 10,000 resamples of bundles in `A`, using the preregistered analysis seed;
- paired exact/permutation p-value at two-sided α=.05;
- valid-output and invalid-output rates;
- liberal all-assigned `FC_lib` and jointly-valid `FC_valid` sensitivity estimates, with the latter explicitly conditional on paired parseability.

A bounded superiority claim requires a beneficial point estimate, two-sided exact `p<.05`, and a 95% interval whose upper bound is below zero. The `−0.08` difference is a planning/practical benchmark reported separately; it is not silently treated as a second pass/fail threshold.

A mixed-effects logistic model is a secondary robustness analysis only; with one item per bundle-condition, the paired test is easier to audit and avoids pretending the synthetic report count is independent evidence.

### 11.3 Safety analysis

Compute the F2−F1 difference in `VOR` on the fixed manifest set `M={i in A: gold_support_origin_certainty_i=multiple}`. Do not intersect `M` with any valid-output set; invalid outputs are `VOR=0`. Record `|M|` and the membership-list hash. Report the absolute difference and the prespecified paired-binary interval. Claim non-inferiority only if the one-sided 95% lower confidence bound for `Delta_VOR` is greater than `−0.05`; publish the interval method, bundle-level bootstrap seed if used, and coverage simulation for the actual `|M|`.

### 11.4 Power simulation algorithm

The simulation is a planning artifact, not an analysis of observed pilot outcomes. Use a fixed simulation seed and publish the code/config.

For each grid point:

```text
baseline_FC ∈ {0.20, 0.30, 0.40}
discordance ∈ {0.10, 0.20, 0.30}
beneficial_delta ∈ {-0.05, -0.08, -0.10}
N ∈ {240, 280, 300, 320, 360}
```

Add a separate `beneficial_delta=0.00` null grid (with the same baseline, discordance, and N values) for type-I-error and interval-coverage checks; do not infer type-I behavior from the nonzero-effect grid.

Construct paired binary outcomes using probabilities:

```text
p10 = P(FC_F1=1, FC_F2=0)  # improvement direction
p01 = P(FC_F1=0, FC_F2=1)  # harm direction
p11 = baseline_FC - p01
p00 = 1 - p10 - p01 - p11
```

Choose `p10 - p01 = -beneficial_delta` and `p01 + p10 = discordance`, subject to valid probabilities. Simulate 10,000 replications per grid point, run the exact predeclared paired test, and record power, type-I error under delta=0, interval coverage, and probability of passing the safety gate. Also simulate invalid-output rates of 0%, 2%, 5%, and 10% under both conservative and liberal coding.

Run a separate VOR planning grid with fixed `|M|` (expected 75), `baseline_VOR ∈ {0.70,0.80,0.90,0.95}`, paired discordance `∈ {0.05,0.10,0.20}`, `Delta_VOR ∈ {0,-0.02,-0.05,-0.08}`, and invalid rates `∈ {0,0.02,0.05,0.10}` coded as zero. Simulate the exact one-sided non-inferiority decision at least 10,000 times per cell and report coverage and probability of passing. If the five-point margin is not estimable with adequate precision at the fixed `|M|`, downgrade VOR to a descriptive guardrail and remove “non-inferior” before preregistration; do not enlarge the sample or loosen the margin after inspecting pilot outcomes.

**Sample decision:** retain `N=300` as the protocol target. If the prespecified minimum useful effect (candidate −0.08) does not reach 80% power at plausible baseline/discordance values, do not quietly increase N; downgrade the paper to estimation/feasibility or preregister a new protocol version before data access. Do not use the pilot effect to justify a favorable N, consistent with [Leon, Davis, & Kraemer (2011)](https://doi.org/10.1016/j.jpsychires.2010.10.008). Effect sizes and practical thresholds should be documented before confirmatory runs, as recommended by [Lakens (2013)](https://doi.org/10.3389/fpsyg.2013.00863).

### 11.5 Multiplicity

Confirmatory family:

1. F2 versus F1 on `FC` (one primary contrast);
2. F2 versus F1 on `VOR` as a safety/non-inferiority gate, not a second superiority claim.

No secondary inferential family is authorized in protocol 0.3. F1-versus-F0, F2-versus-F0, claim-state accuracy, stress-set FC, domain, structure, style, seed, and optional-model slices are descriptive/exploratory with raw counts and uncertainty summaries. They cannot rescue a failed primary endpoint or safety gate. A later protocol may add inferential contrasts only by defining an estimand, decision rule, multiplicity adjustment, and power plan before data access.

## 12. Fixed stopping and pilot acceptance gates

### 12.1 Fixed stopping

Before primary lock, freeze the corpus, split map, prompt templates, tokenizer, model hash, parser, analysis code, thresholds, and release boundary. Run all assigned F0/F1/F2 primary calls once in randomized run order. No efficacy peeking, adaptive resampling, prompt changes, or model changes are allowed after the first primary output.

Permitted early termination:

- private/secret/sensitive material enters the corpus or output;
- unauthorized live/paid retrieval or tool call occurs;
- cross-condition contamination or gold leakage is detected;
- irrecoverable manifest/hash corruption occurs;
- runtime failure invalidates more than 10% of assigned primary bundles;
- a security/injection event propagates across calls.

Any early stop writes a quarantine receipt with the affected IDs and reason. Quarantined runs are not interpreted as evidence for or against F2.

### 12.2 Pilot sequence

The 40-bundle pilot is strictly development/feasibility:

1. schema validation and deterministic generation;
2. predicate-renderer round-trip truth tests, semantic audit, and graph invariants;
3. prompt token parity and max-context check;
4. parser fixture suite;
5. 40-bundle F0/F1/F2 smoke run on the frozen local model;
6. replay and resource ledger check;
7. reproducible leakage/format probes plus deterministic metadata-only and field-only diagnostics;
8. FC and VOR power simulations and all-assigned analysis dry run.

Pilot results may repair templates/parser/thresholds only before primary lock. They may not be reported as efficacy and may not be used to choose a favorable endpoint.

### 12.3 Pilot acceptance gates

All gates must pass before opening primary data:

| Gate | Acceptance criterion | If failed |
| --- | --- | --- |
| G0 schema | 100% dev/pilot records validate; zero duplicate IDs or malformed JSONL lines | Repair schema/generator; regenerate affected files. |
| G1 determinism | Same seed/config regenerates byte-identical JSON and hashes | Stop; fix seed/serializer before proceeding. |
| G2 graph integrity | 100% graph invariants pass; every report has exactly one latent origin and valid derivation state | Stop; no primary generation. |
| G3 semantic QA | Stance/transformation agreement thresholds pass; no unresolved primary-like ambiguity | Repair templates or downgrade claim. |
| G4 split leakage | Zero cross-split proposition/origin family overlap; duplicate thresholds pass | Regenerate split; do not patch IDs post hoc. |
| G5 prompt parity | F1/F2 exact input-token parity per bundle; F0 exact after approved padding; all prompts ≤1920 input tokens | Revise slot/padding grammar; if impossible, stop. |
| G6 parser | All 20+ fixtures map to expected statuses; no silent repair | Fix parser; rerun fixtures. |
| G7 pilot runtime | At least 98% parseable pilot outputs, zero unrecorded runtime state, replay within declared deterministic/seed behavior | Repair runtime; pilot is not evidence. |
| G8 shortcut suite | All hard leakage probes pass; deterministic/field-only diagnostics are recorded; no retained overlap failure is allowed for a semantic-integration claim | Regenerate or narrow to direct-code/formatting behavior. |
| G9 power | Published FC and VOR simulations demonstrate target operating characteristics or the predeclared downgrade | Do not claim superiority/non-inferiority if the corresponding decision is underpowered or too imprecise. |
| G10 governance | Synthetic-only status, licenses, frozen model/tokenizer provenance, raw-output privacy/secret scan, no live/paid calls, and owner release authorization are recorded | Quarantine and stop. |

### 12.4 Preregistration lock

Before opening the primary split or writing any primary model output, archive a timestamped preregistration containing the exact question, all-assigned `FC_cons` estimand, fixed-set VOR formula, bundle unit, `N=300`, `M` membership hash, structure/stress allocation, generator version and seed derivation, split and leakage rules, F0/F1/F2 prompt hashes, selected model/tokenizer hashes, decoder, raw-output schema, parser and invalid-output policy, resource caps, primary/safety decision rules, both power grids and simulation seeds, descriptive/exploratory policy, human-QA sampling and agreement gates, early-stop rules, release boundary, version pair, and permitted claim ladder. The preregistration receives a SHA-256 recorded in the manifest. Any later change is a versioned deviation; it cannot silently alter the primary endpoint, denominator, sample size, or stopping rule.

## 13. Release manifest and reproducibility package

### 13.1 Canonical `manifest.json`

```json
{
  "study_id":"OA-TPC-001",
  "protocol_version":"0.3",
  "specification_version":"loop3-operationalization-0.3",
  "schema_version":"1.0.0",
  "status":"design_only",
  "claim_boundary":"oracle-cue origin accounting on stipulated synthetic provenance graphs",
  "primary_n":300,
  "pilot_n":40,
  "stress_n":60,
  "stress_design":"4 structures x 3 nonzero noise rates x 5 bundles; balanced order/overlap/code-position subcells",
  "split_policy":"proposition_family_and_origin_family_blocked",
  "generator":{"name":"oa-slot-grammar","version":"0.1.0","seed_derivation":"HMAC-SHA256"},
  "model":{"id":"UNSELECTED","revision":null,"tokenizer_revision":null},
  "conditions":["F0","F1","F2"],
  "primary_contrast":"F2_minus_F1_all_assigned_FC_cons",
  "safety_endpoint":"stipulated_support_origin_recall_noninferiority_fixed_M",
  "canonicalization":"RFC8785",
  "data_status":"synthetic_only",
  "licenses":{"generator_template":null,"model":null,"tokenizer":null,"transfer_datasets":[]},
  "privacy_secret_scan":{"status":"not_run","report_path":null},
  "files":[],
  "qa":{"status":"not_run","report_path":null},
  "preregistration":{"url":null,"sha256":null},
  "owner_release_authorization":false,
  "release_policy":"no_public_release until explicit owner authorization and privacy/license review"
}
```

At study lock, replace `UNSELECTED`, null licenses, and empty file entries with exact values. Each file entry must contain `path`, `sha256`, `bytes`, `rows`, `schema_id`, and `visibility` (`public_prompt`, `restricted_gold`, `restricted_run`, `release_candidate`). Record model/checkpoint/tokenizer license and revision, generator/template license, any separately named transfer dataset’s version/license/redistribution terms, the synthetic-only boundary, and a clean privacy/credential scan. The manifest itself is RFC 8785-canonicalized and hashed after all entries are complete.

### 13.2 Required release files if later authorized

- all schema JSON files;
- generator code, slot tables, transformation templates, and exact seeds or a release regeneration mechanism;
- public proposition/report/bundle files, subject to licensing and redaction review;
- restricted gold graph only if safe and authorized; otherwise release hashes and a generator;
- exact prompt templates and tokenizer/model configuration hashes;
- parser, analysis code, power simulation, and unit-test fixtures;
- complete run ledger, raw outputs, parsed outputs, invalid outputs, and quarantine receipts;
- QA codebook, audit sample, disagreement/adjudication log, and leakage report;
- preregistration URL/hash and deviations log;
- environment lockfile and hardware/runtime description.

Never include credentials, tokens, cookies, private prompts, private source text, or hidden master seeds that would expose another system. Provenance metadata must not be used to reconstruct sensitive material.

## 14. Remaining infeasible or ambiguous choices

| Issue left by the protocol | Risk | Consolidated decision |
| --- | --- | --- |
| The prospectus says to make matched pairs where only origin structure changes. | Exact text cannot simultaneously realize every structure (especially conflict versus support-only) without either changing the claim/stance or assigning different latent graphs to identical prose; forcing that match would create a new estimand and can make truth construction incoherent. | Use the within-bundle F1/F2 pair as the only confirmatory match. Treat the four structures as balanced strata, not paired counterfactuals. If cross-structure matched sets are later desired, add an explicit `match_set_id` and a new protocol before generation; do not retrofit them after seeing results. |
| Exact relation-code tokenization varies by model tokenizer. | “Matched slot length” could be asserted without being true. | Select model/tokenizer before prompt lock; calibrate candidate codes and padding; require exact F1/F2 equality per bundle; if impossible, stop. |
| F0’s generic instruction is semantically shorter than F1/F2’s rule. | F0 may differ for verbosity/instruction, not only no rule. | Pad F0 to exact input length; treat F0 comparisons as secondary. Primary is F2 versus byte-identical-rule F1. |
| `claim_state` is underspecified for unknown-origin bundles. | Claim truth and origin certification are different; forced alignment creates construct contamination. | Generate a separate gold claim state, score it descriptively only, and exclude it from primary balance/power. |
| Scalar `confidence` is not a full probability distribution. | Calling it Brier would be methodologically incorrect. | Keep the field for logs; report no multiclass Brier. Extend the output schema in a later calibration study. |
| Unknown-origin latent graph can contain multiple origins. | Treating unknown as one origin or as independent changes the endpoint. | Store `gold_support_origin_certainty=unknown`; conservative FC risk-codes `hat_n≥2` as an error when valid; exclude unknown from fixed set `M`. |
| Synthetic “independent” reports may share generated slots. | Surface similarity or common templates can be mistaken for origin dependence. | Cross overlap/style and run probes; describe `independent_as_stipulated`, never real-world independence. |
| Model selection before primary split. | Prompt/model choice can become test-set tuning. | Select one local model and hash before primary prompt generation; optional second model is unpowered robustness. |
| Public transfer set availability/licensing. | Transfer can introduce contamination, unclear origin, or sensitive content. | Make it optional secondary after lock; if licensing/graph truth is unclear, omit it entirely. |
| Invalid outputs and runtime failures. | Dropping them can make the intervention look safer. | Use all-assigned `FC_cons` as primary, fixed-set invalid=`0` VOR, and publish liberal/complete-case sensitivities without changing denominators post hoc. |
| Human semantic audit capacity. | Under-audited text invalidates synthetic truth. | Audit all dev/pilot and stratified 25% primary with two independent auditors; if thresholds fail, no primary run. |

The one decision that must not remain open is tokenizer/resource parity. If it cannot be achieved, the study should not be described as a matched-resource cue comparison.

## 15. Feasibility verdict and claim ladder

### Feasibility verdict

This specification is executable as an offline benchmark if the authors implement the generator, schemas, tokenizer-calibration builder, parser, evaluator, QA suite, and power simulation before primary lock. It is **not** an executable plan for validating the discrimination layer as a whole.

The main remaining technical risk is not sample size; it is whether text construction and metadata formatting can pass the shortcut suite while retaining plausible linguistic variation. If that risk cannot be controlled, the honest output is a synthetic proof-of-concept or benchmark artifact, not an efficacy paper.

### Claim ladder

| Evidence after this specification | Permitted statement |
| --- | --- |
| Generator and schema only | “We specify a reproducible oracle-cue benchmark design.” |
| Pilot gates only | “The benchmark and runtime are feasible under these checks.” No efficacy claim. |
| Primary F2<F1 with safety pass and leakage gates | “For the tested frozen model, the typed-cue condition produced less all-assigned risk-coded false corroboration than the rule-only condition on these fictional bundles, while the stipulated-support-origin safety gate passed.” |
| Primary null/unstable/harmful | “The tested cue did not demonstrate a robust benefit under these conditions”; narrow or retire the mechanism. |
| Later noisy-relation study | Possible claim about robustness to relation error; still not provenance discovery or real-world independence. |
| Later human study | Separate claim about correction/reliance on a bounded interface; not inherited from this benchmark. |

No result from this study permits “better decisions,” “human oversight solved,” “real-world independent corroboration,” “enterprise readiness,” or “validated discrimination layer.”

## 16. Authoritative and primary anchors

These sources constrain the design but do not validate the proposed benchmark or intervention.

- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12/schema) — machine-readable schema contract.
- [JSON Lines specification](https://jsonlines.org/) — one UTF-8 JSON value per line.
- Zhang, Y., Ives, Z., & Roth, D. (2020), natural-language claim provenance. [ACL Anthology](https://aclanthology.org/2020.acl-main.406/).
- [W3C PROV-O recommendation](https://www.w3.org/TR/prov-o/) — provenance vocabulary; lineage is not correctness or authorization.
- [Cochrane Handbook, Chapter 4](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04) — authoritative precedent for collating reports sharing an underlying study; not a validation of synthetic origin labels.
- Thorne et al. (2018), FEVER. [DOI 10.18653/v1/N18-1074](https://doi.org/10.18653/v1/N18-1074).
- Wadden et al. (2020), SciFact. [DOI 10.18653/v1/2020.emnlp-main.609](https://doi.org/10.18653/v1/2020.emnlp-main.609).
- Schlichtkrull, Guo, & Vlachos (2023), AVeriTeC. [arXiv:2305.13117](https://arxiv.org/abs/2305.13117).
- Laitenberger, Manning, & Liu (2025), stronger RAG baselines. [DOI 10.18653/v1/2025.emnlp-main.1656](https://doi.org/10.18653/v1/2025.emnlp-main.1656).
- Cronbach & Meehl (1955), construct validity. [DOI 10.1037/h0040957](https://doi.org/10.1037/h0040957).
- Campbell & Fiske (1959), convergent/discriminant validation. [DOI 10.1037/h0046016](https://doi.org/10.1037/h0046016).
- Lakens (2013), effect sizes and power planning. [DOI 10.3389/fpsyg.2013.00863](https://doi.org/10.3389/fpsyg.2013.00863).
- Leon, Davis, & Kraemer (2011), pilot-study interpretation. [DOI 10.1016/j.jpsychires.2010.10.008](https://doi.org/10.1016/j.jpsychires.2010.10.008).
- Eldridge et al. (2016), CONSORT pilot/feasibility extension. [DOI 10.1186/s40814-016-0105-8](https://doi.org/10.1186/s40814-016-0105-8).

The artifact becomes a study only after the schema, corpus, prompts, parser, analysis, QA, thresholds, model hash, and release boundary are frozen and preregistered. Until then it is an implementation specification, not evidence.

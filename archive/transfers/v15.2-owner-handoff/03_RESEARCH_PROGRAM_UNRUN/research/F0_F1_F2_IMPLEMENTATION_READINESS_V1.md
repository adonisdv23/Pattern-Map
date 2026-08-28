# F0/F1/F2 implementation readiness v1

**Prepared:** 2026-08-18
**Status:** `OFFLINE_SCAFFOLD_ONLY_NOT_PRIMARY_READY`
**Protocol baseline:** `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md` v1.0
**Historical compatibility inputs:** `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V0.md` v0.3 and `research/overnight/rounds/08_LOOP2_OPERATIONALIZATION_SPEC.md` `loop3-operationalization-0.3` (superseded; not the protocol identity)
**Scope:** deterministic synthetic data, contracts, parser, scoring, diagnostics, receipts, and planning-only simulation.
**Explicit non-scope:** model selection or invocation, provider/network calls, retrieval, Cloud Run, paid services, human participants, preregistration, or an empirical result.

## Answer first

The F0/F1/F2 protocol is now represented by an offline, standard-library-only
scaffold that can generate fictional provenance-controlled records, build
condition prompts, reject malformed outputs without repair, score the locked
all-assigned false-corroboration endpoint, calculate the fixed-set supporting-
origin safety guardrail, emit hashed local receipts, and attach a separate
descriptive sidecar for origin-count and selected-support-origin diagnostics.

This is not a readiness-to-run or readiness-to-claim result. The model and its
intended tokenizer remain unselected, the committed tokenizer is an explicitly
labelled deterministic surrogate, no primary corpus has been opened, and no
model output exists. The implementation is ready for independent code review
and further pre-lock QA. It is not authorized to run a model.

The protocol estimand is preserved exactly:

```text
primary = Delta_FC_cons = mean_A[FC_cons(F2)] - mean_A[FC_cons(F1)]
```

where `A` is the fixed set of all assigned primary bundles and invalid outputs
are conservative risk-coded as failures. The safety denominator is the fixed
manifest set `M` of bundles whose stipulated supporting-origin certainty is
`multiple`; it is never intersected with post-run valid outputs. F2 remains
the same explicit origin-counting rule as F1 plus typed benchmark-stipulated
relation values. F0 remains the ordinary citation-only condition.

## What is implemented

The implementation is intentionally local and dependency-free:

| Area | Implemented artifact | Boundary that remains explicit |
| --- | --- | --- |
| Configuration | `research/origin_accounting/config/frozen_config.json` and `tools/origin_accounting/config.py` | `model_id=UNSELECTED`; no tokenizer revision; no primary lock |
| Record contracts | Ten JSON Schema Draft 2020-12 files under `research/origin_accounting/schema/` | Cross-record invariants still require an independent validator before release |
| Generator | `tools/origin_accounting/generator.py` | Slot grammar and hand-authored transformations; no LLM paraphrasing or public corpus |
| Prompt construction | F0/F1/F2 builder with fixed metadata slots, order, styles, relation codes, and neutral padding | Parity currently uses `deterministic-regex-surrogate-v1`, not the intended model tokenizer |
| Output parser | `tools/origin_accounting/parser.py` | Raw bytes are immutable; malformed output is never repaired, truncated, or retried |
| Primary/safety/secondary scoring | `tools/origin_accounting/analysis.py` | Confirmatory mode requires the ordered 300-row A / 75-row M manifest; descriptive smoke mode is explicitly non-confirmatory; secondary evidence/origin diagnostics remain undefined for invalid and unknown-origin rows |
| Leakage and shortcut diagnostics | `tools/origin_accounting/diagnostics.py` | Nearest-centroid surface check is a smoke diagnostic, not the preregistered TF-IDF probe |
| Planning simulation | `tools/origin_accounting/power.py` | Planning-only; it consumes no pilot or model outcomes |
| Receipts/CLI | `tools/origin_accounting/cli.py` | Receipts are local; public release remains unauthorized |
| Focused tests | `tests/test_origin_accounting.py` | Tests run offline with Python 3.9 standard library |

The smoke command is:

```sh
python3 -m tools.origin_accounting.cli smoke --out /private/tmp/oa-smoke
```

It emits one synthetic bundle per structure in each split, all three prompt
conditions, data hashes, parity flags, split/near-duplicate diagnostics,
relation-noise fixtures, and a receipt with zero model/provider/network calls.
The protocol-sized generator is available with `generate --out`; its output
is still design material and cannot enter a primary analysis without the
remaining gates.

## Estimand and condition lock

The implementation carries forward the distinctions in the protocol and
thesis/terminology contract:

| Condition | Prompt-visible information | Estimand role |
| --- | --- | --- |
| **F0** | Same claim/reports/opaque IDs/dates; `NONE` relation placeholders; citation-only instruction | Secondary ordinary bounded evidence baseline |
| **F1** | Same evidence and `NONE` placeholders; explicit rule to count distinct pathways, avoid repeated/derived independence, and preserve unknown | Primary rule-only comparator |
| **F2** | Byte-length/token-parity-matched F1 rule; fixed relation slots populated with `DPND`, `INDP`, or `UNKN` from the stipulated graph | Primary typed-cue intervention |

`INDP` is rendered and documented as **independent-as-stipulated** only. It
means separate origin nodes in the synthetic graph; it does not establish
real-world causal or epistemic independence. `UNKN` is an unresolved relation,
not a dependent relation and not an independent relation. A root/original
report receives `UNKN` in F2 because no parent relation is supplied; no hidden
`ORIGINAL` cue was added.

The prompt builder keeps the claim, report text, report IDs, report order, and
metadata row shape constant across conditions. F1 and F2 instructions are byte
identical. Relation codes all occupy four ASCII bytes. F0 is length-padded
with neutral `PAD` tokens; F0 comparisons remain secondary. The builder
validates, per bundle:

1. exact equality of F1/F2 input token counts under the local tokenizer;
2. exact equality of F1/F2 input byte lengths;
3. exact equality of F0/F1/F2 input byte lengths in the scaffold;
4. exact equality of the report text hash map and order across conditions; and
5. fixed output cap, zero retrieval calls, and zero tool calls.

The byte-length check is an implementation-level resource-control guard. It
does not change the protocol's F2-versus-F1 estimand.

### Secondary descriptive scorer sidecar

`score_output` now returns the protocol-listed descriptive measures without
changing the primary or safety fields:

- `absolute_origin_count_error` when the valid output is compared with a
  certified gold support-origin count;
- selected supporting-origin-set precision, recall, and exact match;
- an explicit scope/exclusion reason for invalid and unknown-origin rows, with
  conflict rows retained as a separate certified scope.

The paired analysis emits these under `secondary_descriptive`, including scope
summaries that keep certified non-conflict, certified conflict, unknown, and
invalid rows distinct. They are descriptive only. Invalid outputs are not
imputed, unknown-origin gold is not treated as latent truth, and neutral or
refuting evidence selections are not treated as support-selection errors. The
scorer only derives origin metrics from selected reports whose benchmark
stance is `supports` on certified non-contested rows; contested rows remain
visible but unscored for support-only sets, leaving
`FC_cons`, `VOR`, the fixed denominators, and the confirmatory decision
unchanged.

An empty selected support-origin set reports precision as undefined (`None`),
not zero. An empty certified gold support-origin set reports recall as
undefined, while exact-set match remains `1` when both sets are empty. The
scorer does not coerce these cases into misleading numeric values.

Because the current generator makes every `stance=supports` report part of the
restricted support set, a wrong-stipulated-origin fixture cannot be created
without violating the corpus contract. The lane therefore does not emit a
false-origin or misassignment metric; the retained set metrics describe
selected-support-origin omission and exact-set coverage only.

## Data and trust boundary

The schema layout follows the operationalization specification:

```text
origin-accounting/
  schema/       proposition, report, bundle, graph, prompt, run, raw, parsed, QA
  data/         propositions, reports, public bundles, restricted gold, graphs, split map
  prompts/      F0/F1/F2 prompt instances
  runs/         write-once run/raw/parsed/QA receipts (not produced by this lane)
  analysis/     primary plan and planning simulation receipts
  release/      manifest and file hashes
```

The generator distinguishes prompt-visible records from restricted gold. The
model must never receive proposition-family IDs, origin-family IDs, origin IDs,
gold state, supporting-origin counts, split labels, structure labels, or the
condition name. The evaluator joins gold only after raw output bytes are
immutable. The code never contacts a provider to make that join.

Opaque identifiers are derived with HMAC-SHA256 and RFC 4648 Base32 characters
under a local master seed. IDs contain no structure, split, relation, or
condition semantics. The master seed is configuration for this local scaffold,
not a release authorization. Any later public release requires an explicit
release seed policy and owner approval.

The graph validator checks unique nodes, no dangling edges, report/artifact
coverage, split family blocking, and the count/certainty invariant:

```text
gold_support_origin_count = null  iff  gold_support_origin_certainty = unknown
0 → none; 1 → single; 2–6 → multiple
```

Graph origin membership is construction truth for this benchmark only. It does
not imply source honesty, authority, causal independence, permission, or claim
truth.

## Synthetic corpus and fixture design

The deterministic slot grammar creates four balanced structures:

1. **One-origin repetition:** one supporting origin with exact-copy,
   low-overlap paraphrase, and summary transformations.
2. **Multiple-origin convergence:** three separately authored supporting
   origins plus a neutral report; all distinctness is stipulated by the graph.
3. **Unknown origin:** agreement is visible but origin certification is withheld;
   the latent graph may contain multiple origins while the scored state remains
   `unknown`.
4. **Conflict:** one supporting origin and one refuting origin, with dependent
   copies on each side; supporting and refuting origin sets remain separate.

Four report styles are crossed with structure and report position. Deterministic
lexical variation is crossed with structure and style to make exact/near
duplicate detection meaningful. No report text says “independent,” “copied,”
or “unknown”; those are graph/evaluator labels. The reports are fictional,
future-dated, and generated without a model.

The fixture layer includes:

- a small four-structure-per-split corpus for deterministic smoke tests;
- relation-noise values `0.05`, `0.10`, and `0.20` in the stress inventory;
- a direct metadata-only counter for `DPND`/`INDP`/`UNKN`;
- a field-only no-report-text diagnostic that never calls a model; and
- strict parser fixtures for valid JSON, code fences, leading/trailing prose,
  duplicate keys, unknown keys/IDs, wrong types, non-finite numbers, too many
  IDs, multiple objects, empty output, and malformed UTF-8.

Stress relation noise changes only visible F2 cue values; gold graph truth is
never mutated. Unknown-origin fixtures remain unknown in the evaluator and are
conservatively included in the all-assigned false-corroboration risk coding
when a valid output asserts two or more supporting origins.

## Parser and invalid-output policy

`parse_output` accepts immutable bytes and performs these checks in order:

- UTF-8 decode and empty-output handling;
- exactly one JSON object after surrounding ASCII whitespace only;
- duplicate-key rejection through an object-pairs hook;
- exact four-key schema and closed claim-state vocabulary;
- integer `origin_count_supporting` in `[0,6]`;
- finite confidence in `[0,1]`;
- unique evidence IDs, valid opaque ID syntax, and bundle membership.

It does not coerce types, select the first JSON object, strip Markdown fences,
repair punctuation, truncate arrays, re-prompt, or infer an evidence ID. Raw
bytes are stored separately from parsed values, with Base64, byte length, and
SHA-256 receipt. Invalid outputs remain assigned failures.

For the primary endpoint:

```text
FC_obs  = valid AND hat_n >= 2 AND gold_certainty ∈ {none,single,unknown}
FC_cons = NOT valid OR FC_obs
FC_lib  = valid AND FC_obs
```

`FC_cons` is the primary all-assigned risk coding. Liberal and complete-case
variants are sensitivities only and cannot be chosen after results. For the
fixed safety set `M`, invalid outputs receive `VOR=0`; `M` is frozen from gold
membership and is never derived from parseable outputs.

## Diagnostics and contamination controls

Implemented diagnostics include:

- proposition-family and origin-family split blocking;
- exact normalized-text and character 5-gram near-duplicate checks;
- condition-invariant report order and report hash checks;
- structure/domain/style/position balance inventory;
- deterministic surface-only smoke probe;
- metadata-only direct-code counter;
- field-only no-report-text diagnostic;
- relation-noise/unknown fixtures; and
- deterministic regeneration and local hash receipts.

The nearest-centroid surface probe is deliberately labelled a smoke diagnostic.
Before primary lock it must be replaced or supplemented by the specified
blocked character/token TF-IDF probe with the preregistered ceiling and Wilson
interval. A direct-code-only result or a field-only result must not be called
semantic evidence integration. A formatting/position/style result must be
treated as shortcut leakage and repaired or narrowed before any efficacy
interpretation.

The implementation does not claim formal pretraining-contamination proof. The
generator uses new fictional text, no public corpus, no private data, and no
external model. Any future reuse of public data belongs to a separate,
post-lock descriptive transfer split with `unknown` origin unless a documented
derivation path exists.

## Planning-only power scaffolding

`tools/origin_accounting/power.py` contains paired-Bernoulli simulation helpers
for the protocol's FC grid (`baseline ∈ {0.20,0.30,0.40}`, discordance
`{0.10,0.20,0.30}`, delta including `0`, `-0.05`, `-0.08`, `-0.10`, the
planned N values, and invalid rates `{0,0.02,0.05,0.10}`). It defaults to the
protocol's 10,000 repetitions per valid cell when explicitly invoked:

```sh
python3 -m tools.origin_accounting.cli power --out /private/tmp/oa-power --repetitions 10000
```

The simulation is a planning artifact only. It does not consume pilot results,
choose N, tune a prompt, or establish a model effect. The fixed-`M` VOR helper
is clearly labelled a normal-interval scaffold requiring coverage validation;
it is not a substitute for the preregistered paired safety interval.

## Receipts and frozen configuration

The smoke/generate receipts record:

- protocol/specification/schema/generator/parser versions;
- split counts and condition names;
- primary contrast and fixed-set safety endpoint;
- descriptive origin-count and selected-support-origin sidecar metrics, with
  their undefined/exclusion reasons;
- model `UNSELECTED`, null revision fields, and surrogate tokenizer status;
- per-file bytes, rows, and deterministic local hashes;
- parity, split, surface, style, order, noise, and parser fixture diagnostics;
- `model_calls=0`, `provider_calls=0`, `network_calls=0`; and
- `owner_release_authorization=false`.

The local canonical JSON helper sorts object keys, emits compact UTF-8, and
rejects non-finite values. It is intentionally labelled
`deterministic-json-v1`; it is **not** a claim of RFC 8785 conformance. A
publication/release manifest must use an independently tested RFC 8785
implementation and retain conformance fixtures for Unicode, nested maps,
arrays, negative zero, and number boundaries.

## Offline checks run

The focused tests run with the system Python 3.9 standard library; no network
or model backend is involved:

```text
python3 -m unittest discover -s tests -p 'test_*.py' -v
Ran 15 tests ... OK
```

Additional checks run:

```text
python3 -m compileall -q tools/origin_accounting
python3 -m tools.origin_accounting.cli parser-fixtures
  18 fixtures; pass=true
python3 -m tools.origin_accounting.cli smoke --out /private/tmp/oa-smoke
  16 smoke bundles; 48 prompts; no model/provider/network calls
```

The smoke corpus now passes the family-blocking and 0.80 near-duplicate
diagnostic precheck. That result is explicitly `precheck_pass` with
`clearance_status=unresolved`; the surface smoke probe is intentionally not
treated as a readiness gate. Its full preregistered probe and independent
human semantic audit remain required.

## Remaining gates before a primary run

No primary data or model output may be generated until all of the following are
recorded in a new locked protocol/manifest version:

1. Owner-approved frozen model/checkpoint and intended tokenizer revision.
2. Exact model-tokenizer F1/F2 parity and byte-length parity for every primary
   bundle; the surrogate parity result cannot substitute for this.
3. Independent JSON Schema and RFC 8785 conformance checks.
4. Full generator round-trip/stance/transformation audit, including the
   specified independent human audit sample and agreement thresholds.
5. Blocked exact/near-duplicate, condition, structure, order, style, overlap,
   and metadata shortcut probes with their frozen ceilings and intervals.
6. Prompt-control-string and privacy/secret scans with zero failures.
7. Frozen split map, fixed `M` membership list/hash, prompts, parser,
   thresholds, simulation configuration, and release boundary.
8. A preregistration containing the all-assigned FC denominator, fixed safety
   denominator, no-peeking rule, invalid-output policy, and claim ladder.

The implementation does not authorize a pilot model run. If a future pilot
fails any feasibility gate, it is a technical/design failure and cannot be
relabelled as efficacy evidence.

## Owner-approved result commitment

The integration ledger already contains the owner-approved locked commitment
to preserve null, negative/harmful, unstable, and shortcut-driven outcomes.
The table below implements that commitment for this lane's F0/F1/F2 receipts;
it is not a new approval request and does not authorize a model run. The exact
interpretations are kept visible here so a future result cannot silently be
recast as a positive mechanism finding.

| Result class | Locked owner-approved interpretation | Required action |
| --- | --- | --- |
| **Null** | F2 does not show a robust FC improvement over F1 under the frozen model, prompts, labels, and synthetic graph. This is no evidence of an added typed-cue effect; it is not evidence that all origin-aware systems fail. | Stop escalation from this mechanism. Retain only the narrower rule/baseline or redesign under a versioned protocol; do not search for a favorable slice. |
| **Negative / harmful** | F2 increases all-assigned conservative false-corroboration or fails the paired superiority direction. If VOR also falls below its fixed non-inferiority margin, the cue is unsafe for this benchmark task because it suppresses stipulated supporting-origin recall. | Quarantine the cue, inspect invalids/noise/structure, and retire or reverse the tested cue. Never market a harmful result as “conservative behavior.” |
| **Unstable** | The direction or conclusion changes materially across the preregistered seeds, locked stress cells, or an optional unpowered robustness model. The only supported statement is model/configuration-specific instability. | Make no general claim, do not pool favorable runs, and require a new stability protocol before escalation. |
| **Shortcut / direct-code** | The effect is reproduced by metadata-only counting, field-only text replacement, condition formatting, order, style, overlap, or another non-semantic cue. The result is a formatting/direct-code behavior, not semantic evidence integration. | Fail the semantic-integration claim; repair/regenerate or narrow the paper to the observed direct-code behavior, with the diagnostic exposed. |

These dispositions preserve nulls, harms, unstable behavior, and failed controls
as first-class outcomes. They do not change the estimand or authorize any
follow-on study.

## Protocol amendment assessment

No estimand, denominator, condition, sample-size, or claim-boundary amendment
is required by this implementation. One narrow implementation clarification is
recommended for the next locked protocol/specification version:

> **Parity addendum:** require exact F1/F2 input-token equality under the
> intended frozen model tokenizer. Separately, require exact F1/F2 input
> byte-length equality as an implementation resource-control check. Permit the
> deterministic local tokenizer only for development diagnostics and require
> it to be labelled a non-authorizing surrogate.

This addendum makes the resource-control check auditable and prevents a local
token-count surrogate from being mistaken for the frozen model tokenizer. It
does not add an endpoint, alter F0/F1/F2, change the all-assigned FC denominator,
change fixed `M`, or convert stipulated origin relation into real-world
independence. The graph/root `UNKN` convention and unknown-origin conservative
risk coding are already explicit in the current specification and are carried
forward unchanged.

## Files changed by this lane

- `research/F0_F1_F2_IMPLEMENTATION_READINESS_V1.md`
- `research/origin_accounting/README.md`
- `research/origin_accounting/config/frozen_config.json`
- `research/origin_accounting/fixtures/README.md`
- `research/origin_accounting/schema/*.schema.json`
- `tools/origin_accounting/*.py`
- `tests/test_origin_accounting.py`

This memo is an implementation receipt, not a preregistration, study result,
publication authorization, or evidence that the Discrimination Layer works.

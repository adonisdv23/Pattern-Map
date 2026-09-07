# Oracle Origin-Relation Metadata in One Frozen Model

## Confirmatory study protocol v1.0

- **Study ID:** `OA-TPC-001`
- **Prepared:** 2026-08-18
- **Status:** canonical pre-run protocol; offline scaffold exists; primary run
  not authorized or opened
- **Empirical status:** no model selected, no intended tokenizer locked, no
  pilot or primary output, no preregistration, and no result
- **Supersedes for v15:** `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V0.md`
without deleting or rewriting that historical version

## 1. Answer first

For one frozen model, compare an explicit origin-counting rule with the same
byte-identical rule plus benchmark-stipulated origin-relation values. Test
whether the supplied values reduce conservative false corroboration on 300
newly authored fictional evidence bundles without materially suppressing
recall of multiple stipulated supporting origins.

The primary contrast is F2 minus F1. F0 is secondary. Invalid outputs remain in
the assigned denominators. The synthetic graph establishes only benchmark
construction relations. No condition discovers provenance or establishes
real-world independence, source authority, truth, human benefit, or deployment
value.

This document freezes the intended estimand and the gates that must precede a
run. It does not authorize a model, a provider, spending, preregistration,
public release, or the opening of the primary split.

## 2. Version receipt and preserved decisions

| Item | v1.0 decision |
| --- | --- |
| Primary question | Does F2 reduce all-assigned conservative false corroboration relative to F1? |
| Experimental unit | Evidence bundle |
| Model boundary | One frozen locally runnable open-weight instruction model, selected later by owner authorization |
| Primary set | Fixed `A`, 300 fictional bundles, 75 per origin structure |
| Primary endpoint | `FC_cons`, invalid outputs risk-coded as 1 |
| Primary analysis | Exact paired McNemar/binomial test plus paired absolute risk difference and 95% paired bootstrap interval |
| Safety set | Fixed manifest `M`, all primary bundles with stipulated supporting-origin certainty `multiple` |
| Safety endpoint | `VOR`, invalid outputs coded as 0; one-sided lower bound versus `-0.05` |
| Required parity | Exact per-bundle F1/F2 tokens under the selected tokenizer and exact per-bundle input bytes |
| Unknown relation | Explicit `UNKN`; never imputed as independent or dependent |
| Calibration | Excluded from the confirmatory family; scalar confidence remains descriptive |
| Transfer | Optional descriptive `T1`; no `F3`; never enters `A`, `M`, or confirmatory inference |
| Secondary diagnostics | Absolute count error and selected-support-origin-set precision/recall/exact match on certified non-contested rows; descriptive only |
| Negative results | Null, harmful, unstable, and shortcut-driven outcomes are preserved and reported |

The implementation audit found no reason to amend the estimand, denominators,
conditions, sample target, or claim boundary. It added one implementation
clarification: byte-length parity is recorded separately from exact parity
under the selected model tokenizer. A deterministic regex tokenizer may be
used only for development diagnostics and is never a primary lock.

## 3. Permitted claim

If and only if the primary decision and safety gate both pass, the maximum
claim is:

> On newly authored fictional evidence bundles with stipulated provenance
> graphs, the supplied typed-metadata condition produced less conservative
> false corroboration than the byte-identical rule-only condition on the
> tested frozen model, while fixed-set recall of multiple stipulated
> supporting origins remained above the prespecified safety margin.

The title, abstract, results, discussion, and conclusion must retain “supplied”
or “oracle,” “fictional/synthetic,” “one frozen model,” and “stipulated.” The
study may not claim:

- provenance or copying discovery;
- real-world causal, editorial, methodological, or epistemic independence;
- factual truth, source authority, or consensus;
- improved retrieval, human decisions, reliance, safety, or utility;
- validation of the full Discrimination Layer;
- transfer to another model, domain, public corpus, or deployment.

## 4. Symbols and analysis objects

For bundle `i` and condition `c`:

- `valid(i,c)` — strict parser accepts exactly one four-field JSON object;
- `hat_n(i,c)` — emitted `origin_count_supporting` when valid;
- `certainty_i` — restricted manifest value `none`, `single`, `multiple`, or
  `unknown` for supporting origins;
- `E(i,c)` — selected report IDs in the valid output;
- `O_support(E)` — distinct stipulated support-side origin IDs represented by
  the selected evidence IDs, computed only by the evaluator after output
  storage;
- `A` — fixed list of all 300 assigned primary bundle IDs;
- `M = {i in A : certainty_i = multiple}` — fixed safety subset;
- `FC_obs`, `FC_cons`, `FC_lib` — observed, conservative, and liberal
  false-corroboration codes;
- `VOR` — valid supporting-origin recall gate indicator.

Origin IDs, origin structure, support/refute origin sets, gold claim state,
split labels, and condition name are restricted evaluator fields. The model
never receives them.

## 5. Corpus inventory

### 5.1 Split sizes

| Split | Total | One-origin repetition | Multiple-origin convergence | Unknown origin | Conflict |
| --- | ---: | ---: | ---: | ---: | ---: |
| `dev` | 80 | 20 | 20 | 20 | 20 |
| `pilot` | 40 | 10 | 10 | 10 | 10 |
| `primary` | 300 | 75 | 75 | 75 | 75 |
| `stress` | 60 | 15 | 15 | 15 | 15 |

Development repairs generator, schema, parser, prompts, and leakage. Pilot
tests feasibility, replay, runtime, invalid rates, audit workflow, and
simulation assumptions only. Primary supplies the fixed confirmatory set.
Stress is descriptive and cannot enlarge or rescue the primary analysis.

### 5.2 Bundle contract

Each bundle contains:

- one atomic fictional proposition with explicit scope and time;
- four to six fictional reports;
- at least two content domains across the corpus;
- crossed report style and presentation order;
- a public manifest with opaque report/source/artifact IDs and dates;
- a restricted provenance graph and stance/origin manifest;
- an immutable split and generator receipt.

No real person, allegation, private record, production event, medical or
employment decision, credential, cookie, contact information, or externally
licensed article text may enter the synthetic corpus. Dates remain fictional
and future-dated. The generator must not call an LLM or external retrieval
service.

### 5.3 Four origin structures

1. **One-origin repetition.** One supporting root; remaining supporting
   reports are exact copy, paraphrase, or summary transformations. Derived
   reports receive `DPND`; the root receives `UNKN` because no parent relation
   is supplied. Gold supporting-origin certainty is `single`.
2. **Multiple-origin convergence.** Three separately authored supporting roots
   are `INDP` only by construction, plus a neutral report. Gold supporting-
   origin certainty is `multiple` and the count is three.
3. **Unknown origin.** Reports agree, but origin certification is deliberately
   withheld. Every prompt-visible relation value is `UNKN`, even if the latent
   generator graph contains transformations. Gold count is null and certainty
   is `unknown`.
4. **Conflict.** One support root and one refute root, with dependent copies on
   each side. Support and refute origin sets remain separate. A refuting
   `INDP` cue never counts toward supporting-origin recall.

### 5.4 Truth boundary

The generator may establish nodes and edges by construction: source, artifact,
transformation, origin family, report stance, and synthetic time. It cannot
establish real-world honesty, truth, causal independence, authority,
authorization, consequence, or prevalence.

Keep four vocabularies separate:

| Vocabulary | Values / examples | Must not absorb |
| --- | --- | --- |
| Derivation | original, copy, paraphrase, summary, quote, update | Claim stance or truth |
| Origin relation | `DPND`, `INDP`, `UNKN`, `NONE` | Authority, support, or real-world independence |
| Claim stance | supports, refutes, qualifies, insufficient/neutral | Origin relation |
| Action | provisional, hold, escalate, authorized | Claim or origin state |

## 6. Split and contamination lock

Assign splits before any model output. A keyed deterministic seed produces
opaque IDs and assignments. Split on proposition family and origin family so
that no paraphrase, copy, source family, origin family, or claim template
crosses `dev`, `pilot`, `primary`, or `stress`.

Before primary lock, emit and review:

- exact normalized-text duplicate report across splits;
- character- and token-level near-duplicate candidates;
- proposition/origin-family membership across splits;
- template, lexical-marker, punctuation, length, style, domain, and position
  distributions;
- generated graph invariants and dangling-edge report;
- a human semantic/stance/transformation audit on the prespecified sample;
- disagreement, adjudication, and quarantine reason codes.

The current deterministic nearest-centroid surface smoke is insufficient and
must not be called leakage clearance. Freeze a blocked character/token TF-IDF
classifier, held-out family structure, ceiling, and Wilson interval before
opening `primary`. A trivially separable structure label is a corpus failure,
not an interesting model result.

## 7. Conditions and prompt lock

### 7.1 Shared material

All F0/F1/F2 prompts receive the same:

- system output contract and relation-code legend;
- target claim;
- report text bytes and report order;
- opaque report/source/artifact IDs and fictional dates;
- fixed-width metadata rows and delimiters;
- output-token cap, retrieval calls `0`, and tool calls `0`.

The shared legend defines:

```text
DPND = dependent on another observed report or origin path
INDP = separate origin in this benchmark, stipulated rather than discovered
UNKN = relation unresolved; do not count it as independent
NONE = no relation value supplied in this slot
```

### 7.2 Condition instruction

F0 receives an ordinary bounded evidence-assessment instruction, including a
warning not to infer provenance from wording, IDs, dates, or order. All
relation slots are `NONE`.

F1 and F2 receive the exact same instruction bytes:

```text
Count distinct origin pathways when the supplied information permits it. Do
not treat repeated or derived reports as independent support. Preserve an
unknown origin relation as unknown, and do not infer a relation that is not
supplied. Select the report IDs used for your assessment.
```

F1 relation slots are all `NONE`. F2 relation slots use only `DPND`, `INDP`,
and `UNKN` from the frozen graph manifest. No prompt renders the condition
name, split, bundle ID, origin ID, origin structure, gold stance, or gold count.

### 7.3 Parity

After owner selection of the model/checkpoint/tokenizer but before opening the
primary split:

1. apply the exact backend chat template;
2. freeze system/user prompt bytes and output cap;
3. render every F1/F2 pair;
4. require identical report-text hash maps and order;
5. require exact input-byte-length equality;
6. require exact intended-tokenizer input-token equality;
7. record system/user/final-input hashes and counts;
8. fail closed on any mismatch.

The local regex tokenizer and `PAD` strings are development devices only. A
token-parity receipt from that surrogate cannot satisfy step 6.

## 8. Model and run lock

The owner must separately authorize:

- one locally runnable open-weight instruction model;
- exact checkpoint and tokenizer revisions;
- license and permitted use;
- hardware/runtime environment;
- compute, time, and storage budget.

Primary decoding is deterministic if the backend permits. If it does not,
exactly three seeds and a within-bundle aggregation rule must be declared before
any primary output. Seeds are repeated measurements inside a bundle, not
additional experimental units.

No live web, retrieval, tool call, paid model, provider API, prompt tuning,
manual repair, or ad hoc retry is permitted after lock. Record model,
checkpoint, tokenizer, chat template, runtime, dependency hashes, hardware,
decoding, seeds, prompt hashes, input/output counts, timing, memory, error, and
raw bytes for every assigned run.

## 9. Output contract and parser

Required output:

```json
{
  "origin_count_supporting": 0,
  "claim_state": "supported | refuted | insufficient | contested",
  "confidence": 0.0,
  "evidence_ids": ["opaque_report_id"]
}
```

Parser requirements:

- immutable UTF-8 bytes, one JSON object, no Markdown/prose;
- exact four keys, duplicate-key rejection, no unknown keys;
- integer count in `[0,6]`, boolean rejected as integer;
- finite numeric confidence in `[0,1]`, boolean rejected;
- claim state in the closed four-value vocabulary;
- unique evidence-ID array within the fixed maximum;
- each evidence ID matches syntax and belongs to the assigned bundle;
- raw bytes, byte length, hash, parse status, and reason code retained.

No coercion, repair, truncation, extraction of an inner object, manual retry,
or count reconstruction is allowed. Timeout, cancellation, backend error,
empty output, invalid UTF-8, invalid JSON, duplicate key, schema error, semantic
error, and unknown ID receive distinct reason codes and remain visible.

## 10. Endpoints

### 10.1 Primary false corroboration

```text
FC_obs(i,c) = 1[valid(i,c)
                  AND hat_n(i,c) >= 2
                  AND certainty_i in {none,single,unknown}]

FC_cons(i,c) = 1[NOT valid(i,c) OR FC_obs(i,c)=1]
FC_lib(i,c)  = 1[valid(i,c) AND FC_obs(i,c)=1]
```

The primary outcome is `FC_cons`. `FC_lib` and a jointly valid complete-case
rate are prespecified sensitivities only. Neither can replace `A` or become the
headline after results.

Unknown-origin bundles are conservatively risk-coded when a valid output
asserts at least two supporting paths. This is deliberate: the relation is not
certified, so the study asks whether the model overstates corroboration. It is
not evidence that the latent world has zero or one origin.

### 10.2 Fixed-set supporting-origin recall

For each `i in M`:

```text
VOR(i,c) = 1[valid(i,c)
               AND hat_n(i,c) >= 2
               AND |O_support(E(i,c))| >= 2]
```

Otherwise `VOR=0`. `M` is frozen from the restricted manifest before any run,
and its ordered membership list/hash is published in the run receipt. Never
intersect `M` with valid outputs. Refuting, neutral, dependent-copy, or unknown
origins cannot inflate `O_support`.

### 10.3 Secondary/descriptive measures

- absolute origin-count error, defined only when the output is valid and the
  restricted manifest certifies `gold_support_origin_count`;
- claim-state accuracy;
- supporting-origin-set precision, recall, and exact match, using only
  selected evidence whose report stance is `supports` and only certified
  non-contested `none`, `single`, or `multiple` gold support-origin sets;
- invalid-output rate and reason-code distribution;
- confidence attached to the selected claim state, explicitly uncalibrated;
- tokens, bytes, latency, memory, local compute, and errors;
- descriptive structure/domain/style/order and relation-noise slices;
- metadata-only and field-only diagnostic behavior.

The output contract defines `evidence_ids` as reports used for the assessment,
not reports credited as supporting the claim. The scorer therefore does not
interpret a neutral or refuting selected report as an evidence-selection error
and does not expose general evidence-ID precision/recall in this protocol.
Selected-support-origin metrics inspect only selected IDs whose benchmark
stance is `supports`; neutral and refuting selections remain preserved but are
outside these support-origin diagnostics. Contested rows remain a separate
visible scope but are not scored for a support-only set. Invalid outputs and
unresolved support-origin rows remain undefined rather than being imputed. The
scorer exposes the remaining fields as a descriptive sidecar; they cannot change
`FC_cons`, `VOR`, the F0/F1/F2 contrast, a denominator, or either confirmatory
decision.

For the selected-support-origin set metrics, precision is `None` when no
selected supporting origins exist, and recall is `None` when the certified gold
support-origin set is empty. Exact-set match remains defined, so two empty sets
match exactly (`1`). These undefined values are reported as undefined rather
than coerced to zero.

The current generator invariant defines every `stance=supports` report as part
of the bundle's restricted support set. A wrong-stipulated-origin diagnostic is
therefore not construct-valid in this corpus and is intentionally not emitted;
the selected support-origin set measures omission and exact-set coverage only.

No fictional decision-utility score is permitted without a defined consequence
function. No Brier score is permitted for a scalar that lacks a specified
binary probability target.

## 11. Confirmatory analysis

### 11.1 Primary decision

For all `i in A`, form paired binary vectors for F1 and F2. Report:

- `N=300`, with no denominator subtraction;
- F1/F2 `FC_cons` counts and rates;
- paired absolute risk difference F2 minus F1;
- exact two-sided McNemar/binomial p-value;
- 95% paired percentile bootstrap interval from 10,000 bundle resamples using
  a frozen seed;
- invalid counts/rates and reason codes;
- liberal and jointly valid sensitivities with their denominators.

Superiority requires beneficial delta, `p<.05`, and an interval upper bound
below zero. Report whether the `-0.08` planning benchmark was reached; do not
make it an undisclosed additional test.

### 11.2 Safety decision

On fixed `M`, report F1/F2 VOR counts/rates, delta, `|M|`, membership hash, and
the prespecified paired one-sided 95% lower bound. The current bootstrap helper
uses the fifth percentile as a development scaffold, but the final interval
method must be declared and coverage-simulated at actual `|M|` before
preregistration. Pass only if the lower bound is greater than `-0.05`.

### 11.3 Multiplicity

The confirmatory family has exactly the primary superiority decision and the
safety gate. F0, claim state, confidence, evidence selection, stress, domain,
structure, style, seed, and any optional-model slice are descriptive or
exploratory. No secondary p-value family exists in v1.0.

## 12. Planning simulation

Use paired Bernoulli probabilities that satisfy:

```text
p10 = P(F1=1, F2=0)
p01 = P(F1=0, F2=1)
p10 + p01 = discordance
p01 - p10 = Delta_F2_minus_F1
p11 = baseline_F1 - p10
p00 = 1 - p10 - p01 - p11
```

FC grid:

- F1 baseline risk: `0.20`, `0.30`, `0.40`;
- discordance: `0.10`, `0.20`, `0.30`;
- delta: `0`, `-0.05`, `-0.08`, `-0.10`;
- `N`: `240`, `280`, `300`, `320`, `360`;
- invalid rates: `0`, `0.02`, `0.05`, `0.10`;
- at least 10,000 replications per valid cell.

Report power, type-I error at delta zero, interval coverage, and effect of
conservative/liberal invalid coding. The separate VOR grid fixes expected
`|M|=75`, crosses plausible baseline VOR, paired discordance, deltas `0`,
`-0.02`, `-0.05`, `-0.08`, and invalid rates coded as zero. Report coverage
and probability of passing the one-sided gate.

If `N=300` cannot estimate the candidate practically important difference with
adequate operating characteristics, downgrade to estimation/feasibility or
create a new protocol before data access. Do not use the pilot effect to choose
a favorable sample size. If VOR is too imprecise at fixed `M`, downgrade it
before preregistration rather than enlarging `M` after inspection.

## 13. Leakage and shortcut suite

| Threat | Required pre-lock control | Failure interpretation |
| --- | --- | --- |
| Semantic IDs reveal structure | Opaque keyed IDs; no sequential/semantic origin labels | Corpus/prompt failure |
| Condition formatting reveals F2 | Same metadata rows, delimiters, order, code lengths, byte and token counts | Parity/formatting failure |
| Copying similarity solves structure | Cross low-overlap dependent and high-overlap distinct-as-stipulated reports | Lexical shortcut |
| Style/position/template leaks structure | Crossed/frozen style, length, position, order, punctuation, domain | Surface shortcut |
| Family leakage across splits | Proposition/origin-family blocking plus exact/near duplicate audit | Split quarantine |
| Relation code alone solves count | Metadata-only direct counter and field-only no-report-text control | Direct-code behavior, not semantic integration |
| Human-readable codes dominate | Neutral-code and codebook-permutation stress | Label shortcut |
| Perfect relation cue overstates readiness | 0.05/0.10/0.20 relation-noise stress with untouched gold | Oracle upper bound only |
| Unknown becomes independent | All-`UNKN` unknown fixtures and invariant tests | Construct failure |
| Refuting origin inflates recall | Separate support/refute origin sets and scoring test | Scoring failure |

Before a model run, freeze every threshold, classifier split, interval, failure
rule, and repair policy. A failed primary-lock control invalidates the corpus or
prompt version. It cannot be excused after observing a favorable model effect.

## 14. Feasibility and stop gates

### 14.1 Offline implementation gate

Current status: scaffold passes focused determinism, graph, unknown, parity,
parser, denominator, metadata-count, power-probability, compile, parser-fixture,
and 16-bundle smoke checks. This gate proves code behavior only.

### 14.2 Pre-pilot gate

Require:

- independent code and schema review;
- full protocol-sized regeneration and deterministic receipt;
- zero graph/schema/split invariant failures;
- completed semantic/stance/transformation audit;
- passed blocked surface/condition classifier gates;
- exact selected-tokenizer and byte parity;
- zero secret/private-text/prompt-control-string findings;
- fixed parser and raw-output write path;
- validated power and VOR interval coverage plan;
- owner authorization for exact model, budget, and pilot.

### 14.3 Pilot gate

The 40-bundle pilot may test only:

- end-to-end replay and deterministic/seed-bounded behavior;
- at least 98% parseability;
- timing, memory, storage, and output caps;
- zero schema/provenance invariant failures;
- no unresolved cross-split exact/near duplicates;
- semantic-audit process and shortcut probes;
- no more than 10% data-quality invalidation.

Pilot efficacy estimates cannot tune the endpoint, claim, N, margin, or a
favorable prompt. Failures produce a versioned repair on development/pilot
material and a new lock receipt.

### 14.4 Primary stop/quarantine

Stop affected runs for secrets/private material, unauthorized external access,
real-person harmful labels, manifest corruption, prompt/evidence mismatch,
parity failure, condition leakage, raw-output loss, or an unrecoverable backend
deviation. Preserve the receipt. Quarantined data are not efficacy evidence.
No efficacy peeking or outcome-based early stopping is permitted.

## 15. Natural-syndication T1 boundary

T1 is a separate descriptive transfer tier, not a model condition. It can be
constructed only after primary prompt and analysis locks, with a separate
dataset/version/license/annotation manifest and owner authorization.

Permitted relation mapping:

- documented NEWS-COPY same-original pair may yield adapter `DPND` while
  retaining the native duplicate label;
- NEWS-COPY nonduplicate stays `UNKN` absent a source-path audit;
- Newswire recurrence/cluster metadata remain aggregate context, never origin
  count;
- public distinct rows, URLs, publishers, dates, bylines, wording, topics, or
  wire cities never produce synthetic `INDP`.

T1 cannot supply `A`, `M`, primary confidence intervals, McNemar rows, VOR,
confirmatory effects, real-world independence, claim truth, or complete
provenance. Unresolved NEWS-COPY rights and Newswire version/field licensing
block corpus use until resolved. A metadata-only adapter receipt is the safest
possible next transfer artifact if later authorized.

## 16. Negative-result and retirement contract

| Result | Mandatory disposition |
| --- | --- |
| Null F2−F1 | Report no evidence of added typed-cue value in this setting; do not search for a favorable slice |
| F1/F2 both beat F0 but tie | Credit the explicit rule only |
| F2 harmful or primary direction worse | Quarantine/retire the cue; never rebrand harm as useful conservatism |
| FC improves but VOR fails | Reject the current cue as blanket discounting |
| Direct-code/field-only match | Fail semantic-integration interpretation; report formatting behavior |
| Surface/order/style/parity control failure | Repair before primary or narrow to shortcut behavior |
| Noise destroys effect | Oracle-cue upper bound only |
| Seed/model instability | Model/configuration-specific instability; no favorable pooling |
| T1 does not transport | No real-world transfer claim |

The raw outputs, invalids, diagnostic failures, and unfavorable result remain
in the reproducibility record. The paper may still be useful as a negative or
methodological result, but it may not be rewritten as though positive-only
publication were the original plan.

## 17. Reproducibility and release package

If a run and later release are separately authorized, preserve:

- protocol/preregistration versions and amendments;
- generator source, seeds, graph manifests, split map, schema, and dataset card;
- F0/F1/F2 system/user prompts, chat template, padding, hashes, and counts;
- model/checkpoint/tokenizer/license/environment/hardware receipts;
- raw outputs for every assigned run, parser version, parsed rows, invalid
  reason codes, and no-retry proof;
- primary/safety analysis code, simulation code, seeds, interval coverage, and
  all descriptive diagnostics;
- semantic-audit and adjudication records;
- privacy, secret, rights, and source-status receipts;
- a canonical release manifest with file hashes and explicit visibility;
- null, harmful, unstable, shortcut, and stopped-run records.

The current local deterministic JSON serializer is not asserted to implement
RFC 8785. A public release must use an independently tested canonicalization
implementation and conformance fixtures. No generated or public data, model
output, or license-dependent field may be released merely because the local
scaffold exists.

## 18. Current implementation receipt

The committed offline scaffold provides:

- ten closed Draft 2020-12 JSON Schemas;
- deterministic HMAC/Base32 opaque IDs;
- a four-structure fictional generator;
- prompt construction and local surrogate parity receipts;
- strict parser and immutable raw-output receipt helper;
- fixed-denominator scorer and paired analysis, including a separate
  descriptive origin-count/selected-support-origin sidecar;
- split, near-duplicate, balance, surface, metadata-only, field-only, noise,
  and planning-simulation diagnostics;
- fifteen focused offline tests, 18 parser fixtures, and a 16-bundle smoke
  run.

It does **not** provide the intended tokenizer, a cleared surface classifier,
independent semantic audit, fixed primary manifest, model output, effect,
preregistration, publication, or release authorization.

## 19. Owner authorization checklist

No empirical phase begins until the owner separately records:

- [ ] accept or reject this bounded scientific contribution;
- [ ] exact model/checkpoint/tokenizer and license;
- [ ] local compute/time/storage budget;
- [ ] VOR interval and coverage disposition;
- [ ] completed pre-pilot code/corpus/leakage/semantic audit;
- [ ] pilot authorization and permitted output handling;
- [ ] preregistration authorization after pilot feasibility;
- [ ] primary-run authorization after the final lock;
- [ ] any T1 data access, annotation, or licensing authorization;
- [ ] any publication or public-release authorization.

Unchecked items are stops, not invitations to infer a favorable choice.

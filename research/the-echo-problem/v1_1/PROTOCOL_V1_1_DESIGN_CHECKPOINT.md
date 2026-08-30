# Origin Accounting Protocol v1.1 — design checkpoint

**Status:** NON-AUTHORIZING DESIGN-ONLY CHECKPOINT

**Project:** The Echo Problem / ECHO-01

**Version:** EP v1.1

**Date:** 2026-08-23

This document reconciles the preserved v15.2 `ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md`
with the owner-approved Claude-package audit. It is a successor design record,
not a rewrite of the preserved protocol and not a report of a run.

## 1. Locked question and scope

The controlled candidate asks whether visible, benchmark-stipulated relation
values change conservative asserted-count risk relative to the same explicit
counting rule without those values, under matched prompts and resources:

```text
F0: ordinary bounded evidence assessment (secondary baseline)
F1: explicit origin-counting rule; relation slots are NONE
F2: the byte-identical F1 rule plus stipulated DPND / INDP / UNKN values
primary contrast: F2 minus F1
```

The unit remains the frozen bundle. The planned primary set is `A = 300`; the
fixed safety set is `M = 75` multiple-origin bundles. These are design values,
not a denominator from observed data. F0/F1/F2 remain unrun and no model or
tokenizer has been selected.

The six-family Pattern Map v16 thesis is broader than this research track. EP
may constrain claims about recurrence and dependence but cannot redefine v16.

## 2. Relation labels: controlled experiment versus real-world measurement

### 2.1 Controlled F0/F1/F2 labels stay simple

The stipulated graph uses:

| Label | Meaning inside the synthetic benchmark | What it does not mean |
| --- | --- | --- |
| `DPND` | dependent on another observed report or origin path | not a universal dependence estimator |
| `INDP` | separate origin in this benchmark | not proof of epistemic independence or truth |
| `UNKN` | relation unresolved | never permission to count as independent |
| `NONE` | no relation cue rendered in F1/F0 | not a claim that the underlying relation is absent |

These labels are a controlled manipulation. They are intentionally simple so
that F1 and F2 differ in the supplied cue, not in an undisclosed ontology.
They must not be presented as discovered provenance.

### 2.2 Real-world measurement uses typed, graded, uncertain relations

An operational measurement record should allow a set of typed edges rather
than a single binary independence bit. Minimum proposed fields are:

```json
{
  "relation_type": "exact_reproduction|syndication|paraphrase|common_release|shared_extraction|overlap|contradiction|unknown",
  "dependence_grade": "none|weak|moderate|strong|unknown",
  "confidence": 0.0,
  "basis": ["textual", "attribution", "version", "source-path", "manual"],
  "scope": "claim|passage|document|origin-path",
  "status": "observed|inferred|stipulated|held"
}
```

`INDP` in the controlled benchmark maps only to “separate origin in this
benchmark”; it must not be exported as `dependence_grade: none` without a
separate validation basis. Distinct origin is not automatically independent,
and common origin is not automatically false. Unknown remains unknown.

## 3. Endpoints and truth boundary

The v1.0 formulas remain the endpoint authority:

```text
FC_obs(i,c)  = 1[valid(i,c) AND emitted_count >= 2
                  AND certainty_i in {none, single, unknown}]
FC_cons(i,c) = 1[NOT valid(i,c) OR FC_obs(i,c) = 1]

VOR(i,c) = 1[valid(i,c) AND emitted_count >= 2
             AND at least two selected supporting reports map to distinct
                 stipulated support-side origins]
```

VOR is evaluated only on the frozen set `M`, whose membership is fixed before
any future run. Refuting, neutral, dependent-copy, and unknown relations do
not inflate support-side VOR. The selected-support-origin set is a descriptive
diagnostic; it is not a claim of exact provenance discovery.

`FC_cons` is a conservative asserted-count-risk composite. It combines
invalid output with valid asserted-count risk and must be decomposed into
invalid-only and valid-only panels before anyone narrates a semantic cue
effect. `VOR` is selected stipulated support-origin coverage at a threshold,
not exact origin accounting, factual truth, or independence.

The parser must preserve raw bytes, parse status, reason code, output hash,
and no-repair/no-retry status. Unknown or unresolved relations cannot be
imputed from repetition, proximity, or technical access.

## 4. Prompt, hash, and parity locks

F1 and F2 must share:

- identical report bytes, report order, opaque IDs, dates, output contract,
  output cap, and tool/retrieval budget;
- identical instruction bytes except for the visible frozen relation values;
- identical system/user/final-input accounting apart from the permitted cue;
- separate hashes for full serialized bundle content and ordered membership;
- exact selected-tokenizer input-token equality for every pair; and
- a fail-closed mismatch receipt.

Byte-length equality is recorded separately from tokenizer equality. A local
regex tokenizer or development `PAD` string cannot satisfy the selected-model
parity gate. F0 remains secondary; F0 parity may be diagnosed, but an F0
failure cannot weaken, enlarge, or replace the F1/F2 confirmatory contrast.

The active harness implements only offline prompt construction and parity
search. It has no model, provider, network, or cloud runtime integration.

## 5. Corpus transfer firewall

### NEWS-COPY

NEWS-COPY may be considered only if a future owner-authorized data and rights
record verifies the exact version, labels, license, and available text. Its
same-original reproduction labels can validate pair and cluster recovery for
the origin-measurement instrument. They cannot provide:

- claim truth or factual correctness;
- claim-support labels;
- independent corroboration labels;
- `FC_cons` outcomes;
- VOR outcomes; or
- a conclusion that different clusters are independent.

A documented same-original pair may be represented as a typed dependent edge
(`DPND` for an adapter diagnostic). A nonduplicate pair remains `UNKNOWN` for
origin dependence unless a separate source-path audit establishes more.

### Newswire

Newswire may provide aggregate recurrence or cluster-size context. It cannot
enter `A`, `M`, the primary denominator, McNemar rows, VOR, or confirmatory
confidence intervals unless a future review verifies member/version truth,
rights, and the exact annotations needed for those endpoints.

This transfer route is not evidence that the corpus was measured in this
checkpoint. No external corpus was acquired or executed here.

## 6. Prior measurement and novelty boundary

The project must not say “nobody has measured retrieval dependence” or claim
exhaustive novelty. Existing neighboring measurements are recorded in
[PRIOR_MEASUREMENT_MATRIX.md](PRIOR_MEASUREMENT_MATRIX.md). The narrower
possible gap is explicitly provisional:

> validated, typed, provenance-aware same-origin structure in contemporary
> top-k RAG evidence, connected to claim-support status without treating
> cluster difference as independence.

That gap is unproven until a scoped review and a validated instrument establish
what has and has not been measured.

## 7. Planning-only MDE and power surface

The planning surface varies:

- F1 baseline FC risk: `0.20`, `0.30`, `0.40`;
- paired discordance: `0.10`, `0.20`, `0.30`;
- F2-minus-F1 effects: `0`, `-0.05`, `-0.08`, `-0.10`;
- primary sizes: `240`, `280`, `300`, `320`, `360`, with `400` as a
  descriptive candidate when high discordance is the design requirement;
- F1/F2 invalidity stress: `0`, `0.02`, `0.05`, `0.10`, including unequal
  rates; and
- fixed safety size `|M| = 75` for the VOR grid.

The active script uses the exact paired McNemar/binomial p-value in the
canonical decision wherever a simulated cell is evaluated. It reports the
paired risk difference and, when requested, a deterministic paired percentile
interval. It labels every output `planning_only_no_model_or_corpus_outputs`.

Under one declared planning cell—F1 risk `0.38`, paired discordance `0.30`,
zero differential invalidity, and the exact two-sided McNemar decision without
the still-unfrozen interval gate—10,000 deterministic planning repetitions gave:

| Planned effect, F2 minus F1 | `n=300` decision probability |
| --- | --- |
| `-0.08` | approximately `0.69` |
| `-0.09` | approximately `0.79` |
| `-0.095` | approximately `0.84` |
| `-0.10` | approximately `0.88` |

On that cell, the planning MDE for roughly 80% decision probability lies
between `-0.09` and `-0.095`; `-0.08` is below that resolution. Holding the
same assumptions and effect `-0.08`, `n=400` gave approximately `0.82`.
These values are conditional planning calculations, not guarantees. The final
interval method, invalidity rule, discordance assumption, selected-model
receipt, and target power remain open. A future frozen protocol should either
raise the primary assignment to about `n=400` for this cell or explicitly
declare that `n=300` targets effects around `0.095` rather than `0.08`.

## 8. Required offline gates before any future live phase

The following remain open gates, not completed findings:

1. selected model/checkpoint/tokenizer/chat-template and license receipt;
2. exact F1/F2 parity receipt for every assigned pair;
3. frozen content and ordered-membership manifests for `A` and `M`;
4. strict parser and raw-output write-once/no-repair path;
5. invalid-only versus valid-only `FC_cons` decomposition;
6. pairwise/cluster validation of the 0.40 containment threshold on labelled
   real text, including false-merge and false-split rates;
7. leakage, shortcut, semantic, stance, transformation, and privacy scans;
8. final VOR interval and coverage plan at fixed `M=75`; and
9. explicit owner authorization for any model, dataset, participant, provider,
   preregistration, or external action.

No gate is passed by a synthetic fixture, local test, planning simulation,
model review, or preserved package status.

## 9. Negative and stopped result contract

The EP v0.1 taxonomy remains unchanged and applies to the future track:
`null`, `rule_only`, `invalidity_driven`, `threshold_only_vor`, `harmful`,
`shortcut_driven`, `surface_or_semantic_audit_failure`, `unstable`,
`noise_fragile`, `nontransfer`, and `stopped_or_quarantined`. None is an
observed EP v1.1 result. All favorable and unfavorable possibilities must be
retained; a threshold, recurrence count, or passing parser cannot be promoted
to corroboration or truth.

## 10. Source authority

The preserved v15.2 v1.0 protocol and draft amendment remain historical
source material. This active checkpoint is subordinate to the owner handoff,
the locked v16 intent, and the repository authority order. The Claude package
and its red-team report are advisory inputs whose valid findings are recorded
in the accompanying QA report; they do not become evidence merely by being
incorporated here.

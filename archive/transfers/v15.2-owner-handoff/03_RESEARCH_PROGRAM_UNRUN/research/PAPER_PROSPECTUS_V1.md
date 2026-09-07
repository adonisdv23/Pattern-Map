# Oracle Origin-Relation Metadata in One Frozen Model

## Research-paper prospectus v1

- **Program:** Pattern Recognition / The Discrimination Layer v15
- **Prepared:** 2026-08-18
- **Status:** canonical prospectus; study unrun; no preregistration, model lock,
  participant work, publication, or empirical result exists
- **Companion protocol:** `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md`
- **Implementation receipt:** `research/F0_F1_F2_IMPLEMENTATION_READINESS_V1.md`

## Answer first

The credible scientific paper inside the larger framework is deliberately
small. It asks whether one frozen model uses a supplied origin-relation field
to avoid counting repeated reports as separately rooted support, beyond what
the same model does when given the same evidence and an explicit counting rule
without that field.

The primary contrast is F2 minus F1 on fictional evidence bundles with
stipulated provenance graphs. The primary outcome is conservative,
all-assigned false corroboration. A fixed-set measure of whether the model
retains multiple stipulated supporting origins is the safety gate. F0 is a
secondary ordinary evidence-bundle baseline. A separately named natural-news
transfer artifact, T1, may be built later for descriptive boundary testing if
rights and annotation gates pass; it is not F3 and cannot enter either
confirmatory denominator.

This paper is allowed to return zero. A null, negative, harmful, unstable, or
shortcut-driven result must be preserved and reported. A favorable result
would support only a model-, task-, prompt-, label-, and synthetic-graph-
specific condition effect. It would not establish provenance discovery,
real-world independence, truth, better human decisions, deployment value, or
the validity of the full eleven-responsibility framework.

## Scientific title and thought-piece separation

Working scientific title:

> **Oracle Origin-Relation Metadata in One Frozen Model: A Controlled
> False-Corroboration Benchmark**

The thought piece retains its historical title:

> **Pattern Recognition: The Discrimination Layer**

The two titles should not be collapsed. The thought piece is a systems
synthesis and design argument. The proposed paper is one controlled behavioral
test of one supplied field. “Discrimination” also carries social/legal and
classifier meanings, so it should not become the scientific label by default.

## The residual contribution after prior-art review

The targeted primary-source review in `research/PRIOR_ART_DELTA_V1.md` rules
out a broad mechanism-novelty claim:

- copying-aware truth discovery and dynamic source dependence are established;
- double counting and report-versus-study unit errors are established in
  evidence synthesis;
- citation-network amplification without new data has been documented;
- exact, noisy, and semantic duplication, diversity-aware retrieval, and
  set-wise selection have direct precedents;
- current RAG work already studies redundancy, paraphrase, source-set
  variation, conflict, uncertainty, and evidence interaction;
- natural-language claim provenance already has a direct published graph and
  inference precedent in [Zhang, Ives & Roth (ACL 2020)](https://aclanthology.org/2020.acl-main.406/);
- NEWS-COPY and Newswire already operationalize bounded forms of textual
  reproduction and recurrence.

Zhang, Ives & Roth define and infer provenance graphs for natural-language
claims. Their inferred provenance graph is not the current study’s supplied
benchmark relation field: the v15 protocol tests cue use under stipulated
relations and does not infer a source path.

The closest recent working manuscript located in the documented search is
[Ross et al. (2026)](https://arxiv.org/abs/2608.13956), which separately
constructs duplicate, paraphrased, and diverse evidence sets and reports model
behavior on a fictional benchmark. It is an arXiv v1 manuscript submitted
2026-08-14; no venue or acceptance is shown in the checked record. It does not
supply the current origin-relation field or conservative false-corroboration
count. [Naphade (2026)](https://arxiv.org/abs/2601.06189) is an arXiv v1
manuscript submitted 2026-01-08 whose record notes an ACL ARR submission but
shows no acceptance. It reports different behavior under distinct versus
paraphrased opposing evidence, but its “distinct documents” are not verified
distinct origins. Its Table 4 values must remain correctly attributed:
67.6%/76.5% belongs to DeepSeek-R1-8B; Llama-3.1-70B-Instruct is 62.9%/69.8%.

The other close records retain explicit status boundaries. [Li, Padman &
Krishnan](https://arxiv.org/abs/2605.29084) is arXiv v1 submitted 2026-05-27
with no venue acceptance shown; its labels describe cross-source answer
variation, not derivation. [EvidentialRAG](https://arxiv.org/abs/2607.10491) is
arXiv v1 submitted 2026-07-11 with no venue or acceptance shown; it is a
conflict/uncertainty-fusion comparator, not an origin relation system. [RARE](https://arxiv.org/abs/2604.19047)
is arXiv v2 and says accepted to ACL 2026 Main Conference, but an ACL venue page
was not located; [NEST](https://aclanthology.org/2026.acl-industry.35/) is
published in the ACL 2026 Industry Track; [Schelpe](https://arxiv.org/abs/2605.09611)
is an arXiv v1 preprint; and [MMR](https://doi.org/10.1145/290941.291025) is a
published SIGIR 1998 paper. These are adjacent or future comparators, not
required added arms in the locked F0/F1/F2 study.

The residual empirical contribution is therefore:

> A controlled test of whether a visible, benchmark-stipulated origin-relation
> cue changes a frozen model’s asserted count of supporting origin pathways
> relative to a byte-identical explicit rule without populated relation cues,
> under a fixed conservative endpoint and recall guardrail.

This is a representation-and-cue-use question. It is not a claim that the
project created source-aware RAG, detects copying, infers lineage, measures
truth, or supplies a generally useful product architecture.

## Research question, estimand, and decision rule

Research question:

> On newly authored fictional evidence bundles with stipulated source,
> artifact, transformation, origin, time, and claim-stance structure, does F2
> reduce conservative false corroboration relative to F1 for one frozen model?

Primary estimand:

```text
Delta_FC_cons = mean_A[FC_cons(i,F2)] - mean_A[FC_cons(i,F1)]
```

`A` is the fixed set of all 300 assigned primary bundles. Lower is better.
Invalid outputs remain in `A` and receive `FC_cons=1`; no parseability filter
may replace the assigned denominator.

A bounded superiority decision requires all of the following:

1. a beneficial F2-minus-F1 point estimate;
2. a two-sided exact paired McNemar/binomial `p < .05`;
3. a 95% paired bootstrap interval whose upper bound is below zero; and
4. passage of the fixed-set supporting-origin recall safety gate.

The candidate `-0.08` risk difference is a practical planning benchmark. It is
reported as reached or not reached; it is not a hidden second success test.

Safety estimand:

```text
Delta_VOR = mean_M[VOR(i,F2)] - mean_M[VOR(i,F1)]
```

`M` is the frozen manifest subset whose stipulated supporting-origin certainty
is `multiple`, expected to contain 75 primary bundles. Invalid outputs receive
`VOR=0`. F2 passes the candidate non-inferiority guardrail only if the
one-sided 95% lower confidence bound exceeds `-0.05`. The interval method and
coverage simulation must be frozen for the actual `|M|` before preregistration.
If adequate precision is not demonstrated, VOR becomes a descriptive
guardrail and “non-inferior” leaves the claim ladder before any run.

## Conditions

Every condition receives the same target claim, evidence text, report order,
opaque IDs, dates, metadata-row shape, model/checkpoint, decoding policy,
output schema, output-token cap, retrieval count, and tool count.

| ID | Prompt-visible difference | Role |
| --- | --- | --- |
| **F0 — ordinary/citation-only** | `NONE` relation placeholders and an ordinary bounded evidence-assessment instruction; the shared codebook remains visible to equalize exposure | Secondary baseline |
| **F1 — rule only** | Explicitly count distinct origin pathways when supplied information permits, do not count repeated/derived reports as independent support, and preserve unknown; all relation slots are `NONE` | Primary comparator |
| **F2 — supplied typed cue** | Byte-identical F1 instruction; relation slots contain `DPND`, `INDP`, or `UNKN` from the stipulated graph | Primary intervention |

`INDP` means independent-as-stipulated in the synthetic benchmark only.
`DPND` means a documented dependent relation in that graph. `UNKN` is not a
negative relation and cannot be counted as independent. An original/root
report receives `UNKN` when no parent relation is supplied; the benchmark does
not invent an `ORIGINAL` cue.

Exact F1/F2 equality is required twice:

- exact per-bundle input-token equality under the selected frozen model’s
  actual tokenizer; and
- exact per-bundle input byte-length equality as a separate implementation
  resource-control receipt.

The current deterministic regex tokenizer is development scaffolding only. It
cannot authorize a primary split or stand in for the selected model tokenizer.

## Corpus

The complete planned inventory is 480 fictional bundles:

| Split | Bundles | Purpose | Efficacy status |
| --- | ---: | --- | --- |
| Development | 80, 20 per structure | Generator, parser, prompt, and leakage repair | Never efficacy evidence |
| Feasibility pilot | 40, 10 per structure | Replay, runtime, parser, audit, and power-plan feasibility | Never efficacy evidence; cannot tune a favorable endpoint |
| Primary | 300, 75 per structure | Fixed F2-versus-F1 confirmatory analysis | Opened only after every lock/gate |
| Stress | 60 | Relation noise at 0.05/0.10/0.20 crossed with structure; order/overlap/code-position diagnostics | Descriptive only |

The four primary structures are:

1. one-origin repetition;
2. three-origin convergence, independent only as stipulated;
3. unknown origin, with certification deliberately withheld; and
4. conflict, with separate support/refute paths and a dependent copy on each
   side.

Each bundle contains one bounded claim and four to six short reports. Split by
proposition family and origin family, not by document row. No proposition,
origin family, paraphrase family, or derived report may cross development,
pilot, primary, or stress. The synthetic manifest establishes construction
relations only; it does not establish real-world honesty, authority, causal
independence, prevalence, or truth.

## Output and invalid-output contract

Every run must emit one JSON object and nothing else:

```json
{
  "origin_count_supporting": 0,
  "claim_state": "supported | refuted | insufficient | contested",
  "confidence": 0.0,
  "evidence_ids": ["opaque_report_id"]
}
```

The parser rejects Markdown fences, prose, multiple objects, duplicate or
unknown keys, invalid UTF-8, wrong types, non-finite/out-of-range numbers,
duplicate evidence IDs, unknown evidence IDs, and arrays beyond the fixed
limit. Raw bytes are stored before parsing with length and SHA-256. There is no
manual repair, retry, coercion, or reconstruction of
`origin_count_supporting` from citations, claim state, or selected evidence.

The scalar `confidence` is descriptive. It is not automatically a calibrated
probability of correct origin accounting or a multiclass claim state. No
calibration endpoint enters the confirmatory family until an explicit target
probability and proper scoring rule are specified in a separate versioned
study.

## Shortcut and contamination argument

A positive result is uninteresting if the model can obtain it from formatting
or direct code counting alone. Before opening the primary split, the project
must freeze and pass:

- opaque non-semantic IDs;
- relation codes of equal byte length and a codebook permutation check;
- condition-invariant metadata width, delimiters, report order, and evidence
  text hashes;
- low-overlap dependent paraphrases and high-overlap
  independent-as-stipulated reports;
- crossed domain, style, length, position, and presentation order;
- proposition/origin-family split blocking plus exact/near-duplicate audit;
- a blocked character/token surface-only classifier with a prespecified
  ceiling and Wilson interval;
- deterministic metadata-only and field-only diagnostics;
- relation-code position and report-order perturbations; and
- the locked 60-bundle relation-noise stress set.

The current local nearest-centroid probe is not this gate. It is a smoke
diagnostic and, on the 16-bundle smoke corpus, is trivially separable. That
result is an explicit warning that the full blocked leakage and semantic audit
remain unresolved; it is not a pass. A gain matched by direct code counting or
preserved after replacing report text is a shortcut/direct-code result, not
semantic evidence integration.

## Analysis and multiplicity

The confirmatory family contains exactly two decisions:

1. F2 versus F1 on all-assigned `FC_cons`;
2. F2 versus F1 on fixed-set `VOR` as a safety/non-inferiority gate.

F0 contrasts, claim-state accuracy, confidence, evidence-ID precision/recall,
absolute count error, structure/domain/style slices, stress/noise behavior,
latency, tokens, memory, and any optional second-model check are descriptive
or exploratory. They cannot rescue a failed primary or safety decision.

The power program uses paired Bernoulli simulations over plausible F1 risk,
paired discordance, F2-minus-F1 differences, invalid-output rates, and the
fixed `|M|`. Simulations must report power, type-I error under delta zero,
interval coverage, and probability of passing the safety gate. The feasibility
pilot may repair implementation and runtime assumptions; it cannot supply a
favorable efficacy effect size for choosing `N`.

## Natural-syndication transfer: T1

`research/REAL_SYNDICATION_TRANSFER_FEASIBILITY_V1.md` supports one disposition:
**include as descriptive T1**, after primary prompt/analysis locks and only if
rights and annotation gates pass.

- NEWS-COPY’s duplicate relation means same original source article and can
  support a bounded `DPND` candidate fixture.
- NEWS-COPY nonduplicates cannot be relabeled `INDP`; same-story, shared-quote,
  and updated articles can be nonduplicates.
- Newswire exposes one representative per inferred reproduction cluster plus
  aggregate recurrence metadata; `cluster_size` is not origin count.
- Neither resource supplies the target claim, claim stance, support/refute
  spans, support-origin sets, real-world independence, or multiple-origin
  ground truth.
- NEWS-COPY data rights remain unresolved; Newswire’s exact release/version and
  field-level license must be pinned before reuse.

T1 therefore has its own manifest, rights receipt, annotation provenance,
transfer-only flags, and descriptive report. It never enters `A`, `M`, the
McNemar test, either interval, VOR, or a primary effect estimate. No F3 exists.

## Locked result interpretations

| Observed pattern | Required interpretation |
| --- | --- |
| F2 passes primary and safety gates | A bounded supplied-cue condition effect for the tested model/task/format; no discovery or transfer claim |
| F2 does not meaningfully beat F1 | No evidence of added typed-cue value beyond the explicit rule in this setting |
| F1 and F2 beat F0 but tie each other | Attribute the effect to the explicit rule, not the populated relation field |
| F2 reduces FC but fails VOR | Reject the tested cue; it encourages blanket discounting of valid stipulated convergence |
| F2 is worse | Preserve the harmful result and retire/quarantine the tested cue |
| Effect disappears under noise, parity, order, style, or formatting controls | Report a narrower or shortcut-driven interpretation; do not retain the mechanism claim |
| Metadata-only/field-only control matches the effect | Direct-code behavior, not semantic evidence integration |
| Direction changes across declared seeds/stress/optional model | Model/configuration-specific instability; no pooled favorable claim |
| Synthetic effect fails descriptive T1 | No real-world origin-accounting or transfer claim |

No unfavorable outcome may be hidden, rerun until favorable, or replaced with
a post hoc endpoint. A negative gate stops escalation from this mechanism; it
does not retroactively prove or disprove unrelated conceptual responsibilities.

## Paper architecture after a run is authorized

1. **Problem:** false corroboration from report-level repetition.
2. **Prior-art boundary:** copying, double counting, redundancy, diversity,
   conflict, and source-dependence precedents.
3. **Residual question:** supplied origin cue versus an explicit rule.
4. **Method:** synthetic graphs, F0/F1/F2 parity, one frozen model, strict
   parser, fixed denominators, and shortcut controls.
5. **Results:** every assigned bundle, invalid counts, primary interval/test,
   fixed safety result, and all negative-result commitments.
6. **Diagnostics:** direct-code, surface, position/style, relation-noise, and
   descriptive slices.
7. **Limits:** oracle cue, synthetic graph, one model, no provenance discovery,
   no human/field/deployment claim, and no automatic real-world transfer.
8. **Reproducibility:** generator, seeds, prompts, raw outputs, parser, analysis,
   invalids, hashes, environment, and authorization boundary.

If the study has not run, sections 5–6 cannot be mocked, templated with
plausible values, or represented as a results dashboard.

## Wider program, kept outside this paper

Later studies may separately test noisy/predicted relations, construct
comprehension, terminology, claim/evidence structure, cost-bounded routing,
human correction, versioned memory, or field outcomes. Each needs its own
estimand, unit, baseline, outcome, safety measure, ethics/privacy review, and
power plan. They must not be bundled into the current paper to make a larger
story.

Potential sequence:

1. P1 — current supplied-origin-cue benchmark;
2. P2a — noisy/predicted origin relations **or** P2b — human construct
   comprehension, not both in one study;
3. P3 — matched strong-baseline action-policy comparison only if P1/P2 justify
   it;
4. P4 — one compact human correction interface and one human primary outcome;
5. P5 — optional bounded field feasibility after governance and ethics review;
6. P6 — independent second-domain or adversarial replication.

## Current readiness and stop line

Available now:

- verified prior-art and transfer memos;
- ten closed JSON Schema contracts;
- deterministic fictional generator and opaque IDs;
- F0/F1/F2 prompt construction with local surrogate token/byte parity;
- strict parser and immutable raw-output receipts;
- fixed-denominator scorer and paired-analysis scaffolding;
- split, duplicate, surface, metadata-only, field-only, noise, balance, and
  planning-simulation diagnostics;
- seven passing focused offline tests, 18 passing parser fixtures, and a
  16-bundle offline smoke receipt.

Not available or authorized:

- selected model/checkpoint or intended tokenizer;
- full semantic audit or cleared surface-leakage gate;
- frozen primary bundle manifest or fixed `M` hash;
- validated VOR interval coverage at `|M|`;
- preregistration or ethics determination;
- model/pilot/primary/transfer output;
- publication, public release, deployment, or provider spend.

The stop line is simple: the next authorized artifact may be a code/method
review and owner decision on a model/tokenizer budget. It is not a model run.

## Owner decisions required before any empirical phase

1. Whether to proceed after reviewing the bounded contribution and current
   leakage/semantic-audit burden.
2. Which one locally runnable open-weight instruction model/checkpoint and
   tokenizer to freeze, with an explicit compute/time budget.
3. Whether the VOR interval/coverage plan is adequate at fixed `|M|` or must be
   downgraded before preregistration.
4. Whether any pilot is authorized after code, corpus, rights, privacy, and
   preregistration review.
5. Whether descriptive T1 remains worthwhile after NEWS-COPY rights and
   Newswire version/field licensing are resolved.

No choice above is inferred from this prospectus. Until separately authorized,
the program remains a local thought piece, research design, and offline
scaffold with no empirical result.

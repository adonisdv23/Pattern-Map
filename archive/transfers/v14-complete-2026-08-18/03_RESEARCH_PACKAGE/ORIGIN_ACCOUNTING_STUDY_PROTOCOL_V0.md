# Oracle Origin-Relation Metadata in One Frozen Model

**Protocol version:** 0.3 design draft  
**Specification version:** `loop3-operationalization-0.3`  
**Prepared:** 2026-08-18  
**Status:** proposed offline benchmark protocol; no corpus, implementation, preregistration, model run, result, ethics determination, or publication exists  
**Relationship to the larger project:** this is the narrowest current first-paper candidate. It tests one representation/use mechanism and cannot validate the full Pattern Recognition / Discrimination Layer framework.
**Implementation companion:** [Loop 3 consolidated operationalization specification](overnight/rounds/08_LOOP2_OPERATIONALIZATION_SPEC.md), which fixes the JSON/JSONL contracts, generator grammar, prompts, parser, metrics, power simulation, QA gates, and release manifest.

## Answer first

Test one bounded question:

> For one frozen model, does a condition containing an explicit origin-relation field—dependent, independent-as-stipulated, or unresolved—produce fewer false-corroboration errors than the same evidence and the same origin-counting rule without that field?

F2 is deliberately an **oracle origin-relation metadata condition**. It asks whether a frozen model uses a benchmark-stipulated field under a fixed counting rule. It does not test whether a system can discover provenance, establish real-world epistemic independence, retrieve good evidence, improve a human decision, route acquisition, or validate the complete framework.

## Claim permitted by a positive result

If the primary and safety criteria pass, the strongest permitted claim is:

> On newly authored fictional evidence bundles with stipulated provenance graphs, the typed-metadata condition produced less false corroboration than the rule-only condition on the tested frozen model, while recall of stipulated supporting origins remained above the prespecified safety margin.

The study must not translate that result into claims about truth, real-world consensus, source authority, retrieval quality, human correction, enterprise use, or universal AI behavior.

## Primary estimand

For every assigned primary bundle, compare the typed-cue condition with the rule-only condition on a paired item basis. The primary estimand uses a fixed all-assigned denominator and risk-codes invalid outputs conservatively:

`Delta_FC_cons = mean_A[FC_cons(i,F2)] - mean_A[FC_cons(i,F1)]`, where `A` is all 300 assigned primary bundles.

Lower is better. The experimental unit is the **bundle**, not a report, model seed, generated token, or repeated run.

## Corpus

### Primary set

- 300 novel fictional evidence bundles, balanced at 75 per origin structure.
- Four to six short reports per bundle, one bounded target claim, and a complete source-artifact-origin-time manifest.
- At least two fictional content domains and multiple report styles crossed with origin structure and presentation order.
- No real person, current allegation, private record, consequential recommendation, or provider-dependent live retrieval.

### Development and pilot material

- 80 development bundles, 20 per origin structure, for generator, parser, prompt, and leakage repair only.
- 40 pilot bundles, 10 per origin structure, for end-to-end feasibility, replay, resource logging, and power-plan calibration only.
- No proposition family or origin family may cross development, pilot, primary, or stress splits. Pilot effects are not efficacy evidence and cannot tune a favorable endpoint.

The four origin structures are:

1. **One-origin repetition:** all supporting reports derive from one original artifact.
2. **Multiple-origin convergence:** supporting reports derive from three separately authored origins; this is independent only as stipulated by the benchmark graph.
3. **Unknown origin:** reports agree, but the relation is intentionally withheld and must remain unknown.
4. **Conflict:** separate origin paths support and refute the claim, with at least one dependent copy on one side.

### Locked stress set

- 60 additional bundles, frozen before the primary run.
- Exactly 60 cells are allocated as four origin structures × three nonzero relation-noise rates (`0.05`, `0.10`, `0.20`) × five bundles. Report-order, overlap, and relation-code/position permutations are assigned by a frozen balanced subcell table; these factors are descriptive and are not independently powered.
- Every record carries `stress_variant`, `noise_rate`, `noise_seed`, and `stress_cell_id`. A later public-corpus transfer challenge is a separately named `transfer` split and cannot reuse these 60 bundles or enter the primary/safety analyses.
- Secondary and descriptive only; the stress set cannot enlarge the primary sample after results are seen.

### Truth boundary

The generator may establish source, artifact, transformation, time, claim polarity, and report-to-origin membership by construction. It cannot establish real-world source honesty, causal independence, prevalence, usefulness, authority, or truth. Use **origin relation** and **origin accounting**, not unqualified independence or consensus.

Keep four vocabularies separate: derivation (`copied`, `paraphrased`, `summarized`, `quoted`, `inferred`); origin-family (`same`, `distinct-as-stipulated`, `unresolved`); claim stance (`supports`, `refutes`, `qualifies`, `insufficient`); and action (`provisional`, `hold`, `escalate`, `authorized`). The first study manipulates only the origin-family relation. One generic `relation` field must not stand in for all four.

## Conditions

All conditions receive the same target claim, evidence text, report order, model/checkpoint, decoding, output schema, output-token cap, and metadata skeleton. F1 and F2 must have **exact per-bundle input-token parity** under the locked tokenizer; F0 is padded to the same target and remains secondary. If exact F1/F2 parity cannot be achieved, stop before opening the primary split.

| ID | Condition | Difference from the others | What it estimates |
| --- | --- | --- | --- |
| **F0** | Citation only | Opaque source/artifact IDs and dates; no origin rule or relation cue | Ordinary bounded evidence assessment |
| **F1** | Rule only | Adds: count distinct origin pathways; do not treat repeated reports as independent; preserve unknown | Effect of an explicit cognitive/policy rule |
| **F2** | Stipulated origin-relation metadata | Uses the byte-identical F1 rule and populates the fixed relation field with `dependent`, `independent_as_stipulated`, or `unknown` | Value of this supplied relation metadata beyond the rule |

The headline comparison is F2 versus F1. F0 versus F1 and F2 versus F0 are secondary. No retrieval, router, memory, human-interface, or outcome-feedback condition belongs in this first study.

## Output contract

Every run returns one strict object:

```json
{
  "origin_count_supporting": 0,
  "claim_state": "supported | refuted | insufficient | contested",
  "confidence": 0.0,
  "evidence_ids": ["opaque_id"]
}
```

The parser, invalid-output policy, and claim-state decision rule are frozen before the primary run. Invalid outputs are failures under the primary risk-coded estimand; there are no manual retries after test lock. `origin_count_supporting` is a separate model assertion and is never repaired from `claim_state` or `evidence_ids`; deterministic consistency flags are descriptive only.

## Primary and safety endpoints

### Primary endpoint: false corroboration

A false-corroboration observation occurs when a valid output reports two or more supporting origin paths although the restricted manifest certifies zero or one supporting origins—or withholds that supporting-origin certification as unresolved. Define `FC_obs(i,c)=1` only for that valid observed event. Define the all-assigned primary risk code as `FC_cons(i,c)=1` when the output is invalid or `FC_obs(i,c)=1`; otherwise it is zero. Define `FC_lib(i,c)=1` only for valid `FC_obs` events. Claim-state behavior is reported separately so the primary estimand does not mix origin counting with stance accuracy. Complete-case `FC_valid`, invalid counts, and reason codes are locked sensitivities; no parse failure changes the primary denominator.

### Safety endpoint: recall of stipulated supporting origins

Let `M` be the fixed manifest set whose `gold_support_origin_certainty` is `multiple`—expected to be the 75 multiple-origin-convergence bundles. On every bundle in `M`, measure whether a valid output reports at least two origins and selects evidence from at least two stipulated supporting origins without counting dependent copies. Invalid outputs are `VOR=0`; `M` is never intersected with a post-run valid-output set. Freeze the manifest membership hash before the run. F2 is called non-inferior only if the one-sided 95% lower confidence bound for `Delta_VOR = mean_M[VOR(i,F2)] - mean_M[VOR(i,F1)]` is greater than `-0.05`. The five-point margin is a synthetic-task design choice, not a discovered or universal threshold.

The confirmatory family contains exactly two decisions. A bounded superiority statement requires the exact paired F2-versus-F1 test on `FC_cons` at two-sided `alpha=.05`, in the beneficial direction, with the 95% interval’s upper bound below zero. The `-0.08` effect remains a planning/practical benchmark and is reported as reached or not reached; it is not an additional success threshold. The safety gate must also pass the one-sided VOR criterion above. Claim-state accuracy and stress results are descriptive and cannot rescue either decision.

### Secondary measures

- absolute origin-count error;
- claim-state accuracy, descriptive only;
- evidence-ID precision/recall;
- selected-state confidence, descriptive only; the scalar output is not a multiclass probability vector and must not be reported as a Brier score;
- invalid-output rate;
- input/output tokens, latency, memory, and local compute;
- stress-set performance and exploratory moderation by origin structure/domain.

Do not manufacture a decision-utility score for fictional bundles without a defensible consequence function.

## Leakage and shortcut controls

| Risk | Required control |
| --- | --- |
| Origin IDs reveal cluster count | Random opaque IDs per bundle; no sequential or semantic origin labels |
| Typed formatting reveals condition | Identical fixed-width metadata slots and delimiters in every condition; placeholders where relations are absent |
| Lexical copying solves the task | Cross surface similarity with origin structure: low-overlap dependent paraphrases and high-overlap independent-as-stipulated reports |
| Template or position reveals relation | Cross report style, simulated author voice, and order across all structures; hold out combinations |
| Proposition/origin family crosses splits | Split by underlying proposition and origin family; exact and near-duplicate audit |
| Generator punctuation/length leaks labels | Fit a surface-only blinded condition/label classifier; quarantine the corpus if it exceeds the preregistered ceiling |
| Relation codes can be counted without integrating report evidence | Run a deterministic metadata-only counter and a field-only model diagnostic. If a claimed gain is matched by direct code counting or survives without report text, label it a formatting/direct-code shortcut rather than semantic evidence integration. |
| Supplied gold relations are mistaken for inference | Call F2 an oracle-cue representation test in the title, abstract, methods, and limitations |
| Public data is relabeled as independent | Keep public transfer descriptive and use `unknown` unless derivation is documented |
| Human-readable labels or positions drive the result | Lock neutral-code, codebook-permutation, field-position, and report-order stress conditions before the primary run |
| Perfect relations are mistaken for deployment readiness | Run predeclared relation-noise stress conditions and call any fragile gain an oracle upper bound only |

## System and run lock

- One frozen, locally runnable open-weight instruction model selected before the primary test split is opened; the title, abstract, results, and conclusion retain the one-model boundary.
- Deterministic decoding for the primary run, or exactly three seeds declared in advance if the backend is nondeterministic.
- Seeds are nested uncertainty within bundle; they do not increase the item sample size.
- Optional second model only as an unpowered robustness analysis.
- No live web, paid provider, tool acquisition, prompt tuning, or manual output repair after the lock.
- Record model/checkpoint hash, tokenizer, prompt hash, corpus/split hashes, decoding, parser, hardware, timing, and every invalid run.

## Analysis and planning

- One two-sided primary superiority contrast at alpha .05: F2 versus F1 on all-assigned `FC_cons`.
- Use the exact paired McNemar/binomial test over all 300 risk-coded bundle pairs, report the paired absolute risk difference, and report a 95% paired bootstrap interval from 10,000 bundle resamples. Report complete-case and liberal invalid codings only as prespecified sensitivities. A mixed-effects model is secondary robustness only.
- The only other confirmatory decision is VOR non-inferiority on the fixed `M` set, using the one-sided 95% lower confidence bound and `-0.05` margin defined above. F0 comparisons, claim-state accuracy, stress performance, domains, structures, seeds, and optional-model slices are descriptive/exploratory; there is no secondary Holm family in this first protocol.
- Before finalizing `N`, run and publish paired-Bernoulli simulations for both endpoints. The FC grid covers 20–40% F1 risk, an eight-point practically important planning difference, 10–30% paired discordance, and invalid rates of 0%, 2%, 5%, and 10%. The VOR grid fixes `|M|` from the manifest and crosses plausible F1 VOR, discordance, effects of `0`, `-0.02`, `-0.05`, and `-0.08`, and the same invalid rates under invalid=`0`. Run at least 10,000 repetitions per cell and report type-I error, coverage, power, and probability of passing the one-sided gate. If the VOR margin is not estimable at the target precision, downgrade it to a descriptive guardrail and remove “non-inferior” from the claim ladder before preregistration.
- A pilot repairs the generator, parser, timing, and feasibility thresholds; it is not a trustworthy efficacy effect-size estimate ([Leon, Davis & Kraemer, 2011](https://doi.org/10.1016/j.jpsychires.2010.10.008)).
- No efficacy peeking. Early termination is limited to safety/data quarantine or a technical failure governed by a predeclared invalidation rule.

## Gates

### Safety/data quarantine

Stop affected runs for private/secret material, unauthorized retrieval, real-person harmful labeling, untraceable evidence, cross-condition leakage, or unrecoverable manifest corruption. Preserve the receipt and do not interpret quarantined data as efficacy evidence.

### Feasibility

Thresholds are frozen before any pilot primary outputs are inspected:

- at least 98% parsable outputs;
- 100% schema and provenance-graph invariant checks on generated records;
- no unresolved exact/near-duplicate cross-split leakage;
- no private or sensitive text;
- replay within the documented deterministic or seed-bounded behavior;
- no more than 10% primary-bundle invalidation for data-quality reasons.

The full eleven-gate pilot sequence—including deterministic regeneration, semantic QA, split leakage, exact prompt parity, parser fixtures, runtime, shortcut probes, power, and governance—is normative in the [operationalization specification](overnight/rounds/08_LOOP2_OPERATIONALIZATION_SPEC.md). Passing those gates establishes feasibility only, not efficacy.

### Falsifiers and narrowing

| Result | Required interpretation |
| --- | --- |
| F2 does not beat F1 by the minimum important effect | No evidence that typed cues add value beyond the explicit rule in this setting |
| F2 lowers false corroboration but violates the recall margin | Reject the current cue; it encourages blanket discounting |
| F1 and F2 tie while both beat F0 | The rule, not the relation metadata, explains the effect |
| F2 wins only on formatting-easy cases | Treat as shortcut leakage and repair before any efficacy claim |
| F2 succeeds only with perfect relations and fails under declared noise | Claim an oracle-cue upper bound only |
| Effect is unstable across seed/model | Report instability and keep the claim model-specific |
| Synthetic success fails a documented public transfer challenge | Make no real-world origin-accounting claim |
| Metadata overhead is material | Report the cost trade-off; make no efficiency claim |

## Reproducibility package if publication is later authorized

- generator code, seeds, truth manifests, schema, and dataset card;
- frozen prompts, fixed-width condition templates, parser, and analysis code;
- model/configuration hashes and complete run ledger;
- surface-shortcut classifier and leakage report;
- semantic-audit guide and adjudication records;
- power simulation, preregistration, all invalid outputs, and negative results.
- canonical release manifest using RFC 8785 JSON canonicalization, with file hashes, row counts, schema IDs, version pair, visibility levels, model/checkpoint/tokenizer and license data, synthetic-only status, privacy/secret scan status, and an explicit no-public-release-until-authorized policy.

## Closest methodological and substantive anchors

- [Zhang, Ives & Roth (2020), natural-language claim provenance](https://aclanthology.org/2020.acl-main.406/) shows why common source origin can distort article-level evidence counts; it does not validate this intervention.
- [W3C PROV-O](https://www.w3.org/TR/prov-o/) supplies lineage vocabulary; provenance is not correctness or independence.
- [Cochrane Handbook, chapter 4](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04) is an authoritative precedent for collating multiple reports of one study; the proposed synthetic task is not evidence synthesis.
- [Laitenberger, Manning & Liu (2025)](https://aclanthology.org/2025.emnlp-main.1656/) motivates a strong, resource-matched simple baseline.
- [HydraRAG (2025)](https://aclanthology.org/2025.emnlp-main.730/) and [CONFACT (2025)](https://www.ijcai.org/proceedings/2025/1073) show that cross-source corroboration, source reliability, and evidence conflict already belong to integrated current systems.
- [FaithfulRAG (2025)](https://aclanthology.org/2025.acl-long.1062/) motivates the safety boundary: forced context adherence can trade against valid model knowledge.
- [CLUE (2026)](https://aclanthology.org/2026.acl-long.2110/) is direct peer-reviewed precedent for typed claim–evidence and inter-evidence conflict/agreement relations.
- [Xia (2026 preprint)](https://arxiv.org/abs/2606.06758) is a close methodological precedent for matched evidence-utilization conditions; it is not peer-reviewed evidence for this task.
- [ProvenanceGuard (2026 preprint)](https://arxiv.org/abs/2606.18037) separates pooled support from exact source ownership in agent traces; it is post-generation verification, not this origin-cue test.
- [BERGEN (2024)](https://aclanthology.org/2024.findings-emnlp.449/) shows why oracle evidence and benchmark labels are not universal guarantees of improvement.
- [Nematov et al. (2025 preprint)](https://doi.org/10.48550/arXiv.2507.04480) analyzes source attribution, redundancy, complementarity, and synergy in RAG; it is a close source-influence comparator, not this supplied-origin-field contrast.
- [Lakens (2013)](https://doi.org/10.3389/fpsyg.2013.00863) motivates explicit effect sizes and practically meaningful thresholds.

This protocol becomes a study only after its corpus, code, estimand, thresholds, analysis, and release boundary are frozen. Until then it is a falsifiable design artifact, not research evidence.

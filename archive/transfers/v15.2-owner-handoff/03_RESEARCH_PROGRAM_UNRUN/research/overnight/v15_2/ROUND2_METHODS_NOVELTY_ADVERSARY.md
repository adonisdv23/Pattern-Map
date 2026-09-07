# Round 2 methods and novelty adversary — Pattern Map v15.2

**Lane:** independent methods / novelty red team
**Prepared:** 2026-08-19
**Worktree:** `/Users/gpt/Documents/Codex/worktrees/discrimination-layer-v15-2-overnight`
**Branch:** `codex/discrimination-layer-v15-2-overnight`
**Status:** `AUDIT_ONLY · NO STUDY RUN · NO MODEL/PROVIDER/NETWORK EXPERIMENT`

## Executive decision

The v15.2 package remains a coherent pre-run protocol, not an execution-ready
study and not a results package. Round 2 finds no basis for broad “new
discrimination layer,” provenance-discovery, real-world independence, truth,
human-benefit, or reusable-benchmark claims. The defensible residual remains a
bounded, frozen-model diagnostic: whether a visible, benchmark-stipulated
origin-relation cue changes a thresholded output-risk event beyond the same
explicit counting rule under matched resources.

The provisional Dempster–Shafer / EvidentialRAG lead is **DEFERRED**. The
checked EvidentialRAG v1 preprint is direct evidence that one recent system
uses a conflict-preserving, parameterized evidence-fusion router. It is not
evidence that retrieved passages are independent, and it is not evidence that
the Pattern Map F0/F1/F2 protocol needs a Dempster–Shafer arm. Foundational and
dependence-aware sources make distinct/independent evidence an explicit
condition for standard Dempster pooling, while the checked EvidentialRAG text
does not state or operationalize source-family, duplicate, or dependence
handling. That gap is a methods risk, not a formal-error finding.

The two adversarial counterexamples below are mathematical derivations from the
EvidentialRAG equations, not empirical results:

1. repeated identical evidence compounds support (`0.9 → 0.99 → 0.999` for
   two and three identical masses), even though repetition may add no new
   information; and
2. the reported pairwise operator is order-sensitive on a three-mass example,
   changing the default router from “direct answer” to “conflict-aware” when
   the same masses are folded in a different order.

Neither derivation proves the paper’s implementation is formally invalid. A
ranked, order-dependent fold could be an intended design. It does establish
that any future comparison must state its dependence, ranking, duplicate, and
fold semantics and must publish order/duplication sensitivity checks.

For Pattern Map, Round 2 retains the F2-versus-F1 candidate only with the
Round 1 gates. `FC_cons` must be named and interpreted as a conservative
asserted-count-risk composite (or its invalid and valid-only components must be
made an explicit interpretation gate); VOR is a threshold safety guardrail,
not exact origin accounting; `N=300` and `|M|=75` remain planning candidates;
actual tokenizer/chat-template parity, leakage clearance, semantic/stance
audit, and coherence fixtures remain prerequisites. No model run is authorized
by this report.

## Scope, truth boundary, and inspection receipt

This pass read the v15.2 charter, both specified Round 1 research artifacts,
the canonical protocol and implementation-readiness memo, and the relevant
offline harness and tests. It also checked current primary or official source
records for the Dempster–Shafer/EvidentialRAG question. No provider, model,
paid service, live retrieval, external corpus experiment, deployment,
preregistration, publication, or production action was performed.

The only files created by this lane are this report and
`ROUND2_METHODS_DECISION_MATRIX.md`. Existing untracked work in the checkout
was preserved.

The local package establishes these facts, which are treated as observations,
not as negotiable interpretations:

- no model, checkpoint, tokenizer revision, chat-template receipt, primary
  output, pilot, or empirical result exists;
- the synthetic graph supplies benchmark construction labels; `INDP` means
  separately rooted **as stipulated in this benchmark**, not causal,
  epistemic, editorial, or real-world independence;
- `UNKN` is unresolved and must not be silently imputed to either dependence or
  independence;
- local generator/parser/scorer/tests establish offline code-path invariants,
  not model behavior, provenance discovery, or generality;
- T1 is a separate descriptive and rights-gated transfer tier and cannot enter
  the primary denominator or confirmatory inference.

### Local artifacts inspected

| Artifact | Adversarial check | Round 2 finding |
| --- | --- | --- |
| `reports/overnight/v15_2/PROGRAM_CHARTER.md:1-110` | Overnight objective, truth boundary, and no-run/integration rules | The charter forbids silently converting a proposal into a study or result. This report remains a research handoff, not authorization. |
| `research/overnight/v15_2/ROUND1_RESEARCH_METHODS_AUDIT.md:1-705` | Round 1 methods findings, P0/P1/P2 recommendations, direct verdicts | Round 1 correctly narrowed the residual claim and identified the open gates. Every material recommendation is dispositioned in the companion matrix. |
| `research/overnight/v15_2/ROUND1_RESEARCH_SOURCE_LEDGER.md:1-142` | Source/status boundary and prior-art deltas | Broad provenance, evidence-fusion, source-attribution, conflict-aware-RAG, and metadata-bias novelty is not supported. The D-S lead is adjacent prior art, not a novelty rescue. |
| `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:1-612` | F0/F1/F2 conditions, estimands, endpoints, denominators, parity, power, controls, T1 and release gates | Protocol is internally legible, but final interval validation, actual resource parity, leakage/semantic clearance, and coherence interpretation are open. |
| `research/F0_F1_F2_IMPLEMENTATION_READINESS_V1.md:1-404` | Implementation versus empirical readiness; status and release requirements | Correctly calls the surrogate tokenizer and smoke diagnostics non-authorizing. It does not supply a model run or release-grade receipt. |
| `tools/origin_accounting/analysis.py:122-168,364-454` | `FC_cons`, `VOR`, denominator guards, paired analysis | `FC_cons` uses validity/count/certainty only; VOR uses validity/count/selected support-origin threshold only. Confirmatory mode fails closed on exact `A=300`, `|M|=75` manifest shape. |
| `tools/origin_accounting/power.py:44-291` | Planning model, invalid coding, VOR grid, bootstrap scaffold | Invalid outputs are simulated independently between F1 and F2; no invalid dependence or condition-specific invalidity is modeled. The scaffold is planning-only. |
| `tools/origin_accounting/parser.py` | Strict output contract | Duplicate keys, wrong IDs, wrong types, non-finite confidence, and malformed JSON fail closed; no repair/retry/coercion. This supports invalidity decomposition but does not itself define construct validity. |
| `tools/origin_accounting/generator.py:220-270,540-590,629-749` | F0/F1/F2 prompt construction, relation codes, report duplication, hash receipts | F1/F2 share the rule bytes; F2 exposes `DPND`/`INDP`/`UNKN`. `INDP` remains stipulated. The F2 relation code is intentionally visible and can be counted directly. |
| `tools/origin_accounting/diagnostics.py:30-83,153-183` | Leakage and metadata-only smoke diagnostics | Smoke output is `clearance_unresolved`; no blocked held-out-family classifier or independent semantic audit has cleared the primary corpus. |
| `tests/test_origin_accounting.py:1-485` | Offline regression coverage | Fifteen focused tests cover local invariants, not semantics. No explicit contradictory count/stance/evidence fixture or invalidity-only-versus-valid-only interpretation fixture was found. |

### Project-history receipt for the D-S/EvidentialRAG lead

The lead was not inferred from a search result alone. The following project
history was checked to recover its intended scope and prior disposition:

| History artifact | Direct project-history observation | Round 2 implication |
| --- | --- | --- |
| `source/THOUGHT_PIECE_V15.md:362-371` | Names EvidentialRAG as an arXiv v1 conflict/uncertainty-fusion comparator and says it proposes fusion rather than origin inference. | The thought piece already treats the lead as adjacent prior art, not as a Pattern Map mechanism or evidence of provenance discovery. |
| `research/PAPER_PROSPECTUS_V1.md:88-99` | Records EvidentialRAG as arXiv v1 submitted 2026-07-11, with no venue/acceptance shown, and labels it a conflict/uncertainty-fusion comparator rather than an origin-relation system. | Status and construct boundaries are preserved; no publication or priority language is upgraded. |
| `research/PRIOR_ART_DELTA_V1.md:217-232,374-387,412,477-501` | Separates conflict/uncertainty fusion from origin/source dependence, lists EvidentialRAG as S10, and explicitly keeps conflict-aware systems adjacent/future rather than required F0/F1/F2 arms. | The history already rejects substituting conflict for origin. Round 2 adds the independence, duplicate, and fold-order adversary without changing the locked core. |
| `reports/V15_LOOP1_EVIDENCE_NOVELTY_REVIEW.md:57-59,96-102,124-131` | Records the arXiv-only status, conflict/uncertainty scope, and requirement to show working-manuscript status inline; confirms no conflict-system arm was added to F0/F1/F2. | Round 2 maintains the source-status correction and does not turn an unreviewed comparator into settled evidence. |
| `reports/V15_DECISION_LEDGER.md:156-161` (D011, D012, D015) | Rejects generic mechanism novelty; defers retrieval/dedup/conflict-system arms; preserves the F0/F1/F2 core while qualifying EvidentialRAG status. | The D-S lead is explicitly a deferred comparator. Its Round 2 disposition is `DEFER`, with broad novelty and default-independence readings rejected. |

**[INFERENCE]** The history is internally consistent: the lead is useful for
prior-art adjacency and future comparison, but it is not a missing component
whose absence makes the F0/F1/F2 protocol defective. Round 2 therefore tests
the lead's assumptions without adding it to the current causal contrast.

## Evidence labels used in this report

- **[SOURCE]** — directly stated or directly recorded by the linked primary,
  official, or local source.
- **[DERIVATION]** — arithmetic or logical consequence calculated from a
  source-defined equation or the checked local contract; not an experiment.
- **[INFERENCE]** — a bounded interpretation of source evidence or a threat
  model; it is not directly measured here.
- **[UNKNOWN]** — not established by the checked artifacts or source record.

This labeling is important for the EvidentialRAG lead. A source can support a
warning about assumptions without proving that a particular implementation
violates them.

## Current primary/official source ledger for the D-S lead

The URLs below are the records consulted on 2026-08-19. Dates are publication
or submission dates shown by the record; “checked” is the current audit date.
The publisher pages are used for published technical papers. The EvidentialRAG
record is an arXiv preprint, even though its HTML metadata includes a journal
label; no independent acceptance or final-version record was located.

| ID | Record, status, date, URL | Direct source evidence relevant to this audit | Boundary |
| --- | --- | --- | --- |
| E01 | S. M. Asif Hossain, Ruksat Khan Shayoni, M. F. Mridha, **“EvidentialRAG: Quantifying and Mitigating Information Conflict in Multi-Source Retrieval-Augmented Generation via Evidential Deep Learning,”** arXiv v1 submitted 2026-07-11; [abstract](https://arxiv.org/abs/2607.10491), [HTML](https://arxiv.org/html/2607.10491), [PDF](https://arxiv.org/pdf/2607.10491) (checked 2026-08-19) | The paper maps retrieved chunks to evidence vectors/Dirichlet masses over singleton claims plus the frame, applies a conflict-transfer parameter `lambda`, retains unresolved conflict as frame uncertainty, and routes direct/conflict-aware/abstention outputs. Its reported default is `lambda=0.6`, with uncertainty thresholds `.35/.65`, top-`k=5`, and three seeds. | ArXiv v1 is a preprint, not independently verified peer-reviewed acceptance. The paper’s reported baselines/results are not evidence about Pattern Map and were not reproduced. |
| E02 | Glenn Shafer, **A Mathematical Theory of Evidence**, Princeton University Press / JSTOR, 1976; [official JSTOR record](https://www.jstor.org/stable/j.ctv10vm1qb) (checked 2026-08-19) | The foundational framework defines belief functions over a frame and treats pooling as combining evidence from distinct bodies. | This is foundational theory, not a claim about retrieved text, language models, or the Pattern Map corpus. “Distinct” is not a certificate that any two passages are distinct. |
| E03 | Glenn Shafer, **“Dempster’s Rule of Combination,”** International Journal of Approximate Reasoning 79, 26–40, 2016; [publisher record](https://www.sciencedirect.com/science/article/pii/S0888613X15001978), DOI `10.1016/j.ijar.2015.12.009` (published Dec 2016; checked 2026-08-19) | The abstract describes Dempster’s rule as intuitively pooling belief functions based on distinct or independent sources and discusses evidential independence. | It supports an assumption boundary, not a universal requirement for every alternative rule or every custom conflict operator. |
| E04 | Glenn Shafer, **“The Handling of Dependent Evidence,”** International Journal of Approximate Reasoning 79, 41–44, 2016; [publisher record](https://www.sciencedirect.com/science/article/pii/S0888613X16300718), DOI `10.1016/j.ijar.2016.05.003` (published Dec 2016; checked 2026-08-19) | The abstract says Dempster’s rule is appropriate only when combining independent items of evidence and discusses how to handle dependence. | It does not tell us which dependence model is correct for passages; it blocks silent assumption, not the use of all fusion. |
| E05 | Thierry Denœux, **“Conjunctive and Disjunctive Combination of Belief Functions Induced by Nondistinct Bodies of Evidence,”** Artificial Intelligence 172, 234–264, 2008; [publisher record](https://www.sciencedirect.com/science/article/pii/S0004370207001063), DOI `10.1016/j.artint.2007.05.008` (published Feb 2008; checked 2026-08-19) | The abstract explicitly contrasts Dempster’s distinct-body assumption with cautious combination for reliable, possibly overlapping evidence and bold disjunctive combination for possibly overlapping/unreliable evidence. | It provides alternatives and assumptions, not a recommendation that cautious or disjunctive fusion is automatically right for retrieved passages. |
| E06 | Fabio Cattaneo, **“Belief Functions Combination without Assumption of Independence,”** International Journal of Approximate Reasoning 52(3), 299–315, 2011; [publisher record](https://www.sciencedirect.com/science/article/pii/S0888613X10001490), DOI `10.1016/j.ijar.2010.10.006` (published Mar 2011; checked 2026-08-19) | The abstract develops cautious rules for combination when no assumption about source dependence is available. | “No independence assumption” still requires choosing and interpreting a rule; it does not validate the EvidentialRAG interpolation or the Pattern Map endpoint. |
| E07 | Z. Su et al., **“Handling of Dependence in Dempster–Shafer Theory,”** International Journal of Intelligent Systems 30, 441–467, first published 2014-11-25 / issue 2015; [publisher record](https://onlinelibrary.wiley.com/doi/abs/10.1002/int.21695), DOI `10.1002/int.21695` (checked 2026-08-19) | The abstract notes that independence is often unrealistic and develops inner/outer dependence representations and discounting/aggregation treatment. | The paper supports explicit dependence modeling as a research issue; it does not quantify dependence in EvidentialRAG or Pattern Map. |
| E08 | Ronald R. Yager, **“On the Dempster–Shafer Framework and New Combination Rules,”** Information Sciences 41, 93–137, 1987; [publisher record](https://www.sciencedirect.com/science/article/abs/pii/0020025587900077), DOI `10.1016/0020-0255(87)90007-7` (published Mar 1987; checked 2026-08-19) | The abstract discusses conflict, normalization concerns, and alternative combination rules including witness credibility. | It does not establish that the EvidentialRAG `lambda` interpolation is a standard or validated rule. |
| E09 | Lotfi A. Zadeh, **“A Simple View of the Dempster–Shafer Theory of Evidence and Its Implication for the Rule of Combination,”** AI Magazine 7(2), 85–90, Summer 1986; [publisher record](https://onlinelibrary.wiley.com/doi/abs/10.1609/aimag.v7i2.542) (published Summer 1986; checked 2026-08-19) | The article is an early critique/discussion of conflict and combination behavior in the D-S framework. | Historical theory context only; it is not a test of retrieved passage dependence. |

The existing Round 1 ledger was also reconciled conceptually. Its records on
PROV-O, claim provenance, copying/dependence, conflict-aware RAG, source
attribution, evidence-utilization diagnostics, metadata/authority bias, and
complexity-matched RAG baselines all remain relevant. Round 2 does not claim
an exhaustive literature review or a “first” result.

## Dempster–Shafer and EvidentialRAG adversarial audit

### What the checked EvidentialRAG source actually claims

**[SOURCE]** In the checked arXiv v1 HTML, EvidentialRAG represents a candidate
claim frame `Theta={A_q, not-A_q}` and converts each retrieved chunk's
evaluator evidence vector into a Dirichlet/evidence mass. The mass has
singleton support and full-frame ignorance. For two masses it computes a
conflict term `K`, non-conflicting singleton terms `n_j`, and full-frame mass
`h`, then uses a parameterized transfer:

```text
m_ab(Theta) = h + lambda*K
m_ab(j)     = (1 - h - lambda*K) * n_j / sum(n)
```

It iterates that pairwise operator over retrieved chunks and interprets frame
mass as epistemic uncertainty. `lambda=1` is described as Yager-style conflict
transfer to the frame; `lambda=0` redistributes over non-conflicting singleton
support; `lambda=.6` is the reported default. The paper routes below `.35`,
between `.35` and `.65`, or above `.65` to direct, conflict-aware, or abstaining
behavior, respectively.

**[SOURCE]** The same HTML also describes lexical/semantic claim normalization
and alignment: equivalent claim forms are merged, while incompatible claims
remain distinct. That is a claim-alignment operation, not a source-family or
passage-independence certificate. The paper explicitly says equivalent chunks
can increase evidence for the same claim; therefore the duplicate-support
counterexample below remains a relevant stress case when duplicated or
syndicated chunks reach the fusion stage.

**[SOURCE]** Its reported comparison keeps retrieval corpus, generator,
context, and generation length matched, uses top-`k=5`, and reports several
`lambda` values. That is a direct description of one preprint's experiment,
not an independent validation of the rule. The checked limitations discuss
evaluator reliability, human auditing, benchmark representativeness, and
future integration of source credibility/provenance.

**[UNKNOWN]** In the checked v1 HTML, no source-family variable, passage-level
duplicate or syndication control, overlap/correlation estimate, dependence
discount, independence test, or rule-selection protocol for related retrieved
passages is specified. I found no statement that the retrieved passages are
independent.
This is a bounded statement about the version checked, not proof that no
unlinked supplement, code, later version, or author discussion exists.

**[INFERENCE]** The use of a D-S-inspired mass and conflict transfer does not
by itself make the input bodies distinct, and a top-`k` retrieval list is a
ranking, not a certificate of independent evidence. The preprint's future-work
statement about source credibility/provenance is consistent with this gap but
does not establish that the authors intended an independence assumption.

### Why dependence matters, without declaring a formal error

**[SOURCE]** Shafer's foundational and later papers make distinct/independent
evidence a condition or interpretive basis for standard Dempster pooling.
Denœux, Cattaneo, and Su et al. show that overlapping/dependent bodies require
different rules or explicit dependence treatment. These sources establish that
dependence is a known methodological branch, not that one branch is universally
correct.

**[DERIVATION 1 — duplicate-support counterexample]** Take a two-singleton
frame and the valid mass `m=(A:.90, B:0, Theta:.10)`. Applying the checked
EvidentialRAG pair operator to two identical masses gives no cross-singleton
conflict (`K=0`), full-frame mass `h=.01`, and singleton mass `m(A)=.99`.
Three identical copies give `.999` on `A` and `.001` on `Theta`; five give
`.99999` on `A` and `.00001` on `Theta` (up to decimal display). This follows
algebraically because repeated same-direction mass multiplies residual
ignorance away.

| Retrieved list | `m(A)` | `m(Theta)` | Interpretation if all rows are one copied passage |
| --- | ---: | ---: | --- |
| one copy | 0.90000 | 0.10000 | Starting mass |
| two identical copies | 0.99000 | 0.01000 | Apparent confidence increases without a new source |
| three identical copies | 0.99900 | 0.00100 | Near-certainty from repetition |
| five identical copies | 0.99999 | 0.00001 | Effectively certain under this toy mass |

This is a threat model, not an accusation. If each passage is genuinely a
distinct, conditionally independent observation, compounding may be intended.
If rows are syndications, duplicated retrieval windows, or common-pipeline
derivations, treating them as separate bodies can overstate support. The
checked EvidentialRAG paper does not provide the receipt needed to decide
which case applies.

**[DERIVATION 2 — fold-order counterexample]** Use three valid masses, each
representable by the paper's evidence-to-Dirichlet construction:

```text
m_A = (A:.90, B:0,   Theta:.10)
m_B = (A:0,   B:.90, Theta:.10)
m_C = (A:.50, B:0,   Theta:.50)
```

With the paper's default `lambda=.6`, sequentially folding the same multiset
in two orders gives:

| Fold order | Final `m(A)` | Final `m(B)` | Final `m(Theta)` | Router band using `.35/.65` |
| --- | ---: | ---: | ---: | --- |
| `m_A → m_B → m_C` | 0.540256 | 0.136144 | 0.323600 | direct (`u<.35`) |
| `m_A → m_C → m_B` | 0.327071 | 0.154929 | 0.518000 | conflict-aware (`.35≤u<.65`) |

The multiset is unchanged; only fold order changes. The calculation is
reproducible from the displayed operator and is not a provider/model run.
It shows that the custom pairwise transfer is not safe to describe as
order-invariant or associative without an explicit proof. It does **not** show
that order dependence is a bug: ranked retrieval may be an intended input
semantics. It does require a ranking-preservation receipt, order-permutation
sensitivity report, and a clear statement that the router is rank-dependent if
the design is retained.

**[DERIVATION]** Even when `lambda=1` resembles one-step Yager-style full
conflict transfer, pairwise sequential transfer can differ from an n-ary
combination because conflict transferred to `Theta` participates in later
combinations. At `lambda=0`, the custom normalization also should not be
silently equated with every standard normalized-Dempster implementation.
Comparisons must specify the exact operator, arity, normalization, and fold
order.

### Alternative interpretations and combination rules

No combination rule can be chosen from the word “Dempster–Shafer” alone. The
following alternatives are technically live and require different assumptions:

| Candidate interpretation | What it preserves or assumes | Adversarial concern | Minimum future receipt |
| --- | --- | --- | --- |
| Standard normalized Dempster | Pools distinct/independent bodies and normalizes non-total conflict | Repeated/syndicated passages can become overconfident; conflict normalization can hide disagreement | Source-family/duplicate policy, independence rationale, conflict rate, and predeclared failure behavior |
| Unnormalized conjunctive/TBM-style combination | Retains empty-set conflict and is associative/commutative before a later decision rule | Conflict mass may be mistaken for uncertainty or discarded at routing time | Exact frame/open-world semantics and a locked conflict-to-action mapping |
| Yager-style transfer | Sends total conflict to the frame/ignorance | Sequential transfer is not automatically equivalent to one-shot n-ary transfer; high ignorance can be threshold-fragile | Compare n-ary and ranked sequential forms under order permutations |
| Cautious combination (Denœux) | Designed for possibly overlapping reliable evidence; idempotence helps against duplicate inflation | Requires a discount/decomposition interpretation and may be conservative | Certified overlap/dependence fixtures and rule-specific calibration |
| No-independence cautious rules (Cattaneo) | Makes no independence assumption | “No assumption” is not “no dependence”; rule choice still changes the answer | Predeclare rule, target estimand, and dependency stress grid |
| Dependence discounting/aggregation (Su et al.) | Models inner/outer dependence or discounts aggregate evidence | Requires a dependence estimate or declared bounds; unavailable in current lead | Family/overlap metadata, sensitivity bounds, and uncertainty propagation |
| EvidentialRAG custom `lambda` interpolation | Retains a tunable amount of conflict in the frame and routes by uncertainty | `lambda`, fold order, retrieval rank, evaluator mass, and duplicate count jointly define behavior | Lock `lambda`, exact operator, arity, order policy, duplicate policy, and calibration before comparison |

**[INFERENCE]** The existence of these alternatives does not make the custom
operator formally wrong. It makes an unqualified claim that it is “the” D-S
solution, or that its outputs have an independence-backed evidential meaning,
unsupported.

### Novelty boundary for the lead

**[SOURCE]** The checked primary records cover foundational belief functions,
standard Dempster pooling, dependence handling, nondistinct-body rules,
conflict alternatives, and a current conflict-aware RAG preprint.

**[INFERENCE]** The broad novelty hypothesis “Pattern Map introduces an
evidence/discrimination layer using conflict-aware D-S fusion” should be
**REJECTED**. The narrowed claim “a particular relation-cue diagnostic could
compare a rule-only model condition to an oracle/stipulated relation condition”
remains a separate, conditional design question; it is not made novel by
EvidentialRAG and does not need a D-S component.

**[UNKNOWN]** This pass did not conduct a systematic exhaustive search of every
2026 preprint, source code repository, or unpublished supplement. The safe
wording is “adjacent prior art identified; no broad novelty basis in the checked
records,” not “first” or “no one has done this.”

### If a future D-S comparison is separately authorized

It must remain a future comparator, not a locked F0/F1/F2 arm, until all of the
following are fixed in a versioned protocol:

1. source-family, duplicate, near-duplicate, syndication, and common-pipeline
   labels;
2. whether relation labels are stipulated, inferred, or human-corrected;
3. exact mass construction, evaluator model, frame, discounting, `lambda`,
   normalization, open/closed-world semantics, and n-ary versus pairwise fold;
4. ranking and order policy, including random/permuted-order sensitivity;
5. dependence-aware and non-D-S baselines matched for retrieval/context/token
   budget;
6. conflict, uncertainty, calibration, abstention, and action-routing
   endpoints with no post-hoc rule selection; and
7. duplicate inflation, conflicting-source, authority/date/jurisdiction, and
   missing/unknown-origin fixtures.

No such comparison was run or added in Round 2.

## F0/F1/F2 adversarial methods review

### Estimand and construct

**[SOURCE]** The protocol defines F0 as the ordinary rule-only baseline, F1 as
the same rule with `NONE` relation slots, and F2 as the same rule with visible
benchmark-stipulated `DPND`/`INDP`/`UNKN` values. The primary contrast is
F2-versus-F1 on fixed `A=300` bundles; F0, structure, style, order, confidence,
claim state, and optional model slices are descriptive. The protocol explicitly
says `INDP` is stipulated, not discovered.

**[INFERENCE]** This is a legitimate narrow condition contrast, but it is an
oracle-cue test. A positive result can mean the model responds to visible
relation codes, code identity, metadata salience, prompt position, or a useful
rule cue. It cannot identify internal causal use or real provenance reasoning.
Round 1's phrase “supplied-field condition effect” remains the safe estimand.

### `FC_cons`: valid safety composite versus corroboration claim

**[SOURCE]** The protocol and `analysis.py` define:

```text
FC_obs  = valid AND origin_count_supporting >= 2
          AND certainty in {none, single, unknown}
FC_cons = NOT valid OR FC_obs
FC_lib  = valid AND FC_obs       # sensitivity
```

`FC_cons` therefore assigns every invalid output a risk value of one. Its code
does not use `claim_state` or selected `evidence_ids` to decide the primary
event.

**[DERIVATION]** Two conditions can have the same `FC_cons` delta for different
reasons: F2 can reduce invalid JSON while leaving valid overcount unchanged;
it can reduce valid overcount with identical invalidity; or both components can
move in opposite directions. A single composite delta cannot identify which
mechanism occurred.

**[RECOMMENDATION / DECISION]** Retain the all-assigned event only as a
conservative asserted-count-risk endpoint, with paired invalid-rate counts,
invalid reason decomposition, valid-only overcount, and a predeclared narrative
gate. Add contradictory count/stance/evidence fixtures before any lock. Do not
call it false corroboration, semantic origin accounting, or typed-cue value
without a stronger frozen coherence construct.

### VOR: threshold safety guardrail versus exact accounting

**[SOURCE]** `VOR` passes only when an output is valid, count is at least two,
and selected supporting evidence covers at least two gold support origins in
the fixed `M` set (`|M|=75`). It does not require exact count, exact selected
origin set, coherent stance, or absence of wrong-origin credit. Invalid outputs
are coded zero.

**[DERIVATION]** A policy that always emits `2` on every multiple-origin row can
pass the threshold when two supporting origins are selected, even if the gold
count is three or more. That policy may preserve a conservative recall floor;
it does not show exact origin counting.

**[INFERENCE]** Keep VOR as a guardrail and report count error, support-origin
set exact match, precision/recall, and count/stance/evidence coherence as
descriptive panels. Use “selected stipulated support-origin coverage” rather
than “origin assignment accuracy.” A future stress corpus with wrong-origin
distractors is needed for the stronger construct and should stay outside the
first confirmatory family.

### Denominators, interval/power, and invalid dependence

**[SOURCE]** Confirmatory scoring fails closed unless the ordered manifest has
exactly `A=300` primary rows and a fixed `M=75` multiple-origin safety subset;
invalid outputs remain in the assigned denominator. The protocol proposes
paired McNemar/binomial analysis, paired risk difference, bootstrap intervals,
and a one-sided safety comparison for VOR. `N=300` and `|M|=75` are planning
inputs, not established adequacy.

**[SOURCE]** The offline planning scaffold applies invalid coding independently
to F1 and F2 and does not model condition-specific invalid rates or invalid
correlation. The final interval and coverage disposition remains open.

**[DERIVATION]** In paired conditions, invalid outputs can be correlated because
the same bundle, prompt, context, or model failure appears in both arms. An
independent-invalid simulation can misstate discordance, paired power, and the
variance of the contrast. For VOR, `|M|=75` can make a one-sided interval too
wide for a useful gate even when the point estimate looks favorable.

**[RECOMMENDATION / DECISION]** Revise the planning lock: select the exact
interval method, simulate the final paired decision over invalid correlation,
condition-specific invalidity, baseline, discordance, and effect grids, and
report type-I error, power, coverage, and gate probability at `N=300`,
`|M|=75`. Do not call current scaffold output power evidence.

### Resource parity and prompt parity

**[SOURCE]** The generator's local parity receipt uses a deterministic regex
surrogate. The config has `model_id=UNSELECTED` and no tokenizer revision; the
actual tokenizer/chat-template path is not present. F1/F2 are byte-matched in
the local construction but model-token parity is unresolved.

**[INFERENCE]** Relation-code tokenization, chat-template boundaries, truncation,
and output caps can change the treatment effect. Byte parity is necessary but
not sufficient for matched model resources.

**[RECOMMENDATION / DECISION]** Retain the selected-model tokenizer/chat-template
receipt as a hard gate. Before an authorized run, freeze checkpoint, tokenizer
revision, chat template, rendered prompt bytes, token counts, truncation,
output cap, order, hashes, and fail-closed mismatch behavior for every paired
F1/F2 input.

### Coherence fixtures and parser behavior

**[SOURCE]** The strict parser rejects malformed records without repair/retry,
but the existing tests do not include the full contradictory semantic matrix.
The scorer ignores `claim_state` and selected evidence for `FC_cons` and uses
only a threshold for VOR.

**[RECOMMENDATION / DECISION]** Add offline fixtures before lock for at least:

- valid `origin_count_supporting=4` with `claim_state=refuted`;
- valid count `0` with `claim_state=supported`;
- valid count/evidence IDs that disagree with the stipulated support set;
- valid count `2` with confidence `unknown` on `UNKN`;
- invalid JSON/type/duplicate-key records separated by parser reason;
- F1/F2 pairs where only invalidity changes, only valid overcount changes, and
  both components change.

Choose and record whether these are primary field-risk values or secondary
coherence flags. A fixture is not a model result; it is a construct contract.

### Leakage, metadata salience, and semantic audit

**[SOURCE]** The protocol lists codebook permutation, relation position/order,
field-only and metadata-only controls, style/length/domain crossings,
dependent-versus-distinct overlap controls, relation noise, split blocking, and
an independent semantic/stance/transformation audit. The readiness memo and
diagnostics say several remain unresolved; the smoke classifier is not a full
blocked held-out-family clearance test.

**[INFERENCE]** Because F2 exposes four-letter codes in a fixed metadata field,
the model can count code identity or use position/formatting without reading
report content. A positive effect that survives report masking or follows a
permuted token is not evidence of semantic relation use. A corpus template or
structure classifier can also leak the latent stratum.

**[RECOMMENDATION / DECISION]** Keep P0 leakage and semantic gates. Require a
frozen held-out-family character/token classifier and ceiling, codebook
permutation, metadata-only, field-only, position/order swap, low-overlap/high-
overlap, noise, and independent semantic/stance/transformation receipts. Any
failed control quarantines or narrows the claim; listing a control is not
passing it.

### Naming and execution readiness

**[SOURCE]** Round 1's prior-art ledger rejects generic provenance/attribution/
conflict-fusion novelty. The prospectus still risks “benchmark,” “metadata,”
and “origin accounting” being read more broadly than the oracle/threshold
diagnostic. The charter forbids execution and the package has no selected
model, budget, provider adapter, actual primary manifest/output, or owner
authorization.

**[DECISION]** Revise public research language to “frozen-model diagnostic,”
“stipulated origin-relation cue,” “conservative asserted-count risk,” and
“selected stipulated support-origin coverage.” Retain the thought-piece's
broader “discrimination layer” as historical/conceptual framing only. Mark T1
descriptive and rights-gated, and keep all future human/action/memory/noisy-
relation studies separate.

## Round 2 decisions in brief

The companion matrix is the authoritative row-by-row disposition. The short
form is:

- **REJECT** broad mechanism/layer novelty and any claim that EvidentialRAG
  establishes independent retrieval evidence.
- **DEFER** the D-S/EvidentialRAG lead as an unverified adjacent comparator;
  do not add it to F0/F1/F2 or imply its rule is validated.
- **REVISE** the `FC_cons` construct wording, invalidity interpretation gate,
  coherence fixtures, final interval/power plan, and scientific title/abstract.
- **ACCEPT as retained gates** actual tokenizer/chat-template parity, leakage /
  semantic audit, fixed denominators, T1 firewall, one-model qualifiers,
  source-status reconciliation, and release-grade RFC/schema checks.
- **DEFER** future relation-object, wrong-origin stress corpus, human correction,
  action/value-of-information, memory/security, terminology, and reusable-
  benchmark work until a separately authorized protocol.
- **NO RUN:** the package remains `COHERENT_PROTOCOL_NOT_EXECUTION_READY`.

## Integration-safe wording

Use this paragraph in a convergence or parent handoff record:

> The research branch is a pre-run, frozen-model diagnostic proposal. Its only
> residual question is whether supplied, benchmark-stipulated origin-relation
> codes alter a model's conservative asserted-count risk beyond the same
> explicit counting rule. The package does not infer provenance or establish
> real-world independence, truth, human benefit, or framework validity. The
> Dempster–Shafer/EvidentialRAG lead is adjacent, unverified comparator prior
> art: retrieved-passage dependence, duplicate inflation, and fold-order
> sensitivity must be specified and tested before any future fusion comparison,
> and the lead is not part of the locked F0/F1/F2 study. Before any authorized
> pilot, the team must freeze and validate the `|M|=75` safety interval,
> selected-model tokenizer/chat-template parity, blocked leakage and semantic
> audits, invalid-output interpretation, and count/stance/evidence coherence.
> A null, harmful, threshold-only, invalidity-driven, direct-code, order-
> fragile, or noise-fragile result remains a first-class outcome.

## Local validation and non-claims

Validation for this lane is limited to file hygiene and the existing offline
implementation checks. It must not be read as empirical validation:

```text
PYTHONDONTWRITEBYTECODE=1 /Users/gpt/Documents/Codex/projects/Signal-Foundry/.venv/bin/python -m pytest -q tests/test_origin_accounting.py
15 passed in 3.29s; offline only

git diff --check
PASS (no tracked diff errors; the two lane files were untracked at check time)
```

The worktree-local `.venv/bin/python` path was absent, so the first attempted
command exited `127` before running tests; the existing repository environment
was used without editing it. No test here validates a model, source
independence, evidence-fusion calibration, power, interval coverage, or
novelty.

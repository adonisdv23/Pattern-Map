# Current primary-source opportunity scan — 2026-08-30

Status: **TARGETED, NON-EXHAUSTIVE WAYFINDING / CLAIM-CONSTRAINING QA / NO
STUDY, MODEL, PROVIDER, DATASET, PARTICIPANT, OR RESULT**

Reviewed starting checkpoint: `d05aca58910b4463e5afb69b10558b662a446278` on
`codex/pattern-map-v16-loop-research`.

## Purpose and scope

This is the supplemental current-source lane for the v16 opportunity-expansion
cycle. It follows the existing
`qa/research/CURRENT_ADJACENT_SOURCE_VERIFICATION_2026-08-30.md` and the
current source route, which already cover context engineering, evolving
playbooks, recurrence versus support, agent probes, claim/evidence traces,
execution-trace visualization, evidence interfaces, appropriate reliance,
over-searching, budget-constrained search, sufficiency/gap control,
deep-research evaluation, retriever/agent disentanglement, and report-level
logic.

The supplemental scan therefore looked for adjacent primary or official work
that could still change the opportunity map around:

- perspective and counterevidence discovery;
- long-context selection and temporal awareness;
- agent memory, memory management, and outcome-driven updates;
- provenance and workflow receipts; and
- cost-bounded iterative verification and stopping.

Evidence dependence/repeated-source structure and human control/appropriate
reliance remain in scope as cross-cutting constraints, but are not duplicated
as new candidate rows here: the current QA already covers GroupQA,
FACTS&EVIDENCE, and the two CHI 2025 appropriate-reliance records. The new
records below are retained only where they add a distinct operational seam or
materially narrow a claim beyond that existing coverage.

The scan is a targeted wayfinding pass, not a systematic review, exhaustive
search, full-paper risk-of-bias assessment, replication, novelty clearance, or
recommendation of a first paper. Linked ACL Anthology records, arXiv author
records, and the authors' reported abstracts were opened read-only on
2026-08-30 (America/New_York). Conference status is taken from the official
proceedings record; arXiv-only records remain preprints even when their
abstract reports experiments. Findings below are attributed to the authors'
reported setting and are not treated as evidence that Pattern Map works.

No provider or model was called, no corpus or external dataset was acquired,
no participant or person was contacted, no study was run, and no external
state changed.

## Executive disposition

The scan does not require a thesis change, a sixth-family change, a new
architecture, or a new public artifact. It does produce bounded claim and
agenda constraints:

1. **Any claim of component-level empty space is not defensible.** Perspective
   diversity, counterevidence search, context reduction, temporal memory,
   learned memory operations, provenance capture, and evidence-coverage
   stopping all have direct 2025–2026 primary work. The v16 contribution must
   remain an authored, proportional, human-governed design/governance
   synthesis and testable agenda.
2. **The operational seams are more specific than a generic “look wider and
   remember.”** Current work points to explicit perspective coverage, temporal
   validity, source/evidence role separation, memory write/update/retrieval
   decisions, process provenance, and evidence-based stopping. These are
   useful future design questions, not claims that v16 has already supplied or
   validated those mechanisms.
3. **The research agenda should keep mechanisms separate before an omnibus
   playbook interpretation.** Results are task- and representation-dependent:
   memory is not uniformly useful, long context can remain competitive, source
   diversity can change perspective without improving correctness, and search
   can be wasteful or harmful. The existing matched-resource, comparator,
   guardrail, and unfavorable-result boundaries are therefore retained and
   strengthened rather than replaced.
4. **Publication framing should be narrower and clearer.** A source may show
   that a component is active prior art or that a bounded benchmark exposes a
   failure mode. It does not establish a unified Discrimination Layer,
   independent corroboration, truth, human decision quality, transfer, or
   effectiveness of the v16 arrangement.

## Candidate records

### OPP-01 — Open-World Evaluation for Retrieving Diverse Perspectives

Source: [Chen and Choi, “Open-World Evaluation for Retrieving Diverse Perspectives”](https://aclanthology.org/2025.naacl-long.431/).

**Verified bibliographic and status facts.** The ACL Anthology record identifies
Hung-Ting Chen and Eunsol Choi as authors and the work as a NAACL 2025 long
paper in the official proceedings (April 2025, ACL Anthology ID
`2025.naacl-long.431`).

**Authors' reported setting and findings.** The abstract describes BERDS, a
benchmark for subjective questions with multiple perspectives sourced from
survey questions and debate websites. It evaluates retrievers paired with
Wikipedia, a web snapshot, and on-the-fly retrieved pages. The authors report
that existing retrievers covered all listed perspectives on only 33.74% of
examples, and they study query expansion, diversity-focused reranking, and
retriever sycophancy. Their evaluator is language-model-based and asks whether
a retrieved document contains a perspective rather than relying only on
reference-string matching.

**Inference for Pattern Map.** This is direct evidence that missing-perspective
discovery and perspective coverage are an active, operational retrieval
problem. F1/F5 future work should distinguish “a different perspective was
retrieved” from “the perspective is supported, relevant, permitted, or true.”
An expected-perspective key, false-gap calls, and coverage under query
expansion or reranking are more precise opportunities than a generic promise
to diversify sources. The result also supports treating retriever sycophancy
as a failure mode when a system follows the framing of a query instead of
searching for substantive alternatives.

**What this source does not establish.** BERDS is a benchmark for subjective
questions and its perspective evaluator is not a universal truth or support
criterion. The 33.74% figure is not a prevalence estimate for all search or
agent systems. The paper does not test the v16 six-family arrangement, human
decision usefulness, provenance independence, or whether more perspective
coverage improves a decision.

**Disposition.** **Accepted with revision** as a source-route addition and a
claim constraint for C16-008/C16-016/C16-018; no new framework mechanism is
adopted.

### OPP-02 — FIRE: Fact-checking with Iterative Retrieval and Verification

Source: [Xie et al., “FIRE: Fact-checking with Iterative Retrieval and Verification”](https://aclanthology.org/2025.findings-naacl.158/).

**Verified bibliographic and status facts.** The ACL Anthology record lists
Zhuohan Xie, Rui Xing, Yuxia Wang, Jiahui Geng, Hasan Iqbal, Dhruv Sahnan,
Iryna Gurevych, and Preslav Nakov as authors. It identifies a Findings of
NAACL 2025 conference publication (April 2025, ID
`2025.findings-naacl.158`).

**Authors' reported setting and findings.** The authors describe long-form
fact-checking decomposed into atomic claims. FIRE iterates between evidence
retrieval and claim verification and decides whether to answer or issue a
subsequent search query using a unified confidence mechanism. The abstract
reports slightly better performance than comparison frameworks, with average
LLM costs reduced 7.6-fold and search costs reduced 16.5-fold in the reported
fact-checking setting.

**Inference for Pattern Map.** Counterevidence acquisition and stopping can be
one coupled loop: the next query should be justified by the current claim
state, and a stop should be tied to unresolved support/refutation rather than
to a fixed number of documents. This suggests a concrete future mechanism
question for F2/F5 and the cost boundary: does an explicit “support,
refute, or still unresolved” state reduce unnecessary acquisition while
preserving holds and abstentions? It also reinforces that claim
decomposition, retrieval, verification, and stopping should be separately
observable in a receipt.

**What this source does not establish.** The reported cost ratios are authors'
results for the paper's fact-checking tasks and comparison systems, not a
general cost guarantee. Confidence-driven iteration can fail when the
confidence signal is miscalibrated or when the search corpus omits relevant
evidence. FIRE does not establish that a v16 playbook improves decisions,
finds all counterevidence, or transfers outside long-form fact-checking.

**Disposition.** **Accepted with revision** as support for keeping iterative
verification, counterevidence, and cost/stopping as distinct future questions;
do not import FIRE's mechanism or reported numbers into v16 claims.

### OPP-03 — Context Length Alone Hurts LLM Performance Despite Perfect Retrieval

Source: [Du et al., “Context Length Alone Hurts LLM Performance Despite Perfect Retrieval”](https://aclanthology.org/2025.findings-emnlp.1264/).

**Verified bibliographic and status facts.** The ACL Anthology record lists
Yufeng Du, Minyang Tian, Srikanth Ronanki, Subendhu Rongali, Sravan Babu
Bodapati, Aram Galstyan, Azton Wells, Roy Schwartz, Eliu A. Huerta, and Hao
Peng as authors. It identifies a Findings of EMNLP 2025 publication
(November 2025, ID `2025.findings-emnlp.1264`).

**Authors' reported setting and findings.** The abstract reports experiments
across five open- and closed-source LLMs on mathematics, question answering,
and coding. Even with relevant information perfectly retrieved, reported
performance degraded by 13.9%–85% as input length increased within the claimed
context limits; the authors also report degradation when irrelevant tokens were
replaced by whitespace or masked. They report up to a 4% GPT-4o improvement on
RULER from a recitation-based long-to-short-context mitigation.

**Inference for Pattern Map.** Upstream retrieval quality is not the whole
information environment. F1/F5 selection, compression, comparison, and
context-size accounting should be treated as separate from evidence
availability, and the research route should measure both retrieval success and
downstream use. A “more context” or “more sources” intervention can create
burden even when the retrieved material is relevant. This supports explicit
context budgets and a no-monotone-benefit assumption.

**What this source does not establish.** The degradation range is bound to the
reported tasks, models, context construction, and metrics. The recitation
mitigation is not a v16 procedure or a general solution. The paper does not
show that a six-family workflow, source receipt, or human review improves
decision quality, and it does not turn context compression into a universal
requirement.

**Disposition.** **Accepted** as a claim constraint for C16-002/C16-014 and
as a reason to preserve context burden and harm guardrails; no canonical
artifact change beyond the optional route is warranted.

### OPP-04 — EvolveBench: Temporal Awareness on Evolving Knowledge

Source: [Zhu et al., “EvolveBench: A Comprehensive Benchmark for Assessing Temporal Awareness in LLMs on Evolving Knowledge”](https://aclanthology.org/2025.acl-long.788/).

**Verified bibliographic and status facts.** The ACL Anthology record lists
Zhiyuan Zhu, Yusheng Liao, Zhe Chen, Yuhao Wang, Yunfeng Guan, Yanfeng Wang,
and Yu Wang as authors and identifies an ACL 2025 long paper in the official
proceedings (July 2025, ID `2025.acl-long.788`).

**Authors' reported setting and findings.** EvolveBench evaluates five
temporal-competence dimensions: cognition, awareness of temporal misalignment,
trustworthiness around invalid timestamps, understanding, and reasoning. The
abstract reports evaluation of 15 LLMs; GPT-4o had the highest average exact
match score of 79.36, while the authors report that all models still struggled
with temporally misaligned context.

**Inference for Pattern Map.** F3 velocity and F4 absence/memory need a
temporal validity seam, not only timestamps attached after retrieval. A future
test should distinguish current, stale, future-invalid, and temporally
ambiguous evidence and measure appropriate refusal or provisional handling.
This is a concrete way to make “motion,” “memory,” and “what should be here
now” inspectable without equating currency with truth.

**What this source does not establish.** EvolveBench is a benchmark and the
reported exact-match values do not generalize to all evolving knowledge or
agent workflows. Temporal alignment is not the same as provenance, source
authority, or independent support. The paper does not validate v16's memory
contract or show a benefit from any six-family intervention.

**Disposition.** **Accepted with revision** as a source-route addition and a
future temporal-validity constraint for C16-006/C16-007/C16-014.

### OPP-05 — TReMu: Temporal Reasoning in Multi-Session Dialogues

Source: [Ge et al., “TReMu: Towards Neuro-Symbolic Temporal Reasoning for LLM-Agents with Memory in Multi-Session Dialogues”](https://aclanthology.org/2025.findings-acl.972/).

**Verified bibliographic and status facts.** The ACL Anthology record lists
Yubin Ge, Salvatore Romeo, Jason Cai, Raphael Shu, Yassine Benajiba, Monica
Sunkara, and Yi Zhang as authors. It identifies a Findings of ACL 2025
conference publication (July 2025, ID `2025.findings-acl.972`).

**Authors' reported setting and findings.** The authors augment LoCoMo
dialogues to create a multi-session temporal-reasoning task. TReMu uses
timeline summaries with inferred dates and has LLMs generate Python code for
temporal calculations. The abstract reports a GPT-4o score increase from
29.83 with standard prompting to 77.67 with the proposed approach in that
task.

**Inference for Pattern Map.** Temporal memory is an operational mechanism
rather than a synonym for “keep history.” A future F4/F6 design could separate
raw observations, inferred event dates, temporal calculations, and any later
outcome update. It also suggests testing whether a temporal representation is
useful only when the task requires temporal operators, rather than making it
universal.

**What this source does not establish.** The benchmark is an augmented
multi-session dialogue task and the reported improvement is task- and
implementation-specific. Inferred dates and generated code can introduce
errors; a temporal summary is not an immutable source record. The paper does
not establish correct provenance, human oversight, transfer to consequential
work, or effectiveness of the v16 learning loop.

**Disposition.** **Accepted with revision** as a bounded temporal-memory
precedent; preserve the existing ordinary-work escape and do not add a
mandatory temporal layer.

### OPP-06 — Hindsight: Structured Agent Memory that Retains, Recalls, and Reflects

Source: [Latimer et al., “Hindsight: Structured Agent Memory that Retains, Recalls, and Reflects”](https://aclanthology.org/2026.acl-demo.27/).

**Verified bibliographic and status facts.** The ACL Anthology record lists
Christopher Latimer, Nicolò Boschi, Andrew Neeser, Chris Bartholomew, Gaurav
Srivastava, Xuan Wang, and Naren Ramakrishnan as authors. It identifies an ACL
2026 system-demonstration paper in Volume 3 (July 2026, ID
`2026.acl-demo.27`).

**Authors' reported setting and findings.** The authors describe a system with
world, experience, observation, and opinion networks and retain, recall, and
reflect operations. The abstract reports vector, keyword, graph, and temporal
filtering, separation of facts and beliefs, and evaluations on LongMemEval and
LoCoMo. It reports 83.6% and 83.2% accuracy with a 20B open-source model and
91.4% LongMemEval accuracy with Gemini-3 Pro in the stated settings.

**Inference for Pattern Map.** Fact-versus-belief separation and explicit
retain/recall/reflect operations expose a missing operational seam in any
memory proposal that stores only a conclusion. F4/F6 records should preserve
the distinction between a source-bound observation, an interpretation or
opinion, and a later review/update. This is a useful implementation precedent
for inspectability and temporal filtering, not a reason to make graph memory
mandatory.

**What this source does not establish.** A system-demonstration result on
LongMemEval and LoCoMo does not establish general memory correctness,
faithfulness of belief updates, or downstream decision quality. The reported
numbers are author-reported, backbone- and benchmark-bound. The paper does
not validate Pattern Map receipts, human authority, cross-domain transfer, or
the claim that separating facts and beliefs improves consequential decisions.

**Disposition.** **Accepted** as a direct prior-art constraint on memory,
belief separation, and traceable updates; do not adopt the system's graph,
database, model, or production claims.

### OPP-07 — LightMem: Lightweight Agent Memory under Bounded Compute

Source: [Zhang et al., “Lightweight LLM Agent Memory with Small Language Models”](https://aclanthology.org/2026.acl-long.588/).

**Verified bibliographic and status facts.** The ACL Anthology record lists
Jiaquan Zhang, Chaoning Zhang, Shuxu Chen, Zhenzhen Huang, Pengcheng Zheng,
Zhicheng Wang, Ping Guo, Fan Mo, Sung-Ho Bae, Jie Zou, Jiwei Wei, and Yang
Yang as authors. It identifies an ACL 2026 long paper in the official
proceedings (July 2026, ID `2026.acl-long.588`).

**Authors' reported setting and findings.** LightMem separates online
retrieval/writing from offline consolidation, organizes short-, mid-, and
long-term memory, and uses a fixed retrieval budget with coarse vector
retrieval followed by semantic-consistency reranking. The abstract reports an
average F1 improvement of about 2.5 over A-MEM on LoCoMo and median latency of
83 ms for retrieval and 581 ms end-to-end in the reported experiments.

**Inference for Pattern Map.** This is a concrete precedent for making memory
cost and timing visible, and for treating “write,” “retrieve,” and
“consolidate” as different operations. Future F4/F6 work should ask which
memory operation is needed and count its budget rather than treating a memory
store as free context. It supports lightweight/moderate/advanced alternatives,
not a single required implementation.

**What this source does not establish.** LoCoMo results and latency numbers
are not general cost or quality guarantees. Semantic-consistency reranking can
preserve a wrong or stale memory, and offline consolidation can erase source
structure. The paper does not show that a v16 receipt or outcome-review loop
improves human decisions or that small-language-model memory is preferable in
all domains.

**Disposition.** **Accepted with revision** as a source-route addition and
bounded-compute constraint for C16-007/C16-011/C16-014; retain the ordinary
route and no-mandatory-architecture boundary.

### OPP-08 — EvoMemBench: Agent Memory Is Not Uniformly Useful

Source: [Wang et al., “EvoMemBench: Benchmarking Agent Memory from a Self-Evolving Perspective”](https://arxiv.org/abs/2605.18421).

**Verified bibliographic and status facts.** The arXiv record identifies Yuyao
Wang, Zhongjian Zhang, Mo Chi, Kaichi Yu, Yuhan Li, Miao Peng, Bing Tong,
Chen Zhang, Yan Zhou, and Jia Li as authors. It was submitted 18 May 2026 and
last revised as version 2 on 15 June 2026. The checked record is an arXiv
preprint; no peer-reviewed venue is inferred from the page.

**Authors' reported setting and findings.** EvoMemBench organizes evaluation
by memory scope (in-episode versus cross-episode) and content (knowledge
oriented versus execution oriented), comparing 15 memory methods with
long-context baselines. The authors report that long-context baselines remain
competitive, memory helps most when the current context is insufficient or
tasks are difficult, and no single memory form works consistently. They report
retrieval methods as strong for knowledge-intensive settings and procedural or
long-term memory as more useful when stored experience matches the task
structure.

**Inference for Pattern Map.** This is an important agenda-ordering constraint:
memory should be tested as a conditional mechanism with task fit and context
sufficiency, not assumed to improve every workflow. A future flagship should
include long-context and ordinary baselines, separate knowledge from
execution/outcome memory, and preserve null, harmful, and non-transfer
outcomes. It supports the existing proportionality rule and rejects any
implicit “more memory is better” ladder.

**What this source does not establish.** This is a preprint and benchmark
report, not a v16 study. Its task axes and method implementations do not
establish a universal taxonomy or transfer to human-governed work. The authors'
reported comparisons do not show that Pattern Map's six families, receipts,
or learning loop improve outcomes.

**Disposition.** **Accepted** as a claim and sequencing constraint for
C16-007/C16-009/C16-014/C16-018; no benchmark or method is selected for future
execution.

### OPP-09 — Memory-R1: Outcome-Driven Memory Operations

Source: [Yan et al., “Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning”](https://arxiv.org/abs/2508.19828).

**Verified bibliographic and status facts.** The arXiv record identifies Sikuan
Yan, Xiufeng Yang, Zuchao Huang, Ercong Nie, Zifeng Ding, Zonggen Li, Xiaowen
Ma, Jinhe Bi, Kristian Kersting, Jeff Z. Pan, Hinrich Schütze, Volker Tresp,
and Yunpu Ma as authors. The record was submitted 27 August 2025 and last
revised as version 5 on 14 January 2026. The checked record is an arXiv
preprint; its page does not establish a peer-reviewed venue.

**Authors' reported setting and findings.** Memory-R1 uses a Memory Manager
with `ADD`, `UPDATE`, `DELETE`, and `NOOP` operations plus an Answer Agent that
selects and reasons over memory entries. The abstract reports outcome-driven
PPO/GRPO training with 152 training question-answer pairs, evaluation on
LoCoMo, MSC, and LongMemEval, and reported generalization across 3B–14B model
scales.

**Inference for Pattern Map.** A learning loop needs an explicit update
decision and a reason to retain, revise, delete, or leave memory unchanged;
“the agent learned” is not an observable state by itself. This source is a
useful prompt for a future F4/F6 ablation over update operations and outcome
keys, while preserving the v16 boundary that a recorded outcome cannot rewrite
the original observation and that human disposition remains required.

**What this source does not establish.** Outcome-driven reinforcement learning
is not proof that a memory update is correct, source-grounded, authorized, or
safe. The result is a preprint report tied to its training pairs, benchmarks,
models, and reward design. It does not establish a human-governed learning
loop, permission handling, or the effectiveness of Pattern Map.

**Disposition.** **Accepted with revision** as a prior-art constraint on
outcome-learning claims; do not select its models, training pairs, or reward
scheme and do not add a result fixture.

### OPP-10 — PROV-AGENT: Unified Provenance for Agentic Workflows

Source: [Souza et al., “PROV-AGENT: Unified Provenance for Tracking AI Agent Interactions in Agentic Workflows”](https://arxiv.org/abs/2508.02866).

**Verified bibliographic and status facts.** The arXiv record identifies Renan
Souza, Amal Gueroudji, Stephen DeWitt, Daniel Rosendo, Tirthankar Ghosal,
Robert Ross, Prasanna Balaprakash, and Rafael Ferreira da Silva as authors. It
was submitted 4 August 2025 and last revised as version 3 on 20 August 2025.
The record's comments state that the paper was accepted for the 2025 IEEE
21st International Conference on e-Science; this scan did not independently
replace that statement with a proceedings landing page.

**Authors' reported setting and findings.** The authors propose a provenance
model extending W3C PROV and using MCP and data observability to connect
prompts, responses, decisions, and workflow context. The abstract reports an
open-source, near-real-time capture system and cross-facility evaluation across
edge, cloud, and HPC environments for provenance queries and agent reliability
analysis.

**Inference for Pattern Map.** Workflow provenance and claim support are
already active technical areas. A v16 receipt can remain a human-readable
record of what influenced a decision, but it should not be framed as a new
provenance mechanism. Future work should distinguish process provenance
(prompts, tool calls, decisions, outcomes) from claim support, source truth,
permission, and human acceptance. This directly supports the existing F2
dimension separation and the two-project boundary.

**What this source does not establish.** Capturing a workflow does not make its
claims true, its actions authorized, or its sources independent. The abstract
does not establish that provenance improves reliability or decision quality,
and the checked record does not validate Pattern Map's receipt schema or
human-authority contract.

**Disposition.** **Accepted** as a strong component-prior-art constraint for
C16-005/C16-012/C16-016/C16-018; no new receipt or trace artifact is warranted.

### OPP-11 — HALT: Verification-Aware Stopping for Retrieval-Augmented Search Agents

Source: [Roh and Han, “HALT: Verification-Aware Stopping for Retrieval-Augmented Search Agents”](https://arxiv.org/abs/2608.02009).

**Verified bibliographic and status facts.** The arXiv record identifies
Daeyoung Roh and Donghee Han as authors. It was submitted 3 August 2026 and
last revised as version 2 on 4 August 2026. The checked record is an arXiv
preprint with a linked code repository; no conference status is inferred.

**Authors' reported setting and findings.** HALT frames stopping as evidence
coverage rather than generator confidence. Given expected hop claims, it stops
when cumulative evidence supports each required claim. The abstract reports
experiments across three multi-hop QA benchmarks, reduced redundant search
while largely preserving exact match, a gap between generated-hop and
gold-supporting-fact settings, and open-corpus pilots that abstain when
coverage cannot be verified.

**Inference for Pattern Map.** A stop condition can be tied to the unresolved
claim/evidence set and an explicit abstention state instead of a fixed depth or
generic confidence. This is a concrete opportunity for future F2/F5 cost
tests: measure redundant acquisition, missed support, false closure, and
abstention separately. It also supports keeping stop as a first-class
operation while acknowledging that evidence coverage itself must be audited.

**What this source does not establish.** The reported setting is multi-hop QA,
with diagnostic gold-hop and open-corpus variants; it is not general deep
research or consequential decision support. A generated hop claim can be
wrong, and “coverage” can be incomplete or biased by the verifier. The
preprint does not establish a universal stopping policy or a Pattern Map
effectiveness result.

**Disposition.** **Accepted with revision** as a current stopping/cost
precedent and a constraint on C16-014/C16-018; do not adopt HALT as the v16
stop rule.

### OPP-12 — Evaluating the Impact of Source Diversity for RAG in Historical Research

Source: [Mahadeshwar et al., “Evaluating the Impact of Source Diversity for RAG in Historical Research”](https://aclanthology.org/2026.lrec-1.53/).

**Verified bibliographic and status facts.** The ACL Anthology record lists
Ruhi Mahadeshwar, Andreas van Cranenburgh, Tommaso Caselli, and Malvina
Nissim as authors. It identifies an LREC 2026 conference paper in the
official proceedings (May 2026, ID `2026.lrec-1.53`; publisher ELRA Language
Resources Association).

**Authors' reported setting and findings.** The authors compile English,
French, and Dutch historical documents about Napoleon Bonaparte and evaluate
three Qwen3 models on ten questions. They combine BERTScore and ROUGE-L with
frame-semantic and syntactic analysis. The abstract reports high semantic
consistency under traditional metrics while frame semantics exposes
perspective shifts; it reports that RAG introduced diversity differently by
language and characterizes RAG as an active perspective transformation in the
stated setting.

**Inference for Pattern Map.** Raw semantic similarity and source counts are
not enough to assess evidence diversity or perspective coverage. A future F5
measurement should preserve language, source role, framing, and comparison-set
dimensions and should not treat a diverse answer as automatically better. This
supports the current ledger's distinction between decision-relevant evidence
diversity and URL/publisher count.

**What this source does not establish.** The study is bounded to ten questions,
one historical subject, three languages, and three Qwen3 models. Perspective
variation is not proof of factual support, independence, or usefulness. The
paper does not test v16, establish a general RAG effect, or justify a selected
corpus, model, or future study design.

**Disposition.** **Accepted** as a claim-constraining source for C16-008,
C16-014, and C16-018; no metric or corpus is adopted.

## Cross-source opportunity map

The candidates converge on five bounded opportunities rather than one new
framework component:

| Opportunity seam | Current primary-source pressure | Warranted v16 implication | Not established |
| --- | --- | --- | --- |
| Missing perspectives and counterevidence | BERDS measures perspective coverage; FIRE iterates retrieval and verification | Define expected perspectives/claim states and false-gap or false-closure outcomes; make the next query and stop reason observable | More perspectives are true, independent, or decision-improving |
| Context and temporal validity | Context-length work reports degradation despite perfect retrieval; EvolveBench and TReMu expose temporal misalignment and multi-session reasoning constraints | Separate evidence availability, context burden, temporal validity, inferred dates, and temporal calculations | Any one compression or temporal-memory method generalizes |
| Memory and outcome learning | Hindsight, LightMem, EvoMemBench, and Memory-R1 expose retain/recall/update/consolidate choices, cost, and task dependence | Keep memory operations typed and source-bound; compare conditional usefulness and preserve no-update/null/harmful outcomes | Memory, reflection, or reinforcement learning makes an agent reliable or human-governed |
| Provenance and receipts | PROV-AGENT joins prompts, responses, decisions, and workflow context | Treat receipts as inspectable process/claim records and keep provenance, support, authority, recurrence, origin, and permission distinct | A receipt or trace is a new mechanism or proves correctness |
| Cost-bounded stopping | FIRE and HALT connect iterative verification to stopping or abstention | Count acquisition/verification/review burden and test coverage-based stopping against fixed depth/confidence routes | Cost savings or preserved benchmark accuracy transfers to consequential research |

## Agenda and claim consequences

The following bounded updates are warranted and are reflected in the optional
source route and new claims-ledger entry C16-018:

- Keep Candidate A a fixed-answer appropriate-reliance/interface question. The
  current sources do not support promoting a receipt, graph, or evidence view
  into a novel mechanism or assuming that more visible evidence improves
  reliance.
- Keep Candidate B provisional. Temporal misalignment, capture failure,
  missing perspective, and evidence coverage are related but not interchangeable
  axes; no source here settles a single missingness taxonomy.
- Preserve mechanism isolation before DL-PLAYBOOK-01: memory, perspective
  retrieval, context reduction, provenance capture, and stopping have separate
  tasks, costs, and failure modes. A favorable result in one bounded task
  cannot be read as evidence for the full six-family playbook.
- Add no provider, model, benchmark, corpus, sample, paper order, or run. The
  source records constrain future design only.

## Controlled dispositions and affected files

| Finding group | Disposition | Affected files | Governing requirement | Integration action |
| --- | --- | --- | --- | --- |
| OPP-01, OPP-02, OPP-04, OPP-05, OPP-07, OPP-09, OPP-11 | **Accepted with revision** | `manuscript/SOURCES_AND_RESEARCH_ROUTE.md`, `docs/CLAIMS_AND_SOURCE_LEDGER_V16.md` | D-042; A11, A16; research may constrain claims but cannot redefine intent | Add concise current links and C16-018; retain task/status limits |
| OPP-03, OPP-06, OPP-08, OPP-10, OPP-12 | **Accepted** | `manuscript/SOURCES_AND_RESEARCH_ROUTE.md`, `docs/CLAIMS_AND_SOURCE_LEDGER_V16.md` | D-017, D-042; matched resources, proportionality, no-results boundary | Record component-specific constraints; do not adopt a method or result |
| Broad systematic search, full-paper synthesis, novelty clearance, or rights/version audit | **Deferred** | Future separately authorized research route | Publication-time recheck; no-study/no-spend boundary | Re-open only if a later owner instruction authorizes it |
| Any claim that these sources prove v16, establish a unified novel mechanism, or select a first study/model/provider/corpus | **Rejected** | No canonical file | Owner intent; A11, A15–A17; authority order | Keep contribution ceiling and unrun status unchanged |

## Verification boundary

This report records public-source metadata and author-reported abstract claims,
not independent reproduction. Before any later-authorized publication, every
link must be reopened, title/version/status rechecked, and moved links replaced
only with primary or official destinations. No statement in this report closes
the publication-time gate, the owner/mentor gate, the physical accessibility
gate, or any future study authorization gate.

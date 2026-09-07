# Opportunity expansion Loop 2 claims-boundary review

**Checkpoint reviewed:** `2b2d1bad8e9b7c954f209f0c9c6e0cfbc9d4815b`
**Review branch:** `codex/pattern-map-v16-loop2-claims-boundary`
**Review date:** 2026-08-30 (America/New_York)
**Review type:** exact-integrated, read-only red-team of the Loop 0/1 additions; this file is the only change made by this review.

## Disposition summary

The integrated checkpoint has **no P0 or P1 finding**. The optional project-use
starter, publication rehearsal kit, and supplemental source route remain
bounded when read with their surrounding status and no-results language. I
found two P2 issues that should be corrected before treating the integration
record as closed, plus two actionable P3 guardrails:

| ID | Severity | Finding | Disposition |
| --- | --- | --- | --- |
| L2-01 | P2 | The integrated Loop 1 ledger gives PUS-01 a hybrid, non-controlled disposition (`Rejected as P1; ... accepted with revision`). | **Accepted with revision** |
| L2-02 | P2 | The explicitly targeted/non-exhaustive source scan uses a categorical sentence about *any* component-level empty space. | **Accepted with revision** |
| L2-03 | P3 | The optional source route is proportionate at its current size, but citation growth would make it a denser literature defense without a new reader need. | **Deferred** |
| L2-04 | P3 | “Passes the removal test” and similar static closure language can be over-read if lifted out of QA context. | **Accepted with revision** |

No paper, provider, model, corpus, dataset, sample, venue, study, experiment,
participant, outreach, or spend is selected or authorized by this review.

## Authority, scope, and review method

I started a new branch from the exact requested integrated checkpoint. Before
inspection I read `AGENTS.md` and the governing records in the required order:

1. `docs/OWNER_INTENT_V16.md`
2. `docs/THESIS_AND_AUDIENCE_CONTRACT_V16.md`
3. `docs/ARTIFACT_BOUNDARIES.md`
4. `docs/SOURCE_AUTHORITY_AND_LINEAGE.md`
5. `docs/V16_ACCEPTANCE_CRITERIA.md`
6. `docs/DECISION_LOG.md`
7. `docs/REVIEW_AND_DISPOSITION_PROTOCOL.md`

I also read `docs/OPPORTUNITY_EXPANSION_LOOPS_V16.md`, the existing adjacent
source verification record, the complete source-scan report, the integrated
project-use/publication artifacts, and each Loop 0/1 advisory report. The
owner-intent checkpoint passed before and after the review:

```text
(cd docs && shasum -a 256 -c OWNER_INTENT_V16.sha256)
OWNER_INTENT_V16.md: OK
```

The review applies the project authority order: owner intent and the approved
v16 handoff govern; primary sources can narrow claims; agent/model reviews are
advisory evidence about document composition only, never scientific evidence.

## Exact integrated surfaces inspected

The commit history and resulting tree were reviewed as a single integrated
surface, not as isolated claims. The relevant sequence is:

| Commit | Integrated addition/challenge | Boundary checked |
| --- | --- | --- |
| `282e865` | Project-use cold-start starter | Optional, internal, repository-local wayfinding; not a portable packet, adoption standard, or transfer result. |
| `f7661ba` | Supplemental primary-source opportunity scan | Targeted/non-exhaustive; author-reported settings and findings; no v16 effectiveness result or chosen study. |
| `481dcb4` | Unpublished public review rehearsal kit | Unsent, unpublished, owner-review candidate; no reader/mentor/public response. |
| `c0a861c` | Public-surface challenge | No public starter pointer, no deployment, no publication authorization. |
| `04082d1` | Project-use claims challenge | Static composition is not transfer/ease evidence; permission and canonical route remain required. |
| `318c362` | Publication-kit challenge | Kit remains subordinate to the human essay/site and separate from project transfer. |
| `2b2d1ba` | Exact integration convergence | Retains the narrow surfaces and records that Loop 2 review is required. |

The inspected files include the project-use page and framework index, the
source route and claims ledger, the supplemental source-scan report, the
publication README/mentor sequence/X drafts/release checklist, their QA and
advisory reports, the root README, owner packet/package map, QA README and
validators, the advisory-disposition ledger, and D-043. No canonical essay,
short version, cover note, abstract, site source, framework template, Echo
preserved/historical subtree, or archive was edited.

## Primary/official source recheck

The twelve records named by the supplemental scan were reopened read-only on
2026-08-30. The check was limited to bibliographic/status facts and the
authors' own abstract or official record; it was not an independent
replication, systematic review, full-paper risk-of-bias assessment, or
verification of Pattern Map claims.

| Scan ID | Official record checked | Status/date check and bounded fact checked |
| --- | --- | --- |
| OPP-01 | [Open-World Evaluation for Retrieving Diverse Perspectives](https://aclanthology.org/2025.naacl-long.431/) | ACL Anthology 2025 proceedings record; the abstract reports perspective-coverage evaluation and retrieval/query-expansion work, with bounded benchmark findings. |
| OPP-02 | [FIRE: Factual Information Retrieval and Evidence verification](https://aclanthology.org/2025.findings-naacl.158/) | ACL Findings of NAACL 2025 record; the abstract reports iterative retrieval/verification and author-reported cost reductions in its setting. |
| OPP-03 | [Context Length Alone Hurts LLM Performance Despite Perfect Retrieval](https://aclanthology.org/2025.findings-emnlp.1264/) | ACL Findings of EMNLP 2025 record; five-model setting and reported degradation despite perfect retrieval match the official abstract. |
| OPP-04 | [EvolveBench: Towards Evolving Temporal Knowledge Understanding in LLMs](https://aclanthology.org/2025.acl-long.788/) | ACL 2025 proceedings record; the abstract reports five temporal-competence dimensions, fifteen LLMs, and temporal-misalignment failures. |
| OPP-05 | [TReMu: A Temporal-Aware Retrieval-Augmented Framework for Long-Term Memory](https://aclanthology.org/2025.findings-acl.972/) | ACL Findings 2025 record; the augmented LoCoMo/timeline setting and reported author-side score change match the abstract. |
| OPP-06 | [Hindsight is 20/20: Building Agent Memory that Learns from Experience](https://aclanthology.org/2026.acl-demo.27/) | ACL 2026 demo record; the four-network retain/recall/reflect description and reported benchmark figures match the official abstract. |
| OPP-07 | [LightMem: Lightweight and Efficient Memory-Augmented Generation](https://aclanthology.org/2026.acl-long.588/) | ACL 2026 proceedings record; modular memory, fixed retrieval budget, reported F1 gain, and latency figures match the abstract. |
| OPP-08 | [EvoMemBench: Benchmarking Memory-Augmented Agents in Dynamic Environments](https://arxiv.org/abs/2605.18421) | arXiv record, submitted 2026-05-18 and revised 2026-06-15; it is a preprint, not a proceedings status, and reports no single memory method consistently winning in its benchmark. |
| OPP-09 | [Memory-R1: Enhancing Large Language Model Memory with Reinforcement Learning](https://arxiv.org/abs/2508.19828) | arXiv record, submitted 2025-08-27 and revised 2026-01-14; preprint status and ADD/UPDATE/DELETE/NOOP memory-operator description match the record. |
| OPP-10 | [PROV-AGENT: Provenance-Aware Agentic Workflows](https://arxiv.org/abs/2508.02866) | arXiv record, submitted 2025-08-04 and revised 2025-08-20; it remains labeled a preprint in the scan even though the comments mention an e-Science acceptance, and the W3C PROV/MCP workflow description matches the record. |
| OPP-11 | [HALT: Learning to Stop Searching for Evidence](https://arxiv.org/abs/2608.02009) | arXiv record, submitted 2026-08-03 and revised 2026-08-04; preprint status and evidence-coverage stopping/three-task abstract description match the record. |
| OPP-12 | [Retrieval-Augmented Generation for Historical Question Answering: The Role of Source Diversity](https://aclanthology.org/2026.lrec-1.53/) | ACL Anthology LREC-COLING 2026 record; the English/French/Dutch Napoleon setting, three Qwen3 models, ten questions, and perspective-shift framing match the abstract. |

These rechecks found no source-status correction required. In particular,
OPP-08 through OPP-11 remain arXiv preprints; the scan does not upgrade them
to peer-reviewed evidence. The records support “active prior work in the
scanned seams” and conditional/task-specific observations, not a unified
Pattern Map mechanism, correctness, human decision quality, transfer, or
effectiveness.

## Findings

### L2-01 — scoped compound dispositions violate the controlled status vocabulary

**Severity:** P2
**Disposition:** **Accepted with revision**
**Affected surface:** `docs/ADVISORY_REVIEW_DISPOSITIONS.md:459` (PUS-01),
`qa/applied/PROJECT_USE_COLD_START_QA_2026-08-30_d05aca5.md:55` (PU-01),
`qa/publication/OPPORTUNITY_EXPANSION_PUBLIC_MENTOR_REHEARSAL_QA_2026-08-30_d05aca5.md:63`
(PUB-07), and the mirrored PUB-07 row in
`qa/applied/advisory/PUBLIC_MENTOR_KIT_CROSS_LANE_CHALLENGE_2026-08-30_f2311d0.md:385`;
the integration decision is also summarized in D-043.
**Governing requirement:** `docs/REVIEW_AND_DISPOSITION_PROTOCOL.md` requires
one controlled disposition per material finding: `Accepted`, `Accepted with
revision`, `Deferred`, or `Rejected`. It does not define a compound status.

The integrated PUS-01 row currently says:

> `Rejected as P1; optional boundary accepted with revision`

That sentence preserves a useful disagreement, but it places two statuses in
the disposition column. A downstream reader cannot tell whether PUS-01 is
closed as rejected, accepted with revision, or still split by scope. The
reason text already explains the distinction: the proposed *mandatory generic
adoption layer* was rejected, while the narrower optional starter was retained
under D-042. The distinction belongs in the finding/reason, not in a hybrid
controlled-status cell.

The same status-shape problem appears in the newly integrated candidate
inventories: PU-01 says `Rejected after static composition probe`, while PUB-07
says `Rejected for current need; social-image decision Deferred` in both the
public QA and its applied cross-lane mirror. These are understandable scoped
decisions, but the controlled status cell still contains more than one status
or a non-controlled suffix. They should be normalized at the same time rather
than leaving the ledger and its source reports to encode scope inconsistently.

**Smallest safe action for integration:** split each scoped finding into clearly
named rows, or set each current row's disposition to one exact controlled value
(most faithfully, `Accepted with revision` for PUS-01's retained optional
boundary; `Rejected` for PU-01/PUB-07's current candidate, with any future
decision recorded separately). State the rejected/retained scope in the reason
column or surrounding prose. Preserve the historical P1 challenge and the
future social-image option as narrative/follow-up text, but do not create a
fifth or hybrid disposition. No starter, publication, or canonical artifact
change is required.

### L2-02 — categorical empty-space sentence exceeds the scan boundary

**Severity:** P2
**Disposition:** **Accepted with revision**
**Affected surface:** `qa/research/OPPORTUNITY_SOURCE_SCAN_2026-08-30_d05aca5.md:38-44,50-79`; the compact source-route paragraph and C16-018 are
already narrower, but should not be read as silently ratifying the categorical
sentence.
**Governing requirement:** the research and source-authority rules require
targeted/non-exhaustive labeling, separation of author-reported findings from
Pattern Map inference, and no inflated novelty claim.

The scan correctly says it is a targeted, non-exhaustive wayfinding pass and
that it did not perform systematic search or novelty clearance. Its executive
disposition nevertheless says:

> “Any claim of component-level empty space is not defensible.”

The twelve records materially constrain empty-space claims in the *scanned*
seams: perspective diversity, counterevidence verification, context burden,
temporal validity, memory operations, provenance, and evidence-coverage
stopping all have adjacent work. They cannot establish a universal negative
about every possible component-level formulation, representation, task, or
unscanned literature. A categorical sentence can be quoted independently of
the nearby limitation and thereby turn “this targeted scan found active work”
into an unsupported exhaustive conclusion.

**Smallest safe action for integration:** revise the sentence to something such
as “For the component areas and records scanned here, an empty-space claim is
not warranted” or “The reviewed records occupy these seams; this targeted scan
does not assess broader component-level novelty.” Keep the existing narrower
C16-018 and source-route language, which correctly says the work does not
establish a unified mechanism, validated method, or unsupported component
absence. This is a claim-boundary repair, not a thesis or six-family change.

### L2-03 — optional source-route density is currently proportionate; freeze it

**Severity:** P3
**Disposition:** **Deferred**
**Affected surface:** `manuscript/SOURCES_AND_RESEARCH_ROUTE.md:110-128` and
the supplemental scan pointer.
**Governing requirement:** D-042 and the Loop 2 proportionality/removal test
require additions to reduce a named friction and preserve progressive
disclosure; the route is optional and subordinate to the manuscript.

I specifically tested whether the new citations improve the optional route or
merely make it denser. The addition is 19 lines and five anchor links, not a
30-line bibliography dump. It points to one detailed QA report rather than
moving all twelve records into the manuscript. Each selected anchor represents
a distinct constraint—perspective coverage, context burden, conditional
memory usefulness, workflow provenance, and evidence-coverage stopping—and the
paragraph explicitly states what those sources do *not* establish. The current
shape therefore earns its space: it makes the route's claim ceiling legible
without turning the essay into a literature review.

**Action:** hold the route at this compact five-anchor/one-report shape. Do not
add the remaining source links, a paper order, or a provider/model/corpus/study
recommendation unless a later owner-authorized question identifies a specific
reader or claim gap and the extra link replaces an existing burden. Recheck
status and URLs at publication time, as the route already requires. This is a
maintenance guard, not a reason to remove the current addition.

### L2-04 — static removal/closure labels need contextual qualifiers when reused

**Severity:** P3
**Disposition:** **Accepted with revision**
**Affected surface:** the publication QA/advisory summaries that say each
note “passes the removal test” and that Loop 1 “closes” after accepted
revisions; the project-use QA wording is already more explicit about a static
composition probe.
**Governing requirement:** D-042 and the research boundary prohibit presenting
protocol, fixture, planning simulation, model review, or static composition as
empirical reader, transfer, or effectiveness evidence.

Read in context, the publication QA correctly labels the kit as local,
unpublished, unsent, and not a reader/mentor/effectiveness result. The removal
test is also a reasonable design check: deleting a note should remove a named
editorial friction. The residual risk is portability of the phrase. “Passes the
removal test” or “Loop 1 closes” can sound like observed validation when copied
into a summary without the adjacent static-evidence caveat.

**Action:** in future cross-lane summaries, write “passes the conceptual/static
removal check” and “Loop 1 closes its document-composition review, with no
reader or transfer result.” No current public artifact or canonical text needs
to be expanded; this is a precision guard for subsequent summaries.

## Boundary matrix: claims that remain safe

| Risk challenged | Finding after exact integration |
| --- | --- |
| Novelty inflation | No integrated text says the six families, provenance, memory, retrieval diversification, or stopping mechanisms were invented here. The source route and C16-018 explicitly frame them as active prior work and retain an authored synthesis/testable-agenda ceiling. L2-02 is the only material over-broad negative found. |
| Effectiveness inflation | The starter's and publication kit's QA records are explicitly static/document-composition evidence. No reader comprehension, mentor response, transfer, decision quality, or framework effectiveness result is claimed. |
| Generality/transfer inflation | The starter says optional, internal, repository-local, and non-portable; the public QA says it is not a transfer result. The root README and handoff keep it out of the canonical Signal Foundry packet. No P1/P2 generality defect remains. |
| Readiness/publication inflation | The publication kit says local owner-review candidate, unsent, unpublished, no identity/destination/URL, and HOLD/NOT AUTHORIZED. The site has no starter/publication pointer and was not deployed. |
| Source-status accuracy | All twelve named primary/official records were reopened. ACL records remain official proceedings; arXiv records remain preprints. No scan status is upgraded by comments, benchmark figures, or model review. |
| Targeted-not-exhaustive labeling | Source route and scan state the boundary. L2-02 repairs the one sentence that outruns it. Existing claims ledger language is already appropriately conditional. |
| Manuscript/source-route burden | The route addition is 19 lines/five anchors/one QA pointer and adds distinct claim constraints. It is proportionate now; L2-03 freezes growth absent a named gap. |
| Echo/v16 separation | The route, handoff, package map, and D-043 preserve Echo as a separate v15.2-derived origin-accounting track. V16 uses only the fictional common-origin example and imports no Echo result, selected model, or discovered provenance. |
| No-results preservation | No current study was run. The Echo protocol/fixtures/unfavorable-result classes remain unrun/no-results. Static QA is not framed as validation. |
| Provenance/receipts | No source claims that a Pattern Map receipt, ledger, or trace is a new mechanism merely because components are composed. PROV-AGENT is treated as adjacent prior work, not v16 validation. |
| Paper/provider/model/corpus/study selection | None is selected. The scan records source wayfinding only; it does not choose a first paper, order, vendor/provider, model, corpus, sample, benchmark run, study design, or spend. |
| Thesis authority | The broad six-family, human-governed thesis is retained. Research narrows component-level claims and exposes agenda seams; it does not redefine v16 as memory, provenance, retrieval, or Echo. |

## Removal and proportionality test

The current additions survive a bounded removal test with the qualifications
above:

- Removing the project-use starter would remove a repository-local cold-start
  wayfinding aid, but it would not remove a canonical claim or an empirical
  result. Its retention is justified only as optional internal composition and
  should remain out of public/canonical packets.
- Removing the publication kit would remove a private rehearsal aid for an
  already existing human essay/site; it would not remove publication authority,
  reader evidence, or a new public artifact. Retention is proportionate while
  it remains unsent and subordinate.
- Removing the compact source-route paragraph would hide useful current
  claim constraints and force readers to infer them from a large QA report.
  Its five anchors and explicit limits are therefore justified. Adding the
  other seven links would not currently remove a distinct route friction.
- Removing the detailed scan would remove source-by-source status/limits and
  make the compact route less auditable. It is appropriately kept in QA, not
  promoted into the essay as an exhaustive literature review.

The test does not show that any addition is easy, effective, transferable, or
scientifically validated. It only supports bounded document-composition and
claim-audit reasons for their current locations.

## Controlled follow-up required

The integrator should address L2-01 and L2-02 before recording the integrated
checkpoint as fully closed. L2-03 and L2-04 are maintenance guards and do not
authorize a new artifact, source search, study, provider, model, corpus,
participant, or public action. After correction, the same checksum and
research-boundary checks should be rerun; the owner-intent checksum must not be
refreshed.

## Validation run

The following checks were run on this review branch after writing this report:

```text
(cd docs && shasum -a 256 -c OWNER_INTENT_V16.sha256)
OWNER_INTENT_V16.md: OK

python3 qa/research/validate_research_boundaries.py
PASS: no-results language is preserved
PASS: no study/provider/model/corpus/sample selection language detected
PASS: targeted/non-exhaustive source-route language is present
PASS: Echo/v16 separation language is present
PASS: contribution ceiling language is present
PASS: no canonical manuscript edits detected in research scope

python3 -m unittest discover -s qa/research -p 'test_*.py' -v
Ran 7 tests ... OK

python3 qa/applied/validate_framework.py
PASS

node qa/publication/publication-kit-contract.spec.mjs
PASS

git diff --check d05aca58910b4463e5afb69b10558b662a446278..HEAD
PASS
```

The final commit must contain only this advisory report. No push or merge is
performed by this review.

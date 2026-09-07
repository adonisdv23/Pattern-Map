# EP v1.1 design checkpoint QA and Claude-finding dispositions

**Reviewed branch:** `codex/pattern-map-v16-echo-v1-1`

**Base:** `d4b7b9e481165b3f692986cdda1b8a0da8b4388b`

**Review date:** 2026-08-23

**Scope owner:** `research/the-echo-problem/**`, `qa/research/**`

**Status:** design-only; no model, provider, corpus, participant, or empirical
run

## Executive disposition

The owner-approved recommendations from the Claude-package audit are
implemented with bounded revisions. Amendment A1 is **adopted with the
NEWS-COPY narrowing**, not adopted wholesale. NEWS-COPY can validate
same-original/origin-cluster recovery only. It cannot provide claim support,
truth, `FC_cons`, VOR, or independence labels; nonduplicate relations remain
`UNKNOWN`. Newswire remains aggregate recurrence context unless a future,
separately authorized review verifies member/version and rights truth.

The controlled F0/F1/F2 design remains the first-paper candidate. A typed,
graded, uncertain real-world dependence instrument is a prospective second-paper
candidate only after targeted prior-art review, labelled validation, rights and
version checks, and a new owner decision. Neither is a completed paper or a
research result.

The active implementation is a new provider-free scaffold under
`research/the-echo-problem/v1_1/harness/`. The byte-preserved
`research/the-echo-problem/preserved/**` subtree was not modified.

## Source and authority boundary

The advisory package was:

```text
/Users/gpt/Downloads/PATTERN_MAP_CLAUDE_SESSION_2026-08-19.zip
SHA-256: b544b734324699a93abbb8cf0bcef3d61cc590ff7b603fc167a46b8f8539a253
```

The required package sources were read in the requested order:

1. `00_READ_FIRST/HANDOFF_TO_CODEX.md`
2. `00_READ_FIRST/SESSION_TRANSCRIPT.md`
3. `01_REVIEWS_AND_AUDITS/RED_TEAM_OF_CLAUDE_WORK.md`

The package is advisory material. The repository authority order remains the
owner handoff, locked v16 intent, recovered v13 intent, v14/v15 constraints,
v15.2 for Echo, and then reviews. The package's instructions were not treated
as owner authorization. The preserved v15.2 files and the historical draft
amendment were inspected but left byte-for-byte unchanged.

## Finding dispositions

The controlled vocabulary is the repository's `Accepted`, `Accepted with
revision`, `Deferred`, and `Rejected`. “Accepted” below means an implementation
or boundary was adopted; it never means a future study ran.

| ID | Claude finding or recommendation | Disposition | Evidence checked and exact treatment | Affected active files / governing requirement |
| --- | --- | --- | --- | --- |
| CPK-01 | The original claim of zero database truth-discovery coverage was wrong; Pochampally is already cited and binary dependence is too coarse. | **Accepted with revision** | The source-archive-relative files `00_READ_FIRST/HANDOFF_TO_CODEX.md` §1 and `01_REVIEWS_AND_AUDITS/RED_TEAM_OF_CLAUDE_WORK.md` F1 were checked against the preserved P08 entry at `research/the-echo-problem/preserved/v15.2/prior-art/overnight/01_THEORY_AND_PRIOR_ART_LUNA_MAX.md:82`. The active design retains simple stipulated F0/F1/F2 labels but specifies typed/graded/uncertain dependence for real-world measurement. | `v1_1/PROTOCOL_V1_1_DESIGN_CHECKPOINT.md` §§2, 6; `v1_1/PRIOR_MEASUREMENT_MATRIX.md`. A01/A10/A11/A15; D-001/D-008; authority order. |
| CPK-02 | The prospectus claim that synthetic generation is necessary because public corpora have no origin truth is too absolute. | **Accepted with revision** | The archived sentence at `archive/transfers/v15.2-owner-handoff/03_RESEARCH_PROGRAM_UNRUN/research/PAPER_PROSPECTUS_V0.md:119` is historical and was not rewritten. The active boundary distinguishes NEWS-COPY reproduction labels from claim support/truth and treats Newswire as aggregate context. | `v1_1/PROTOCOL_V1_1_DESIGN_CHECKPOINT.md` §5; `STATUS_AND_BOUNDARIES.md`; A10/A11/A15; archive immutability. |
| CPK-03 | NEWS-COPY and Newswire should be added as full endpoint arms. | **Rejected** | The package's first amendment language at `02_RESEARCH_CONTRIBUTIONS/ORIGIN_ACCOUNTING_PROTOCOL_AMENDMENT_A1.md:68` was narrowed by its own red team at `01_REVIEWS_AND_AUDITS/RED_TEAM_OF_CLAUDE_WORK.md:65`. Reproduction is not claim support, truth, or independence. NEWS-COPY is restricted to same-original/origin-cluster validation; nonduplicates remain unknown; Newswire cannot enter `A`, `M`, FC, VOR, or confirmatory inference. | `v1_1/PROTOCOL_V1_1_DESIGN_CHECKPOINT.md` §5; A10/A11/A15; D-008. |
| CPK-04 | The manifest hash covered only index-assigned IDs and could not detect content changes. | **Rejected as a canonical-defect claim; accepted with revision as a design safeguard** | The current package implementation already separates content and membership in `03_CODE/origin-accounting/oa/schema.py:77`; the canonical preserved helper separates content and ordered membership at `preserved/v15.2/tools/origin_accounting/canonical.py:49`. The absent pre-fix implementation cannot be independently audited. The new active receipt makes the distinction explicit and tests content mutation and membership reordering separately. | `v1_1/harness/canonical.py`, `v1_1/harness/test_v1_1.py`; A10/A14; archive/provenance rules. |
| CPK-05 | Calibration controlling distinct rather than supporting origins is confounded. | **Accepted with revision** | The package warning is at `HANDOFF_TO_CODEX.md:36` and `RED_TEAM_OF_CLAUDE_WORK.md:45`. The active scorer reports invalid-only and valid-count-risk components, preserves supporting-origin scope, and does not make calibration confirmatory. | `v1_1/harness/scoring.py`; `PROTOCOL_V1_1_DESIGN_CHECKPOINT.md` §3; A10/A11; canonical v1 endpoint boundary. |
| CPK-06 | The F0 parity defect is a one-token issue and the package says it is fixed. | **Accepted with revision** | Real BPE independently refuted the old package claim: the preserved package ran 3 failed / 6 passed, with representative mismatches 386/387, 402/403, and 390/391; broader reported failure counts include 44/300, 22/120, 10/60, and 38/200. The old package's `03_CODE/origin-accounting/oa/conditions.py:88` was not adopted. The new solver tests F1/F2 and keeps F0 secondary. | `v1_1/harness/parity.py`, `harness/test_v1_1.py`, `harness/README.md`; A10/A15; v1.0 parity gate. |
| CPK-07 | Replace origin grouping with graded typed dependence everywhere. | **Accepted with revision** | Pochampally supports graded correlation, but the canonical F0/F1/F2 question deliberately uses simple stipulated labels to isolate the supplied-cue contrast. Real-world measurement records now use typed, graded, uncertain fields; controlled labels are not exported as independence. | `PROTOCOL_V1_1_DESIGN_CHECKPOINT.md` §2; A03/A10/A11; D-007/D-008. |
| CPK-08 | Power is approximately 87% at effect 0.10 and 33% at 0.05 at N=300; −0.08 is near the resolution limit. | **Accepted with revision** | Claude's script reproduced `0.873` and `0.327` under its declared bootstrap/mixing assumptions. The active exact-McNemar surface makes discordance explicit: at baseline `0.38`, discordance `0.30`, and `n=300`, decision probability was about `0.69` for `-0.08`; the 80% planning MDE lay between `-0.09` and `-0.095`. At `n=400`, `-0.08` reached about `0.82`. All are planning-only and conditional on an unfrozen interval/invalidity design. | `v1_1/harness/planning.py`, `PROTOCOL_V1_1_DESIGN_CHECKPOINT.md` §7; A10/A11/A15; v1.0 planning section. |
| CPK-09 | Make the measurement paper the first paper because nobody has measured retrieval dependence. | **Rejected as an exclusive reframe; accepted with revision as a second-paper route** | The package recommendation is at `02_RESEARCH_CONTRIBUTIONS/OVERNIGHT_FINDINGS_AND_RECOMMENDATION.md:98`. The targeted matrix records Henzinger, Groundhog Day, CopyCat, News Provenance, NEWS-COPY, Newswire, RARE, and Ross et al.; it makes no exhaustive novelty claim. Controlled F0/F1/F2 remains first-paper candidate; typed real-world measurement remains second-paper candidate pending validation. | `v1_1/PRIOR_MEASUREMENT_MATRIX.md`; `README.md`, `RELATION_TO_V16.md`, `VERSION_HISTORY.md`; owner intent, A01/A10/A16. |
| CPK-10 | The seven-system review shows systems do not account for independence; EvidentialRAG is a decisive gap. | **Accepted with revision** | Only the EvidentialRAG derivation was fully checked. The package itself says its seven-system summary is not fully audited at source-archive-relative `02_RESEARCH_CONTRIBUTIONS/OVERNIGHT_FINDINGS_AND_RECOMMENDATION.md:78`. The active record treats it as an adjacent specific finding, not a systematic absence claim. | `v1_1/PRIOR_MEASUREMENT_MATRIX.md`; `PROTOCOL_V1_1_DESIGN_CHECKPOINT.md` §6; no novelty/exhaustiveness claim. |
| CPK-11 | EvidentialRAG's conflict mechanism produces K=0 for same-claim copies and never engages. | **Accepted with revision** | [EvidentialRAG v1](https://arxiv.org/html/2607.10491v1) equations (7)–(13) and §§6.4–7 were checked in the authors' complete paper. Same-claim singleton supports create no pairwise conflict, so specifically the `lambda K` conflict-transfer term adds no uncertainty. The late limitations mention provenance/source credibility only as future work and add no independence, correlation, copying, or syndication correction. Other evidential accumulation still operates; this is one mechanism-specific derivation, not evidence that all retrieval systems fail. | `v1_1/PRIOR_MEASUREMENT_MATRIX.md`; `PROTOCOL_V1_1_DESIGN_CHECKPOINT.md` §6; prior-art claim boundary. |
| CPK-12 | Every origin-rate figure is a lower bound because heavy transformation over-splits. | **Rejected as a universal claim; accepted with revision as a bidirectional-error warning** | The package claim is at `02_RESEARCH_CONTRIBUTIONS/OVERNIGHT_FINDINGS_AND_RECOMMENDATION.md:150`; the single-linkage implementation is at `03_CODE/origin-dependence/origin_rate.py:55`. False merges, bridge documents, and topic-matched passages can bias in the opposite direction. | `PROTOCOL_V1_1_DESIGN_CHECKPOINT.md` §8; threshold-validation gate; no active adoption of package origin-rate code. |
| CPK-13 | The containment threshold 0.40 is ready to use or can be accepted from synthetic ARI alone. | **Accepted** | Synthetic ARI is retained only as an implementation diagnostic. Before any reported real number, the threshold must be tuned/validated on labelled text with pairwise and cluster metrics, false-merge/false-split rates, transformation strata, and a declared loss function. | `PROTOCOL_V1_1_DESIGN_CHECKPOINT.md` §8; A10/A11/A15. |
| CPK-14 | Adopt the package `origin-accounting` harness as the protocol implementation. | **Rejected as wholesale adoption; accepted with revision as a defect inventory** | The package harness asks for origin IDs not shown to the model (`03_CODE/origin-accounting/oa/schema.py:69`), conflates one-origin support with empty support (`generate.py:55`), differs in endpoint semantics (`metrics.py:13`), permits parser repair (`models.py:7`), omits exact paired p in the primary decision (`run.py:52`), and has a vacuous assertion (`tests/test_pipeline.py:45`). The active scaffold is rebuilt from the preserved v1 definitions and has no provider path. | `v1_1/harness/{parser,scoring,canonical,planning}.py`; A10/A11/A15; review/disposition protocol. |
| CPK-15 | Use the package's A2/Kish-style calibration interpolation and its broad full-endpoint F3 amendment. | **Rejected** | The calibration and F3 recommendations exceed the canonical endpoint and truth boundary. Calibration remains exploratory/decomposed; F3 transfer remains an origin-validation sidecar only. | `PROTOCOL_V1_1_DESIGN_CHECKPOINT.md` §§3, 5, 8; A10/A11/A16. |
| CPK-16 | Treat the package's synthetic power, ARI, parser, or mock-model checks as support for efficacy. | **Rejected** | All active docs label these as deterministic implementation or planning checks. The no-results boundary and all 11 unfavorable-result classes remain preserved. | `README.md`, `STATUS_AND_BOUNDARIES.md`, `v1_1/README.md`, `EP_V0_1_STATUS.json`; A10/A11/A15. |
| CPK-17 | Claude's separate site branch found extension/type mismatches and stale-history differences. | **Deferred** | The image-extension hygiene finding is real but belongs to the site/visual ownership lane, not this Echo branch. The stale-history assertion is not adopted as authority; current canonical Git history is authoritative for current state. | No active Echo file; future site maintenance task. Artifact ownership and review protocol. |
| CPK-18 | The package should be integrated into v16 as the primary thesis or site opening. | **Rejected** | The owner-locked broad thesis and six-family firebreak explicitly prohibit provenance-only drift. EP remains a separate optional route and a bounded common-origin example. | `RELATION_TO_V16.md`, `README.md`; A01/A03/A10/A16; D-001/D-008. |
| E11-AUDIT-01 | The documented invalidity sweep was not exposed by `run_power_surface` or its CLI. | **Accepted with revision** | The surface and CLI now accept repeatable explicit F1/F2 invalidity pairs, including unequal rates; `0,0` remains the bounded default. Deterministic tests cover equal-zero and unequal `0.02,0.05` cells. | `v1_1/harness/planning.py`, `harness/test_v1_1.py`, `harness/README.md`; implementation/documentation agreement. |
| E11-AUDIT-02 | The naive exact-tail calculation could emit a negative p-value through cancellation and overflow at larger discordant N. | **Accepted with revision** | The exact-binomial decision now uses a stable lower-tail recurrence with an explicit `[0,1]` bound. Regression tests cover all-discordant `n=100`, `400`, and `2000`, all-concordant `n=400`, and bootstrap pair-shape failures. | `v1_1/harness/planning.py`, `harness/test_v1_1.py`; valid planning arithmetic. |

## Verification performed

### Authority and preservation

```text
(cd docs && shasum -a 256 -c OWNER_INTENT_V16.sha256)
OWNER_INTENT_V16.md: OK
```

The preserved-source verifier was run against the curated v15.2 copy. No file
under `research/the-echo-problem/preserved/**` was edited by this task.

### Active harness

```text
python3 -m unittest discover -s research/the-echo-problem/v1_1/harness -p 'test_*.py' -v
Ran 12 tests ... OK (skipped=1)
```

The one skip is the optional `tiktoken` test when the system interpreter does
not have that dependency. It is explicitly a skip, not a parity pass. The
other eleven tests cover strict parser fixtures, FC/VOR separation, content
and membership hashes, bounded/stable exact paired logic, bootstrap pair-shape
failures, three deterministic parity checks, explicit equal and unequal
invalidity cells, planning determinism, and a static no-provider import scan.

In an ephemeral `uv` environment, the optional real-BPE test passed against
the checked fixture generated from Claude's own seed-1 renderer:

```text
package: tiktoken 0.14.0
encoding: cl100k_base
mergeable ranks: 100256
encoding-table fingerprint: 5af8a02a651e9db4366b5b14c2cc8f506d721ebdab0db3294337dd8ba15c4528
package/version-inclusive fingerprint: b5d2d2f6c0d6accb1d0fc3ab8700f485200a941c7e950216ff9f5737312df4e2
Claude-renderer F1/F2 prompt pairs: 300
exact parity failures: 0
base F2-minus-F1 deltas: [-7,-6,-5,-4,-3,-1,0,1,3,4,5,6,7,8]
padded token-count range: 292-486
fixture SHA-256: 98b29d886a839e8adada99737d6a001e269f21b2dbea89f1d5bbf09091f131e8
```

This is exact parity for Claude's rendered synthetic protocol templates after
the new solver uses its reserved development padding slot. It is **not** parity
for a selected model's chat template, because no model, checkpoint, or
production tokenizer has been selected. It is also not a model or research
result. The fixture generator replayed byte-identically against source archive
SHA-256 `b544b734324699a93abbb8cf0bcef3d61cc590ff7b603fc167a46b8f8539a253`.

The old Claude package's real-BPE parity claim was separately refuted: with the
same `tiktoken 0.14.0`/`cl100k_base` family, its suite was 3 failed / 6 passed;
representative one-token mismatches were 386/387, 402/403, and 390/391, and
reported broader failure counts included 44/300, 22/120, 10/60, and 38/200.
The new solver's pass does not retroactively change that historical result.

The checked fixture and optional test exercise the exact Claude-package
`oa.generate`/`oa.conditions.render` bytes named by their source hashes. The
fixture contains no model output and imports no provider at test time. The
source package remains advisory; preserving its rendered synthetic prompts for
replay does not adopt its protocol or make it canonical authority.

The package's planning script was also reproduced exactly: at `n=300` it
reported `0.873` for effect `0.10` and `0.327` for effect `0.05`. Under the
active exact-McNemar surface with baseline `0.38` and discordance `0.30`,
10,000 planning repetitions gave `0.6863` at `-0.08`, `0.7864` at `-0.09`,
`0.8372` at `-0.095`, and `0.8782` at `-0.10`. With effect `-0.08`, increasing
`n` from 300 to 400 changed the planning decision probability from about
`0.69` to `0.82`. These are simulated design calculations, not observed power.

### Scope limitations

- No model, provider, corpus, participant, external dataset, or paid service
  was called or acquired.
- No live prompt, selected chat template, output, effect, power, coverage,
  threshold, or generalization was observed.
- NEWS-COPY and Newswire were not acquired or executed in this checkpoint.
- The 0.40 containment threshold remains unvalidated on labelled real text.
- The prior-measurement matrix is targeted and non-exhaustive.
- The active solver's development padding slot requires a future selected
  template/resource receipt and semantic audit before any live condition.
- The preserved v15.2 protocol remains historically unchanged; this active
  checkpoint is a design successor, not a result or authorization.

## Remaining owner gate

No consequential decision is required to merge this design checkpoint later.
Before any live research, the owner must separately authorize the model or
provider, data/rights route, selected tokenizer/chat template, final parity
receipt, threshold validation, interval method, and study or publication path.
Until then, the strategic order remains F0/F1/F2 first-paper candidate and
typed real-world measurement second-paper candidate, both unrun.

# V15 loop 1 evidence-fix validation

## Validation identity

- **Worktree:** `/Users/gpt/Documents/Codex/worktrees/discrimination-layer-v15-evidence-fix`
- **Branch:** `codex/discrimination-layer-v15-evidence-fix`
- **Base reviewed:** `9708109` (`review: record v15 loop1 evidence novelty findings`)
- **Validation date and status cutoff:** 2026-08-18
- **Disposition:** `PASS`
- **External effects:** none. No model, provider, paid service, deployment, publication, contact, or dataset download was used.

This receipt rechecks the P1-01 and P2-01–P2-05 findings from
`reports/V15_LOOP1_EVIDENCE_NOVELTY_REVIEW.md`. The corrections are limited to
source visibility, status wording, provenance/origin terminology, and
reconciliation bookkeeping. The locked F0/F1/F2 causal core is not broadened.

## Finding-by-finding re-review

### P1-01 — closest direct natural-language provenance comparator: PASS

- `research/PRIOR_ART_DELTA_V1.md:86` now records S19, Zhang, Ives & Roth,
  ACL 2020, published ACL Anthology, pages 4416–4426.
- `research/PRIOR_ART_DELTA_V1.md:344-356` separates the primary-record fact,
  the project inference, the blocked claim, and the residual contribution.
- `source/THOUGHT_PIECE_V15.md:324-330` names the published comparator and
  states that inferred provenance is not the supplied benchmark relation.
- `research/PAPER_PROSPECTUS_V1.md:63-73` carries the same boundary into the
  residual-contribution section.
- `site/app/content.ts:286` surfaces the ACL 2020 source and its boundary;
  `site/app/page.tsx:625` routes readers to the full S1–S19 source/status
  ledger.
- `research/V15_CLAIM_SOURCE_ARTIFACT_MATRIX.md:13-15,24` names the source and
  prohibits provenance-discovery or inferred-source-path wording.
- Primary record rechecked: [ACL Anthology 2020.acl-main.406](https://aclanthology.org/2020.acl-main.406/).
  The record identifies a published ACL 2020 paper that defines natural-language
  claim-provenance graphs, uses information extraction/textual entailment for
  provenance inference, and evaluates on two benchmark datasets.

**Result:** PASS. The comparator is now visible and the project does not
present the supplied relation treatment as provenance inference.

### P2-01 — omitted retrieval comparator visibility: PASS

- `site/app/content.ts:291-295` now includes MMR, SetR, NEST, RARE, and Schelpe
  with primary URLs, publication/preprint status, and adjacent/future scope.
- `source/THOUGHT_PIECE_V15.md:348-353` names MMR, NEST, RARE, and Schelpe with
  exact status qualifiers and states that these are not required F0/F1/F2 arms.
- `research/PAPER_PROSPECTUS_V1.md:93-98` carries the same status and
  comparator boundary.
- `research/PRIOR_ART_DELTA_V1.md:77-83,360-369,487-498` remains the full
  S1–S19 route with the layered retrieval boundary and primary URL index.
- `site/app/page.tsx:617-625` presents the selected sources and directly routes
  to `research/PRIOR_ART_DELTA_V1.md` for the complete status ledger.

**Result:** PASS. The omitted records are surfaced or directly routed, while
the confirmatory study remains unchanged.

### P2-02 — unqualified reader independence terminology: PASS

- `site/app/page.tsx:10-11` now uses “Origin relation / stipulated
  distinctness” in the central distinction contract.
- `site/app/page.tsx:24,34,106,139,191,480` no longer uses unqualified
  independence terminology for the central reader distinctions; the remaining
  explicit `real-world independence` and `INDEPENDENT-AS-STIPULATED` uses are
  qualified boundary statements.
- `site/app/content.ts:264,268,284,287` defines origin relation, recurrence,
  NEWS-COPY, and Naphade without treating document distinctness as a verified
  separate origin.
- `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:160-164` still prohibits
  the origin vocabulary from absorbing real-world independence.

**Result:** PASS. The reader’s central labels now point to the stipulated
origin-relation construct rather than implying an open-world independence
detector.

### P2-03 — explicit manuscript statuses: PASS

- `source/THOUGHT_PIECE_V15.md:332-346` identifies:
  - RAMDocs as a COLM 2025 conflict benchmark;
  - Li/Padman/Krishnan as arXiv v1 submitted 2026-05-27 with no venue
    acceptance shown;
  - EvidentialRAG as arXiv v1 submitted 2026-07-11 with no venue or acceptance
    shown;
  - Naphade as arXiv v1 submitted 2026-01-08 with an ACL ARR comment and no
    acceptance shown; and
  - Ross as arXiv v1 submitted 2026-08-14 with no venue or acceptance shown.
- `research/PAPER_PROSPECTUS_V1.md:76-97` repeats the status boundaries and
  qualifies RARE as an arXiv v2 record claiming ACL 2026 acceptance without an
  ACL venue page located.
- `research/PRIOR_ART_DELTA_V1.md:370-401,451-462` remains the status ledger
  and closest-working-manuscript register.

**Result:** PASS. A reader can distinguish published venue records, accepted
records without a venue page, and arXiv-only working manuscripts.

### P2-04 — stale case-study ownership wording: PASS

- `research/PRIOR_ART_DELTA_V1.md:108` now refers to “Any project origin field.”
- `research/PRIOR_ART_DELTA_V1.md:385` now refers to an automatic detector “for
  the project,” not Signal Foundry.
- `rg -n "Any Signal Foundry origin|detector for Signal Foundry"
  research/PRIOR_ART_DELTA_V1.md` returns no matches.
- The bounded case-study boundary remains in
  `source/THOUGHT_PIECE_V15.md:433-444` and
  `research/V15_CLAIM_SOURCE_ARTIFACT_MATRIX.md:20`.

**Result:** PASS. Signal Foundry remains a bounded design case and is not named
as owner of the research program.

### P2-05 — Laitenberger source fact versus project inference: PASS

- `site/app/content.ts:297` now labels the entry explicitly:
  “Sourced fact: published EMNLP 2025 DOS RAG and matched-budget baseline
  recommendation. Project inference: added structure must earn value against a
  simple baseline; adjacent/future comparator, not a required F0/F1/F2 arm.”
- `research/PRIOR_ART_DELTA_V1.md:427,435,483` and
  `reports/V15_DECISION_LEDGER.md:151` preserve the adjacent/future comparator
  boundary and keep those systems out of the locked core.
- Primary record rechecked: [ACL Anthology EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1656/).
  The abstract describes DOS RAG as a simple retrieve-then-read baseline that
  preserves source fidelity and recommends matched token budgets; the added
  complexity implication is recorded here as project inference.

**Result:** PASS. The source finding is no longer presented as a direct mandate
to add an arm to the locked study.

## Independent primary-record status recheck

The following primary/official records were reopened on 2026-08-18:

| Record | Rechecked status and boundary |
| --- | --- |
| [Zhang, Ives & Roth, ACL 2020](https://aclanthology.org/2020.acl-main.406/) | Published ACL paper; natural-language claim-provenance graph and inference precedent. |
| [Naphade, arXiv:2601.06189](https://arxiv.org/abs/2601.06189) | Submitted 2026-01-08; ACL ARR submission comment; no acceptance shown. Table 4 model attribution remains DeepSeek-R1-8B 67.6%/76.5% and Llama-3.1-70B-Instruct 62.9%/69.8%. |
| [Li, Padman & Krishnan, arXiv:2605.29084](https://arxiv.org/abs/2605.29084) | Submitted 2026-05-27; no venue acceptance shown; cross-source answer relation, not derivation. |
| [EvidentialRAG, arXiv:2607.10491](https://arxiv.org/abs/2607.10491) | Submitted 2026-07-11; no venue or acceptance shown; conflict/uncertainty fusion, not provenance. |
| [Ross et al., arXiv:2608.13956](https://arxiv.org/abs/2608.13956) | Submitted 2026-08-14; no venue or acceptance shown; FictionalQA duplicate/paraphrase/diversity comparator. |
| [MMR](https://doi.org/10.1145/290941.291025) | Published SIGIR 1998 diversity-reranking record. |
| [SetR](https://aclanthology.org/2025.acl-long.861/) | Published ACL 2025 set-wise retrieval record. |
| [NEST](https://aclanthology.org/2026.acl-industry.35/) | Published ACL 2026 Industry Track record. |
| [RARE](https://arxiv.org/abs/2604.19047) | arXiv v2; record says accepted to ACL 2026 Main Conference; no ACL venue page located in this pass. |
| [Schelpe](https://arxiv.org/abs/2605.09611) | arXiv v1 preprint submitted 2026-05-10. |
| [Laitenberger, Manning & Liu](https://aclanthology.org/2025.emnlp-main.1656/) | Published EMNLP 2025 record; simple retrieve-then-read baseline and matched-budget recommendation. |

No reviewed source was used to claim a project result, provenance discovery,
real-world independence, or a universal RAG law.

## Locked-core regression checks

- `source/THOUGHT_PIECE_V15.md:459-469`,
  `research/PAPER_PROSPECTUS_V1.md:133-159`, and
  `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:16-48` retain F0/F1/F2,
  F2-minus-F1, byte/token parity, fixed denominators, explicit `UNKN`, and no
  model run.
- `research/PRIOR_ART_DELTA_V1.md:483`,
  `research/PAPER_PROSPECTUS_V1.md:240-257`, and
  `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md:378-383` retain exactly two
  confirmatory decisions; calibration remains descriptive without an explicit
  probability target and proper scoring rule.
- `site/app/page.tsx:547-570` retains the three conditions, 300 assigned
  bundles, conservative invalid coding, and exact parity boundary.
- `site/app/page.tsx:579-584` and
  `source/THOUGHT_PIECE_V15.md:501-518` retain descriptive T1 outside `A`,
  `M`, intervals, tests, VOR, and effect estimates.
- `reports/V15_DECISION_LEDGER.md:68-76,141-151` records the loop-1 receipt
  without changing the study estimand, denominators, calibration exclusion, or
  T1 boundary.
- No model-result, transfer-result, human-result, deployment-result, or effect
  claim was introduced.

## Corrected artifact hashes

These hashes are the corrected files at validation time. The ledger’s own hash
is intentionally not listed because its loop-1 receipt records this table and
must be hashed after the final commit.

| Artifact | SHA-256 |
| --- | --- |
| `research/PRIOR_ART_DELTA_V1.md` | `3db0592bba071d3075a7694f1364545523f555af3c96f3122bf767489b4a1c66` |
| `source/THOUGHT_PIECE_V15.md` | `6d6149016cda9816785051cf6a07a5cbeb5c5740f321101ce1a0cf457ef4f7c3` |
| `research/PAPER_PROSPECTUS_V1.md` | `e88b79307200a11ef1c07f6541ba6e047985501e37769e06c59b5f9ac5bd4d34` |
| `site/app/content.ts` | `91213f679cc7ea1300fa85c05473b5568bd2d3cf87fbccd70c3da045aebb73fd` |
| `site/app/page.tsx` | `bdc9cbb24cfa5af3be27ca442c1639052ed4551483e20933459d6aeab1ae80d9` |
| `research/V15_CLAIM_SOURCE_ARTIFACT_MATRIX.md` | `2aa06b7ffa9c04d983eb6615fec162d4592e0b97095ff6737fafa20a1006cc73` |
| `reports/V15_LOOP1_EVIDENCE_NOVELTY_REVIEW.md` | `e0120c310c784f67160c2b62cfb834365a018ef6d225b4f2aa7c535cbadd2e88` |

## Checks run

All checks were offline except public primary-record verification:

- `git status --short --branch` and `git diff --stat`: only the seven intended
  canonical artifacts were modified before this receipt; the validation report
  is the only new artifact.
- `git diff --check`: pass.
- Standard-library Markdown URL syntax check over the corrected source/report
  files: pass; all extracted links had `http`/`https` schemes and hosts.
- Bounded HTTP status probe over 50 unique extracted URLs from the corrected
  research/report files and changed site source (excluding the pre-existing
  auth-protected v13 visual-map link, which returned 401 and was not changed):
  44 returned 2xx/203.
  Four DOI endpoints returned 403 (publisher anti-bot behavior for BMJ, ACM,
  and the two PVLDB DOI links), and the two ETH Research Collection URLs
  returned 500 on the bounded HEAD request (one bounded GET subsequently reset
  the connection). The corresponding direct/official records were independently
  re-opened through the primary-record browser check; these transport responses
  do not change the cited publication/status findings.
- `python3 -m unittest -q tests/test_origin_accounting.py`: 7 tests passed.
- `python3 -m compileall -q tools tests`: pass.
- `site/node_modules` is absent, so the Next/ESLint checks could not be run;
  packages were not installed.
- No model, provider, paid service, deployment, publication, or dataset action
  was run.

## Final validation disposition

**PASS.** P1-01 and P2-01–P2-05 are addressed with primary-source links,
explicit fact/inference boundaries, exact status labels, central reader
terminology, corrected project ownership wording, and updated hash/disposition
bookkeeping. The F0/F1/F2 protocol, confirmatory family, calibration boundary,
descriptive T1 boundary, and no-results status remain unchanged.

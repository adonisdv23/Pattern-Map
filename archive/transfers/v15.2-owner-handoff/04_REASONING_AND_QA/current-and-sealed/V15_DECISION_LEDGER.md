# V15 task and decision ledger

Recorded: 2026-08-18
Status: `READY_FOR_LOCAL_OWNER_REVIEW_NO_EMPIRICAL_RESULTS`

Canonical integration branch: `codex/discrimination-layer-v15`

Baseline documentation HEAD: `d0d26e28236e50d49e57bea9554e2a3a7b392198`

Baseline artifact-content commit: `261c516710f67998224a16c056bba0aefd5c26f4`

This is the shared execution and disposition record for v15. It records
reviewable reasons and evidence boundaries; it is not a substitute for source
material, hidden reasoning, empirical results, owner approval, or publication
authorization.

## Frozen truth boundary

- V15 is the canonical local owner-review thought piece, conceptual framework,
  two-track reader, and execution-ready but unrun research program. It is not
  empirical validation, peer review, a scientific novelty finding, provenance
  discovery, deployment guidance, or a published artifact.
- The v14 artifact-content baseline remains commit `261c516`; later baseline
  HEAD `d0d26e2` adds only the historical v14 transfer guide. V15 supersedes
  v14 for owner review without deleting its audit history.
- The original v14 checkout contains an untracked `output/` directory. It is
  user-owned and will not be modified or removed.
- V15 work occurred in an isolated integration worktree. Three bounded review
  lanes returned advisory reports or patches from separate worktrees; the
  primary integrator dispositioned and integrated them.
- The exact recovered v13 PNG remains historical evidence, not current
  topology. Its SHA-256 is
  `8a8204a05e993e84f2bd9037c59b7beb2ab6b4bca89304e299f66b3961f203ae`.
  The archived rendered DOM is not the unavailable original standalone HTML.
- E2 remains an illustrative worked-example image. H1 remains archived by
  default because its aperture can imply a gatekeeper or one-way pipeline.
- Alpha Solver and Signal Foundry remain bounded design/implementation
  illustrations, not independent empirical validation.
- No study, model run, pilot, preregistration, participant contact, ethics/IRB
  determination, publication, deployment, push, PR, production mutation, or
  externally licensed dataset acquisition is authorized by this program.

### Baseline hashes

| Artifact | SHA-256 at baseline |
| --- | --- |
| `source/THOUGHT_PIECE_V14.md` | `52c78b94543b55b427531d783447fe4deef6e66a11acbaa070260083dd15227f` |
| `source/FRAMEWORK_COMPONENT_MAP.json` | `e35f28c3853d77add0dfc191993a393ddda65295adddca3c749d593b28fbef66` |
| `research/PAPER_PROSPECTUS_V0.md` | `2bb710764bca37be4500b0741783b98ecfb6ee0a66fa7131f43b8719b6e99d69` |
| `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V0.md` | `7d15a7a0c506292a560c975ec75eefe4f8f9922459080b5f5b8a08562704505e` |
| `exports/THOUGHT_PIECE_V14.pdf` | `c96b5f062fec5dd9a09b7a592dc88c915839a872bb172f1a621bdbb53d0612f7` |

### Historical first-reconciliation v15 hashes

These hashes record the historical v15 reconciliation inputs. Loop-1 edits are
authorized only with the recorded `MODIFY` disposition below and a new corrected
artifact hash; the historical values must not be presented as the final hashes
for amended files.

| Artifact | SHA-256 after first reconciliation |
| --- | --- |
| `research/PRIOR_ART_DELTA_V1.md` | `13bfd7760544a9cd5202ce5fb6a365b97c3c8a7b298eb2a47b690e479e2ea7f9` |
| `research/REAL_SYNDICATION_TRANSFER_FEASIBILITY_V1.md` | `75c70dbc0e5d530b5fc079688d787f3b5c0afbde4055ccf27c9fe46408035b14` |
| `research/F0_F1_F2_IMPLEMENTATION_READINESS_V1.md` | `ae6201edf715b626d2dd86a11b2b424351eb51e13eeb782fbdd8d2d891fb38d1` |
| `research/PAPER_PROSPECTUS_V1.md` | `cd51cb00143559000c3b84679614994dfc158507e1352d3a596720347ea8c8c9` |
| `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md` | `55320a95d078accde69bcede8852fcc0b0241c44dae545e81254b52019dee77a` |
| `reports/V15_EDITORIAL_AND_SITE_SYNTHESIS_BLUEPRINT.md` | `11f207e78011977ce7eccf925e4970285a069f9c5418c9cde741be2354d42421` |

### Loop-1 correction receipt

Recorded: 2026-08-18
Disposition: `MODIFY · LOOP1_EVIDENCE_NOVELTY_CORRECTIONS`

The loop-1 review identified one P1 reconciliation defect and five P2
documentation/terminology defects. The correction set adds the published
Zhang/Ives/Roth natural-language claim-provenance comparator, routes the full
S1–S19 status ledger and omitted retrieval comparators, clarifies supplied
benchmark relations versus inferred provenance, qualifies central reader
origin terminology, makes working-manuscript statuses explicit, removes stale
case-study ownership wording, and separates the Laitenberger source fact from
the project inference. It does not change F0/F1/F2, `A`, `M`, `FC_cons`, VOR,
calibration exclusion, T1, or the no-results boundary.

Corrected hashes for amended artifacts are recorded after the loop-1 edits in
the validation report `reports/V15_LOOP1_EVIDENCE_FIX_VALIDATION.md`. The
ledger’s own final hash is intentionally not listed here because this receipt
changes the ledger itself; package finalization must hash it after commit.

Current corrected artifact hashes at this receipt:

| Artifact | SHA-256 after loop-1 correction |
| --- | --- |
| `research/PRIOR_ART_DELTA_V1.md` | `3db0592bba071d3075a7694f1364545523f555af3c96f3122bf767489b4a1c66` |
| `source/THOUGHT_PIECE_V15.md` | `6d6149016cda9816785051cf6a07a5cbeb5c5740f321101ce1a0cf457ef4f7c3` |
| `research/PAPER_PROSPECTUS_V1.md` | `e88b79307200a11ef1c07f6541ba6e047985501e37769e06c59b5f9ac5bd4d34` |
| `site/app/content.ts` | `91213f679cc7ea1300fa85c05473b5568bd2d3cf87fbccd70c3da045aebb73fd` |
| `site/app/page.tsx` | `bdc9cbb24cfa5af3be27ca442c1639052ed4551483e20933459d6aeab1ae80d9` |
| `research/V15_CLAIM_SOURCE_ARTIFACT_MATRIX.md` | `2aa06b7ffa9c04d983eb6615fec162d4592e0b97095ff6737fafa20a1006cc73` |
| `reports/V15_LOOP1_EVIDENCE_NOVELTY_REVIEW.md` | `e0120c310c784f67160c2b62cfb834365a018ef6d225b4f2aa7c535cbadd2e88` |

## Owner-approved locked result commitment

**Decision: `ACCEPT · LOCKED`**

If the study is run, preserve and report a null, negative, harmful, unstable,
or shortcut-driven result. Do not hide an unfavorable result, change the
primary outcome after seeing it, rerun until it becomes favorable, or write the
paper as though only a positive result is publishable.

- **Null:** F2 does not meaningfully improve the primary outcome relative to
  F1.
- **Negative or harmful:** F2 worsens the primary outcome, recall, robustness,
  or another preregistered safety measure.
- **Shortcut-driven:** an apparent benefit is explained by labels, formatting,
  ordering, token differences, leakage, or another superficial cue rather than
  the intended origin-relation information.
- If F0/F1 improve but F2 does not beat F1, attribute the benefit to the
  explicit rule, not the typed relation field.
- If the effect disappears under noise, parity, position, or formatting
  controls, report the narrower interpretation.

This commitment does not authorize a model run, provider spend, publication,
preregistration, recruitment, or external/private data use.

## Task ledger

| ID | Deliverable or gate | Owner | Status | Evidence / next check |
| --- | --- | --- | --- | --- |
| T00 | Freeze v14 truth boundary and isolate worktrees | Primary integrator | `ACCEPT · COMPLETE` | Baseline commits/hashes above; four isolated worktrees created from `d0d26e2` |
| T01 | `research/PRIOR_ART_DELTA_V1.md` | Lane 1 | `ACCEPT · COMPLETE` | Reviewed and integrated with corrected Naphade attribution, Newswire authorship, current RAG adjacency, and a bounded residual claim |
| T02 | `research/REAL_SYNDICATION_TRANSFER_FEASIBILITY_V1.md` | Lane 2 | `ACCEPT · COMPLETE` | Reviewed and integrated as descriptive `T1`; no `F3`, model run, dataset download, or denominator change |
| T03 | `research/F0_F1_F2_IMPLEMENTATION_READINESS_V1.md` plus safe offline scaffolding | Lane 3 | `ACCEPT · COMPLETE` | Reviewed, repaired, and integrated; 12 focused tests, 18 parser fixtures, compile check, 16-bundle smoke, 480-bundle full generation, fixed 300/75 manifests, and reduced planning simulation pass offline; model/intended tokenizer remain unselected |
| T04 | Reconciled prospectus v1 and protocol v1 | Primary integrator | `ACCEPT · COMPLETE` | Canonical v1 files preserve F0/F1/F2, fixed denominators, descriptive T1, no calibration family, and open pre-run gates |
| T05 | V15 editorial/site synthesis blueprint | Primary integrator | `ACCEPT · COMPLETE` | Canonical blueprint now reflects all three lane dispositions and the Essay / Explore / Lab boundary |
| T06 | Canonical v15 manuscript and local reader | Primary integrator | `ACCEPT · COMPLETE` | `source/THOUGHT_PIECE_V15.md` and `site/`; Essay/Explore is separated from the explicitly unrun Lab, and the repaired reader passes lint, production build, five rendered-HTML tests, identifier/fragment checks, and no-results assertions |
| T07 | Improvement loop 1: evidence/novelty | Primary integrator + bounded review lanes | `ACCEPT · COMPLETE` | `reports/V15_LOOP1_EVIDENCE_NOVELTY_REVIEW.md`, corrected artifacts, and `reports/V15_LOOP1_EVIDENCE_FIX_VALIDATION.md`; no F0/F1/F2 expansion |
| T08 | Improvement loop 2: method/adversarial | Primary integrator + bounded review lanes | `ACCEPT · COMPLETE` | `reports/V15_LOOP2_METHOD_ADVERSARIAL_REVIEW.md` and `reports/V15_LOOP2_METHOD_FIX_VALIDATION.md`; all seven P1 and two P2 findings repaired and re-run offline; no protocol amendment |
| T09 | Improvement loop 3: reader/design/accessibility | Primary integrator + bounded review lanes | `ACCEPT · COMPLETE` | `reports/V15_LOOP3_READER_DESIGN_ACCESSIBILITY_REVIEW.md`, independent fix validation, and root live layout QA; three P1 and four P2 findings repaired; screenshot and live-zoom limitations disclosed |
| T10 | Visual/print PDF companion | Primary integrator | `ACCEPT · COMPLETE` | 20 A4 pages, explicitly untagged, SHA-256 `0542cdd14311fd07f7d9fa5e02c05584e83ed31d4d2cb07f305c5e3751254dca`; every final page rasterized and inspected; visual-QA attribution correction re-rendered and rechecked |
| T11 | Owner packet, transfer guide, manifest, checksums, ZIP | Primary integrator | `ACCEPT · COMPLETE` | Compact owner path and transfer guide complete; committed 101-file payload built into 103 ZIP members with 102 checksum entries; filesystem, archive, CRC, deterministic metadata, sidecar, and independently extracted-copy verification all pass |

## Decision log

| ID | Question | Disposition | Reason and consequence |
| --- | --- | --- | --- |
| D001 | What is the maximum current claim? | `ACCEPT` | V15 may improve the conceptual synthesis and experimental readiness; it may not imply a study result, provenance discovery, real-world independence, or validated mechanism. |
| D002 | Preserve the F0/F1/F2 causal core? | `ACCEPT` | The implementation audit found no estimand, denominator, condition, sample-size, or claim-boundary defect. F2-minus-F1 remains the primary supplied-cue contrast beyond the byte-identical F1 rule. |
| D003 | Add calibration to the confirmatory family? | `REJECT` | The current scalar confidence has no explicit calibrated target distribution or proper scoring rule. It remains descriptive unless separately specified. |
| D004 | Treat natural-syndication transfer as confirmatory or add F3? | `REJECT` | The feasibility audit found no public-data basis for extending the synthetic confirmatory or safety denominators. No transfer record enters `A`, `M`, the primary interval/test, or VOR. |
| D005 | Treat `independent_as_stipulated` as real-world epistemic independence? | `REJECT` | The label describes the synthetic benchmark graph only. |
| D006 | Use H1 in the v15 reader? | `DEFER_ARCHIVED_BY_DEFAULT` | Its visual topology can imply a one-way gatekeeper that the framework does not claim. |
| D007 | Replace the v13 map with current topology? | `REJECT` | Preserve it unchanged as historical origin; current topology remains deterministic live text/HTML. |
| D008 | Run a model, pilot, paid provider, or Cloud Run job during implementation? | `REJECT_OUT_OF_SCOPE` | Only deterministic offline scaffolding and simulation are authorized. |
| D009 | Publish, deploy, push, open a PR, or preregister? | `REJECT_OUT_OF_SCOPE` | Each requires a new explicit instruction for that exact external action. |
| D010 | Retain a real-syndication transfer artifact? | `ACCEPT_AS_DESCRIPTIVE_T1` | NEWS-COPY can support bounded same-original/dependent fixtures and Newswire can preserve aggregate recurrence context, but neither supplies real-world `INDP`, complete provenance, claim stance, or multiple-origin ground truth. Any future T1 remains separately named, rights-gated, descriptive, and outside all confirmatory/safety denominators. |
| D011 | Claim generic mechanism novelty for the discrimination layer? | `REJECT` | Copying-aware truth discovery, double-counting control, citation-network amplification, duplicate detection, set-wise/diversity retrieval, conflict-aware RAG, and source-dependence auditing all have direct precedents. Retain only the boundary-preserving synthesis and the narrow supplied-origin-cue versus rule-only hypothesis. |
| D012 | Add retrieval/deduplication/conflict-system arms to the locked F0/F1/F2 study? | `DEFER` | MMR, SetR, RAMDocs, EvidentialRAG, exact deduplication, and related systems are important adjacent or future comparators, but adding them would broaden the frozen F0/F1/F2 causal core without a demonstrated fatal defect. |
| D013 | Treat local surrogate-tokenizer parity as the primary parity lock? | `REJECT` | The scaffold requires exact F1/F2 bytes and local-surrogate tokens for development only. A future authorized study must separately prove exact per-bundle parity under the selected frozen model tokenizer before opening the primary split. |
| D014 | Interpret the current surface-only smoke probe as leakage clearance? | `REJECT` | The deterministic nearest-centroid check is diagnostic scaffolding, not the preregistered blocked classifier or an independent semantic audit. Its current small-corpus accuracy is not a readiness pass; the full surface-leakage gate remains unresolved. |
| D015 | Apply loop-1 evidence/novelty corrections? | `MODIFY` | Add S19 Zhang/Ives/Roth as published natural-language provenance prior art; expose MMR/NEST/RARE/Schelpe and exact statuses; replace central unqualified independence labels; qualify Li/EvidentialRAG/Naphade/Ross status; replace stale case-study ownership wording; split Laitenberger source fact from project inference. Preserve the locked F0/F1/F2 core and validate in `reports/V15_LOOP1_EVIDENCE_FIX_VALIDATION.md`. |
| D016 | Apply loop-2 method repairs or amend the estimand? | `MODIFY_IMPLEMENTATION_NO_PROTOCOL_AMENDMENT` | Repair all-`UNKN` stress semantics, fixed 300/75 manifest enforcement, payload-derived parity receipts, cross-record integrity checks, FC/VOR planning outputs, raw/run receipts, config identity, and non-authorizing leakage labels. These make the scaffold conform to protocol v1.0; F0/F1/F2, F2-minus-F1, all-assigned `FC_cons`, fixed-set VOR, T1, and the unfavorable-result lock remain unchanged. |
| D017 | Apply loop-3 reader and accessibility repairs? | `MODIFY` | Expose all eleven evidence-status labels before disclosure, use a two-tone focus treatment, make comparison tables print-safe, remove localhost social metadata, restore serif reading typography, compress the first fold, separate the worked application from the receipt, and load substantive images eagerly. Static, rendered-HTML, live-layout, and PDF checks pass with disclosed screenshot/live-zoom limitations. |
| D018 | Which framework map is canonical in v15? | `ACCEPT_CANONICAL_SYNTHESIS` | Freeze `source/FRAMEWORK_COMPONENT_MAP.json` as the v15 six-family/eleven-responsibility conceptual map. Preserve C01–C11, F1–F6, and D01–D08; D04 is `origin_relation`, while `independence` remains compatibility language only. Preserve the v13 PNG unchanged as historical origin rather than current topology. |
| D019 | Is the visual companion an accessible PDF? | `REJECT` | It is a polished 20-page visual/print companion but is not tagged. Every page visibly states that HTML is canonical and that no empirical results exist; the semantic HTML and Markdown remain the accessible reading surfaces. |
| D020 | Package the full repository history or a compact canonical release? | `ACCEPT_COMPACT_CANONICAL_RELEASE` | Seal the 101-file v15 payload plus manifest/checksums. Exclude dependencies, builds, caches, intermediate QA rasters, superseded v0/v14 final surfaces, old overnight memos, and unrelated review bundles. Preserve necessary v13 history, selected/rejected visual rationale, bounded cases, all v15 loop reports, canonical research artifacts, reproduction tools, and tests. |

## Disposition vocabulary

- `ACCEPT`: retain as stated.
- `MODIFY`: retain after a named correction with affected artifacts listed.
- `DEFER`: preserve as an open choice or later study; do not imply completion.
- `REJECT`: exclude from canonical v15, while retaining the reason in this
  ledger.

Every material research or editorial finding must receive one of these
dispositions before it can alter a canonical artifact.

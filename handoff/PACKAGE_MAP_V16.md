# Pattern Map v16 owner-review package map

Status: **CANONICAL LOCAL REVIEW MAP**

## Governing records

| Purpose | Canonical path |
| --- | --- |
| Locked owner intent | `docs/OWNER_INTENT_V16.md` + `docs/OWNER_INTENT_V16.sha256` |
| Thesis and audience | `docs/THESIS_AND_AUDIENCE_CONTRACT_V16.md` |
| Artifact firebreaks | `docs/ARTIFACT_BOUNDARIES.md`, `docs/TWO_PROJECT_SEPARATION.md` |
| Source authority and lineage | `docs/SOURCE_AUTHORITY_AND_LINEAGE.md`, `docs/MIGRATION_INVENTORY.md` |
| Acceptance and roadmap | `docs/V16_ACCEPTANCE_CRITERIA.md`, `docs/V16_ROADMAP.md` |
| Public/transfer hardening contract | `docs/PUBLIC_AND_TRANSFER_HARDENING_PLAN_V16.md` |
| Decisions and advisory dispositions | `docs/DECISION_LOG.md`, `docs/ADVISORY_REVIEW_DISPOSITIONS.md` |
| Claim control | `docs/CLAIMS_AND_SOURCE_LEDGER_V16.md` |
| Version status | `docs/VERSION_HISTORY.md` |

## Human-facing v16

| Artifact | Path | Role |
| --- | --- | --- |
| Canonical essay | `manuscript/PATTERN_RECOGNITION_V16.md` | Complete 10–15-minute thought piece estimate |
| Short version | `manuscript/NINETY_SECOND_VERSION.md` | Cumulative 60–90-second entry |
| Mentor cover note | `manuscript/MENTOR_COVER_NOTE.md` | Personal invitation to challenge/expand |
| Public abstract | `manuscript/PUBLIC_ABSTRACT.md` | Standalone concise description |
| Origin note | `manuscript/ORIGIN_NOTE.md` | Historical continuity and two-project split |
| Optional source route | `manuscript/SOURCES_AND_RESEARCH_ROUTE.md` | Targeted, non-exhaustive evidence/prior-art route |

## Builder-facing v16

| Artifact family | Paths |
| --- | --- |
| Six-family specification | `framework/SIX_FAMILIES.md`, `framework/SIX_FAMILIES.json`, `framework/SIX_FAMILIES.schema.json` |
| Relationship and terms | `framework/RELATIONSHIP_MAP.md`, `framework/GLOSSARY.md` |
| Operating choices | `framework/OPERATOR_PLAYBOOK.md`, `framework/IMPLEMENTATION_CHOICES.md`, `framework/BOUNDARIES_AND_FAILURES.md` |
| Mechanisms and templates | `framework/mechanisms/**`, `framework/templates/**` |
| Proportionate applied controls | `framework/templates/ORDINARY_RECORD.md`, `framework/templates/MEMORY_RECORD.md`, `qa/applied/PUBLIC_TRANSFER_APPLIED_INTEGRITY_QA_2026-08-30.md` |
| Signal Foundry | `cases/signal-foundry/README.md` |
| Neutral cases | `cases/general-research/README.md`, `cases/product-and-process/README.md` |

## Signal Foundry transfer

| Artifact | Path | Role |
| --- | --- | --- |
| Canonical Pattern Map handoff | `handoff/signal-foundry/PATTERN_MAP_V16_CANONICAL_HANDOFF.md` | Exact source-of-truth hierarchy, six-family translation, smallest schema seam, unsupported-request refusals, and orphan recovery |
| Copyable integration brief | `handoff/signal-foundry/SIGNAL_FOUNDRY_INTEGRATION_BRIEF.md` | Tired-owner fast path, design-only offline fixture plan, exact checkpoints, and safe Claude Code prompt |
| Portable bundle builder | `handoff/signal-foundry/build_portable_bundle.py` | Deterministic exact-commit ZIP, START_HERE, manifest, verifier, sidecar, all-payload safety, explicit operating-input selection, and machine-classified out-of-packet link contract |
| Post-Ultracode finalization QA | `qa/handoff/POST_ULTRACODE_FINALIZATION_QA_2026-08-28.md` | Independent dispositions, reusable-framework contracts, fresh-clone portability, and explicit deferred/manual work |

## Agent-facing v16

| Artifact | Path |
| --- | --- |
| Quickstart | `framework/agent-playbook/QUICKSTART.md` |
| Full guide | `framework/agent-playbook/FULL_OPERATING_GUIDE.md` |
| Copyable brief | `framework/agent-playbook/COPYABLE_AGENT_BRIEF.md` |
| Preflight | `framework/agent-playbook/PREFLIGHT_CHECKLIST.md` |
| Decision receipt | `framework/agent-playbook/DECISION_RECEIPT_TEMPLATE.md` |
| Ordinary-versus-layered examples | `framework/agent-playbook/ORDINARY_VS_DISCRIMINATION_LAYER.md` |

## Local reader surface

| Artifact | Path | Boundary |
| --- | --- | --- |
| Shared site source/build | `site/build.mjs`, `site/src/**`, `site/check.mjs` | Dependency-free authored ten-route source with review/public adapters; continuous Guided read, line-free current Map, contextual term helpers, planning-only Apply, and fail-closed publication metadata; no hosting |
| Apply recommendation model | `site/src/recommendation.js`, `qa/interaction/apply-state-contract.spec.mjs` | Pure 108-combination Stage 0/consequence/uncertainty/budget/permission contract; never records actual events from planning inputs |
| Map, term, and reader regressions | `qa/interaction/map-layout-contract.spec.mjs`, `qa/interaction/term-popover-geometry-contract.spec.mjs`, `qa/content/reader-language-contract.spec.mjs` | Narrow/medium/wide Map contract, measured desktop term-panel clearance/viewport clamp, and cumulative-entry/plain-language contract |
| Standalone HTML | `site/exports/standalone/pattern-map-v16.html` | Semantic direct-open ten-section review companion; one rail/guide/frame and no false current route |
| Public-preview standalone | `site/exports/standalone/pattern-map-v16-public.html` | Prose-first direct-open ten-section public adapter; no review/package chrome; local `noindex,nofollow` candidate only |
| PDF companion | `site/exports/pattern-map-v16-owner-review.pdf` | Untagged visual companion; not the accessibility route |
| Site implementation QA | `qa/site/SITE_QA_REPORT.md`, `qa/site/audit_site.py` | Structural/accessibility proxy only |
| Current-head live browser boundary | `qa/site/LIVE_BROWSER_BOUNDARY_CHECK_2026-08-19_79a2392.md` | Pointer/focus/state evidence; physical keyboard/screen-reader/print remain manual |
| Current Pro correction QA | `qa/site/PRO_ROUND_2_CORRECTION_QA_2026-08-22_c889260.md`, `qa/site/advisory/CHATGPT_PRO_INDEPENDENT_REVIEW_ROUND_2_2026-08-22_4d2505e.md` | Round 2 exact review/correction, 108-case Stage 0 contract, mobile/medium live viewports, transparent P2 dispositions, and current manual residuals |
| Owner visual/export closeout | `qa/site/OWNER_VISUAL_EXPORT_CLOSEOUT_2026-08-23.md` | Traces the attached export failure to a real standalone-markup defect, records its structural repair, and verifies the flow-native recurrence visual, term-helper containment, and print-width safeguards |
| Terminal finalization QA | `qa/site/TERMINAL_FINALIZATION_QA_2026-08-27.md`, `qa/site/advisory/CLAUDE_TERMINAL_AUDIT_2026-08-27_e565502.md` | Exact-baseline independent audits, accepted desktop term-panel correction, deferred focus/touch/taste items, package closeout, and honest synthetic-browser limits |
| Public presentation QA | `qa/site/PUBLIC_MODE_BROWSER_QA_2026-08-30.md`, `qa/site/public-mode-contract.spec.mjs`, `qa/visual/public-mode/**` | Shared-source parity, prose-first viewports, deterministic reveal, Stage 0 applicability, responsive captures, and fail-closed release contract; physical/manual gates remain open |
| Final site hygiene | `qa/site/SITE_HYGIENE_QA_2026-08-23_d4b7b9e.md`, `qa/visual/verify_image_formats.py` | Stale-selector removal, truthful current image signatures, immutable archive exceptions, and human-first standalone regression |
| Prior Pro correction QA | `qa/site/PRO_ROUND_1_CORRECTION_QA_2026-08-20_5eb860e.md`, `qa/site/advisory/CHATGPT_PRO_INDEPENDENT_REVIEW_2026-08-20_cc5547d.md` | Round 1 exact review history; superseded for the current Apply matrix and term/mobile behavior |
| Historical site-polish QA | `qa/site/SITE_POLISH_QA.md`, `qa/site/advisory/SITE_VISUAL_EXPERIENCE_POST_POLISH_2026-08-19_a319794.md` | Earlier `a319794` design checkpoint; superseded for current Map/Apply semantics |
| Visual QA | `qa/visual/POLISH_PLAN.md`, `qa/visual/VISUAL_QA_REPORT.md`, `qa/visual/VISUAL_EXPERIENCE_REVISION_REPORT.md`, historical routed-site screenshots, current PDF renders | Design history and bounded rendered evidence; `qa/visual/README.md` distinguishes current from superseded captures |
| Image decision/use records | `qa/visual/VISUAL_NEEDS.md`, `assets/IMAGE_USE_LEDGER.md` | No generated bitmap candidates |

## The Echo Problem / ECHO-01

| Artifact | Path |
| --- | --- |
| EP identity | `research/the-echo-problem/README.md` |
| Status/no-results | `research/the-echo-problem/STATUS_AND_BOUNDARIES.md` |
| Relationship to v16 | `research/the-echo-problem/RELATION_TO_V16.md` |
| EP version history | `research/the-echo-problem/VERSION_HISTORY.md` |
| Future low/no-cost plan | `research/the-echo-problem/FUTURE_EXECUTION_PLAN.md` |
| EP v1.1 design checkpoint | `research/the-echo-problem/v1_1/README.md`, `research/the-echo-problem/v1_1/PROTOCOL_V1_1_DESIGN_CHECKPOINT.md` |
| Targeted prior-measurement route | `research/the-echo-problem/v1_1/PRIOR_MEASUREMENT_MATRIX.md` |
| Provider-free v1.1 harness and frozen render fixture | `research/the-echo-problem/v1_1/harness/**`, `research/the-echo-problem/v1_1/fixtures/CLAUDE_PRIMARY_RENDER_AUDIT_SEED1_N300.json` |
| Preserved v15.2 map | `research/the-echo-problem/PRESERVED_V15_2_INDEX.md` |
| Curated source checkpoint | `research/the-echo-problem/preserved/v15.2/**` |
| Complete accession | `archive/transfers/v15.2-owner-handoff/**` |
| EP QA | `research/the-echo-problem/qa/**`, `qa/research/ECHO_V1_1_DESIGN_CHECKPOINT_QA_2026-08-23.md` |

## Broader unrun research agenda

| Artifact | Path |
| --- | --- |
| Research boundary/index | `research/README.md` |
| Broader agenda | `research/THE_DISCRIMINATION_LAYER_RESEARCH_AGENDA.md` |
| Matched-budget protocol candidate | `research/future-studies/DL_PLAYBOOK_MATCHED_BUDGET_PROTOCOL_V0_1.md` |
| Narrow-wedge decision memo | `research/future-studies/DL_NARROW_WEDGE_DECISION_MEMO_V0_1.md` |
| Current adjacent-source and boundary QA | `qa/research/CURRENT_ADJACENT_SOURCE_VERIFICATION_2026-08-30.md`, `qa/research/RESEARCH_BOUNDARY_HARDENING_QA_2026-08-30.md` |
| Research QA | `qa/research/**` |

## Historical archive

| Checkpoint | Path / verifier |
| --- | --- |
| Complete v14 transfer | `archive/transfers/v14-complete-2026-08-18/**`; original 429-file SHA-256 ledger |
| Complete extracted v15.2 accession | `archive/transfers/v15.2-owner-handoff/**`; `verify_accession.py` |
| Curated v13/v14/v15/v15.1/v15.2 indexes | `archive/v13/`, `archive/v14/`, `archive/v15/`, `archive/v15.1/`, `archive/v15.2/` |
| Cross-version anchor verifier | `archive/CHECKPOINT_INDEX.json`, `archive/verify_checkpoint_index.py` |

## Final review and integrity

| Artifact | Path |
| --- | --- |
| Acceptance matrix | `qa/FINAL_ACCEPTANCE_MATRIX_V16.md` |
| External-action audit | `qa/FINAL_ACTION_AUDIT_V16.md` |
| Complete local verification runner | `qa/run_owner_review_checks.sh` |
| Portable-bundle regression | `qa/handoff/test_portable_bundle.py` |
| Public/transfer convergence QA | `qa/handoff/PUBLIC_AND_TRANSFER_HARDENING_QA_2026-08-30.md` |
| Exact-checkpoint Claude sealing audit | `qa/handoff/advisory/CLAUDE_PUBLIC_TRANSFER_TERMINAL_AUDIT_2026-08-30_fb7d808.md` |
| Exact-checkpoint Claude terminal recheck | `qa/handoff/advisory/CLAUDE_PUBLIC_TRANSFER_TERMINAL_RECHECK_2026-08-30_4a1acab.md` |
| Post-Ultracode finalization | `qa/handoff/POST_ULTRACODE_FINALIZATION_QA_2026-08-28.md` |
| Advisory ledger | `docs/ADVISORY_REVIEW_DISPOSITIONS.md` |
| Owner packet | `handoff/OWNER_REVIEW_PACKET_V16.md` |
| Branch/PR state | `handoff/BRANCH_AND_PR_STATE.md` |
| Checksum manifest | `handoff/OWNER_REVIEW_MANIFEST_V16.json` |
| Manifest verifier | `handoff/verify_owner_review_package.py` |

Historical archives remain immutable. Generated site output under `site/dist/`
and caches/dependency directories are not package artifacts and are not
tracked.

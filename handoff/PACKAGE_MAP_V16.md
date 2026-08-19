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
| Signal Foundry | `cases/signal-foundry/README.md` |
| Neutral cases | `cases/general-research/README.md`, `cases/product-and-process/README.md` |

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
| Site source/build | `site/build.mjs`, `site/src/**`, `site/check.mjs` | Dependency-free local build; no hosting |
| Standalone HTML | `site/exports/standalone/pattern-map-v16.html` | Semantic direct-open review route |
| PDF companion | `site/exports/pattern-map-v16-owner-review.pdf` | Untagged visual companion; not the accessibility route |
| Site implementation QA | `qa/site/SITE_QA_REPORT.md`, `qa/site/audit_site.py` | Structural/accessibility proxy only |
| Visual QA | `qa/visual/VISUAL_QA_REPORT.md`, screenshots, PDF renders | Layout evidence only |
| Image decision/use records | `qa/visual/VISUAL_NEEDS.md`, `assets/IMAGE_USE_LEDGER.md` | No generated bitmap candidates |

## The Echo Problem / ECHO-01

| Artifact | Path |
| --- | --- |
| EP identity | `research/the-echo-problem/README.md` |
| Status/no-results | `research/the-echo-problem/STATUS_AND_BOUNDARIES.md` |
| Relationship to v16 | `research/the-echo-problem/RELATION_TO_V16.md` |
| EP version history | `research/the-echo-problem/VERSION_HISTORY.md` |
| Future low/no-cost plan | `research/the-echo-problem/FUTURE_EXECUTION_PLAN.md` |
| Preserved v15.2 map | `research/the-echo-problem/PRESERVED_V15_2_INDEX.md` |
| Curated source checkpoint | `research/the-echo-problem/preserved/v15.2/**` |
| Complete accession | `archive/transfers/v15.2-owner-handoff/**` |
| EP QA | `research/the-echo-problem/qa/**` |

## Broader unrun research agenda

| Artifact | Path |
| --- | --- |
| Research boundary/index | `research/README.md` |
| Broader agenda | `research/THE_DISCRIMINATION_LAYER_RESEARCH_AGENDA.md` |
| Matched-budget protocol candidate | `research/future-studies/DL_PLAYBOOK_MATCHED_BUDGET_PROTOCOL_V0_1.md` |
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
| Advisory ledger | `docs/ADVISORY_REVIEW_DISPOSITIONS.md` |
| Owner packet | `handoff/OWNER_REVIEW_PACKET_V16.md` |
| Branch/PR state | `handoff/BRANCH_AND_PR_STATE.md` |
| Checksum manifest | `handoff/OWNER_REVIEW_MANIFEST_V16.json` |
| Manifest verifier | `handoff/verify_owner_review_package.py` |

Historical archives remain immutable. Generated site output under `site/dist/`
and caches/dependency directories are not package artifacts and are not
tracked.

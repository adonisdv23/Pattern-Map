# Claims and evidence register

Status: current v14 drafting register. Historical rows are based on the complete owner-designated live v13 reference and the hash-verified original diagram; exact standalone-HTML comparison remains pending. The CSV is the row-complete machine-readable counterpart.

## Type legend

- `OWNER_PREMISE`: supplied intent or proposition; not external evidence.
- `HISTORICAL_V13_CLAIM`: faithfully recovered historical proposition; its presence is supported, its truth is not implied.
- `CONCEPTUAL_SYNTHESIS`: a distinction or integration derived from multiple sources.
- `PRIMARY_SOURCE_SUPPORTED`: bounded claim directly supported by a paper, standard, or official source.
- `CASE_DERIVED`: bounded observation from a named project artifact.
- `DESIGN_HYPOTHESIS`: proposed architecture or terminology choice requiring evaluation.
- `EMPIRICAL_HYPOTHESIS`: measurable prediction not yet tested here.
- `UNVERIFIED`: currently lacks sufficient support.
- `REJECTED_OR_NARROWED`: stronger wording rejected in favor of a bounded claim.

## Current high-level disposition

| Claim ID | Short claim | Type | Disposition |
| --- | --- | --- | --- |
| C-001 | An explicit discrimination responsibility before generation may be useful. | OWNER_PREMISE / DESIGN_HYPOTHESIS | Retain as provisional thesis, not conclusion. |
| C-002 | Search and enrichment have costs and stopping trade-offs. | PRIMARY_SOURCE_SUPPORTED | Retain, scoped to decision-theoretic and foraging models. |
| C-003 | Relevance can be updated from feedback. | PRIMARY_SOURCE_SUPPORTED | Retain; do not equate relevance with truth. |
| C-004 | Source assessment and content assessment are distinct. | PRIMARY_SOURCE_SUPPORTED | Retain. |
| C-005 | Atomic claims can have different support states within one answer. | PRIMARY_SOURCE_SUPPORTED | Retain. |
| C-006 | Provenance is not factual correctness. | CONCEPTUAL_SYNTHESIS | Retain as a central boundary. |
| C-007 | Recurrence is not independence. | PRIMARY_SOURCE_SUPPORTED / CONCEPTUAL_SYNTHESIS | Retain; common origin may remain unknown. |
| C-008 | A first-party source can support a narrow first-party claim without proving broader effectiveness. | CONCEPTUAL_SYNTHESIS | Retain as a central boundary. |
| C-009 | Attention priority is not a factual conclusion. | CONCEPTUAL_SYNTHESIS | Retain as a central boundary. |
| C-010 | Larger context does not guarantee uniform model use. | PRIMARY_SOURCE_SUPPORTED | Retain, model/task scoped. |
| C-011 | RAG is established prior art for retrieved external context. | PRIMARY_SOURCE_SUPPORTED | Use to reject generic retrieval novelty claims. |
| C-012 | Source-aware RAG and context attribution already exist. | PRIMARY_SOURCE_SUPPORTED | Use to reject generic source-awareness novelty claims. |
| C-013 | Agent-memory mechanisms already exist. | PRIMARY_SOURCE_SUPPORTED | Use to reject generic memory novelty claims. |
| C-014 | Mixed initiative requires explicit uncertainty, timing, correction, and control. | PRIMARY_SOURCE_SUPPORTED | Retain, bounded to design guidance. |
| C-015 | Confidence should be evaluated against observed correctness. | PRIMARY_SOURCE_SUPPORTED | Retain; do not equate calibration with authority or utility. |
| C-016 | Copying or coordination can manufacture recurrence. | PRIMARY_SOURCE_SUPPORTED | Retain as a risk, not a default accusation. |
| C-017 | Signal Foundry can illustrate bounded evidence responsibilities. | CASE_DERIVED | Retain as a bounded case, not validation. |
| C-018 | Alpha Solver can illustrate bounded reasoning and routing responsibilities. | CASE_DERIVED | Retain as a bounded case, not validation. |
| C-019 | Alpha Solver or Signal Foundry validates the full framework. | REJECTED_OR_NARROWED | Reject. |
| C-020 | The framework is enterprise-ready or validated. | UNVERIFIED | Reject currently. |
| C-021 | Separating the judgment dimensions improves decisions. | EMPIRICAL_HYPOTHESIS | Open test required. |
| C-022 | `Discrimination layer` communicates the intended meaning. | DESIGN_HYPOTHESIS | Keep provisionally with an explicit definition and reader test. |
| C-039 | The project introduces a novel universal pre-generation layer. | REJECTED_OR_NARROWED | Reject as a scientific contribution; current integrated RAG, conflict, provenance, evidence-interface, and decision-support systems cover overlapping responsibility surfaces. |
| C-040 | Supplied origin-relation metadata reduces false corroboration beyond the same explicit rule. | EMPIRICAL_HYPOTHESIS | This is the single proposed first-paper estimand; no result exists. |
| C-041 | A positive F2-versus-F1 result would show provenance discovery, internal reasoning, or real-world independence. | REJECTED_OR_NARROWED | Reject. F2 supplies an oracle origin-relation field on fictional graphs; the experiment can identify only an observable condition effect for one frozen model. |
| C-042 | Derivation, origin-family, claim-stance, and action relations can share one generic relation label. | REJECTED_OR_NARROWED | Reject. Keep the four vocabularies distinct in the benchmark, interface, and later policy work. |

## Historical v13 disposition

| Claim ID | Historical idea | Current disposition |
| --- | --- | --- |
| C-023 | The leverage is in pattern recognition and discrimination applied before generation. | Preserve as historical thesis; test as a design hypothesis. |
| C-024 | Peripheral does not mean true. | Preserve and strengthen with typed evidence and authorization boundaries. |
| C-025 | Six historical mechanism families. | Preserve the visual lineage; redesign the v14 responsibility map. |
| C-026 | Cross-ecosystem recurrence is stronger evidence. | Narrow: recurrence still requires common-origin analysis and an `UNKNOWN` independence state. |
| C-027 | Source track-record weighting. | Retain as a domain-, claim-, and time-scoped hypothesis; split authority from support. |
| C-028 | Velocity is an early signal. | Retain only as an attention hypothesis based on repeated observations and a baseline. |
| C-029 | Absence can be detected against expectation. | Retain with typed gaps and an explicit observation boundary. |
| C-030 | Peer-set normalization can surface target gaps. | Retain as a domain-specific comparison pattern; do not infer causality. |
| C-031 | Structured longitudinal memory. | Retain as a historical requirement, with prior-art attribution and provenance/retention controls. |
| C-032 | Outcomes should update weights and frames. | Retain as design and empirical hypothesis with predefined outcomes and approved updates. |
| C-033 | Process, reasoning-layer, and custom-model paths. | Preserve as illustrative paths, not an exhaustive hierarchy. |
| C-034 | Standard operating discipline is the novelty. | Reject as a current novelty fact; retain as the author's motivation. |
| C-035 | Encoding decomposable expertise can raise non-expert output to expert grade. | Narrow to a bounded evidence-handling hypothesis. |
| C-036 | Default GPT cannot perform the named mechanisms. | Reject blanket capability claims; evaluate named configurations. |
| C-037 | Orders-of-magnitude adoption and unusually fast model commoditization. | Remove from the core argument unless independently measured. |
| C-038 | V13 works at a narrow mobile viewport. | Rejected by direct visual inspection; redesign and retest v14. |

## Remaining exact-source merge

If the standalone v13 files or migration packet arrive, compare every historical row with the exact bytes and add locations or divergences. Do not silently reclassify later product language as historical owner intent.

# Research expansion and integration report

Recorded: 2026-08-18  
Status: `FOUR_BOUNDED_RESEARCH_PASSES_INTEGRATED_NO_STUDY_RUN`

## Outcome

Three independent Luna Max research lanes completed an initial pass and three
additional critique/expansion/build loops. The result is not a research paper
and is not evidence that the discrimination layer works. It is a substantially
more research-ready local package: the broad framework claim is narrowed, the
first feasible experiment has a frozen estimand and safety rule, the data and
scoring contract is more reproducible, and a separate formative reader study
now tests the visual explanation without confusing comprehension with model
performance.

No participants were recruited or contacted. No model benchmark, pilot,
preregistration, ethics submission, publication, deployment, or external data
collection occurred.

## The four passes

| Pass | Independent lanes | Main contribution | Integrated consequence |
| --- | --- | --- | --- |
| Initial research | Theory/prior art; empirical design; opportunities/visuals | Located the framework among provenance, evidence synthesis, RAG, information foraging, claim verification, mixed initiative, memory, and decision support; proposed falsifiable study families; identified possible visual and product opportunities. | The work is framed as a boundary-preserving synthesis and research agenda, not a novel mechanism family. |
| Loop 1 — adversarial red team | Theory; empirical design; reader/visual | Challenged novelty, construct collapse, hidden denominator choices, unsupported causal language, and pipeline/gatekeeper imagery. | Claims were narrowed; origin relation was separated from real-world epistemic independence; the first visual candidate became conditional. |
| Loop 2 — specification expansion | Current literature; operationalization; interface | Added recent source-attribution and matched-condition precedents; specified schemas, predicates, assignment rules, scoring, release manifests, and a deterministic receipt; designed a concrete comprehension surface. | The site gained the origin-accounting receipt; the study acquired a machine-auditable data/scoring contract and stronger comparators. |
| Loop 3 — pre-handoff audit | ML/NLP; HCI/ethics; reader/design | Found remaining estimand, denominator, multiplicity, versioning, accessibility, visual-topology, and stale-artifact defects. | The protocol/specification moved to v0.3; the prospectus moved to v0.4; H1 was omitted from final rendering; the PDF and responsive QA packet were regenerated. |

## Integrated first-paper direction

The narrowest credible first paper is now titled:

> **Oracle Origin-Relation Metadata in One Frozen Model: A Controlled
> False-Corroboration Benchmark**

The proposed experiment compares citation-only, rule-only, and byte-identical
rule-plus-oracle-metadata conditions under exact prompt/token controls. The
confirmatory comparison is within the same evidence bundle; the protocol does
not claim that different origin structures can be made exact textual matched
pairs.

The proposed primary estimand is the difference between the all-assigned,
risk-coded F2 and F1 false-corroboration rates. The proposed safety check is
fixed-set stipulated-support recall with a one-sided 95% lower confidence bound
above the frozen `-0.05` non-inferiority margin. The earlier `-0.08` value is
retained only as a planning scenario, not a success rule. Other condition,
domain, structure, stress, seed, and optional-model slices remain descriptive or
exploratory in this first protocol; there is no secondary Holm family.

This design estimates an observable condition effect. It does not establish
that a model internally used the metadata, discovered provenance, reasoned in a
particular way, benefited a human decision, or validated the full framework.

## Operational and governance improvements

- Raw outputs, parsed fields, assignment status, closed error enums, and release
  artifacts are explicitly separated.
- The predicate grammar and render map are deterministic and require
  round-trip tests.
- `DEPENDENT`, `INDEPENDENT_AS_STIPULATED`, and `UNKNOWN` remain distinct;
  unknowns are never silently reassigned.
- Gold origin relation and claim support/refutation semantics are separate.
- The false-corroboration primary uses all assigned units under the frozen
  conservative coding rule; observed-only and complete-case forms are
  sensitivity analyses, not replacement denominators.
- Model-assisted grading cannot silently adjudicate its own errors; the
  protocol specifies blinded human adjudication and agreement gates.
- Canonicalization, hashes, environment/model identifiers, privacy/licensing,
  release manifests, and post-lock change control are recorded before a run.
- Deterministic metadata-only and field-only diagnostics distinguish a broken
  treatment channel from a null model result.

## Separate formative reader study

`research/FORMATIVE_READER_STUDY_PROTOCOL_V0.md` defines an eight-participant,
four-condition, 4×4 Latin-square formative comparison of the receipt and image
roles. It tests whether readers can distinguish observations, known origin
clusters, counted supporting origins, and a human `HOLD` disposition; whether
they misread v13 as the current map; and whether H1 causes pipeline, truth-filter,
or gatekeeper interpretations.

This study is explicitly formative. Eight participants cannot support
population-level accessibility, terminology-safety, or efficacy claims. The
appropriate ethics or exemption determination, recruitment plan, consent,
privacy handling, compensation, and accessibility accommodations must be in
place before any contact with participants.

## Visual and product opportunities retained

- The deterministic origin-accounting receipt is the strongest immediate
  artifact opportunity because it is inspectable without generated imagery.
- The E2 “nine mentions, one origin” illustration remains a bounded editorial
  aid, not a dataset, topology, or result.
- The original v13 DALL-E-created map remains unchanged as the historical
  anchor, with its seven-step strip transcribed into live text.
- The H1 evidence-aperture image remains in the design archive but was removed
  from the final site/PDF because its topology can imply a one-way gatekeeper.
- A new social card was generated once through the current OpenAI/ChatGPT image
  route and used only as share-preview art. The interface exposed no exact model
  name, so no legacy DALL-E model is inferred.
- Longer-term opportunities include an origin-relation benchmark, receipt
  schema/validator, reviewer interface, and provenance-aware evaluation kit.
  None is presented as validated product-market evidence.

## Research artifacts

### Canonical integrated package

- `research/PAPER_PROSPECTUS_V0.md` — integrated prospectus v0.4.
- `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V0.md` — protocol v0.3.
- `research/FORMATIVE_READER_STUDY_PROTOCOL_V0.md` — formative HCI protocol.
- `research/overnight/rounds/08_LOOP2_OPERATIONALIZATION_SPEC.md` — consolidated
  operationalization/specification v0.3.
- `research/REFERENCES.md` and `research/references.bib` — reconciled bibliography.

### Independent research and review memos

1. `research/overnight/01_THEORY_AND_PRIOR_ART_LUNA_MAX.md`
2. `research/overnight/02_EMPIRICAL_RESEARCH_DESIGN_LUNA_MAX.md`
3. `research/overnight/03_NEW_INSIGHTS_AND_VISUAL_OPPORTUNITIES_LUNA_MAX.md`
4. `research/overnight/rounds/04_LOOP1_THEORY_RED_TEAM.md`
5. `research/overnight/rounds/05_LOOP1_EMPIRICAL_RED_TEAM.md`
6. `research/overnight/rounds/06_LOOP1_VISUAL_READER_RED_TEAM.md`
7. `research/overnight/rounds/07_LOOP2_CURRENT_LITERATURE_EXPANSION.md`
8. `research/overnight/rounds/08_LOOP2_OPERATIONALIZATION_SPEC.md`
9. `research/overnight/rounds/09_LOOP2_OPPORTUNITY_AND_INTERFACE_SPEC.md`
10. `research/overnight/rounds/10_LOOP3_ML_NLP_REVIEW.md`
11. `research/overnight/rounds/11_LOOP3_HCI_ETHICS_REVIEW.md`
12. `research/overnight/rounds/12_LOOP3_READER_DESIGN_REVIEW.md`

The memos are advisory work products. Historical observations in earlier memos
may be superseded by later integration notes and do not override the canonical
protocol, source, site, or final QA records.

## Gates before this can become a proper research paper

1. Freeze the contribution type, protocol/specification pair, corpus license,
   benchmark generator, model snapshot, prompts, token accounting, schemas,
   adjudication manual, and release manifest.
2. Implement the generator, validators, scorers, deterministic diagnostics, and
   audit bundle; exercise them with synthetic fixtures before any feasibility
   run.
3. Complete the ethics/exemption, privacy, licensing, consent, compensation, and
   accessibility decisions appropriate to each human or model study.
4. Run a feasibility-only pilot that cannot leak into the primary analysis;
   freeze exclusions and perform the preregistered simulation/power update.
5. Preregister the final primary and safety rules before examining primary
   outcomes.
6. Run the locked benchmark and blinded adjudication, publish nulls and harms,
   and distinguish confirmatory, sensitivity, and exploratory results.
7. Seek independent replication or a new domain/model test before generalizing
   beyond the frozen benchmark.

Until those gates are met, the correct description is **research-ready design
package**, not research paper, empirical result, validated framework, or
scientific novelty claim.

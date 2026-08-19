# Loop 3: Final independent ML/NLP/IR peer review

**Prepared:** 2026-08-18
**Scope:** final review of the integrated v14 thought-piece, first-paper prospectus, origin-accounting protocol, prior-art map, references, Loop 2 literature and operationalization reports, and the current public site source.
**Review status:** no study was run; no publication, deployment, or site mutation was performed.
**Literature cutoff:** 2026-08-18, inclusive.

## Conventions used in this review

- **[S] Sourced evidence:** a bibliographic fact, method, result, limitation, or status stated in a linked paper, standard, official record, or repository file.
- **[I] Inference:** a conclusion from comparing the sources and the project package.
- **[H] Hypothesis/design proposal:** an untested contribution or expected effect.
- **[DJ] Editorial judgment:** a recommendation about terminology, title, structure, or review risk.

This is a targeted peer-review audit, not a systematic review, patentability opinion, or claim that the search established an exhaustive absence of prior work.

## Answer-first verdict

**Verdict: REVISE before preregistration or manuscript submission.** The integrated package is now intellectually honest about the central novelty problem: the broad “Pattern Recognition / The Discrimination Layer” architecture should not be presented as a new scientific layer, mechanism, or universal pre-generation stack. That broad claim should be **rejected as a paper contribution** and retained only as historical/editorial framing and a research agenda. The public site can keep the historical title because it visibly labels itself a provisional thought piece, but the first scientific artifact needs a functional title and a stronger oracle/frozen-model qualifier.

The narrow F2-versus-F1 idea is viable as a **conditional, frozen-model behavioral diagnostic**. The protocol correctly defines the headline quantity as

`Delta_FC = P(false corroboration | F2 typed cue) - P(false corroboration | F1 rule only)`

with a bundle as the unit, F0 as secondary, and valid-origin recall as a safety/non-inferiority endpoint. It does not yet earn an accept decision because five issues remain material:

1. The prospectus still says to “Generate matched pairs in which only origin structure changes,” while the operationalization specification correctly says that exact cross-structure counterfactual matching is incoherent for several structures. The only confirmatory pair should be F2 versus F1 **within the same bundle**.
2. The protocol’s permitted-result sentence says the model “used” metadata. That wording implies an internal mechanism. The experiment can identify an observable condition effect, not internal cue use, provenance reasoning, or a causal cognitive process.
3. The directly countable F2 relation codes create a plausible field-reading shortcut. A deterministic metadata-only counter/field-only diagnostic must be added before primary lock so a model result is not mistaken for reasoning or semantic integration.
4. The scientific package is mostly careful, but the thought-piece and public receipt still use unqualified “independent,” “independence,” and “independent test” in places where the only defensible construct is a stipulated origin relation. These phrases invite a real-world epistemic-independence reading that the protocol explicitly disclaims.
5. The bibliography is not yet synchronized: the closest current source-attribution comparator, Nematov et al. (2025), appears in `REFERENCES.md` but not `references.bib` or the Loop 2 matrix; A-Mem and the Sabouhi working artifact have similar status/alignment gaps; PaperTrail’s canonical DOI is absent from the Markdown reference list.

Subject to those corrections, I would **conditionally accept the narrow study as a preregistration candidate**, not as evidence for the larger layer. A null, harmful, formatting-only, noise-fragile, or deterministic-baseline-matched result should be publishable only as a boundary/diagnostic result and should retire the typed-cue novelty claim.

## Review protocol and package status

I read the following current files:

- `source/THOUGHT_PIECE_V14.md`;
- `research/PAPER_PROSPECTUS_V0.md`;
- `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V0.md`;
- `research/PRIOR_ART_AND_ADJACENT_FIELDS_MAP.md`;
- `research/REFERENCES.md` and `research/references.bib`;
- `research/CLAIMS_AND_EVIDENCE_REGISTER.md`;
- `research/OVERCLAIM_AND_COUNTERARGUMENT_REGISTER.md`;
- `research/RESEARCH_PAPER_READINESS_PATH.md`;
- `research/overnight/rounds/07_LOOP2_CURRENT_LITERATURE_EXPANSION.md`;
- `research/overnight/rounds/08_LOOP2_OPERATIONALIZATION_SPEC.md`;
- `research/overnight/rounds/09_LOOP2_OPPORTUNITY_AND_INTERFACE_SPEC.md`;
- `site/app/page.tsx` and `site/app/content.ts`.

The search emphasis was 2024–2026 ML/NLP/IR, RAG, provenance, source attribution, evidence utilization, agent memory, and human/source-bias work, using ACL Anthology, official conference/proceedings records, W3C, publisher pages, arXiv records, and official author artifacts where necessary. Preprints and working manuscripts are treated as **preprints/working artifacts**, not peer-reviewed evidence. The Loop 2 search correctly warns that “we did not locate a peer-reviewed study isolating this exact contrast in the searched sources” is supportable, whereas “we are the first” is not.

## What passes the final novelty audit

| Review question | Verdict | Evidence and remaining boundary |
|---|---|---|
| Has broad architecture novelty been retired? | **Yes, in the core claim registers and central prose.** | The thought piece says it does not claim an unoccupied universal layer and lists “no claim of mechanism novelty.” The prospectus calls the first paper a single cue-use study, the prior-art map says the thesis is not clean sheet, Loop 2 rejects the broad layer as a novelty claim, and the site labels the synthesis conceptual and unvalidated. Keep those dispositions synchronized in every abstract/title. |
| Is F2 versus F1 isolated? | **Yes, conceptually; fix the prospectus wording.** | The protocol makes F2 the oracle typed-relation condition, F1 the byte-identical rule-only condition, F0 secondary, and the bundle the unit. Four origin structures are strata, not cross-structure pairs. |
| Is the truth boundary adequate? | **Mostly yes.** | Synthetic origin/provenance is true by construction only. The package explicitly excludes real-world independence, truth, authority, retrieval, routing, human correction, decisions, and deployment. Unqualified “independence” in editorial examples still weakens this boundary. |
| Are leakage and resource controls credible on paper? | **Design-ready, not evidence.** | Exact F1/F2 token parity, opaque IDs, order/style/overlap controls, split-by-proposition/origin-family, parser policy, invalid-output sensitivity, relation noise, and stopping gates are appropriate. They must be implemented and passed before any efficacy language. |
| Is the current effect claim properly status-labeled? | **Not quite.** | “May reduce” and “would support” are used in Loop 2; the protocol’s “used supplied metadata” is too mechanistic. No file may report a positive result until a study is actually run. |
| Is the public site safe as a thought piece? | **Conceptually yes; terminology needs one pass.** | It states “conceptual synthesis · not empirical validation,” says the first paper tests cue use rather than provenance/full layer, and keeps the receipt fictional/no-verdict. Its title and several examples still carry avoidable “independent” and “route” readings. |
| Are references accurate and synchronized? | **Mostly, but not submission-ready.** | The ACL/DOI records in the Bib are generally strong and no duplicate Bib keys were found. Markdown/Bib omissions, PaperTrail link choice, and incomplete preprint metadata need correction. |

## Broad architecture novelty: final disposition

**[S]** The package itself now contains the correct concessions:

- `THOUGHT_PIECE_V14.md` states that current literature contains integrated systems spanning cross-source verification, conflict modeling, source-aware attribution, adaptive search, and evidence interfaces; it explicitly says the piece does not claim an unoccupied universal layer.
- Its limitations state “No claim of mechanism novelty,” “No proven minimum,” no validated constructs, and no validation from the product cases.
- `PAPER_PROSPECTUS_V0.md` calls the first paper a single offline cue-use study and explicitly renounces invention of information foraging, VOI/metareasoning, provenance/evidence graphs, RAG, mixed initiative, cognitive forcing, human review, calibration, organizational memory, and learning.
- `CLAIMS_AND_EVIDENCE_REGISTER.md` marks the universal-layer claim rejected/narrowed and the F2 effect an empirical hypothesis.
- `OVERCLAIM_AND_COUNTERARGUMENT_REGISTER.md` says to retire broad architecture novelty and lead with F2-versus-F1.
- The public page calls the work a practitioner thought piece with an academic readiness path and says its closing is not a complete, empirically validated, or novel scientific mechanism.

**[I]** This is sufficient to say broad novelty has been retired in the integrated package. It is not sufficient to leave the historical title, “layer” metaphor, and wide component map unqualified in a scientific title, abstract, or contribution statement. The map remains a useful taxonomy/design agenda; it is not a discovered architecture. A manuscript reviewer should not need to infer this from the limitations section.

## F2 versus F1: estimand and naming audit

### What is correctly isolated

**[S]** The protocol’s primary estimand is the right narrow object:

- F0: citation-only condition, secondary;
- F1: explicit origin-counting rule, with neutral relation slots;
- F2: the byte-identical F1 rule plus stipulated `dependent`, `independent_as_stipulated`, or `unknown` metadata;
- same evidence text, report order, schema, model/checkpoint, decoding, output cap, and exact per-bundle token parity;
- one parsed origin-count assertion per bundle-condition;
- primary FC event defined from the restricted manifest;
- F2/F1 paired comparison, with valid-origin recall as a safety endpoint;
- no retrieval, router, memory, human-interface, outcome-feedback, or field condition.

This is best named a **within-bundle paired cue-conditioned false-corroboration contrast**. “Cue use” may remain as a shorthand in a methods title only if the paper defines it as an observable output difference and says it does not identify internal use.

### What is not correctly isolated yet

The sentence at `research/PAPER_PROSPECTUS_V0.md:121` says:

> “Generate matched pairs in which only origin structure changes.”

The operationalization specification correctly explains that conflict versus support-only structures cannot all share identical text and a coherent latent graph under that instruction. This is not a cosmetic inconsistency: it changes the estimand and could make the truth construction incoherent.

**Required replacement:**

> “Generate balanced strata across the four origin structures. The only confirmatory paired contrast is F2 versus F1 within each bundle, where evidence text, report order, rule, output contract, and resources are held constant. Cross-structure differences are descriptive/stratified, not counterfactual matches. If cross-structure matched sets are later desired, define a new `match_set_id` and protocol before generation.”

The current four structures can remain: one-origin repetition, multiple-origin convergence, unknown origin, and conflict. Report structure-specific estimates descriptively or with a prespecified interaction; do not call them matched counterfactual effects.

### Naming the safety endpoint

“Valid-origin recall” is understandable but can be read as recall of real origins. Use **stipulated-support-origin recall** or **recall of stipulated supporting origins** in the paper title/abstract and define `VOR` as an internal shorthand. Keep “independent-as-stipulated” in the codebook, not as an unqualified scientific property.

### Estimand signs and denominators

The protocol is correct to define lower `Delta_FC` as better and to preserve invalid outputs in assigned-run denominators while reporting valid-output and invalid-output sensitivities. The manuscript must state all of the following together:

1. primary analysis is over the prespecified jointly valid F1/F2 set `I*`;
2. all assigned runs remain in runtime/invalid denominators;
3. conservative and liberal invalid-output codings are sensitivity analyses;
4. unknown-origin bundles do not become evidence for real-world absence or dependence;
5. the five-percentage-point recall margin is a planning candidate fixed before efficacy inspection, not a discovered universal standard.

## Closest-work comparison matrix

The following sources should anchor the final manuscript’s prior-art paragraph. The residual distinction is narrow and methodological; none licenses a broad “layer” novelty claim.

| Source and verified record | Direct overlap [S] | What could still differ [I] | Disposition |
|---|---|---|---|
| Lebo, Sahoo & McGuinness, **PROV-O: The PROV Ontology** (W3C Recommendation, 2013), [official standard](https://www.w3.org/TR/prov-o/) | Standardizes entities, activities, agents, derivation and provenance relations. | Does not prescribe this model task or false-corroboration endpoint. | Must cite as a provenance vocabulary, never as evidence of truth/independence. |
| Zhang, Ives & Roth, **Who Said It, and Why? Provenance for Natural Language Claims** (ACL 2020), DOI [10.18653/v1/2020.acl-main.406](https://doi.org/10.18653/v1/2020.acl-main.406), [ACL](https://aclanthology.org/2020.acl-main.406/) | Direct natural-language claim provenance and source/derivation reasoning. | Does not isolate a supplied origin-family cue against a rule-only control. | Closest conceptual claim-provenance anchor; cite in first paragraph of prior art. |
| Amaral, Rodrigues & Simperl, **ProVe** (Semantic Web 2024), DOI [10.3233/SW-233467](https://doi.org/10.3233/SW-233467) | Automated provenance verification against text; graph/text relation checking. | Verification pipeline, not an oracle-cue behavioral comparison. | Must cite; rules out provenance verification as new architecture. |
| Tan et al., **HydraRAG** (EMNLP 2025), DOI [10.18653/v1/2025.emnlp-main.730](https://doi.org/10.18653/v1/2025.emnlp-main.730), [ACL](https://aclanthology.org/2025.emnlp-main.730/) | Structured cross-source reasoning, source reliability, graph topology, and corroboration. | Retrieval/agentic reasoning over real benchmark evidence; no F2/F1 stipulated relation-field contrast. | Closest integrated source-aware/corroboration comparator; must cite and block broad novelty language. |
| Ge et al., **CONFACT** (IJCAI 2025), DOI [10.24963/IJCAI.2025/1073](https://doi.org/10.24963/IJCAI.2025/1073), [official proceedings](https://www.ijcai.org/proceedings/2025/1073) | Conflict modeling and credibility information in RAG fact checking. | Credibility is not origin dependence; no stipulated `unknown` origin state. | Must cite; add as a conflict/credibility comparator, not an origin-equivalent. |
| Hwang et al., **Retrieval-Augmented Generation with Estimation of Source Reliability** (EMNLP 2025), [ACL](https://aclanthology.org/2025.emnlp-main.1738/) | Source reliability is made explicit in RAG. | Reliability weighting differs from source derivation/origin-family relation. | Must cite to prevent “source reliability” from being recast as new. |
| Zhang et al., **FaithfulRAG** (ACL 2025), DOI [10.18653/v1/2025.acl-long.1062](https://doi.org/10.18653/v1/2025.acl-long.1062), [ACL](https://aclanthology.org/2025.acl-long.1062/) | Fact-level conflict modeling and context-faithful generation. | End-to-end RAG faithfulness, not a metadata-vs-rule behavioral isolate. | Must cite as a source/context-faithfulness comparator. |
| Sun et al., **CLUE: Explaining Sources of Uncertainty in Automated Fact-Checking** (ACL 2026), DOI [10.18653/v1/2026.acl-long.2110](https://doi.org/10.18653/v1/2026.acl-long.2110), [ACL](https://aclanthology.org/2026.acl-long.2110/) | Claim–evidence and inter-evidence conflict/agreement relations; uncertainty explanation. | Does not test this oracle relation cue or FC endpoint. | Must cite; makes relational uncertainty non-novel. |
| **Xia, Diagnosing Evidence Utilization… under Matched Evidence Conditions** (arXiv 2026), DOI [10.48550/arXiv.2606.06758](https://doi.org/10.48550/arXiv.2606.06758), [arXiv](https://arxiv.org/abs/2606.06758) | Direct matched-condition diagnostic of whether models use supplied evidence. | Different evidence-utilization task; no origin-family relation field or false-corroboration event. | Essential nearest methodological precedent; use “we extend the matched-condition logic to origin accounting,” not “first evidence-use test.” |
| **Nematov et al., Source Attribution in Retrieval-Augmented Generation** (arXiv 2025), DOI [10.48550/arXiv.2507.04480](https://doi.org/10.48550/arXiv.2507.04480), [arXiv](https://arxiv.org/abs/2507.04480) | Shapley-based attribution of influential retrieved documents; evaluates redundancy, complementarity, and synergy among sources. | Influence attribution is not a supplied origin-family graph and does not isolate F2/F1. | **Missing closest comparator.** Add to Loop 2 matrix, `REFERENCES.md`, `references.bib`, and the manuscript’s source-attribution paragraph. Label preprint. |
| Alvarez et al., **ProvenanceGuard** (arXiv 2026), DOI [10.48550/arXiv.2606.18037](https://doi.org/10.48550/arXiv.2606.18037), [arXiv](https://arxiv.org/abs/2606.18037) | Claim-level source ownership, source-aware factuality, and block/allow decisions in tool traces. | Post-generation verification and captured source labels, not pre-generation synthetic cue use. | Must cite as current preprint; do not claim claim-level source ownership is new. |
| Louck, **Securing LLM-Agent Long-Term Memory Against Poisoning** (arXiv 2026), DOI [10.48550/arXiv.2606.24322](https://doi.org/10.48550/arXiv.2606.24322), [arXiv](https://arxiv.org/abs/2606.24322) | Origin-bound authority, non-malleable propagation, manufactured-corroboration threats, and authenticated origin labels. | Security/action authorization model, not benign synthetic FC diagnostic. | Must cite with preprint status; it is a direct conceptual limit on origin-bound claims. |
| Martin-Boyle et al., **PaperTrail** (CHI 2026), DOI [10.1145/3772318.3791101](https://doi.org/10.1145/3772318.3791101), [ACM record](https://doi.org/10.1145/3772318.3791101) | Claim–evidence interface for grounding provenance in scholarly Q&A. | Human interface and provenance grounding, not model-only F2/F1. | Must cite as an evidence-interface comparator; do not claim inspectable claim/evidence paths are new. |
| Laitenberger, Manning & Liu, **Stronger Baselines for Retrieval-Augmented Generation with Long-Context Language Models** (EMNLP 2025), DOI [10.18653/v1/2025.emnlp-main.1656](https://doi.org/10.18653/v1/2025.emnlp-main.1656), [ACL](https://aclanthology.org/2025.emnlp-main.1656/) | Shows that a simple source-faithful baseline can match or beat elaborate RAG under scaled budgets. | Not origin-aware. | Must cite as the complexity-tax comparator; a typed cue earns value only against matched simple rules. |
| Abolghasemi et al., **Evaluation of Attribution Bias in Generator-Aware RAG** (Findings ACL 2025), DOI [10.18653/v1/2025.findings-acl.1087](https://doi.org/10.18653/v1/2025.findings-acl.1087), [ACL](https://aclanthology.org/2025.findings-acl.1087/) | Counterfactual authorship metadata can change attribution behavior without changing evidence. | Different attribution task, but exactly the cue-salience threat relevant to F2. | Must cite and use to motivate codebook permutation, metadata-position controls, and field-only diagnostics. |
| Li et al., **Authority Bias in RAG** (ACL 2025), DOI [10.18653/v1/2025.acl-long.1400](https://doi.org/10.18653/v1/2025.acl-long.1400), [ACL](https://aclanthology.org/2025.acl-long.1400/) | Authority cues can distort evidence use. | Authority is not origin dependence. | Must cite as a terminology/construct-separation warning. |
| Sabouhi, **Context Is Not Control** (working manuscript, 2026), [PDF](https://symbolicsuite.com/context-is-not-control.pdf), [author repository](https://github.com/rjsabouhi/context-is-not-control) | Closest openly described boundary-conditioned synthetic cue-use warning: explicit source-status/admissibility records can alter behavior without proving intrinsic inference. | Not peer-reviewed and not the same endpoint or origin graph. | Cite only as a working artifact/negative-boundary comparator; never present it as settled literature. |

**[I]** Across these sources, the residual space is not “a layer before generation.” It is a specific experimental contrast: a frozen model receives the same evidence and rule, plus a stipulated origin relation field, and is scored on a formally defined false-corroboration event. That may be a useful measurement artifact. It is not a new architecture.

## Terminology stress test

| Term in current package | Risk | Recommended controlled use |
|---|---|---|
| **Discrimination layer** | [DJ] Collides with social/legal discrimination, classifier/discriminator terminology, and fairness literature. The technical definition does not erase the ordinary meaning. | Keep as historical thought-piece title only if the nearby definition and provisional status remain. Use **origin accounting**, **evidence-context judgment**, or **selection-and-action audit record** for scientific artifacts. |
| **Layer** | [I] Implies an implementation boundary, stack position, or universal architectural primitive. | Say “proposed systems responsibility” or “conceptual map.” Do not claim a new layer in title/abstract. |
| **Independence / independent corroboration** | [S/I] Can mean causal, statistical, epistemic, institutional, or source independence. The benchmark only stipulates origin-family relations. | Use **origin relation**, **dependent**, **distinct-as-stipulated**, **unresolved**, or **separately rooted under the packet’s rule**. Reserve `independent_as_stipulated` for the codebook and define it every time it appears in methods. |
| **Provenance** | [S/I] In the protocol, graph provenance is supplied/gold by construction. Readers may infer discovery or verification. | Say **stipulated provenance graph** or **oracle relation metadata**. Never say the model “discovers provenance.” |
| **Cue use** | [DJ] “Use” can imply attention, reasoning, internal representation, or causal mediation. | Define behaviorally as **cue-conditioned output difference**. Replace “the model used metadata” with “the typed-cue condition produced…” unless a separate mechanistic study is run. |
| **False corroboration** | [DJ] Useful but not universally standardized; can be confused with false consensus or attribution error. | Keep as the primary endpoint only with the exact event definition at first use: a valid output asserts at least two supporting origin paths when the stipulated manifest certifies zero/one/unknown. Report claim stance separately. |
| **Benchmark** | [I] A synthetic generator plus one frozen model and one primary contrast is better described as a diagnostic/protocol than a general benchmark. | Use **frozen-model diagnostic**, **cue-use diagnostic**, or **synthetic origin-accounting test**. Retain “benchmark” only if the artifact is released as a reusable multi-model task with stable task documentation. |
| **Valid-origin recall** | [DJ] Sounds like real provenance recall. | Use **stipulated-support-origin recall** in prose; keep `VOR` as a defined analysis abbreviation if needed. |
| **Route receipt** | [DJ] “Route” implies a mandatory pipeline despite the explicit no-workflow boundary. | Prefer **origin-accounting receipt** or **selection-and-action audit record**. If “route receipt” is retained, add “static illustrative record, not a workflow” in the heading, accessible description, and caption. |
| **Independent test** (public site) | [I] The site example does not establish that a test is epistemically independent merely because it is separately authored. | Replace with **documented distinct-origin test** or **separately authored test, with relation still to be assessed**. |

## P0 corrections: required before preregistration or scientific handoff

### P0-1 — Repair the cross-structure matching statement

**File:** `research/PAPER_PROSPECTUS_V0.md:121`
**Current:** “Generate matched pairs in which only origin structure changes.”
**Replace with:**

> Generate balanced strata across the four origin structures. The confirmatory paired contrast is F2 versus F1 within each bundle; evidence, reports, rule, output contract, and resources are held constant. Cross-structure differences are descriptive/stratified, not counterfactual matches. Define a new match-set identifier and protocol before attempting any later cross-structure pair design.

Also remove any abstract/method sentence that calls the four structures “matched pairs.” This is the one direct contradiction between the prospectus and the operationalization specification.

### P0-2 — Change the positive claim from an internal-use assertion to an observable effect

**Files:** `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V0.md:21`, `source/THOUGHT_PIECE_V14.md:554`, and any first-paper abstract/claim ladder copied from them.
**Current:** “the tested model used supplied origin-relation metadata to reduce false corroboration…”
**Replace with:**

> On newly authored fictional bundles with a stipulated provenance graph, the typed-cue condition produced a lower false-corroboration rate than the rule-only condition under exact F1/F2 resource matching, on the tested frozen model, while retaining stipulated-support-origin recall within the preregistered safety margin.

Add immediately afterward:

> This is an observable condition effect. It does not identify internal reasoning, provenance discovery, real-world independence, or a causal mechanism of cue use.

The phrase “used supplied metadata” may remain only in an explicitly behavioral shorthand sentence that defines “use” as a measurable F2-versus-F1 output contrast, never as a claim about model internals.

### P0-3 — Add a deterministic metadata-only diagnostic before primary lock

**Files:** `research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V0.md`, `research/overnight/rounds/08_LOOP2_OPERATIONALIZATION_SPEC.md`.
**Current gap:** F2 relation values (`DPND`, `INDP`, `UNKN` or equivalent) are intentionally countable, but no explicit deterministic metadata-only comparator appears in the current protocol/specification.

Add two secondary diagnostics, with no change to the primary F2/F1 estimand:

1. **Metadata-only rule oracle:** a deterministic script reads only the relation field and the fixed claim/stance manifest and emits the prespecified origin count/claim state. This is a format/ceiling check, not a language-model baseline.
2. **Field-only model diagnostic:** mask or neutralize evidence wording while preserving the relation field and output contract, and/or run a codebook-permutation field condition. This measures whether the model can copy/count the field without integrating report content.

If F2 matches the metadata-only oracle, that does not invalidate the behavioral result, but it limits the claim to field execution/counting. If the F2 effect disappears under codebook permutation, relation noise, or evidence-content masking, report it as a shortcut/oracle upper bound rather than semantic origin accounting. Freeze these diagnostics and their interpretation before primary outputs are opened.

### P0-4 — Put the oracle/frozen-model boundary in the title and abstract

**File:** `research/PAPER_PROSPECTUS_V0.md:15–17`; protocol title/answer-first section; any eventual submission abstract.
**Current title:** “Origin-Relation Cue Use in Evidence Bundles: A Controlled False-Corroboration Benchmark.”
**Recommended title:**

> **A Frozen-Model Diagnostic of Stipulated Origin-Relation Cues in Evidence Bundles**

Acceptable shorter alternative:

> **Do Typed Origin Relations Change Evidence Counting? A Synthetic Cue-Conditioned Diagnostic**

If “benchmark” is retained, the manuscript must state that it is a synthetic, single-model-at-first, oracle-cue benchmark artifact and must not imply multi-model or deployment generality. “Discrimination layer,” “evidence before generation,” “trust,” “independent corroboration,” and “decision quality” should not appear in the first paper’s title.

## P1 corrections: required before manuscript submission or public handoff

### P1-1 — Add the missing source-attribution comparator

Add **Ikhtiyor Nematov, Tarik Kalai, Elizaveta Kuzmenko, Gabriele Fugagnoli, Dimitris Sacharidis, Katja Hose, and Tomer Sagi (2025), “Source Attribution in Retrieval-Augmented Generation,” arXiv:2507.04480, DOI 10.48550/arXiv.2507.04480** to:

- the closest-work matrix in `research/overnight/rounds/07_LOOP2_CURRENT_LITERATURE_EXPANSION.md`;
- `research/REFERENCES.md`, with the arXiv DOI and “preprint” status;
- `research/references.bib`, under a stable key such as `NematovEtAl2025SourceAttribution`;
- the final paper’s attribution/source-influence paragraph.

**Why it is closest:** the source studies Shapley-style attribution of influential retrieved documents and explicitly analyzes redundancy, complementarity, and synergy. It does not supply the project’s `dependent`/`independent_as_stipulated`/`unknown` origin field and does not isolate F2/F1, so the residual distinction remains narrow and defensible.

### P1-2 — Synchronize Markdown and Bib records

| Record | Current inconsistency | Exact disposition |
|---|---|---|
| PaperTrail | `REFERENCES.md:41` links only to arXiv while the Bib has the canonical ACM DOI. | Use [10.1145/3772318.3791101](https://doi.org/10.1145/3772318.3791101) in Markdown; optionally retain arXiv as a secondary link. |
| Nematov et al. | Present in `REFERENCES.md`, absent from Bib. | Add full authors, title, arXiv ID, DOI, URL, and preprint note. |
| A-Mem | Present in `REFERENCES.md`, absent from Bib. | Add a full record and official NeurIPS DOI [10.52202/085713-0593](https://doi.org/10.52202/085713-0593), with venue/status verified at submission. |
| Louck | Bib has the full subtitle but no DOI/URL; Markdown has a shortened title and arXiv URL only. | Use the full title and arXiv DOI [10.48550/arXiv.2606.24322](https://doi.org/10.48550/arXiv.2606.24322); label preprint. |
| Sabouhi | Loop 2 treats “Context Is Not Control” as an unusually close working artifact, but it is not in the formal refs. | Either add a clearly marked working-artifact entry with PDF/repository links or state explicitly that it is supplemental, not part of the peer-reviewed bibliography. |
| Xia, ProvenanceGuard, Pandey, Astaraki | Bib has arXiv-issued DOI fields; Markdown has only arXiv URLs. | Add arXiv DOI links and “preprint” labels consistently. |
| Paper metadata | Minor capitalization differences (“Sub-Optimal,” “Multi-Hop,” “Real-World”) are non-substantive. | Normalize titles to official records before submission; no novelty consequence. |

No duplicate Bib keys were found in the current file. The remaining problem is alignment and status, not wholesale citation unreliability.

### P1-3 — Fix stale Loop 2 interface notes

`research/overnight/rounds/09_LOOP2_OPPORTUNITY_AND_INTERFACE_SPEC.md` still describes a five-versus-nine count contradiction and an H1 ordering that is no longer true in the current page source. The current `site/app/page.tsx` uses nine consistently in the receipt/illustration/example, places the receipt before the demoted H1, and the question grid currently has no duplicate final three items. Mark those sections of 09 as historical/stale or update them to the current v14 state. Do not carry the obsolete contradiction into an owner handoff.

### P1-4 — Qualify independence in the thought piece

**File:** `source/THOUGHT_PIECE_V14.md`, especially C02/C04/C05/C06/C09 and the worked example.
**Risky examples:** “independent rollback test,” “independent corroboration,” “claim-level independence,” “independence context,” “no independence from the vendor,” and “changes two articles from independent to common-origin.”
**Recommended replacements:**

- “independent rollback test” → “separately authored rollback test, with origin relation still to be assessed”;
- “independent corroboration” → “distinct-origin support under the stated relation rule”;
- “claim-level independence” → “claim-level origin relation”;
- “independence context” → “origin-dependence context”;
- “no independence from the vendor” → “vendor-linked origin relation; no separately rooted support established”;
- “changes two articles from independent to common-origin” → “relabels two articles from separately rooted-as-stipulated to common-origin under the packet’s relation rule.”

The glossary’s careful definition of origin relation should become the default wording in the body, not only a footnote-like safeguard.

### P1-5 — Qualify the public receipt and site examples

**Files:** `site/app/page.tsx`, `site/app/content.ts`. The current live source is much safer than earlier drafts, and its duplicate question-grid bug is already absent. Remaining exact replacements:

| Current phrase | Recommended phrase |
|---|---|
| “do not automatically become independent confirmation” | “do not establish distinct-origin support under this packet’s relation rule” |
| “nine mentions do not become nine independent confirmations” | “nine mentions do not establish nine distinct origins” |
| “Independent supporting origins established for this claim” | “Supporting origins counted under the stated relation rule” |
| “HOLD · SEEK INDEPENDENT TEST” | “HOLD · SEEK A DOCUMENTED DISTINCT-ORIGIN TEST” |
| “How many independent origins are there?” | “How many distinct origins are documented under the packet’s relation rule?” |
| “not independent support” | “not separately rooted support under the stated relation rule” |
| `route receipt` | `origin-accounting receipt` or `selection-and-action audit record` |
| C02 “independent rollback test” | “separately authored rollback test” |
| C04 “independent corroboration” / “claim-level independence” | “distinct-origin support” / “origin relation” |
| C06 “independence” / “non-independent from the vendor” | “origin relation” / “vendor-linked under the stated relation rule” |
| C09 “from independent to common-origin” | “from separately rooted-as-stipulated to common-origin” |

The relation key may retain `INDEPENDENT-AS-STIPULATED` as a benchmark token, but the visible legend must say that the token is a stipulated graph value, not a finding about real-world epistemic independence.

### P1-6 — Do not let one-model evidence generalize

The current first-paper panel correctly says “one frozen model.” Make this limitation visible in the title, abstract, results heading, and conclusion. An optional second model is unpowered robustness, not cross-model evidence. If the study remains one model, use “on the tested frozen model” in every positive claim and do not use “language models” or “models” generically except for the research question.

### P1-7 — Align the protocol/specification version identifiers

The protocol front matter says version 0.2 while the operationalization release manifest shown in the specification still contains `protocol_version: "0.1"` and `specification_version: "loop2-operationalization-0.1"`. Freeze a version map before preregistration. This is a reproducibility correction, not a conceptual novelty issue, but a reviewer will treat mismatched hashes/versions as a serious audit defect.

## Bibliography and citation audit

### Sources that are currently well-positioned

The current Bib has strong records for PROV-O, Zhang et al. claim provenance, ProVe, Pendo, HydraRAG, CONFACT, FaithfulRAG, CLUE, BERGEN, NoMIRACL, KUP, GenProve, TROVE, authority bias, attribution bias, Search-o1, Agentic Reasoning, DeepResearcher, and the matched-evidence preprints. The ACL DOI/page metadata inspected for the 2025–2026 papers is generally consistent with official records. Keep industry material such as Anthropic’s context-engineering note clearly marked as implementation context, not independent empirical support.

### Must-cite additions or corrections

1. **Nematov et al. 2025** — closest source-influence/redundancy comparator; add everywhere above.
2. **Xia 2026** — matched evidence-utilization precedent; retain the corrected exact title, DOI, and preprint status.
3. **Abolghasemi et al. 2025** — metadata/attribution bias threat; use to justify codebook permutation and field-only controls.
4. **Laitenberger et al. 2025** — simple source-faithful RAG can win under scaled resources; use as complexity-tax warning.
5. **Louck 2026** — origin-bound memory/security is a direct conceptual limit; label preprint and do not collapse security provenance into benign origin accounting.
6. **PaperTrail 2026** — claim/evidence interface/provenance grounding; use canonical ACM DOI in formal references.
7. **Sabouhi working artifact** — only if the paper relies on its unusually close framing; clearly label it unreviewed.

### Sources that should not be overstated

- PROV-O gives a vocabulary, not truth or independence.
- Claim provenance, evidence graphs, and source attribution show representation/traceability precedents, not this specific F2/F1 effect.
- Source reliability, authority bias, and credibility are not origin-family relations.
- RAG and long-context papers show evidence-use and complexity risks, not the first paper’s endpoint.
- A-Mem, Hindsight, Louck, and other memory work cannot validate organizational learning or outcome feedback in this project.
- A current preprint can be a must-cite comparator while remaining insufficient to establish a settled field consensus.

## Claim-level disposition

| Claim or phrase | Disposition | Reason |
|---|---|---|
| “A novel universal discrimination layer before generation” | **Reject.** | Current integrated systems cover overlapping provenance, conflict, attribution, retrieval, source reliability, interfaces, memory, and action surfaces. |
| “The project integrates known responsibilities into a conceptual map” | **Retain as conceptual synthesis.** | Accurate if each responsibility is sourced and the map is not sold as mechanism novelty. |
| “A candidate compact/minimal policy” | **Defer.** | “Compact” and especially “minimal” require ablation, task/domain profile, cost, and strong baselines. |
| “Typed origin cues may reduce false corroboration beyond an explicit rule” | **Retain as empirical hypothesis.** | This is the narrow F2/F1 estimand, not a result. |
| “The model used the metadata” | **Rewrite.** | Observable output contrast cannot establish internal use. |
| “Independent corroboration” in synthetic/public examples | **Qualify or replace.** | Real-world epistemic independence is out of scope; use stipulated origin relation. |
| “Controlled false-corroboration benchmark” | **Use cautiously.** | A single frozen model and synthetic oracle field make “diagnostic” more accurate unless a reusable multi-model benchmark is released. |
| “Improves evidence quality, decisions, or outcomes” | **Reject currently.** | No human, retrieval, consequence, utility, or field endpoint exists. |
| “Validates provenance-aware generation” | **Reject currently.** | F2 receives provenance/origin metadata; it does not discover or validate provenance. |
| “Route receipt” as a required pre-generation stage | **Rewrite.** | Current receipt is a static illustrative record, not a workflow or mandatory pipeline. |
| “First study to test whether models use evidence/origin metadata” | **Reject.** | Xia, Pandey, Astaraki, Sabouhi, attribution-bias work, and Nematov-related attribution make priority claims unsafe. |

## Contradictions and methodological limits that must remain visible

1. **Oracle versus discovery:** F2’s graph is stipulated. A positive result says the output is sensitive to a supplied field under the prompt; it says nothing about extracting provenance from raw documents.
2. **Code execution versus semantic integration:** direct relation codes can be counted without reading or reconciling reports. The deterministic and field-only controls are needed to bound this interpretation.
3. **Synthetic origin versus real independence:** “independent-as-stipulated” means separate origin nodes in the generator. It does not imply causal independence, epistemic reliability, absence of shared background data, or truth.
4. **Unknown is not zero:** the conservative FC rule treats an output of two or more supporting paths as an error when the manifest certifies zero/one/unknown, but the paper must report unknown-origin sensitivity separately and avoid turning uncertainty into a factual absence.
5. **Conflict is not a matched manipulation:** conflict bundles can differ in claim stance and truth construction. They are strata unless a new counterfactual design is preregistered.
6. **One model is not a model class:** exact decoding and 300 bundles yield a model/prompt/generator result. They do not establish general language-model behavior.
7. **Exact token parity is necessary, not sufficient:** equal length does not remove semantic salience, label readability, position effects, or relation-code shortcuts.
8. **The safety margin is a design choice:** five percentage points is a candidate non-inferiority margin, not a validated safety standard.
9. **False corroboration is not truth:** the primary event concerns counting of supporting paths, not whether the underlying proposition is true. Claim stance and support are descriptive/secondary here.
10. **A null is informative:** F2=F1, a rule-only win, or an F2 gain matched by a deterministic oracle may show no incremental semantic value. Do not escalate to routing, memory, human correction, or deployment after a null.
11. **The public receipt is an interface hypothesis:** semantic HTML and explicit labels may improve comprehension, but no reader study has established that it does. The site’s receipt remains illustrative.
12. **Organizational learning is not present:** a versioned ledger and feedback loop are design concepts; without prespecified outcomes, update rules, longitudinal users, and governance, the project cannot claim learning.

## Recommended final claim paragraph

Use the following paragraph, or a materially equivalent version, as the bounded first-paper abstract/conclusion claim. It is deliberately result-conditional and includes the model and oracle limits:

> We propose an offline, frozen-model diagnostic on newly authored fictional evidence bundles. Within each bundle, reports and an explicit origin-counting instruction are held constant; F1 receives neutral relation slots and F2 receives benchmark-stipulated origin-relation codes. We estimate the paired difference in false-corroboration outputs (F2 minus F1), with stipulated-support-origin recall/non-inferiority, invalid-output, leakage, metadata-only baseline, and relation-noise analyses. A qualifying result would show only that the tested model’s output was condition-sensitive to supplied origin-relation metadata under this prompt, model, generator, and resource budget. It would not establish provenance discovery, real-world independence, truth, source authority, better retrieval, human correction, better decisions, or a general evidence-selection layer.

If results are null, harmful, formatting-only, or fragile under codebook/noise/model controls, replace “qualifying result” with the corresponding negative interpretation and retire the typed-cue novelty claim. Do not convert a safety-pass or a descriptive secondary measure into efficacy.

## Stop/retire criteria

The package should stop or narrow rather than expand when any of the following occurs:

- exact F1/F2 token/resource parity cannot be achieved;
- the prospectus/specification still contains the cross-structure “matched pairs” instruction at preregistration;
- deterministic regeneration, graph integrity, semantic QA, parser, leakage, or governance gates fail;
- relation codes, position, formatting, style, or surface patterns predict the condition beyond the preregistered ceiling;
- F2 does not beat F1 by the prespecified minimum effect;
- F2 reduces FC but violates stipulated-support-origin recall non-inferiority;
- F1 and F2 tie while both beat F0, indicating that the rule—not metadata—explains the effect;
- the gain disappears under relation noise, codebook permutation, field-only masking, or a strong deterministic baseline;
- the result is unstable across predeclared seeds or the optional model;
- the effect survives only on formatting-easy structures;
- model/checkpoint, prompt, parser, or bundle generation is changed after primary access;
- any manuscript sentence implies provenance discovery, real-world independence, truth, trust, human correction, decision quality, organizational learning, deployment readiness, or universal architecture.

If the study is stopped for these reasons, a null/diagnostic paper may still be valuable. The broad layer must remain retired as a novelty claim regardless of the F2 result.

## Compact final disposition table

| Disposition | Items |
|---|---|
| **Must change** | Repair `PAPER_PROSPECTUS_V0.md:121`; replace internal-use wording in protocol/thought-piece; add deterministic metadata-only and field-only diagnostics; put oracle/frozen-model wording in title/abstract; add Nematov and synchronize Bib/Markdown; update stale Loop 2 interface notes; qualify unbounded independence language; align protocol/specification version identifiers. |
| **Optional but worthwhile** | Rename the first artifact to “frozen-model diagnostic”; run a reader terminology test for “discrimination layer”; add a second model only as clearly unpowered robustness; include Schreieder’s 2026 terminology survey as a secondary status-labeled citation; retain a supplemental working-artifact note for Sabouhi if needed. |
| **Reject / retire** | Universal “discrimination layer” novelty; “first” claims; minimal/compact architecture claims before ablations; real-world independence/truth/authority claims; provenance discovery or human/decision/outcome claims from F2; broad language-model generalization from one frozen model; deployment, organizational learning, or routing conclusions from the first study. |

## Final reviewer recommendation

**REVISE, then preregister only the bounded diagnostic.** The package has successfully moved from an overstated architecture thesis to a potentially falsifiable origin-accounting measurement question. The remaining corrections are not a request to enlarge the theory; they are the opposite: remove the last implicit mechanism and independence claims, make the within-bundle estimand unambiguous, expose the metadata shortcut baseline, and close the bibliography/status gaps. After those edits, the narrow paper can be judged on whether F2 changes false-corroboration behavior beyond F1 under exact matched resources. Nothing in that result, positive or negative, should be used to revive broad architecture novelty without a separate, preregistered study with its own estimand, comparators, human/field endpoints, and stop rules.

export type FrameworkComponent = {
  id: string;
  name: string;
  summary: string;
  what: string;
  why: string;
  consumes: string;
  produces: string;
  interacts: string;
  risks: string;
  example: string;
  support: string;
  speculative: string;
};

export type FrameworkFamily = {
  number: string;
  name: string;
  question: string;
  output: string;
  tone: string;
  components: FrameworkComponent[];
};

export const families: FrameworkFamily[] = [
  {
    number: "01",
    name: "Intent + authorization",
    question: "What are we deciding, what is allowed, and what can it cost?",
    output: "A versioned decision brief and permission envelope.",
    tone: "teal",
    components: [
      {
        id: "C01",
        name: "Decision brief and authorization envelope",
        summary: "A versioned brief for the decision, permissions, expected baselines, and budget.",
        what: "A versioned statement of the question, intended use, owner, stakes, expected baselines, allowed operations, sensitive-source rules, and budgets.",
        why: "Relevance and meaningful absence are task-relative. Acquisition, disclosure, stopping, and escalation need an explicit frame.",
        consumes: "The owner’s question; audience and use; constraints; permissions; time, money, token, compute, and attention limits; expected sources or perspectives.",
        produces: "A brief version, permission policy, expected baseline, cost envelope, and success, abstention, or escalation criteria.",
        interacts: "Every later record points to this version. It constrains acquisition, defines relevance, gives gaps a baseline, and predefines outcomes.",
        risks: "Technical access becomes mistaken for authorization; a vague question makes relevance arbitrary; a baseline is invented after the evidence; a changed brief fails to invalidate old work.",
        example: "Authorize public-source research and a synthetic-data sandbox; prohibit production data; limit the question to whether a pilot is warranted.",
        support: "Decision analysis, value-of-information, mixed-initiative design, and risk-management practice support explicit task, cost, and authority framing—not this exact schema.",
        speculative: "The minimum useful brief and whether one representation can travel across domains without flattening different evidence and permission rules.",
      },
    ],
  },
  {
    number: "02",
    name: "Evidence spine",
    question: "What did we acquire, from whom, in which version?",
    output: "Governed capture plus stable identity, normalization, and provenance records.",
    tone: "sage",
    components: [
      {
        id: "C02",
        name: "Acquisition controller",
        summary: "A governed controller for proposing, authorizing, recording, and stopping acquisition.",
        what: "A governed mechanism that proposes, authorizes, records, and stops retrieval or collection actions.",
        why: "One more search consumes resources and may cross privacy or permission boundaries. Search therefore needs both value and stopping logic.",
        consumes: "The brief; candidate sources, queries, and tools; current gaps and uncertainty; expected improvement; remaining budget.",
        produces: "An acquisition proposal, authorization result, capture or failure receipt, immutable raw-artifact reference, and budget update.",
        interacts: "It receives targeted gaps from the graphs and router, gives captures to the evidence spine, and reports costs and failures.",
        risks: "Novelty becomes value; scope expands silently; paid or sensitive retrieval runs without permission; failed capture becomes negative evidence; search has no stop state.",
        example: "Authorize one targeted search for a separately authored rollback test—whose origin relation still must be assessed—instead of another broad search for product praise.",
        support: "Information foraging, relevance feedback, active learning, value of information, and metareasoning are direct precedents for bounded selection.",
        speculative: "Reliable value estimates in open-world research, especially with asymmetric harm and rare decisive evidence.",
      },
      {
        id: "C03",
        name: "Source, artifact, normalization, and provenance spine",
        summary: "Stable source and artifact identities with append-only provenance.",
        what: "Stable identities and append-only derivation records for sources, artifacts, captures, versions, transformations, actors, and times.",
        why: "A source is not an artifact; a mutable page is not timeless; a normalized extract is not the original; a summary should not gain authority by losing its origin.",
        consumes: "Raw captures, source observations, artifact bytes or stable references, transformation specifications, and tool versions.",
        produces: "Source and artifact identities, versions or hashes, normalized representations, provenance edges, and explicit identity ambiguity.",
        interacts: "It grounds both graphs, travels with context packets and memory, and lets a correction point to exact evidence.",
        risks: "False merges, duplicate counting, qualifier loss, provenance laundering, unversioned page changes, and lineage presented as truth.",
        example: "Keep the vendor, documentation page, capture time, page version, extracted text, and parser version linked but distinct.",
        support: "Provenance standards such as W3C PROV-O, data lineage, and evidence-synthesis practice support traceable derivation.",
        speculative: "Reliable identity resolution across aliases and complete provenance through opaque provider transformations.",
      },
    ],
  },
  {
    number: "03",
    name: "Relationships + claims",
    question: "What is repeated, dependent, supported, contradicted, or missing?",
    output: "Typed origin, recurrence, gap, claim, evidence, and contradiction relationships.",
    tone: "violet",
    components: [
      {
        id: "C04",
        name: "Relationship, recurrence, common-origin, and gap graph",
        summary: "Typed relationships for recurrence, common origin, time, and meaningful gaps.",
        what: "A typed graph among sources, artifacts, events, observations, time points, copies, derivations, comparison sets, and expected-but-missing perspectives.",
        why: "Repetition does not establish distinct-origin support. Velocity needs repeated observations; meaningful absence needs an expected baseline.",
        consumes: "Identified sources and artifacts, provenance, timestamps, grouping rules, baselines, similarity observations, and citations.",
        produces: "Typed relationships, candidate common-origin clusters, dependence-aware recurrence, comparison sets, gaps, temporal observations, and signal candidates.",
        interacts: "It informs claim-level origin relations, shapes attention and enrichment, and can request targeted acquisition.",
        risks: "Copies become votes; unknown origin becomes separately rooted; similarity becomes shared cause; one timestamp becomes velocity; an unspecified expectation manufactures absence.",
        example: "Nine launch articles remain nine observations, but all link to one announcement rather than counting as nine confirmations.",
        support: "Evidence synthesis, provenance, sensemaking, and coordinated-amplification research support the boundary.",
        speculative: "Useful partial-dependence estimates and defensible thresholds for recurrence, velocity, gaps, or coordination.",
      },
      {
        id: "C05",
        name: "Claim, evidence, comparison, and contradiction graph",
        summary: "Claim-level support, contradiction, qualification, and comparison.",
        what: "A claim-level view connecting atomic propositions to exact evidence spans, support states, qualifications, contradictions, alternatives, and unresolved questions.",
        why: "One document can contain differently supported claims. Publisher reputation and citation presence cannot substitute for entailment.",
        consumes: "Exact artifact spans, candidate claims, identity and common-origin relationships, domain evidence standards, and comparison frames.",
        produces: "Claim versions; support, contradiction, qualification, and insufficiency edges; rationales; alternatives; and comparison matrices.",
        interacts: "It receives provenance and origin-dependence context, supplies claim support without deciding action priority, and feeds cited material to the packet.",
        risks: "Claims stay too broad; citation becomes entailment; authority transfers across claims; lexical overlap becomes evidence; open-world unknowns become binary verdicts.",
        example: "‘Rollback is supported’ links to documentation; ‘rollback is reliable under interruption’ remains insufficient until that condition is tested.",
        support: "FEVER, SciFact, FActScore, evidence synthesis, and structured analytic techniques establish strong claim-level precedents.",
        speculative: "Domain-general claim decomposition and evidence standards that transfer without erasing expert judgment.",
      },
    ],
  },
  {
    number: "04",
    name: "Discrimination policy",
    question: "Which judgment applies, and what permitted step should happen next?",
    output: "Separate assessments, a cost-bounded route, and an inspectable context packet.",
    tone: "coral",
    components: [
      {
        id: "C06",
        name: "Multidimensional assessment",
        summary: "Separate task-scoped judgments that must not collapse into one score.",
        what: "Separate task-scoped judgments for attention priority, domain source authority, claim support, origin relation, relevance, enrichment value, action priority, and owner disposition. Uncertainty and possible consequence remain explicit qualifying attributes.",
        why: "Compressing unlike judgments into one score hides where an error began and lets one virtue launder another.",
        consumes: "The brief, source and artifact records, both graphs, uncertainty, and possible consequences.",
        produces: "Typed assessments with reasons and evidence, unknown or contested states, action considerations, and a review queue.",
        interacts: "It converts evidence structure into routing inputs while keeping each dimension open to correction.",
        risks: "A trust score becomes a verdict; owner interest becomes endorsement; confidence substitutes for support; precise numbers hide uncertain origin.",
        example: "Official documentation can be authoritative for a documented feature, vendor-linked under the stated origin rule, highly relevant, and insufficient for real-world reliability at once.",
        support: "Source-credibility, epistemic-vigilance, claim-verification, relevance, and calibration research support the separations.",
        speculative: "Whether people and models can apply the dimensions reliably and whether the added explicitness improves outcomes enough to justify its cost.",
      },
      {
        id: "C07",
        name: "Enrichment, stopping, and action router",
        summary: "A cost-bounded policy for choosing the next permitted action—or stopping.",
        what: "A policy comparing permitted next actions: acquire, compare, enrich, clarify, answer, answer provisionally, hold, defer, escalate, or refuse.",
        why: "Assessment matters only if it guides a bounded step, but an action decision must not masquerade as a factual conclusion.",
        consumes: "Separate assessments, gap states, allowed actions, remaining resources, expected benefit and consequence, deadline, and stopping criteria.",
        produces: "A recommended action, alternatives, reason, expected benefit and cost range, uncertainty, and a stop or escalation receipt.",
        interacts: "It can loop to acquisition, ask a person for permission, route evidence to packaging, and log predictions and costs for later comparison.",
        risks: "An enrichment-value estimate becomes acceptance or dictates action priority; utility creates false precision; search stops at convenience or never stops; the route exceeds authorization.",
        example: "With rollback risk unresolved and fifteen minutes left, select one reproducible sandbox check instead of ten general articles.",
        support: "Value of information, metareasoning, resource rationality, and mixed-initiative systems are mature precedents.",
        speculative: "Portable utility functions and defensible treatment of unknown or asymmetric harm.",
      },
      {
        id: "C08",
        name: "Bounded context packet",
        summary: "A versioned, reviewable package of selected context and material exclusions.",
        what: "A versioned package of selected material plus provenance, claim links, inclusion and exclusion reasons, unresolved states, budgets, and generation constraints.",
        why: "A generator needs usable context; a reviewer needs to know what influenced it and what was left out. A long prompt guarantees neither.",
        consumes: "The authorized route, exact artifact spans and claims, provenance, assessments, exclusions, gaps, and token or disclosure limits.",
        produces: "A packet version, selection and exclusion manifests, citation map, uncertainty and abstention instructions, and an invocation receipt.",
        interacts: "It binds evidence and routing, stays reviewable before use, and links exact input to output and later outcome.",
        risks: "Compression alters claims; ordering over-amplifies evidence; exclusions vanish; provenance is stripped; sensitive information crosses a boundary.",
        example: "Package documentation, benchmark method, issue passages, common-origin note, material exclusions, unresolved state, and a no-false-certainty instruction.",
        support: "RAG, context engineering, long-context evaluation, and provenance provide adjacent precedents.",
        speculative: "Which fields, ordering, and compression policy best improve correction across models and tasks.",
      },
    ],
  },
  {
    number: "05",
    name: "Human disposition + memory",
    question: "What was accepted, corrected, withheld, or retained?",
    output: "A reviewable disposition and a versioned evidence-and-decision ledger.",
    tone: "ochre",
    components: [
      {
        id: "C09",
        name: "Owner disposition, review, and override",
        summary: "Human acceptance, correction, override, deferral, and escalation.",
        what: "A human control surface for accepting, rejecting, deferring, holding, overriding, requesting enrichment, correcting relationships, and revising constraints.",
        why: "The framework promises correctability. Some permissions and domain judgments belong to accountable people, not a model.",
        consumes: "Assessment and route receipts, packet, evidence paths, uncertainties, costs, consequences, and reviewer role.",
        produces: "A versioned disposition, reason, override, correction, changed constraint, or escalation destination.",
        interacts: "It can revise the brief, correct identity or relationships, approve or reject a route, alter a packet, and supply a decision to the ledger.",
        risks: "Rubber-stamping; evidence-free conclusions; preference stored as fact; unauthorized overrides; excessive review load; access controls that hide needed context.",
        example: "An analyst relabels two articles from separately rooted-as-stipulated to common-origin under the packet’s relation rule and reruns the route without altering either capture.",
        support: "HCI, mixed initiative, structured analysis, and risk management support explicit control; a person ‘in the loop’ alone proves nothing.",
        speculative: "Which decisions require mandatory review and which interface enables real intervention rather than ceremonial approval.",
      },
      {
        id: "C10",
        name: "Versioned evidence, decision, and memory ledger",
        summary: "Append-only history for evidence, decisions, corrections, and supersession.",
        what: "Append-only retention of observations, interpretations, decisions, packets, outputs, corrections, and supersession relationships, with current views built over history.",
        why: "Audit and learning require prior state. Mutable memory can erase why a decision was made or turn an old error into a durable fact.",
        consumes: "Records from earlier components, retention and access policy, correction events, and model, prompt, and tool versions.",
        produces: "Immutable events, current views, supersession links, origin-bound retrieval indexes, an audit timeline, and staleness flags.",
        interacts: "It preserves each stage, supplies authorized prior cases, and gives outcome evaluation the decision state that existed at the time.",
        risks: "Summaries overwrite evidence; memory loses epistemic type; preference becomes a fact; sensitive records outlive authorization; repetition launders authority.",
        example: "A corrected rollback claim remains visible as superseded, excluded from default retrieval, and tied to the evidence and decision that produced it.",
        support: "Provenance, data lineage, organizational learning, and agent-memory research support versioned retention and retrieval.",
        speculative: "Safe cross-task reuse and provenance-preserving compression across opaque model and tool transformations.",
      },
    ],
  },
  {
    number: "06",
    name: "Outcome feedback",
    question: "What happened later, and should any policy change?",
    output: "An expected-versus-observed comparison and a proposed, reviewable update.",
    tone: "blue",
    components: [
      {
        id: "C11",
        name: "Outcome feedback and revisable policy update",
        summary: "Outcome comparison that can propose—but never silently apply—a policy update.",
        what: "A controlled comparison between a predefined expected outcome and an observed later result, followed by a proposal—not silent application—for policy change.",
        why: "Without a defined outcome, feedback becomes retrospective storytelling. Without versioning, learning rewrites history.",
        consumes: "The original brief, route prediction, disposition, output, predefined outcome and horizon, observed result, confounders, and review authority.",
        produces: "An outcome record, attribution limits, error or calibration signal, and an approve/reject/defer proposal for policy update.",
        interacts: "It reads the preserved decision state, returns a proposed update to human review, and never alters raw evidence or prior receipts.",
        risks: "A noisy proxy becomes truth; hindsight changes the target; one owner’s preference becomes a global prior; contamination, selective follow-up, or drift compounds.",
        example: "A sandbox rollback outcome may revise the rule for a later pilot decision; it does not establish that the tool is generally reliable or unreliable.",
        support: "Calibration, organizational learning, decision analysis, and versioned governance are precedents for measured, reviewable updates.",
        speculative: "Causal attribution, useful update rates, safe transfer across tasks, and whether feedback improves policy rather than merely reinforcing local taste.",
      },
    ],
  },
];

export const componentMaturity: Record<string, { label: string; kind: "evidence" | "hypothesis" }> = {
  C01: { label: "Prior art + synthesis", kind: "evidence" },
  C02: { label: "Prior art + design hypothesis", kind: "hypothesis" },
  C03: { label: "Prior art + synthesis", kind: "evidence" },
  C04: { label: "Prior art + design hypothesis", kind: "hypothesis" },
  C05: { label: "Prior art + synthesis", kind: "evidence" },
  C06: { label: "Conceptual synthesis", kind: "hypothesis" },
  C07: { label: "Prior art + design hypothesis", kind: "hypothesis" },
  C08: { label: "Design hypothesis + adjacent precedent", kind: "hypothesis" },
  C09: { label: "Prior art + design hypothesis", kind: "hypothesis" },
  C10: { label: "Design hypothesis + adjacent precedent", kind: "hypothesis" },
  C11: { label: "Design + empirical hypothesis", kind: "hypothesis" },
};

export const researchPaths = [
  { name: "Conceptual systems framework", question: "Can experts distinguish the typed responsibilities, and does an existing architecture already cover them?", proof: "Protocol-led synthesis, construct sorting, discriminant validity, inter-rater agreement, and adversarial boundary cases." },
  { name: "Design-science artifact", question: "Can a bounded artifact make the evidence-to-action path traceable and correctable?", proof: "Requirements traceability, technical invariants, usability work, a strong simple baseline, and mechanism ablations." },
  { name: "HCI / sensemaking system", question: "Which representation supports correction and calibrated reliance without overwhelming people?", proof: "Representative-user studies, comprehension and correction measures, cognitive-load analysis, accessibility evaluation, and qualitative strategy analysis." },
  { name: "AI context / evidence architecture", question: "Does origin-aware context policy improve supported generation under matched budgets?", proof: "Strong RAG and reranker baselines, known-derivation corpora, matched tokens and spend, repeated runs, ablations, and blinded adjudication." },
  { name: "Decision-support evaluation", question: "When does the framework improve decisions enough to justify its overhead?", proof: "Preregistered comparative studies, validated outcomes, matched resources, blinded scoring, delayed outcomes where possible, and harm analysis." },
  { name: "Practitioner thought piece", question: "Can the framework sharpen practice without borrowing academic authority it has not earned?", proof: "Transparent synthesis, disciplined status labels, concrete examples, counterarguments, and an explicit route to future evidence." },
];

export const glossary = [
  ["Discrimination layer", "A proposed systems responsibility for deciding what context may influence generation; not a claim about one service, model, or novel mechanism."],
  ["Attention priority", "How urgently an item deserves inspection because of possible relevance or consequence; not truth probability."],
  ["Domain source authority", "Task- and claim-scoped standing to speak about a domain; not universal trust."],
  ["Claim support", "The relationship between exact evidence and a bounded proposition; not source popularity or citation presence."],
  ["Origin relation", "Whether records share an upstream origin, have separate roots only as stipulated, or remain unresolved; this is not real-world causal or epistemic independence."],
  ["Derivation relation", "How one artifact was copied, paraphrased, summarized, translated, quoted, or inferred from another; not the same as claim support."],
  ["Claim stance", "Whether a bounded evidence span supports, refutes, qualifies, or is insufficient for a claim; not an origin or authorization relation."],
  ["Action relation", "A provisional, hold, escalate, authorized, or unauthorized disposition; not a truth or source-quality label."],
  ["Recurrence", "Repeated observation of a pattern; not necessarily separately rooted corroboration."],
  ["Relevance", "Usefulness to the current brief; not general importance, correctness, or permission."],
  ["Operational authorization", "Permission to acquire, process, disclose, retain, or act; not source competence or evidential support."],
  ["Enrichment value", "The expected benefit of another permitted operation considered with cost and risk; not action priority or acceptance."],
  ["Action priority", "The ordered permitted next step after consequence, uncertainty, cost, and authorization are considered; not a factual verdict."],
  ["Provenance", "A trace of identity, derivation, actors, and time; not proof that content is correct."],
  ["Signal candidate", "A derived pattern worth inspection; not a verified event or conclusion."],
  ["Owner disposition", "An accountable person’s recorded action or judgment; not external truth."],
];

export const technicalGlossary = [
  {
    id: "conditions",
    term: "F0 / F1 / F2",
    definition: "Three versions of the same planned test. F0 is the ordinary baseline, F1 adds an explicit counting rule, and F2 adds the supplied origin clues being tested.",
    example: "If F2 does better than F1, the difference is evidence about the supplied clue—not proof that the whole framework improves decisions.",
    boundary: "They are experimental conditions, not product versions, performance grades, or three different AI systems.",
  },
  {
    id: "transfer",
    term: "T1",
    definition: "A separate, descriptive transfer check using real repetition patterns. It is not part of the main experiment because those datasets do not provide all the ground truth the main question needs.",
    example: "A duplicate-news dataset may show that two articles came from one text, but it cannot by itself show that a claim is true or that every other article had a separate origin.",
    boundary: "It cannot validate the main experiment or certify that real-world sources are independent.",
  },
  {
    id: "sample-size",
    term: "N=300",
    definition: "A plan to assign 300 fictional evidence bundles to the primary comparison. N is simply the number of bundles; it is not a score, a confidence level, or a result.",
    example: "The final number may change after the power and safety checks. No study has been run with these 300 bundles.",
    boundary: "It is not the number of people, reports, model calls, or favorable outcomes.",
  },
  {
    id: "provenance-audit",
    term: "Provenance audit",
    definition: "A review that traces where an item came from, how it changed, and which people or systems handled it. It is not a guarantee that the item is correct.",
    example: "A receipt can show that nine articles came from one announcement without proving the announcement’s claim.",
    boundary: "Tracing an origin does not establish truth, quality, independence, or permission to use the material.",
  },
  {
    id: "system-runtime",
    term: "System runtime",
    definition: "A live program actually processing inputs and producing outputs. The illustrated receipt is only a teaching example, not a running system.",
    example: "Nothing on this page is quietly reading your files or making a pilot decision.",
    boundary: "A diagram, protocol, mockup, or offline generator is not by itself a deployed runtime.",
  },
  {
    id: "human-disposition",
    term: "Human disposition",
    definition: "The accountable person’s recorded next step—such as hold, verify, escalate, or authorize—after considering the evidence and constraints.",
    example: "HOLD means do not act on the broad claim yet; verify a separately authored benchmark first.",
    boundary: "The person’s decision is not external truth and does not erase the underlying evidence.",
  },
  {
    id: "negative-result-commitment",
    term: "Locked negative-result commitment",
    definition: "An agreement made before a test that an unhelpful, harmful, null, or shortcut-driven result will still be reported instead of being hidden or spun as success.",
    example: "If the origin clue makes the model worse, the correct conclusion is that the clue should be rejected in this setting.",
    boundary: "It does not predict failure or authorize the study; it prevents selective interpretation after results are known.",
  },
  {
    id: "relation-codes",
    term: "DPND / INDP / UNKN",
    definition: "Short labels used in the fictional benchmark: dependent on a known upstream source, separate only as the benchmark stipulates, or unresolved.",
    example: "A different URL is not automatically INDP; when the relation is not established, it stays UNKN.",
    boundary: "The labels do not discover real provenance or certify universal real-world independence.",
  },
];

export const sources = [
  { label: "Dong, Berti-Équille & Srivastava (2009), source dependence", url: "https://www.vldb.org/pvldb/vol2/vldb09-pvldb47.pdf", use: "Published truth-discovery precedent for copying, partial dependence, and why matching values alone do not prove a shared source." },
  { label: "Senn (2009), double counting in meta-analysis", url: "https://doi.org/10.1186/1471-2288-9-10", use: "Published evidence-synthesis precedent for identifying the unit and preserving dependence rather than manufacturing precision." },
  { label: "Greenberg (2009), citation-network amplification", url: "https://pubmed.ncbi.nlm.nih.gov/19622839/", use: "Published bounded case showing how citation recurrence can create apparent authority without new data." },
  { label: "Cochrane Handbook, reports versus studies", url: "https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04", use: "Authoritative operational precedent for linking several reports to one underlying study while retaining useful secondary reports." },
  { label: "W3C PROV-O", url: "https://www.w3.org/TR/prov-o/", use: "Direct standard for entities, activities, agents, and derivation; lineage is not correctness." },
  { label: "Silcock et al. (2023), NEWS-COPY", url: "https://arxiv.org/abs/2210.04261", use: "ICLR paper defining duplicates as the same original article despite abridgement/OCR; nonduplicate does not mean a separate origin." },
  { label: "Silcock et al. (2024), Newswire", url: "https://papers.nips.cc/paper/2024/hash/58f52a01a516609336da78ff17e6f81f-Abstract-Datasets_and_Benchmarks_Track.html", use: "NeurIPS dataset paper for historical reproduction clusters; cluster size is recurrence, not origin count." },
  { label: "Zhang, Ives & Roth (2020), natural-language claim provenance", url: "https://aclanthology.org/2020.acl-main.406/", use: "Published ACL 2020 graph and inference precedent for natural-language claim provenance; inferred provenance is not the supplied benchmark relation." },
  { label: "Naphade (2026), redundant group evidence", url: "https://arxiv.org/abs/2601.06189", use: "Unreviewed arXiv v1 submitted 2026-01-08; the record notes an ACL ARR submission but no acceptance. Distinct versus paraphrased evidence is a behavioral comparator, not verified separate origins." },
  { label: "Li, Padman & Krishnan (2026), source-dependent RAG", url: "https://arxiv.org/abs/2605.29084", use: "Unreviewed arXiv v1 submitted 2026-05-27 with no venue acceptance shown; it audits cross-source answer variation, not a derivation relation." },
  { label: "Wang et al. (2025), RAMDocs", url: "https://arxiv.org/abs/2504.13079", use: "COLM conflict benchmark establishing that ambiguity, misinformation, and noise are active RAG problems adjacent to origin accounting." },
  { label: "Hossain et al. (2026), EvidentialRAG", url: "https://arxiv.org/abs/2607.10491", use: "Unreviewed arXiv v1 submitted 2026-07-11 with no venue or acceptance shown; conflict/uncertainty fusion is not provenance or source-origin inference." },
  { label: "Carbonell & Goldstein (1998), MMR", url: "https://doi.org/10.1145/290941.291025", use: "Published SIGIR 1998 diversity-reranking precedent; adjacent/future comparator, not a required F0/F1/F2 arm." },
  { label: "Lee et al. (2025), SetR", url: "https://aclanthology.org/2025.acl-long.861/", use: "Published set-wise retrieval precedent for joint coverage and redundancy reduction." },
  { label: "Verma et al. (2026), NEST", url: "https://aclanthology.org/2026.acl-industry.35/", use: "Published ACL 2026 Industry Track redundancy-removal and recall/selection precedent; adjacent/future comparator." },
  { label: "Cho & Lee (2026), RARE", url: "https://arxiv.org/abs/2604.19047", use: "Unreviewed arXiv v2; record says accepted to ACL 2026 Main Conference, but no ACL venue page was located. High-similarity redundancy comparator." },
  { label: "Schelpe (2026), byte-exact deduplication", url: "https://arxiv.org/abs/2605.09611", use: "Unreviewed arXiv v1 preprint submitted 2026-05-10; exact deduplication comparator, not an origin relation." },
  { label: "Ross et al. (2026), redundancy and diversity", url: "https://arxiv.org/abs/2608.13956", use: "Closest recent unreviewed arXiv v1 submitted 2026-08-14 with no venue or acceptance shown; controlled duplicate/paraphrase/diversity comparator, not the present origin-counting estimand." },
  { label: "Laitenberger, Manning & Liu (2025), strong RAG baselines", url: "https://aclanthology.org/2025.emnlp-main.1656/", use: "Sourced fact: published EMNLP 2025 DOS RAG and matched-budget baseline recommendation. Project inference: added structure must earn value against a simple baseline; adjacent/future comparator, not a required F0/F1/F2 arm." },
];

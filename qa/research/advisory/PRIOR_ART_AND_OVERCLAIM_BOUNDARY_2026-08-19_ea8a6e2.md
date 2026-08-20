# Prior-art and overclaim-boundary audit

**Status:** Advisory review — no canonical disposition assigned

**Reviewed commit:** `ea8a6e2383fc15f09c17522e0758decba6fe4068`

**Reviewed date:** 2026-08-19

**Scope:** Public-facing v16 manuscript artifacts and the curated Echo Problem
route, checked against the locked v16 contracts and the hash-verified v14
prior-art/evidence records. The applied framework and site were not treated as
complete at this commit: `framework/**`, `cases/**`, and `site/**` contain only
the scaffold/README material in this state, so implementation and site claims
remain subject to their later lane reviews.

## Verdict

**Pass with revisions.**

The broad v16 argument is within the approved evidence boundary. The manuscript
does not claim that the six families are newly invented, that the framework
works or improves outcomes, that a case validates it, that provenance is truth,
that recurrence is independent corroboration, or that a protocol/QA pass is a
research result. The Echo Problem is clearly described as separate, fictional
in its v16 example, unrun, and without results.

Two bounded revisions should be made before the manuscript source route is
called owner-review complete:

1. update the stale Echo paragraph in `manuscript/SOURCES_AND_RESEARCH_ROUTE.md`
   so it links to the already integrated EP v0.1 successor rather than saying
   that the material belongs there “after” integration; and
2. expose a direct, optional route to the targeted prior-art map and selected
   primary sources. This is a public-credibility and wayfinding gap, not a
   finding that the current prose overclaims.

The remaining wording cautions below are optional polish unless the text is
later presented as empirical or technical evidence.

## Integrity and review method

- Read `AGENTS.md`, the locked intent and thesis/audience contracts, artifact
  boundaries, lineage, fidelity matrix, acceptance criteria, and review
  protocol in the required order.
- Verified `(cd docs && shasum -a 256 -c OWNER_INTENT_V16.sha256)` — **OK**.
- Read all files under `manuscript/*.md`, including the revised canonical essay,
  short version, cover note, abstract, origin note, and sources route.
- Read `research/the-echo-problem/README.md`,
  `STATUS_AND_BOUNDARIES.md`, and `RELATION_TO_V16.md`.
- Read the archived v14 claims/evidence register, targeted prior-art map,
  overclaim/counterargument register, and references completely.
- Performed a contextual scan for novelty, effectiveness, causal, capability,
  independent-corroboration, provenance, result, and permission language. No
  browsing or new literature search was performed; the archived targeted map is
  the review base and is explicitly not a completeness claim.

## Claim inventory

“Strongest allowable status” uses the repository’s evidence vocabulary. A
status describes what the sentence may be used for; it does not make an owner
proposition an external finding.

| Claim surface | Exact locator(s) | Strongest allowable status | Boundary check |
| --- | --- | --- | --- |
| AI-assisted work inherits choices made before generation; generic-feeling output may reflect upstream search, comparison, omission, and memory choices | `manuscript/PATTERN_RECOGNITION_V16.md:11–27`; `NINETY_SECOND_VERSION.md:3–7`; `PUBLIC_ABSTRACT.md:3–7` | `OWNER_PREMISE` / `CONCEPTUAL_SYNTHESIS`; future benefit is a `DESIGN_HYPOTHESIS` | The prose says “may,” “can,” and “often” as the editorial framing; it does not claim a measured prevalence, model-internal cause, or demonstrated improvement. |
| The six-family arrangement | `PATTERN_RECOGNITION_V16.md:46–54`; headings at `:56`, `:87`, `:111`, `:123`, `:161`, `:179` | `HISTORICAL_V13_CLAIM` preserved by `OWNER_PREMISE` / owner-locked scope | It explicitly says the practices were not invented here and treats the families as a non-mandatory reader map, not validated topology. |
| Peripheral/specialist search can expose a candidate the default route missed | `PATTERN_RECOGNITION_V16.md:56–85` | `HISTORICAL_V13_CLAIM` / `DESIGN_HYPOTHESIS` | The specialist account is hypothetical; underweighting is expressly not truth, authority, or authorization. |
| Source role, claim support, relevance, recurrence, origin, permission, and authority must remain distinct | `PATTERN_RECOGNITION_V16.md:87–109` | `CONCEPTUAL_SYNTHESIS` with `PRIMARY_SOURCE_SUPPORTED` boundaries in the archived map | No universal trust score is proposed. Provenance is explicitly not correctness and repetition is not independent support. |
| Motion/velocity deserves examination only against a meaningful baseline | `PATTERN_RECOGNITION_V16.md:111–121`, worked example `:139–159` | `HISTORICAL_V13_CLAIM` / `DESIGN_HYPOTHESIS` | The example is hypothetical; denominator, collection-gap, and stopping cautions prevent a causal or predictive reading. |
| Expected absence and versioned memory can change what should be checked | `PATTERN_RECOGNITION_V16.md:123–159` | `HISTORICAL_V13_CLAIM` / `DESIGN_HYPOTHESIS` | Absence is tied to an explicit expectation and may be an observation gap; memory preserves source/time and does not erase history. |
| Structured comparison can reveal contrast, recurrence, or a missing perspective without making unlike cases equivalent | `PATTERN_RECOGNITION_V16.md:161–177` | `HISTORICAL_V13_CLAIM` / `CONCEPTUAL_SYNTHESIS` | A legible pattern is called a candidate explanation, not a fact or a causal conclusion. |
| Outcomes can inform bounded route updates while preserving the original record | `PATTERN_RECOGNITION_V16.md:179–199` | `HISTORICAL_V13_CLAIM` / `DESIGN_HYPOTHESIS` with an open `EMPIRICAL_HYPOTHESIS` | The manuscript explicitly warns that preference, confounding, or luck is not a new fact and that no universal weight is discovered. |
| Decomposable practices can be scaffolded without automating expertise | `PATTERN_RECOGNITION_V16.md:351–355`; `NINETY_SECOND_VERSION.md:28–33` | `OWNER_PREMISE` / `DESIGN_HYPOTHESIS` | The text says it cannot replace taste, accountability, permission, contextual judgment, or novel-situation sensemaking; it does not retain the rejected “expert-grade” historical claim. |
| Lightweight, moderate, and advanced implementation paths | `PATTERN_RECOGNITION_V16.md:231–270`; `PUBLIC_ABSTRACT.md:25–29` | `DESIGN_HYPOTHESIS` / illustrative implementation proposal | Modal language (“might,” “may”) and “naming a service ... would not establish that it works” avoid an efficacy claim. A07/A08 still require the later framework/playbook artifacts. |
| “Discrimination Layer” names a responsibility rather than a product or neural module | `PATTERN_RECOGNITION_V16.md:35–44`, `:308–313`; `PUBLIC_ABSTRACT.md:9–16` | `DESIGN_HYPOTHESIS` / owner terminology choice | The technical/social boundary is explicit; communication success remains an owner/cold-reader question, not a measured result. |
| Nine reports can share one announcement without becoming eight new origins | `PATTERN_RECOGNITION_V16.md:201–229` | `CONCEPTUAL_SYNTHESIS` plus a clearly marked fictional illustration; the future effect question is an `EMPIRICAL_HYPOTHESIS` | The example is subordinate, says the reports are not thereby false, leaves independence unestablished, and does not import an Echo result. |
| A fair matched-budget comparison could test whether extra structure is useful or merely costly | `PATTERN_RECOGNITION_V16.md:315–337`; `SOURCES_AND_RESEARCH_ROUTE.md:32–41` | `EMPIRICAL_HYPOTHESIS` / future study design | No model/provider is selected, no study is claimed, and null, harmful, shortcut, fragility, non-transfer, and stopped outcomes remain reportable. |
| Signal Foundry as an application | `PATTERN_RECOGNITION_V16.md:333–337`; `PUBLIC_ABSTRACT.md:25–29` | `CASE_DERIVED` / bounded design illustration only | The manuscript expressly says a case cannot validate the framework and that effectiveness would require an authorized comparison. |
| Prior art and non-novelty boundary | `PATTERN_RECOGNITION_V16.md:272–280`; `ORIGIN_NOTE.md:23–26`; archived `PRIOR_ART_AND_ADJACENT_FIELDS_MAP.md` | `PRIMARY_SOURCE_SUPPORTED` boundary / `CONCEPTUAL_SYNTHESIS`; targeted rather than exhaustive | The essay says search, provenance, evidence synthesis, memory, and decision support precede v16 and narrows the contribution to a possible working discipline. |
| Blanket default-model/training-data, universal capability, and generic novelty claims | Historical rows C-034/C-036/C-039 in archived `CLAIMS_AND_EVIDENCE_REGISTER.md`; current manuscript scan | `REJECTED_OR_NARROWED` historical formulations; absent from current public prose | No claim about training distributions, default GPT incapacity, universal architecture, or a novel mechanism family appears in the reviewed manuscript. |
| Echo status and no-results boundary | `research/the-echo-problem/README.md:1–21`, `:33–49`; `STATUS_AND_BOUNDARIES.md:3–18`, `:45–74`; `RELATION_TO_V16.md:5–11`, `:24–37` | Preservation/status record, not evidence of effectiveness; future study remains an `EMPIRICAL_HYPOTHESIS` | The status names no model study, no participants, no external dataset, and no results; integrity/offline tests are explicitly not research results. |

## Stable findings

These findings are the review’s recommendations, not final integration
dispositions. The primary orchestrator should assign the controlled
`Accepted`, `Accepted with revision`, `Deferred`, or `Rejected` disposition in
the project ledger if needed.

### PAOB-01 — Moderate — stale Echo route and missing direct link

**Class:** Factual route-state defect / separation wayfinding, not a thesis
overclaim.

**Exact locator:** `manuscript/SOURCES_AND_RESEARCH_ROUTE.md:23–30`.

**Governing requirement:** Owner-intent permanent two-project separation;
artifact-boundary Echo firebreak; acceptance A10 (clear link to the separate
Echo project) and A11 (claims/source route stays credible).

**Local evidence/source:** The paragraph says the Echo materials “belong in
`research/the-echo-problem/` after that track’s curated successor is
integrated.” At the reviewed commit, the EP v0.1 successor is already present
and integrated (`research/the-echo-problem/README.md`, `STATUS_AND_BOUNDARIES.md`,
and `RELATION_TO_V16.md`; the integration record is also documented in
`docs/ADVISORY_REVIEW_DISPOSITIONS.md` under ECHO-01–ECHO-04).

**Recommendation:** Replace the future-tense/pending wording with a direct
Markdown link to the EP v0.1 README and status page, state that the curated
successor is present but unrun/no-results, and retain the sentence that the
v16 manuscript uses only the fictional example. Do not pull the protocol into
the essay.

**Rationale:** A reader following the optional route should not be told to wait
for a curation that has already occurred. The stale sentence can make a
completed preservation step look absent, while a plain path in backticks is
weaker than a clear project link. This is a route defect, not evidence that the
Echo/v16 separation failed.

### PAOB-02 — Moderate — prior-art route is too indirect for public credibility

**Class:** Source-route gap; not a present overclaim defect.

**Exact locator:** `manuscript/SOURCES_AND_RESEARCH_ROUTE.md:7–21` and the
prior-art claim at `manuscript/PATTERN_RECOGNITION_V16.md:272–280`.

**Governing requirement:** Thesis contract evidence boundary; acceptance A11;
the archived prior-art map’s instruction that the map is targeted and not an
exhaustive review.

**Local evidence/source:** The essay responsibly says that search, source
evaluation, provenance, evidence synthesis, memory, and decision support
precede the arrangement. The optional route links the v13 recovery memo and
the v14 thought piece, but not the archived
`03_RESEARCH_PACKAGE/PRIOR_ART_AND_ADJACENT_FIELDS_MAP.md`, its
`REFERENCES.md`, or a small set of direct primary/official sources. The
archived map itself records mature overlap across information foraging,
relevance feedback, provenance, evidence synthesis, mixed initiative, RAG,
agent memory, calibration, and organizational learning, while explicitly
calling its coverage targeted.

**Recommendation:** Add an optional “targeted prior-art map” link and a short
selected-source list or links for the most material boundaries: information
foraging/value of information, provenance/claim evidence, common-origin
collation, RAG/context selection, memory, and mixed initiative. Label the route
as targeted rather than complete, preserve preprint labels, and carry the
archived access date or re-verify the links before public release.

**Rationale:** The current essay is not making a novelty claim, so this gap
does not make it scientifically false. Direct wayfinding lets a skeptical
reader verify the deliberate narrowing without turning the thought piece into
a literature review. It also prevents the V14 thought piece from appearing to
be the only prior-art basis.

### PAOB-03 — Low / optional citation polish — rhetorical prevalence and
capability wording

**Class:** Potential reader interpretation risk; not a material defect under
the locked owner intent.

**Exact locator:** `manuscript/PATTERN_RECOGNITION_V16.md:18–21` (“AI slop often
begins ...”) and `:58–60` (“the path most likely to be repeated”).

**Governing requirement:** Owner-intent provisional editorial center; fidelity
matrix guard against universal/default-model claims; thesis contract maximum
scientific claim.

**Local evidence/source:** The same upstream framing is owner-approved in
`docs/OWNER_INTENT_V16.md`. The current wording does not assert a measured rate,
all-model behavior, training-data fact, or causal effect; the surrounding
paragraphs use conditional and experiential language.

**Recommendation:** Preserve the owner’s strong framing for the human essay, or
if the site later presents it as technical fact, soften to “can begin” / “may
be repeated” or route a primary source to the claim. Do not introduce a generic
model-training explanation merely to justify the rhetoric.

**Rationale:** This is an optional credibility refinement, not an overclaim
finding. Changing it is not necessary to protect the locked proposition, and
the archived v14 register specifically rejects blanket default-GPT claims.

### PAOB-04 — Release-gate scope note — implementation claims cannot yet be
certified at this commit

**Class:** Completeness limitation, not an overclaim in the manuscript.

**Exact locator:** `manuscript/PATTERN_RECOGNITION_V16.md:231–270` and the
active tree at `ea8a6e2` (`framework/**`, `cases/**`, and `site/**` are still
scaffolds/README material).

**Governing requirement:** Acceptance A07–A09 and the artifact-boundary rule
that the essay is not the builder framework or agent companion.

**Local evidence/source:** The essay presents light/moderate/advanced paths
with modal language and says naming a service would not establish that it
works. The full applied framework/playbook and bounded cases are not part of
the reviewed commit, so inputs, outputs, failure modes, receipts, stop rules,
and Signal Foundry translation cannot be certified from this state.

**Recommendation:** Keep the manuscript language as design proposal. Do not
describe `ea8a6e2` alone as a complete applied-framework release. Re-run this
lane after the playbook/cases branch is integrated, and inspect every concrete
implementation or case claim against the same status vocabulary.

**Rationale:** This prevents an editorial pass from being mistaken for A07/A08
evidence. It is a dependency and review-scope note, not a defect in the
manuscript’s cautious wording.

## Required boundary confirmations

### Echo/v16 separation — confirmed, with PAOB-01 route repair

The separation passes the substantive firebreak at this commit:

- The broad essay opens with generic-feeling output and upstream choices; the
  common-origin example first appears at `PATTERN_RECOGNITION_V16.md:201`, after
  all six families and the motion/absence example.
- The example is explicitly fictional (`:206`), subordinate (`:203–204`), and
  removable without collapsing the broad thesis (`:224–229`).
- The separate EP README identifies ECHO-01 / EP v0.1, says it is unrun/no
  results/not published, and states that v15.2 remains historically named and
  byte-preserved (`README.md:1–21`).
- EP status explicitly says no model/empirical/pilot/participant study ran, no
  model/provider was called by this curation, no participants were contacted,
  and no external dataset was acquired (`STATUS_AND_BOUNDARIES.md:8–18`).
- The preserved unfavorable classes are marked as possible planned outcomes,
  not observed results (`STATUS_AND_BOUNDARIES.md:45–67`).
- The relationship document says Echo cannot define v16, replace the six
  families, or supply results (`RELATION_TO_V16.md:5–11`, `:24–37`).

The only separation issue found is the stale/pending language in the optional
manuscript source route (PAOB-01). It should be repaired for accurate wayfinding;
it does not change the substantive verdict.

### No-results language — confirmed

The v16 manuscript says no study has run and no model/provider was selected as
evidence (`PATTERN_RECOGNITION_V16.md:326–331`), says protocols, fixtures,
planning simulations, and validators are not empirical results (`:326–330`),
and keeps Signal Foundry in the bounded illustration category (`:333–337`).
The Echo status adds the explicit no-results declaration and distinguishes
integrity/offline tests from research outcomes. No QA pass, hash, fixture,
protocol, model-assisted editorial review, or preserved historical result is
presented as evidence that v16 works.

## Missing citation/source-route needs

The following are recommendations for credibility and verification, not claims
that the current manuscript is false:

1. Add the targeted prior-art map and references to
   `SOURCES_AND_RESEARCH_ROUTE.md`, with an explicit “targeted, not exhaustive”
   label.
2. Link a small set of primary/official sources already listed in the archive:
   W3C PROV-O for lineage, the NeurIPS RAG paper for retrieved context,
   Pirolli & Card for information foraging, Howard/Russell & Wefald for
   value-of-information/metareasoning, Zhang–Ives–Roth for claim provenance,
   Cochrane’s current handbook for collating common-origin reports, and
   Horvitz/Amershi for mixed initiative and human correction. These links can
   remain an optional deeper route rather than footnotes in the human essay.
3. If the route mentions recent RAG, memory, or provenance systems, keep the
   archive’s distinction between peer-reviewed/official sources, preprints,
   industry guidance, and working artifacts. Do not turn a targeted map into a
   completeness claim.
4. Link directly to EP v0.1’s README and status/no-results page once PAOB-01 is
   repaired; do not link only to a future directory path.

## Overall assessment by risk class

| Risk class | Result |
| --- | --- |
| Generic novelty / “new field” claim | **No defect found.** The manuscript explicitly says the work is old under a new arrangement and asks for fair comparison. |
| Capability absolute / training-data or default-model claim | **No defect found.** Historical blanket claims are narrowed/rejected in the archive and do not appear in current prose. |
| Causality / effectiveness / “works” implication | **No defect found.** Modal proposal language, future-test framing, and explicit no-results language are used. |
| Peripheral = true / provenance = truth / recurrence = independence | **No defect found.** Each boundary is stated in the essay and short version. |
| Case = validation / QA = research result | **No defect found.** Signal Foundry and Echo tests are explicitly bounded. |
| Six-family erasure or Echo takeover | **No defect found.** All six families remain visible; Echo arrives later and is removable. |
| Public source credibility and route accuracy | **Revision needed.** PAOB-01 and PAOB-02. |
| Builder/playbook acceptance | **Not yet auditable at this commit.** PAOB-04; recheck after integration. |

No final `Accepted`, `Accepted with revision`, `Deferred`, or `Rejected`
disposition is assigned here; those belong to the primary integrator’s
disposition ledger.

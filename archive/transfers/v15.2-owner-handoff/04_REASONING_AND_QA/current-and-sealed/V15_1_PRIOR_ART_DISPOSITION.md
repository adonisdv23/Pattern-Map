# v15.1 prior-art disposition

- **Lane:** bounded prior-art consolidation
- **Date:** 2026-08-18 (America/New_York)
- **Branch:** `codex/v15-1-prior-art`
- **Status:** `CONSOLIDATED_WITH_BOUNDARY`
- **Scope:** close the demonstrated Pochampally/graded-source-dependence gap; audit principal novelty wording; do not reopen an unlimited literature search
- **Empirical status:** no model, provider, participant, dataset, deployment, or external transfer was run

## Decision

Accept Pochampally et al.’s *Fusing Data with Correlations* (SIGMOD 2014) as a
bounded prior-art correction. The paper is a direct precedent for a point that
was present in the overnight research but missing from the canonical v15
prior-art ledger: source correlation is broader than literal copying. Positive
correlation can arise from common extraction rules without copying; negative
correlation can arise from complementary source domains or extractors.

This closes a consolidation gap, not a novelty gap. The canonical claim remains
narrow: `DPND`, `INDP`, and `UNKN` are three task-specific,
benchmark-stipulated accounting states for the proposed diagnostic. They are
not a complete source-dependence ontology, a real-world independence claim, or
a learned origin detector. A future extension may need typed relation,
direction, scope, time, confidence, and relation provenance, but those fields
are not added to the locked F0/F1/F2 study in this lane.

## Evidence used

The source was checked through the primary records:

- [ACM DOI record](https://doi.org/10.1145/2588555.2593674)
- [Authors’ primary PDF](https://people.cs.umass.edu/~ameli/projects/dataIntegration/papers/corrFusion-SIGMOD2014.pdf)

The paper is a published SIGMOD 2014 conference contribution, pages 433–444,
by Ravali Pochampally, Anish Das Sarma, Xin Luna Dong, Alexandra Meliou, and
Divesh Srivastava. It studies structured data fusion with correlated sources;
it does not evaluate natural-language claim provenance, LLM cue use, or the
current F2-versus-F1 estimand. Those boundaries are preserved.

## Changes made

1. Added source card **S20** to `research/PRIOR_ART_DELTA_V1.md`, including
   sourced fact, exact finding, project inference, blocked claims, residual
   contribution, and disposition.
2. Added S20 to the ledger’s search scope, primary URL index, analogies, and
   unresolved-boundary notes.
3. Added the Pochampally paragraph to the manuscript’s prior-art section and
   updated the source-ledger pointer from S1–S19 to S1–S20.
4. Added the full bibliographic record to `research/REFERENCES.md` and
   `research/references.bib`.

## Novelty-language audit

The canonical manuscript and prior-art delta were searched for principal-risk
terms: `first`, `nobody`, `no one`, `unoccupied`, `unprecedented`, `unique`,
`novel`, `new universal`, and `never been studied`.

No unqualified principal claim of being first, being the only work, or
occupying an unoccupied mechanism space was found in the canonical manuscript
or delta. The remaining hits are boundary statements that explicitly reject
or qualify those claims, such as “the component ideas are not blank territory”
and “the project cannot claim ... unoccupied.” The manuscript’s surviving
contribution is described as a synthesis/design hypothesis plus a narrow,
observable-condition study—not as a new universal layer or a provenance
discovery mechanism.

## Deliberately not changed

- No new empirical arm was added.
- No `DPND`/`INDP`/`UNKN` protocol state was redefined.
- No claim was made that source correlation transfers directly from structured
  truth discovery to natural-language or LLM settings.
- No broad literature sweep, patent search, external dataset acquisition, or
  venue-status expansion was undertaken.
- The site, protocol code, deployment configuration, and other worktrees were
  not touched.

## Parent integration note

The parent v15.1 integrator should propagate S20’s status into any regenerated
claim/source matrix, owner packet, site source route, or release manifest. The
smallest correct propagation is a citation and boundary update; it should not
turn the future typed-correlation extension into a current protocol
requirement.


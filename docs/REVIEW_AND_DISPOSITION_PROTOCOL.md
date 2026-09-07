# Review and disposition protocol

Status: **BINDING INTEGRATION WORKFLOW**

This protocol governs every subordinate-task handoff, advisory report, red-team
finding, and final acceptance review. A long or confident review is not evidence
and is not accepted merely because it is detailed. The primary orchestrator is
the sole integrator.

## Review sequence

1. Verify the contributor's branch, base commit, exclusive path ownership, and
   clean final status.
2. Inspect the actual diff and artifacts rather than relying on the contributor's
   summary.
3. Re-run the narrow checks reported by the contributor, then the relevant
   governing acceptance checks.
4. Verify `docs/OWNER_INTENT_V16.sha256` before and after integration.
5. Assign each material recommendation or finding one disposition from the
   controlled set below.
6. Record the reason, affected canonical files, governing requirement, and
   integration action or follow-up owner decision.
7. Integrate only reviewed commits; record any integrator revision separately.

## Controlled dispositions

| Disposition | Meaning | Required record |
| --- | --- | --- |
| **Accepted** | The recommendation directly satisfies a governing requirement and can be integrated as proposed | Reason, affected files, governing requirement, integration commit |
| **Accepted with revision** | The underlying finding is valid, but the proposed expression or implementation requires a bounded change | Reason, original and revised treatment, affected files, governing requirement, integration commit |
| **Deferred** | The finding is relevant but belongs to a later dependency, needs evidence not yet available, or is outside the present release gate | Reason, destination phase or decision owner, affected files, governing requirement |
| **Rejected** | The recommendation conflicts with authority, repeats resolved work, exceeds evidence, weakens the artifact for its reader, or falls outside scope | Reason, affected files if any, governing requirement or boundary |

No fifth category such as `noted`, `consider`, or `mostly accepted` may hide an
undecided recommendation. Small copyedits can be grouped when they have the same
reason and governing requirement.

## Advisory-report rules

- Advisory agents are read-only except for one uniquely named report path named
  in their assignment.
- Reports identify the exact commits and files reviewed.
- Findings distinguish factual defects, intent drift, usability risk, claim
  overreach, and optional preference.
- A proxy reader may report comprehension friction but may not claim to be the
  mentor, the public, or evidence of measured comprehension.
- A model review is never a scientific source, an owner instruction, or proof
  that a procedure works.
- Proposed changes to locked owner intent are recorded as
  `PROPOSED — OWNER DECISION REQUIRED` and cannot be integrated automatically.

## Planned advisory waves

| Wave | Lane | Intended report family | Dependency |
| --- | --- | --- | --- |
| 1 | V13 continuity and owner-intent fidelity | `qa/editorial/advisory/V13_CONTINUITY_AND_INTENT_FIDELITY_*.md` | Phase 1 checkpoint; relevant draft available |
| 1 | Prior-art and overclaim boundary | `qa/research/advisory/PRIOR_ART_AND_OVERCLAIM_BOUNDARY_*.md` | Relevant manuscript/framework claims available |
| 1 | Mentor-reader and anti-slop editorial audit | `qa/editorial/advisory/MENTOR_READER_ANTI_SLOP_*.md` | Manuscript draft available |
| 2 | Agent-playbook usefulness and Signal Foundry translation | `qa/applied/advisory/PLAYBOOK_AND_SIGNAL_FOUNDRY_*.md` | Integrated playbook and cases |
| 2 | Site comprehension and accessibility | `qa/site/advisory/SITE_COMPREHENSION_ACCESSIBILITY_*.md` | Rendered site |
| 2 | Echo Problem research-separation integrity | `qa/research/advisory/ECHO_SEPARATION_INTEGRITY_*.md` | Integrated EP v0.1 accession and curation |
| Final | Hostile novelty reviewer | `qa/research/advisory/HOSTILE_NOVELTY_REVIEW_*.md` | Owner-review candidate |
| Final | Cold nontechnical reader | `qa/editorial/advisory/COLD_NONTECHNICAL_READER_*.md` | Owner-review candidate |
| Final | Builder/operator acceptance reviewer | `qa/applied/advisory/BUILDER_OPERATOR_ACCEPTANCE_*.md` | Owner-review candidate |

Report suffixes use the review date and reviewed short commit, so repeated loops
never overwrite earlier advice.

## Disposition ledger schema

Every material entry in `docs/ADVISORY_REVIEW_DISPOSITIONS.md` records:

- stable finding ID and advisory lane;
- reviewed commit or artifact state;
- concise recommendation;
- disposition from the controlled set;
- integrator reason;
- affected files;
- governing requirement;
- implementation commit or explicit follow-up owner decision; and
- verification status.

## Conflict handling

When reviews disagree, the authority order governs. Preserve useful tension in
the ledger instead of blending incompatible recommendations into vague prose.
Research can narrow a claim; it cannot silently redefine the thesis. Editorial
clarity can simplify expression; it cannot erase a family or a boundary.
Implementation convenience can change a mechanism; it cannot turn a proposed
architecture into a universal requirement.

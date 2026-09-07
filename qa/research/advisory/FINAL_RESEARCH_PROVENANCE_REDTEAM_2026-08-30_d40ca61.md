# Final research and provenance red team — `d40ca61`

**Reviewed checkpoint:** `d40ca61c7b64ce89aabac2e36170e701b69c94d6`
**Review date:** 2026-08-30
**Lane:** independent read-only research / claims / provenance review

This report preserves advisory model feedback. It is not a literature review,
novelty clearance, experiment, model or participant study, owner approval, or
evidence of effectiveness. The reviewer verified the exact clean checkpoint
and locked owner-intent hash, reopened a bounded set of primary/official source
routes, ran provider-free structural checks, and made no repository edits.

## Verdict

No P0. One expected P1 terminal-packaging condition, two P2 process/verification
defects, and one P3 manifest-scope clarity issue were reported. No actionable
research-claim, prior-art, current-source, provisional-study, or Echo-separation
defect was found. The contribution ceiling remained defensible at the evidence
level available.

## Findings

| ID | Priority | Finding | Evidence at reviewed checkpoint | Smallest safe correction |
| --- | --- | --- | --- | --- |
| RP-01 | P1 terminal gate | The owner manifest was intentionally stale after convergence edits, and the Signal Foundry builder correctly refused a commit that was not the exact named branch tip. | D-036; `handoff/verify_owner_review_package.py`; `handoff/signal-foundry/build_portable_bundle.py`; portable tests | Finish source/evidence edits, regenerate manifest last, push/read back exact tip, run clean-clone suite, then build and externally verify the exact-tip ZIP. Do not weaken fail-closed checks. |
| RP-02 | P2 | D-036 said later evidence would be written into a manifest-covered QA narrative, contradicting the non-self-referential sealing design. | `docs/DECISION_LOG.md`; `qa/handoff/PUBLIC_AND_TRANSFER_HARDENING_QA_2026-08-30.md`; `qa/README.md` | Put remote/PR/ZIP observations in an external exact-hash terminal attestation, not back into a manifest-covered file. |
| RP-03 | P2 | The twelve-stage runner omitted the new research-convergence unit suite required by the research QA instructions. | `qa/run_owner_review_checks.sh`; `qa/research/README.md`; `qa/research/test_research_claim_convergence.py` | Run unittest discovery during research stage 9. |
| RP-04 | P3 | The package map described `qa/research/**`, while the bounded owner manifest omitted the newest convergence QA and unit test. | `handoff/PACKAGE_MAP_V16.md`; `handoff/verify_owner_review_package.py` | Add the final research-convergence files to the bounded manifest or narrow the package-map claim. |

## Research and claims pass areas

- The contribution is framed as an authored, proportional, human-governed
  design/governance synthesis and testable agenda—not a novel mechanism,
  exhaustive taxonomy, validated method, universal architecture, or proven
  effectiveness claim.
- Current 2025–2026 sources are explicitly targeted rather than systematic;
  primary/official routes and publication-status caveats were retained.
- Candidate A remains fixed-answer interface research; Candidate B remains
  provisional; no paper order, model, provider, corpus, sample, registry, or
  run is selected.
- Echo remains separate, unrun, no-results, and unable to redefine v16.
- Synthetic fixtures and implementation checks remain labeled as such.

## Evidence boundary

The bounded source recheck cannot establish an exhaustive literature search,
technical novelty, real-world performance, empirical benefit, participant
response, or publication readiness. Publication-time source and status checks
remain required.

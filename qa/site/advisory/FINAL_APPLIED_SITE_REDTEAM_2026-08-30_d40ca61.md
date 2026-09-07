# Final applied and site contract red team — `d40ca61`

**Reviewed checkpoint:** `d40ca61c7b64ce89aabac2e36170e701b69c94d6`
**Review date:** 2026-08-30
**Lane:** independent read-only applied / interaction / site review

This report preserves advisory model feedback. It is not a runtime trial, a
live-agent result, a permission judgment, an accessibility study, or evidence
of effectiveness. The reviewer verified the locked owner intent and exact
clean checkpoint, inspected source and generated output, exercised provider-
free contracts, and made no repository edits.

## Verdict

No P0. Three P1 contract defects, three P2 contract/portability defects, and
one P3 semantic-markup defect were reproduced. Home, Map, the visible F2 pane,
responsive layouts, and the ordinary plus 144 layered Apply combinations
otherwise behaved as intended.

## Findings

| ID | Priority | Finding | Reproduction at reviewed checkpoint | Smallest safe correction |
| --- | --- | --- | --- | --- |
| AS-01 | P1 | The outcome validator rejected `LEARNING_PLANNED` yet admitted claimed results, reviews, dispositions, or updates in pending/non-applicable states. | `qa/applied/validate_framework.py`; adversarial mutations based on `qa/applied/receipts/layered-ready.json` | Use an exact status-discriminated outcome schema and positive/negative transition controls. |
| AS-02 | P1 | The advertised fail-closed recommendation API rejected five selector names but accepted arbitrary route, evidence, execution, outcome, learning, stop, and human-disposition fields. | `site/src/recommendation.js`; `qa/interaction/apply-state-contract.spec.mjs` | Ordinary accepts exactly `{evidenceSelection}`; layered accepts exactly the six declared selector fields. |
| AS-03 | P1 | `framework/IMPLEMENTATION_CHOICES.md` allowed volume or longevity to imply Advanced, while executable Apply required consequential work, high uncertainty, and substantial separately approved capacity together. | framework, playbook, recommender, and cross-artifact test | Use the three-part conjunction everywhere; treat volume, reuse, and longevity as capability-shaping considerations only. |
| AS-04 | P2 | The no-script guide listed separate rows but did not tell a reader which action controls when permission, human gate, and capacity mismatch overlap. | `site/build.mjs`; generated public Apply | Add explicit precedence and a capacity-mismatch branch, then contract-test conflict cases. |
| AS-05 | P2 | The release validator accepted localhost, private/loopback/unspecified addresses, dotless internal hosts, and reserved example/test destinations as usable. | `site/src/publication-config.mjs`; public-mode release tests | Reject obviously non-public hosts deterministically; keep reachability and link checks as publication-time human gates. |
| AS-06 | P2 | The executable Advanced evidence receipt could not carry F2 role, track record, claim-scoped authority, support, recurrence/origin, relevance, provenance, and permission separately. | `qa/applied/validate_framework.py`; evidence fixtures; `framework/templates/EVIDENCE_REGISTER.md` | Extend the exact receipt schema and fixtures with the F2 dimensions and removal/collapse mutations. |
| AS-07 | P3 | Multiple “when not to use” clauses were concatenated without punctuation or semantic separation. | `site/build.mjs`; generated family detail | Render a semantic list. |

## Pass areas

- The visible Apply form preserved typed permission, a separate human action
  gate, capacity mismatch, and unobserved event state across 145 planning
  inputs.
- The Map retained the six locked families, and the rendered F2 pane visibly
  kept the required source-weighing dimensions distinct.
- Generated review/public manifests retained the same route IDs, source
  hashes, claim anchors, and family tuple.
- Responsive Map and standalone structural checks passed in the audited scope.

## Evidence boundary

The review was source, generated-artifact, and synthetic contract evidence. It
does not establish truthful evidence content, legal authorization, live-agent
compliance, physical accessibility, human comprehension, answer quality, or
framework effectiveness.

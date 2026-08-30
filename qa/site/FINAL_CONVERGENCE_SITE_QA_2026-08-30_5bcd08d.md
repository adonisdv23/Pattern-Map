# Final convergence site QA — 2026-08-30

Status: **PASS FOR EXACT IMPLEMENTATION CHECKPOINT `5bcd08d` — PHYSICAL AND
OWNER GATES REMAIN OPEN**

This report covers the shared-source review/public site, F2 reader contract,
Apply planning surface, and publication-readiness gate after the applied and
research convergence lanes were integrated. It is artifact, browser, and
procedural evidence only. It is not a participant result, a comprehension
study, an effectiveness result, a deployment, or a publication.

## Governing intent

The first screen must begin with the human problem; the three principal doors
must feel substantial; all six families must remain visible; origin accounting
must remain subordinate; technical detail must use progressive disclosure;
and Apply must expose observable, proportionate behavior without manufacturing
a run, result, permission decision, or human disposition.

The locked owner-intent checksum passed before this review.

## Findings and dispositions

| ID | Finding | Disposition | Result at `5bcd08d` |
| --- | --- | --- | --- |
| FC-SITE-01 | The teaching reveal previously appeared before the three principal doors, making the opening feel like another explanatory document instead of a useful public choice. | **Accepted** | Home now presents headline, standfirst, then the three substantial doors. The plain bridge, term help, Guided route, and reveal follow. Static order contracts fail if this regresses. |
| FC-SITE-02 | The prior Apply classifier blurred a genuine ordinary transformation with layered evidence work and collapsed permission and human approval. | **Accepted with revision** | Stage 0 ordinary accepts only the evidence-selection answer `none`, rejects any supplied layered field, returns exactly `ORDINARY_RECORD` plus the four-field ordinary boundary, and creates no route/event semantics. Layered work covers consequence, uncertainty, approved capacity, four permission states, and an independent human-action gate. |
| FC-SITE-03 | A larger budget could be misread as a reason to choose Advanced, while an under-resourced high-consequence/high-uncertainty route could proceed silently. | **Accepted** | Advanced now requires consequence + high uncertainty + substantial approved capacity. A quick/bounded mismatch yields `NARROW_OR_ESCALATE` and `CLARIFY` unless a stronger permission or human gate already blocks it. Substantial capacity on a lightweight route is visibly `EXCEEDS_WARRANTED_SCOPE`; it does not enlarge the route. |
| FC-SITE-04 | F2 needed one stable public question that included both source and information path, a plainer bridge, and a concise boundary that did not collapse recurrence, authority, support, relevance, origin, or permission. | **Accepted** | The exact reader question is “What role does each source and information path play for this exact claim?” Closed implementation detail retains source role, track-record evidence, claim-scoped authority, support, relevance, recurrence, origin, provenance, and permission. |
| FC-SITE-05 | The detailed Signal Foundry case dominated the ordinary public Examples route. | **Accepted with revision** | The case remains open in review mode for owner inspection and closed by default in public mode. Its `ILLUSTRATION_ONLY / READ_ONLY / NOT_VALIDATION` label remains unchanged. |
| FC-SITE-06 | A release build could publish a social image without alternative text. | **Accepted** | `social_image_alt` is now a required release field. The release adapter emits both Open Graph and Twitter image alternatives only after the independent `--release` flag and valid publication configuration pass. The current value remains `null`, so the public preview stays `noindex,nofollow`. |
| FC-SITE-07 | One suggested state-matrix approach treated disabled layered fields as meaningful Stage 0 inputs and collapsed all of them to ordinary. | **Rejected; strict API accepted** | The UI disables all five layered groups during ordinary work and the pure API fails closed if any is supplied. The durable matrix is one valid ordinary state plus 144 valid layered states, not 288 raw form combinations that normalize invalid input. |

## Deterministic verification

The following commands passed against the implementation checkpoint:

```text
npm run build
npm run check
python3 qa/site/audit_site.py
python3 qa/editorial/validate_content_interface.py
python3 qa/applied/validate_framework.py
python3 qa/research/validate_research_boundaries.py
python3 -m unittest discover -s qa/research -p 'test_*.py' -v
python3 -m unittest discover -s research/the-echo-problem/v1_1/harness -p 'test_*.py' -v
python3 research/the-echo-problem/qa/verify_preserved_sources.py
```

The site suite built ten review routes, ten public routes, and both standalone
exports. It passed route/source parity, no-script meaning, semantic hierarchy,
link integrity, release gating, map layout, term-panel geometry, reader
language, stylesheet reachability, one ordinary + 144 layered Apply states,
and cross-artifact Apply parity. The standard Echo v1.1 run passed 11 tests and
skipped its explicitly optional tokenizer import; the already preserved
ephemeral `tiktoken 0.14.0` receipt covers the same frozen 300-pair real-BPE
fixture. No model was called.

## Live in-app Browser review

The public preview was served locally at `http://127.0.0.1:4173/` and inspected
through the in-app Browser rather than inferred from static screenshots.

- At 1440×900, Home had no document-level horizontal overflow. The three doors
  measured 374.4×272.0 pixels each and appeared immediately after the
  standfirst. Their top 234 pixels were visible in the initial viewport.
- At 390×844, the standfirst ended at y=571.4 and the one-column door grid began
  at y=590.6. The explanatory bridge followed the complete door grid. Document
  scroll width equaled the 390-pixel viewport.
- The current Map showed exactly six family cards, a shared decision/permission
  anchor, optional records, and four limited relationship bands without a
  connector topology. F2 displayed the exact question and boundary above.
- The common-origin figure rendered as nine report chips, a readable
  left-to-right “trace known paths” bridge, one known announcement, `09`
  observations, `01` known origin, `00` counted support paths, and independence
  `UNKNOWN`. No diagonal trace collision was present.
- At 390×844, the Apply form and recommendation card each measured 370 pixels
  wide inside the 390-pixel viewport. All five layered groups were initially
  disabled and the recommendation showed `ORDINARY_RECORD`, permission/human
  gate/capacity `NOT_APPLICABLE`, and unchanged observed state.
- A submitted consequential + high-uncertainty + quick-capacity + `UNKNOWN`
  permission scenario returned `ESCALATE`, preserved `UNKNOWN`, reported
  `NARROW_OR_ESCALATE`, and kept execution `NOT_RUN`.
- The same scenario with `AUTHORIZED` permission returned `CLARIFY` because the
  approved capacity was insufficient; execution remained `NOT_RUN`, outcome
  `NOT_OBSERVED`, and human disposition `NOT_RECORDED`.

Tracked visual evidence:

- `qa/visual/final-convergence/home-public-1440x900.jpg`
- `qa/visual/final-convergence/map-public-1440x900.jpg`
- `qa/visual/final-convergence/common-origin-public-1440x900.jpg`
- `qa/visual/final-convergence/apply-public-390x844.jpg`

The capture bytes are unchanged. Their filename extensions were corrected from
`.png` to truthful `.jpg` during the final package-wide image-signature audit.

## What remains genuinely manual

This checkpoint does not close a physical end-to-end keyboard traversal,
VoiceOver/NVDA review, real 200% browser/OS zoom, real forced-colors mode,
native print preview, hardware touch, mentor comprehension, owner voice/taste,
or publication-time link/metadata checks. The secondary PDF is intentionally
an untagged visual companion; semantic standalone HTML remains the accessible
portable route. Publication identity, canonical URL, social image, social
image alternative text, deployment, and publication remain unset and
unauthorized.

# Formative origin-accounting reader study

**Protocol version:** 0.1 design draft  
**Prepared:** 2026-08-18  
**Status:** proposed HCI design only; no participant has been contacted, recruited, recorded, or studied  
**Separation rule:** this study cannot validate, rescue, or modify the model-only F2-versus-F1 benchmark. It tests comprehension of reader-facing representations, not model efficacy, provenance discovery, truth, accessibility conformance, or population prevalence.

## Answer first

Run a small, explicitly formative comparison only after the appropriate ethics or exemption determination. The decision question is whether the semantic origin-accounting receipt remains understandable without generated imagery and whether the archived H1 “evidence aperture” image introduces a pipeline, gatekeeper, or truth-filter interpretation.

The current local handoff defaults to **no H1**. This protocol preserves H1 as an experimental candidate; it does not justify rendering it in the final surface before a study.

## Fixed design

- Target exactly eight adults who did not author the page, image prompts, or research memos.
- Use a within-reader four-condition design, one exposure per condition:
  1. `C1_CURRENT_IMAGE` — earlier large H1 placement plus E2 and the semantic receipt;
  2. `C2_DEMOTED_H1` — semantic receipt first, smaller H1 later, plus E2;
  3. `C3_NO_H1` — semantic receipt and E2 only;
  4. `C4_TEXT_ONLY` — semantic receipt with all editorial rasters blocked.
- Assign conditions with this frozen 4×4 Latin square, repeated twice across eight readers:

| Order group | Position 1 | Position 2 | Position 3 | Position 4 |
| --- | --- | --- | --- | --- |
| A | C1 | C2 | C4 | C3 |
| B | C2 | C3 | C1 | C4 |
| C | C3 | C4 | C2 | C1 |
| D | C4 | C1 | C3 | C2 |

- Use four semantically equivalent fictional packet forms whose names, dates, claim wording, and surface prose differ while preserving the same origin structure and count logic. Rotate forms independently of condition so a reader cannot answer by remembering the previous packet.
- Freeze the pages, packet forms, allocation, scoring rubric, timing script, exclusion codes, and analysis template before the first exposure.

## Ten-item comprehension and boundary rubric

Each exposure asks the reader to answer, without coaching:

1. How many observations are preserved?
2. How many known common-origin clusters are recorded?
3. How many supporting origins are counted under the stated relation rule?
4. Does `UNKNOWN` mean dependent, separate, or unresolved?
5. Are B1/C1 established as support for the claim?
6. Does the receipt decide whether the claim is true?
7. Does `HOLD` automatically reject the tool or action?
8. Is the historical v13 image the current v14 topology?
9. If H1 is visible, is it an illustration, a process diagram, or a measured result?
10. What is the next human-owned step stated by the receipt?

The four critical topology errors are: `09` interpreted as nine origins; `01` interpreted as one source record rather than one known common-origin cluster; H1 interpreted as the current system pipeline; or `HOLD` interpreted as automatic rejection. The answer key and boundary explanations are frozen before recruitment.

## Session procedure

1. Provide the consent script, study boundary, withdrawal route, compensation terms, and accessibility choices.
2. Assign the reader’s Latin-square order and packet-form rotation from the frozen allocation file.
3. Start timing when the assigned surface is fully visible; stop when the ten-item response is submitted.
4. Record item responses, confidence, effort, total time, scrolling/crop observations, and a short free-text explanation. Do not treat confidence as correctness.
5. Do not record screen, video, voice, or identifying metadata unless the participant separately opts in. Declining recording does not prevent participation.
6. Two scorers who cannot see condition labels or study hypotheses independently score the responses. The named third adjudicator resolves disagreements under the frozen codebook.

## Accessibility and accommodation

Offer keyboard-only, screen-reader, 200% zoom/reflow, high-contrast, and text-only versions. Collect only accommodation information needed to run the session. Do not publish a participant’s disability or assistive-technology details when they could identify that person. A single assistive-technology user cannot establish accessibility or WCAG conformance; their observations are formative design evidence only.

## Missingness, scoring, and local design gates

- `CORRECT`, `INCORRECT`, `UNCLEAR`, `NO_RESPONSE`, `TECHNICAL_FAILURE`, and `WITHDRAWN` are the only response-state codes.
- `UNCLEAR` and `NO_RESPONSE` remain in the eight-reader denominator and do not count as correct.
- `TECHNICAL_FAILURE` triggers a replay only if the failure happened before exposure; otherwise preserve it and report the gate as unevaluable for that item.
- If fewer than eight participants complete, report observations only and label every eight-reader gate `NOT EVALUATED`; do not change the denominator.
- Two blinded scorers report raw agreement and Cohen’s kappa with a bootstrap 95% interval. If the frozen prevalence diagnostic makes kappa unstable, report that fact and the predeclared Krippendorff nominal alpha; do not select a favorable statistic afterward.
- Local design gates, not population estimates:
  - all eight readers correctly separate observations, known origin clusters, and supporting-origin count in the no-H1 condition;
  - no more than one of eight readers makes any one critical topology error in the chosen handoff condition;
  - no image condition reduces critical-item accuracy by more than one response out of eight relative to no-H1;
  - every keyboard/screen-reader/zoom blocker is corrected or explicitly recorded before any external share.

Do not report p-values, confidence intervals as population prevalence, “X% of users,” general usability, calibrated reliance, improved decisions, accessibility conformance, or efficacy from this sample. Report reader-by-item counts, error examples, timing as descriptive context, and the concrete revision decision.

## Ethics, privacy, and governance gate

Before recruitment, obtain the applicable institutional IRB/ethics determination or documented exemption; finalize the consent script, compensation, withdrawal, recruitment, recording opt-in, retention, deletion, and access-control plan; and review the fictional packets for sensitive or consequential content. Use pseudonymous IDs and a separate restricted linkage file only if necessary. Do not recruit subordinates under coercive conditions or use product/customer records. Raw responses and accessibility notes remain restricted; only privacy-reviewed aggregate formative results may be considered for release.

The governing anchors are the [Belmont Report](https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/index.html), applicable [45 CFR 46](https://www.hhs.gov/ohrp/regulations-and-policy/regulations/45-cfr-46/index.html), and [WCAG 2.2](https://www.w3.org/TR/WCAG22/) for the testable web requirements. These sources constrain the procedure; they do not imply approval or conformance.

## Stop, revise, or retain decisions

- If H1 increases any critical topology error, omit it. Do not try to repair a topology error with a longer caption.
- If E2 causes a reader to treat texture/color as evidence status or to add B1/C1 to the support count, revise or remove it.
- If the semantic receipt fails in text-only form, repair the HTML/copy before changing imagery.
- If the v13 anchor is mistaken for v14, increase its archival boundary and prefer its textual transcript over a larger portrait.
- If no-H1 and H1 conditions are comprehension-equivalent, prefer no H1 unless a separately defined editorial objective justifies the extra visual load.

This protocol becomes participant research only after the ethics, consent, allocation, instrument, scoring, privacy, and retention gates are satisfied. Until then it is a design artifact.

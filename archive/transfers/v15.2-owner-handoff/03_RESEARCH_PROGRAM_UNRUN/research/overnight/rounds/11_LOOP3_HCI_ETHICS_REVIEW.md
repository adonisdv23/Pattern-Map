# Loop 3: HCI, ethics, and reproducibility review

**Study under review:** Origin-Relation Cue Use in Evidence Bundles
**Reviewed:** 2026-08-18
**Review status:** design-time audit; no model call, participant contact, live retrieval, paid provider, deployment, publication, or empirical result occurred
**Decision:** **NOT READY for preregistration, the primary model run, or public PDF release.**

This review audits the current protocol, the Loop 2 operationalization specification, the Loop 2 opportunity/interface specification, the route-receipt implementation, the thought piece, the readiness path, the claims register, the overclaim register, the local QA reports, and the rendered PDF. It records only material P0/P1 issues. “P0” below means that a primary run or release should stop until the item is repaired and re-checked. “P1” means that the item must be frozen, repaired, or explicitly downgraded before the corresponding claim or human-facing artifact is used.

## Evidence posture and scope

The labels below separate what is observed from what this review infers or recommends.

- **[S] Sourced/observed:** a fact visible in a repository artifact or supported by a primary/authoritative method or governance source.
- **[R] Review recommendation/inference:** a design conclusion drawn from the observed materials and the cited methods.
- **[H] Speculative hypothesis:** a proposition the proposed study may test; it is not an observed effect.

The protocol’s own boundary is appropriate: F2 is an oracle cue supplied by a fictional benchmark graph. A positive result would concern use of that cue by one frozen model under one prompt and resource contract. It would not establish real-world provenance discovery, epistemic independence, truth, source authority, consensus, human benefit, utility, fairness, enterprise readiness, or validity of the complete Pattern Recognition / Discrimination Layer. Alpha Solver and Signal Foundry remain implementation contexts only and are not validation data.

## Readiness verdict

The narrow benchmark remains a potentially executable first study, but the current specification does not yet identify one reproducible primary estimand. The model-facing synthetic corpus is also not ready to freeze because the grammar, schema, gold-support fields, stress allocation, and release manifest do not yet form one internally closed contract. The human-reader test is promising as a formative interface check but is currently under-specified and cannot support a comprehension, accessibility, or efficacy claim.

The minimum readiness decision is therefore:

1. **Stop all primary model interpretation** until the FC/VOR denominators, invalid-output coding, non-inferiority direction/level, and success criterion are rewritten in one analysis block.
2. **Stop corpus lock** until grammar-to-schema truth tests, conflict/support-origin semantics, raw-output schema, canonical serialization, leakage procedures, stress allocation, and version identifiers are frozen.
3. **Stop public PDF release** until the stale “five”/“nine” contradiction on PDF page 18 is removed and the PDF hash and visual QA receipt are refreshed.
4. Treat the human-reader work as a **separate, ethics-reviewed, formative HCI study**. It cannot be used to validate the F2-versus-F1 model result or to establish WCAG conformance.

After those repairs, an offline 40-bundle feasibility pilot is reasonable if it is used only for parser, generator, replay, resource, leakage, and QA gates. A 300-bundle primary run is reasonable only if the pilot passes the frozen gates and the power simulation shows that the chosen FC and VOR claims are estimable at the stated precision. If it does not, the paper should be downgraded to a feasibility/measurement paper rather than enlarged after seeing outcomes.

## P0 blockers: exact corrections required

### P0-1 — FC and VOR have incompatible denominators and invalid-output rules

**Observed [S].** Loop 2 §8.3 defines `FC(i,c)=0 otherwise`, which includes invalid outputs. Loop 2 §8.4 then says the primary FC estimate is over bundles valid in both F1 and F2 and describes invalid outputs as separate conservative/liberal sensitivities. Loop 2 §11.2 performs the paired test on `I*`, the complete-case set. Loop 2 §11.3 performs VOR on the fixed multiple-origin set intersected with `I*`, although the protocol says invalid outputs remain in the assigned denominator and are failures. Thus an invalid response can be `0` in one formula, omitted in the primary analysis, and coded as `1` or `0` in sensitivities. The VOR denominator can also shrink differently by condition.

**Why this blocks the run [R].** Complete-case analysis can remove harder or condition-specific failures. If F2 produces more malformed output, dropping those bundles can make F2 look safer; if F1 produces more malformed output, the opposite distortion is possible. A safety endpoint whose denominator changes after parsing is not the prespecified safety endpoint. The issue is not a minor reporting choice: it changes the estimand and can change the sign of the contrast.

**Required correction [R].** Replace the current definitions with one fixed all-assigned primary analysis. Let `A` be all 300 assigned primary bundles, `valid(i,c)` be the locked parser result, and `nonmultiple(i)` mean that the restricted gold manifest certifies zero or one supporting origin or intentionally withholds that certification as unresolved. Keep the observed event separate from risk coding:

```text
FC_obs(i,c) = 1[valid(i,c)
                 AND origin_count_supporting(i,c) >= 2
                 AND nonmultiple(i)]

FC_cons(i,c) = 1[NOT valid(i,c) OR FC_obs(i,c) = 1]
FC_lib(i,c)  = 1[valid(i,c) AND FC_obs(i,c) = 1]
FC_valid(i,c) = FC_obs(i,c) for valid(i,c) only
```

Use `Delta_FC_cons = mean_A[FC_cons(i,F2)] - mean_A[FC_cons(i,F1)]` as the prespecified all-assigned risk-coded primary contrast. The conservative invalid coding deliberately treats a parser/runtime failure as a failure for risk control; it must not be described as an observed false-corroboration assertion. Report `FC_lib` and complete-case `FC_valid` as locked sensitivities, along with invalid counts and reason codes by condition. If the team instead wants complete-case FC as primary, it must explicitly adopt a missingness assumption, state that the model result is conditional on paired parseability, and remove the current claim that invalid outputs remain in the primary denominator. The recommended choice is the fixed all-assigned conservative estimand.

For VOR, define the denominator once and never intersect it with `I*`:

```text
M = {i in A : gold_support_origin_certainty(i) == multiple}

VOR(i,c) = 1[valid(i,c)
             AND origin_count_supporting(i,c) >= 2
             AND selected_support_origin_count(i,c) >= 2]
```

Invalid outputs are `VOR=0`. Compute `Delta_VOR = mean_M[VOR(i,F2)] - mean_M[VOR(i,F1)]` over every bundle in the fixed `M` set, expected to be the 75 multiple-origin-convergence bundles unless the locked manifest says otherwise. Do not use `M ∩ I*`. Report `|M|` and the exact membership list hash in the restricted manifest. The same fixed denominator must be used in the power simulation, estimate, interval, and claim.

**Non-inferiority correction [R].** Freeze the margin as `m=-0.05` before opening primary outputs, and choose one interval convention. Recommended wording: “F2 is called non-inferior on VOR only when the one-sided 95% lower confidence bound for `Delta_VOR` is greater than `-0.05`; this is a prespecified guardrail for this synthetic task, not a universal margin.” The analysis code must implement that exact direction and confidence level. A two-sided 90% interval may be used instead, but the protocol must say so rather than mixing “95% interval” with a one-sided decision. Publish the paired-binary interval method, bootstrap seed and resampling unit; run coverage simulations for `|M|=75`.

**Acceptance evidence.** A versioned metric specification, unit tests on hand-constructed valid/invalid and multiple/nonmultiple fixtures, a denominator table showing `N=300` for FC and fixed `|M|` for VOR, and a preregistration hash. The tests must demonstrate that changing parse status cannot silently change the denominator.

### P0-2 — The primary success criterion and multiplicity family are not one frozen decision rule

**Observed [S].** The protocol says a bounded efficacy statement requires a “minimum reduction” in false corroboration, but no exact reduction gate is defined in the protocol’s primary analysis. Loop 2 calls `-0.08` a candidate planning effect, while the inferential section specifies a two-sided McNemar test and a confidence interval without stating whether a practical effect threshold is required. Loop 2 §8.3 and §8.5 call claim-state accuracy and stress performance descriptive, but §11.5 places claim-state accuracy and stress-set FC in a secondary inferential family.

**Why this blocks the run [R].** A later choice between statistical significance, a point estimate, an interval crossing zero, or the candidate `-0.08` changes what counts as success. Adding descriptive outcomes to a Holm family after describing them as non-inferential invites unplanned multiplicity and selective interpretation.

**Required correction [R].** Keep the confirmatory family to exactly two prespecified contrasts:

1. F2 minus F1 on `Delta_FC_cons`, with the direction, exact two-sided alpha, and all-assigned conservative coding above.
2. F2 minus F1 on `Delta_VOR`, a non-inferiority safety gate and not a second superiority claim.

Remove claim-state accuracy and stress-set FC from the inferential family; report them descriptively with raw counts and uncertainty summaries clearly labeled exploratory. If either is intended to be inferential, define its estimand, hypothesis, multiplicity adjustment, and power before the run; the recommended decision is to keep both descriptive for this first paper.

For FC, replace “minimum reduction” with one explicit rule. Recommended rule: a bounded superiority claim requires a two-sided exact paired test at `alpha=.05` in the beneficial direction and a 95% interval whose upper bound is below zero; `-0.08` remains a planning/practical benchmark and is reported as “did or did not reach the prespecified planning effect,” not silently converted into a post-hoc success threshold. If the paper intends to claim a minimum effect of eight percentage points, use the upper 95% bound `<= -0.08` as the decision rule and rerun the power simulation for that rule before preregistration. Do not use a candidate value for both power planning and an unannounced success gate.

**Acceptance evidence.** One analysis table with the two confirmatory estimands, exact directions, alpha/interval conventions, invalid coding, and decision rules; a separate descriptive/exploratory table; simulation output showing type-I error/coverage and the chosen practical-effect rule.

### P0-3 — Protocol, operationalization, stress, and release manifest do not identify one frozen version

**Observed [S].** The protocol header is version `0.2`, while the Loop 2 manifest example uses `"protocol_version":"0.1"` and `"specification_version":"loop2-operationalization-0.1"`. The protocol defines 60 stress bundles with report-order, overlap, code/position permutation, and 5/10/20% relation-noise conditions. Loop 2 provides a 60-bundle stress count but no locked `stress_variant`, `noise_rate`, `noise_seed`, or complete allocation in the schema. The specification also describes a possible later 60-bundle public transfer challenge, which can be confused with the locked fictional stress split.

**Why this blocks the run [R].** A future analyst cannot tell which specification generated a stress row, whether a 60-item count refers to fictional robustness or public transfer, or whether the manifest describes the protocol actually preregistered. This is a reproducibility and degrees-of-freedom failure before any model result exists.

**Required correction [R].** Issue a versioned protocol/specification pair after this review. Recommended identifiers are `protocol_version=0.3` and `specification_version=loop3-operationalization-0.3` (or another pair chosen by the owner), with the old identifiers retained only as historical draft labels. Every manifest, schema `$id`, preregistration, prompt hash, and QA report must use the same pair.

Add to every stress-bundle record:

```text
stress_variant: enum {order, overlap, relation_code_permutation, relation_noise}
noise_rate: number in {0, 0.05, 0.10, 0.20}
noise_seed: opaque string or null when noise_rate == 0
stress_cell_id: opaque frozen cell identifier
```

Choose and document an exact allocation before generation. One executable recommendation is 60 items as `4 origin structures × 3 nonzero noise rates × 5 items per cell`, with order/overlap/code permutations assigned by a predeclared balanced subcell rule; do not imply that all factors are independently powered. Alternatively remove relation-noise from this split and give each stress factor its own count. The important correction is a single frozen design, not this particular allocation.

Move any FEVER/SciFact/AVeriTeC transfer challenge to a separately named, later `transfer` split with its own count, license/terms review, and no role in primary FC/VOR power, intervals, or real-world independence claims. Do not reuse `stress_n=60` for two meanings.

**Acceptance evidence.** Regenerated schemas, a split map with exact cell counts, a manifest whose hashes and row counts reconcile, a replay that reproduces every stress row byte-for-byte, and a preregistration that names the final version pair.

### P0-4 — The rendered PDF is stale and contains a visible count contradiction

**Observed [S].** Visual inspection of `exports/THOUGHT_PIECE_V14.pdf`, page 18, shows the heading “Nine positive articles. One launch announcement.” and a nine-observation framing, but Step 2 and the resulting paragraph still say “Five positive articles” / “Five positive articles share one known origin.” The current canonical source and current HTML route use nine. The PDF is therefore not a current visual companion to the source. The PDF metadata and the existing visual-reader report hash predate the later source/site correction.

**Why this blocks release [R].** This is an internal factual/count contradiction in a document that demonstrates the very origin-accounting distinction under discussion. It can make a reader believe that the receipt, source text, and illustration disagree. It also invalidates a QA receipt that says the required example text passed without checking the current source/PDF pair.

**Required correction [R].** Freeze the example at nine, because that is the current source/site/receipt construction, and regenerate the PDF from the canonical source. Confirm that the heading, image/caption text, Step 2, Step 3, final result, alt-equivalent text, and any page-break continuation all use the same count. Recompute the PDF SHA-256, page count and metadata receipt; rerun full text extraction and raster inspection, including page 18 and adjacent pages; update the visual-reader QA report with the new hash and date. Keep the PDF explicitly labeled a visual/print companion and keep semantic HTML as the canonical accessible surface. Do not distribute or cite the PDF as current until these checks pass.

**Acceptance evidence.** A fresh PDF hash, a count-consistency test over source/HTML/PDF text, page-level raster review, and a release receipt that says the PDF is untagged unless an accessible tagged PDF is actually produced.

## Site, PDF, and claim-register language audit

**Observed [S].** The current README, thought piece, paper-readiness path, claims/evidence register, overclaim/counterargument register, local HTML surface, and QA reports consistently state that the project is a provisional thought piece/research agenda with no empirical validation, no participant result, no deployment, no peer review, and no publication authorization. The route receipt is labeled fictional/no-live-data and does not present a score, confidence ranking, approval, or automatic gate. The thought piece explicitly says Alpha Solver and Signal Foundry are illustrative rather than validation. I found no separate P0/P1 site sentence claiming that the benchmark has been run or that the framework has been validated.

The two material language exceptions are the stale PDF count documented in P0-4 and the unqualified `HOLD · SEEK INDEPENDENT TEST` wording documented in P1-10. The existing visual-reader QA report is appropriately a local-review receipt, not a usability result or WCAG conformance claim; its PDF section also says the PDF is untagged. Preserve those boundaries when refreshing the PDF and route receipt. Do not turn the presence of a rendered receipt, a QA report, or a source citation into evidence that the proposed mechanism works.

## P1 issues to repair or explicitly downgrade before the relevant claim

### P1-1 — Generator grammar and proposition schema can encode different propositions

**Observed [S].** The environmental grammar hardcodes “recorded,” while its slot example includes “recorded” and “did not record.” The proposition schema enumerates predicates such as `reduced`, `increased`, `detected`, `did_not_change`, `supports`, and `failed_to_support`, while the shown grammar does not render all of them. The schema and grammar therefore do not establish that the text’s semantic polarity equals the restricted gold proposition.

**Correction [R].** Choose a canonical predicate enum and a versioned rendering map. Every enum value must have exactly one grammar rendering, a truth-state test, a negative/contrast test where applicable, and a round-trip fixture. Either remove unsupported schema values or implement their grammar. For environmental predicates, use canonical machine values such as `recorded` and `did_not_record` and map them to the visible phrases. The generator must fail closed if a slot has no renderer. Run 100% render-to-gold semantic tests before any pilot; do not rely on auditors to discover a generator mismatch after model outputs exist.

### P1-2 — Gold support-origin semantics are not explicit enough for conflict bundles

**Observed [S].** The formulas use `support_origin_certainty`, but the specification does not fully distinguish the number of supporting origins from the number of all origins in a conflict bundle. Conflict contains support and refutation paths, so “multiple origins” could accidentally mean one supporting plus one refuting origin. The VOR denominator must contain at least two *supporting* origins, not merely two origins anywhere in the graph.

**Correction [R].** Add restricted gold fields for `gold_support_origin_count` (or a lower-bound/certainty representation), `gold_support_origin_certainty` (`none`, `single`, `multiple`, `unknown`), and the support/refute origin sets. Define `M` only from the supporting side. Define FC’s `nonmultiple` status from the supporting side, with unknown conservatively nonmultiple for the primary risk-coded event. Write conflict fixtures that cover one-support/one-refute, multiple-support/one-refute, and dependent-copy/refute combinations. Never expose hidden graph labels to the model beyond the deliberately visible F2 relation cue.

### P1-3 — Raw-output schema, error vocabulary, and canonical serialization are incomplete

**Observed [S].** Loop 2 adds `raw_outputs.jsonl` and a parser contract but does not include a corresponding `raw_output.schema.json`; `error_code` is not a closed enum; several metadata maps and run records remain loosely typed. The manifest says “canonical-serialized” without specifying the canonical algorithm.

**Correction [R].** Add a strict raw-output schema with required fields, closed `parse_status` and `error_code` enums, UTF-8/base64 byte rules, one record per run, and cross-field constraints (`byte_length` equals decoded length; SHA-256 equals decoded bytes; raw bytes never reconstructed from parsed values). Add parser fixtures for duplicate keys, non-finite numbers, Unicode, fences, leading prose, timeout, empty output, and schema/semantic errors. Use RFC 8785 JSON Canonicalization Scheme for every hashed JSON artifact, or specify an equally complete serializer (encoding, whitespace, recursive key order, numeric representation, and array-order rule) and publish conformance fixtures. RFC 8785 defines canonical JSON for repeatable hashing/signing: <https://www.rfc-editor.org/rfc/rfc8785.html>.

### P1-4 — The leakage/shortcut suite is not reproducible and one probe confounds structure with true stance

**Observed [S].** The condition probe says to remove relation values and condition-specific instruction but does not specify the exact mask, feature extractor, classifier, split, seed, or confidence interval. The report-order probe uses stance/style features even though conflict structure is intentionally defined partly by stance composition. Lexical-overlap imbalance may be retained as a “limitation” while still permitting a primary cue-use interpretation.

**Correction [R].** Freeze the following before primary generation:

- mask every relation slot and condition-specific instruction to the same literal sentinel and preserve byte/token position;
- specify the exact feature representation, classifier, train/test split, seed, tuning procedure, accuracy CI, and stopping rule for condition and structure probes;
- make the report-order probe use position and formatting only, or condition on a predeclared compatible stance composition; do not call predictable gold stance a formatting shortcut;
- make cross-condition lexical-overlap and style balance a hard primary gate, not an optional limitation. If the locked generator cannot meet the balance threshold, downgrade the primary claim to a descriptive association under the observed surface distribution;
- record all probe code/configuration and raw predictions in the release-candidate manifest.

The condition probe must not be evaluated on a classifier that has access to the relation values it is supposed to test. A failed primary-surface gate means the F2/F1 difference is not identified as a relation-cue effect; it is not repaired by a post-hoc caveat.

### P1-5 — VOR non-inferiority has no safety-specific power/precision plan

**Observed [S].** The power grid covers FC baseline, discordance, candidate effects, null effects, and invalid rates, but not VOR baseline, `|M|`, harm scenarios, margin passage, or the fixed invalid=0 rule. With 75 multiple-origin bundles, the five-point margin may be too precise for the planned bootstrap, but no simulation currently establishes whether it is.

**Correction [R].** Add a VOR planning grid using the fixed `|M|` (expected 75), plausible baseline VOR values, paired discordance, harms at `0`, `-0.02`, `-0.05`, and `-0.08`, and invalid rates at `0%`, `2%`, `5%`, and `10%`. Simulate the exact one-sided non-inferiority decision and interval method at least 10,000 times per cell, with coverage and probability of passing reported. If the chosen safety margin is not estimable at the target precision, downgrade VOR to a descriptive safety guardrail and remove “non-inferior” from the allowed claim ladder. Do not increase N or loosen the margin after seeing pilot outputs. Non-inferiority reporting should state the margin, direction, analysis set, and confidence convention explicitly; see Piaggio et al., JAMA 2012, DOI <https://doi.org/10.1001/jama.2012.87802>.

### P1-6 — QA agreement and pilot gates can be tuned after observing the pilot

**Observed [S].** The specification says acceptance thresholds are “to be frozen after the pilot” and allows “Cohen’s kappa or an appropriate multi-rater agreement statistic.” The number of audited items and the audit strata are described, but the exact reliability statistic, missing/uncertain coding, and threshold lock date are not fixed.

**Correction [R].** Freeze the codebook, exact auditor sample and strata, nominal agreement statistic, confidence interval method, and pass/fail thresholds before the pilot’s primary outputs are seen. Recommended minimum: two blinded auditors on all dev/pilot items and the fixed stratified primary sample; Cohen’s kappa for the nominal stance/transformation labels with raw agreement and prevalence counts reported; a named third adjudicator; `uncertain` treated by a prespecified rule rather than silently removed. If prevalence makes kappa unstable, report that fact and use the predeclared alternative (for example, Krippendorff’s alpha for nominal data) without choosing after results. Cohen’s original agreement statistic is: Cohen (1960), <https://doi.org/10.2307/3001757>. Pilot edits may repair a generator or codebook only before primary lock and must be versioned; they may not choose a favorable metric or threshold.

### P1-7 — The output contract does not say how count and claim-state inconsistencies are handled

**Observed [S].** `origin_count_supporting`, `claim_state`, and `evidence_ids` are all returned, but the semantic relation between them is not fully specified. A model could report two supporting origins and `claim_state="refuted"`, or select evidence that does not support its count. The current parser’s strictness does not itself resolve whether this is invalid, a meaningful disagreement, or an automatic repair opportunity.

**Correction [R].** State that `origin_count_supporting` is the model’s separate origin-count assertion and that FC is computed from that field, not from claim state. Add a deterministic derived audit flag such as `count_claim_state_consistent` without changing the primary FC event. Define any hard semantic invalidity (for example, count exceeding the number of selected eligible evidence IDs if that is intended) before fixtures are generated. Never repair or overwrite one field from another. Report count/state disagreements descriptively and keep them out of the FC claim unless the protocol explicitly changes the estimand.

### P1-8 — HCI reader test is under-specified and its thresholds invite over-interpretation

**Observed [S].** The interface specification proposes “6–8 independent readers,” a “between-/within-reader” design, “at least one screen-reader or low-vision reader if feasible,” and gates such as “6 of 8.” It does not choose the design, exact allocation/order, item-form strategy, response-time anchors, scorer blinding, missing-response treatment, consent/recording procedure, or ethics determination. The proposed sample cannot support a general comprehension, accessibility, or prevalence claim.

**Correction [R].** Make the test explicitly formative and use one fixed design. Recommended executable version:

1. Target exactly eight adults who did not author the page or memos; if fewer than eight complete, report observations only and declare the gate unevaluable rather than changing the denominator.
2. Use a within-reader, four-condition design (current-image, demoted-H1, no-H1, text-only), one exposure per condition, with a frozen 4×4 Latin-square order. Use semantically matched packet variants or randomized equivalent item forms so the same answer is not simply learned on the first exposure.
3. Start timing when the assigned surface becomes visible and stop when the ten-item response is submitted; record no screen/video unless separately consented. Record correct/incorrect, confidence, effort, critical topology errors, scrolling/cropping/accessibility observations, and missing responses with fixed codes.
4. Have two blinded scorers apply a ten-item rubric without seeing condition labels or study hypotheses; preselect the agreement statistic and adjudication rule. Do not use participant self-confidence as correctness evidence.
5. Report only per-reader and per-item formative counts, error examples, and revision decisions. Do not use p-values, reader percentages as population estimates, or a single assistive-technology user as evidence of accessibility conformance.

The 6/8 style thresholds may remain as local design gates only if the exact denominator is eight and the ten critical items are frozen before recruitment. A gate is “pass” only when the target sample is complete; with fewer participants it is “not evaluated.” Keep this test separate from the F2/F1 benchmark and do not let its result rescue a failed model endpoint.

### P1-9 — Human-participant ethics, privacy, and accessibility procedures are absent

**Observed [S].** The interface memo does not state consent, recruitment, compensation, withdrawal, data retention, screen-recording consent, ethics/IRB/exemption review, or handling of accessibility accommodations. The site/QA reports document semantic HTML and visual checks but also say the full automated Tab/200% zoom/screen-reader/print harness was not completed. The PDF is not tagged.

**Correction [R].** Before contacting any reader, obtain the institution’s ethics/IRB determination or documented exemption decision, a consent script, compensation and withdrawal policy, minimal pseudonymous identifiers, retention/deletion dates, recording opt-in, and a no-coercion recruitment plan. Collect only accommodation information needed to run the session; do not publish disability or assistive-technology details in a way that identifies a participant. Provide keyboard, screen-reader, zoom, high-contrast, and text-only options. A reader who declines recording must still be able to participate. Keep raw responses/accessibility notes restricted and release only aggregate formative results after privacy review.

For public web release, complete a manual keyboard traversal, 200% zoom/reflow, screen-reader reading-order check, and print preview. If the PDF remains untagged, state plainly that HTML is the accessible canonical surface and do not claim PDF accessibility or WCAG conformance. WCAG 2.2 makes information/relationships and non-color communication testable requirements, but a static code inspection or one reader does not establish conformance: <https://www.w3.org/TR/WCAG22/> (SC 1.3.1 and 1.4.1). Human-subject protections should be considered under the Belmont principles and applicable Common Rule/45 CFR 46 determination: <https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/index.html> and <https://www.hhs.gov/ohrp/regulations-and-policy/regulations/45-cfr-46/index.html>.

### P1-10 — The route receipt uses an unqualified “independent test” label

**Observed [S].** The current route receipt heading is `HOLD · SEEK INDEPENDENT TEST`. The benchmark and interface documents carefully qualify `independent-as-stipulated`, but “independent test” in the receipt can be read as a claim that a real-world independent source or statistical independence has been established.

**Correction [R].** Replace the heading in the canonical HTML and interface specimen with `HOLD · SEEK A SEPARATELY AUTHORED TEST` or `HOLD · SEEK A BOUNDED EXTERNAL CHECK`. Keep the adjacent text: relation labels are illustrative/typed, unknown remains unknown, and claim support is not assessed by the receipt. Do not use “independent” without the qualifier `as stipulated` when referring to the synthetic benchmark.

### P1-11 — Interface specification and implementation have drifted

**Observed [S].** The Loop 2 opportunity/interface memo describes the route receipt as a proposed artifact and says it is not a core-file implementation. The current `site/app/page.tsx` contains an implemented receipt with nine rows, the count ledger, relation key, B1/C1 boundary, and a slightly different disposition sentence. Tests and QA reports also refer to the implemented route. The source/site is now ahead of the memo, but no canonical implementation/version link is recorded in the memo.

**Correction [R].** Before any public or reader-facing use, designate one canonical receipt source, mark the interface memo as implemented/superseded or update it to the exact DOM/copy, and record the implementation commit/hash, test fixture, and rendered surface version in the QA manifest. Re-run the route-receipt tests after the terminology correction and ensure the source, HTML, print output, and specimen use the same nine-row fictional bundle. A design memo cannot be used as an implementation receipt while the live local surface differs.

### P1-12 — Accessibility evidence is being used as a risk check, not yet as a release claim

**Observed [S].** The local QA report is appropriately cautious: semantic HTML, server output, visible focus CSS, reduced motion, print rules, and selected interactions passed; a full automated Tab traversal, 200% zoom, and print-emulation pass was unavailable. The report also identifies the PDF as untagged and the HTML as canonical.

**Correction [R].** Preserve that wording. Add a dated manual accessibility checklist and reviewer receipt before any external share. The receipt should name the tested browser/OS/assistive technology, keyboard path, zoom level, print path, table caption/header behavior, focus return, and unresolved limitations. Do not change “local review ready” into “accessible,” “WCAG compliant,” “validated,” or “reader-tested” without the corresponding evidence. WCAG is a conformance standard, not a result implied by visual polish.

### P1-13 — Privacy, licensing, model provenance, and governance are not yet a release manifest gate

**Observed [S].** The primary design is synthetic-only and says no private/sensitive data or live retrieval will be used. The specification nonetheless permits later public transfer material and raw outputs, and the model is not selected in the example manifest. The current reports correctly prohibit deployment/publication but do not turn license/privacy/model terms into a required release-manifest check.

**Correction [R].** Add a release gate that records: synthetic-only status; generator/template license; any public-transfer dataset name, version, license and permitted redistribution; model/checkpoint/tokenizer license and revision; no provider credentials, cookies, hidden prompts or secrets; raw-output privacy scan; no personal, medical, employment, allegation, or consequential-decision content; and owner authorization for release. If a public transfer set is used, retain only fields permitted by its license and report that those labels do not establish origin independence. If any secret/PII or unauthorized live call appears, quarantine the run and invoke the fixed stop rule. No Alpha Solver or Signal Foundry artifact may appear in the primary truth manifest merely because it informed schema design.

## Metric, parser, and resource audit conclusions

The following conclusions are material and should be preserved in the final protocol rather than left implicit.

### What is sound after correction

- **Bundle unit:** one bundle per condition is the correct paired unit for the proposed question. Reports, tokens, seeds, and generated characters are not independent observations.
- **F2/F1 resource control:** exact per-bundle input-token parity is the right requirement. It must be checked with the selected model/tokenizer before primary lock, not inferred from character length. F0 can remain secondary and padded only if the padding rule is fixed.
- **Strict parser:** no repair, retry, fence removal, type coercion, or first-object selection is appropriate for a format-sensitive benchmark, provided invalid outputs remain visible in the assigned denominator and are not silently treated as abstention.
- **F0/F1/F2 structure:** citation-only, rule-only, and rule-plus-stipulated-cue conditions can isolate whether the typed cue adds value beyond an explicit rule. If F1 and F2 tie, the result belongs to the rule/instruction, not necessarily to provenance representation.
- **Synthetic truth boundary:** graph relations can be true by generator construction; they cannot validate real-world source honesty, causal independence, authority, prevalence, or truth. “Independent-as-stipulated” is the correct label.
- **No invented utility:** fictional bundles do not have a defensible consequence function. Time, tokens, latency, memory, and local compute can be reported, but not converted into decision utility or dollars without a preregistered cost model.

### What remains unsafe without the corrections above

- a valid-only primary result that omits condition-specific invalid output;
- a VOR claim whose denominator is `M ∩ I*` rather than fixed `M`;
- a non-inferiority conclusion without one-sided direction, confidence level, and VOR power/coverage simulation;
- a claim-state/stress result described as descriptive but corrected for multiplicity as if confirmatory;
- a generator result whose visible predicate may not equal the gold predicate;
- a “shortcut-free” claim based on an unspecified probe or a structure probe that uses gold stance;
- an output parser that rejects/repairs fields without a closed error schema;
- a human-reader percentage from an ambiguous 6–8-person design;
- “independent test,” “accessible PDF,” “validated interface,” or similar language not supported by the evidence boundary.

## Pre-run and pre-release checklist

The following checklist is the minimum evidence package. A blank item is a stop, not an invitation to explain the omission in the results section.

### Primary benchmark lock

- [ ] One versioned protocol/specification pair; all manifest, schema, prompt, preregistration, QA, and code hashes reconcile.
- [ ] FC formulas distinguish observed false corroboration from conservative/liberal invalid coding; primary denominator is all assigned `N=300` (or the preregistered alternative with a justified missingness rule).
- [ ] VOR uses fixed `M`, explicitly support-side origin semantics, invalid=0, one-sided confidence direction/level, and a frozen `m=-0.05` or a formally chosen replacement.
- [ ] Exact FC decision rule is frozen; no unannounced “minimum reduction” gate; the `-0.08` planning scenario is not silently used as a result threshold.
- [ ] Confirmatory multiplicity family contains only FC and VOR; claim-state, stress, domain, structure, style, seed, and model slices are descriptive/exploratory unless separately powered and registered.
- [ ] Gold schema distinguishes supporting from refuting origins and unknown support-origin certification; conflict fixtures pass.
- [ ] Every predicate enum has a grammar renderer, truth-state test, and round-trip fixture; no unsupported slot value can be generated.
- [ ] Split map blocks proposition/origin lineage across dev, pilot, primary, and stress; duplicate/near-duplicate checks pass with recorded thresholds.
- [ ] Stress fields and exact cell allocation are present; public transfer, if retained, has a distinct split and does not alter primary denominators.
- [ ] F1/F2 byte/token parity, order, metadata skeleton, decoder, output cap, and model/tokenizer revisions are locked and tested.
- [ ] Raw-output schema, closed error codes, parser fixtures, canonical JSON serialization, hashes, and replay are complete. RFC 8785 or an equivalent fully specified serializer is used.
- [ ] Leakage probes have fixed masking, features, classifiers, splits, seeds, intervals, and hard-fail rules; lexical/format balance is not waived after outcomes.
- [ ] VOR-specific power, interval coverage, invalid-rate sensitivity, and non-inferiority pass probability are simulated at the actual `|M|`.
- [ ] Human QA codebook, exact sample, strata, blinded scoring, statistic, missing/uncertain handling, adjudication, and threshold are frozen before the pilot’s results.
- [ ] Preregistration is timestamped and hashed before the primary split is opened; the no-peeking/no-retry/no-model-change rule is executable.

### HCI and ethics gate

- [ ] The reader test is labeled formative and separate from model efficacy.
- [ ] Exactly one reader design, target N, counterbalancing, matched packet/item forms, timing anchors, scoring rubric, missing handling, and reporting rule are frozen.
- [ ] Ethics/IRB/exemption determination, consent, withdrawal, compensation, recording opt-in, minimal data collection, retention/deletion, and no-coercion recruitment are documented before contact.
- [ ] Accessibility accommodations and manual keyboard/zoom/screen-reader/print checks are planned; no single participant or code review is treated as WCAG conformance.
- [ ] The receipt says “separately authored test” or “bounded external check,” not unqualified “independent test.”
- [ ] The receipt implementation, interface memo, source text, route tests, and print/PDF surface use one frozen fictional nine-row specimen.

### Release and claim gate

- [ ] PDF page 18 count contradiction is fixed; new PDF hash, page-level raster review, text checks, and visual QA receipt are archived.
- [ ] HTML remains the accessible canonical surface; an untagged PDF is not described as accessible or WCAG-conformant.
- [ ] Synthetic-only, model/license, dataset/license, raw-output privacy, no-secret, no-live-call, and owner-authorization checks are recorded in the manifest.
- [ ] No site, PDF, README, paper prospectus, or receipt says that a result, validation, independent provenance, source authority, utility, fairness, or publication exists before it does.
- [ ] Alpha Solver and Signal Foundry are labeled illustrative implementation contexts only.

## Allowed claim ladder

This ladder is the maximum wording allowed at each evidence state. It should be copied into the preregistration and release manifest.

### L0 — current state, before any run

Allowed: “The project proposes a bounded synthetic benchmark and research question about whether a frozen model uses supplied origin-relation metadata beyond an explicit origin-counting rule.” “The thought piece is a conceptual synthesis/research agenda.”

Not allowed: any claim of improvement, validation, usability, accessibility conformance, provenance discovery, or result.

### L1 — generator/parser feasibility only

Allowed: “The locked generator, schema, parser, replay, and resource ledger passed the stated feasibility gates on the designated development/pilot artifacts.” This is an implementation/reproducibility result, not an efficacy result.

Not allowed: “The model can account for origins,” “the cue works,” or “the framework is validated.”

### L2 — primary FC/VOR result, if all gates pass

Allowed, only with exact scope: “For the tested model, prompts, tokenizer/resource contract, and newly authored fictional bundles with benchmark-stipulated provenance, F2 [did/did not] reduce the prespecified all-assigned risk-coded false-corroboration endpoint relative to F1, while VOR [met/did not meet] the prespecified safety guardrail.” Report estimates, intervals, invalid rates, and all sensitivity codings.

The phrase “independent” must be written as “independent-as-stipulated.” The result is not a real-world independence claim, a truth claim, a source-authority claim, or evidence that the full framework improves decisions.

### L3 — null, harmful, invalid, or shortcut result

Allowed: “Under this protocol, typed relation metadata did not add detectable value beyond the rule,” or “the cue was harmful/unstable/format-sensitive/noisy,” with the exact uncertainty and gate failure. If F1 and F2 tie while both differ from F0, the bounded interpretation is that the explicit rule may explain the observed difference; do not attribute the result to provenance representation.

If invalidity, semantic QA failure, or leakage occurs, the paper is a feasibility/measurement or benchmark-repair report. It is not an efficacy paper.

### L4 — locked stress results

Allowed only if the stress set was frozen and its factors are labeled: “The effect [did/did not] persist under the declared order/overlap/code/noise cells.” A gain that disappears under relation noise is an oracle-cue upper bound or a fragile result, not deployment evidence.

### L5 — formative HCI result

Allowed: “Eight recruited readers provided formative observations about whether this specimen’s labels and boundaries were understood under the tested surfaces.” Report critical errors, accessibility observations, and revisions. Do not generalize to users, populations, accessibility conformance, or model performance.

### Permanently out of scope for this first paper

Real-world provenance discovery; real-world epistemic independence; truth or consensus; source authority; retrieval quality; human decision improvement; decision utility; enterprise readiness; universal AI behavior; subgroup fairness; deployment safety; publication or peer-review status; and validation of the complete Pattern Recognition / Discrimination Layer.

## What would falsify or narrow the thesis

These are prespecified narrowing outcomes, not predictions of what will occur.

- **F2 equals F1:** supplied typed metadata adds no observed value beyond the explicit rule for this model/task; the claim narrows to rule/instruction design.
- **F2 increases FC:** the cue worsens false corroboration; the typed cue is not safe for this task under the fixed contract.
- **VOR falls below the margin:** even if FC improves, the cue suppresses valid stipulated convergence; no bounded efficacy claim is allowed.
- **Invalid outputs differ materially or exceed the gate:** parser/resource behavior is part of the result; no clean cue-use interpretation is allowed.
- **Grammar/gold QA or leakage fails:** the benchmark does not identify the intended mechanism; regenerate or report a benchmark-feasibility failure.
- **Effect disappears under declared relation noise, overlap, or code permutation:** retain at most an oracle upper-bound/fragility claim.
- **F0/F1/F2 resource parity fails:** any condition contrast is confounded; stop and redesign.
- **QA agreement fails:** synthetic truth or semantic labels are not sufficiently reliable; repair the codebook/generator before efficacy.
- **Readers make critical topology or status errors:** the receipt/interface needs revision; it does not validate the framework or prove a need for a larger HCI study.
- **Human burden or accessibility work is disproportionate:** drop the interface claim and retain a text-only bounded artifact until a governed study is feasible.
- **A simpler rule-only or source-faithful comparator is as good under matched resources:** the typed integration has not earned complexity; narrow or retire the mechanism for this class.

## Source and authority notes

The repository artifacts are the direct evidence for the implementation-specific findings above. The external sources below support method/governance recommendations only; none validates the thought piece or predicts the study result.

- Piaggio, Elbourne, Pocock, Evans, Altman, and CONSORT Group (2012), reporting non-inferiority/equivalence trials, JAMA, DOI <https://doi.org/10.1001/jama.2012.87802>. Used for the recommendation to state the margin, direction, analysis set, and confidence convention explicitly.
- Leon, Davis, and Kraemer (2011), “The role and interpretation of pilot studies in clinical research,” DOI <https://doi.org/10.1016/j.jpsychires.2010.10.008>. Used for the boundary that pilot effects should not tune the confirmatory effect size or favorable endpoint.
- Lakens (2013), “Calculating and reporting effect sizes to facilitate cumulative science,” DOI <https://doi.org/10.3389/fpsyg.2013.00863>. Used for preregistering practical effects and reporting estimates rather than treating a p-value as a practical threshold.
- Cohen (1960), “A coefficient of agreement for nominal scales,” DOI <https://doi.org/10.2307/3001757>. Used for naming an agreement statistic in advance; raw agreement and prevalence must also be reported.
- Rundgren, Jordan, and Erdtman (2020), RFC 8785, “JSON Canonicalization Scheme,” <https://www.rfc-editor.org/rfc/rfc8785.html>. Used for deterministic serialization and repeatable artifact hashing.
- W3C (2024), Web Content Accessibility Guidelines 2.2 Recommendation, <https://www.w3.org/TR/WCAG22/>. Used for the distinction between semantic/accessibility checks and an unsupported conformance claim.
- U.S. HHS, Belmont Report, <https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/index.html>, and 45 CFR 46, <https://www.hhs.gov/ohrp/regulations-and-policy/regulations/45-cfr-46/index.html>. Used for the required ethics/IRB or exemption determination, consent, privacy, and risk review before human-reader contact.

**Final disposition:** repair P0 items, freeze the P1 contracts, and rerun the local QA receipts. Until then, the honest artifact is a design-only research agenda with a bounded synthetic-study proposal—not an executed benchmark, a validated interface, or a research result.

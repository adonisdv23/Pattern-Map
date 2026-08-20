# Reasoning and logic - Pattern Recognition / The Discrimination Layer v15.2

Status: `CURRENT END-TO-END HANDOFF NARRATIVE`

Date: 2026-08-19

This document explains how the project moved from the recovered v13 map to the
v15.2 owner-review candidate, why the major decisions were made, what was
rejected, what the research program can honestly claim, and how another GPT
should continue. It is the narrative bridge across the owner packet, decision
ledger, research memos, image ledger, red teams, and final outputs.

It does not replace those records. Where precision matters, follow the
authority order in `PACKAGE_MAP_V15_2.md`.

## 1. The owner's objective

The owner did not want a merely polished map or another attractive AI-themed
site. The target evolved into four connected but distinct outputs:

1. an authored thought piece that stands on its own in the current moment;
2. a practical framework that can improve how AI-assisted tools admit,
   separate, route, and expose evidence;
3. an inspectable site that teaches the idea to non-specialists without
   flattening its technical depth; and
4. a serious, falsifiable path toward an empirical research paper.

The owner repeatedly prioritized depth, distinctiveness, usefulness, and
honesty over superficial completion. They also asked for fast parallel work,
independent model critique, visual exploration, versioned standalone pages,
PDFs for rapid review, a complete image-use table, and a package another GPT
could understand without the chat history.

## 2. What was recovered and preserved

The original v13 live site supplied the project's visual and conceptual
origin: pattern recognition before generation, peripheral-signal mining, six
families, expandable records, and a historical diagram generated in the
earlier DALL-E-era workflow.

Two preservation decisions matter:

- The recovered v13 diagram is kept byte-for-byte unchanged. It is a
  historical anchor, not a current topology or empirical result.
- The original v13 HTML bytes were not recovered. A rendered DOM snapshot is
  preserved as historical evidence, but is not mislabeled as an exact
  self-contained original.

The package also preserves the sealed v14, v15, and v15.1 checkpoints. V15.2
is called a convergence and hardening release, not v16, because it clarifies
and validates the same core proposition rather than replacing it.

## 3. The central conceptual decision

The strongest idea is not “better retrieval” in general and not a universal
new AI layer. It is this narrower claim:

> An AI answer inherits choices made before it writes: what was available,
> what was treated as separate evidence, what supported which claim, what was
> allowed to influence the answer, what action was permitted, and what remained
> unresolved. In evidence-sensitive work, those choices should be visible and
> correctable.

The concrete failure that makes the idea memorable is also deliberately
simple: nine favorable reports may all descend from one announcement. A system
that summarizes “nine sources agree” has changed the evidence structure. It
has turned nine observations into nine apparent origin paths and then into
corroboration.

The correction is not to delete eight reports. All nine can remain useful as
records of reach, framing, timing, or transformation. The correction is to
preserve the difference between:

- report count;
- known origin relation;
- claim-level support;
- authority for that claim;
- relevance to the present decision;
- permission to use or act;
- action priority; and
- the accountable person's disposition.

Unknown relations must remain unknown. Zero separately rooted support for a
broad claim means `HOLD / VERIFY`; it does not automatically mean the claim is
false.

## 4. Why earlier drafts felt artificial

The earlier versions accumulated taxonomy, cards, labels, routes, and polished
containers faster than they sharpened the argument. Independent critique from
Codex lanes and Claude Cowork converged on the same problem: layout cannot fix
prose, and a complete-looking system can make an unrun research program feel
more established than it is.

The anti-slop response was editorial subtraction:

- reach the nine-reports/one-announcement failure immediately;
- show a small receipt before the full framework;
- organize the public essay around three questions rather than eleven records;
- keep the six families and C01-C11 records in Explore, where depth is wanted;
- move exact research notation into Lab and define it in ordinary language;
- use asymmetry, whitespace, prose rhythm, and bounded figures instead of
  repeating an interchangeable card pattern; and
- require the essay to work without generated imagery or interaction.

The current public reading contract is cumulative: 60-90 seconds, about four
minutes, and about nine minutes. Explore, Lab, Sources, and the PDF are
optional deeper routes. These are editorial estimates, not measured reader
results.

## 5. Why the technical explanations are interactive

The owner correctly flagged that labels such as `F0`, `F1`, `F2`, `T1`,
`N=300`, `M=75`, `FC_cons`, `VOR`, provenance audit, system runtime, and human
disposition were incomprehensible or incomplete for a thoughtful
non-specialist.

V15.2 applies a plain-language-first rule: the visible sentence must make
sense even if the reader never opens the definition. Selected terms can then
open a definition, concrete example, “does not mean” boundary, and—in a few
cases—a code-native microvisual.

The explanations use semantic native controls, keyboard/touch behavior,
explicit close, focus return, an in-flow fallback, and print treatment. Static
tests verify the structure. Fresh supported-browser and assistive-technology
operation remains a manual residual rather than an invented pass.

## 6. Visual-generation logic

Image generation was used as a design exploration, not as evidence. Multiple
hero, worked-example, and social-card candidates were produced and compared
for conceptual fidelity, non-misleading topology, editorial fit, crop
resilience, accessibility support, and craft.

The final selection is deliberately restrained:

- no generated hero is used because the strongest candidates still implied a
  one-way gatekeeper, filter, or pipeline;
- the E2 derivative is used only in the deeper worked example, after the
  deterministic receipt, with an explicit illustration/no-result boundary;
- the v13 diagram appears only as preserved history;
- the generated social card is retained for a possible later publication
  decision but is not referenced by the local v15.2 metadata; and
- high-stakes current relationships are live HTML/CSS and text, not raster
  topology.

`IMAGE_USE_TABLE_V15_2.md` accounts for each eligible generated design image,
preview, historical anchor, and production raster as used, unused, rejected,
or audit-only. Raw historical QA screenshots are intentionally excluded from
the owner ZIP; their material findings remain in text records.

## 7. What the current framework is—and is not

The framework is best understood as a reviewable responsibility, not
necessarily one service, model, prompt, database, or box in a stack. Its
minimum commitments are:

- preserve distinct observations without inflating distinct support;
- represent origin relations and uncertainty explicitly;
- separate unlike judgments rather than compressing them into one score;
- record what entered the answer and why;
- preserve accountable human correction or disposition; and
- use outcomes to improve later judgments without silently rewriting history.

It is not a truth oracle, automated provenance discovery, universal ranking
system, compliance certification, runtime implementation, or proof that every
AI workflow needs eleven components. It should be retired wherever a simpler
method performs as well at lower cost.

Signal Foundry and Alpha Solver remain bounded translations and design cases.
They do not independently validate the general framework. Signal Foundry's
visible action is `HOLD / DEFER`, preserving the difference between an
inspectable judgment and automatic permission to act.

## 8. Prior art and the honest novelty boundary

The broad ingredients have substantial prior art: provenance and lineage,
copying detection, truth discovery, duplicate handling, evidence-synthesis
double counting, citation amplification, claim verification, retrieval
diversity, conflict-aware RAG, mixed-initiative systems, and decision theory.

The project therefore does not claim to have discovered that copied reports
are dependent or that evidence should be traceable. The credible contribution
is the synthesis, the inspectable receipt, the insistence on preserving
separate judgment types, and one narrow candidate empirical question:

> Does a supplied, benchmark-stipulated origin-relation cue change a frozen
> model's origin-aware evidence aggregation beyond an explicit counting rule?

The prior-art work also identified natural news syndication as a valuable
future transfer challenge. It remains `T1`: optional, descriptive, rights- and
annotation-gated, and outside the confirmatory denominators. A near-duplicate
cluster is not automatically a complete provenance graph or proof of
independent origins.

Calibration was deferred because the present scalar confidence field does not
define a probability for the event the proposed origin-accounting study needs.
Adding a fashionable metric without defining its target would weaken the
paper.

## 9. The proposed research program

The canonical v1.0 protocol proposes three fictional-bundle conditions:

- `F0`: the ordinary task, used descriptively;
- `F1`: the same reports plus an explicit rule not to count copied or derived
  reports as separate origin paths; and
- `F2`: the same rule and reports plus supplied relation labels (`DPND`,
  `INDP`, `UNKN`).

The planned primary denominator is `A=300` fictional cases. The fixed planned
safety subset is `M=75` multiple-origin cases. Both are design values, not
results. The current local tokenizer is a development surrogate, not a
selected study tokenizer.

The primary conservative risk measure (`FC_cons`) includes every assigned
case. It counts invalid answers and valid overclaims of multiple supporting
origins under the fictional benchmark rule. Those components must also be
reported separately so an apparent improvement cannot hide invalid output.

The safety measure (`VOR`) asks whether the model still uses at least two
benchmark-stipulated support roots on the fixed subset where the test says they
exist. Ordered membership and its hash come from the restricted pre-run
manifest, freeze before execution, and are never filtered using validity or
post-run output. The intended F2-minus-F1 one-sided lower bound must exceed the
locked `-0.05` margin. The interval method, coverage simulation, and paired
invalid-output operating characteristics remain open gates.

F1 and F2 preserve report text, order, output shape, rule, and resources. The
relation field is the intended difference, so complete prompt bytes and hashes
may differ. Input byte lengths and selected-tokenizer counts must match.

Protocol v1.1 is a proposed amendment drafted to clarify these meanings and
failure dispositions. It is not canonical and does not authorize a run until
the owner explicitly accepts it.

## 10. Why the unfavorable-result commitment matters

The owner approved the plain-language commitment to preserve results that make
the project look weaker. In practice:

- if F2 does not outperform F1, report that the supplied cue added no detected
  benefit;
- if F1 and F2 tie while both improve on F0, attribute the benefit to the rule,
  not the metadata;
- if composite movement comes from invalid outputs, say so;
- if the safety threshold alone fails, do not call the mechanism safe;
- if the cue causes harm, reject or retire it;
- if a model uses direct codes, formatting, stance leakage, or a semantic
  shortcut, quarantine the run rather than treating it as understanding;
- if the result is unstable, noise-fragile, or does not transfer, narrow the
  claim; and
- if a run is stopped or quarantined, keep that record.

This is ordinary research honesty: the study must be able to shrink, reject,
or retire the tested mechanism. It is not a promise that the conceptual essay
must disappear if one implementation fails.

## 11. Multi-agent program and integration discipline

The overnight program used bounded parallel lanes for:

- prior art and research-method clarification;
- protocol amendments and offline implementation readiness;
- editorial voice and non-specialist comprehension;
- information architecture, accessibility, and explanatory visuals;
- owner-reader cold review;
- post-integration methods/evidence red team; and
- post-fix static site acceptance.

The parent integrator remained the sole canonical editor. Agent outputs were
accepted, modified, deferred, or rejected in the integration decision ledger
rather than merged because they looked polished.

The final methods re-review passed with one non-blocking maintainability
residual: the fictional `ORIGIN-EX-01` receipt appears in compact, detailed,
presentation, and generated forms. The copies are currently aligned and
explicitly fictional. A later typed shared content object or consistency test
would reduce drift.

The static site re-review passed with manual QA residuals. Build, lint,
server-rendered route tests, self-containment checks, skip targets, current
research language, and corrected Lab strings pass. Supported-browser
interaction, screen-reader behavior, viewport collision, forced colors, and
print preview remain manual.

## 12. Important rejected or deferred choices

- **Generated hero:** rejected for topology and gatekeeper risk.
- **A decorative system map:** rejected because it could present a proposed
  responsibility as validated architecture.
- **A fourth confirmatory real-syndication arm:** deferred to descriptive T1
  feasibility work.
- **Calibration endpoint:** deferred until a probability target and scoring
  rule are defined.
- **Broad first/nobody-has-done-this novelty claims:** rejected.
- **Replacing F0/F1/F2 after every research idea:** rejected; the narrow core
  remains unless a demonstrated defect requires amendment.
- **Treating Signal Foundry or Alpha Solver as validation:** rejected.
- **Publishing or deploying while the owner is asleep:** not authorized and
  not performed.
- **Silently canonizing protocol v1.1:** rejected.
- **Running a model, provider, pilot, or primary study:** not authorized and
  not performed.

## 13. What v15.2 contains

The current owner candidate includes:

- the canonical v15.2 manuscript;
- a four-route editable site (Essay, Explore, Lab, Sources);
- four self-contained current-route HTML exports;
- separate self-contained v14, v15, v15.1, and v15.2 manuscript pages;
- a visually inspected 20-page v15.2 PDF companion;
- a PDF comparison ZIP containing v14, v15, v15.1, and v15.2 companions;
- the canonical framework map and glossary;
- research protocols, prior-art records, fictional generators, parsers,
  validators, planning simulations, tests, and explanatory experiments;
- all eligible generated image candidates plus use/rejection accounting;
- the v13 historical anchor;
- multi-agent lane reports, red teams, decisions, and QA receipts; and
- deterministic package manifests and SHA-256 sidecars.

The current output is in `01_FINAL_OUTPUT/`. Historical and rejected artifacts
are intentionally kept elsewhere so another GPT cannot mistake them for the
current release.

## 14. Known limits and unresolved decisions

- The owner has not yet completed the intended voice and comprehension pass.
- Real cold-reader sessions have not occurred.
- Browser/assistive-technology acceptance remains manual for the final build.
- No empirical research result exists.
- The model, checkpoint, tokenizer, provider/runtime, final interval method,
  ethics/privacy/licensing decisions, registration destination, budget, and run
  authority remain open.
- `A=300` and `M=75` remain provisional until operating-characteristic gates
  pass.
- T1 rights, schema, and annotation feasibility remain unresolved.
- The public GitHub repository and hosted site were not changed.
- A Claude course-correction message was prepared but remains blocked behind
  Claude's elevated re-authentication screen. No credential handling was
  attempted, and local work did not depend on it.

## 15. Recommended continuation sequence

Another GPT should proceed in this order:

1. Preserve this ZIP and its manifest as the v15.2 owner checkpoint.
2. Ask the owner to read the 60-90-second, four-minute, and nine-minute stops
   before starting another broad expansion.
3. Collect the owner's voice, confusion, and emphasis notes in one bounded
   revision pass.
4. Run several real cold-reader sessions using the v15.2 reader contract.
5. Fix any comprehension failure in prose or information architecture before
   adding glossary terms or visuals.
6. Complete the short manual browser/assistive-technology acceptance matrix.
7. Decide whether to accept, revise, or reject protocol v1.1.
8. Close the scientific gates without opening the primary run.
9. Only after exact owner authorization, curate the GitHub checkpoint or
   prepare a pilot. A GitHub write, deployment, provider call, preregistration,
   dataset acquisition, or study run is never implied by this package.
10. Preserve and report every outcome class, including results that narrow or
    retire the proposed cue.

## 16. Final recommendation

V15.2 should be treated as a strong owner-review checkpoint, not a finished
scientific paper and not a dead-end personal artifact. It already stands as an
authored conceptual piece and a credible practitioner framework proposal. The
specific research program is promising because it is narrow enough to fail.

The next improvement should come from owner and real-reader evidence, not from
another unconstrained loop of model-generated completeness.

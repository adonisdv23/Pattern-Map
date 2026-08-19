# Round 2 owner / cold-reader red team

## Pattern Recognition: The Discrimination Layer v15.1 → v15.2 candidate

**Lane:** independent owner-proxy, cold comprehension, voice, and bounded-usefulness audit
**Status:** red-team recommendation for the parent integrator; read-only review of canonical and candidate content
**Date:** 2026-08-19
**Evidence inspected:** `reports/overnight/v15_2/PROGRAM_CHARTER.md`,
`source/THOUGHT_PIECE_V15.md`, the current v15.1 site surfaces in
`site/app/page.tsx` and `site/app/content.ts`,
`reports/overnight/v15_2/ROUND1_EDITORIAL_OWNER_PROXY_AUDIT.md`,
`source/candidates/THOUGHT_PIECE_V15_2_EDITORIAL_CANDIDATE.md`, and the reader
outcome / terminology contracts. No site run, browser check, external search,
model call, or live study was used.

## Executive verdict

**Select the candidate as the editorial base, but accept it only after one
small rewrite pass. Do not expand the framework.** The candidate makes the
receipt more usable, makes the next action concrete, replaces most schema
cadence with ordinary prose, and gives the unrun research program an honest
bridge. It is closer to the intended thought piece than v15.1.

The candidate is not yet ready for owner review as a finished reading path.
Three problems would be visible to the intended owner almost immediately:

1. The advertised first route is not a 60–90-second route. “How to read this,”
   the scene, the count table, the zero-support explanation, the next-action
   paragraph, and the relation-state key are several hundred words before the
   reader reaches a stable thesis. At normal attentive reading speed, the
   candidate’s declared first path is roughly a three-minute path, not a
   minute-and-a-half path.
2. The candidate opens as a review packet. “Candidate status,” “Empirical
   status,” the term boundary, route instructions, and the sentence about what
   the longer routes must survive all precede the scene. This repeats the
   v15.1 problem of signaling project metadata before earning the reader’s
   attention. The site can carry this status in chrome; the essay should spend
   its first words on the failure and changed decision.
3. The compressed prior-art section is easier to read but less exact than
   v15.1. “Relevant primary and official precedents” (candidate lines 284–295)
   is a blanket authority cue over a list that includes standards, published
   papers, datasets, and recent preprints with different review and status
   boundaries. The full ledger still exists, but the public sentence should
   not imply that the list has a single evidentiary status.

The central reader outcome nevertheless passes in substance:

> Repetition is not automatically independent support. Preserve the relation,
> the claim boundary, the permission, and the human next step so another person
> can inspect and correct the route.

The candidate’s strongest mechanism is also real and visible: a relation change
must change the count and route while preserving the original observation
(lines 199–202). That is more than a slogan. It is the receipt’s operational
test. The remaining work is to put that mechanism inside a shorter, more
memorable first route and restore precise evidence-status language where the
compression now overstates authority.

## What I simulated

I read the candidate as a capable, systems-minded owner who is not a specialist
in provenance, evidence synthesis, or experimental methods. I used three
questions throughout:

- What would I remember if I stopped now?
- What action would I take differently because of this passage?
- Is the passage making a claim, showing a mechanism, or merely naming a
  container?

The owner proxy is attracted by the receipt, the hold, the unknown state, and
the possibility of a small reversible check. The proxy is impatient with route
metadata, unearned status labels, named components without a consequence,
methods jargon, and prose that says the same caveat in several polished forms.

### 60-second path

The candidate instructs the reader to read “Nine tabs, one announcement” and
“The first decision” (lines 13–22). In practice the path behaves as follows:

| Moment | What lands | What fails or remains unstable |
| --- | --- | --- |
| Title / status | The title’s historical continuity is visible; the technical meaning of “discrimination” is carefully bounded. | The first semantic association can still be social classification or a classifier. The reader has also been asked to process three metadata labels before seeing a problem. |
| First 20–30 seconds | “Sandbox pilot,” “90 minutes,” “production data off limits,” and a broad validation claim make the stakes concrete. | The route instructions and status block make the genre feel like an owner packet rather than a thought piece. |
| Scene | Nine favorable articles and one launch announcement clearly show repetition becoming apparent corroboration. | “Nine tabs” is a weaker unit than “nine reports”: tabs are browser state, not evidence records, and can make the example sound like a UI demo. |
| Count table | `09 / 01 / 00 / HOLD` is a powerful decision receipt. | “Known common-origin clusters” is not plain language; the zero-support row invites “why zero if one origin is known?” before the answer arrives. |
| Stop | The reader can say “copies are not automatically independent evidence.” | Unless the reader reaches lines 63–77, they may not know what to preserve or what the team does next. The declared one-minute route therefore does not meet the charter’s full first-impression outcome. |

**60-second verdict: borderline pass for problem recognition, fail for the
promised time budget and complete behavior change.** A reader who stops after
the scene remembers the false-corroboration error. A reader who stops at the
table may think the framework is simply rejecting a vendor claim, rather than
recording a narrower hold and a reversible verification step.

The first route should be no more than approximately 300–350 visible words,
excluding the title, status badge, and a compact table. It should contain only:

1. the nine-report / one-origin scene;
2. one sentence saying what was changed (recurrence was treated as
   independent support);
3. the four receipt values `09 / 01 / 00 / HOLD`; and
4. one sentence saying “zero is not rejection; it means the broad claim has no
   counted support under this rule yet, so inspect one other relation.”

The three-state key and rollback detail belong immediately after that stop
point, not inside the declared first minute.

### Five-minute path

The candidate says the essential route continues through “Three questions
before the answer” (lines 149–217). The prose in the route-intended sections,
including the opening metadata and tables, is materially above a five-minute
read at a normal 220–260 words per minute. It also asks the reader to absorb:

- report / artifact / capture / normalized extract / summary;
- provenance;
- five separate judgments in the claim section;
- eight possible next actions;
- disposition;
- six “not this” distinctions; and
- the difference between the public essay and the Explore route.

The *content* of this route is stronger than v15.1. A reader who spends the
extra time can answer all five contract questions:

1. the problem is false corroboration before generation;
2. nine reports can share an upstream path;
3. the responsibility makes origin, claim, permission, and action judgments
   inspectable;
4. a person can hold, correct, or authorize the next step; and
5. no study or model result exists.

But the route promises a conclusion in five minutes and delivers a compact
design dossier. The likely owner reaction is not “this is too difficult”; it is
“why did the essay make me carry the whole record model to learn the receipt’s
lesson?”

**Five-minute verdict: conceptual pass, route-budget fail.** Put a visible
“five-minute stop” immediately after the third question’s correction invariant.
Move the “full project map,” the six non-collapse sentences, and the destination
note to Explore / the handoff. Target no more than 1,100–1,250 visible words
before that stop, including the receipt but excluding a compact status badge.

### Full read

The full candidate is 3,217 words by the local file count, before any site
chrome or glossary interaction. It is therefore a plausible 14–18-minute main
essay, not a five-minute essay with a few optional appendices. The full read is
more disciplined than v15.1 in proportion and voice, but it has four losses:

- v15.1’s “the summary has not merely shortened the evidence; it has changed
  its structure” is weakened into the more generic “changed what the reports
  mean as evidence” (candidate lines 43–47);
- the contrast roots `B1` and `C1`, which make “separate only in this test”
  tangible, disappear from the manuscript (they can remain in Explore/site);
- the v15.1 source-by-source status distinctions are compressed into a
  “primary and official” list; and
- the detailed lab invariants—fixed denominator, safety set, invalid-output
  handling, exact parity, and shortcut controls—are mostly named rather than
  explained. That is right for the public essay only if the Lab route carries
  the full receipt and the essay does not imply that “pre-run gates” are already
  closed.

The full read still ends with a credible authorial voice. “Perfect lineage for
a false claim is still perfect lineage for a false claim” survives intact.
“If nothing downstream changes, the review control is decorative” is a strong
new operational sentence. The one-week habit is memorable and practical. The
full-read issue is not lack of substance; it is where substance is placed and
how much of it is presented as the same kind of thing.

## Claim, mechanism, consequence, usefulness, research bridge

| Test | Result | Evidence and red-team judgment |
| --- | --- | --- |
| Memorable claim | **Pass after one wording repair** | Lines 405–408 give the best one-week claim: count observations, inspect distinct paths, ask what each supports, leave unresolved unresolved, record the next action. The opening should recover the sharper v15.1 reversal “the summary has not merely shortened the evidence; it has changed its structure.” |
| Actual mechanism | **Pass** | The candidate specifies a chain: classify a relation → change the counted support → change the claim state / route → preserve the prior record. Lines 199–202 make correction consequential. Put this chain in one plain sentence near the first receipt so the essay does not read as a taxonomy of good intentions. |
| Concrete consequence | **Pass, with one ambiguity** | `HOLD · VERIFY ANOTHER ORIGIN RELATION`, sandbox-only permission, no production data, and a 90-minute budget are concrete. “Permitted synthetic rollback check” (lines 73–77) arrives before the reader knows why rollback is the relevant test; call it a bounded local check or defer the word “rollback” to the research section. |
| Bounded usefulness | **Pass in principle; weak one-week transfer** | The use boundary is clear: due diligence / evidence packets / production changes may justify a receipt; rewrites and supplied-input calculations usually do not. Add a five-field mini-receipt that a practitioner can use next week: claim, observations, relation state, permission, next human action. |
| Honest bridge to unrun research | **Pass after jargon/status repair** | Lines 343–379 explicitly state no model, no run, and no result; they commit to null, harm, instability, and shortcut outcomes. “Final tokenizer, denominator, leakage checks, safety checks” is accurate but opaque in the main essay. Translate it once and move the mechanics to Lab. |

The candidate does not make a false empirical claim. The main risk is subtler:
the table labels “Primary intervention,” “planned test cases,” and “current
research question” can make a prepared protocol feel like a validated study to a
fast reader. A single plain status sentence immediately before the research
question should read: **“This is a proposed comparison, not a result; no model
has been selected and no study has run.”**

## Regression and loss ledger

The candidate’s changes are evaluated against the v15.1 manuscript and its
current site, not against an idealized rewrite.

### Improvements to protect

- The sandbox-pilot decision and 90-minute budget enter before the framework
  vocabulary (candidate lines 31–33).
- “The articles have not become false” preserves the crucial distinction between
  common origin and falsity (lines 43–47).
- “One origin is known; zero origins support the broad claim yet” is nearly the
  right explanation of the counterintuitive count (lines 63–71).
- The relation states are translated before the codes: shared path, separate
  only in this test, unresolved (lines 82–98).
- The receipt explicitly says it does not decide the pilot on its own (lines
  115–117).
- The correction invariant is stated in operational terms (lines 195–202).
- The current-decision / outcome-loop distinction is retained without the
  v15.1 C01–C11 parade (lines 221–237).
- The “when not to use it” paragraph is concrete and honest (lines 253–267).
- The objections are direct questions rather than six nearly identical
  component cards (lines 302–336).
- The F0/F1/F2 conditions are translated into ordinary names before their
  technical role is described (lines 353–366).
- The one-week habit and negative-result bridge are the best handoff to actual
  practice (lines 401–418).

### Regressions or losses to repair

| Candidate passage | Regression / loss against v15.1 | Severity | Required response |
| --- | --- | --- | --- |
| Lines 1–25, title, status, “How to read” | The title risk remains; the opening metadata and route instructions make the essay look like a package. The candidate also drops “repeated reports / one origin” from the subtitle, losing an immediate concrete promise. | High for first impression | Keep the historical title provisionally, shorten the subtitle to a concrete promise, move status and route timing to site chrome / a compact note, and begin with the scene. |
| Lines 27–50, “Nine tabs” | “Tabs” is less evidential than “reports.” The v15.1 sentence about changing structure and “eight new roots” is more memorable than “changed what the reports mean as evidence.” | High for memory, medium for comprehension | Rename the section “Nine reports, one origin” or “Nine reports, one announcement.” Restore the structural-reversal sentence and the “no new roots” image. |
| Lines 52–80, first receipt explanation | Stronger consequence than v15.1, but “common-origin clusters” is unexplained and `00` can sound like a rejected or missing origin. Rollback detail arrives early. | High | Use “one known shared path” in the first table; state in the same sentence that zero means “no counted support for this claim yet,” not “no source exists.” Defer rollback. |
| Lines 82–98, relation states | Plain terms are a major gain. “The place a polished summary is tempted to erase” is slightly abstract and “dependent or independence” reintroduces statistical/causal ambiguity. | Medium | Keep the three states; say “unknown is the state a summary most often turns into a guess.” Reserve dependent / independent codes for Lab. |
| Lines 100–117, receipt | Simpler than v15.1 but loses B1/C1 contrast roots and the visible proof that stipulated distinctness is separate from claim support. | Medium | Accept in the short essay; restore B1/C1 and the contrast note in the site / Explore receipt. Do not add the full nine-row ledger to the first route. |
| Lines 119–147, judgment setup | The manual/community example is good. “Cheaper to inspect” and “more likely to change a decision” are useful but the list still feels generated if left as seven parallel adjectives. | Medium | Group into three questions—authority, decision relevance, permission/cost—and keep the contrast. |
| Lines 149–217, three questions | Correct replacement for the v15.1 13-row table, but the “six families and eleven records” sentence is an inventory before the reader needs it. The final destination note is self-conscious. | High for pacing | Delete the inventory sentence from the main route; introduce provenance only after “where it came from.” Move full-map language to Explore. Keep the correction invariant. |
| Lines 219–251, loops and placements | More readable than v15.1. “Current-decision loop,” “outcome loop,” “record types,” and “product box” are still design jargon / product language. | Medium | Define each loop by action first; replace “product box” with “a named component.” Keep the no-retroactive-omniscience sentence. |
| Lines 253–267, use boundary | Better negative space than v15.1. “Dependence-heavy” and “source-sensitive investigation” are unexplained terms. | Low / medium | Say “likely to share sources” and “an investigation where the source path matters.” Keep the ceremony sentence. |
| Lines 269–300, prior art | Readability improves, but status precision and exact provenance weaken. “Primary and official” falsely flattens standards, published work, datasets, and unreviewed preprints. | High for owner trust | Rewrite the heading paragraph as a selected, non-exhaustive precedent map; retain the linked status ledger. Name only the precedents needed to narrow the claim in the essay; keep all recent comparators in Sources. |
| Lines 302–336, objections | Strongest sustained prose in the candidate. It loses v15.1’s explicit task-scoped retirement framing but retains the substance. | Low | Accept with a short “for this task” qualifier in the baseline objection. Do not expand. |
| Lines 338–379, research note | Plain condition names are an improvement. `tokenizer`, `denominator`, `leakage`, `safety checks`, and “primary fictional test cases” are still likely to interrupt a non-specialist. | High for research-status comprehension | Keep the one question, three-condition logic, and result commitment. Move exact gate names and `300` mechanics to Lab; if `300` remains, call it “300 planned fictional cases, subject to design checks.” |
| Lines 381–399, history | Good recovery of v13’s voice and boundary. “Terminal decisions” is more opaque than “recorded decisions.” | Low | Replace one term; keep the historical caution and explicitly retain the v13 image as historical, not current topology. |
| Lines 401–418, memory / close | The strongest one-week behavior is present. The final paragraph has four stacked “too…” possibilities and three “let” clauses, which risks a polished-cadence finish. | Medium for voice | Keep the quote; reduce the closing to one consequence, one test, and one honest next step. |
| Lines 420–431, deep routes / status | This is handoff metadata, not public-essay prose; it duplicates the opening status. | High for genre | Delete from the manuscript or move to site footer / owner packet. Preserve route labels in the site navigation. |

## False authority and AI-slop audit

### False authority cues

The candidate is careful about its own status but creates three avoidable cues:

1. **“Relevant primary and official precedents.”** This reads as a verified
   authority class. Replace with “Selected precedents narrow the claim; the
   linked ledger records publication and review status.”
2. **The table role labels “Primary comparator” and “Primary intervention.”**
   These are protocol terms. They can sound like a study’s established arms
   rather than a plan. Use “planned comparison” and “planned added-cue
   condition” in the essay; reserve the formal labels for Lab.
3. **“Current plan names 300 primary fictional test cases.”** The sentence
   does say it is a design input, but the number can read as statistical
   authority. Say “One draft proposes 300 fictional cases; that number remains
   provisional and no run has occurred.”

The candidate should not restore v15.1’s detailed methods in the public route to
solve this. More method nouns would increase authority theater. Exact status
belongs in the Lab and source ledger, where each gate has an owner and a state.

### Unnatural or model-templated cadence

The candidate is substantially less slop-like than v15.1, but these patterns
remain:

- repeated “The project does not claim… It claims…” / “It does not… It…”
  constructions around lines 204–217 and 269–300;
- the symmetrical lists of seven properties, eight next actions, and six
  “not” distinctions;
- “These are placements, not maturity levels” followed by “A new product box
  does not become a responsibility merely because it is named”; and
- the final sequence “too costly, too easy to game, too difficult… too close…”
  followed by “let readers… let practitioners… let the study…”.

None is individually bad. The repair is selective: keep one reversal or
boundary per paragraph, break the parallel list with a concrete action, and
remove any sentence that only announces the architecture’s restraint.

### Voice worth protecting

These passages sound authored and should survive editing, subject to the small
term changes above:

- “The articles have not become false” and the distinction between reach and
  support (lines 43–47).
- “So the supporting-origin count is zero. That does not mean the tool is
  rejected” (lines 69–71).
- “It makes a hidden change in route visible” (lines 79–80).
- “Unknown is the place a polished summary is tempted to erase” (lines 95–98),
  after a minor plain-language rewrite.
- “If nothing downstream changes, the review control is decorative” (lines
  199–202).
- “Perfect lineage for a false claim is still perfect lineage for a false claim”
  (lines 316–319).
- “A framework that cannot say when it is not worth using becomes a demand for
  ceremony” (lines 266–267).
- “Before saying ‘many sources agree’…” (lines 405–408).

## Terminology and popup shortlist

The public route should remain understandable with every popup closed. The
shortlist below is the maximum useful set; everything else should be translated
or moved to Explore / Lab.

| Term / phrase | First-route treatment | Popup or deeper definition | What it must not imply |
| --- | --- | --- | --- |
| **Origin** | First say “where a report’s information came from,” then use “origin.” | Example: nine reports trace to one launch announcement; a relation trace does not prove the announcement true or relevant to the claim. | A publisher, causal root, truth source, or independent evidence by itself. |
| **Shared path / separate only in this test / unresolved** | Keep these three visible in ordinary language; do not lead with codes. | One-line key plus the receipt example. | Statistical independence or a discovered fact about the real web when the relation is stipulated. |
| **Claim support** | Explain as “what exact claim this passage supports, refutes, or leaves unsettled.” | Optional example using the vendor announcement versus field reliability. | Source popularity, citation presence, or origin count. |
| **Provenance** | Introduce only after the plain definition at candidate lines 157–163. | “A trace of origin, custody, transformation, and time,” with the nine-report example. | Correctness, authority, permission, or independence. |
| **Disposition** | Prefer “recorded human next step”; if the schema term remains, explain once. | Hold / verify / proceed example with the receipt. | Truth, model confidence, or an automatic action. |
| **Discrimination layer** | Keep in title only while the rename test is open; use “pre-answer responsibility” in body copy. | The title note may define technical differentiation and the social meaning it excludes. | A social classifier, protected-class decision, or universal ranking score. |
| **Origin-relation field** | In the research section say “a supplied note about whether reports share a path.” | Lab-only explanation of supplied labels. | Real provenance discovery. |
| **Offline harness** | Say “local test machinery; no model was called.” | Lab-only definition with no visual required. | A completed experiment or deployment. |
| **300 planned cases** | Say “one provisional plan for 300 fictional cases,” or omit from the essay. | Lab-only sample and denominator explanation. | People, model results, statistical confidence, or quality. |
| **Tokenizer / denominator / leakage / safety set** | Do not use in the public five-minute route. | Keep in Lab with explicit plain definitions and gate status. | Evidence that the research is run or approved. |

No popup should be added for every occurrence. A popup is useful only at the
first/highest-value occurrence and must include: a plain definition, one
receipt-grounded example, and a boundary. A static sentence must still work if
JavaScript or the interaction is unavailable.

## Final reading-time promise

The candidate should make this promise, in both manuscript and site route
labels:

> **60–90 seconds:** see the nine-report failure, the `09 / 01 / 00 / HOLD`
> receipt, and the fact that zero counted support is a hold—not a rejection.
> **About five minutes:** understand the three questions, the correction
> invariant, who can change the route, and that the proposal has no empirical
> result.
> **12–15 minutes:** see the loops, use boundary, objections, and the narrow
> research bridge.
> **Optional Lab / Explore / Sources:** inspect the framework records, protocol
> gates, prior-art statuses, and historical artifact.

This is more honest than promising a 15–20-minute “deeper design” route inside
the same manuscript and a separate 10–15-minute “research and history” route
when the candidate’s front matter already consumes much of the first route.
The route labels must point to explicit stop markers, not merely headings.

## Exact acceptance tests

These are candidate acceptance tests. They do not authorize a study, a site
deployment, or external reader recruitment.

### A. First-minute comprehension

Use five owner-proxy readers with no glossary, links, or project context. Give
them only the title, opening scene, compact receipt, and first consequence,
ending at no more than 350 visible prose words. Ask:

1. What went wrong in the example?
2. What should be preserved?
3. What should not be claimed yet?

**Pass:** at least 4/5 answer, in ordinary language, that repeated reports may
share one path; reports/relations should be preserved; and the broad claim is
held rather than accepted or rejected. No answer requires “discrimination
layer,” “provenance,” “F0/F1/F2,” or “origin accounting.”

**Automatic fail examples:** “the articles are false,” “the tool is rejected,”
“the model discovered independence,” “nine sources prove validation,” or “the
receipt makes the pilot decision automatically.”

### B. Five-minute completeness

Place an explicit stop marker after the third question and correction
invariant. Keep that route to at most 1,250 visible prose words, excluding a
compact status badge and the receipt’s small numeric table. Ask the five
contract questions from `source/READER_OUTCOME_AND_READING_PATH_V15_1.md`.

**Pass:** at least 4/5 readers answer all five materially correctly, including
that `09` observations do not equal `09` supporting origins, `HOLD` is a human
next step, and no empirical validation exists. A glossary lookup is not allowed
on the first attempt.

### C. Correction consequentiality

Show a reader the receipt, then change one relation from “shared path” to
“unresolved.” Ask what changes and what remains fixed.

**Pass:** 4/5 say that the support/count/route may change, the original report
remains in history, and the correction does not prove the claim or discover
independence. If a relation correction changes no downstream field, the
candidate fails this test even if the prose sounds clear.

### D. One-week behavior / bounded usefulness

Seven days after reading, ask five readers without showing the quote: “When a
summary says many sources agree, what do you check?” Then give each a
hypothetical evidence packet and three minutes to fill a five-field receipt:
claim, observations, relation state, permission, next human action.

**Pass:** 4/5 spontaneously mention repeated observations versus distinct paths
and unresolved relations; 4/5 complete the five fields without using one score
as a substitute for relation, support, or permission; and no reader treats the
receipt as a truth verdict.

### E. Title / term test

Before and after the title definition, ask five readers what “discrimination
layer” means.

**Pass:** after the definition, at least 4/5 restate a pre-answer information /
action differentiation responsibility rather than a protected-class classifier
or fairness policy. **Rename trigger:** two or more readers still infer the
wrong thesis after the definition, or the alternative “Context judgment layer”
produces equal comprehension with materially less confusion.

### F. Voice / anti-slop review

Have two independent editors annotate the revised candidate for concrete,
generic, or templated sentences.

**Pass:** at least five passages are marked worth protecting; no paragraph has
more than three consecutive abstract sentences without an object, action, or
boundary; no caveat (“no result / not truth / not validation”) is repeated in
more than one form within a route; and no section contains an unbroken
parallel-list cadence longer than five items without an example or consequence.

### G. Status and authority integrity

Run a local text review against the manuscript and route labels.

**Pass conditions:**

- “No model has been selected,” “no study has run,” and “no result” appear at
  the research boundary in one plain-language status sentence.
- The prior-art paragraph says “selected precedents” or equivalent and points
  to the status ledger; it does not call heterogeneous entries “primary and
  official” as one class.
- Every named methods term in the public route is either defined in ordinary
  language first or moved to Lab.
- `300` is labeled provisional and fictional; it is never presented as a
  result, confidence, participant count, or quality score.
- No sentence says the framework improves decisions, discovers provenance,
  establishes independence, validates a product, or proves a broad claim.
- No first-minute route uses `F0`, `F1`, `F2`, `T1`, `N=300`, tokenizer,
  denominator, construct validity, or leakage as unexplained shorthand.

### H. Site / manuscript agreement

No site run was performed in this red team. Before integration, compare the
candidate route labels against the current v15.1 site and update them together.

**Pass conditions:** the site’s first viewport and manuscript use the same
opening claim, the same receipt values, the same status boundary, and the same
stop points; Explore carries the full map and contrast roots; Lab carries the
protocol mechanics; Sources carries the exact prior-art status; and the v13
image remains historical and unchanged. A candidate that passes in Markdown but
leaves the site’s old route timing or v15.1 wording in place is not a coherent
v15.2 owner surface.

## Recommendation to the parent integrator

Accept the candidate’s receipt-first architecture and its shorter prose. Make
the following bounded repairs, then hand it to the owner:

1. Replace “Nine tabs” with “Nine reports” or “Nine reports, one announcement”
   and restore the structural-reversal line from v15.1.
2. Move front-matter status and route instructions into compact owner/site
   chrome; make the first route no more than 350 visible prose words.
3. Put `09 / 01 / 00 / HOLD` and the zero-is-not-rejection explanation in the
   same first-minute stop.
4. Keep the plain three-state relation key; move codes and B1/C1 contrast roots
   to Explore / the receipt detail.
5. Trim the three-question route to 1,250 words and keep the correction
   invariant as its end condition.
6. Replace “primary and official precedents” with an exact status-aware phrase;
   retain the source ledger rather than adding a literature parade.
7. Translate or relocate tokenizer / denominator / leakage / safety terms and
   make the proposed-comparison status explicit.
8. Delete “Canonical deep routes and boundaries” from the public essay. Keep
   route navigation and file references in the owner handoff.

The candidate already contains the idea’s best test. The owner should be asked
whether this receipt changes how they would build an evidence-sensitive system,
not whether the manuscript can carry more components.

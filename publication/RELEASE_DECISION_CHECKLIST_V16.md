# Release-decision checklist — Pattern Map v16

Status: **LOCAL FAIL-CLOSED CHECKLIST — RELEASE NOT AUTHORIZED**

This checklist is a later decision gate, not permission to publish, post,
deploy, merge, or contact anyone. It is intentionally separate from the
public-preview build: local preview should remain `noindex,nofollow` with
publication identity unset until the owner gives an exact instruction.

## 0. Name the decision before touching release metadata

Record the scope of the proposed action, or leave it unresolved:

| Field | Value |
| --- | --- |
| Exact source commit to review | `UNRESOLVED — resolve at use` |
| Proposed artifact(s) | `UNRESOLVED` |
| Owner decision record / instruction | `UNRESOLVED` |
| Final byline | `UNRESOLVED` |
| Canonical URL | `UNRESOLVED` |
| Publication destination | `UNRESOLVED` |
| Author handle | `UNRESOLVED` |
| Social image URL | `UNSET` |
| Social image alternative text | `UNSET` |
| Publication authorization | `NOT GRANTED` |

If any field is unknown, stop at `HOLD`. Do not substitute a test host,
repository URL, temporary handle, guessed name, or remembered metadata.

The exact proposed artifact and channel control which later gates apply. A
gate may be marked `NOT APPLICABLE` only after the artifact is named and the
owner records why that surface is outside the authorized action; for example,
an X-only copy decision does not silently authorize or require a site release.
Unknown applicability remains `HOLD`.

## 1. Owner and content gates

- [ ] The owner explicitly authorized this exact release action and destination.
- [ ] The final source commit is named and rebuilt from a clean checkout.
- [ ] The human-first opening still leads with the problem before protocol,
      release machinery, literature defense, or origin accounting.
- [ ] The 60–90-second entry conveys upstream choices, inspectability/correction,
      human judgment, and breadth beyond common-origin recurrence.
- [ ] All six families remain visible and meaningful.
- [ ] The three examples still cover peripheral/specialist signal, motion or
      expected absence, and common-origin recurrence.
- [ ] The Echo Problem remains a separate unrun project with no results.
- [ ] Signal Foundry and other cases remain bounded illustrations, not
      validation or product results.
- [ ] The contribution ceiling remains an authored human-governed
      design/governance synthesis and testable agenda.

## 2. Build, provenance, and link gates

- [ ] `docs/OWNER_INTENT_V16.sha256` passes before and after the release review.
- [ ] The current site build and focused checks pass, including public/review
      source parity and the public-only navigation spacing regression.
- [ ] The semantic public standalone opens directly and retains the complete
      human-first reading path without review-only chrome.
- [ ] The PDF, if included, is labeled as an untagged visual companion; the
      standalone HTML remains the semantic route.
- [ ] Internal links resolve from the exact artifact location.
- [ ] External links, citations, route paths, and dated sources are rechecked
      immediately before any later authorized release.
- [ ] The public release configuration has the exact owner-supplied schema,
      absolute HTTPS canonical URL, syntactically public host, final byline,
      and social-image alternative text. No value is inferred from this file.
- [ ] The release build is invoked only after the owner changes the status and
      fields in the configuration under that exact authorization.

## 3. Human and accessibility gates

- [ ] Owner/mentor judgment confirms the voice is a continuation of a serious
      conversation and remains open to challenge.
- [ ] A physical keyboard traversal has been completed and recorded.
- [ ] A supported screen-reader review has been completed and recorded.
- [ ] Real 200% zoom/reflow has been inspected.
- [ ] Real forced-colors behavior has been inspected where practical.
- [ ] Native browser print preview has been inspected, including Sources,
      Research, History, and wide tables.
- [ ] Hardware touch behavior has been checked where the artifact needs it.

Proxy screenshots, model reviews, static checks, and in-app-browser automation
may support these checks but cannot mark them complete by assertion.

## 4. Action and claim audit

- [ ] No merge, deployment, public-site replacement, GitHub Release, or
      publication occurred during preparation.
- [ ] No post, direct message, mentor outreach, participant contact, or other
      representational communication occurred during preparation.
- [ ] No model-comparison, empirical, participant, or live-product study was
      run; no provider, corpus, sample, or spend was selected or acquired.
- [ ] Every statement about research, novelty, effectiveness, prevalence, or
      validation is either removed, explicitly bounded, or supported by an
      owner-authorized future evidence record.
- [ ] The final artifact inventory distinguishes canonical content, review
      evidence, and optional rehearsal material.

## 5. Decision

Choose exactly one after the preceding fields and gates are resolved:

- `HOLD — unresolved owner identity, URL, destination, evidence, or manual gate`.
- `REVISE — a bounded content, accessibility, link, or claim correction is needed`.
- `NOT AUTHORIZED — no exact owner instruction for this release action`.
- `GO — only after every required gate is checked and the owner executes the
  separately authorized publication action`.

This local copy is currently **HOLD / NOT AUTHORIZED**. It does not change
`site/publication.config.json`, does not make a release build pass, and does
not select the final byline, URL, handle, social image, or destination.

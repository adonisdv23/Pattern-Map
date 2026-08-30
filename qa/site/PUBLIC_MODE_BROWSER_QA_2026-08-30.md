# Pattern Map v16 public-mode browser QA — 2026-08-30

## Scope and evidence boundary

This check covers the thin `public` presentation adapter built from the same
canonical sources and route IDs as the existing `review` mode. The tested lane
was based on Phase-0 commit `37c7c852ff406431454346eacc694ac04c5f57a5` and
is represented by the commit containing this record.

The routed public build was served over local HTTP at `127.0.0.1`. Inspection
used the Codex in-app browser's responsive viewport control, visible-page DOM,
semantic interactions, screenshots, and tab-scoped print/no-script emulation.
No network or model call was made by the teaching reveal or Apply studio. This
is browser-assisted local QA, not a physical keyboard, assistive-technology,
touch-hardware, comprehension, or publication result.

## Required first viewport

The public Read route begins with the actual prose from
`manuscript/NINETY_SECOND_VERSION.md`; it does not substitute a synopsis.

| viewport | substantive opening top–bottom | in first viewport | page overflow | publication frame |
| --- | ---: | --- | ---: | ---: |
| 1280 × 720 | 458.5–607.0 px | yes | 0 px | 64–1216 px |
| 390 × 844 | 439.1–722.4 px | yes | 0 px | 10–380 px |

Both sizes had exactly one `h1`, three principal navigation links, and no
orientation rail, mobile review guide, route index, source manifest, or
owner-review footer/header language. The public preview reported
`noindex,nofollow` with publication status `LOCAL_PREVIEW_UNSET`.

## Responsive route sweep

All ten routes were visited at 1280 × 720, 821 × 900, and 390 × 844: 30 routed
states in total. Every state had:

- `data-presentation-mode="public"`;
- exactly one `h1`;
- zero document-level horizontal overflow;
- three principal navigation links;
- a `main` landmark and footer; and
- no owner-review orientation rail, mobile review guide, route index, or
  source-manifest disclosure.

The Map retained six family nodes on its route. Home contained exactly one
decision reveal; the other nine routes contained none.

The committed public standalone was also served from the repository root. It
had one `h1`, one `.page-content` child inside the publication frame, all ten
expected standalone section IDs, zero owner-review chrome, zero horizontal
overflow, and `noindex,nofollow`. Its repository-relative historical image
loaded at its preserved 1024 × 1536 intrinsic dimensions.

## Home decision reveal

At 1280 px, the four numbered stages formed one four-card row with no card
overlap. At 390 px, they became one readable column with no document overflow.
Opening the native `details` control exposed three distinct fields:
`BECAME VISIBLE`, `REMAINS UNKNOWN`, and `HUMAN DECISION`. The always-visible
text equivalent remained present when the control was closed.

The reveal contained no form, remote URL, source score, automated action, or
observed-result claim. With script execution disabled, the `no-js` class,
four-stage static sequence, and complete text equivalent remained readable.

Print-media emulation at 816 × 1056 produced a two-column stage sequence and a
three-column visible/unknown/human ledger, hid the interactive summary and site
header, expanded the decision boundary, and retained zero document overflow.
This is print-CSS evidence; native OS print preview remains a manual gate.

## Apply contradiction and progressive disclosure

With Stage 0 set to supplied-material transformation only:

- consequence, uncertainty, and evidence-route budget were disabled;
- each dependent fieldset reported `data-applicability="not-applicable"`;
- the visible explanation said those choices were not applicable rather than
  silently ignored; and
- stale dependent values were reset to the ordinary defaults.

Changing Stage 0 to evidence selection needed enabled all three dependent
groups. A consequential / high-uncertainty / substantial-budget plan produced
the bounded `advanced` / `COMPARE` recommendation with an explicit permission
and human-review gate. Returning Stage 0 to supplied-material-only cleared the
contradictory combination and disabled the groups again.

Throughout those interactions, the five observed-state values remained:

`NOT_RUN` · `NOT_TRIGGERED` · `NOT_OBSERVED` · `NOT_AVAILABLE` · `NOT_RECORDED`.

The plain route recommendation and required gate appeared before the collapsed
internal planning-state simulation and before the collapsed builder/agent
depth. The internal static planning table was also collapsed in the scripted
public view. With script execution disabled, the form and recommendation card
were hidden, the no-script explanation became visible, and the complete static
guide remained natively open and visible. The source therefore fails open to
the readable planning table when JavaScript is unavailable.

## Captures

- `qa/visual/public-mode/public-read-1280x720.jpg`
- `qa/visual/public-mode/public-read-390x844.jpg`
- `qa/visual/public-mode/public-home-reveal-1280x720.jpg`
- `qa/visual/public-mode/public-home-reveal-390x844.jpg`
- `qa/visual/public-mode/public-apply-stage0-1280x720.jpg`

## Manual and release-time residuals

Still open by design:

- physical keyboard traversal and focus order;
- VoiceOver/NVDA or another supported screen reader;
- real 200% zoom and forced-colors use;
- native OS print preview and printer/PDF pagination;
- hardware touch behavior;
- cold mentor/public-reader comprehension and owner visual taste; and
- publication-time identity, canonical URL, social image, link, metadata,
  analytics/cookie (if any), deployment, and share-card verification.

No public release, deployment, publication, external message, study, or spend
was performed by this lane.

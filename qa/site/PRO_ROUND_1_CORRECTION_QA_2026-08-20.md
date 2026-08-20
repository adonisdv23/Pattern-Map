# ChatGPT Pro round-one correction QA

Status: **implementation pass; named manual checks and owner judgment remain open**

Reviewed source checkpoint:
`cc5547def98aeec819eabc68bbf850548e97d4c6`

Corrected implementation checkpoint:
the corrected checkpoint recorded in `handoff/BRANCH_AND_PR_STATE.md`

This report records the repository response to the independent ChatGPT Pro
review. It is implementation and artifact evidence, not reader research,
accessibility certification, framework effectiveness, or evidence that an
agent actually followed the playbook.

## Corrected P0 contracts

### Apply is planning, not an event recorder

The Apply route now derives only a recommended implementation level, next
action, authority gate, planned stopping condition, and optional learning
path. Planning selections never write completed-run or observed-result states.

The pure recommendation contract covers all 54 combinations of consequence,
uncertainty, permission, and repeatability:

- `restricted` permission always recommends `CLARIFY`;
- `human-gate` permission always recommends `HOLD`;
- initial observed state remains `NOT_RUN`, `NOT_TRIGGERED`, `NOT_OBSERVED`,
  `NOT_AVAILABLE`, and `NOT_RECORDED`; and
- a learning option is described as a future possibility, not emitted as a
  completed `LEARNED` or `NOT_LEARNED` event.

The agent Quickstart and full operating guide now open with Stage 0: decide
whether the task contains a real evidence-selection decision. Ordinary
supplied-material work can remain ordinary and does not manufacture evidence
or learning records.

### The Map is a relationship view, not a false pipeline

The conflicting 821–1100-pixel absolute-position override was removed. The
current map uses six ordered family cards plus four line-free relationship
bands: baseline, common origin, authority, and conditional learning. Visible
copy states that the families are not a mandatory sequence.

The layout contract checks the narrow, medium, and wide CSS regimes. Live
browser inspection at 821 and 1024 pixels showed the intended three-column
family grid, two-column record/band layout, no overlap, and no horizontal
overflow. The 390-pixel layout becomes a single readable column, and the
default desktop layout presents all six families in one row.

## Reader and interaction corrections

- The cumulative entry is 250 raw words (249 words under the site token
  contract), opens with a concrete product-release example, presents all six
  family questions, and introduces the framework name after its function.
- A tenth **Guided** route restores a continuous authored reading path while
  retaining the three principal doors and the routed publication structure.
- Essential term meaning remains inline. Optional term buttons provide deeper
  plain-language help, a code-native microvisual, a boundary, and a glossary
  link; they support click, touch, keyboard activation, Escape, and focus
  return.
- No-script Apply hides the enhanced controls and presents a complete static
  decision guide with unchanged initial observed state.
- Live-region output is concise, `IntersectionObserver` enhancement is
  guarded, and discrete touch targets have a 44-pixel minimum.
- New visuals are responsive HTML/CSS teaching objects. No generated bitmap
  was justified or created.

## Verification replay

The following repository checks pass from the corrected source tree:

```text
cd site && npm run build
PASS: built 10 routes and refreshed the standalone export

cd site && npm run check
PASS: route/link/content/semantic/no-script checks
PASS: 54-combination Apply planning-state contract
PASS: narrow/medium/wide Map layout contract
PASS: short-version and plain-language reader contract

python3 qa/editorial/validate_content_interface.py
PASS: 3,289-word essay and 250-word cumulative entry

python3 qa/applied/validate_applied_framework.py
PASS

python3 qa/research/validate_research_boundaries.py
PASS

python3 qa/site/audit_site.py
PASS: 10 routed pages and current planning semantics

python3 docs/verify_owner_intent.py
PASS: locked owner-intent SHA-256
```

The six-page PDF companion was regenerated from the corrected source,
reopened, text-checked, rendered at 144 DPI, and visually inspected. The
standalone export contains ten named route sections and 339 unique IDs.

## Live browser inspection

The corrected local routed site was inspected in the in-app browser at:

- 390 × 844: Home, Map, Apply, and a term helper;
- 821 × 900: Map at the exact former cascade boundary;
- 1024 pixels wide: Map medium layout; and
- the default desktop viewport: Home, Map, Apply, and Guided.

No inspected view had horizontal overflow. The restricted and human-gate
Apply cases yielded `CLARIFY` and `HOLD` respectively while all observed-event
fields stayed in their initial states. The browser console ended with no
errors or warnings.

## Evidence-integrity boundary

The routed-site PNG matrix under
`qa/visual/screenshots-final-v16-polish/` and its original report document the
earlier `a319794f5cf2d395c34e5af4935c9299f12dfd5c` checkpoint. They are
retained as historical QA evidence, but they are superseded for current Map
and Apply semantics because they show the removed connector geometry and the
old event-writing receipt. Current evidence is this exact-checkpoint report,
the source and executable contracts, the live-browser observations above, and
the regenerated PDF renders. No new site screenshot binaries are presented as
if they were captured at the corrected checkpoint recorded in `handoff/BRANCH_AND_PR_STATE.md`.

## Residual checks

These remain deliberately open:

- physical end-to-end keyboard traversal;
- a supported screen-reader pass;
- real browser/OS 200% zoom;
- browser print preview; and
- owner/mentor judgment of voice, comprehension, pacing, terminology, and
  visual taste.

No merge, deployment, publication, empirical or model study, participant
activity, research-provider selection/call, incremental purchase, Release, or
public-site replacement occurred during this correction pass. The ChatGPT Pro
advisory itself was separately and exactly authorized on the owner's existing
account; it is model feedback, not a study or result.

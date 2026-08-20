# Sites publication readiness

Status: `READY_FOR_A_LATER_OWNER_DECISION_NOT_PUBLISHED`

No Site project was created, no version was saved, and nothing was deployed.
The current local server is not a public publication.

## What is ready locally

- A complete server-rendered visual reader under `site/`.
- A five-minute route and a complete route within one canonical page.
- A local visual system with no runtime dependency on remote fonts or images.
- Source-grounded claims, source links, evidence-boundary labels, case-study
  limits, counterarguments, and research-readiness material.
- A tested production build, fresh 1440/720/390 responsive captures, and a
  fully inspected 29-page visual/print PDF companion.
- Local Open Graph/Twitter metadata with a 1200×630 social card generated
  through the current OpenAI image-generation route. Its model name was not
  exposed and is not inferred.
- A deterministic origin-accounting receipt that remains interpretable without
  generated imagery; H1 is archived outside the public tree because of its
  pipeline/gatekeeper risk.
- A four-pass research-design package with a narrow first-paper prospectus,
  protocol/specification, and formative HCI protocol. These are publication
  context only—not empirical results.
- A local repository structure compatible with a later Sites source archive.

## Canonical source files

Content authority:

1. `source/THOUGHT_PIECE_V14.md`
2. `source/FRAMEWORK_COMPONENT_MAP.json`
3. `source/FRAMEWORK_COMPONENT_MAP.md`
4. `source/THESIS_AND_TERMINOLOGY_CONTRACT.md`
5. `source/GLOSSARY.md`
6. `research/CLAIMS_AND_EVIDENCE_REGISTER.csv`
7. `research/REFERENCES.md` and `research/references.bib`

Reader implementation: `site/app/`, with `site/app/content.ts` kept reconciled
to the canonical content for rendering.

PDF renderer: `tools/render_visual_reader_pdf.py`, which consumes the canonical
framework data and curated manuscript content.

## What a later publication would contain

A publication candidate would expose the visual reader, its accessible text
equivalent, citations, counterarguments, bounded product cases, and research
horizon. It would not expose internal review logs, local paths, temporary QA
captures, private application context, credentials, environment files, product
working trees, or mutable repository access.

## What remains provisional

- The thesis is a design proposition, not an outcome claim.
- The eleven-component synthesis has not beaten a simpler baseline.
- Component boundaries, minimum useful metadata, reliable assessment, stopping
  policy, feedback attribution, and domain transfer remain open.
- No reader study establishes comprehension or terminology safety.
- No model benchmark, feasibility pilot, preregistration, participant contact,
  or empirical paper exists; the research package remains design-only.
- The exact historical v13 diagram is preserved and hash-verified; the expected standalone v13 HTML remains unavailable.
- Alpha Solver and Signal Foundry are inspected-document illustrations only.
- The visual PDF is untagged; HTML remains the canonical accessible surface.

## Privacy and attribution review required before publication

- Confirm that every Alpha Solver and Signal Foundry reference may be public and
  that no internal identifier, repository path, customer information, or
  confidential design detail remains.
- Recheck all author names, paper titles, years, URLs, standards references, and
  primary-versus-preprint labels.
- Decide whether the live v13 URL may be named publicly or should remain an
  internal recovery receipt.
- Review the title and the technical definition of `discrimination` for the
  intended audience, jurisdiction, and discoverability context.
- Perform manual keyboard, actual 200% zoom, screen-reader, and print-preview checks;
  decide whether a tagged PDF is required.
- Confirm that `og.png`, its generated-image provenance, and the historical
  v13 DALL-E attribution are appropriate for the intended audience.
- Reconfirm that model-review output and owner intent are not presented as
  evidence.

## Exact owner decision that would authorize publication

The owner must explicitly identify:

1. the approved commit;
2. the intended audience and access level—private, organization-only, or public;
3. whether the product case names and live-v13 attribution may appear;
4. whether the provisional thesis and terminology are approved for that
   audience;
5. whether publication should be the local visual reader as-is or a revised
   shareable framework edition; and
6. explicit authorization to create/save/deploy a Sites version from that exact
   source state.

Approval to review locally, continue drafting, or prepare this readiness record
does not satisfy that publication decision.

## Non-divergent update procedure

If publication is later authorized:

1. Make content changes only in the canonical repository files.
2. Reconcile `site/app/content.ts` and the PDF renderer from those canonical
   sources; do not edit a deployed page as a separate source of truth.
3. Run lint, build, SSR/navigation tests, browser QA, PDF generation, link and
   attribution checks, and privacy review.
4. Commit the exact approved source state locally and, only if separately
   authorized, push it to an approved remote.
5. Build the Sites archive from that exact commit; record its hash and the commit
   SHA.
6. Save a version before deployment and deploy only that saved version with the
   approved access level.
7. Record the Site ID, version ID, deployment URL, access level, commit, archive
   hash, and approval receipt in the repository.
8. For every update, repeat from the canonical repo; never patch the published
   Site independently.

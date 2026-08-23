# Pattern Map v16 local site

This directory contains the local owner-review site for Pattern Recognition /
The Discrimination Layer v16. It has three principal doors—Read the idea,
Explore the map, and Apply it—plus Examples, Boundaries, Sources, Research, and
History routes. An optional tenth Guided route composes one continuous reading
path from the same canonical sources without replacing the three doors. The
content hierarchy and source paths are frozen in
`docs/CONTENT_INTERFACE_FREEZE_V16.md` and its JSON companion.

The routed site is the primary owner-review experience. Wide screens use a
persistent chapter rail; narrow screens use a normal-flow route guide. Map
opens with the current six-family relationship view and a visible text
equivalent. Apply includes a local, reversible route studio that first asks
the Stage 0 evidence-selection question and produces planning recommendations—
level, action, required gate, planned stopping
condition, and learning option—without pretending a run, stop, outcome,
learning review, or human decision occurred. The observed-state fields remain
explicitly unrun/unobserved, and the studio calls no provider or external
service. Read and Examples use distinct editorial and teaching rhythms rather
than repeating one card grid.

The build is dependency-free and reads the canonical Markdown/JSON sources at
build time. It produces ignored transient output under `site/dist/` and a
committed direct-open export under `site/exports/standalone/`.

From this directory:

```sh
npm run build
npm run check
npm run dev
```

The local preview is <http://127.0.0.1:4173/>. `npm run dev` serves the latest
build and does not deploy or publish anything. The owner-review PDF is kept in
`site/exports/` and is generated/inspected separately under the repository PDF
workflow. It is an untagged visual review companion, not the accessibility
route. Use the standalone HTML for semantic headings, landmarks, links, and
assistive-technology navigation.

For visual review, use the routed local preview or the committed standalone
HTML. For a PDF, use `site/exports/pattern-map-v16-owner-review.pdf`; it is the
deliberately composed six-page companion. A browser extension's full-page
capture or a custom jsPDF export is not an equivalent artifact: it may combine
route sections, expand technical disclosures, or impose a non-print viewport.
If a fresh browser print is needed, build first, print one routed page at a
time, and confirm Sources, Research, History, and wide evidence tables in print
preview before sharing the file. The committed standalone is also structurally
checked: every route must remain inside the main publication column before the
build can pass.

The standalone HTML is direct-open within the repository package: CSS and
JavaScript are embedded, while the preserved historical v13 image remains an
explicit repository-relative asset. It has one `All routes` orientation system rather than
pretending one section is current. The site preserves progressive disclosure,
the separate Echo route, the historical/current-map distinction, a no-script
reading path, print styling, and the no-deployment boundary. No public-site
replacement, publication, or deployment is authorized by this package.

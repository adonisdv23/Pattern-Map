# Pattern Map v16 local site

This directory contains the local owner-review site for Pattern Recognition /
The Discrimination Layer v16. It has three principal doors—Read the idea,
Explore the map, and Apply it—plus Examples, Boundaries, Sources, Research, and
History routes. The content hierarchy and source paths are frozen in
`docs/CONTENT_INTERFACE_FREEZE_V16.md` and its JSON companion.

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

The site preserves progressive disclosure, the separate Echo route, the
historical/current-map distinction, a no-script reading path, print styling,
and the no-deployment boundary. No public-site replacement, publication, or
deployment is authorized by this package.

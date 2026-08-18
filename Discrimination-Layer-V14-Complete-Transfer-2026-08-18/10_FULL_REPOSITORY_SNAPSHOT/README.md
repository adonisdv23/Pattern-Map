# Pattern Recognition: The Discrimination Layer

This standalone repository contains the canonical local-owner-review draft of a source-grounded v14 thought piece and visual systems framework about how an AI system decides which information deserves acquisition, comparison, enrichment, preservation, withholding, and influence before generation.

The current maturity is **provisional thought piece and research agenda**. The manuscript, framework map, local visual reader, bounded case studies, research-readiness path, and visual PDF companion are complete for owner review. They are not empirical validation, peer review, a scholarly novelty claim, enterprise validation, or publication authorization.

## Current status

- Repository: local only; no remote, deployment, publication, or external share has been created.
- Branch: `codex/discrimination-layer-thought-piece-v14`
- Literal requested target: `/Users/games/Developer/Discrimination-Layer` (absent and outside the active user home).
- Relocated local sibling target: `/Users/gpt/Documents/Codex/projects/Discrimination-Layer`.
- Alpha Solver: read-only case-study source; pre-existing working-tree changes preserved.
- Signal Foundry: read-only case-study source; pre-existing working-tree changes preserved.
- v13 recovery: the owner-designated live site is the current reference. Its original 1024×1536 diagram is preserved byte-for-byte at `archive/v13/pattern-recognition-diagram-v12.png` and matches supplied SHA-256 `8a8204…3ae`. A post-render DOM reference snapshot is archived at `archive/v13/live-v13-rendered-dom-snapshot.html`; it is not the unavailable standalone source and cannot verify the supplied HTML hash. See [the preflight report](reports/PREFLIGHT_AND_SOURCE_STATUS.md).
- Canonical thought piece: [`source/THOUGHT_PIECE_V14.md`](source/THOUGHT_PIECE_V14.md).
- Canonical framework map: [`source/FRAMEWORK_COMPONENT_MAP.json`](source/FRAMEWORK_COMPONENT_MAP.json) with a human-readable companion.
- Local visual reader: `site/`, served for owner review at `http://127.0.0.1:8773/`.
- PDF: a 29-page A4 visual/print companion under `exports/`; the semantic HTML reader is the accessible canonical reading surface.
- Research expansion: three Luna Max lanes completed an initial pass plus three additional research/critique/build loops. Twelve advisory memos were integrated into a prospectus v0.4, study protocol/specification v0.3, and separate formative reader-study protocol. No study, participant contact, model benchmark, or preregistration occurred. See [the integration report](reports/RESEARCH_EXPANSION_AND_INTEGRATION_REPORT.md).
- Visual assets: six clean generated candidates and signed-in ChatGPT Images previews were compared. E2 remains the bounded worked-example illustration; H1 was archived and removed from the rendered deliverables because of pipeline/gatekeeper risk. One current OpenAI/ChatGPT image-generation request produced the 1200×630 social card. The interface exposed no exact model name, so the ledger does not infer legacy DALL-E 3. The recovered v13 diagram remains the unchanged historical DALL-E-created anchor. See [the image ledger](assets/imagegen/IMAGE_SELECTION_LEDGER.md).
- Earlier external critique: four direct read-only Luna audits remain dispositioned; the single Claude CLI call and the ChatGPT Pro page were exactly documented as unavailable. In the exact owner-designated Claude Work task, the owner manually submitted two review markdown files and twelve PNG captures to `Opus 5 Max`; the resulting visual critique was captured read-only, hashed, and independently dispositioned. Model output is advisory, not evidence.

## Claim boundary

This project is a visually approachable thought piece and systems framework ready for local owner review. It is not a research paper, a novelty claim, an empirical validation, an enterprise-proven method, peer review, or publication authorization. Inspected Alpha Solver and Signal Foundry documents provide bounded implementation illustrations; neither product proves the framework.

## Repository layout

Canonical content lives under `source/`; the integrated research prospectus,
protocols, bibliography, and twelve multi-pass memos live under `research/`;
bounded examples live under `case-studies/`; review receipts live under
`reviews/`; the local-only reading experience lives under `site/`; and handoff/
QA material lives under `reports/` and `exports/`. Historical-source receipts
live under `archive/v13/`; exactness is claimed only for the verified diagram,
not for the unavailable standalone HTML or the live deployment as a whole.

## Local review

```sh
cd site
npm run dev -- --hostname 127.0.0.1 --port 8773
```

Start with `http://127.0.0.1:8773/#five-minute`. No deployment or publication is part of this repository state.

For the shortest handoff, use [`reports/OWNER_REVIEW_GUIDE.md`](reports/OWNER_REVIEW_GUIDE.md). QA evidence is in [`reports/VISUAL_READER_QA_REPORT.md`](reports/VISUAL_READER_QA_REPORT.md), the research-paper path is summarized in [`reports/RESEARCH_EXPANSION_AND_INTEGRATION_REPORT.md`](reports/RESEARCH_EXPANSION_AND_INTEGRATION_REPORT.md), and the later-publication boundary is in [`reports/SITES_PUBLICATION_READINESS.md`](reports/SITES_PUBLICATION_READINESS.md).

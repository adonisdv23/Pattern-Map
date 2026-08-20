# Archive

Everything under this directory is historical evidence or an immutable
transfer. Never rewrite an archived file to reflect a later name, claim, or
decision. Add a new accession record or curated successor instead.

The complete v14 transfer lives under `transfers/v14-complete-2026-08-18/`.
The complete extracted payload of the verified v15.2 owner handoff is
accessioned losslessly under `transfers/v15.2-owner-handoff/`. The exact
distribution ZIP remains preserved at its verified source location until the
owner authorizes an appropriate LFS or Release archival channel.

The `v13/`, `v14/`, `v15/`, `v15.1/`, and `v15.2/` directories are curated,
version-specific indexes into those two immutable transfers. They do not copy
the same historical bytes into a second checkout location. Their selected
anchors are machine-checked by `CHECKPOINT_INDEX.json` and
`verify_checkpoint_index.py`; the transfer manifests remain authoritative for
complete contents.

Run from the repository root:

    python3 archive/verify_checkpoint_index.py

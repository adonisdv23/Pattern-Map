#!/bin/sh

# Run the complete local Pattern Map v16 owner-review verification sequence.
# This is artifact and implementation QA. It does not run a provider, model,
# empirical study, participant activity, deployment, or publication action.

set -eu

qa_repository_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
qa_source_zip=""

usage() {
  printf '%s\n' \
    "Usage: qa/run_owner_review_checks.sh [--source-zip PATH]" \
    "" \
    "--source-zip PATH  Also verify the exact external v15.2 ZIP container." \
    "                   Without it, the clone-contained extracted accession," \
    "                   manifest, sidecar, and hashes are still verified."
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --source-zip)
      if [ "$#" -lt 2 ]; then
        usage >&2
        exit 2
      fi
      qa_source_zip=$2
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      printf 'Unknown argument: %s\n' "$1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

cd "$qa_repository_root"

printf '\n[1/12] Locked owner intent\n'
(
  cd docs
  shasum -a 256 -c OWNER_INTENT_V16.sha256
)

printf '\n[2/12] Immutable v14 transfer ledger\n'
qa_v14_log=$(mktemp -t pattern-map-v14-ledger.XXXXXX)
trap 'rm -f "$qa_v14_log"' EXIT HUP INT TERM
(
  cd archive/transfers/v14-complete-2026-08-18
  shasum -a 256 -c 00_START_HERE/SHA256SUMS.txt > "$qa_v14_log"
)
qa_v14_count=$(wc -l < "$qa_v14_log" | tr -d ' ')
if [ "$qa_v14_count" -ne 429 ]; then
  printf 'FAIL: expected 429 v14 ledger entries; observed %s\n' "$qa_v14_count" >&2
  exit 1
fi
printf 'PASS: %s v14 ledger entries\n' "$qa_v14_count"

printf '\n[3/12] Historical checkpoint index\n'
python3 archive/verify_checkpoint_index.py

printf '\n[4/12] Complete extracted v15.2 accession\n'
if [ -n "$qa_source_zip" ]; then
  python3 archive/transfers/v15.2-owner-handoff/verify_accession.py \
    --source-zip "$qa_source_zip"
else
  python3 archive/transfers/v15.2-owner-handoff/verify_accession.py
  printf '%s\n' \
    "NOTE: exact ZIP-container verification was not requested; use" \
    "      --source-zip PATH when the preserved owner-local ZIP is available."
fi

printf '\n[5/12] Echo curated preservation and preserved deterministic harness\n'
python3 research/the-echo-problem/qa/verify_preserved_sources.py
(
  cd research/the-echo-problem/preserved/v15.2
  PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
)

printf '\n[6/12] Active EP v1.1 provider-free design harness\n'
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover \
  -s research/the-echo-problem/v1_1/harness -p 'test_v1_1.py' -v

printf '\n[7/12] Content-interface and applied-framework contracts\n'
python3 qa/editorial/validate_content_interface.py
python3 qa/applied/validate_framework.py

printf '\n[8/12] Site build and route checks\n'
(
  cd site
  npm run build
  npm run check
)

printf '\n[9/12] Site, visual, and research-boundary audits\n'
python3 qa/site/audit_site.py
python3 qa/visual/verify_image_formats.py
python3 qa/research/validate_research_boundaries.py

printf '\n[10/12] Cross-computer portable-bundle contract\n'
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v qa/handoff/test_portable_bundle.py

printf '\n[11/12] Bounded owner-review manifest\n'
python3 handoff/verify_owner_review_package.py

printf '\n[12/12] Reproducible export and clean authored diff\n'
git diff --exit-code -- site/exports/standalone/pattern-map-v16.html
git diff --exit-code -- site/exports/standalone/pattern-map-v16-public.html
git diff --check

printf '\nPASS: complete local owner-review verification sequence\n'
printf '%s\n' \
  "BOUNDARY: artifact checks are not owner comprehension, physical-keyboard," \
  "supported screen-reader, real browser zoom, real forced-colors, print-preview," \
  "hardware-touch, effectiveness, or empirical evidence."

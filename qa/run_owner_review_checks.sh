#!/bin/sh

# Run the complete local Pattern Map v16 owner-review verification sequence.
# This is artifact and implementation QA. It does not run a provider, model,
# empirical study, participant activity, deployment, or publication action.

set -eu

qa_repository_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
qa_source_zip=""
qa_signal_packet_checkpoint="529852497109dc152928de642038d07b109a52e2"
qa_signal_packet_worktree=""
qa_extracted_package=0

usage() {
  printf '%s\n' \
    "Usage: qa/run_owner_review_checks.sh [--source-zip PATH] [--extracted-package]" \
    "" \
    "--source-zip PATH  Also verify the exact external v15.2 ZIP container." \
    "                   Without it, the clone-contained extracted accession," \
    "                   manifest, sidecar, and hashes are still verified." \
    "--extracted-package  Run only checks that are truthful without .git." \
    "                     Git-tip, canonical Signal-packet, and authored-diff" \
    "                     stages are reported NOT RUN, never PASS."
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
    --extracted-package)
      qa_extracted_package=1
      shift
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

qa_git_checkout=0
if command -v git >/dev/null 2>&1 \
  && git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  qa_git_top=$(git rev-parse --show-toplevel)
  qa_git_top_physical=$(CDPATH= cd -- "$qa_git_top" && pwd -P)
  qa_repository_root_physical=$(CDPATH= cd -- "$qa_repository_root" && pwd -P)
  if [ "$qa_git_top_physical" = "$qa_repository_root_physical" ]; then
    qa_git_checkout=1
  fi
fi

if [ "$qa_extracted_package" -eq 0 ] && [ "$qa_git_checkout" -eq 0 ]; then
  printf '%s\n' \
    "FAIL: complete owner-review verification requires a Git clone/worktree." \
    "This appears to be an extracted package. Start with:" \
    "  handoff/START_HERE_OWNER_REVIEW.md" \
    "Then use:" \
    "  sh qa/run_owner_review_checks.sh --extracted-package" >&2
  exit 1
fi

if [ "$qa_extracted_package" -eq 0 ]; then
  qa_initial_dirty_state=$(git status --porcelain=v1 --untracked-files=all)
  if [ -n "$qa_initial_dirty_state" ]; then
    printf '%s\n' \
      "FAIL: complete owner-review verification requires a clean tracked and" \
      "      untracked Git worktree before stage 1." >&2
    exit 1
  fi
fi

printf '\n[1/12] Locked owner intent\n'
(
  cd docs
  shasum -a 256 -c OWNER_INTENT_V16.sha256
)

printf '\n[2/12] Immutable v14 transfer ledger\n'
qa_v14_log=$(mktemp -t pattern-map-v14-ledger.XXXXXX)
cleanup() {
  rm -f "$qa_v14_log"
  if [ -n "$qa_signal_packet_worktree" ] && [ -d "$qa_signal_packet_worktree" ]; then
    git -C "$qa_repository_root" worktree remove --force "$qa_signal_packet_worktree" >/dev/null 2>&1 || true
  fi
}
trap cleanup EXIT HUP INT TERM
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

printf '\n[9/12] Site, visual, publication-rehearsal, and research-boundary audits\n'
python3 qa/site/audit_site.py
sh qa/site/headless_print_contract.sh
python3 qa/visual/verify_image_formats.py
if [ -f qa/publication/publication-kit-contract.spec.mjs ]; then
  node qa/publication/publication-kit-contract.spec.mjs
else
  printf '%s\n' \
    "NOTE: optional publication-rehearsal lane is absent; core owner-review checks continue."
fi
python3 qa/research/validate_research_boundaries.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover \
  -s qa/research -p 'test_*.py' -v

printf '\n[10/12] Cross-computer Signal Foundry packet contract\n'
if [ "$qa_extracted_package" -eq 1 ]; then
  printf '%s\n' \
    "NOT RUN: this stage requires Git commit identity and the canonical" \
    "         Signal Foundry packet checkpoint. Extracted-package verification" \
    "         does not impersonate that Git-only evidence."
else
  qa_current_head=$(git rev-parse --verify HEAD)
  if [ "$qa_current_head" = "$qa_signal_packet_checkpoint" ]; then
    PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v qa/handoff/test_portable_bundle.py
  else
    if ! git cat-file -e "$qa_signal_packet_checkpoint^{commit}" 2>/dev/null; then
      printf 'FAIL: canonical Signal Foundry packet checkpoint is unavailable: %s\n' \
        "$qa_signal_packet_checkpoint" >&2
      exit 1
    fi
    qa_signal_packet_worktree=$(mktemp -d -t pattern-map-signal-packet.XXXXXX)
    rmdir "$qa_signal_packet_worktree"
    git worktree add --quiet --detach "$qa_signal_packet_worktree" \
      "$qa_signal_packet_checkpoint"
    printf 'NOTE: current work continues after the sealed Signal Foundry packet;\n'
    printf '      verifying its exact canonical source checkpoint %s instead.\n' \
      "$qa_signal_packet_checkpoint"
    (
      cd "$qa_signal_packet_worktree"
      PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v \
        qa/handoff/test_portable_bundle.py
    )
    git worktree remove --force "$qa_signal_packet_worktree"
    qa_signal_packet_worktree=""
  fi
fi

printf '\n[11/12] Owner-package controls and bounded owner-review manifest\n'
if [ "$qa_extracted_package" -eq 1 ]; then
  printf '%s\n' \
    "NOT RUN: authoring/builder adversarial tests require a Git executable and" \
    "         temporary Git repositories; wrapper-root VERIFY_PACKAGE.py is the" \
    "         complete received-file integrity check."
else
  PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v \
    qa/handoff/test_owner_review_bundle.py
fi
python3 handoff/verify_owner_review_package.py

printf '\n[12/12] Reproducible export and clean authored diff\n'
if [ "$qa_extracted_package" -eq 1 ]; then
  printf '%s\n' \
    "NOT RUN: authored export diffs and clean-tree checks require Git." \
    "         Stage 11 still checks the bounded selected-artifact hashes." \
    "PASS: extracted-package artifact/implementation checks completed with" \
    "      Git-only stages 10 and 12 explicitly NOT RUN." \
    "NEXT: use VERIFY_PACKAGE.py at the wrapper root for the complete shipped" \
    "      file-set/hash check, and a Git clone/worktree for the full 12 stages."
else
  git diff --exit-code -- site/exports/standalone/pattern-map-v16.html
  git diff --exit-code -- site/exports/standalone/pattern-map-v16-public.html
  git diff --check
  qa_dirty_state=$(git status --porcelain=v1 --untracked-files=all)
  if [ -n "$qa_dirty_state" ]; then
    printf '%s\n' \
      "FAIL: complete owner-review verification requires a clean tracked and" \
      "      untracked Git worktree at stage 12." >&2
    exit 1
  fi
  printf '\nPASS: complete local owner-review verification sequence\n'
fi
printf '%s\n' \
  "BOUNDARY: artifact checks are not owner comprehension, physical-keyboard," \
  "supported screen-reader, real browser zoom, real forced-colors, print-preview," \
  "hardware-touch, effectiveness, or empirical evidence."

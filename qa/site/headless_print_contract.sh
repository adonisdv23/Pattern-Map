#!/bin/sh

# Verify the actual JavaScript-enabled public Apply print output. This is a
# localhost/headless implementation proxy, not a native print-preview or human
# accessibility result.

set -eu

qa_print_root=$(CDPATH= cd -- "$(dirname -- "$0")/../.." && pwd)
qa_print_chrome=${CHROME_BIN:-}
qa_print_pdftotext=${PDFTOTEXT_BIN:-}

if [ -z "$qa_print_chrome" ]; then
  if command -v google-chrome >/dev/null 2>&1; then
    qa_print_chrome=$(command -v google-chrome)
  elif command -v chromium >/dev/null 2>&1; then
    qa_print_chrome=$(command -v chromium)
  elif [ -x "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" ]; then
    qa_print_chrome="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
  fi
fi

if [ -z "$qa_print_chrome" ] || [ ! -x "$qa_print_chrome" ]; then
  printf '%s\n' "SKIP headless public-Apply print contract: Chrome/Chromium unavailable"
  exit 0
fi
if [ -z "$qa_print_pdftotext" ] && command -v pdftotext >/dev/null 2>&1; then
  qa_print_pdftotext=$(command -v pdftotext)
fi
if [ -z "$qa_print_pdftotext" ] || [ ! -x "$qa_print_pdftotext" ]; then
  printf '%s\n' "SKIP headless public-Apply print contract: pdftotext unavailable"
  exit 0
fi

qa_print_tmp=$(mktemp -d -t pattern-map-headless-print.XXXXXX)
qa_print_server_pid=""
qa_print_chrome_pid=""
cleanup_print_contract() {
  if [ -n "$qa_print_chrome_pid" ] && kill -0 "$qa_print_chrome_pid" 2>/dev/null; then
    kill "$qa_print_chrome_pid" 2>/dev/null || true
    wait "$qa_print_chrome_pid" 2>/dev/null || true
  fi
  if [ -n "$qa_print_server_pid" ] && kill -0 "$qa_print_server_pid" 2>/dev/null; then
    kill "$qa_print_server_pid" 2>/dev/null || true
    wait "$qa_print_server_pid" 2>/dev/null || true
  fi
  if [ -d "$qa_print_tmp" ]; then
    find "$qa_print_tmp" -depth -delete
  fi
}
trap cleanup_print_contract EXIT HUP INT TERM

qa_print_port=$(python3 - <<'PY'
import socket

with socket.socket() as listener:
    listener.bind(("127.0.0.1", 0))
    print(listener.getsockname()[1])
PY
)
qa_print_url="http://127.0.0.1:${qa_print_port}/apply/"
qa_print_standalone_url=$(python3 - "$qa_print_root/site/exports/standalone/pattern-map-v16-public.html" <<'PY'
import sys
from pathlib import Path

print(Path(sys.argv[1]).resolve().as_uri())
PY
)
qa_print_cdp_port=$(python3 - <<'PY'
import socket

with socket.socket() as listener:
    listener.bind(("127.0.0.1", 0))
    print(listener.getsockname()[1])
PY
)

(
  cd "$qa_print_root/site"
  SITE_PORT="$qa_print_port" node serve.mjs --public
) >"$qa_print_tmp/server.log" 2>&1 &
qa_print_server_pid=$!

python3 - "$qa_print_url" <<'PY'
import sys
import time
import urllib.request

url = sys.argv[1]
for _ in range(100):
    try:
        with urllib.request.urlopen(url, timeout=0.5) as response:
            if response.status == 200:
                break
    except Exception:
        time.sleep(0.05)
else:
    raise SystemExit("FAIL headless public-Apply print contract: localhost server unavailable")
PY

"$qa_print_chrome" \
  --headless=new \
  --disable-background-networking \
  --disable-component-update \
  --disable-gpu \
  --disable-sync \
  --metrics-recording-only \
  --no-default-browser-check \
  --no-first-run \
  --remote-debugging-port="$qa_print_cdp_port" \
  --safebrowsing-disable-auto-update \
  --user-data-dir="$qa_print_tmp/chrome-profile" \
  about:blank >"$qa_print_tmp/chrome.log" 2>&1 &
qa_print_chrome_pid=$!

python3 - "$qa_print_cdp_port" <<'PY'
import json
import sys
import time
import urllib.request

url = f"http://127.0.0.1:{sys.argv[1]}/json/list"
for _ in range(100):
    try:
        with urllib.request.urlopen(url, timeout=0.5) as response:
            if any(item.get("type") == "page" for item in json.load(response)):
                break
    except Exception:
        time.sleep(0.05)
else:
    raise SystemExit("FAIL headless public-Apply print contract: DevTools target unavailable")
PY

node --input-type=module - "$qa_print_url" "$qa_print_standalone_url" "$qa_print_cdp_port" "$qa_print_tmp/apply.pdf" "$qa_print_tmp/standalone.pdf" <<'NODE'
import fs from "node:fs";

const [pageUrl, standaloneUrl, cdpPort, pdfPath, standalonePdfPath] = process.argv.slice(2);
const targets = await fetch(`http://127.0.0.1:${cdpPort}/json/list`).then((response) => response.json());
const target = targets.find((item) => item.type === "page");
if (!target) throw new Error("no DevTools page target");

const socket = new WebSocket(target.webSocketDebuggerUrl);
await new Promise((resolve, reject) => {
  socket.addEventListener("open", resolve, { once: true });
  socket.addEventListener("error", reject, { once: true });
});
let nextId = 1;
const pending = new Map();
socket.addEventListener("message", (event) => {
  const message = JSON.parse(event.data);
  const waiter = pending.get(message.id);
  if (!waiter) return;
  pending.delete(message.id);
  if (message.error) waiter.reject(new Error(JSON.stringify(message.error)));
  else waiter.resolve(message.result);
});
const send = (method, params = {}) => new Promise((resolve, reject) => {
  const id = nextId++;
  pending.set(id, { resolve, reject });
  socket.send(JSON.stringify({ id, method, params }));
});
const evaluate = async (expression) => {
  const result = await send("Runtime.evaluate", { expression, returnByValue: true });
  if (result.exceptionDetails) throw new Error(JSON.stringify(result.exceptionDetails));
  return result.result.value;
};
const delay = (milliseconds) => new Promise((resolve) => setTimeout(resolve, milliseconds));

const printPage = async (url, outputPath, label) => {
  await send("Page.navigate", { url });
  for (let attempt = 0; attempt < 100; attempt += 1) {
    const ready = await evaluate('document.readyState === "complete" && document.documentElement.dataset.enhanced === "true"');
    if (ready) break;
    if (attempt === 99) throw new Error(`${label} did not become ready`);
    await delay(50);
  }
  const guideWasClosed = await evaluate('document.querySelector("[data-progressive-static-guide]").open === false');
  if (!guideWasClosed) throw new Error(`${label} progressive guide was not closed before printing`);

  const printed = await send("Page.printToPDF", {
    displayHeaderFooter: false,
    preferCSSPageSize: true,
    printBackground: true,
  });
  fs.writeFileSync(outputPath, Buffer.from(printed.data, "base64"));

  for (let attempt = 0; attempt < 40; attempt += 1) {
    if (await evaluate('document.querySelector("[data-progressive-static-guide]").open === false')) return;
    if (attempt === 39) throw new Error(`${label} progressive guide screen state was not restored after printing`);
    await delay(50);
  }
};

await send("Page.enable");
await send("Runtime.enable");
await printPage(pageUrl, pdfPath, "public Apply route");
await printPage(standaloneUrl, standalonePdfPath, "public standalone");
socket.close();
NODE

"$qa_print_pdftotext" -layout "$qa_print_tmp/apply.pdf" "$qa_print_tmp/apply.txt"
"$qa_print_pdftotext" -layout "$qa_print_tmp/standalone.pdf" "$qa_print_tmp/standalone.txt"
python3 - "$qa_print_tmp/apply.txt" "$qa_print_tmp/standalone.txt" <<'PY'
import re
import sys
from pathlib import Path

ordered = [
    "material claim judgment",
    "comparison",
    "selection or withholding",
    "permission resolution",
    "memory reuse",
    "acquisition",
    "human action gate",
    "consequential external influence",
]
for label, path in zip(("public Apply route", "public standalone"), sys.argv[1:]):
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    normalized = re.sub(r"\s+", " ", text)
    cursor = 0
    for phrase in ordered:
        cursor = normalized.find(phrase, cursor)
        if cursor < 0:
            raise SystemExit(f"FAIL headless print contract ({label}): missing ordered phrase {phrase!r}")
        cursor += len(phrase)
    for token in ("ORDINARY_RECORD", "NOT_RUN", "NOT_TRIGGERED", "NOT_OBSERVED"):
        if token not in normalized:
            raise SystemExit(f"FAIL headless print contract ({label}): missing {token}")
    print(f"PASS headless print contract ({label}): {len(text)} extracted characters")
PY

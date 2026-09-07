import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import { fileURLToPath } from "node:url";

const QA_DIR = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(QA_DIR, "../..");
const read = (relativePath) => fs.readFileSync(path.join(ROOT, relativePath), "utf8");

const sources = read("site/dist/sources/index.html");
const research = read("site/dist/research/index.html");
const boundaries = read("site/dist/boundaries/index.html");
const history = read("site/dist/history/index.html");
const publicRead = read("site/public-dist/read/index.html");
const publicSources = read("site/public-dist/sources/index.html");
const publicResearch = read("site/public-dist/research/index.html");
const publicBoundaries = read("site/public-dist/boundaries/index.html");
const publicHistory = read("site/public-dist/history/index.html");
const reviewStandalone = read("site/exports/standalone/pattern-map-v16.html");
const publicStandalone = read("site/exports/standalone/pattern-map-v16-public.html");
const siteScript = read("site/src/site.js");

const plainText = (html) => html
  .replace(/<[^>]+>/g, " ")
  .replaceAll("&amp;", "&")
  .replaceAll("&#39;", "'")
  .replaceAll("&quot;", '"')
  .replace(/\s+/g, " ")
  .trim();

const anchorsIn = (html) => [...html.matchAll(/<a\b[^>]*href="([^"]+)"[^>]*>([\s\S]*?)<\/a>/g)]
  .map((match) => ({ href: match[1], label: plainText(match[2]) }));

const exactHrefFor = (html, labelPart) => {
  const matches = anchorsIn(html).filter((anchor) => anchor.label.includes(labelPart));
  assert.ok(matches.length >= 1, `expected at least one rendered link labeled ${labelPart}; found none`);
  const destinations = new Set(matches.map((match) => match.href));
  assert.equal(destinations.size, 1, `rendered links labeled ${labelPart} disagree about their exact destination`);
  return matches[0].href;
};

for (const [sourcesHtml, researchHtml, mode] of [
  [sources, research, "review"],
  [publicSources, publicResearch, "public"],
]) {
  assert.equal(exactHrefFor(sourcesHtml, "V16 claims and source ledger"), "../sources/index.html#claims-ledger-document", `${mode} claims-ledger destination drifted`);
  assert.equal(exactHrefFor(sourcesHtml, "EP v0.1 project"), "../research/index.html#echo-identity-document", `${mode} Echo identity destination drifted`);
  assert.equal(exactHrefFor(sourcesHtml, "status/no-results record"), "../research/index.html#echo-status-document", `${mode} Echo status destination drifted`);
  assert.equal(exactHrefFor(researchHtml, "THE_DISCRIMINATION_LAYER_RESEARCH_AGENDA.md"), "../research/index.html#research-agenda-document", `${mode} agenda destination drifted`);
  assert.equal(exactHrefFor(researchHtml, "future-studies/DL_PLAYBOOK_MATCHED_BUDGET_PROTOCOL_V0_1.md"), "../research/index.html#dl-playbook-protocol-document", `${mode} protocol destination drifted`);
  assert.equal(exactHrefFor(researchHtml, "the-echo-problem/README.md"), "../research/index.html#echo-identity-document", `${mode} Echo README destination drifted`);
  assert.equal(exactHrefFor(researchHtml, "Status and evidence boundary"), "../research/index.html#echo-status-document", `${mode} Echo status link drifted`);
  assert.equal(exactHrefFor(researchHtml, "Open the exact Echo identity and no-results record"), "../research/index.html#echo-identity-document", `${mode} Echo callout destination drifted`);
}

assert.equal(exactHrefFor(publicRead, "Open the mentor handoff"), "#mentor-handoff-document");
assert.match(
  publicRead,
  /<details id="mentor-handoff-disclosure"><summary id="mentor-heading">[\s\S]*?<div class="reading-column" id="mentor-handoff-document">/,
  "public mentor handoff target is not nested inside the actual disclosure",
);
assert.equal(exactHrefFor(publicStandalone, "Open the mentor handoff"), "#read-mentor-handoff-document");
assert.match(
  publicStandalone,
  /<details id="read-mentor-handoff-disclosure"><summary id="read-mentor-heading">[\s\S]*?<div class="reading-column" id="read-mentor-handoff-document">/,
  "public standalone mentor target is not nested inside the actual disclosure",
);

for (const [label, repositoryPath] of [
  ["Locked v16 owner intent", "docs/OWNER_INTENT_V16.md"],
  ["Thesis and audience contract", "docs/THESIS_AND_AUDIENCE_CONTRACT_V16.md"],
]) {
  for (const [sourcesHtml, mode] of [[sources, "review"], [publicSources, "public"]]) {
    assert.equal(anchorsIn(sourcesHtml).some((anchor) => anchor.label.includes(label)), false, `${mode} ${label} is presented as a routed document although it is not rendered`);
    assert.match(
      sourcesHtml,
      new RegExp(`<span class="owner-package-reference">${label}[\\s\\S]*?Owner package path: <code>${repositoryPath.replaceAll(".", "\\.")}</code>`),
      `${mode} ${label} lacks its honest owner-package path`,
    );
  }
}

for (const [label, repositoryPath] of [
  ["Relation to v16", "research/the-echo-problem/RELATION_TO_V16.md"],
  ["EP v0.1 version history", "research/the-echo-problem/VERSION_HISTORY.md"],
  ["EP v1.1 design checkpoint", "research/the-echo-problem/v1_1/README.md"],
  ["Preserved v15.2 index", "research/the-echo-problem/PRESERVED_V15_2_INDEX.md"],
  ["Future execution plan", "research/the-echo-problem/FUTURE_EXECUTION_PLAN.md"],
  ["QA evidence", "research/the-echo-problem/qa/EP_V0_1_QA.md"],
  ["Immutable v15.2 accession", "archive/transfers/v15.2-owner-handoff/ACCESSION_RECORD.md"],
]) {
  for (const [researchHtml, mode] of [[research, "review"], [publicResearch, "public"]]) {
    assert.equal(anchorsIn(researchHtml).some((anchor) => anchor.label.includes(label)), false, `${mode} ${label} collapses a non-rendered Echo document into site navigation`);
    assert.ok(researchHtml.includes(`Owner package path: <code>${repositoryPath}</code>`), `${mode} ${label} lacks its owner-package path`);
  }
}

for (const repositoryPath of [
  "archive/transfers/v14-complete-2026-08-18/10_FULL_REPOSITORY_SNAPSHOT/reports/V13_RECOVERY_AND_INTENT_MEMO.md",
  "archive/transfers/v14-complete-2026-08-18/10_FULL_REPOSITORY_SNAPSHOT/source/THOUGHT_PIECE_V14.md",
  "archive/transfers/v14-complete-2026-08-18/03_RESEARCH_PACKAGE/PRIOR_ART_AND_ADJACENT_FIELDS_MAP.md",
  "archive/transfers/v14-complete-2026-08-18/03_RESEARCH_PACKAGE/REFERENCES.md",
]) {
  assert.ok(sources.includes(`Owner package path: <code>${repositoryPath}</code>`), `historical source lacks owner-package path: ${repositoryPath}`);
  assert.ok(publicSources.includes(`Owner package path: <code>${repositoryPath}</code>`), `public historical source lacks owner-package path: ${repositoryPath}`);
}

for (const repositoryPath of [
  "archive/transfers/v14-complete-2026-08-18/05_HISTORICAL_V13/LIVE_SITE_REFERENCE_MANIFEST.json",
  "archive/transfers/v14-complete-2026-08-18/05_HISTORICAL_V13/V13_RECOVERY_AND_INTENT_MEMO.md",
  "archive/transfers/v14-complete-2026-08-18/05_HISTORICAL_V13/live-v13-rendered-dom-snapshot.html",
  "archive/transfers/v14-complete-2026-08-18/05_HISTORICAL_V13/pattern-recognition-diagram-v12.png",
]) {
  assert.ok(history.includes(`Owner package path: <code>${repositoryPath}</code>`), `history source lacks owner-package path: ${repositoryPath}`);
  assert.ok(publicHistory.includes(`Owner package path: <code>${repositoryPath}</code>`), `public history source lacks owner-package path: ${repositoryPath}`);
}

for (const [detailsId, documentId] of [
  ["claims-ledger-disclosure", "claims-ledger-document"],
  ["dl-playbook-protocol-disclosure", "dl-playbook-protocol-document"],
  ["echo-documents-disclosure", "echo-identity-document"],
  ["echo-documents-disclosure", "echo-status-document"],
]) {
  const routePairs = detailsId.startsWith("claims")
    ? [[sources, "review"], [publicSources, "public"]]
    : [[research, "review"], [publicResearch, "public"]];
  for (const [routeHtml, mode] of routePairs) {
    const detailsIdPosition = routeHtml.indexOf(`id="${detailsId}"`);
    const detailsStart = routeHtml.lastIndexOf("<details", detailsIdPosition);
    const documentStart = routeHtml.indexOf(`id="${documentId}"`, detailsStart);
    const detailsEnd = routeHtml.indexOf("</details>", detailsStart);
    assert.ok(detailsIdPosition > detailsStart && documentStart > detailsIdPosition && detailsEnd > documentStart, `${mode} ${documentId} is not nested in its named disclosure`);
  }
}

const echoCallout = research.match(/<div class="echo-callout">([\s\S]*?)<\/div><details id="echo-documents-disclosure">/)?.[1] ?? "";
assert.ok(echoCallout, "Echo callout could not be isolated");
assert.equal(anchorsIn(echoCallout).some((anchor) => /#echo$/.test(anchor.href)), false, "Echo callout still links to its own section");

for (const [reviewHtml, publicHtml, targetId] of [
  [boundaries, publicBoundaries, "artifact-boundaries-document"],
  [sources, publicSources, "claims-ledger-document"],
  [research, publicResearch, "research-overview-document"],
  [research, publicResearch, "research-agenda-document"],
  [research, publicResearch, "dl-playbook-protocol-document"],
  [research, publicResearch, "echo-identity-document"],
  [research, publicResearch, "echo-status-document"],
  [history, publicHistory, "origin-note-document"],
  [history, publicHistory, "source-lineage-document"],
  [history, publicHistory, "archive-index-document"],
  [history, publicHistory, "archive-v13-document"],
]) {
  assert.ok(reviewHtml.includes(`id="${targetId}"`), `review rendered source target is missing: ${targetId}`);
  assert.ok(publicHtml.includes(`id="${targetId}"`), `public rendered source target is missing: ${targetId}`);
}

for (const [standaloneHtml, mode] of [[reviewStandalone, "review"], [publicStandalone, "public"]]) {
  for (const [href, id] of [
    ["#sources-claims-ledger-document", "sources-claims-ledger-document"],
    ["#research-research-agenda-document", "research-research-agenda-document"],
    ["#research-dl-playbook-protocol-document", "research-dl-playbook-protocol-document"],
    ["#research-echo-identity-document", "research-echo-identity-document"],
    ["#research-echo-status-document", "research-echo-status-document"],
  ]) {
    assert.ok(standaloneHtml.includes(`href="${href}"`), `${mode} standalone export lacks exact document destination ${href}`);
    assert.ok(standaloneHtml.includes(`id="${id}"`), `${mode} standalone export lacks exact document target ${id}`);
  }
  for (const id of [
    "boundaries-artifact-boundaries-document",
    "sources-claims-ledger-document",
    "research-research-overview-document",
    "research-research-agenda-document",
    "research-dl-playbook-protocol-document",
    "research-echo-identity-document",
    "research-echo-status-document",
    "history-origin-note-document",
    "history-source-lineage-document",
    "history-archive-index-document",
    "history-archive-v13-document",
  ]) {
    assert.ok(standaloneHtml.includes(`id="${id}"`), `${mode} standalone export lacks normalized document target ${id}`);
  }
}

const eventListeners = new Map();
const registerListener = (type, listener) => {
  const listeners = eventListeners.get(type) ?? [];
  listeners.push(listener);
  eventListeners.set(type, listeners);
};
const classList = { add() {}, remove() {}, toggle() {} };
let scrollCount = 0;
let focusCount = 0;
const outerDisclosure = { open: false, parentElement: null };
const innerDisclosure = {
  open: false,
  parentElement: { closest: (selector) => selector === "details" ? outerDisclosure : null },
};
const initialTarget = {
  closest: (selector) => selector === "details" ? innerDisclosure : null,
  scrollIntoView: ({ block }) => {
    assert.equal(block, "start");
    scrollCount += 1;
  },
  focus: () => {
    focusCount += 1;
  },
};
const secondDisclosure = { open: false, parentElement: null };
const secondTarget = {
  closest: (selector) => selector === "details" ? secondDisclosure : null,
  scrollIntoView: () => {
    scrollCount += 1;
  },
  focus: () => {
    focusCount += 1;
  },
};
const targets = new Map([
  ["claims-ledger-document", initialTarget],
  ["echo-status-document", secondTarget],
]);
const windowMock = {
  location: {
    hash: "#claims-ledger-document",
    href: "https://pattern-map.test/sources/index.html#claims-ledger-document",
  },
  addEventListener: registerListener,
  requestAnimationFrame: (callback) => callback(),
  innerHeight: 800,
  innerWidth: 1280,
  scrollY: 0,
};
const documentMock = {
  querySelectorAll: () => [],
  querySelector: () => null,
  getElementById: (id) => targets.get(id) ?? null,
  addEventListener: registerListener,
  documentElement: { classList, dataset: {} },
};

vm.runInNewContext(siteScript, {
  document: documentMock,
  window: windowMock,
  console,
  Map,
  Set,
  Date,
  URL,
  decodeURIComponent,
});

assert.equal(innerDisclosure.open, true, "initial hash did not open the closest disclosure");
assert.equal(outerDisclosure.open, true, "initial hash did not open an outer disclosure ancestor");
assert.equal(scrollCount, 1, "initially hidden hash target was not scrolled into view after reveal");
assert.equal(focusCount, 0, "initial hash reveal hijacked focus");

innerDisclosure.open = false;
outerDisclosure.open = false;
const sameHashAnchor = { href: windowMock.location.href };
const sameHashClick = {
  target: {
    closest: (selector) => selector === "a[href]" ? sameHashAnchor : null,
  },
};
for (const listener of eventListeners.get("click") ?? []) listener(sameHashClick);
assert.equal(innerDisclosure.open, true, "same-hash document link did not reopen the closest disclosure");
assert.equal(outerDisclosure.open, true, "same-hash document link did not reopen an outer disclosure ancestor");
assert.equal(scrollCount, 2, "same-hash document link did not restore the revealed target position");
assert.equal(focusCount, 0, "same-hash document link hijacked focus");

windowMock.location.hash = "#echo-status-document";
windowMock.location.href = "https://pattern-map.test/sources/index.html#echo-status-document";
assert.equal(eventListeners.get("hashchange")?.length, 1, "hashchange reveal listener is missing or duplicated");
eventListeners.get("hashchange")[0]();
assert.equal(secondDisclosure.open, true, "hashchange did not open the target disclosure");
assert.equal(scrollCount, 3, "hashchange target was not scrolled into view after reveal");
assert.equal(focusCount, 0, "hashchange reveal hijacked focus");

windowMock.location.hash = "#%E0%A4%A";
assert.doesNotThrow(() => eventListeners.get("hashchange")[0](), "malformed hash did not fail safely");

console.log("PASS exact source destinations, stable document targets, owner-package path honesty, and focus-neutral disclosure reveal behavior");

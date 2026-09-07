import assert from "node:assert/strict";
import { access, readFile } from "node:fs/promises";
import test from "node:test";

const projectRoot = new URL("../", import.meta.url);

async function render(path = "/") {
  const workerUrl = new URL("../dist/server/index.js", import.meta.url);
  workerUrl.searchParams.set("test", `${process.pid}-${Date.now()}`);
  const { default: worker } = await import(workerUrl.href);

  return worker.fetch(
    new Request(`http://localhost${path}`, { headers: { accept: "text/html" } }),
    { ASSETS: { fetch: async () => new Response("Not found", { status: 404 }) } },
    { waitUntil() {}, passThroughOnException() {} },
  );
}

test("server-renders the v15.2 reader-first root with three honest stop points", async () => {
  const response = await render();
  assert.equal(response.status, 200);
  assert.match(response.headers.get("content-type") ?? "", /^text\/html\b/i);

  const html = await response.text();
  assert.match(html, /<title>Pattern Recognition: The Discrimination Layer<\/title>/i);
  assert.match(html, /name="robots" content="noindex, nofollow"/i);
  assert.equal((html.match(/<h1\b/gi) ?? []).length, 1);
  assert.match(html, /application-name" content="Pattern Recognition v15\.2"/);
  assert.match(html, /No model selected · no study run · no empirical result · not published/);
  assert.match(html, /discrimination means technical differentiation among information and possible actions—not social classification or discriminatory treatment/i);

  for (const id of ["stop-60-90", "stop-5", "stop-12-15"]) {
    assert.match(html, new RegExp(`id="${id}"`));
    assert.match(html, new RegExp(`href="#${id}"`));
    assert.match(html, new RegExp(`id="${id}"[^>]*tabindex="-1"`));
  }
  assert.match(html, /Stop here after 60–90 seconds\./);
  assert.match(html, /Stop here after about four minutes\./);
  assert.match(html, /Stop here after the roughly nine-minute full argument\./);

  assert.match(html, /Nine favorable reports arrive through nine different sites\./);
  assert.match(html, /Nine sources agree that the new tool is broadly validated\./);
  assert.match(html, /The summary has not merely shortened the evidence\./);
  assert.match(html, /It has changed its structure/);
  assert.match(html, /repetition alone did not create eight new roots/);
  assert.match(html, /If that relationship disappears from the evidence record, an AI system can inherit the inflated plurality/);
  assert.match(html, /observations<\/dt><dd>09<\/dd>/);
  assert.match(html, /known shared paths<\/dt><dd>01<\/dd>/);
  assert.match(html, /counted support paths<\/dt><dd>00<\/dd>/);
  assert.match(html, /human next step<\/dt><dd>HOLD<\/dd>/);
  assert.match(html, /That is a hold, not a rejection or a truth verdict\./);

  assert.match(html, /Shared path/);
  assert.match(html, /Separate only in this test/);
  assert.match(html, /Unresolved/);
  assert.match(html, /A review control must change something downstream\./);
  assert.match(html, /The program commits in advance to keeping an unhelpful result\./);
  assert.match(html, /no model selected · no study run · no result/i);
  assert.match(html, /Historical reference · v13 · not the v15\.2 system map/);
  assert.match(html, /src="\/images\/v13-six-families-origin-map\.png"/);

  assert.doesNotMatch(html, /id="deep-receipt"/);
  assert.doesNotMatch(html, /id="map"/);
  assert.doesNotMatch(html, /id="lab"/);
  assert.doesNotMatch(html, /id="sources"/);
  assert.doesNotMatch(html, /src="\/images\/context-before-answer\.jpg"/);
  assert.doesNotMatch(html, /property="og:/);
  assert.doesNotMatch(html, /name="twitter:/);

  const firstRoute = html.slice(html.indexOf('id="stop-60-90"'), html.indexOf('aria-label="End of the 60–90-second route"'));
  assert.doesNotMatch(firstRoute, /\bF[012]\b|\bT1\b|N=300|tokenizer|provenance audit/i);
});

test("renders genuine explore, lab, and sources routes with the right depth and status", async () => {
  const routes = {
    "/explore": [
      /id="deep-receipt"/,
      /The technical record behind 09 \/ 01 \/ 00 \/ HOLD/,
      /Typed relation ledger for the nine illustrative observations/,
      /Shared path · DPND/,
      /Separate only in this test · INDP/,
      /Unresolved · UNKN/,
      /B1/,
      /C1/,
      /id="map"/,
      /id="mechanisms"/,
      /id="connections"/,
      /id="example"/,
      /id="challenges"/,
      /id="cases"/,
      /Eleven responsibilities, each open to inspection\./,
      /Inspect the five-field Signal Foundry case/,
      /Two observations, one known supporting-origin path/,
      /HOLD \/ DEFER/,
      /CONTEXT_DISPOSITION/,
      /design proposal—not an implemented capability or production fact/,
    ],
    "/lab": [
      /id="lab"/,
      /No AI model chosen · test not run · no result/,
      /Written plan \+ local test code/,
      /Proposed study title · model not yet selected/,
      /Supplied Origin-Relation Cues in One Model to Be Selected/,
      /Ordinary version · F0/,
      /Rule-only version · F1/,
      /Added-cue version · F2/,
      /300 planned fictional cases/,
      /provisional until the paired design and safety checks are complete/,
      /FC_cons/,
      /A=300/,
      /M=75/,
      /VOR/,
      /ordered membership and hash come from the restricted pre-run manifest/,
      /never filtered by validity or post-run output/,
      /one-sided 95% lower bound is greater than <strong>-0\.05<\/strong>/,
      /interval method, coverage simulation, and paired-invalid operating-characteristic receipt all remain open/,
      /DPND/,
      /INDP/,
      /UNKN<\/code> is never silently counted as independent/,
      /COHERENT_PROTOCOL_NOT_EXECUTION_READY/,
      /A listed safeguard is not a passed safeguard/,
      /even complete gate receipts authorize nothing by themselves/,
      /In plain English: we decide in advance to report what actually happens/,
      /Direct-code or field-only shortcut/,
      /Surface or semantic-audit failure/,
      /Unstable:/,
      /Noise-fragile or non-transferable/,
    ],
    "/sources": [
      /id="sources"/,
      /Selected precedents and status notes/,
      /Prior art narrows the claim\./,
      /Compact glossary/,
      /Technical terms, without the gatekeeping\./,
    ],
  };

  for (const [path, patterns] of Object.entries(routes)) {
    const response = await render(path);
    assert.equal(response.status, 200, path);
    const html = await response.text();
    assert.equal((html.match(/<h1\b/gi) ?? []).length, 1, path);
    for (const pattern of patterns) assert.match(html, pattern, path);
  }
});

test("keeps navigation, fragment targets, popover targets, and identifiers resolvable", async () => {
  const expectedCurrent = {
    "/": "/",
    "/explore": "/explore#deep-receipt",
    "/lab": "/lab#lab",
    "/sources": "/sources#sources",
  };
  for (const path of ["/", "/explore", "/lab", "/sources"]) {
    const html = await (await render(path)).text();
    const ids = [...html.matchAll(/\bid="([^"]+)"/g)].map((match) => match[1]);
    const fragments = [...html.matchAll(/\bhref="#([^"]+)"/g)].map((match) => match[1]);
    const popoverTargets = [...html.matchAll(/\bpopoverTarget="([^"]+)"/gi)].map((match) => match[1]);
    const skipTarget = html.match(/class="skip-link" href="#([^"]+)"/)?.[1];

    assert.equal(new Set(ids).size, ids.length, `duplicate HTML id on ${path}`);
    for (const fragment of fragments) assert.ok(ids.includes(fragment), `missing target for #${fragment} on ${path}`);
    for (const target of popoverTargets) assert.ok(ids.includes(target), `missing popover target #${target} on ${path}`);
    assert.ok(skipTarget, `missing skip target on ${path}`);
    assert.match(html, new RegExp(`id="${skipTarget}"[^>]*tabindex="-1"`), `skip target is not focusable on ${path}`);
    assert.match(html, /aria-label="Primary reading navigation"/);
    assert.match(html, new RegExp(`href="${expectedCurrent[path]}" aria-current="location"`));
    if (path !== "/") assert.doesNotMatch(html, /href="\/" aria-current="location"/);
  }
});

test("provides a keyboard-returning close control for long component records", async () => {
  const source = await readFile(new URL("../app/CollapseControl.tsx", import.meta.url), "utf8");
  assert.match(source, /details\.open = false/);
  assert.match(source, /details\.querySelector\("summary"\)\?\.focus\(\)/);
  assert.match(source, /Close \{componentId\} and return to its summary/);
});

test("uses native nonmodal, no-JS term explanations with explicit focus return", async () => {
  const source = await readFile(new URL("../app/Term.tsx", import.meta.url), "utf8");
  assert.match(source, /type="button"/);
  assert.match(source, /popoverTarget=\{popoverId\}/);
  assert.match(source, /popoverTargetAction="toggle"/);
  assert.match(source, /popover="auto"/);
  assert.match(source, /role="region"/);
  assert.match(source, /aria-labelledby=\{headingId\}/);
  assert.match(source, /aria-describedby=\{descriptionId\}/);
  assert.match(source, /popoverTargetAction="hide"/);
  assert.match(source, /requestAnimationFrame\(\(\) => triggerRef\.current\?\.focus\(\)\)/);
  assert.match(source, /addEventListener\("beforetoggle", beforeToggle\)/);
  assert.match(source, /addEventListener\("toggle", afterToggle\)/);
  assert.match(source, /panel\.contains\(document\.activeElement\)/);
  assert.match(source, /role="heading" aria-level=\{3\}/);
  assert.match(source, /What it does not mean:/);
  assert.doesNotMatch(source, /useState|role="dialog"|aria-modal|visual ===/);

  const labHtml = await (await render("/lab")).text();
  assert.equal((labHtml.match(/aria-label="Explain N=300"/g) ?? []).length, 1);
  assert.match(labHtml, /popover="auto"/);
  assert.match(labHtml, /id="term-lab-sample-size-note"/);
  assert.match(labHtml, /N is simply the number of bundles/);
});

test("removes the disposable starter preview", async () => {
  const packageJson = await readFile(new URL("../package.json", import.meta.url), "utf8");
  assert.doesNotMatch(packageJson, /react-loading-skeleton/);
  await assert.rejects(access(new URL("app/_sites-preview/SkeletonPreview.tsx", projectRoot)));
});

test("keeps typography, focus, responsive figures, print definitions, and metadata safe", async () => {
  const css = await readFile(new URL("../app/globals.css", import.meta.url), "utf8");
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const layout = await readFile(new URL("../app/layout.tsx", import.meta.url), "utf8");

  assert.match(css, /body\s*\{[^}]*font:\s*17px\/1\.58 var\(--serif\)/s);
  assert.match(css, /:focus-visible[^}]*outline:\s*3px solid #fff[^}]*box-shadow:\s*0 0 0 7px var\(--ink\)/s);
  assert.match(css, /\.term-popover\s*\{[^}]*position:\s*fixed;[^}]*max-height:/s);
  assert.match(css, /\.term-popover::backdrop\s*\{[^}]*background:\s*transparent;/s);
  assert.match(css, /@supports \(position-anchor: --term-anchor\)/);
  assert.match(css, /position-try-fallbacks:\s*flip-block, flip-inline/);
  assert.match(css, /@supports not selector\(:popover-open\)/);
  assert.match(css, /section\[tabindex="-1"\]:focus/);
  assert.match(css, /@media \(max-width: 780px\)[\s\S]*\.term-popover\s*\{[\s\S]*env\(safe-area-inset-bottom\)/);
  assert.match(css, /@media \(forced-colors: active\)/);
  assert.match(css, /@media print[\s\S]*\[popover\]\.term-popover\s*\{[\s\S]*display:\s*block !important;/);
  assert.match(css, /@media print[\s\S]*\.condition-table-wrap, \.state-table\s*\{\s*overflow:\s*visible;/);
  assert.match(css, /@media print[\s\S]*\.condition-table-wrap table, \.state-table table\s*\{[^}]*min-width:\s*0;[^}]*table-layout:\s*fixed;/);
  assert.match(css, /\.origin-observations\s*\{[^}]*grid-template-columns:\s*repeat\(9,/s);
  assert.doesNotMatch(page, /loading="lazy"/);
  assert.doesNotMatch(layout, /\bopenGraph\s*:/);
  assert.doesNotMatch(layout, /\btwitter\s*:/);
});

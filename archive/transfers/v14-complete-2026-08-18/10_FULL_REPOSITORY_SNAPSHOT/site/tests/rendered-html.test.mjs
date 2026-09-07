import assert from "node:assert/strict";
import { access, readFile } from "node:fs/promises";
import test from "node:test";

const projectRoot = new URL("../", import.meta.url);

async function render() {
  const workerUrl = new URL("../dist/server/index.js", import.meta.url);
  workerUrl.searchParams.set("test", `${process.pid}-${Date.now()}`);
  const { default: worker } = await import(workerUrl.href);

  return worker.fetch(
    new Request("http://localhost/", { headers: { accept: "text/html" } }),
    { ASSETS: { fetch: async () => new Response("Not found", { status: 404 }) } },
    { waitUntil() {}, passThroughOnException() {} },
  );
}

test("server-renders the complete v14 reading experience", async () => {
  const response = await render();
  assert.equal(response.status, 200);
  assert.match(response.headers.get("content-type") ?? "", /^text\/html\b/i);

  const html = await response.text();
  assert.match(html, /<title>Pattern Recognition: The Discrimination Layer<\/title>/i);
  assert.match(html, /name="robots" content="noindex, nofollow"/i);
  assert.equal((html.match(/<h1\b/gi) ?? []).length, 1);
  assert.match(html, /The visible answer is often where hidden decisions surface\./);
  assert.match(html, /Underweighted is a starting condition, not a conclusion\./);
  assert.match(html, /discrimination means technical differentiation among information and possible actions/i);
  assert.match(html, /not empirically validated/i);
  assert.match(html, /Relationship diagram/);
  assert.match(html, /One fast loop\. One slower loop\./);
  assert.match(html, /Three implementation paths/);
  assert.match(html, /Twelve boundaries the presentation cannot smooth away\./);
  assert.match(html, /Repeated mentions remain separate observations, but they do not establish distinct-origin support under this packet’s relation rule/i);
  assert.equal((html.match(/<details[^>]*class="component\b/gi) ?? []).length, 11);
  assert.match(html, /Nine observations can still represent one origin\./);
  assert.match(html, /Typed relation ledger for the nine illustrative observations/);
  assert.match(html, /Supporting origins counted under the stated relation rule/);
  assert.match(html, /UNKNOWN stays unknown\./);
  assert.match(html, /HOLD · VERIFY ANOTHER ORIGIN RELATION/);
  assert.match(html, /id="origin-receipt-claim-title"/);
  assert.match(html, /O01–O09 · Origin A · DEPENDENT · zero supporting origins counted/);
  assert.equal((html.match(/>O0[1-9]<\/th>/g) ?? []).length, 9);
  assert.match(html, /Historical reference · v13 · not the v14 system map/);
  assert.match(html, /Collect widely, including weak signals and non-traditional sources/);
  assert.match(html, /Continuously update weights and baselines through the learning loop/);
  assert.match(html, /src="\/images\/nine-mentions-one-origin\.jpg"/);
  assert.match(html, /Many mentions can preserve one origin\./);
  assert.match(html, /src="\/images\/v13-six-families-origin-map\.png"/);
  assert.doesNotMatch(html, /src="\/images\/context-before-answer\.jpg"/);
  assert.match(html, /property="og:image" content="http:\/\/localhost:3000\/og\.png"/);
  assert.match(html, /name="twitter:card" content="summary_large_image"/);
  assert.match(html, /oracle origin-relation metadata/i);
  for (let index = 1; index <= 11; index += 1) {
    assert.match(html, new RegExp(`C${String(index).padStart(2, "0")}`));
  }
  assert.doesNotMatch(html, /react-loading-skeleton|Your site is taking shape/i);
});

test("keeps same-page navigation complete and identifiers unique", async () => {
  const html = await (await render()).text();
  const ids = [...html.matchAll(/\bid="([^"]+)"/g)].map((match) => match[1]);
  const fragments = [...html.matchAll(/\bhref="#([^"]+)"/g)].map((match) => match[1]);

  assert.equal(new Set(ids).size, ids.length, "duplicate HTML id");
  for (const fragment of fragments) {
    assert.ok(ids.includes(fragment), `missing target for #${fragment}`);
  }
  assert.match(html, /aria-label="Primary reading navigation"/);
  assert.match(html, />04 Connections</);
  assert.match(html, /Skip to the five-minute overview/);
  assert.match(html, /On narrow screens, scroll this comparison horizontally\./);
  assert.match(html, /Prior art \+ synthesis/);
  assert.match(html, /Design \+ empirical hypothesis/);
  assert.match(html, /class="component-exits"/);
  assert.doesNotMatch(html, /status-evidence">Prior art<\/span>/);
});

test("provides a keyboard-returning close control for long component records", async () => {
  const source = await readFile(new URL("../app/CollapseControl.tsx", import.meta.url), "utf8");
  assert.match(source, /details\.open = false/);
  assert.match(source, /details\.querySelector\("summary"\)\?\.focus\(\)/);
  assert.match(source, /Close \{componentId\} and return to its summary/);
});

test("removes the disposable starter preview", async () => {
  const packageJson = await readFile(new URL("../package.json", import.meta.url), "utf8");
  assert.doesNotMatch(packageJson, /react-loading-skeleton/);
  await assert.rejects(access(new URL("app/_sites-preview/SkeletonPreview.tsx", projectRoot)));
});

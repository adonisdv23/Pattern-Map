#!/usr/bin/env node

/** Build self-contained, offline-readable snapshots of every v15.2 route. */

import { mkdir, readFile, writeFile } from "node:fs/promises";
import { extname, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const site = resolve(root, "site");
const output = resolve(root, "output/v15_2/standalone");
const routes = [
  ["/", "index.html"],
  ["/explore", "explore.html"],
  ["/lab", "lab.html"],
  ["/sources", "sources.html"],
];

const mimeByExtension = {
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".png": "image/png",
  ".svg": "image/svg+xml",
  ".webp": "image/webp",
};

function routeHref(href) {
  if (href === "/") return "index.html";
  if (href.startsWith("/#")) return `index.html${href.slice(1)}`;
  for (const [route, filename] of routes.slice(1)) {
    if (href === route) return filename;
    if (href.startsWith(`${route}#`)) return `${filename}${href.slice(route.length)}`;
  }
  return href;
}

async function imageDataUrl(source) {
  const extension = extname(source).toLowerCase();
  const mime = mimeByExtension[extension];
  if (!mime) throw new Error(`Unsupported embedded image type: ${source}`);
  const bytes = await readFile(resolve(site, "public", source.replace(/^\//, "")));
  return `data:${mime};base64,${bytes.toString("base64")}`;
}

async function render(route) {
  const workerUrl = pathToFileURL(resolve(site, "dist/server/index.js"));
  workerUrl.searchParams.set("standalone", `${route}-${Date.now()}-${Math.random()}`);
  const { default: worker } = await import(workerUrl.href);
  const response = await worker.fetch(
    new Request(`http://standalone.local${route}`, { headers: { accept: "text/html" } }),
    { ASSETS: { fetch: async () => new Response("Not found", { status: 404 }) } },
    { waitUntil() {}, passThroughOnException() {} },
  );
  if (!response.ok) throw new Error(`Route ${route} returned ${response.status}`);
  return response.text();
}

function stripRuntime(html) {
  return html
    .replace(/<script\b[^>]*>[\s\S]*?<\/script>/gi, "")
    .replace(/<link\b[^>]*(?:modulepreload|stylesheet|data-rsc-css-href|as="image")[^>]*>/gi, "")
    .replace(/\sdata-rsc-css-href="[^"]*"/gi, "");
}

async function makeStandalone(route) {
  let html = stripRuntime(await render(route));
  const css = (await readFile(resolve(site, "app/globals.css"), "utf8"))
    .replace(/^@import\s+"tailwindcss";\s*/m, "")
    .replace(/<\/style/gi, "<\\/style");

  const imageSources = [...new Set([...html.matchAll(/\bsrc="(\/images\/[^"]+)"/g)].map((match) => match[1]))];
  for (const source of imageSources) {
    html = html.replaceAll(`src="${source}"`, `src="${await imageDataUrl(source)}"`);
    html = html.replaceAll(`href="${source}"`, `href="${await imageDataUrl(source)}"`);
  }

  html = html.replace(/\bhref="(\/(?:explore|lab|sources)?(?:#[^"]*)?)"/g, (_, href) => `href="${routeHref(href)}"`);
  html = html.replace(
    "</head>",
    `<style>${css}</style><meta name="generator" content="Pattern Map v15.2 standalone exporter"></head>`,
  );
  html = html.replace(
    "</body>",
    `<script>
(() => {
  for (const panel of document.querySelectorAll('[popover]')) {
    let restore = false;
    panel.addEventListener('beforetoggle', event => {
      if (event.newState === 'closed') restore = panel.contains(document.activeElement);
    });
    panel.addEventListener('toggle', event => {
      if (event.newState !== 'closed' || !restore) return;
      restore = false;
      const trigger = document.querySelector('[popovertarget="' + CSS.escape(panel.id) + '"]');
      requestAnimationFrame(() => trigger?.focus());
    });
  }
})();
</script></body>`,
  );
  return `<!-- Pattern Recognition v15.2 · standalone owner-review route · ${route} · no study run · no empirical result -->\n${html}\n`;
}

async function verify(filename, html) {
  const failures = [];
  if (!/^<!DOCTYPE html>/im.test(html)) failures.push("missing doctype");
  if ((html.match(/<h1\b/gi) ?? []).length !== 1) failures.push("expected exactly one h1");
  if (/_next\/|data-rsc-|<script\b[^>]*\bsrc=|<link\b[^>]*stylesheet/i.test(html)) failures.push("runtime asset reference remains");
  if (/\bsrc="\/images\//i.test(html)) failures.push("local image path remains");
  if (!/No (?:AI )?model (?:selected|chosen).*no study run.*no (?:empirical )?result/is.test(html)) failures.push("no-results boundary missing");
  if (filename === "index.html" && !/data:image\/png;base64,/i.test(html)) failures.push("historical v13 image was not embedded");
  if (filename === "explore.html" && !/data:image\/jpeg;base64,/i.test(html)) failures.push("worked-example image was not embedded");
  if (failures.length) throw new Error(`${filename}: ${failures.join("; ")}`);
}

await mkdir(output, { recursive: true });
const manifest = [];
for (const [route, filename] of routes) {
  const html = await makeStandalone(route);
  await verify(filename, html);
  await writeFile(resolve(output, filename), html, "utf8");
  manifest.push({ route, filename, bytes: Buffer.byteLength(html) });
}
await writeFile(
  resolve(output, "STANDALONE_ROUTES.json"),
  `${JSON.stringify({ version: "v15.2", status: "LOCAL_OWNER_REVIEW_NO_RESULTS", routes: manifest }, null, 2)}\n`,
  "utf8",
);
for (const item of manifest) console.log(`${item.filename}\t${item.bytes}`);

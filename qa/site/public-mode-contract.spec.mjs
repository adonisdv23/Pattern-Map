import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const QA_DIR = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(QA_DIR, "../..");
const SITE = path.join(ROOT, "site");
const read = (relativePath) => fs.readFileSync(path.join(ROOT, relativePath), "utf8");

const reviewManifest = JSON.parse(read("site/dist/build-manifest.json"));
const publicManifest = JSON.parse(read("site/public-dist/build-manifest.json"));
for (const field of ["route_ids", "canonical_source_sha256", "claim_anchors", "family_tuple"]) {
  assert.deepEqual(publicManifest[field], reviewManifest[field], `public/review ${field} drifted`);
}
assert.equal(publicManifest.release_build, false, "ordinary public preview must remain a non-release build");

const config = JSON.parse(read("site/publication.config.json"));
assert.equal(config.status, "LOCAL_PREVIEW_UNSET");
for (const field of ["author_name", "author_handle", "canonical_url", "social_image_url"]) {
  assert.equal(config[field], null, `public identity field should remain unset: ${field}`);
}

const releaseAttempt = spawnSync(process.execPath, ["build.mjs", "--mode=public", "--release"], {
  cwd: SITE,
  encoding: "utf8",
});
assert.notEqual(releaseAttempt.status, 0, "release build unexpectedly succeeded with unset identity and URL fields");
assert.match(`${releaseAttempt.stdout}\n${releaseAttempt.stderr}`, /Public release is gated/);
assert.match(read("site/build.mjs"), /releaseMetadataEnabled = releaseBuildRequested && publicationReleaseReady\(\)/);

const publicRead = read("site/public-dist/read/index.html");
const shortOpening = "An AI answer can sound polished yet be generic because weakness can begin before writing.";
assert.ok(publicRead.indexOf(shortOpening) > 0, "existing short-version prose is missing from public Read");
assert.equal(publicRead.includes('class="route-brief"'), false);
assert.equal(publicRead.includes('class="reading-progress-wrap"'), false);
assert.equal(publicRead.includes('class="pull-quote"'), false);

const publicApply = read("site/public-dist/apply/index.html");
for (const dependent of ["consequence", "uncertainty", "budget"]) {
  assert.match(publicApply, new RegExp(`data-stage0-dependent="${dependent}"[^>]*disabled`));
}
assert.match(publicApply, /are not applicable while Stage 0 remains supplied-material only/);
assert.match(publicApply, /<details class="static-route-equivalent" open data-progressive-static-guide><summary>/);

const siteScript = read("site/src/site.js");
assert.match(siteScript, /document\.querySelectorAll\("\[data-progressive-static-guide\]"\)/);
assert.match(siteScript, /guide\.open = false/);
assert.match(siteScript, /syncStageZeroApplicability/);
assert.match(siteScript, /fieldset\.disabled = ordinary/);
assert.match(siteScript, /fieldset\.dataset\.applicability = ordinary \? "not-applicable" : "active"/);

const publicHome = read("site/public-dist/index.html");
const reveal = publicHome.match(/<figure class="decision-reveal"[\s\S]*?<\/figure>/)?.[0] ?? "";
assert.ok(reveal, "public teaching reveal is missing");
for (const stage of ["DEFAULT PATH", "WIDEN ONCE", "COMPARE", "EXPECTED ABSENCE", "BECAME VISIBLE", "REMAINS UNKNOWN", "HUMAN DECISION"]) {
  assert.ok(reveal.includes(stage), `teaching reveal stage missing: ${stage}`);
}
assert.doesNotMatch(reveal, /https?:\/\/|<script\b|<form\b|source score|observed result|automated action/i);
assert.match(reveal, /Text equivalent:/);

const css = read("site/src/site.css");
assert.match(css, /@media print[\s\S]*?\.decision-reveal-boundary:not\(\[open\]\) > \.decision-reveal-ledger \{ display: grid !important;/);

console.log("PASS public mode shared-source, release gate, prose-first, Stage 0, and teaching-reveal contracts");

import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import {
  PUBLICATION_CONFIG_SCHEMA,
  PUBLICATION_RELEASE_STATUS,
  assertPublicationReleaseConfig,
  publicationMetadataEnabled,
  publicationReleaseReady,
} from "../../site/src/publication-config.mjs";

const QA_DIR = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(QA_DIR, "../..");
const SITE = path.join(ROOT, "site");
const read = (relativePath) => fs.readFileSync(path.join(ROOT, relativePath), "utf8");

const assertNoSkippedHeadingLevels = (html, label) => {
  const main = html.match(/<main id="main"[^>]*>([\s\S]*?)<\/main>/i)?.[1] ?? "";
  const levels = [...main.matchAll(/<h([1-6])\b/gi)].map((match) => Number(match[1]));
  assert.ok(levels.length > 0, `${label} has no headings in main`);
  assert.equal(levels[0], 1, `${label} does not begin with a level-one heading`);
  for (let index = 1; index < levels.length; index += 1) {
    assert.ok(
      levels[index] <= levels[index - 1] + 1,
      `${label} skips from h${levels[index - 1]} to h${levels[index]}`,
    );
  }
};

const validReleaseConfig = {
  schema_version: PUBLICATION_CONFIG_SCHEMA,
  status: PUBLICATION_RELEASE_STATUS,
  author_name: "Publication Gate Test",
  author_handle: null,
  canonical_url: "https://example.test/pattern-map",
  social_image_url: "https://example.test/pattern-map/social-card.png",
  release_boundary: "Test-only configuration in a disposable site copy.",
};

const adversarialReleaseConfigs = [
  ["empty canonical host", { ...validReleaseConfig, canonical_url: "https://" }],
  ["malformed canonical host", { ...validReleaseConfig, canonical_url: "https://." }],
  ["non-HTTPS canonical URL", { ...validReleaseConfig, canonical_url: "http://example.test/pattern-map" }],
  ["canonical URL with whitespace", { ...validReleaseConfig, canonical_url: " https://example.test/pattern-map" }],
  ["canonical URL with user information", { ...validReleaseConfig, canonical_url: "https://owner@example.test/pattern-map" }],
  ["empty social-image host", { ...validReleaseConfig, social_image_url: "https://" }],
  ["malformed social-image URL", { ...validReleaseConfig, social_image_url: "https://example .test/social-card.png" }],
];

for (const [label, candidate] of adversarialReleaseConfigs) {
  assert.equal(publicationReleaseReady(candidate), false, `${label} was treated as release-ready`);
  assert.throws(() => assertPublicationReleaseConfig(candidate), /Public release is gated/, `${label} did not fail closed`);
  assert.equal(publicationMetadataEnabled(candidate, true), false, `${label} enabled release metadata`);
}
assert.equal(publicationReleaseReady(validReleaseConfig), true, "valid absolute HTTPS release configuration was rejected");
assert.doesNotThrow(() => assertPublicationReleaseConfig(validReleaseConfig));
assert.equal(publicationMetadataEnabled(validReleaseConfig, false), false, "release metadata was enabled without --release");
assert.equal(publicationMetadataEnabled(validReleaseConfig, true), true, "valid release configuration did not enable metadata with --release");

const disposableRoot = fs.mkdtempSync(path.join(os.tmpdir(), "pattern-map-publication-gate-"));
try {
  for (const directory of ["archive", "assets", "cases", "docs", "framework", "manuscript", "research"]) {
    fs.symlinkSync(path.join(ROOT, directory), path.join(disposableRoot, directory), "dir");
  }
  const disposableSite = path.join(disposableRoot, "site");
  fs.cpSync(SITE, disposableSite, { recursive: true });
  const disposableConfigPath = path.join(disposableSite, "publication.config.json");
  const runDisposableBuild = (...arguments_) => spawnSync(process.execPath, ["build.mjs", ...arguments_], {
    cwd: disposableSite,
    encoding: "utf8",
  });

  for (const [label, candidate] of adversarialReleaseConfigs) {
    fs.writeFileSync(disposableConfigPath, `${JSON.stringify(candidate, null, 2)}\n`);
    const attempt = runDisposableBuild("--mode=public", "--release");
    assert.notEqual(attempt.status, 0, `${label} unexpectedly passed the real release build`);
    assert.match(`${attempt.stdout}\n${attempt.stderr}`, /Public release is gated/, `${label} failed without the release-gate diagnosis`);
  }

  fs.writeFileSync(disposableConfigPath, `${JSON.stringify(validReleaseConfig, null, 2)}\n`);
  const preview = runDisposableBuild("--mode=public");
  assert.equal(preview.status, 0, `valid public preview failed:\n${preview.stdout}\n${preview.stderr}`);
  const previewHtml = fs.readFileSync(path.join(disposableSite, "public-dist", "index.html"), "utf8");
  const previewManifest = JSON.parse(fs.readFileSync(path.join(disposableSite, "public-dist", "build-manifest.json"), "utf8"));
  assert.match(previewHtml, /<meta name="robots" content="noindex,nofollow">/);
  assert.doesNotMatch(previewHtml, /rel="canonical"|property="og:url"|name="author"/);
  assert.equal(previewManifest.release_build, false, "valid config enabled release state without --release");

  const release = runDisposableBuild("--mode=public", "--release");
  assert.equal(release.status, 0, `valid release build failed:\n${release.stdout}\n${release.stderr}`);
  const releaseHtml = fs.readFileSync(path.join(disposableSite, "public-dist", "index.html"), "utf8");
  const releaseManifest = JSON.parse(fs.readFileSync(path.join(disposableSite, "public-dist", "build-manifest.json"), "utf8"));
  assert.match(releaseHtml, /<meta name="robots" content="index,follow">/);
  assert.match(releaseHtml, /<link rel="canonical" href="https:\/\/example\.test\/pattern-map\/">/);
  assert.match(releaseHtml, /<meta property="og:image" content="https:\/\/example\.test\/pattern-map\/social-card\.png">/);
  assert.match(releaseHtml, /<meta name="author" content="Publication Gate Test">/);
  assert.equal(releaseManifest.release_build, true, "--release did not record the valid release build");
} finally {
  fs.rmSync(disposableRoot, { recursive: true, force: true });
}

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
assert.match(read("site/build.mjs"), /releaseMetadataEnabled = publicationMetadataEnabled\(publicationConfig, releaseBuildRequested\)/);

const publicRead = read("site/public-dist/read/index.html");
const shortOpening = "An AI answer can sound polished yet be generic because weakness can begin before writing.";
assert.ok(publicRead.indexOf(shortOpening) > 0, "existing short-version prose is missing from public Read");
assert.equal(publicRead.includes('class="route-brief"'), false);
assert.equal(publicRead.includes('class="reading-progress-wrap"'), false);
assert.equal(publicRead.includes('class="pull-quote"'), false);
for (const route of ["index.html", "read/index.html", "map/index.html", "apply/index.html", "guided/index.html", "examples/index.html", "boundaries/index.html", "sources/index.html", "research/index.html", "history/index.html"]) {
  assertNoSkippedHeadingLevels(read(`site/public-dist/${route}`), `public route ${route}`);
}
assertNoSkippedHeadingLevels(read("site/exports/standalone/pattern-map-v16-public.html"), "public standalone");
assert.match(publicRead, /<h2 id="short-pattern-recognition-the-discrimination-layer">Pattern Recognition: The Discrimination Layer<\/h2>/);

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
assert.doesNotMatch(reveal, /normal release packet|usually contains/i);
assert.match(reveal, /this illustrative team expected from a release packet after four previous releases/i);

const css = read("site/src/site.css");
assert.match(css, /@media print[\s\S]*?\.decision-reveal-boundary:not\(\[open\]\) > \.decision-reveal-ledger \{ display: grid !important;/);

console.log("PASS public mode shared-source, release gate, prose-first, Stage 0, and teaching-reveal contracts");

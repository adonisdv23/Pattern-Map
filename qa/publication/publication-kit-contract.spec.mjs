import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const QA_DIR = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(QA_DIR, "../..");
const read = (relativePath) => fs.readFileSync(path.join(ROOT, relativePath), "utf8");
const publicationFiles = [
  "publication/README.md",
  "publication/MENTOR_REVIEW_SEQUENCE_V16.md",
  "publication/X_COPY_VARIANTS_V16.md",
  "publication/RELEASE_DECISION_CHECKLIST_V16.md",
];

for (const relativePath of publicationFiles) {
  assert.ok(fs.existsSync(path.join(ROOT, relativePath)), `missing publication artifact: ${relativePath}`);
}

const readme = read("publication/README.md");
const mentor = read("publication/MENTOR_REVIEW_SEQUENCE_V16.md");
const xCopy = read("publication/X_COPY_VARIANTS_V16.md");
const checklist = read("publication/RELEASE_DECISION_CHECKLIST_V16.md");
const config = JSON.parse(read("site/publication.config.json"));
const imageLedger = read("assets/IMAGE_USE_LEDGER.md");

assert.match(readme, /d05aca58910b4463e5afb69b10558b662a446278/);
assert.match(readme, /DO NOT POST, SEND, DEPLOY, OR\s+PUBLISH/);
for (const token of ["UNRESOLVED", "UNSET", "NOT GRANTED", "noindex,nofollow", "separate unrun project"]) {
  assert.match(readme, new RegExp(token.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")), `README lost fail-closed token: ${token}`);
}

for (const phrase of [
  "NO MENTOR CONTACT HAS OCCURRED",
  "The sequence",
  "Response sheet",
  "Stop and safety conditions",
  "What this sequence cannot establish",
  "Apply is planning-only",
]) {
  assert.match(mentor, new RegExp(phrase.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")), `mentor sequence lost ${phrase}`);
}

const variantExpectedLengths = { A: 278, B: 269, C: 273 };
const lines = xCopy.split("\n");
for (const [variant, expectedLength] of Object.entries(variantExpectedLengths)) {
  const start = lines.findIndex((line) => line.startsWith(`## Variant ${variant}`));
  assert.ok(start >= 0, `missing X variant ${variant}`);
  const quote = lines.slice(start, start + 16).find((line) => line.startsWith("> "));
  assert.ok(quote, `X variant ${variant} has no copy line`);
  assert.equal(quote.slice(2).length, expectedLength, `X variant ${variant} local character count drifted`);
}
for (const [post, expectedLength] of [["1/4", 193], ["2/4", 237], ["3/4", 217], ["4/4", 168]]) {
  const start = lines.findIndex((line) => line === `**${post}**`);
  assert.ok(start >= 0, `missing X thread post ${post}`);
  const quote = lines.slice(start, start + 8).find((line) => line.startsWith("> "));
  assert.ok(quote, `X thread post ${post} has no copy line`);
  assert.equal(quote.slice(2).length, expectedLength, `X thread post ${post} local character count drifted`);
}
assert.match(xCopy, /DRAFT COPY ONLY — DO NOT POST/);
for (const token of ["UNRESOLVED", "UNSET", "NOT GRANTED", "explicitly unrun"]) {
  assert.match(xCopy, new RegExp(token.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")), `X rehearsal lost fail-closed token: ${token}`);
}
assert.doesNotMatch(xCopy, /https?:\/\//i, "X rehearsal invented a destination URL");
assert.doesNotMatch(xCopy, /@[A-Za-z0-9_]{2,}/, "X rehearsal invented an account handle");

for (const phrase of [
  "LOCAL FAIL-CLOSED CHECKLIST — RELEASE NOT AUTHORIZED",
  "Name the decision before touching release metadata",
  "Owner and content gates",
  "Human and accessibility gates",
  "Action and claim audit",
  "exact proposed artifact and channel",
  "HOLD / NOT AUTHORIZED",
]) {
  assert.match(checklist, new RegExp(phrase.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")), `release checklist lost ${phrase}`);
}
for (const token of ["UNRESOLVED", "UNSET", "NOT AUTHORIZED", "NOT GRANTED", "noindex,nofollow"]) {
  assert.match(checklist, new RegExp(token.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")), `release checklist lost fail-closed token: ${token}`);
}
assert.doesNotMatch(checklist, /GO\s+—\s+only after every required gate is checked[\s\S]*\[x\]/i, "release checklist prechecked GO");

for (const field of ["author_name", "author_handle", "canonical_url", "social_image_url", "social_image_alt"]) {
  assert.equal(config[field], null, `publication identity field was set during rehearsal: ${field}`);
}
assert.equal(config.status, "LOCAL_PREVIEW_UNSET", "local preview status changed during rehearsal");
assert.match(imageLedger, /Generated bitmap candidates \| None created/);
const candidateDirectory = path.join(ROOT, "assets/generated-candidates");
const candidateFiles = fs.existsSync(candidateDirectory)
  ? fs.readdirSync(candidateDirectory).filter((name) => name !== ".gitkeep")
  : [];
assert.deepEqual(candidateFiles, [], "a bitmap candidate was added without a written need");

const relativeLinks = [...`${readme}\n${mentor}`.matchAll(/\]\(([^)]+)\)/g)].map((match) => match[1]);
for (const link of relativeLinks) {
  if (/^(?:https?:|mailto:|tel:|#)/i.test(link)) continue;
  const target = link.split(/[?#]/, 1)[0];
  assert.ok(target, `empty publication link target: ${link}`);
  const resolved = path.resolve(ROOT, "publication", target);
  assert.ok(fs.existsSync(resolved), `publication link target is missing: ${link}`);
}

console.log("PASS unpublished publication kit, fail-closed fields, copy sizes, and source links");

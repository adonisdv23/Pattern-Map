import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const SITE_DIR = path.dirname(fileURLToPath(import.meta.url));
const DIST_DIR = path.join(SITE_DIR, "dist");
const EXPORT_PATH = path.join(SITE_DIR, "exports", "standalone", "pattern-map-v16.html");

const requiredRoutes = [
  "index.html",
  "read/index.html",
  "map/index.html",
  "apply/index.html",
  "examples/index.html",
  "boundaries/index.html",
  "sources/index.html",
  "research/index.html",
  "history/index.html",
];

const assert = (condition, message) => {
  if (!condition) throw new Error(message);
};

const read = (filePath) => fs.readFileSync(filePath, "utf8");

const localLinksIn = (html) => [...html.matchAll(/(?:href|src)="([^"]+)"/g)].map((match) => match[1]);

const checkLink = (fromFile, href) => {
  if (!href || href.startsWith("#") || /^(https?:|mailto:|tel:|data:|javascript:)/i.test(href)) return;
  const [withoutHash] = href.split("#");
  const [filePart] = withoutHash.split("?");
  if (!filePart) return;
  const target = path.resolve(path.dirname(fromFile), filePart);
  assert(target.startsWith(`${DIST_DIR}${path.sep}`), `${fromFile} escapes dist: ${href}`);
  assert(fs.existsSync(target), `${fromFile} points to missing local target: ${href}`);
};

const main = () => {
  for (const route of requiredRoutes) assert(fs.existsSync(path.join(DIST_DIR, route)), `missing built route: ${route}`);
  assert(fs.existsSync(EXPORT_PATH), "missing committed standalone export; run build first");
  const root = read(path.join(DIST_DIR, "index.html"));
  const map = read(path.join(DIST_DIR, "map/index.html"));
  const apply = read(path.join(DIST_DIR, "apply/index.html"));
  const examples = read(path.join(DIST_DIR, "examples/index.html"));
  const research = read(path.join(DIST_DIR, "research/index.html"));
  const history = read(path.join(DIST_DIR, "history/index.html"));
  const headline = "AI slop often begins before the model writes a word.";
  const standfirst = "A polished answer can still feel generic when the system follows the obvious search path";
  assert(root.includes(headline), "root headline missing");
  assert(root.includes(standfirst), "root standfirst missing");
  for (const door of ["Read the idea", "Explore the map", "Apply it"]) assert(root.indexOf(door) >= 0, `principal door missing: ${door}`);
  const doorEnd = root.indexOf("</nav>", root.indexOf('<nav class="door-grid"'));
  const echoIndex = root.indexOf("Echo");
  assert(doorEnd > 0 && (echoIndex < 0 || echoIndex > doorEnd), "Echo appears before principal doors");
  const familyOrder = ["F1", "F2", "F3", "F4", "F5", "F6"].map((id) => map.indexOf(`id="family-${id}"`));
  assert(familyOrder.every((position) => position >= 0), "one or more family cards missing");
  assert(familyOrder.every((position, index) => index === 0 || position > familyOrder[index - 1]), "family card order changed");
  for (const familyName of ["Peripheral signal", "Source weighing", "Velocity / motion", "Absence + memory", "Structured patterns", "Learning loop"]) assert(map.includes(familyName), `family name missing: ${familyName}`);
  for (const level of ["ordinary", "lightweight", "moderate", "advanced"]) assert(apply.toLowerCase().includes(level), `implementation level missing: ${level}`);
  for (const example of ["specialist signal", "explicit baseline", "independence: UNKNOWN"]) assert(examples.includes(example), `teaching pattern missing: ${example}`);
  assert(examples.includes("ILLUSTRATION ONLY / READ-ONLY / NOT VALIDATION"), "Signal Foundry status missing");
  assert(examples.includes("The Echo Problem</strong> is a separate project"), "late Echo boundary missing from examples");
  assert(research.includes("UNRUN") && research.includes("NO RESULTS") && research.includes("NO PROVIDER OR MODEL SELECTED"), "research no-results status missing");
  assert(research.includes("separate project — unrun — no results"), "Echo status missing from research route");
  assert(history.includes("Historical v13 origin — not the current v16 topology."), "historical label missing");
  assert(history.includes("current relationship view"), "current/historical distinction missing");
  const htmlFiles = requiredRoutes.map((route) => path.join(DIST_DIR, route));
  for (const filePath of htmlFiles) for (const href of localLinksIn(read(filePath))) checkLink(filePath, href);
  console.log(`PASS routes: ${requiredRoutes.length}`);
  console.log("PASS exact first-screen headline/standfirst and principal-door presence");
  console.log("PASS six-family order/names, implementation levels, teaching patterns");
  console.log("PASS Signal Foundry, Echo, and historical/current topology boundaries");
  console.log("PASS local route/assets link integrity");
  console.log("PASS standalone export exists");
};

main();

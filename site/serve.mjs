import http from "node:http";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const SITE_DIR = path.dirname(fileURLToPath(import.meta.url));
const DIST_DIR = path.join(SITE_DIR, "dist");
const PORT = Number(process.env.SITE_PORT || 4173);
const MIME_TYPES = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".svg": "image/svg+xml",
  ".json": "application/json; charset=utf-8",
};

const server = http.createServer((request, response) => {
  try {
    const requestUrl = new URL(request.url ?? "/", `http://${request.headers.host ?? "localhost"}`);
    let pathname = decodeURIComponent(requestUrl.pathname);
    if (pathname.endsWith("/")) pathname += "index.html";
    const candidate = path.resolve(DIST_DIR, `.${pathname}`);
    if (!candidate.startsWith(`${DIST_DIR}${path.sep}`)) {
      response.writeHead(400, { "content-type": "text/plain; charset=utf-8" });
      response.end("Bad request");
      return;
    }
    if (!fs.existsSync(candidate) || !fs.statSync(candidate).isFile()) {
      response.writeHead(404, { "content-type": "text/plain; charset=utf-8" });
      response.end("Not found");
      return;
    }
    const extension = path.extname(candidate).toLowerCase();
    response.writeHead(200, {
      "content-type": MIME_TYPES[extension] ?? "application/octet-stream",
      "cache-control": "no-cache",
    });
    fs.createReadStream(candidate).pipe(response);
  } catch (error) {
    response.writeHead(500, { "content-type": "text/plain; charset=utf-8" });
    response.end(`Server error: ${error.message}`);
  }
});

server.listen(PORT, "127.0.0.1", () => {
  console.log(`Pattern Map local preview: http://127.0.0.1:${PORT}/`);
});

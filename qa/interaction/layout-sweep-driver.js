/**
 * Pattern Map v16 — layout sweep driver.
 *
 * Companion to `layout-probe.js`. The probe measures one rendered page; this
 * driver walks a queue of routes at a fixed viewport so every route in a sweep
 * is measured by the same probe version under the same conditions.
 *
 * It is a local QA instrument, not part of the published site. Inject it into
 * a locally served build (for example by appending a script tag to the files
 * under `site/dist/`), then start a sweep from the console:
 *
 *     patternMapSweep.start({
 *       viewport: "1024x768",
 *       routes: ["/", "/read/", "/map/", "/apply/", "/guided/", "/examples/"],
 *       collector: "http://127.0.0.1:4199/",
 *       probes: ["layout", "enhancement"]
 *     });
 *
 * The queue lives in sessionStorage so it survives the navigations the driver
 * performs. Progress is readable at any time through patternMapSweep.status().
 */
(() => {
  const KEY = "pattern-map-layout-sweep";
  const readState = () => {
    try {
      return JSON.parse(sessionStorage.getItem(KEY) ?? "null");
    } catch {
      return null;
    }
  };
  const writeState = (state) => sessionStorage.setItem(KEY, JSON.stringify(state));

  const PROBES = {
    layout: { module: "/assets/layout-probe.js", global: "patternMapLayoutProbe" },
    enhancement: { module: "/assets/enhancement-probe.js", global: "patternMapEnhancementProbe" },
  };

  const runOne = async (state) => {
    const route = state.routes[state.index];
    const label = `${route}@${state.viewport}`;
    let pass = true;
    for (const name of state.probes ?? ["layout"]) {
      const probe = PROBES[name];
      if (!probe) continue;
      if (typeof globalThis[probe.global] !== "function") await import(probe.module);
      const report = globalThis[probe.global]({ label });
      report.label = report.label ?? label;
      report.sweep = { viewport: state.viewport, route, probe: name, startedAt: state.startedAt };
      await fetch(state.collector, {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify(report),
      });
      pass = pass && report.pass;
    }
    state.done.push({ label, pass });
    state.index += 1;
    writeState(state);
    if (state.index < state.routes.length) {
      location.href = state.routes[state.index];
      return { advancing: true, to: state.routes[state.index] };
    }
    state.finished = true;
    writeState(state);
    return { finished: true, done: state.done };
  };

  globalThis.patternMapSweep = {
    async start({ viewport, routes, collector, probes = ["layout"] }) {
      const state = {
        viewport,
        routes,
        collector,
        probes,
        index: 0,
        done: [],
        finished: false,
        startedAt: new Date().toISOString(),
      };
      writeState(state);
      if (location.pathname !== routes[0]) {
        location.href = routes[0];
        return { started: true, navigatingTo: routes[0] };
      }
      return runOne(state);
    },
    status() {
      const state = readState();
      if (!state) return { active: false };
      return {
        active: !state.finished,
        viewport: state.viewport,
        completed: state.done.length,
        total: state.routes.length,
        failures: state.done.filter((entry) => !entry.pass).map((entry) => entry.label),
      };
    },
    clear() {
      sessionStorage.removeItem(KEY);
      return { cleared: true };
    },
  };

  // Continue an in-flight sweep as soon as the next route finishes loading.
  const state = readState();
  if (state && !state.finished && state.index < state.routes.length) {
    if (location.pathname === state.routes[state.index]) {
      const go = () => runOne(state).catch((error) => console.error("sweep failed", error));
      if (document.readyState === "complete") setTimeout(go, 60);
      else window.addEventListener("load", () => setTimeout(go, 60));
    }
  }
})();

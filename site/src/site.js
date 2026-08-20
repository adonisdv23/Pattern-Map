(() => {
  const familyGrid = document.querySelector(".family-grid");
  const focusStatus = document.querySelector("#family-focus-status");
  const familyCards = [...document.querySelectorAll("[data-family-card]")];
  const focusButtons = [...document.querySelectorAll("[data-family-focus]")];
  const mapStage = document.querySelector("[data-map-stage]");
  const mapButtons = [...document.querySelectorAll("[data-map-family]")];
  const clearButton = document.querySelector("[data-family-clear]");
  const mapFocusTitle = document.querySelector("[data-map-focus-title]");
  const mapFocusQuestion = document.querySelector("[data-map-focus-question]");
  const mapFocusInputs = document.querySelector("[data-map-focus-inputs]");
  const mapFocusRecord = document.querySelector("[data-map-focus-record]");
  const mapFocusBoundary = document.querySelector("[data-map-focus-boundary]");
  const mapFocusStatus = document.querySelector("[data-map-focus-status]");

  const mapButtonFor = (family) => mapButtons.find((button) => button.dataset.mapFamily === family);
  const cardFor = (family) => familyCards.find((card) => card.dataset.familyCard === family);

  const clearFamilyFocus = (announce = true) => {
    familyGrid?.classList.remove("has-focus");
    mapStage?.classList.remove("has-map-focus");
    if (mapStage) delete mapStage.dataset.activeFamily;
    familyCards.forEach((card) => card.classList.remove("is-focused"));
    focusButtons.forEach((button) => button.setAttribute("aria-pressed", "false"));
    mapButtons.forEach((button) => {
      button.setAttribute("aria-pressed", "false");
      button.classList.remove("is-selected");
    });
    if (mapFocusTitle) mapFocusTitle.textContent = "All six families remain in view.";
    if (mapFocusQuestion) mapFocusQuestion.textContent = "Choose a family to inspect its question, inputs, comparison, boundary, record, and adjacent connections. Focus adds emphasis; it never hides essential meaning.";
    if (mapFocusInputs) mapFocusInputs.textContent = "decision brief, permission, evidence, baselines, gaps, comparisons, and outcomes";
    if (mapFocusRecord) mapFocusRecord.textContent = "the route keeps observation, interpretation, recommendation, and human disposition distinct";
    if (mapFocusBoundary) mapFocusBoundary.textContent = "unknown relations stay unknown; human authority remains explicit";
    if (mapFocusStatus) mapFocusStatus.textContent = "All six families are available for comparison.";
    if (announce && focusStatus) focusStatus.textContent = "All six families are visible. Focus controls add emphasis; they never hide essential meaning.";
  };

  const focusFamily = (family, sourceButton) => {
    const card = cardFor(family);
    const mapButton = mapButtonFor(family);
    if (!card || !mapButton) return;
    const alreadyFocused = card.classList.contains("is-focused");
    clearFamilyFocus(false);
    if (alreadyFocused) {
      if (focusStatus) focusStatus.textContent = "All six families are visible. Focus controls add emphasis; they never hide essential meaning.";
      return;
    }
    familyGrid?.classList.add("has-focus");
    mapStage?.classList.add("has-map-focus");
    if (mapStage) mapStage.dataset.activeFamily = family;
    card.classList.add("is-focused");
    focusButtons.find((button) => button.dataset.familyFocus === family)?.setAttribute("aria-pressed", "true");
    mapButtons.forEach((button) => {
      const selected = button === mapButton;
      button.setAttribute("aria-pressed", String(selected));
      button.classList.toggle("is-selected", selected);
    });

    if (mapFocusTitle) mapFocusTitle.textContent = `${mapButton.dataset.mapFamily} · ${mapButton.dataset.mapName}`;
    if (mapFocusQuestion) mapFocusQuestion.textContent = `Question: ${mapButton.dataset.mapQuestion}`;
    if (mapFocusInputs) mapFocusInputs.textContent = `${mapButton.dataset.mapInputs}. Compare: ${mapButton.dataset.mapComparison}. Adjacent connection: ${mapButton.dataset.mapConnections}.`;
    if (mapFocusRecord) mapFocusRecord.textContent = mapButton.dataset.mapRecords;
    if (mapFocusBoundary) mapFocusBoundary.textContent = mapButton.dataset.mapBoundary;
    if (mapFocusStatus) mapFocusStatus.textContent = `${family} is focused in the relationship view. Its question, inputs, comparison, record, boundary, and connections remain visible.`;
    if (focusStatus) focusStatus.textContent = `${family} is focused. The other families remain visible for comparison.`;
    sourceButton?.setAttribute("aria-pressed", "true");
  };

  focusButtons.forEach((button) => {
    button.addEventListener("click", () => focusFamily(button.dataset.familyFocus, button));
  });
  mapButtons.forEach((button) => {
    button.addEventListener("click", () => focusFamily(button.dataset.mapFamily, button));
  });
  clearButton?.addEventListener("click", () => clearFamilyFocus());

  const moreButton = document.querySelector(".nav-more");
  const secondary = document.querySelector(".secondary-nav-wrap");
  const setMoreOpen = (isOpen, moveFocus = false) => {
    moreButton?.setAttribute("aria-expanded", String(isOpen));
    secondary?.classList.toggle("is-open", isOpen);
    if (isOpen && moveFocus) secondary?.querySelector("a")?.focus();
  };
  moreButton?.addEventListener("click", () => {
    const isOpen = moreButton.getAttribute("aria-expanded") === "true";
    setMoreOpen(!isOpen, !isOpen);
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && moreButton?.getAttribute("aria-expanded") === "true") {
      setMoreOpen(false);
      moreButton.focus();
    }
    if (event.key === "Escape") {
      document.querySelectorAll(".orientation-mobile[open]").forEach((details) => {
        details.removeAttribute("open");
        details.querySelector("summary")?.focus();
      });
    }
  });

  const readingSections = [...document.querySelectorAll("[data-reading-section]")];
  const readingLinks = [...document.querySelectorAll("[data-reading-link]")];
  const progress = document.querySelector("[data-reading-progress]");
  const progressValue = document.querySelector("[data-reading-progress-value]");
  if (readingSections.length) {
    const setReadingActive = (id) => {
      readingLinks.forEach((link) => {
        const active = link.getAttribute("href") === `#${id}`;
        link.classList.toggle("is-current", active);
        if (active) link.setAttribute("aria-current", "location");
        else link.removeAttribute("aria-current");
      });
    };
    const updateReadingProgress = () => {
      const route = document.querySelector(".reading-route");
      if (!route || !progress) return;
      const start = route.getBoundingClientRect().top + window.scrollY;
      const end = start + route.scrollHeight - window.innerHeight;
      const percent = end <= start ? 100 : Math.max(0, Math.min(100, ((window.scrollY - start) / (end - start)) * 100));
      progress.querySelector("span")?.style.setProperty("width", `${percent}%`);
      progress.setAttribute("aria-valuenow", String(Math.round(percent)));
      progress.setAttribute("aria-valuetext", `${Math.round(percent)} percent of the reading route`);
      if (progressValue) progressValue.textContent = `${Math.round(percent)}%`;
    };
    const observer = new IntersectionObserver((entries) => {
      const visible = entries.filter((entry) => entry.isIntersecting).sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
      if (visible[0]?.target.id) setReadingActive(visible[0].target.id);
    }, { rootMargin: "-18% 0px -68% 0px", threshold: 0 });
    readingSections.forEach((section) => observer.observe(section));
    window.addEventListener("scroll", updateReadingProgress, { passive: true });
    window.addEventListener("resize", updateReadingProgress);
    updateReadingProgress();
  }

  const routeStudio = document.querySelector("[data-route-studio]");
  const receipt = document.querySelector("[data-route-receipt]");
  if (routeStudio && receipt) {
    const fieldValue = (name) => routeStudio.querySelector(`input[name="${name}"]:checked`)?.value ?? "";
    const setReceiptText = (selector, value) => {
      const element = receipt.querySelector(selector);
      if (element) element.textContent = value;
    };
    const buildReceipt = () => {
      const consequence = fieldValue("consequence");
      const uncertainty = fieldValue("uncertainty");
      const budget = fieldValue("budget");
      const permission = fieldValue("permission");
      let route = "ordinary";
      let routeToken = "ANSWER";
      let stop = "COMPLETE";
      let learning = "LEARNING_NOT_APPLICABLE";
      let authority = "HUMAN_DISPOSITION_RECORDED";
      let title = "Do less when the task is simple.";
      let summary = "For reversible work with low uncertainty, keep the route small and leave the important distinctions visible.";
      if (budget === "substantial" || (consequence === "consequential" && uncertainty === "high")) {
        route = "advanced";
        routeToken = "CLARIFY";
        stop = "STOPPED_DEADLINE";
        learning = "LEARNING_PLANNED";
        authority = "HUMAN_DISPOSITION_REQUIRED";
        title = "Engineer only when hidden mistakes justify it.";
        summary = "A larger route is a proposal for queryable lineage and review, not permission to acquire, disclose, spend, or act.";
      } else if (consequence === "consequential" || uncertainty === "high" || permission === "human-gate") {
        route = "moderate";
        routeToken = permission === "supplied" ? "COMPARE" : "HOLD";
        stop = "STOPPED_OTHER";
        learning = "LEARNING_PENDING_OUTCOME";
        authority = "HUMAN_DISPOSITION_REQUIRED";
        title = "Make repeated or consequential work reproducible.";
        summary = "Keep identity, comparison, uncertainty, permission, a stop reason, and a human checkpoint visible before influence.";
      } else if (uncertainty === "mixed" || budget === "bounded" || permission === "restricted") {
        route = "lightweight";
        routeToken = "ANSWER_PROVISIONALLY";
        stop = "STOPPED_BUDGET";
        learning = "LEARNING_PLANNED";
        title = "One brief, one alternate route, one clear stop.";
        summary = "A bounded pass records the decision, one peripheral candidate, one comparison, one challenge, and what remains uncertain.";
      }
      const routeBadge = receipt.querySelector("[data-receipt-route]");
      if (routeBadge) routeBadge.textContent = route;
      setReceiptText("[data-receipt-title]", title);
      setReceiptText("[data-receipt-summary]", summary);
      setReceiptText("[data-receipt-route-value]", routeToken);
      setReceiptText("[data-receipt-stop]", stop);
      setReceiptText("[data-receipt-learning]", learning);
      setReceiptText("[data-receipt-authority]", authority);
      setReceiptText("[data-receipt-status]", `Receipt built for ${route}. Route, stop, learning, and authority remain separate fields.`);
      const flow = receipt.querySelector("[data-receipt-flow-state]");
      if (flow) {
        flow.querySelector("strong").textContent = route === "ordinary" ? "complete" : route === "lightweight" ? "stop" : route === "moderate" ? "disposition" : "clarify";
        flow.querySelector("small").textContent = route === "ordinary" ? "ordinary path" : route === "lightweight" ? "budget boundary" : route === "moderate" ? "human gate" : "question authority";
      }
      receipt.dataset.route = route;
    };
    routeStudio.addEventListener("submit", (event) => {
      event.preventDefault();
      buildReceipt();
    });
    routeStudio.querySelector("[data-route-reset]")?.addEventListener("click", () => {
      routeStudio.reset();
      buildReceipt();
    });
    receipt.querySelectorAll("[data-route-action]").forEach((button) => {
      button.addEventListener("click", () => {
        const action = button.dataset.routeAction;
        const actionDetails = {
          hold: { route: "HOLD", stop: "STOPPED_OTHER", authority: "HUMAN_DISPOSITION_REQUIRED", message: "HOLD recorded. A person must decide whether the route may continue." },
          escalate: { route: "ESCALATE", stop: "STOPPED_OTHER", authority: "HUMAN_DISPOSITION_REQUIRED", message: "ESCALATE recorded. Consequential authority remains with a person." },
          stop: { route: "ANSWER_PROVISIONALLY", stop: "STOPPED_BUDGET", authority: "HUMAN_DISPOSITION_RECORDED", message: "STOPPED_BUDGET recorded. Remaining uncertainty stays visible." },
        }[action];
        if (!actionDetails) return;
        setReceiptText("[data-receipt-route-value]", actionDetails.route);
        setReceiptText("[data-receipt-stop]", actionDetails.stop);
        setReceiptText("[data-receipt-authority]", actionDetails.authority);
        setReceiptText("[data-receipt-status]", actionDetails.message);
        const flow = receipt.querySelector("[data-receipt-flow-state]");
        if (flow) {
          flow.querySelector("strong").textContent = action === "stop" ? "stop" : action;
          flow.querySelector("small").textContent = action === "stop" ? "budget boundary" : "human disposition";
        }
        receipt.dataset.state = action;
      });
    });
    buildReceipt();
  }
})();

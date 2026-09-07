"use client";

import type { MouseEvent } from "react";

export default function CollapseControl({ componentId }: { componentId: string }) {
  const closeRecord = (event: MouseEvent<HTMLButtonElement>) => {
    const details = event.currentTarget.closest("details");
    if (!(details instanceof HTMLDetailsElement)) return;

    details.open = false;
    details.querySelector("summary")?.focus();
  };

  return (
    <button className="collapse-control" type="button" onClick={closeRecord}>
      Close {componentId} and return to its summary ↑
    </button>
  );
}

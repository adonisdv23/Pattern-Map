"use client";

import { useEffect, useState } from "react";

const items = [
  ["start", "Start"],
  ["five-minute", "01 Overview"],
  ["map", "02 Families"],
  ["mechanisms", "03 Mechanisms"],
  ["connections", "04 Connections"],
  ["example", "05 Example"],
  ["challenges", "06 Challenges"],
  ["cases", "07 Cases"],
  ["research", "08 Research"],
  ["sources", "09 Sources"],
] as const;

export default function ReadingNav() {
  const [active, setActive] = useState("start");

  useEffect(() => {
    const sections = items
      .map(([id]) => document.getElementById(id))
      .filter((element): element is HTMLElement => Boolean(element));

    const observer = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((entry) => entry.isIntersecting)
          .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
        if (visible[0]?.target.id) setActive(visible[0].target.id);
      },
      { rootMargin: "-18% 0px -70% 0px", threshold: 0 },
    );

    sections.forEach((section) => observer.observe(section));
    const syncHash = () => {
      const hash = window.location.hash.slice(1);
      if (items.some(([id]) => id === hash)) setActive(hash);
    };
    window.addEventListener("hashchange", syncHash);
    syncHash();
    return () => {
      observer.disconnect();
      window.removeEventListener("hashchange", syncHash);
    };
  }, []);

  return (
    <nav aria-label="Primary reading navigation">
      {items.map(([id, label]) => (
        <a key={id} href={`#${id}`} aria-current={active === id ? "location" : undefined}>
          {label}
        </a>
      ))}
    </nav>
  );
}

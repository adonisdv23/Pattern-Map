import HomeEssay from "./HomeEssay";
import {
  PatternRecognitionPage as ReferencePage,
  type PageMode as ReferencePageMode,
} from "./ReferenceRoutes";

export type PageMode = "home" | ReferencePageMode;

export function PatternRecognitionPage({ mode = "home" }: { mode?: PageMode }) {
  if (mode === "home") return <HomeEssay />;
  return <ReferencePage mode={mode} />;
}

export default function Home() {
  return <HomeEssay />;
}

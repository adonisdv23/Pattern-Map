import type { Metadata, Viewport } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Pattern Recognition: The Discrimination Layer",
  description: "A provisional visual systems framework for inspectable context judgment before AI generates.",
  applicationName: "Pattern Recognition v14",
  robots: { index: false, follow: false },
  openGraph: {
    type: "article",
    title: "Pattern Recognition: The Discrimination Layer",
    description: "A provisional map of context judgment before generation.",
    images: [
      {
        url: "/og.png",
        width: 1200,
        height: 630,
        alt: "Pattern Recognition: The Discrimination Layer — nine observations related to one shared origin, with two separate comparison roots.",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "Pattern Recognition: The Discrimination Layer",
    description: "A provisional map of context judgment before generation.",
    images: ["/og.png"],
  },
};

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  themeColor: "#f3efe5",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body>{children}</body></html>;
}

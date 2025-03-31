import type { Metadata } from "next";
import LocalFont from "next/font/local";

import "./globals.css";

const geistSans = LocalFont({
  src: "/fonts/Geist/Geist-VariableFont_wght.ttf",
  variable: "--font-geist-sans"
});

const geistMono = LocalFont({
  src: "/fonts/Geist_Mono/GeistMono-VariableFont_wght.ttf",
  variable: "--font-geist-mono"
});

export const metadata: Metadata = {
  title: "PersonalAIs",
  description: "Advanced AI Agent for music.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${geistSans.variable} ${geistMono.variable} antialiased`}>
        {children}
      </body>
    </html>
  );
}

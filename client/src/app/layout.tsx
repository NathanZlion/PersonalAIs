import type { Metadata } from "next";
import LocalFont from "next/font/local";
import { Toaster } from "@/components/ui/sonner"
import { ThemeProvider } from "@/components/ui/theme-provider";


import "./globals.css";
import { TooltipProvider } from "@/components/ui/tooltip";

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
    <html lang="en" suppressHydrationWarning suppressContentEditableWarning>
      <body className={`${geistSans.variable} ${geistMono.variable} antialiased`}>
        <ThemeProvider
          attribute="class"
          defaultTheme="dark"
          enableSystem
          disableTransitionOnChange
        >
          <TooltipProvider>
            <Toaster />
            {children}
          </TooltipProvider>
        </ThemeProvider>
      </body>
    </html >
  );
}

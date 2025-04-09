"use client";

import { useAuthStore } from "@/lib/store/auth";
import LandingPage from "./_landing/landing_page";
// import redirect
import { redirect } from "next/navigation";

export default function Home() {
  // add conditional rendering for logged in user
  const {
    is_loading,
    is_authenticated,
  } = useAuthStore()


  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen pb-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-[32px] row-start-2 items-center sm:items-start">
        {
          is_loading && <p>
            Loading...
          </p>
        }

        {
          is_authenticated && (
            <>
              <p>You are logged in!</p>
              {redirect("/app")}
            </>
          )
        }

        {
          !is_authenticated &&
          <LandingPage />
        }
      </main>
    </div>
  );
}

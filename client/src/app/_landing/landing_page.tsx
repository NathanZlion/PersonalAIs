'use client'

import HeroSection from "./hero_section";
import LandingPageNavBar from "./nav_bar";


export default function LandingPage() {
    return (
        <div className="mx-auto w-full lg:px-10">
            <LandingPageNavBar />
            <main>
                <HeroSection />
            </main>
        </div>
    );
}
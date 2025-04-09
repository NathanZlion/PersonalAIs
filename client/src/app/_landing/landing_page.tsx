'use client'

import HeroSection from "./hero_section";
import NavBar from "../nav_bar";


export default function LandingPage() {

    return (
        <div className="mx-auto w-full lg:px-10">
            <NavBar />

            <main>
                <HeroSection />
            </main>
        </div>
    );
}
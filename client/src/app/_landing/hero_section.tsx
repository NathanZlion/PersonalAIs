import { BackgroundBeams } from "@/components/ui/background-beam";
import { Button } from "@/components/ui/button";
import React from "react";
import { DotLottieReact } from "@lottiefiles/dotlottie-react";
import { IconBrandSpotify } from "@tabler/icons-react";

export default function HeroSection() {
    return (
        <section className="p-10 lg:py-28 lg:px-16 text-2xl lg:text-7xl grid grid-cols-1 lg:grid-cols-6 items-center min-h-[90vh] h-fit gap-3 relative">
            <div className="flex flex-col col-span-4 gap-9 items-center lg:items-start justify-between h-2/3 lg:h-fit">
                <BackgroundBeams className="border-none outline-none" key={"beam"} />
                <div className="w-full text-center lg:text-start text-4xl lg:text-7xl">
                    <div>Elevate Your Music</div>
                    <span className="italic text-primary stroke-secondary stroke-1 fill-transparent">With AI</span>
                </div>
                <p className="text-lg lg:text-2xl text-muted-foreground max-w-2xl text-center lg:text-left">
                    Your personal AI-powered music assistant.
                </p>
                <div className="flex gap-4">
                    {/* <Button className="text-lg px-6 py-3" size="lg">Get Started</Button> */}

                    <Button className="max-md:hidden font-azeretMono">
                        <IconBrandSpotify />
                        Signup with Spotify
                    </Button>
                </div>
            </div>

            <div className="col-span-2 p-0 m-0 aspect-square min-h-5 relative overflow-hidden hidden lg:block zoom-in-150">
                <DotLottieReact
                    src="/animations/astraunut_music.lottie"
                    loop autoplay />
            </div>
        </section>
    );
}
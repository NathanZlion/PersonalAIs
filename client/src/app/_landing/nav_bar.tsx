import LogoComponent from "@/components/logo";
import { Button } from "@/components/ui/button";
import { FloatingNav } from "@/components/ui/floating-navbar";
import { IconBrandGithub, IconBrandSpotify, IconMenu2, IconX } from "@tabler/icons-react";
import { motion } from "framer-motion";
import Link from "next/link";
import { useState, useRef, useEffect, JSX } from "react";

type NavItem = {
    name: string;
    link: string;
    icon?: JSX.Element;
};

const navItems: NavItem[] = [
    { name: "Github", link: "https://github.com/NathanZlion/PersonalAIs", icon: <IconBrandGithub /> },
];

export default function LandingPageNavBar() {
    const [open, setOpen] = useState(false);

    return (
        <nav className="top-0 left-0 w-full bg-background/80 z-50 flex flex-row p-2 justify-between border-b-2 border-b-foreground/15 max-md:fixed">
            {/* Logo & Mobile Menu Button */}
            <div className="flex flex-row gap-4 items-center ps-5 lg:ps-20 w-fit">
                <button className="md:hidden" onClick={() => setOpen(true)}>
                    <IconMenu2 size={24} />
                </button>
                <LogoComponent />
                <h1 className="text-lg max-md:hidden"> PersonalAIs </h1>
            </div>

            {/* Desktop Nav */}
            <div className="max-md:hidden flex flex-row justify-end items-center px-5 w-full space-x-8">
                {navItems.map(({ name, link, icon }) => (
                    <Link key={name} className="flex gap-2" href={link}>
                        {icon} <span className="sm:hidden">{name}</span>
                    </Link>
                ))}
            </div>

            {/* Actions */}
            <div className="flex flex-row justify-between items-center pe-5 lg:pe-20 gap-5 font-azeretMono">
                <Button className="max-md:hidden font-azeretMono">
                    <IconBrandSpotify />
                    Signup with Spotify
                </Button>
            </div>

            {/* Floating Nav for scroll visibility */}
            <FloatingNav className="max-md:hidden" navItems={
                [
                    {
                        link: "#",
                        name: "PersonalAIs",
                        icon: <LogoComponent />
                    },
                    ...navItems
                ]
            } />

            {/* Mobile Sidebar */}
            <MobileNavbarSidebar open={open} setOpen={setOpen} />
        </nav>
    );
}



const MobileNavbarSidebar = ({ open, setOpen }: { open: boolean; setOpen: (state: boolean) => void; }) => {
    const sidebarRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        const handleClickOutside = (event: MouseEvent) => {
            if (sidebarRef.current && !sidebarRef.current.contains(event.target as Node)) {
                setOpen(false);
            }
        };

        document.addEventListener("mousedown", handleClickOutside);
        return () => {
            document.removeEventListener("mousedown", handleClickOutside);
        };
    }, [setOpen]);

    return (
        <motion.div
            ref={sidebarRef}
            initial={{ x: "-100%" }}
            animate={{ x: open ? "0%" : "-100%" }}
            transition={{ type: "spring", stiffness: 200, damping: 30 }}
            className="fixed inset-y-0 left-0 w-64 bg-background shadow-lg p-6 z-50 md:hidden"
            drag="x"
            dragConstraints={{ left: 0, right: 0 }}
            onDragEnd={(_event, info) => {
                if (info.point.x < -50) {
                    setOpen(false);
                }
            }}
        >
            <Button
                className="absolute top-4 right-4"
                onClick={() => setOpen(false)}
                variant={"outline"}
            >
                <IconX size={24} />
            </Button>
            <div className="flex flex-col gap-6 mt-10">
                {navItems.map(({ name, link, icon }) => (
                    <Link key={name} href={link} className="flex gap-3 items-center text-lg font-medium" onClick={() => setOpen(false)}>
                        {icon} {name}
                    </Link>
                ))}
            </div>
        </motion.div>
    );
};
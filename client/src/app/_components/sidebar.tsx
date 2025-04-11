'use client'

import * as React from "react"
import { NavUser } from "@/app/_components/nav-user"
import {
    Sidebar,
    SidebarContent,
    SidebarFooter,
    SidebarHeader,
    SidebarRail,
} from "@/components/ui/sidebar"
import Logo from "@/components/logo"
import { NavGroup, NavMenuItem } from "@/app/_components/nav-group"

import { IconHome, IconCube3dSphere, IconBrandGithub, IconBug, IconMail, IconSparkles } from "@tabler/icons-react"
import { Skeleton } from "@/components/ui/skeleton"
import { useAuthStore } from "@/lib/store/auth"
import { SignInButton } from "./signin-button"

// This is sample data.


export function AppSidebar({ ...props }: React.ComponentProps<typeof Sidebar>) {
    // const { isSignedIn, user, isLoaded } = 
    const { user, is_loading, is_authenticated } = useAuthStore();

    const data = {
        user: {
            name: user?.display_name,
            email: user?.email,
            avatar: user?.images?.[0]?.url,
        },
        navMenuItems: [
            {
                title: "Dashboard",
                url: "/app",
                icon: <IconHome />
            },
            {
                title: "Chat",
                url: "/app/chat",
                icon: <IconCube3dSphere />,
                items: [
                    {
                        title: "Introduction",
                        url: "intro"
                    },
                    {
                        title: "Linkedlist",
                        url: "linkedin"
                    }
                ]
            },
        ] as NavMenuItem[],
        footerItems: [
            {
                title: "Github",
                url: "https://github.com/NathanZlion/PersonalAIs/",
                icon: <IconBrandGithub />,
                target: "_blank"
            },
            {
                title: "Report a bug",
                url: "https://github.com/NathanZlion/PersonalAIs/issues/new",
                icon: <IconBug />,
                target: "_blank",
            },
            {
                title: "Feature Request",
                url: "https://github.com/NathanZlion/PersonalAIs/issues/new",
                icon: <IconSparkles />,
                target: "_blank"
            },
            {
                title: "Contact",
                url: "mailto:nathandere1357@gmail.com",
                icon: <IconMail />,
                target: "_blank"
            }
        ] as NavMenuItem[],
    }

    return (
        <Sidebar collapsible="icon" {...props}>

            <SidebarHeader>
                <div className="flex flex-row gap-2 items-center w-full overflow-hidden">
                    <Logo />
                    <h1 className="
                    max-md:hidden
                     text-lg font-dotGothic">PersonalAIs</h1>
                </div>
            </SidebarHeader>

            <SidebarContent>
                <NavGroup items={data.navMenuItems} />
            </SidebarContent>
            <SidebarFooter>
                <NavGroup items={data.footerItems} />

                {is_loading &&
                    <div className="flex items-center space-x-2 p-2">
                        <Skeleton className="h-9 w-9 rounded-xl bg-muted" />
                        <div className="space-y-2 flex-1">
                            <Skeleton className="h-4 w-1/2 bg-muted" />
                            <Skeleton className="h-4 bg-muted" />
                        </div>
                        <Skeleton className="h-4 w-4 bg-muted rounded-none" />
                    </div>
                }

                {
                    is_authenticated &&
                    <NavUser
                        user={{
                            name: user?.display_name || user?.id || "",
                            email: user?.email || "",
                            avatar: user?.images?.[0]?.url || "",
                        }}
                    />
                }

                {!is_loading && !is_authenticated && <SignInButton />}

            </SidebarFooter>
            <SidebarRail />
        </Sidebar>
    )
}
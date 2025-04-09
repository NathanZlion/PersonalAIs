"use client"

import { Button } from "@/components/ui/button";
import { AxiosInstance } from "@/lib/axios";
import { redirect } from "next/navigation";

export const SignInButton = ({ children }: { children?: React.ReactNode }
) => {

    const handleSignin = async () => {
        const res = await AxiosInstance.get("/auth/login");
        const { redirect_url } = res.data;
        // window.location.href = url;
        redirect(redirect_url);
    };

    return (
        <Button
            className="flex items-center gap-2 text-sm font-medium cursor-pointer"
            onClick={handleSignin}
        >
            {
                children ? children : "Sign In"
            }
        </Button>
    );
}
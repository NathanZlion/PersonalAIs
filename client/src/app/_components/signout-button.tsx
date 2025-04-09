'use client'

import { useAuthStore } from "@/lib/store/auth";

export const SignOutButton = () => {
    const { logout } = useAuthStore.getState();

    const handleLogout = () => {
    };
    logout();

    return (
        <div
            className="flex items-center gap-2 text-sm font-medium cursor-pointer"
            onClick={handleLogout}
        >
            Sign Out
        </div>
    );
}
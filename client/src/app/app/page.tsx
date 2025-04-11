"use client";

import { useAuthStore } from "@/lib/store/auth";
import { Loader2 } from "lucide-react";

export default function Page() {
    const { user, is_loading, is_authenticated } = useAuthStore();

    return (
        <div className="flex flex-col items-center justify-center w-full h-full">
            <h1 className="text-4xl font-bold">Welcome to PersonalAIs</h1>
            <p className="mt-4 text-lg">Your advanced AI agent for music.</p>

            {is_loading && (
                <div className="flex items-center mt-4">
                    <Loader2 className="animate-spin mr-2" />
                    <span>Loading...</span>
                </div>
            )}

            {is_authenticated && (
                <div className="mt-4">
                    <p className="text-lg">Hello, {user?.display_name}!</p>
                    <p className="text-sm text-gray-500">{user?.email}</p>
                </div>
            )}

        </div>
    );
}
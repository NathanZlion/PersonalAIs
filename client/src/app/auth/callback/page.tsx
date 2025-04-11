'use client'

import { useEffect, useState } from "react"
import { redirect, useRouter, useSearchParams } from "next/navigation"
import { useAuthStore } from "@/lib/store/auth"
import { toast } from "sonner"
import { Button } from "@/components/ui/button"
import { Loader2 } from "lucide-react"
import { useShallow } from 'zustand/react/shallow'



export const CallbackPage = () => {
    const router = useRouter()
    const searchParams = useSearchParams()

    // const  = useAuthStore()
    const [is_loading, is_authenticated, login] = useAuthStore(
        useShallow(
            (state) => [
                state.is_loading,
                state.is_authenticated,
                state.login
            ])
    )

    const state = searchParams.get("state")
    const code = searchParams.get("code")

    const [error, _] = useState<string | null>(searchParams.get("error"));

    useEffect(() => {
        if (!code) {
            toast("Error Signing In...", { description: `Missing code`, duration: 5000 });
            return;
        }
        if (error) {
            toast("Error Signing In...", { description: `${error}`, duration: 5000 });
        } else {
            login(code, state);
        }
    }, [code, state, error]);

    useEffect(() => {
        if (is_authenticated) {
            redirect("/");
        }
    }, [is_authenticated]);

    return (
        <div className="flex items-center justify-center h-screen">
            {/* show is_authenticated state */}

            <div className="flex flex-col items-center">
                {error ? (
                    <>
                        <h1 className="text-2xl font-bold mb-4 text-red-500">Something went wrong</h1>
                        <p className="mb-4">{error}</p>
                        <Button
                            variant="outline"
                            onClick={() => (
                                // go home
                                router.push("/")
                            )}
                        >
                            Retry Redirect
                        </Button>
                    </>
                ) : (
                    <>
                        <h1 className="text-2xl font-bold mb-4">Redirecting...</h1>
                        {is_loading && (
                            <Button disabled={is_loading} variant="outline">
                                <Loader2 className="animate-spin" />
                            </Button>
                        )}

                        {
                            is_authenticated && (
                                <div>
                                    <p className="mb-4">You are now logged in. Redirecting you please wait ...</p>

                                    <Button
                                        variant="outline"
                                        onClick={() => (router.push("/"))}
                                    >
                                        Redirect Manually
                                    </Button>
                                </div>
                            )
                        }
                    </>
                )}
            </div>
        </div>

    );
};

export default CallbackPage;
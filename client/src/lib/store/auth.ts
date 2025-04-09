import { create } from "zustand"
import { persist, createJSONStorage } from "zustand/middleware"
import { AxiosInstance } from "../axios"

export type Image = {
    url: string,
    height?: number,
    width?: number,
}

export type User = {
    id: string,
    spotify_id: string,
    email: string,
    country: string,
    display_name?: string,
    images?: Image[],
}


type AuthState = {
    user: User | null,
    access_token: string | null,
    refresh_token: string | null,
    access_token_expires_at: number | null,
    refresh_token_expires_at: number | null,
    is_authenticated: boolean,
    is_loading: boolean,
}


export interface AuthCallbackResponse {
    user: User;
    access_token: string;
    refresh_token: string;
    // expires_at is a timestamp in milliseconds
    expires_at: number;
}

type AuthActions = {
    set_loading: (is_loading: boolean) => void,
    set_user: (user: User | null) => void,
    login: (
        code: string,
        state: string | null,
    ) => void,
    logout: () => void,
    refresh_access_token: (access_token: string, access_token_expires_at: number) => void,
}

const initialAuthState: AuthState = {
    user: null,
    is_loading: false,
    access_token: null,
    refresh_token: null,
    access_token_expires_at: null,
    refresh_token_expires_at: null,
    is_authenticated: false,
}

export const useAuthStore = create<AuthState & AuthActions>()(
    persist(
        (set) => ({
            ...initialAuthState,

            // called when the user updates their profile
            set_user: (user) => {
                set({ is_loading: true })
                set({ user })
                set({ is_loading: false })
            },

            set_loading: (is_loading) => {
                set((state) => ({
                    ...state,
                    is_loading: is_loading
                }))
            },

            login: async (code, state) => {
                try {
                    set((state) => ({
                        ...state,
                        is_loading: true
                    }))

                    const res = await AxiosInstance.post<AuthCallbackResponse>('/auth/callback', { code, state })
                    const { user, access_token, refresh_token, expires_at } = res.data;

                    set((state) => ({
                        ...state,
                        user,
                        access_token,
                        refresh_token,
                        access_token_expires_at: expires_at,
                        is_authenticated: true,
                    }))

                } finally {
                    set((state) => ({
                        ...state,
                        is_loading: false
                    }))
                }
            },
            logout: () => {
                useAuthStore.persist.clearStorage()

                set((state) => ({
                    ...state,
                    initialAuthState
                }))

                console.log("Logged out")

            },

            refresh_access_token: (access_token, access_token_expires_at) => set({
                access_token,
                access_token_expires_at,
            })
        }),
        {
            name: "auth-storage",
            storage: createJSONStorage(() => localStorage),
        }
    )
)
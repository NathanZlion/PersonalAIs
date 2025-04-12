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
    expires_at: number;  // expires_at is a timestamp in milliseconds
}

export interface AuthLogoutResponse {
    message: string;
}

type AuthActions = {
    set_loading: (is_loading: boolean) => void,
    set_user: (user: AuthState["user"]) => void,
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

            set_user: (user) => {
                set({ is_loading: true });
                set({ user });
                set({ is_loading: false });
            },

            set_loading: (is_loading) => {
                set(() => ({
                    is_loading,
                }));
            },

            login: async (code, state) => {
                try {
                    set({ is_loading: true });
                    const res = await AxiosInstance.post<AuthCallbackResponse>('/auth/callback', { code, state });
                    const { user, access_token, refresh_token, expires_at } = res.data;

                    set({
                        user,
                        access_token,
                        refresh_token,
                        access_token_expires_at: expires_at,
                        is_authenticated: true,
                        is_loading: false,
                    });
                } catch (error) {
                    console.error("Login error:", error);
                } finally {
                    set({ is_loading: false });
                }
            },

            logout: async () => {
                // Reset the state to initialAuthState
                set({ is_loading: true });
                set(() => ({
                    ...initialAuthState
                }));
                console.log("Logged out");
                set({ is_loading: false });
            },

            refresh_access_token: (access_token, access_token_expires_at) =>
                set({
                    access_token,
                    access_token_expires_at,
                }),
        }),
        {
            name: "auth-storage",
            storage: createJSONStorage(() => localStorage),
            partialize: (state) => ({
                user: state.user,
                access_token: state.access_token,
                refresh_token: state.refresh_token,
                access_token_expires_at: state.access_token_expires_at,
                refresh_token_expires_at: state.refresh_token_expires_at,
                is_authenticated: state.is_authenticated,
            }),
        }
    )
);

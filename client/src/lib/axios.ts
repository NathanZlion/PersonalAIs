import axios from "axios";
import { useAuthStore } from "./store/auth";

export const AxiosInstance = axios.create({
    baseURL: process.env.NEXT_PUBLIC_SERVER_BASE_URL,
    timeout: 9000,
    headers: {
        "Content-Type": "application/json",
    },
});

AxiosInstance.interceptors.request.use(
    (config) => {
        const { access_token } = useAuthStore.getState();

        // If token is present, add it to request's Authorization Header
        if (access_token) {
            config.headers["Authorization"] = `Bearer ${access_token}`;
        }

        return config;
    },
    (error) => {
        // Handle request errors here
        return Promise.reject(error);
    }
);


// Axios Interceptor: Response Method
AxiosInstance.interceptors.response.use(
    (response) => {
        // Can be modified response
        console.log("Response Interceptor: ", response);
        return response;
    },
    (error) => {
        // Handle response errors here
        return Promise.reject(error);
    }
);


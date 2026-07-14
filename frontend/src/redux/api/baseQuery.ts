import { fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import type { RootState } from "../store/store";

export const baseQuery = fetchBaseQuery({
    baseUrl: import.meta.env.VITE_API_BASE_URL,

    prepareHeaders: (headers, { getState }) => {

        const token = (getState() as RootState).auth.accessToken;

        if (token) {
            headers.set("Authorization", `Bearer ${token}`);
        }

        return headers;
    },
});
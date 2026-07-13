import { baseApi } from "../api/baseApi";

export const authApi = baseApi.injectEndpoints({
    endpoints: (builder) => ({
        login: builder.mutation({
            query: (data) => ({
                url: "auth/login",
                method: "POST",
                body: data
            })
        }),

        requestOTP: builder.mutation({
            query: (data) => ({
                url: "auth/request",
                method: "POST",
                body: data
            })
        }),

        getMe: builder.query<any, void>({
            query: () => ({
                url: "/auth/me",
                method: "GET",
            }),
        }),

    })
})

export const { useLoginMutation, useRequestOTPMutation, useGetMeQuery, useLazyGetMeQuery } = authApi;
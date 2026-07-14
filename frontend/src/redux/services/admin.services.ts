import { baseApi } from "../api/baseApi";

export const authApi = baseApi.injectEndpoints({
    endpoints: (builder) => ({
        addUser: builder.mutation({
            query: (data) => ({
                url: "api/v1/user",
                method: "POST",
                body: data
            })
        }),

        getUser: builder.query<any, void>({
            query: () => ({
                url: "api/v1/user",
                method: "GET",
            })
        }),

        addEvent: builder.mutation({
            query: (data) => ({
                url: "auth/addUser",
                method: "POST",
                body: data
            })
        }),
    })
})

export const { useAddEventMutation, useAddUserMutation, useGetUserQuery } = authApi;
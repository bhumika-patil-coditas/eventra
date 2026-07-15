import { baseApi } from "../api/baseApi";

export const organizerApi = baseApi.injectEndpoints({
    endpoints: (builder) => ({
        getPresined: builder.mutation({
            query: (key) => ({
                url: "/aws/s3/get-uplaod-presigned-url",
                method: "POST",
                params: {
                    key: key
                }
            })
        }),

        changeEventStatus: builder.mutation({
            query: (status) => ({
                url: "/changeStatus",
                method: "POST",
                body: status
            })
        })


    })
})

export const { useGetPresinedMutation, useChangeEventStatusMutation } = organizerApi;
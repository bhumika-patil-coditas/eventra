import { createSlice, type PayloadAction } from "@reduxjs/toolkit";

export interface User {
    id: number;
    name: string;
    email: string;
    role: "ORGANIZER" | "VENDOR" | "ADMIN";
}

interface AuthState {
    accessToken: string | null;
    user: User | null;
    isInitializing: boolean | null,
}

const initialState: AuthState = {
    accessToken: null,
    user: null,
    isInitializing: true,
};

const authSlice = createSlice({
    name: "auth",
    initialState,
    reducers: {
        setAccessToken: (state, action: PayloadAction<string | null>) => {
            state.accessToken = action.payload
        },

        setUser: (state, action: PayloadAction<User | null>) => {
            state.user = action.payload
        },

        setInitializing: (state, action: PayloadAction<boolean | null>) => {
            state.isInitializing = action.payload;
        },

        logout: (state) => {
            state.accessToken = null;
            state.user = null;
            state.isInitializing = false;
        }
    }
})

export const { setAccessToken, setUser, logout, setInitializing } = authSlice.actions;

export default authSlice.reducer;
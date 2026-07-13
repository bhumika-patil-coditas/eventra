const ACCESS_TOKEN_KEY = "accessToken";

export const tokenStorage = {
    setTokens(accessToken: string) {
        localStorage.setItem(ACCESS_TOKEN_KEY, accessToken);
    },

    getAccessToken() {
        return localStorage.getItem(ACCESS_TOKEN_KEY);
    },

    clearTokens() {
        localStorage.removeItem(ACCESS_TOKEN_KEY);
    }
};
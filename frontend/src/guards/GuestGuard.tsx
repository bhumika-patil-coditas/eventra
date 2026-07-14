import { Navigate, Outlet } from "react-router-dom";
import { Roleconfig } from "../config/Role.config";
import { useAppSelector } from "../hooks/useHooks";

const GuestGuard = () => {
    const { accessToken, user, isInitializing } = useAppSelector((state) => state.auth);

    if (!isInitializing) return <p>Loading...</p>

    const isAuthenticated = !!accessToken && !!user;

    if (isAuthenticated && user) {
        <Navigate to={Roleconfig[user.role]} replace />
    }

    return <Outlet />

}

export default GuestGuard;
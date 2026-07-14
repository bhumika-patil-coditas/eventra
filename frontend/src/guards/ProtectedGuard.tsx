import { useSelector } from "react-redux"
import { Navigate, Outlet } from "react-router-dom";

const ProtectedGuard = () => {
    const { accessToken, user, isInitializing } = useSelector((state: any) => state.auth);

    if (!isInitializing) return <p>Loading...</p>

    const isAuthenticated = !!accessToken && !!user;

    if (!isAuthenticated) return <Navigate to="/" replace />

    return <Outlet />
}

export default ProtectedGuard;
import DashboardLayout from "../layout/DashboardLayout/DashboardLayout";
import RootLayout from "../layout/RootLayout/RootLayout";
import AdminPanel from "../pages/AdminPanel/AdminPanel";
import LoginPanel from "../pages/loginPanel/LoginPanel";
import GuestGuard from "../guards/GuestGuard";
import ProtectedGuard from "../guards/ProtectedGuard";
import { createBrowserRouter } from "react-router-dom";
import Events from "../components/Events/Events";
import ViewDetails from "../components/ViewDetails/ViewDetails";

export const router = createBrowserRouter([
    {
        element: <RootLayout />,
        children: [
            {
                element: <GuestGuard />,
                children: [
                    {
                        path: "/",
                        Component: LoginPanel
                    }
                ]
            },

            {
                element: <DashboardLayout />,
                children: [
                    {
                        path: "/admin/dashboard",
                        Component: AdminPanel
                    },
                    {
                        path: "/admin/events",
                        Component: Events
                    },
                    {
                        path: "/events/1234",
                        Component: ViewDetails
                    }
                ]
            }
        ]
    }

])

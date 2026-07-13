import { Outlet } from "react-router-dom";
import Header from "../../components/GenericComponents/Header/Header";
import Sidebar from "../../components/GenericComponents/Sidebar/Sidebar";
import styles from "./DashboardLayout.module.scss";
import Footer from "../../components/GenericComponents/Footer/Footer";

const DashboardLayout = () => {
    return (
        <div className={styles.dashboardLayout}>

            <Sidebar />

            <div className={styles.mainContainer}>
                <Header />
                <main className={styles.content}>
                    <Outlet />
                </main>
                {/* <Footer children="Child" /> */}
            </div>

        </div>
    );
};

export default DashboardLayout;
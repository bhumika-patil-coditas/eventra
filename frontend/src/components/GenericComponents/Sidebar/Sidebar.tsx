import { NavLink } from "react-router-dom";
import { SidebarConfig } from "../../../config/Sidebar.config";
import styles from "./Sidebar.module.scss";

const Sidebar = () => {
    const role = "ADMIN";
    const menus = SidebarConfig[role];

    return (
        <div className={styles.sidebar}>
            <div className={styles.sidebarHeader}>
                <img className={styles.logo} src="/favicon.svg" alt="logo" />
                <h2>Eventra</h2>
            </div>
            <div className={styles.contents}>
                {menus.map(menu =>
                    <NavLink
                        to={menu.path}
                        className={({ isActive }) => isActive ? styles["active"] : styles.content}
                    >
                        {menu.label}
                    </NavLink>
                )}
            </div>
        </div>
    )
}

export default Sidebar;
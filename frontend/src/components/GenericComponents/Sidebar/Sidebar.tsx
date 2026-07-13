import { NavLink } from "react-router-dom";
import { SidebarConfig } from "../../../config/Sidebar.config";
import styles from "./Sidebar.module.scss";

const Sidebar = () => {
    const role = "ADMIN";
    const menus = SidebarConfig[role];

    return (
        <div className={styles.sidebar}>
            {/* {menus.map(menu =>
                <NavLink
                    to={menu.path}
                    className={({ isActive }) => isActive ? styles["active"] : ""}
                >
                    {menu.label}
                </NavLink>
            )} */}
        </div>
    )
}

export default Sidebar;
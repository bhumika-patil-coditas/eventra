import { useState } from "react";
import Button from "../../components/GenericComponents/Button/Button";
import styles from "./AdminPanel.module.scss";
import AddEventForm from "../../components/Admin/AddEventForm/AddEventForm";
import AddUserForm from "../../components/Admin/AddUserForm/AddUserForm";

const AdminPanel = () => {
    const [isAddEventPanelOpen, setIsAddEventPanelOpen] = useState(false);
    const [isAddUserPanelOpen, setIsAddUserPanelOpen] = useState(false);

    return (
        <div className={styles.mainPanel}>

            <div className={styles.actions}>
                <h2>Quick Actions</h2>
                <Button className="primary" children="Add Event" onClick={() => setIsAddEventPanelOpen(true)} />
                <Button className="primary" children="Add User" onClick={() => setIsAddUserPanelOpen(true)} />
            </div>

            <div>
                Admin
            </div>

            {isAddEventPanelOpen && <AddEventForm onClose={() => setIsAddEventPanelOpen(false)} />}
            {isAddUserPanelOpen && <AddUserForm onClose={() => setIsAddUserPanelOpen(false)} />}
        </div>
    )
}

export default AdminPanel;
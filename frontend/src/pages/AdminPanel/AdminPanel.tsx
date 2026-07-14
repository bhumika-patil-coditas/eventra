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

            <h2 className={styles.heading}>Welcome Admin!</h2>
            <div className={styles.countGrid}>
                <div className={styles.card}>
                    <h3>Total Vendors</h3>
                    <h1>30</h1>
                </div>
                <div className={styles.card}>
                    <h3>Total Organizers</h3>
                    <h1>50</h1>
                </div>
                <div className={styles.card}>
                    <h3>Total Events</h3>
                    <h1>20</h1>
                </div>
                <div className={styles.card}>
                    <h3>Total Reviewers</h3>
                    <h1>4</h1>
                </div>
            </div>

            <div className={styles.subcontainer}>
                <div className={styles.actions}>
                    <h3>Quick Actions</h3>
                    <Button className="primary" children="Add Event" onClick={() => setIsAddEventPanelOpen(true)} />
                    <Button className="primary" children="Add User" onClick={() => setIsAddUserPanelOpen(true)} />
                </div>

                <div>
                  
                </div>
            </div>




            {isAddEventPanelOpen && <AddEventForm onClose={() => setIsAddEventPanelOpen(false)} />}
            {isAddUserPanelOpen && <AddUserForm onClose={() => setIsAddUserPanelOpen(false)} />}
        </div>
    )
}

export default AdminPanel;
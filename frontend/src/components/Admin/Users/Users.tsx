import styles from "./Users.module.scss";
import Button from "../../GenericComponents/Button/Button";
import { useState } from "react";
import DeleteUser from "../DeleteUser/DeleteUser";
import AddUserForm from "../AddUserForm/AddUserForm";

const Users = () => {

    const [isDeletePanelOpen, setIsDeletePanelOpen] = useState("");
    const [isEditPanelOpen, setIsEditPanelOpen] = useState("");
    const events = [
        {
            id: "1234",
            name: "Bhumika Patil",
            email: "26/12/2025",
            role: "Organizer",
            contact: 7654543527
        },
        {
            id: "1234",
            name: "Deep Patil",
            email: "26/12/2025",
            role: "Vendor",
            contact: 7654543527
        },
        {
            id: "1234",
            name: "Yash Divekar",
            email: "26/12/2025",
            role: "Vendor",
            contact: 7654543527
        },
    ]


    return (
        <div className={styles.container}>
            <div className={styles.header}>
                <input type="text" placeholder="Search event" />
                <h2 className={styles.heading}>Users</h2>
                <Button children="Add User" className="secondary" />
            </div>

            <div className={styles.grid}>
                {events.map(event =>
                    <div key={event.id} className={styles.card}>
                        <div className={styles.statusSection}>
                            <h3 className={styles.subheading}>{event.name}</h3>
                            <Button className="status" children={event.role} />
                        </div>
                        <p>Email: {event.email}</p>
                        <p>Contact: {event.contact}</p>

                        <div className={styles.btnSection}>
                            <Button onClick={() => setIsEditPanelOpen(event.id)} className="tertiary" children="Edit User" />
                            <Button onClick={() => setIsDeletePanelOpen(event.id)} className="danger" children="Delete User" />
                        </div>
                    </div>
                )}
            </div>
            {isDeletePanelOpen && <DeleteUser onClose={() => setIsDeletePanelOpen("")} id={isDeletePanelOpen} />}
            {isEditPanelOpen && <AddUserForm onClose={() => setIsEditPanelOpen("")} id={isEditPanelOpen} />}
        </div>
    )
}

export default Users;
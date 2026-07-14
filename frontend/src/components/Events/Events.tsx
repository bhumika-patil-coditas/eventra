import { useNavigate } from "react-router-dom";
import Button from "../GenericComponents/Button/Button";
import styles from "./Events.module.scss";
import { useState } from "react";
import AddEventForm from "../Admin/AddEventForm/AddEventForm";
import FormInput from "../GenericComponents/FormInput/FormInput";

const Events = () => {

    const events = [
        {
            id: "1234",
            name: "Coditas Clap",
            date: "26/12/2025",
            location: "Pune",
            requirements: "Anything",
            budget_upper: "15000",
            budget_lower: "2000",
            status: "OPEN",
            reviewer_summery: ""
        },
        {
            id: "2345",
            name: "CBL 2025",
            date: "26/12/2025",
            location: "Pune",
            requirements: "Anything",
            budget_upper: "10000",
            budget_lower: "2000",
            status: "OPEN",
            reviewer_summery: ""
        },
        {
            id: "4567",
            name: "CPL 2026",
            date: "26/12/2025",
            location: "Pune",
            requirements: "Anything",
            budget_upper: "10000",
            budget_lower: "2000",
            status: "OPEN",
            reviewer_summery: ""
        },
        {
            id: "9567",
            name: "YDB Project",
            date: "26/12/2025",
            location: "Pune",
            requirements: "Anything",
            budget_upper: "10000",
            budget_lower: "2000",
            status: "OPEN",
            reviewer_summery: ""
        },
    ]

    const navigate = useNavigate();
    const [isAddEventPanelOpen, setIsAddEventPanelOpen] = useState(false);


    return (
        <div className={styles.container}>
            <div className={styles.header}>
                <input type="text" placeholder="Search event" />
                <h2 className={styles.heading}>Events</h2>
                <Button className="secondary" children="Add Event" onClick={() => setIsAddEventPanelOpen(true)} />
            </div>

            <div className={styles.grid}>
                {events.map(event =>
                    <div key={event.id} className={styles.card}>
                        <h3 className={styles.subheading}>{event.name}</h3>
                        <div className={styles.statusSection}>
                            <p>Location: {event.location}</p>
                            <Button className="status" children={event.status} />
                        </div>
                        <p>Date: {event.date}</p>
                        <p>Requirements: {event.requirements}</p>
                        <p><span>Budget: {event.budget_lower} - {event.budget_upper}</span></p>
                        <Button onClick={() => navigate(`/events/${event.id}`)} className="primary" children="View Details" />
                    </div>
                )}
            </div>
            {isAddEventPanelOpen && <AddEventForm onClose={() => setIsAddEventPanelOpen(false)} />}

        </div>
    )
}

export default Events;
import { useNavigate } from "react-router-dom";
import Button from "../GenericComponents/Button/Button";
import styles from "./ViewDetails.module.scss";
import { useState } from "react";
import Form from "../GenericComponents/Form/Form";
import { Controller, useForm } from "react-hook-form";
import { useChangeEventStatusMutation } from "../../redux/services/organizer.services";

const ViewDetails = () => {

    const navigate = useNavigate();
    const [isProposalOpen, setIsProposalOpen] = useState(false);
    const [changeEventStatus] = useChangeEventStatusMutation();

    const { handleSubmit, control } = useForm({
        defaultValues: {
            proposal: ""
        },
    });

    const onSubmit = async () => {
        try {
            // const res = await changeEventStatus("open").unwrap()
        } catch (error) {
            throw error;
        }
    }

    const event = {
        id: "2345",
        name: "CBL 2025",
        date: "26/12/2025",
        location: "Pune",
        requirements: "Anything",
        budget_upper: "10000",
        budget_lower: "2000",
        status: "OPEN",
        reviewer_summery: [
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsam id et aliquid odio quisquam alias corporis similique temporibus libero eligendi voluptatibus illo, fuga itaque praesentium animi fugit neque repudiandae excepturi.",

            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsam id et aliquid odio quisquam alias corporis similique temporibus libero eligendi voluptatibus illo, fuga itaque praesentium animi fugit neque repudiandae excepturi.",
        ]
    }

    return (
        <div className={styles.container}>

            <div className={styles.subcontainer}>

                <div className={styles.topheading}>
                    <Button onClick={() => navigate("/admin/events")} className="secondary" children="Back" />
                    <h2 className={styles.subheading}>{event.name}</h2>

                    <div className={styles.btnSection}>
                        <Button className="status" children={event.status} />
                        <Button
                            onClick={() => setIsProposalOpen(true)}
                            className="secondary"
                            children="Proposal"
                        />
                    </div>

                    {isProposalOpen && (
                        <div className={styles.form}>
                            <div className={styles.close}>
                                <Button
                                    onClick={() => setIsProposalOpen(false)}
                                    className="danger"
                                    children="X"
                                />
                            </div>

                            <Form onSubmit={handleSubmit(onSubmit)}>

                                {/* Checkboxes */}
                                <Controller
                                    control={control}
                                    name="services"
                                    defaultValue={[]}
                                    render={({ field }) => (
                                        <div className={styles.checkboxGroup}>
                                            {["Catering", "Management", "Decor"].map((service) => (
                                                <label key={service}>
                                                    <input
                                                        type="checkbox"
                                                        value={service}
                                                        checked={field.value?.includes(service)}
                                                        onChange={(e) => {
                                                            if (e.target.checked) {
                                                                field.onChange([...field.value, service]);
                                                            } else {
                                                                field.onChange(
                                                                    field.value.filter((item:any) => item !== service)
                                                                );
                                                            }
                                                        }}
                                                    />
                                                    {service}
                                                </label>
                                            ))}
                                        </div>
                                    )}
                                />

                                {/* Proposal textarea */}
                                <Controller
                                    control={control}
                                    name="proposal"
                                    render={({ field }) => (
                                        <textarea
                                            {...field}
                                            rows={5}
                                            placeholder="Enter proposal description"
                                        />
                                    )}
                                />

                                <Button
                                    type="submit"
                                    className="primary"
                                    children="Submit"
                                />
                            </Form>
                        </div>
                    )}
                </div>

                <p>Date: {event.date}</p>
                <p>Location: {event.location}</p>
                <p>Requirements: {event.requirements}</p>
                <p><span>Budget: {event.budget_lower} - {event.budget_upper}</span></p>
                <p>Summary:
                    <ol>
                        {event.reviewer_summery?.map(data =>
                            <li className={styles.list}>{data}</li>
                        )}
                    </ol>
                </p>
            </div>
        </div>
    )
}

export default ViewDetails;
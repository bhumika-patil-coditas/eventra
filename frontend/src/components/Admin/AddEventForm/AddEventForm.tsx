import { Controller, useForm } from "react-hook-form";
import Button from "../../GenericComponents/Button/Button";
import Form from "../../GenericComponents/Form/Form";
import Modal from "../../GenericComponents/Modal/Modal";
import FormInput from "../../GenericComponents/FormInput/FormInput";
import type { AddEventFormProps } from "./AddEventForm.types";
import { useState } from "react";

const AddEventForm = ({ onClose }: AddEventFormProps) => {

    const { handleSubmit, control, formState: { errors } } = useForm({
        defaultValues: {
            name: "",
            date: "",
            location: "",
            requirements: "",
            budget_upper: 0,
            budget_lower: 0,
            status: "",
            file: []
        },
    });

    const onSubmit = () => {

    }

    return (
        <Modal>
            <Modal.ModalHeading>
                <h2>Add Event</h2>
                <Button onClick={onClose} className="danger" children="X" />
            </Modal.ModalHeading>

            <div>
                <Form onSubmit={handleSubmit(onSubmit)}>
                    <Controller
                        control={control}
                        name="name"
                        render={({ field }) => (
                            <FormInput
                                {...field}
                                type="text"
                                placeholder="Enter event name"
                            />
                        )}
                    />

                    <Controller
                        control={control}
                        name="date"
                        render={({ field }) => (
                            <FormInput
                                {...field}
                                type="date"
                                placeholder="Choose event date"
                            />
                        )}
                    />

                    <Controller
                        control={control}
                        name="location"
                        render={({ field }) => (
                            <FormInput
                                {...field}
                                type="text"
                                placeholder="Choose event location"
                            />
                        )}
                    />

                    <Controller
                        control={control}
                        name="requirements"
                        render={({ field }) => (
                            <FormInput
                                {...field}
                                type="text"
                                placeholder="Choose event requirements"
                            />
                        )}
                    />

                    <Controller
                        control={control}
                        name="budget_upper"
                        render={({ field }) => (
                            <FormInput
                                {...field}
                                type="text"
                                placeholder="Choose event upper budget"
                            />
                        )}
                    />
                    <Controller
                        control={control}
                        name="budget_lower"
                        render={({ field }) => (
                            <FormInput
                                {...field}
                                type="text"
                                placeholder="Choose event lower budget"
                            />
                        )}
                    />

                    <Controller
                        control={control}
                        name="status"
                        render={({ field }) => (
                            <FormInput
                                {...field}
                                type="text"
                                placeholder="Choose event status"
                            />
                        )}
                    />

                    <Button type="submit" className="primary" children="Add Event" />
                </Form>
            </div>
        </Modal>
    )
}
export default AddEventForm;
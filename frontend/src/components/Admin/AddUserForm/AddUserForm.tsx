import { Controller, useForm } from "react-hook-form";
import Button from "../../GenericComponents/Button/Button";
import Form from "../../GenericComponents/Form/Form";
import Modal from "../../GenericComponents/Modal/Modal";
import FormInput from "../../GenericComponents/FormInput/FormInput";
import type { AddUserFormProps } from "./AddUserForm.types";
import { useAddUserMutation, useEditUserMutation } from "../../../redux/services/admin.services";

const AddUserForm = ({ onClose, id }: AddUserFormProps) => {

    const [addUser] = useAddUserMutation();
    const [editUser] = useEditUserMutation();

    const { handleSubmit, control } = useForm({
        defaultValues: {
            name: "",
            email: "",
            role: ""
        },
    });

    interface Role {
        name: string,
        email: string,
        role: string
    }

    const onSubmit = async (data: Role) => {
        if (id) {editUser

        } else {
            
        }

    }

    return (
        <Modal>
            <Modal.ModalHeading>
                <h2>Add User</h2>
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
                                placeholder="Enter user name"
                            />
                        )}
                    />

                    <Controller
                        control={control}
                        name="email"
                        render={({ field }) => (
                            <FormInput
                                {...field}
                                type="text"
                                placeholder="Enter user email"
                            />
                        )}
                    />

                    <Controller
                        control={control}
                        name="role"
                        render={({ field }) => (
                            <FormInput
                                {...field}
                                type="text"
                                placeholder="Choose role"
                            />
                        )}
                    />

                    <Button type="submit" className="primary" children="Add User" />
                </Form>
            </div>
        </Modal>
    )
}
export default AddUserForm;
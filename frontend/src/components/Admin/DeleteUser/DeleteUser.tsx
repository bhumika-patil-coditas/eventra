import Button from "../../GenericComponents/Button/Button";
import Modal from "../../GenericComponents/Modal/Modal";
import { useDeleteUserMutation } from "../../../redux/services/admin.services";
import type { DeleteUserProps } from "./DeleteUser.types";
import styles from "./DeleteUser.module.scss";

const DeleteUser = ({ id, onClose }: DeleteUserProps) => {

    const [deleteUser] = useDeleteUserMutation();

    const handleDeleteUser = async () => {
        try {
            const res = await deleteUser(id).unwrap();
        } catch (error) {
            throw error;
        }
    }

    return (
        <Modal>
            <Modal.ModalHeading>
                <h2>Delete User</h2>
                <Button onClick={onClose} className="danger" children="X" />
            </Modal.ModalHeading>

            <div className={styles.deleteSection}>
                <h2>Are you sure?</h2>
                <Button onClick={onClose} className="secondary" children="Cancel" />
                <Button onClick={handleDeleteUser} className="danger" children="Delete" />
            </div>
        </Modal>
    )
}
export default DeleteUser;
import styles from "./Modal.module.scss";
import type { ModalProps } from "./Modal.types";

const Modal = ({ children }: ModalProps) => {
    return (
        <div className={styles.modal}>
            <div className={styles.modalForm}>
                {children}
            </div>
        </div>
    )
}

Modal.ModalHeading = ({ children }: ModalProps) => {
    return (
        <div className={styles.headingSection}>
            {children}
        </div>
    )
}

export default Modal;
import type { FormProps } from "./Form.types";
import styles from "./Form.module.scss";

const Form = ({ children , ...props}: FormProps) => {
    return <form className={styles.form} {...props}>{children}</form>
}

export default Form;
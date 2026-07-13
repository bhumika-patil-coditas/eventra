import type { FormInputProps } from "./FormInput.types";
import styles from "./FormInput.module.scss";

const FormInput = ({ placeholder, type, ...props }: FormInputProps) => {
    return (
        <input
            {...props}
            className={styles.input}
            placeholder={placeholder}
            type={type}
        />
    )
}
export default FormInput;
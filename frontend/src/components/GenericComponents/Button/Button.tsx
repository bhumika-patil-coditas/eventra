import type { ButtonProps } from "./Button.types"
import styles from "./Button.module.scss";

const Button = ({ children, className, ...props }: ButtonProps) => {
    return <button className={[styles.btn, styles[className]].join(" ")} {...props}>{children}</button>
}

export default Button;

import type { ButtonProps } from "./Button.types"
import styles from "./Button.module.scss";

const Button = ({ children, className }: ButtonProps) => {
    return <button className={[styles.btn, styles[className]].join(" ")}>{children}</button>
}

export default Button;

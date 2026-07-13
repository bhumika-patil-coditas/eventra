import type { FormProps } from "./Form.types";

const Form = ({ children }: FormProps) => {
    return <form>{children}</form>
}

export default Form;
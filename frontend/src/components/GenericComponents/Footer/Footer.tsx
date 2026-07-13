import type { FooterProps } from "./Footer.types";

const Footer = ({ children }: FooterProps) => {
    return (
        <footer>{children}</footer>
    )
}

export default Footer;
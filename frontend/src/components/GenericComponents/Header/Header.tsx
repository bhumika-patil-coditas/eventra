import Button from "../Button/Button";
import styles from "./Header.module.scss";

const Header = () => {
    return (
        <header className={styles.header}>
            <Button className="danger" children="Logout" />
        </header>
    )
}
export default Header;
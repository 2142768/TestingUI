import logo from "../assets/designs/Logo Color.png";
import styles from "../styles/Header.module.css";

function Header({ onClose }) {
  return (
    <>
      <header className={styles.header}>
        <div className={styles.logo}>
          <img src={logo} alt="Responsible AI" />
        </div>
        <div className={styles.actions}>
          <button className={styles.actionButton} onClick={onClose}>
            X
          </button>
        </div>
      </header>
    </>
  );
}

export default Header;

import styles from "../styles/FloatingButton.module.css";
import logo from "../assets/designs/Logo Color.png";

function FloatingButton({ onClick }) {
  return (
    <button className={styles.floatingButton} onClick={onClick}>
      <img src={logo} alt="Responsible AI" />
    </button>
  );
}

export default FloatingButton;

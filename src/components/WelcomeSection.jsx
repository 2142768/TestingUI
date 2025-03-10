import styles from "../styles/WelcomeSection.module.css";
import WelcomeLogo from "../assets/images/WelcomeLogo.png";

function WelcomeSection() {
  return (
    <div className={styles.welcomeSection}>
      <img
        src={WelcomeLogo}
        alt="AI Assistant"
        className={styles.assistantIcon}
      />
      <h2>Hi, Divyanshu</h2>
      <h1>How can I help you today?</h1>
    </div>
  );
}

export default WelcomeSection;

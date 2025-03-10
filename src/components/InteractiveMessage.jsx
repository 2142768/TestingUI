import styles from "../styles/InteractiveMessage.module.css";
import Radio from "../assets/images/Radio.png";

function InteractiveMessage({ content, options, onSelect }) {
  return (
    <div className={styles.interactiveMessage}>
      <div className={styles.content}>
        <img src={Radio} alt="Radio" className={styles.contentIcon} />
        <p className={styles.messageContent}>{content}</p>
      </div>

      <div className={styles.options}>
        {options.map((option, index) => (
          <label key={index} className={styles.optionLabel}>
            <input
              type="radio"
              name="aiOptions"
              value={option}
              onChange={() => onSelect(option)}
              className={styles.radioInput}
            />
            {option}
          </label>
        ))}
      </div>
    </div>
  );
}

export default InteractiveMessage;

import { useState } from "react";
import styles from "../styles/ChatInput.module.css";
import Upload from "../assets/images/Upload.png";
import AskRAI from "../assets/images/AskRai.png";

function ChatInput({ onSendMessage }) {
  const [message, setMessage] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (message.trim()) {
      onSendMessage(message);
      setMessage("");
    }
  };

  return (
    <form className={styles.container} onSubmit={handleSubmit}>
      <img src={Upload} alt="" className={styles.icon} />
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Ask me anything..."
        className={styles.input}
      />
      <button type="submit" className={styles.button}>
        <img src={AskRAI} alt="Ask" className={styles.buttonIcon} />
        Ask RAI
      </button>
    </form>
  );
}

export default ChatInput;

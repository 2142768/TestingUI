import styles from "../styles/ChatMessage.module.css";
import InteractiveMessage from "./InteractiveMessage";
import AiMessage from "../assets/images/AIMessage.png";

function ChatMessage({ message, onSelectOption }) {
  return (
    <div
      className={
        message.isUser ? styles.userMessageContainer : styles.aiMessageContainer
      }
    >
      <div className={message.isUser ? styles.userMessage : styles.aiMessage}>
        <div className={styles.messageHeader}>
          {!message.isUser && (
            <img src={AiMessage} alt="RAI Assist" className={styles.icon} />
          )}
          <span className={message.isUser ? styles.name : styles.aiName}>
            {message.isUser ? "You" : "RAI Assist"}
          </span>
          <span className={styles.timestamp}>{message.timestamp}</span>
        </div>
        {message.options ? (
          <InteractiveMessage
            content={message.content}
            options={message.options}
            onSelect={onSelectOption}
          />
        ) : (
          <p className={styles.messageContent}>{message.content}</p>
        )}
      </div>
    </div>
  );
}

export default ChatMessage;

import styles from "../styles/ExampleQuestions.module.css";

function QuestionCard({
  icon,
  title,
  description,
  messages,
  setMessages,
  chatStarted,
  setChatStarted,
  setLoading,
  formatTime,
}) {
  const handleMessage = () => {
    if (!chatStarted) setChatStarted(true);
    const userMessage = {
      id: messages.length + 1,
      content: title,
      timestamp: formatTime(new Date()),
      isUser: true,
    };

    setMessages((prev) => [...prev, userMessage]);

    // Simulate AI response
    setLoading(true);
    setTimeout(() => {
      const aiMessage = {
        id: messages.length + 2,
        content: `Response to: ${title}`,
        timestamp: formatTime(new Date()),
        isUser: false,
      };
      setMessages((prev) => [...prev, aiMessage]);
      setLoading(false);
    }, 1000);
  };

  return (
    <div className={styles.card} onClick={handleMessage}>
      <img src={icon} alt="" className={styles.icon} />
      <h3 className={styles.cardTitle}>{title}</h3>
      <p className={styles.description}>{description}</p>
    </div>
  );
}

export default QuestionCard;

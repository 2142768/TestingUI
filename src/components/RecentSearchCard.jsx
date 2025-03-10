import styles from "../styles/RecentSearches.module.css";

const RecentSearchCard = ({
  icon,
  searchText,
  messages,
  setMessages,
  chatStarted,
  setChatStarted,
  setLoading,
  formatTime,
}) => {
  const handleMessage = () => {
    if (!chatStarted) setChatStarted(true);
    const userMessage = {
      id: messages.length + 1,
      content: searchText,
      timestamp: formatTime(new Date()),
      isUser: true,
    };

    setMessages((prev) => [...prev, userMessage]);

    // Simulate AI response
    setLoading(true);
    setTimeout(() => {
      const aiMessage = {
        id: messages.length + 2,
        content: `Response to: ${searchText}`,
        timestamp: formatTime(new Date()),
        isUser: false,
      };
      setMessages((prev) => [...prev, aiMessage]);
      setLoading(false);
    }, 1000);
  };

  return (
    <div className={styles.searchItem} onClick={handleMessage}>
      <img src={icon} alt="" className={styles.searchIcon} />
      <span className={styles.searchText}>{searchText}</span>
    </div>
  );
};

export default RecentSearchCard;

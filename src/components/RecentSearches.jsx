import styles from "../styles/RecentSearches.module.css";
import RecentSearchCard from "./RecentSearchCard";
import RecentSearch from "../assets/images/RecentSearches.png";

const recentSearches = [
  {
    icon: RecentSearch,
    searchText: "Figma ipsum component variant main layer. Star underli...",
  },
  {
    icon: RecentSearch,
    searchText: "Figma ipsum component variant main layer. Star underli...",
  },
  {
    icon: RecentSearch,
    searchText: "Figma ipsum component variant main layer. Star underli...",
  },
  {
    icon: RecentSearch,
    searchText: "Figma ipsum component variant main layer. Star underli...",
  },
];

function RecentSearches({
  messages,
  setMessages,
  chatStarted,
  setChatStarted,
  setLoading,
  formatTime,
}) {
  return (
    <div className={styles.recentSearches}>
      <div className={styles.sectionHeader}>
        <h2 className={styles.title}>Recent Searches:</h2>
        <button className={styles.seeAll}>See All</button>
      </div>
      <div className={styles.searchesList}>
        {recentSearches.map((search, index) => (
          <RecentSearchCard
            key={index}
            icon={search.icon}
            searchText={search.searchText}
            messages={messages}
            setMessages={setMessages}
            chatStarted={chatStarted}
            setChatStarted={setChatStarted}
            setLoading={setLoading}
            formatTime={formatTime}
          />
        ))}
      </div>
    </div>
  );
}

export default RecentSearches;

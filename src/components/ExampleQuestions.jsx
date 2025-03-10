import styles from "../styles/ExampleQuestions.module.css";
import QuestionCard from "./QuestionCard";
import ExampleQuestion from "../assets/images/ExampleQuestion.png";

const questions = [
  {
    icon: ExampleQuestion,
    title: "How can RAIQA help me?",
    description:
      "Figma ipsum component variant main layer. Prototype project object export stroke blur pixel overflow pen.",
  },
  {
    icon: ExampleQuestion,
    title: "Get started with Responsible AI assessment on testing front",
    description:
      "Figma ipsum component variant main layer. Prototype project object export...",
  },
  {
    icon: ExampleQuestion,
    title: "Frequent FAQs",
    description:
      "Figma ipsum component variant main layer. Prototype project object export stroke blur pixel overflow pen.",
  },
];

function ExampleQuestions({
  messages,
  setMessages,
  chatStarted,
  setChatStarted,
  setLoading,
  formatTime,
}) {
  return (
    <div className={styles.container}>
      <h2 className={styles.title}>Example Questions:</h2>
      <p className={styles.subtitle}>
        Use of one of the most common Questions below or use your own to begin
      </p>
      <div className={styles.grid}>
        {questions.map((ques, index) => (
          <QuestionCard
            key={index}
            icon={ques.icon}
            title={ques.title}
            description={ques.description}
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

export default ExampleQuestions;

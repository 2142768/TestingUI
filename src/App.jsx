import { useState, useRef, useEffect } from "react";
import Header from "./components/Header";
import WelcomeSection from "./components/WelcomeSection";
import ExampleQuestions from "./components/ExampleQuestions";
import RecentSearches from "./components/RecentSearches";
import ChatInput from "./components/ChatInput";
import ChatMessage from "./components/ChatMessage";
import FloatingButton from "./components/FloatingButton";
import styles from "./styles/App.module.css";
import Hourglass from "./assets/images/Hourglass.png";
import Search from "./assets/images/Search.png";
import Done from "./assets/images/Done.png";
import AiMessage from "./assets/images/AIMessage.png";

function App() {
  const formatTime = (date) => {
    const options = { hour: "2-digit", minute: "2-digit", hour12: true };
    return new Intl.DateTimeFormat("en-US", options).format(date);
  };

  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([]);
  const [chatStarted, setChatStarted] = useState(false);
  const [loading, setLoading] = useState(false); // Loading state
  const messagesEndRef = useRef(null); // Create a ref for the messages container
  const [currentQuestion, setCurrentQuestion] = useState("");
  const [currentQuestionNumber, setCurrentQuestionNumber] = useState("");

  const [socket, setSocket] = useState(null);

  useEffect(() => {
    // Create a new WebSocket connection
    const ws = new WebSocket("ws://localhost:8000/ws");

    // Set WebSocket instance in state
    setSocket(ws);

    // Listen for messages
    ws.onmessage = (event) => {
      // setLoading(true);

      setLoading(false);

      setCurrentQuestion(JSON.parse(event.data).current_question);
      setCurrentQuestionNumber(JSON.parse(event.data).question_no);
      let aiMessage = {
        id: messages.length + 2,
        content: JSON.parse(event.data).current_question,
        timestamp: formatTime(new Date()),
        isUser: false,
      };

      setMessages((prev) => [...prev, aiMessage]);
    };

    // Log any errors
    ws.onerror = (error) => {
      console.error("WebSocket Error:", error);
    };

    // Handle WebSocket close event
    ws.onclose = () => {
      console.log("WebSocket connection closed");
    };

    // Clean up when component unmounts
    return () => {
      ws.close();
    };
  }, []);

  const handleOpen = () => setIsOpen(true);
  const handleClose = () => setIsOpen(false);

  const handleSendMessage = (message) => {
    if (!chatStarted) setChatStarted(true);

    if (socket && message) {
      let data = {
        current_question: currentQuestion,
        current_response: message,
        question_type: "general",
        question_sub_type: "general",
        question_no: currentQuestionNumber
      }
      setLoading(true);
      socket.send(JSON.stringify(data));
      const userMessage = {
        id: messages.length + 1,
        content: message,
        timestamp: formatTime(new Date()),
        isUser: true,
      };

      setMessages((prev) => [...prev, userMessage]);
    }
  };

  const handleSelectOption = (option) => {
    const userMessage = {
      id: messages.length + 1,
      content: option,
      timestamp: formatTime(new Date()),
      isUser: true,
    };

    setMessages((prev) => [...prev, userMessage]);

    // Simulate AI response
    setLoading(true);
    setTimeout(() => {
      const aiMessage = {
        id: messages.length + 2,
        content: `You selected: ${option}`,
        timestamp: formatTime(new Date()),
        isUser: false,
      };
      setMessages((prev) => [...prev, aiMessage]);
      setLoading(false);
    }, 1000);
  };

  // Scroll to the bottom of the messages when a new message is added
  useEffect(() => {
    if (messagesEndRef.current) {
      messagesEndRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [messages]);

  if (!isOpen) {
    return <FloatingButton onClick={handleOpen} />;
  }

  return (
    <div className={styles.appOverlay}>
      <Header onClose={handleClose} />

      <div className="app-container">
        <main className="main-content">
          {!chatStarted && (
            <div className={styles.preChatContent}>
              <WelcomeSection />
              <ChatMessage message={messages[0]} />
              <ExampleQuestions
                messages={messages}
                setMessages={setMessages}
                chatStarted={chatStarted}
                setChatStarted={setChatStarted}
                setLoading={setLoading}
                formatTime={formatTime}
              />
              <RecentSearches
                messages={messages}
                setMessages={setMessages}
                chatStarted={chatStarted}
                setChatStarted={setChatStarted}
                setLoading={setLoading}
                formatTime={formatTime}
              />
            </div>
          )}
          {chatStarted && (
            <div className={styles.messages}>
              {messages.map((msg) => (
                <ChatMessage
                  key={msg.id}
                  message={msg}
                  onSelectOption={handleSelectOption}
                />
              ))}
              {loading && (
                <div className={styles.loader}>
                  <div className={styles.messageHeader}>
                    <img
                      src={AiMessage}
                      alt="RAI Assist"
                      className={styles.icon}
                    />

                    <span className={styles.aiName}>RAI Assist</span>
                  </div>

                  <span className={styles.loaderText}>
                    <img src={Hourglass} alt="Hourglass" /> Understanding
                    requirement..
                  </span>
                  <span className={styles.loaderText}>
                    <img src={Search} alt="Search" /> Looking into relevant
                    questions..
                  </span>
                  <span className={styles.loaderText}>
                    <img src={Done} alt="Done" /> Wait a moment, Let's Go
                  </span>
                </div>
              )}
              <div ref={messagesEndRef} />
            </div>
          )}
          <ChatInput onSendMessage={handleSendMessage} />
        </main>
      </div>
    </div>
  );
}

export default App;

import React from 'react';
import { useChat } from '../../hooks/useChat';
import ChatHistory from './ChatHistory';
import MessageInput from './MessageInput';
import '../../styles/chat.css';

interface ChatWindowProps {
  bookId?: string;
  title?: string;
}

const ChatWindow: React.FC<ChatWindowProps> = ({ bookId, title = 'Chat with Book' }) => {
  const {
    messages,
    sendMessage,
    isLoading,
    error,
    sessionId,
    startNewSession
  } = useChat({ bookId });

  // Initialize session on component mount if we have a bookId
  React.useEffect(() => {
    if (bookId && !sessionId) {
      startNewSession(bookId);
    }
  }, [bookId, sessionId, startNewSession]);

  return (
    <div className="chat-container">
      <div className="chat-header">
        {title} {bookId && `for Book: ${bookId.substring(0, 12)}...`} {sessionId ? `(Session: ${sessionId.substring(0, 8)}...)` : ''}
      </div>

      {error && (
        <div className="chat-error">
          Error: {error}
        </div>
      )}

      <ChatHistory messages={messages} sessionId={sessionId} />

      {isLoading && (
        <div className="loading-indicator">
          <div className="loading-spinner" aria-label="Loading..."></div>
        </div>
      )}

      <MessageInput
        onSendMessage={sendMessage}
        isLoading={isLoading}
        placeholder={`Ask about ${bookId ? 'this book' : 'the content'}...`}
      />
    </div>
  );
};

export default ChatWindow;
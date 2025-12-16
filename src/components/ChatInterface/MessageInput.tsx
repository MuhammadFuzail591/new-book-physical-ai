import React, { useState, KeyboardEvent } from 'react';
import '../../styles/chat.css';

interface MessageInputProps {
  onSendMessage: (message: string) => void;
  isLoading: boolean;
  placeholder?: string;
}

const MessageInput: React.FC<MessageInputProps> = ({
  onSendMessage,
  isLoading,
  placeholder = 'Type your message...'
}) => {
  const [message, setMessage] = useState<string>('');

  const handleSubmit = () => {
    if (message.trim() && !isLoading) {
      onSendMessage(message.trim());
      setMessage('');
    }
  };

  const handleKeyDown = (e: KeyboardEvent<HTMLTextAreaElement>) => {
    // Submit on Enter (but allow Shift+Enter for new line)
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  return (
    <div className="chat-input-area" role="form" aria-label="Chat message input">
      <textarea
        className="chat-input"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        onKeyDown={handleKeyDown}
        placeholder={placeholder}
        disabled={isLoading}
        rows={1}
        aria-label="Type your message"
        aria-disabled={isLoading}
        autoComplete="off"
        maxLength={1000} // Assuming max length from config
      />
      <button
        className="send-button"
        onClick={handleSubmit}
        disabled={isLoading || !message.trim()}
        aria-label={isLoading ? "Sending message" : "Send message"}
      >
        {isLoading ? 'Sending...' : 'Send'}
      </button>
    </div>
  );
};

export default MessageInput;
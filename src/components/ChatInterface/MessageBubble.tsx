import React from 'react';
import { ChatMessage } from '../../services/types/chat-types';
import '../../styles/chat.css';

interface MessageBubbleProps {
  message: ChatMessage;
}

const MessageBubble: React.FC<MessageBubbleProps> = ({ message }) => {
  const messageClass = `message-bubble ${message.sender} ${message.status === 'error' ? 'error' : ''}`;

  // Format timestamp for display
  const formatTime = (date: Date) => {
    return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  };

  return (
    <div className={messageClass} aria-label={`Message from ${message.sender}: ${message.content}`}>
      <div className="message-content" role="text">
        <pre style={{
          whiteSpace: 'pre-wrap',
          wordWrap: 'break-word',
          fontFamily: 'inherit',
          margin: 0,
          padding: 0,
          backgroundColor: 'transparent',
          border: 'none'
        }}>
          {message.content}
        </pre>
      </div>
      <div className="message-info">
        <span className="message-sender" aria-hidden="true">
          {message.sender === 'user' ? 'You' : 'BookBot'} •
        </span>{' '}
        {formatTime(message.timestamp)}
        {message.status && (
          <span className="message-status" aria-label={`Status: ${message.status}`}>
            {message.status === 'error' ? '❌' : message.status === 'delivered' ? '✓' : '...'}
          </span>
        )}
      </div>
    </div>
  );
};

export default MessageBubble;
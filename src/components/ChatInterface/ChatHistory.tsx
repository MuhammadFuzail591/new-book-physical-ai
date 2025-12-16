import React, { useEffect, useRef } from 'react';
import { ChatMessage } from '../../services/types/chat-types';
import MessageBubble from './MessageBubble';
import '../../styles/chat.css';

interface ChatHistoryProps {
  messages: ChatMessage[];
  sessionId?: string | null;
  onSessionHistoryLoaded?: (messages: ChatMessage[]) => void;
}

const ChatHistory: React.FC<ChatHistoryProps> = ({
  messages,
  sessionId,
  onSessionHistoryLoaded
}) => {
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const chatContainerRef = useRef<HTMLDivElement>(null);

  // Auto-scroll to bottom when messages change
  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    // Use instant scroll when new messages arrive for real-time experience
    messagesEndRef.current?.scrollIntoView({ behavior: 'instant' });
  };

  // Function to check if user is scrolled near bottom
  const isScrolledToBottom = () => {
    if (!chatContainerRef.current) return true;
    const { scrollTop, scrollHeight, clientHeight } = chatContainerRef.current;
    return scrollHeight - scrollTop - clientHeight < 50; // 50px threshold
  };

  // Scroll to bottom only if user is already at the bottom
  useEffect(() => {
    if (isScrolledToBottom()) {
      scrollToBottom();
    }
  }, [messages]);

  return (
    <div className="chat-messages" ref={chatContainerRef}>
      {messages.length === 0 ? (
        <div className="no-messages">
          {sessionId ? 'Loading conversation history...' : 'No messages yet. Start a conversation!'}
        </div>
      ) : (
        messages.map((message) => (
          <MessageBubble key={message.id} message={message} />
        ))
      )}
      <div ref={messagesEndRef} />
    </div>
  );
};

export default ChatHistory;
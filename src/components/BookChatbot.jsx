import React from 'react';
import ChatWindow from './ChatInterface/ChatWindow';
import '../styles/chat.css';

// A Docusaurus-compatible chatbot component that can be embedded in MDX pages
const BookChatbot = ({ bookId, title = "Ask about this chapter" }) => {
  // Extract book ID from the current page if not provided
  const currentBookId = bookId || typeof window !== 'undefined'
    ? window.location.pathname.split('/').filter(Boolean).pop() || 'default-book'
    : 'default-book';

  return (
    <div style={{ marginTop: '2rem', marginBottom: '2rem' }}>
      <ChatWindow bookId={currentBookId} title={title} />
    </div>
  );
};

export default BookChatbot;
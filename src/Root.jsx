import React, { useState, useEffect } from 'react';
import BookChatbot from '../components/BookChatbot';

// Root component that wraps the entire application
const Root = ({ children }) => {
  const [showChatbot, setShowChatbot] = useState(false);
  const [isChatbotReady, setIsChatbotReady] = useState(false);

  // Determine if we should show the chatbot based on the current route
  useEffect(() => {
    const shouldShow = !window.location.pathname.includes('/api/') &&
                      !window.location.pathname.includes('/sitemap') &&
                      !window.location.pathname.includes('/feed');
    setIsChatbotReady(shouldShow);
  }, []);

  // Toggle function for chatbot visibility
  const toggleChatbot = () => {
    setShowChatbot(!showChatbot);
  };

  return (
    <div style={{ position: 'relative' }}>
      {/* Main content */}
      {children}

      {/* Floating chatbot button */}
      {isChatbotReady && (
        <div
          style={{
            position: 'fixed',
            bottom: '20px',
            right: '20px',
            zIndex: 1000,
          }}
        >
          {!showChatbot && (
            <button
              onClick={toggleChatbot}
              style={{
                backgroundColor: '#007bff',
                color: 'white',
                border: 'none',
                borderRadius: '50%',
                width: '60px',
                height: '60px',
                fontSize: '24px',
                cursor: 'pointer',
                boxShadow: '0 4px 8px rgba(0,0,0,0.3)',
              }}
              aria-label="Open chatbot"
            >
              💬
            </button>
          )}

          {showChatbot && (
            <div
              style={{
                width: '350px',
                height: '500px',
                border: '1px solid #ddd',
                borderRadius: '8px',
                boxShadow: '0 4px 12px rgba(0,0,0,0.3)',
                backgroundColor: 'white',
              }}
            >
              <div
                style={{
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  padding: '10px',
                  backgroundColor: '#f8f9fa',
                  borderTopLeftRadius: '8px',
                  borderTopRightRadius: '8px',
                  borderBottom: '1px solid #ddd',
                }}
              >
                <h3 style={{ margin: 0, fontSize: '16px' }}>Book Assistant</h3>
                <button
                  onClick={toggleChatbot}
                  style={{
                    background: 'none',
                    border: 'none',
                    fontSize: '20px',
                    cursor: 'pointer',
                    padding: '0 5px',
                  }}
                  aria-label="Close chatbot"
                >
                  ×
                </button>
              </div>
              <div style={{ height: 'calc(100% - 50px)' }}>
                <BookChatbot title="Ask about this book" />
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default Root;
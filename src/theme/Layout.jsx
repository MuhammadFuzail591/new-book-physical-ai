import React, { useState, lazy, Suspense } from 'react';
import OriginalLayout from '@theme-original/Layout';

// Lazy load the BookChatbot component to avoid initialization issues
const BookChatbot = lazy(() => import('../components/BookChatbot'));

// Custom Layout wrapper that adds global chatbot functionality
const Layout = (props) => {
  const [showChatbot, setShowChatbot] = useState(false);

  const toggleChatbot = () => {
    setShowChatbot(!showChatbot);
  };

  // Loading component for the chatbot
  const ChatbotLoader = () => (
    <div style={{ padding: '20px', height: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
      <div>Loading chatbot...</div>
    </div>
  );

  return (
    <>
      <OriginalLayout {...props} />

      {/* Floating chatbot button - appears on all pages */}
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
              backgroundColor: 'var(--ifm-color-primary, #007bff)',
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
              width: '380px',
              height: '550px',
              border: '1px solid var(--ifm-color-emphasis-300, #ddd)',
              borderRadius: '8px',
              boxShadow: '0 4px 12px rgba(0,0,0,0.3)',
              backgroundColor: 'var(--ifm-background-surface-color, white)',
            }}
          >
            <div
              style={{
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center',
                padding: '10px',
                backgroundColor: 'var(--ifm-color-emphasis-200, #f8f9fa)',
                borderTopLeftRadius: '8px',
                borderTopRightRadius: '8px',
                borderBottom: '1px solid var(--ifm-color-emphasis-300, #ddd)',
              }}
            >
              <h3 style={{ margin: 0, fontSize: '16px', color: 'var(--ifm-heading-color, inherit)' }}>
                Book Assistant
              </h3>
              <button
                onClick={toggleChatbot}
                style={{
                  background: 'none',
                  border: 'none',
                  fontSize: '20px',
                  cursor: 'pointer',
                  padding: '0 5px',
                  color: 'var(--ifm-font-color-base)',
                }}
                aria-label="Close chatbot"
              >
                ×
              </button>
            </div>
            <div style={{ height: 'calc(100% - 50px)' }}>
              <Suspense fallback={<ChatbotLoader />}>
                <BookChatbot title="Ask about this book" />
              </Suspense>
            </div>
          </div>
        )}
      </div>
    </>
  );
};

export default Layout;
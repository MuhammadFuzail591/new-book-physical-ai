# Quickstart Guide: Book Chatbot Frontend

## Prerequisites
- Node.js 18+ installed
- Access to the backend chatbot API
- Existing book UI application codebase

## Setup

### 1. Install Dependencies
```bash
npm install react react-dom typescript @types/react @types/react-dom
npm install axios react-hook-form
```

### 2. Environment Configuration
Create a `.env` file with the following variables:
```env
REACT_APP_CHATBOT_API_URL=http://localhost:8000/api
REACT_APP_CHATBOT_WS_URL=ws://localhost:8000/ws
```

### 3. Component Integration
Add the chatbot component to your existing book UI:

```tsx
import { ChatInterface } from './components/ChatInterface/ChatWindow';

function BookPage() {
  return (
    <div className="book-container">
      <div className="book-content">
        {/* Your existing book content */}
      </div>
      <div className="chatbot-sidebar">
        <ChatInterface bookId={currentBookId} />
      </div>
    </div>
  );
}
```

## Running the Development Server
```bash
npm start
```

## Key Components

### ChatWindow
Main container for the chat interface with message history display and input area.

### MessageBubble
Displays individual messages with different styling for user vs bot messages.

### MessageInput
Handles user input with validation and submission.

### ChatHistory
Manages and displays the conversation history within a session.

## API Integration
The frontend communicates with the backend via the API endpoints defined in the contract. WebSocket is used for real-time message streaming.

## Testing
```bash
# Unit tests
npm run test

# Integration tests
npm run test:integration

# End-to-end tests
npm run test:e2e
```

## Building for Production
```bash
npm run build
```
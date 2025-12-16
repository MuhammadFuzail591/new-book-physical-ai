# Data Model: Book Chatbot Frontend

## Entities

### ChatMessage
- **id**: string (unique identifier for the message)
- **content**: string (the actual message text)
- **sender**: enum (either 'user' or 'bot')
- **timestamp**: Date (when the message was sent/received)
- **status**: enum ('sent', 'delivered', 'error') - for tracking message delivery
- **chatSessionId**: string (reference to the parent chat session)

### ChatSession
- **id**: string (unique identifier for the session)
- **messages**: ChatMessage[] (array of messages in the conversation)
- **createdAt**: Date (when the session was started)
- **updatedAt**: Date (when the session was last updated)
- **isActive**: boolean (whether the session is currently active)

### ChatConfig
- **apiEndpoint**: string (URL for the backend chatbot API)
- **websocketEndpoint**: string (URL for real-time communication)
- **maxMessageLength**: number (maximum allowed length for user messages)
- **timeoutMs**: number (request timeout in milliseconds)

## Validation Rules

### ChatMessage Validation
- Content must not be empty or whitespace only
- Content length must be less than or equal to maxMessageLength from ChatConfig
- Sender must be either 'user' or 'bot'
- Timestamp must be a valid date

### ChatSession Validation
- Must have at least one message in the messages array
- Session must be active to accept new messages
- Session should not exceed maximum conversation length (TBD based on performance)

## State Transitions

### Message Status Transitions
- Initial state: 'sent' (when user sends message)
- On successful delivery: 'delivered' (when message is confirmed by server)
- On error: 'error' (when there's a delivery failure)

### Session Lifecycle
- New session created when user opens chat interface
- Session becomes active when first message is sent
- Session remains active until user closes the chat or timeout occurs
- Session can be temporarily paused but preserved for context
# Chatbot API Documentation

## Base URL
`http://localhost:8000/api/v1` (or your deployed URL)

## Authentication
This API does not require authentication for basic usage.

## Endpoints

### GET /health
**Description**: Check the health status of the API and its dependencies.

**Response**:
```json
{
  "status": "healthy",
  "dependencies": {
    "qdrant": "connected",
    "llm": "available",
    "embeddings_model": "loaded"
  },
  "timestamp": "2025-12-16T10:30:00Z"
}
```

### POST /chat
**Description**: Submit a query about the textbook content.

**Request Body**:
```json
{
  "query_text": "What are the key principles of physical AI?",
  "session_id": "optional-session-id"
}
```

**Response**:
```json
{
  "response_text": "Physical AI combines robotics and artificial intelligence...",
  "sources": [
    {
      "content": "Physical AI is defined as the integration of...",
      "score": 0.92,
      "page_number": 45,
      "section_title": "Introduction to Physical AI",
      "metadata": {}
    }
  ],
  "confidence": 0.85,
  "query_id": "query_abc123"
}
```

### POST /chat/conversation
**Description**: Submit a query with conversation context for multi-turn conversations.

**Request Body**:
```json
{
  "query_text": "Can you elaborate on that?",
  "session_id": "required-session-id"
}
```

**Response**:
Same as POST /chat

## Error Responses

### 400 Bad Request
```json
{
  "error": "VALIDATION_ERROR",
  "message": "Query exceeds maximum length of 1000 characters",
  "details": {
    "max_length": 1000,
    "actual_length": 1200
  }
}
```

### 500 Internal Server Error
```json
{
  "error": "INTERNAL_ERROR",
  "message": "Internal server error occurred while processing the query"
}
```

### 503 Service Unavailable
Returned when dependencies are unavailable.

## Models

### Query
- `query_text`: string (required, 1-1000 characters)
- `session_id`: string (optional, pattern: ^[a-zA-Z0-9_-]+$)
- `user_id`: string (optional, pattern: ^[a-zA-Z0-9_-]+$)

### Response
- `response_text`: string (required)
- `sources`: array of Source objects (optional)
- `confidence`: number (0.0-1.0, optional)
- `query_id`: string (optional)

### Source
- `content`: string (required)
- `score`: number (0.0-1.0, required)
- `page_number`: integer (optional)
- `section_title`: string (optional)
- `metadata`: object (optional)

### HealthStatus
- `status`: string ("healthy", "degraded", "unavailable")
- `dependencies`: object with dependency statuses
- `timestamp`: datetime (ISO 8601 format)
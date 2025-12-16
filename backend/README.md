# Chatbot API for Physical AI & Humanoid Robotics Textbook

This is a FastAPI-based chatbot API that allows users to query the Physical AI & Humanoid Robotics textbook content using a RAG (Retrieval-Augmented Generation) approach.

## Features

- Query the textbook content using natural language
- Health check endpoint to verify service status
- Multi-turn conversations with context maintenance
- Response confidence scoring
- Source attribution for responses

## Requirements

- Python 3.11+
- Cohere API key
- Qdrant vector database with book embeddings

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file with your configuration:
   ```env
   COHERE_API_KEY=your_cohere_api_key_here
   QDRANT_HOST=localhost
   QDRANT_PORT=6333
   QDRANT_COLLECTION_NAME=book_embeddings
   ```

3. Run the application:
   ```bash
   uvicorn src.main:app --host 0.0.0.0 --port 8000
   ```

## API Endpoints

### Chat
- `POST /api/v1/chat` - Basic chat query
- `POST /api/v1/chat/conversation` - Chat with conversation context (requires session_id)

### Health Check
- `GET /api/v1/health` - Health status of the service and dependencies

## Docker

Build and run with Docker:

```bash
docker build -t chatbot-api .
docker run -p 8000:8000 chatbot-api
```

## Testing

Run the tests:

```bash
pytest
```

Or with coverage:

```bash
pytest --cov=src --cov-report=html
```

## Architecture

The application follows a RAG (Retrieval-Augmented Generation) pattern:
1. User query is embedded using Cohere
2. Vector similarity search is performed in Qdrant to find relevant content
3. Relevant content is used as context for response generation with Cohere
4. Response is returned with source attribution and confidence score

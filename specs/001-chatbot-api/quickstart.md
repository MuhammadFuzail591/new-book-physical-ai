# Quickstart: Chatbot API via FastAPI

## Prerequisites

- Python 3.9+
- pip package manager
- Access to Cohere API key (for embeddings)
- Qdrant database with book embeddings already loaded

## Setup

1. **Install dependencies**:
   ```bash
   pip install fastapi uvicorn python-dotenv qdrant-client cohere
   ```

2. **Environment Configuration**:
   Create a `.env` file with the following variables:
   ```env
   COHERE_API_KEY=your_cohere_api_key_here
   QDRANT_HOST=localhost
   QDRANT_PORT=6333
   QDRANT_COLLECTION_NAME=book_embeddings
   ```

3. **Run the API**:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

## Basic Usage

### Chat Endpoint
Send a query to get a response based on the book content:

```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "query_text": "What are the key principles of physical AI?"
  }'
```

### Health Check
Verify that the API is running and connected to dependencies:

```bash
curl -X GET "http://localhost:8000/health"
```

## Example Response

```json
{
  "response_text": "Physical AI combines robotics and artificial intelligence...",
  "sources": [
    {
      "content": "Physical AI is defined as the integration of...",
      "score": 0.92,
      "page_number": 45,
      "section_title": "Introduction to Physical AI"
    }
  ],
  "confidence": 0.85,
  "query_id": "query_abc123"
}
```

## Development

1. **Run with auto-reload**:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

2. **Access interactive API documentation**:
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## Testing

Run the test suite:
```bash
pytest tests/
```

## Deployment

The API can be deployed using:
- Docker container with uvicorn workers
- Cloud platforms like AWS, GCP, or Azure
- Container orchestration with Kubernetes
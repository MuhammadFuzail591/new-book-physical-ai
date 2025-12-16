# Data Model: Chatbot API via FastAPI

## Entities

### Query
- **Fields**:
  - `query_text` (string, required): The user's natural language question about the book content
  - `session_id` (string, optional): For maintaining conversation context (future enhancement)
  - `user_id` (string, optional): For user identification (future enhancement)
- **Validation**:
  - `query_text` must be 1-1000 characters
  - `query_text` must not be empty or contain only whitespace
- **Relationships**: None initially, may relate to Session in future

### Response
- **Fields**:
  - `response_text` (string, required): The chatbot's answer to the user's query
  - `sources` (array of objects, optional): List of source chunks that informed the response
  - `confidence` (number, optional): Confidence score of the response (0.0-1.0)
  - `query_id` (string, optional): Reference to the original query
- **Validation**:
  - `response_text` must be provided
  - `confidence` must be between 0.0 and 1.0 if provided
- **Relationships**: Links to Query that generated this response

### Context
- **Fields**:
  - `content` (string, required): Retrieved book content chunk relevant to the query
  - `score` (number, required): Similarity score from vector search (0.0-1.0)
  - `page_number` (number, optional): Page reference in the original book
  - `section_title` (string, optional): Section title from the book
  - `metadata` (object, optional): Additional metadata from Qdrant
- **Validation**:
  - `content` must not be empty
  - `score` must be between 0.0 and 1.0
- **Relationships**: Used to generate Response from Query

### Session
- **Fields**:
  - `session_id` (string, required): Unique identifier for the conversation
  - `created_at` (datetime, required): Timestamp of session creation
  - `last_activity` (datetime, required): Timestamp of last interaction
  - `conversation_history` (array of objects, optional): History of query-response pairs
- **Validation**:
  - `session_id` must be unique
  - `created_at` and `last_activity` must be valid timestamps
- **Relationships**: Contains multiple Query-Response pairs

## State Transitions

### Query Processing States
1. **Received**: Query submitted to API, waiting for processing
2. **Searching**: Performing vector similarity search in Qdrant
3. **Generating**: LLM generating response from retrieved context
4. **Completed**: Response ready for return to user
5. **Failed**: Error occurred during processing

## API Endpoints Data Flow

### POST /chat
- **Input**: Query entity
- **Processing**: Query → Context retrieval → Response generation
- **Output**: Response entity

### GET /health
- **Input**: None
- **Processing**: Check Qdrant connection, model availability
- **Output**: Health status object with connectivity information

### POST /chat/context (Future)
- **Input**: Query entity with session context
- **Processing**: Query + Session context → Enhanced Context retrieval → Response generation
- **Output**: Enhanced Response entity
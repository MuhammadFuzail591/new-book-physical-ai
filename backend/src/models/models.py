from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime


class Query(BaseModel):
    """
    A user's natural language question about the book content
    """
    query_text: str = Field(
        ...,
        description="The user's natural language question about the book content",
        min_length=1,
        max_length=1000
    )
    session_id: Optional[str] = Field(
        None,
        description="Session identifier for maintaining conversation context",
        pattern=r"^[a-zA-Z0-9_-]+$"
    )
    user_id: Optional[str] = Field(
        None,
        description="User identifier for user-specific features",
        pattern=r"^[a-zA-Z0-9_-]+$"
    )

    class Config:
        schema_extra = {
            "example": {
                "query_text": "What are the key principles of physical AI?",
                "session_id": "sess_abc123"
            }
        }


class Source(BaseModel):
    """
    Retrieved book content chunk that informed the response
    """
    content: str = Field(
        ...,
        description="Retrieved book content chunk relevant to the query"
    )
    score: float = Field(
        ...,
        description="Similarity score from vector search",
        ge=0.0,
        le=1.0
    )
    page_number: Optional[int] = Field(
        None,
        description="Page reference in the original book"
    )
    section_title: Optional[str] = Field(
        None,
        description="Section title from the book"
    )
    metadata: Optional[Dict[str, Any]] = Field(
        None,
        description="Additional metadata from Qdrant"
    )

    class Config:
        schema_extra = {
            "example": {
                "content": "Physical AI is defined as the integration of...",
                "score": 0.92,
                "page_number": 45,
                "section_title": "Introduction to Physical AI"
            }
        }


class Response(BaseModel):
    """
    The chatbot's answer to the user's query
    """
    response_text: str = Field(
        ...,
        description="The chatbot's answer to the user's query"
    )
    sources: Optional[List[Source]] = Field(
        None,
        description="List of source chunks that informed the response"
    )
    confidence: Optional[float] = Field(
        None,
        description="Confidence score of the response",
        ge=0.0,
        le=1.0
    )
    query_id: Optional[str] = Field(
        None,
        description="Unique identifier for the query",
        pattern=r"^[a-zA-Z0-9_-]+$"
    )

    class Config:
        schema_extra = {
            "example": {
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
        }


class Context(BaseModel):
    """
    Retrieved book content chunks relevant to the query
    """
    content: str = Field(
        ...,
        description="Retrieved book content chunk relevant to the query"
    )
    score: float = Field(
        ...,
        description="Similarity score from vector search",
        ge=0.0,
        le=1.0
    )
    page_number: Optional[int] = Field(
        None,
        description="Page reference in the original book"
    )
    section_title: Optional[str] = Field(
        None,
        description="Section title from the book"
    )
    metadata: Optional[Dict[str, Any]] = Field(
        None,
        description="Additional metadata from Qdrant"
    )

    class Config:
        schema_extra = {
            "example": {
                "content": "Physical AI is defined as the integration of...",
                "score": 0.92,
                "page_number": 45,
                "section_title": "Introduction to Physical AI",
                "metadata": {"url": "https://example.com/page", "chunk_id": 123}
            }
        }


class Message(BaseModel):
    """
    A message in a conversation
    """
    role: str = Field(
        ...,
        description="Role of the message sender",
        enum=["user", "assistant"]
    )
    content: str = Field(
        ...,
        description="Content of the message"
    )

    class Config:
        schema_extra = {
            "example": {
                "role": "user",
                "content": "What are the key principles of physical AI?"
            }
        }


class Session(BaseModel):
    """
    A conversation context that maintains state across multiple queries
    """
    session_id: str = Field(
        ...,
        description="Unique identifier for the conversation",
        pattern=r"^[a-zA-Z0-9_-]+$"
    )
    created_at: datetime = Field(
        ...,
        description="Timestamp of session creation"
    )
    last_activity: datetime = Field(
        ...,
        description="Timestamp of last interaction"
    )
    conversation_history: Optional[List[Message]] = Field(
        None,
        description="History of query-response pairs"
    )

    class Config:
        schema_extra = {
            "example": {
                "session_id": "sess_abc123",
                "created_at": "2025-12-16T10:30:00Z",
                "last_activity": "2025-12-16T10:35:00Z",
                "conversation_history": [
                    {
                        "role": "user",
                        "content": "What is physical AI?"
                    },
                    {
                        "role": "assistant",
                        "content": "Physical AI combines robotics and artificial intelligence..."
                    }
                ]
            }
        }


class HealthStatus(BaseModel):
    """
    Health status response with dependency information
    """
    status: str = Field(
        ...,
        description="Overall health status",
        enum=["healthy", "degraded", "unavailable"]
    )
    dependencies: Dict[str, str] = Field(
        ...,
        description="Status of various dependencies"
    )
    timestamp: datetime = Field(
        ...,
        description="Time when health check was performed"
    )

    class Config:
        schema_extra = {
            "example": {
                "status": "healthy",
                "dependencies": {
                    "qdrant": "connected",
                    "embeddings_model": "loaded",
                    "llm": "available"
                },
                "timestamp": "2025-12-16T10:30:00Z"
            }
        }


class Error(BaseModel):
    """
    Error response structure
    """
    error: str = Field(
        ...,
        description="Error code"
    )
    message: str = Field(
        ...,
        description="Human-readable error message"
    )
    details: Optional[Dict[str, Any]] = Field(
        None,
        description="Additional error details"
    )

    class Config:
        schema_extra = {
            "example": {
                "error": "QUERY_TOO_LONG",
                "message": "Query exceeds maximum length of 1000 characters",
                "details": {
                    "max_length": 1000,
                    "actual_length": 1200
                }
            }
        }
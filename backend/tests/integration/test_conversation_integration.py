import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
import uuid
import os
from ...src.main import app

# Set up environment for testing
os.environ["COHERE_API_KEY"] = "test-key"
os.environ["QDRANT_HOST"] = "localhost"
os.environ["QDRANT_PORT"] = "6333"
os.environ["QDRANT_COLLECTION_NAME"] = "test_collection"

client = TestClient(app)

def test_conversation_flow():
    """Integration test for full conversation flow with context"""
    session_id = str(uuid.uuid4())

    # First query
    query_data = {
        "query_text": "What is physical AI?",
        "session_id": session_id
    }

    # Mock the services that would normally call external APIs
    with patch('backend.src.services.qdrant_service.qdrant_service.search_similar') as mock_search, \
         patch('backend.src.services.cohere_service.cohere_service.generate_response_with_sources') as mock_generate, \
         patch('backend.src.services.cohere_service.cohere_service.embed_text') as mock_embed:

        # Mock embedding generation
        mock_embed.return_value = [0.1, 0.2, 0.3]  # Mock embedding vector

        # Mock search results for first query
        from ...src.models.models import Context
        mock_contexts1 = [
            Context(
                content="Physical AI is defined as the integration of robotics and artificial intelligence...",
                score=0.92,
                page_number=45,
                section_title="Introduction to Physical AI"
            )
        ]
        mock_search.return_value = mock_contexts1

        # Mock response generation for first query
        mock_generate.return_value = (
            "Physical AI combines robotics and artificial intelligence to create intelligent physical systems.",
            []
        )

        response1 = client.post("/chat/conversation", json=query_data)

        assert response1.status_code == 200
        response_data1 = response1.json()
        assert "Physical AI" in response_data1["response_text"]


def test_conversation_follow_up():
    """Integration test for follow-up question in conversation"""
    session_id = str(uuid.uuid4())

    # First query
    first_query_data = {
        "query_text": "What is physical AI?",
        "session_id": session_id
    }

    # Follow-up query
    followup_query_data = {
        "query_text": "Can you elaborate on that?",
        "session_id": session_id
    }

    with patch('backend.src.services.qdrant_service.qdrant_service.search_similar') as mock_search, \
         patch('backend.src.services.cohere_service.cohere_service.generate_response_with_sources') as mock_generate, \
         patch('backend.src.services.cohere_service.cohere_service.embed_text') as mock_embed:

        # Mock embedding generation
        mock_embed.return_value = [0.1, 0.2, 0.3]  # Mock embedding vector for all calls

        # Mock search results for both queries
        from ...src.models.models import Context
        mock_contexts = [
            Context(
                content="Physical AI is defined as the integration of robotics and artificial intelligence...",
                score=0.92,
                page_number=45,
                section_title="Introduction to Physical AI"
            )
        ]
        mock_search.return_value = mock_contexts

        # Mock response generation
        mock_generate.return_value = (
            "Physical AI combines robotics and artificial intelligence to create intelligent physical systems.",
            []
        )

        # First query
        response1 = client.post("/chat/conversation", json=first_query_data)
        assert response1.status_code == 200

        # Follow-up query
        response2 = client.post("/chat/conversation", json=followup_query_data)
        assert response2.status_code == 200
        response_data2 = response2.json()
        assert "Physical AI" in response_data2["response_text"]


def test_conversation_without_session_id():
    """Test conversation endpoint without session_id (should fail)"""
    query_data = {
        "query_text": "What is physical AI?",
        # No session_id provided
    }

    response = client.post("/chat/conversation", json=query_data)

    assert response.status_code == 400
    assert "session_id is required" in response.json()["detail"]


def test_conversation_with_invalid_session():
    """Test conversation with invalid session ID"""
    query_data = {
        "query_text": "What is physical AI?",
        "session_id": "invalid-session-id"
    }

    response = client.post("/chat/conversation", json=query_data)

    assert response.status_code == 400
    assert "does not exist or has expired" in response.json()["detail"]
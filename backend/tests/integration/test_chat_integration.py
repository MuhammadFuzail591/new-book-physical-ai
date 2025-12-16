import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
import os
from ...src.main import app

# Set up environment for testing
os.environ["COHERE_API_KEY"] = "test-key"
os.environ["QDRANT_HOST"] = "localhost"
os.environ["QDRANT_PORT"] = "6333"
os.environ["QDRANT_COLLECTION_NAME"] = "test_collection"

client = TestClient(app)

def test_chat_integration_basic_query():
    """Integration test for basic chat functionality"""
    query_data = {
        "query_text": "What are the key principles of physical AI?"
    }

    # Mock the services that would normally call external APIs
    with patch('backend.src.services.qdrant_service.qdrant_service.search_similar') as mock_search, \
         patch('backend.src.services.cohere_service.cohere_service.generate_response_with_sources') as mock_generate, \
         patch('backend.src.services.cohere_service.cohere_service.embed_text') as mock_embed:

        # Mock embedding generation
        mock_embed.return_value = [0.1, 0.2, 0.3]  # Mock embedding vector

        # Mock search results
        from ...src.models.models import Context
        mock_contexts = [
            Context(
                content="Physical AI is defined as the integration of...",
                score=0.92,
                page_number=45,
                section_title="Introduction to Physical AI"
            )
        ]
        mock_search.return_value = mock_contexts

        # Mock response generation
        mock_generate.return_value = (
            "Physical AI combines robotics and artificial intelligence...",
            []
        )

        response = client.post("/chat", json=query_data)

        assert response.status_code == 200
        response_data = response.json()
        assert "Physical AI" in response_data["response_text"]
        assert response_data["confidence"] > 0
        assert response_data["query_id"] is not None


def test_chat_integration_no_context():
    """Integration test for query with no relevant context"""
    query_data = {
        "query_text": "What is the meaning of life?"
    }

    # Mock the services that would normally call external APIs
    with patch('backend.src.services.qdrant_service.qdrant_service.search_similar') as mock_search, \
         patch('backend.src.services.cohere_service.cohere_service.embed_text') as mock_embed:

        # Mock embedding generation
        mock_embed.return_value = [0.1, 0.2, 0.3]  # Mock embedding vector

        # Mock empty search results
        mock_search.return_value = []

        response = client.post("/chat", json=query_data)

        assert response.status_code == 200
        response_data = response.json()
        assert "I don't know" in response_data["response_text"] or "not contain information" in response_data["response_text"]
        assert response_data["confidence"] == 0.0


def test_chat_integration_low_similarity():
    """Integration test for query with low similarity contexts"""
    query_data = {
        "query_text": "What is quantum physics?"
    }

    # Mock the services that would normally call external APIs
    with patch('backend.src.services.qdrant_service.qdrant_service.search_similar') as mock_search, \
         patch('backend.src.services.cohere_service.cohere_service.embed_text') as mock_embed:

        # Mock embedding generation
        mock_embed.return_value = [0.1, 0.2, 0.3]  # Mock embedding vector

        # Mock search results with low similarity scores
        from ...src.models.models import Context
        mock_contexts = [
            Context(
                content="This is about robotics...",
                score=0.1,  # Below threshold
                page_number=10,
                section_title="Robotics Basics"
            )
        ]
        mock_search.return_value = mock_contexts

        response = client.post("/chat", json=query_data)

        assert response.status_code == 200
        response_data = response.json()
        assert "I don't know" in response_data["response_text"] or "not contain information" in response_data["response_text"]


def test_health_check_endpoint_exists():
    """Basic test to ensure the API is running"""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
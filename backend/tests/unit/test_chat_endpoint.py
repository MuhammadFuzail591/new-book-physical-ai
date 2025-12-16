import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from ...src.models.models import Query
from ...src.main import app

client = TestClient(app)

def test_chat_endpoint_success():
    """Test successful chat query"""
    query_data = {
        "query_text": "What are the key principles of physical AI?"
    }

    with patch('backend.src.services.chat_service.chat_service.process_query') as mock_process:
        mock_response = MagicMock()
        mock_response.response_text = "Physical AI combines robotics and artificial intelligence..."
        mock_response.sources = []
        mock_response.confidence = 0.85
        mock_response.query_id = "test-id-123"

        mock_process.return_value = mock_response

        response = client.post("/chat", json=query_data)

        assert response.status_code == 200
        assert "Physical AI" in response.json()["response_text"]


def test_chat_endpoint_empty_query():
    """Test chat endpoint with empty query"""
    query_data = {
        "query_text": ""
    }

    response = client.post("/chat", json=query_data)

    assert response.status_code == 400
    assert "detail" in response.json()


def test_chat_endpoint_long_query():
    """Test chat endpoint with query that exceeds length limit"""
    query_data = {
        "query_text": "This is a very long query " + "x" * 1001  # Exceeds 1000 char limit
    }

    response = client.post("/chat", json=query_data)

    assert response.status_code == 400
    assert "exceeds maximum length" in response.json()["detail"]


def test_chat_endpoint_validation_error():
    """Test chat endpoint with invalid session_id format"""
    query_data = {
        "query_text": "What is physical AI?",
        "session_id": "invalid session id with spaces"  # Invalid format
    }

    response = client.post("/chat", json=query_data)

    assert response.status_code == 400
    assert "detail" in response.json()


def test_chat_endpoint_internal_error():
    """Test chat endpoint with internal processing error"""
    query_data = {
        "query_text": "What is physical AI?"
    }

    with patch('backend.src.services.chat_service.chat_service.process_query') as mock_process:
        mock_process.side_effect = Exception("Internal error")

        response = client.post("/chat", json=query_data)

        assert response.status_code == 500
        assert "detail" in response.json()


def test_chat_conversation_endpoint():
    """Test conversation endpoint (currently same as basic chat)"""
    query_data = {
        "query_text": "What are the key principles of physical AI?"
    }

    with patch('backend.src.services.chat_service.chat_service.process_query') as mock_process:
        mock_response = MagicMock()
        mock_response.response_text = "Physical AI combines robotics and artificial intelligence..."
        mock_response.sources = []
        mock_response.confidence = 0.85
        mock_response.query_id = "test-id-123"

        mock_process.return_value = mock_response

        response = client.post("/chat/conversation", json=query_data)

        assert response.status_code == 200
        assert "Physical AI" in response.json()["response_text"]
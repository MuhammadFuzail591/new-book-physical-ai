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

def test_health_check_success():
    """Test health check with all dependencies available"""
    with patch('backend.src.services.qdrant_service.qdrant_service.check_connection') as mock_qdrant, \
         patch('backend.src.services.cohere_service.cohere_service.check_connection') as mock_cohere, \
         patch('backend.src.services.qdrant_service.qdrant_service.get_collection_info') as mock_collection:

        mock_qdrant.return_value = True
        mock_cohere.return_value = True
        mock_collection.return_value = MagicMock()

        response = client.get("/health")

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert data["dependencies"]["qdrant"] == "connected"
        assert data["dependencies"]["llm"] == "available"
        assert data["dependencies"]["embeddings_model"] == "loaded"


def test_health_check_qdrant_disconnected():
    """Test health check with Qdrant disconnected"""
    with patch('backend.src.services.qdrant_service.qdrant_service.check_connection') as mock_qdrant, \
         patch('backend.src.services.cohere_service.cohere_service.check_connection') as mock_cohere:

        mock_qdrant.return_value = False  # Qdrant disconnected
        mock_cohere.return_value = True

        response = client.get("/health")

        assert response.status_code == 503  # Service unavailable
        data = response.json()
        assert data["status"] == "unavailable"
        assert data["dependencies"]["qdrant"] == "disconnected"


def test_health_check_cohere_error():
    """Test health check with Cohere connection error"""
    with patch('backend.src.services.qdrant_service.qdrant_service.check_connection') as mock_qdrant, \
         patch('backend.src.services.cohere_service.cohere_service.check_connection') as mock_cohere:

        mock_qdrant.return_value = True
        mock_cohere.side_effect = Exception("API Key error")  # Cohere error

        response = client.get("/health")

        assert response.status_code == 503  # Service unavailable
        data = response.json()
        assert data["status"] == "unavailable"
        assert data["dependencies"]["llm"] == "error"


def test_health_check_cohere_unavailable():
    """Test health check with Cohere unavailable"""
    with patch('backend.src.services.qdrant_service.qdrant_service.check_connection') as mock_qdrant, \
         patch('backend.src.services.cohere_service.cohere_service.check_connection') as mock_cohere:

        mock_qdrant.return_value = True
        mock_cohere.return_value = False  # Cohere unavailable

        response = client.get("/health")

        assert response.status_code == 503  # Service unavailable
        data = response.json()
        assert data["status"] == "unavailable"
        assert data["dependencies"]["llm"] == "unavailable"


def test_health_check_degraded():
    """Test health check with degraded status"""
    with patch('backend.src.services.qdrant_service.qdrant_service.check_connection') as mock_qdrant, \
         patch('backend.src.services.cohere_service.cohere_service.check_connection') as mock_cohere, \
         patch('backend.src.services.qdrant_service.qdrant_service.get_collection_info') as mock_collection:

        mock_qdrant.return_value = True
        mock_cohere.return_value = True
        mock_collection.side_effect = Exception("Collection not found")  # Embeddings model error

        response = client.get("/health")

        # Should still return 200 but with degraded status
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "degraded"  # Degraded because embeddings model has error
        assert data["dependencies"]["embeddings_model"] == "error"
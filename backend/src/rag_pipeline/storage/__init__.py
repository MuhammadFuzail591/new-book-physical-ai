"""Storage module for the RAG pipeline."""

from .qdrant_client import (
    QdrantStorage,
    create_qdrant_storage
)

__all__ = [
    "QdrantStorage",
    "create_qdrant_storage"
]
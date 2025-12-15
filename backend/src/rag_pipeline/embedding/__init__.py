"""Embedding module for the RAG pipeline."""

from .cohere_client import (
    CohereEmbedder,
    create_cohere_embedder,
    embed_text,
    embed_texts
)

__all__ = [
    "CohereEmbedder",
    "create_cohere_embedder",
    "embed_text",
    "embed_texts"
]
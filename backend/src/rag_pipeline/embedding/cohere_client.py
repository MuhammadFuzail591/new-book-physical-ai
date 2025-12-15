"""Cohere client for embedding generation in the RAG pipeline."""

from typing import List, Union

import cohere

from ..config.settings import settings
from ..utils.errors import EmbeddingError
from ..utils.logger import logger


class CohereEmbedder:
    """
    Cohere client for generating text embeddings using Cohere's embedding models.
    """

    def __init__(self, model_name: str = "embed-multilingual-v2.0"):
        """
        Initialize the Cohere embedder.

        Args:
            model_name: Name of the Cohere embedding model to use
        """
        # Validate settings
        settings.validate()

        self.model_name = model_name
        self.client = cohere.Client(settings.COHERE_API_KEY)

    def embed_text(self, text: str) -> List[float]:
        """
        Generate embedding for a single text.

        Args:
            text: Text to embed

        Returns:
            Embedding vector as a list of floats
        """
        try:
            logger.debug(f"Generating embedding for text of length {len(text)}")

            # Call Cohere API to generate embedding
            response = self.client.embed(
                texts=[text],
                model=self.model_name,
                input_type="search_document"  # Optimize for search documents
            )

            # Extract the embedding from the response
            if response.embeddings and len(response.embeddings) > 0:
                embedding = response.embeddings[0]
                logger.debug(f"Generated embedding with {len(embedding)} dimensions")
                return embedding
            else:
                raise EmbeddingError("No embeddings returned from Cohere API")

        except Exception as e:
            logger.error(f"Error generating embedding for text: {e}")
            raise EmbeddingError(f"Failed to generate embedding: {str(e)}")

    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for multiple texts.

        Args:
            texts: List of texts to embed

        Returns:
            List of embedding vectors
        """
        if not texts:
            return []

        try:
            logger.debug(f"Generating embeddings for {len(texts)} texts")

            # Cohere has limits on batch size, so we might need to chunk the requests
            # For now, let's assume reasonable batch size
            response = self.client.embed(
                texts=texts,
                model=self.model_name,
                input_type="search_document"  # Optimize for search documents
            )

            # Extract embeddings from the response
            if response.embeddings and len(response.embeddings) == len(texts):
                logger.debug(f"Generated {len(response.embeddings)} embeddings")
                return response.embeddings
            else:
                raise EmbeddingError(f"Expected {len(texts)} embeddings, got {len(response.embeddings) if response.embeddings else 0}")

        except Exception as e:
            logger.error(f"Error generating embeddings for texts: {e}")
            raise EmbeddingError(f"Failed to generate embeddings: {str(e)}")

    def embed_chunk(self, text: str) -> List[float]:
        """
        Embed a text chunk (convenience method with validation).

        Args:
            text: Text chunk to embed

        Returns:
            Embedding vector
        """
        if not text or not text.strip():
            raise EmbeddingError("Cannot embed empty text")

        # Validate text length (Cohere has limits)
        if len(text) > 50000:  # Conservative limit
            logger.warning(f"Text length ({len(text)}) exceeds recommended limit, consider chunking")

        return self.embed_text(text)


def create_cohere_embedder(model_name: str = "embed-multilingual-v2.0") -> CohereEmbedder:
    """
    Create a Cohere embedder instance.

    Args:
        model_name: Name of the Cohere embedding model to use

    Returns:
        CohereEmbedder instance
    """
    return CohereEmbedder(model_name=model_name)


def embed_text(text: str, model_name: str = "embed-multilingual-v2.0") -> List[float]:
    """
    Convenience function to embed a single text.

    Args:
        text: Text to embed
        model_name: Name of the Cohere embedding model to use

    Returns:
        Embedding vector
    """
    embedder = create_cohere_embedder(model_name)
    return embedder.embed_text(text)


def embed_texts(texts: List[str], model_name: str = "embed-multilingual-v2.0") -> List[List[float]]:
    """
    Convenience function to embed multiple texts.

    Args:
        texts: List of texts to embed
        model_name: Name of the Cohere embedding model to use

    Returns:
        List of embedding vectors
    """
    embedder = create_cohere_embedder(model_name)
    return embedder.embed_texts(texts)


if __name__ == "__main__":
    # Test the Cohere client (only if API key is available)
    import os
    if settings.COHERE_API_KEY:
        try:
            embedder = CohereEmbedder()
            test_text = "This is a test sentence for embedding."
            embedding = embedder.embed_text(test_text)
            print(f"Generated embedding with {len(embedding)} dimensions")
            print(f"First 10 dimensions: {embedding[:10]}")
        except Exception as e:
            print(f"Could not test Cohere client: {e}")
    else:
        print("COHERE_API_KEY not set, skipping client test")
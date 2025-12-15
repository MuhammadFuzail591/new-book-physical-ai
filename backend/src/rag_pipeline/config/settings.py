"""Configuration settings for the RAG pipeline."""

import os
from typing import Optional

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings:
    """Application settings loaded from environment variables."""

    # API Keys and URLs
    COHERE_API_KEY: str = os.getenv("COHERE_API_KEY", "")
    QDRANT_API_KEY: str = os.getenv("QDRANT_API_KEY", "")
    QDRANT_URL: str = os.getenv("QDRANT_URL", "")

    # Source configuration
    SOURCE_URL: str = os.getenv("SOURCE_URL", "https://new-book-physical-ai.vercel.app/")

    # Qdrant configuration
    QDRANT_COLLECTION_NAME: str = os.getenv("QDRANT_COLLECTION_NAME", "rag_chunks")

    # Processing configuration
    CHUNK_SIZE: int = int(os.getenv("CHUNK_SIZE", "800"))
    OVERLAP_SIZE: int = int(os.getenv("OVERLAP_SIZE", "100"))

    # Pipeline configuration
    FORCE_REINDEX: bool = os.getenv("FORCE_REINDEX", "false").lower() == "true"

    # Validation
    def validate(self) -> None:
        """Validate that required settings are present."""
        errors = []

        if not self.COHERE_API_KEY:
            errors.append("COHERE_API_KEY is required")

        if not self.QDRANT_API_KEY:
            errors.append("QDRANT_API_KEY is required")

        if not self.QDRANT_URL:
            errors.append("QDRANT_URL is required")

        if not self.SOURCE_URL:
            errors.append("SOURCE_URL is required")

        if errors:
            raise ValueError("Missing required configuration values: " + "; ".join(errors))

    def __str__(self) -> str:
        """String representation with sensitive data masked."""
        return (
            f"Settings(\n"
            f"  SOURCE_URL='{self.SOURCE_URL}',\n"
            f"  QDRANT_COLLECTION_NAME='{self.QDRANT_COLLECTION_NAME}',\n"
            f"  CHUNK_SIZE={self.CHUNK_SIZE},\n"
            f"  OVERLAP_SIZE={self.OVERLAP_SIZE},\n"
            f"  FORCE_REINDEX={self.FORCE_REINDEX}\n"
            f")"
        )


# Global settings instance
settings = Settings()
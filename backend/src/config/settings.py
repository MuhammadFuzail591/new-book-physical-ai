import os
from typing import Optional
from pydantic import BaseSettings, validator
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings(BaseSettings):
    """
    Application settings with validation
    """

    # API Configuration
    app_name: str = "Chatbot API for Physical AI & Humanoid Robotics Textbook"
    app_version: str = "1.0.0"
    debug: bool = False
    host: str = "0.0.0.0"
    port: int = 8000

    # Cohere Configuration
    cohere_api_key: str = os.getenv("COHERE_API_KEY", "")
    cohere_generation_model: str = os.getenv("COHERE_GENERATION_MODEL", "command-r-plus")
    cohere_embedding_model: str = os.getenv("COHERE_EMBEDDING_MODEL", "embed-english-v3.0")

    # Qdrant Configuration
    qdrant_host: str = os.getenv("QDRANT_HOST", "localhost")
    qdrant_port: int = int(os.getenv("QDRANT_PORT", "6333"))
    qdrant_collection_name: str = os.getenv("QDRANT_COLLECTION_NAME", "book_embeddings")
    qdrant_api_key: Optional[str] = os.getenv("QDRANT_API_KEY")

    # Application-specific settings
    max_query_length: int = 1000
    min_query_length: int = 1
    max_response_tokens: int = 500
    default_temperature: float = 0.7
    max_contexts_per_query: int = 5
    context_similarity_threshold: float = 0.3  # Minimum similarity score to include context

    # Performance settings
    response_timeout: int = 30  # seconds
    max_concurrent_requests: int = 100
    query_processing_timeout: int = 5  # seconds for query processing

    # Validation methods
    @validator('cohere_api_key')
    def validate_cohere_api_key(cls, v):
        if not v:
            raise ValueError('COHERE_API_KEY environment variable is required')
        return v

    @validator('qdrant_host')
    def validate_qdrant_host(cls, v):
        if not v:
            raise ValueError('QDRANT_HOST environment variable is required')
        return v

    @validator('port')
    def validate_port(cls, v):
        if v < 1 or v > 65535:
            raise ValueError('Port must be between 1 and 65535')
        return v

    @validator('max_query_length')
    def validate_max_query_length(cls, v):
        if v <= 0:
            raise ValueError('max_query_length must be positive')
        if v > 10000:  # Reasonable upper limit
            raise ValueError('max_query_length is too large')
        return v

    @validator('context_similarity_threshold')
    def validate_context_similarity_threshold(cls, v):
        if v < 0.0 or v > 1.0:
            raise ValueError('context_similarity_threshold must be between 0.0 and 1.0')
        return v

    class Config:
        env_file = ".env"
        case_sensitive = True

# Create global settings instance
settings = Settings()

def get_settings() -> Settings:
    """
    Get the application settings instance

    Returns:
        Settings: The application settings
    """
    return settings
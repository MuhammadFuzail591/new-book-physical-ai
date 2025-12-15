"""Custom error classes for the RAG pipeline."""


class RAGPipelineError(Exception):
    """Base exception for RAG pipeline errors."""

    def __init__(self, message: str, error_code: str = "RAG_PIPELINE_ERROR"):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.error_code}] {self.message}"


class ConfigurationError(RAGPipelineError):
    """Raised when there are configuration issues."""

    def __init__(self, message: str):
        super().__init__(message, "CONFIG_ERROR")


class ContentExtractionError(RAGPipelineError):
    """Raised when content extraction fails."""

    def __init__(self, message: str, url: str = ""):
        self.url = url
        super().__init__(f"Content extraction failed for {url}: {message}", "CONTENT_EXTRACTION_ERROR")


class ChunkingError(RAGPipelineError):
    """Raised when content chunking fails."""

    def __init__(self, message: str):
        super().__init__(message, "CHUNKING_ERROR")


class EmbeddingError(RAGPipelineError):
    """Raised when embedding generation fails."""

    def __init__(self, message: str):
        super().__init__(message, "EMBEDDING_ERROR")


class StorageError(RAGPipelineError):
    """Raised when storage operations fail."""

    def __init__(self, message: str):
        super().__init__(message, "STORAGE_ERROR")


class ValidationError(RAGPipelineError):
    """Raised when validation fails."""

    def __init__(self, message: str):
        super().__init__(message, "VALIDATION_ERROR")


class NetworkError(RAGPipelineError):
    """Raised when network operations fail."""

    def __init__(self, message: str, url: str = ""):
        self.url = url
        super().__init__(f"Network error for {url}: {message}", "NETWORK_ERROR")


class RateLimitError(RAGPipelineError):
    """Raised when API rate limits are exceeded."""

    def __init__(self, message: str = "API rate limit exceeded"):
        super().__init__(message, "RATE_LIMIT_ERROR")


class ProcessingError(RAGPipelineError):
    """Raised when general processing fails."""

    def __init__(self, message: str):
        super().__init__(message, "PROCESSING_ERROR")
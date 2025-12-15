"""RAG Pipeline package."""

__version__ = "0.1.0"

# Import main components for easy access
from .main import run_ingestion_pipeline
from .config.settings import settings
from .ingestion import (
    discover_urls,
    extract_content,
    is_docusaurus_page,
    parse_docusaurus_page
)
from .processing import (
    ContentChunker,
    chunk_content,
    TextCleaner,
    clean_text_for_rag
)
from .embedding import (
    CohereEmbedder,
    embed_text,
    embed_texts
)
from .storage import (
    QdrantStorage,
    create_qdrant_storage
)

__all__ = [
    "run_ingestion_pipeline",
    "settings",
    # Ingestion
    "discover_urls",
    "extract_content",
    "is_docusaurus_page",
    "parse_docusaurus_page",
    # Processing
    "ContentChunker",
    "chunk_content",
    "TextCleaner",
    "clean_text_for_rag",
    # Embedding
    "CohereEmbedder",
    "embed_text",
    "embed_texts",
    # Storage
    "QdrantStorage",
    "create_qdrant_storage"
]
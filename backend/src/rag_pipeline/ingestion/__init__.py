"""Ingestion module for the RAG pipeline."""

from .url_discovery import discover_urls
from .content_extractor import extract_content
from .docusaurus_parser import (
    is_docusaurus_page,
    parse_docusaurus_page,
    extract_docusaurus_content,
    extract_docusaurus_metadata
)

__all__ = [
    "discover_urls",
    "extract_content",
    "is_docusaurus_page",
    "parse_docusaurus_page",
    "extract_docusaurus_content",
    "extract_docusaurus_metadata"
]
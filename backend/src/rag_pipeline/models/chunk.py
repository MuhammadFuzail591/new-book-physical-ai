"""Data model for a book content chunk."""

import hashlib
from datetime import datetime
from typing import Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class BookContentChunk:
    """
    A semantically coherent segment of book content that has been processed for RAG,
    containing the text content, metadata, and vector embedding.
    """

    id: str  # Unique identifier combining URL and chunk index
    content: str  # The actual text content of the chunk
    url: str  # Original URL of the source page
    title: str  # Page title from HTML
    section: str  # Section/chapter identifier
    chunk_index: int  # Sequential index of this chunk within the source page
    content_hash: str  # Hash of the content for change detection
    created_at: datetime  # Timestamp when chunk was created
    updated_at: datetime  # Timestamp when chunk was last updated

    def __post_init__(self):
        """Validate the chunk after initialization."""
        if not self.content.strip():
            raise ValueError("Content must be non-empty")
        if len(self.content) > 10000:  # Rough token limit check
            raise ValueError("Content exceeds reasonable size limit")
        if not self.url.strip():
            raise ValueError("URL must be valid")
        if not self.content_hash.strip():
            raise ValueError("Content hash must be valid")

    @classmethod
    def create_from_content(
        cls,
        content: str,
        url: str,
        title: str,
        section: str,
        chunk_index: int,
    ) -> "BookContentChunk":
        """
        Create a BookContentChunk from content with automatic ID and hash generation.

        Args:
            content: The text content of the chunk
            url: Original URL of the source page
            title: Page title from HTML
            section: Section/chapter identifier
            chunk_index: Sequential index of this chunk within the source page

        Returns:
            BookContentChunk instance
        """
        # Generate ID combining URL and chunk index
        chunk_id = f"{url}#{chunk_index}"

        # Generate content hash
        content_hash = hashlib.sha256(content.encode()).hexdigest()

        # Create timestamps
        now = datetime.now()

        return cls(
            id=chunk_id,
            content=content,
            url=url,
            title=title,
            section=section,
            chunk_index=chunk_index,
            content_hash=content_hash,
            created_at=now,
            updated_at=now,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert the chunk to a dictionary representation."""
        return {
            "id": self.id,
            "content": self.content,
            "url": self.url,
            "title": self.title,
            "section": self.section,
            "chunk_index": self.chunk_index,
            "content_hash": self.content_hash,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BookContentChunk":
        """Create a BookContentChunk from a dictionary representation."""
        return cls(
            id=data["id"],
            content=data["content"],
            url=data["url"],
            title=data["title"],
            section=data["section"],
            chunk_index=data["chunk_index"],
            content_hash=data["content_hash"],
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
        )

    def update_content(self, new_content: str) -> None:
        """
        Update the content and hash of the chunk.

        Args:
            new_content: New content for the chunk
        """
        if not new_content.strip():
            raise ValueError("Content must be non-empty")

        self.content = new_content
        self.content_hash = hashlib.sha256(new_content.encode()).hexdigest()
        self.updated_at = datetime.now()
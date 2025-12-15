"""Content chunking module for the RAG pipeline."""

import re
from typing import List, Optional

from ..models.chunk import BookContentChunk
from ..utils.errors import ChunkingError
from ..utils.logger import logger


class ContentChunker:
    """
    Content chunking algorithm that breaks text into semantically coherent segments
    suitable for RAG with appropriate size balancing recall, precision, and context window efficiency.
    """

    def __init__(self, chunk_size: int = 800, overlap_size: int = 100):
        """
        Initialize the content chunker.

        Args:
            chunk_size: Target size of chunks in tokens/approximate length
            overlap_size: Overlap between chunks in tokens/approximate length
        """
        self.chunk_size = chunk_size
        self.overlap_size = overlap_size

        if chunk_size <= 0:
            raise ValueError("chunk_size must be positive")
        if overlap_size < 0:
            raise ValueError("overlap_size cannot be negative")
        if overlap_size >= chunk_size:
            raise ValueError("overlap_size must be smaller than chunk_size")

    def chunk(
        self,
        content: str,
        source_url: str,
        title: str,
        section: str,
    ) -> List[BookContentChunk]:
        """
        Chunk the content into semantically coherent segments.

        Args:
            content: The content to chunk
            source_url: Original URL of the source page
            title: Page title
            section: Section identifier

        Returns:
            List of BookContentChunk objects
        """
        if not content.strip():
            return []

        logger.info(f"Chunking content from {source_url} ({len(content)} chars)")

        # Split content into sentences while preserving sentence boundaries
        sentences = self._split_into_sentences(content)

        if len(sentences) == 1 and len(sentences[0]) <= self.chunk_size:
            # If the entire content fits in one chunk, return it as is
            chunk = BookContentChunk.create_from_content(
                content=content,
                url=source_url,
                title=title,
                section=section,
                chunk_index=0,
            )
            logger.debug(f"Created single chunk for {source_url}")
            return [chunk]

        # Create chunks using a sliding window approach
        chunks = []
        current_chunk = ""
        chunk_index = 0

        for sentence in sentences:
            # Estimate token count (rough approximation: 1 token ~ 4 chars)
            sentence_length = len(sentence)
            current_length = len(current_chunk)

            if current_length == 0:
                # Start a new chunk with this sentence
                current_chunk = sentence
            elif current_length + sentence_length + 1 <= self.chunk_size:
                # Add sentence to current chunk (with space separator)
                current_chunk += " " + sentence
            else:
                # Current chunk is full, create a chunk and start a new one
                if current_chunk.strip():
                    chunk = BookContentChunk.create_from_content(
                        content=current_chunk.strip(),
                        url=source_url,
                        title=title,
                        section=section,
                        chunk_index=chunk_index,
                    )
                    chunks.append(chunk)
                    chunk_index += 1

                # Start new chunk with potential overlap
                # Add overlapping content from the end of the previous chunk
                overlap_content = self._get_overlap_content(current_chunk)
                current_chunk = overlap_content + " " + sentence if overlap_content else sentence

                # If the new chunk is too large, try to split the sentence
                if len(current_chunk) > self.chunk_size:
                    # Split the sentence and continue building chunks
                    sub_sentences = self._split_sentence_for_chunking(sentence)
                    for sub_sentence in sub_sentences:
                        if len(current_chunk) + len(sub_sentence) + 1 <= self.chunk_size:
                            current_chunk += " " + sub_sentence
                        else:
                            if current_chunk.strip():
                                chunk = BookContentChunk.create_from_content(
                                    content=current_chunk.strip(),
                                    url=source_url,
                                    title=title,
                                    section=section,
                                    chunk_index=chunk_index,
                                )
                                chunks.append(chunk)
                                chunk_index += 1

                            overlap_content = self._get_overlap_content(current_chunk)
                            current_chunk = overlap_content + " " + sub_sentence if overlap_content else sub_sentence

        # Add the last chunk if it has content
        if current_chunk.strip():
            chunk = BookContentChunk.create_from_content(
                content=current_chunk.strip(),
                url=source_url,
                title=title,
                section=section,
                chunk_index=chunk_index,
            )
            chunks.append(chunk)

        logger.info(f"Created {len(chunks)} chunks from {source_url}")
        return chunks

    def _split_into_sentences(self, text: str) -> List[str]:
        """
        Split text into sentences while preserving sentence boundaries.

        Args:
            text: Text to split

        Returns:
            List of sentences
        """
        # This is a simplified sentence splitter
        # For more robust sentence splitting, consider using nltk or spacy
        sentences = re.split(r'(?<=[.!?])\s+', text)
        return [sentence.strip() for sentence in sentences if sentence.strip()]

    def _get_overlap_content(self, text: str) -> str:
        """
        Get the overlap content from the end of a chunk.

        Args:
            text: Text to extract overlap from

        Returns:
            Overlap content (last N characters, roughly respecting word boundaries)
        """
        if len(text) <= self.overlap_size:
            return text

        # Start from the overlap size and look for a word boundary
        start_pos = max(0, len(text) - self.overlap_size)
        overlap_text = text[start_pos:]

        # Find the last space to avoid cutting words
        last_space = overlap_text.rfind(' ')
        if last_space > 0:
            overlap_text = overlap_text[last_space + 1:]

        return overlap_text

    def _split_sentence_for_chunking(self, sentence: str) -> List[str]:
        """
        Split a long sentence into smaller parts for chunking.

        Args:
            sentence: Sentence to split

        Returns:
            List of sentence parts
        """
        if len(sentence) <= self.chunk_size:
            return [sentence]

        # Split by commas or other natural breaks first
        parts = re.split(r'[,;]\s+', sentence)

        # If parts are still too long, split by words
        final_parts = []
        for part in parts:
            if len(part) <= self.chunk_size:
                final_parts.append(part)
            else:
                # Split into chunks of roughly self.chunk_size characters
                words = part.split()
                current_part = ""
                for word in words:
                    if len(current_part) + len(word) + 1 <= self.chunk_size:
                        current_part += " " + word if current_part else word
                    else:
                        if current_part:
                            final_parts.append(current_part)
                        current_part = word
                if current_part:
                    final_parts.append(current_part)

        return final_parts


def chunk_content(
    content: str,
    source_url: str,
    title: str,
    section: str,
    chunk_size: int = 800,
    overlap_size: int = 100,
) -> List[BookContentChunk]:
    """
    Convenience function to chunk content.

    Args:
        content: The content to chunk
        source_url: Original URL of the source page
        title: Page title
        section: Section identifier
        chunk_size: Target size of chunks
        overlap_size: Overlap between chunks

    Returns:
        List of BookContentChunk objects
    """
    chunker = ContentChunker(chunk_size=chunk_size, overlap_size=overlap_size)
    return chunker.chunk(content, source_url, title, section)


if __name__ == "__main__":
    # Test the chunker
    test_content = (
        "This is a test sentence. Here is another one! And a third one? "
        "This paragraph has multiple sentences that should be handled properly. "
        "The chunker should respect sentence boundaries while maintaining chunk size limits. "
        "Additional content to make the text longer for testing purposes. "
        "More sentences to ensure we have enough content to create multiple chunks. "
        "Final sentence to complete the test content."
    )

    chunker = ContentChunker(chunk_size=100, overlap_size=20)
    chunks = chunker.chunk(
        content=test_content,
        source_url="https://example.com/test",
        title="Test Page",
        section="Test Section"
    )

    print(f"Created {len(chunks)} chunks:")
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i}: {len(chunk.content)} chars - {chunk.content[:50]}...")
"""Text cleaning module for RAG-friendly content."""

import re
from typing import List, Optional

from ..utils.logger import logger


class TextCleaner:
    """
    Text cleaning utility for creating RAG-friendly content.
    Cleans text to optimize for semantic retrieval while preserving meaning.
    """

    def __init__(self):
        """Initialize the text cleaner."""
        pass

    def clean(self, text: str) -> str:
        """
        Clean text for RAG-friendly format.

        Args:
            text: Raw text to clean

        Returns:
            Cleaned text
        """
        if not text:
            return ""

        # Apply cleaning steps in order
        cleaned_text = text

        # Remove extra whitespace and normalize
        cleaned_text = self._normalize_whitespace(cleaned_text)

        # Remove common boilerplate
        cleaned_text = self._remove_boilerplate(cleaned_text)

        # Fix common text issues
        cleaned_text = self._fix_common_issues(cleaned_text)

        # Ensure proper sentence structure
        cleaned_text = self._ensure_sentence_structure(cleaned_text)

        # Remove extra whitespace again after all operations
        cleaned_text = self._normalize_whitespace(cleaned_text)

        return cleaned_text.strip()

    def _normalize_whitespace(self, text: str) -> str:
        """Normalize whitespace in text."""
        # Replace multiple spaces with single space
        text = re.sub(r' +', ' ', text)
        # Replace multiple newlines with single newline
        text = re.sub(r'\n+', '\n', text)
        # Replace multiple tabs with single space
        text = re.sub(r'\t+', ' ', text)
        # Remove leading/trailing whitespace from each line
        text = '\n'.join(line.strip() for line in text.split('\n'))
        # Remove extra blank lines
        text = re.sub(r'\n\s*\n', '\n\n', text)
        return text.strip()

    def _remove_boilerplate(self, text: str) -> str:
        """Remove common boilerplate text."""
        # Patterns for common boilerplate
        boilerplate_patterns = [
            r'Copyright \d{4}.*?$',  # Copyright notices
            r'All rights reserved.*?$',  # Rights reserved
            r'Privacy Policy.*?$',  # Privacy policy links
            r'Terms of Service.*?$',  # Terms of service
            r'Contact us.*?$',  # Contact info
            r'Subscribe.*?$',  # Subscribe prompts
            r'Follow us.*?$',  # Social media prompts
            r'Was this page helpful.*?$',  # Feedback prompts
            r'Edit this page.*?$',  # Edit links
            r'Last updated.*?$',  # Update info
            r'On this page.*?$',  # Table of contents
            r'Continue reading.*?$',  # Read more links
            r'Next.*?$',  # Next page links
            r'Previous.*?$',  # Previous page links
            r'Found an issue.*?$',  # Issue reporting
            r'Like this.*?$',  # Like buttons
            r'Tweet this.*?$',  # Share buttons
        ]

        for pattern in boilerplate_patterns:
            text = re.sub(pattern, '', text, flags=re.MULTILINE | re.IGNORECASE)

        return text

    def _fix_common_issues(self, text: str) -> str:
        """Fix common text formatting issues."""
        # Fix hyphens that might be artifacts of text extraction
        text = re.sub(r'(\w)-\s+(\w)', r'\1\2', text)  # Remove hyphens at line breaks

        # Fix common encoding issues
        text = text.replace('â€™', "'")  # Right single quotation mark
        text = text.replace('â€œ', '"')  # Left double quotation mark
        text = text.replace('â€\x9d', '"')  # Right double quotation mark
        text = text.replace('â€“', '-')  # En dash
        text = text.replace('â€”', '-')  # Em dash
        text = text.replace('â€¢', '•')  # Bullet

        # Fix extra punctuation
        text = re.sub(r'\.{3,}', '...', text)  # Multiple dots to ellipsis
        text = re.sub(r'!{2,}', '!', text)  # Multiple exclamation marks
        text = re.sub(r'\?{2,}', '?', text)  # Multiple question marks

        # Fix common OCR/copy-paste errors
        text = re.sub(r'\s+([,.!?;:])', r'\1', text)  # Spaces before punctuation
        text = re.sub(r'([,.!?;:])\s*([a-z])', r'\1 \2', text)  # Missing space after punctuation

        return text

    def _ensure_sentence_structure(self, text: str) -> str:
        """Ensure proper sentence structure."""
        # Add space after sentence endings if missing
        text = re.sub(r'([.!?])([A-Z])', r'\1 \2', text)

        # Ensure paragraphs have proper spacing
        paragraphs = text.split('\n\n')
        cleaned_paragraphs = []

        for paragraph in paragraphs:
            # Remove extra spaces within paragraphs but preserve sentence structure
            lines = paragraph.split('\n')
            cleaned_lines = []

            for line in lines:
                line = line.strip()
                if line:
                    cleaned_lines.append(line)

            if cleaned_lines:
                cleaned_paragraph = ' '.join(cleaned_lines)
                cleaned_paragraphs.append(cleaned_paragraph)

        return '\n\n'.join(cleaned_paragraphs)

    def clean_batch(self, texts: List[str]) -> List[str]:
        """
        Clean a batch of texts.

        Args:
            texts: List of texts to clean

        Returns:
            List of cleaned texts
        """
        return [self.clean(text) for text in texts]


def clean_text_for_rag(text: str) -> str:
    """
    Convenience function to clean text for RAG.

    Args:
        text: Raw text to clean

    Returns:
        Cleaned text
    """
    cleaner = TextCleaner()
    return cleaner.clean(text)


def clean_batch_for_rag(texts: List[str]) -> List[str]:
    """
    Convenience function to clean a batch of texts for RAG.

    Args:
        texts: List of texts to clean

    Returns:
        List of cleaned texts
    """
    cleaner = TextCleaner()
    return cleaner.clean_batch(texts)


if __name__ == "__main__":
    # Test the text cleaner
    test_texts = [
        "This  is   a test.\n\nWith multiple    spaces and\nline breaks.",
        "Copyright 2023 Example Corp. All rights reserved.\n\nThis is actual content.",
        "This is a sentence.This is another sentence.",
        "Text with\u200bzero-width\u200bspaces and\u00a0non-breaking\u00a0spaces."
    ]

    cleaner = TextCleaner()

    for i, text in enumerate(test_texts):
        print(f"Original {i+1}: {repr(text)}")
        cleaned = cleaner.clean(text)
        print(f"Cleaned {i+1}:  {repr(cleaned)}")
        print("---")
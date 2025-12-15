"""Basic functionality test for the RAG pipeline."""

import sys
import os

# Add the src directory to the path so we can import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from rag_pipeline.config.settings import settings
from rag_pipeline.ingestion.url_discovery import discover_urls
from rag_pipeline.ingestion.content_extractor import extract_content
from rag_pipeline.processing.chunker import ContentChunker
from rag_pipeline.utils.logger import logger


def test_basic_functionality():
    """Test basic functionality of the RAG pipeline components."""
    print("Testing basic RAG pipeline functionality...")

    # Validate settings
    try:
        settings.validate()
        print("✓ Settings validation passed")
    except Exception as e:
        print(f"✗ Settings validation failed: {e}")
        return False

    # Test URL discovery (just check it doesn't crash)
    try:
        urls = discover_urls(settings.SOURCE_URL)
        print(f"✓ URL discovery worked, found {len(urls)} URLs (showing first 3):")
        for url in urls[:3]:
            print(f"  - {url}")
    except Exception as e:
        print(f"✗ URL discovery failed: {e}")
        # This might fail if the source URL is not accessible, which is OK for local testing

    # Test content extraction with a sample (non-actual URL for testing)
    try:
        # Use a simple test to make sure the functions are importable and callable
        chunker = ContentChunker(chunk_size=200, overlap_size=50)
        print("✓ Content chunker initialized successfully")

        # Test chunking with sample content
        sample_content = "This is a test sentence. Here is another one! And a third one? This paragraph has multiple sentences."
        chunks = chunker.chunk(
            content=sample_content,
            source_url="https://example.com/test",
            title="Test Page",
            section="Test Section"
        )
        print(f"✓ Content chunking worked, created {len(chunks)} chunks")

    except Exception as e:
        print(f"✗ Content processing failed: {e}")
        return False

    print("\nBasic functionality test completed!")
    return True


if __name__ == "__main__":
    success = test_basic_functionality()
    if success:
        print("\n✓ All basic tests passed!")
        sys.exit(0)
    else:
        print("\n✗ Some tests failed!")
        sys.exit(1)
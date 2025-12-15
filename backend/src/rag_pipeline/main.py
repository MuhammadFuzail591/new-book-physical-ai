"""Main entry point for the RAG pipeline."""

import asyncio
import sys
from typing import Optional

from .config.settings import settings
from .ingestion.url_discovery import discover_urls
from .ingestion.content_extractor import extract_content
from .processing.chunker import ContentChunker
from .embedding.cohere_client import CohereEmbedder
from .storage.qdrant_client import QdrantStorage
from .utils.logger import logger
from .models.pipeline import IngestionPipeline, PipelineStatus


def run_ingestion_pipeline(
    source_url: Optional[str] = None,
    force_reindex: Optional[bool] = None,
    chunk_size: Optional[int] = None,
    overlap_size: Optional[int] = None,
) -> IngestionPipeline:
    """
    Run the complete RAG ingestion pipeline.

    Args:
        source_url: Base URL to ingest (defaults to configured SOURCE_URL)
        force_reindex: Whether to force reprocessing all content (defaults to configured FORCE_REINDEX)
        chunk_size: Size of text chunks in tokens (defaults to configured CHUNK_SIZE)
        overlap_size: Overlap between chunks in tokens (defaults to configured OVERLAP_SIZE)

    Returns:
        IngestionPipeline with run statistics
    """
    # Use default values if not provided
    source_url = source_url or settings.SOURCE_URL
    force_reindex = force_reindex or settings.FORCE_REINDEX
    chunk_size = chunk_size or settings.CHUNK_SIZE
    overlap_size = overlap_size or settings.OVERLAP_SIZE

    logger.info(f"Starting RAG ingestion pipeline for {source_url}")

    # Validate settings
    settings.validate()

    # Create pipeline run record
    import uuid
    run_id = f"run_{uuid.uuid4().hex[:8]}"
    pipeline = IngestionPipeline.create_new(run_id, source_url)
    pipeline.start()

    try:
        # Initialize components
        chunker = ContentChunker(chunk_size=chunk_size, overlap_size=overlap_size)
        embedder = CohereEmbedder()
        storage = QdrantStorage()
        storage.initialize_collection()

        # Discover URLs
        logger.info("Discovering URLs...")
        urls = discover_urls(source_url)
        logger.info(f"Discovered {len(urls)} URLs")

        # Process each URL
        processed_urls = 0
        successful_chunks = 0
        failed_chunks = 0
        total_chunks = 0

        for url in urls:
            try:
                logger.info(f"Processing URL: {url}")

                # Extract content
                content, title, section = extract_content(url)

                if not content.strip():
                    logger.warning(f"No content extracted from {url}")
                    continue

                # Chunk content
                chunks = chunker.chunk(content, url, title, section)

                # Process each chunk
                for i, chunk in enumerate(chunks):
                    try:
                        # Generate embedding
                        embedding = embedder.embed_text(chunk.content)

                        # Store in Qdrant
                        storage.store_chunk(chunk, embedding)

                        successful_chunks += 1
                        total_chunks += 1

                        logger.debug(f"Processed chunk {i+1}/{len(chunks)} for {url}")

                    except Exception as e:
                        logger.error(f"Failed to process chunk {i} for {url}: {e}")
                        failed_chunks += 1

                processed_urls += 1

                # Update pipeline progress
                pipeline.update_progress(
                    processed_urls=processed_urls,
                    successful_chunks=successful_chunks,
                    failed_chunks=failed_chunks,
                    total_chunks=total_chunks,
                )

            except Exception as e:
                logger.error(f"Failed to process URL {url}: {e}")
                failed_chunks += 1
                processed_urls += 1  # Count as processed even if failed

                # Update pipeline progress
                pipeline.update_progress(
                    processed_urls=processed_urls,
                    successful_chunks=successful_chunks,
                    failed_chunks=failed_chunks,
                    total_chunks=total_chunks,
                )

        # Complete pipeline
        pipeline.complete()
        logger.info(
            f"Pipeline completed. Processed {processed_urls} URLs, "
            f"created {successful_chunks} chunks, {failed_chunks} failed."
        )

        return pipeline

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        pipeline.fail()
        raise


async def async_run_ingestion_pipeline(
    source_url: Optional[str] = None,
    force_reindex: Optional[bool] = None,
    chunk_size: Optional[int] = None,
    overlap_size: Optional[int] = None,
) -> IngestionPipeline:
    """
    Async version of the ingestion pipeline.
    """
    return run_ingestion_pipeline(
        source_url=source_url,
        force_reindex=force_reindex,
        chunk_size=chunk_size,
        overlap_size=overlap_size,
    )


def main():
    """Main entry point when running as a script."""
    try:
        pipeline = run_ingestion_pipeline()
        print(f"Pipeline completed successfully: {pipeline.run_id}")
        print(f"Processed URLs: {pipeline.processed_urls}")
        print(f"Successful chunks: {pipeline.successful_chunks}")
        print(f"Failed chunks: {pipeline.failed_chunks}")
        print(f"Total chunks: {pipeline.total_chunks}")
    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        print(f"Pipeline failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
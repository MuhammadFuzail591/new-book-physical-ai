"""Qdrant client for vector storage in the RAG pipeline."""

from typing import Dict, List, Optional, Any
from uuid import uuid4

from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.models import Distance, VectorParams, PayloadSchemaType

from ..config.settings import settings
from ..models.chunk import BookContentChunk
from ..models.embedding import VectorEmbedding
from ..utils.errors import StorageError
from ..utils.logger import logger


class QdrantStorage:
    """
    Qdrant client for storing and retrieving vector embeddings with rich metadata.
    """

    def __init__(self):
        """Initialize the Qdrant storage client."""
        # Validate settings
        settings.validate()

        # Initialize Qdrant client
        self.client = QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY,
            prefer_grpc=False  # Use HTTP for better compatibility
        )

        self.collection_name = settings.QDRANT_COLLECTION_NAME

    def initialize_collection(self) -> None:
        """Initialize the Qdrant collection with proper configuration."""
        try:
            # Check if collection already exists
            collections = self.client.get_collections()
            collection_exists = any(col.name == self.collection_name for col in collections.collections)

            if not collection_exists:
                # Create collection with cosine distance and proper vector size
                # Cohere's embed-multilingual-v2.0 produces 768-dimensional vectors
                self.client.create_collection(
                    collection_name=self.collection_name,
                    vectors_config=VectorParams(size=768, distance=Distance.COSINE),
                )

                # Create payload indices for efficient filtering
                self.client.create_payload_index(
                    collection_name=self.collection_name,
                    field_name="url",
                    field_schema=PayloadSchemaType.KEYWORD
                )

                self.client.create_payload_index(
                    collection_name=self.collection_name,
                    field_name="title",
                    field_schema=PayloadSchemaType.TEXT
                )

                self.client.create_payload_index(
                    collection_name=self.collection_name,
                    field_name="section",
                    field_schema=PayloadSchemaType.KEYWORD
                )

                self.client.create_payload_index(
                    collection_name=self.collection_name,
                    field_name="chunk_index",
                    field_schema=PayloadSchemaType.INTEGER
                )

                logger.info(f"Created Qdrant collection '{self.collection_name}' with proper schema")
            else:
                logger.info(f"Qdrant collection '{self.collection_name}' already exists")

        except Exception as e:
            logger.error(f"Error initializing Qdrant collection: {e}")
            raise StorageError(f"Failed to initialize Qdrant collection: {str(e)}")

    def store_chunk(self, chunk: BookContentChunk, embedding: VectorEmbedding) -> bool:
        """
        Store a content chunk with its embedding in Qdrant.

        Args:
            chunk: The content chunk to store
            embedding: The vector embedding for the chunk

        Returns:
            True if successful, False otherwise
        """
        try:
            logger.debug(f"Storing chunk {chunk.id} in Qdrant")

            # Prepare the payload with rich metadata
            payload = {
                "url": chunk.url,
                "title": chunk.title,
                "section": chunk.section,
                "chunk_index": chunk.chunk_index,
                "content_hash": chunk.content_hash,
                "content": chunk.content,
                "created_at": chunk.created_at.isoformat(),
                "updated_at": chunk.updated_at.isoformat(),
                "model_name": embedding.model_name,
                "model_version": embedding.model_version,
            }

            # Upsert the point in Qdrant
            # Using upsert to support idempotent operations (re-indexing)
            self.client.upsert(
                collection_name=self.collection_name,
                points=[
                    models.PointStruct(
                        id=chunk.id,  # Use the chunk ID as the point ID for stable references
                        vector=embedding.vector,
                        payload=payload
                    )
                ]
            )

            logger.debug(f"Successfully stored chunk {chunk.id}")
            return True

        except Exception as e:
            logger.error(f"Error storing chunk {chunk.id} in Qdrant: {e}")
            raise StorageError(f"Failed to store chunk {chunk.id}: {str(e)}")

    def store_chunks(self, chunks: List[BookContentChunk], embeddings: List[VectorEmbedding]) -> int:
        """
        Store multiple content chunks with their embeddings in Qdrant.

        Args:
            chunks: List of content chunks to store
            embeddings: List of corresponding vector embeddings

        Returns:
            Number of chunks successfully stored
        """
        if len(chunks) != len(embeddings):
            raise StorageError(f"Number of chunks ({len(chunks)}) must match number of embeddings ({len(embeddings)})")

        if not chunks:
            return 0

        try:
            logger.info(f"Storing {len(chunks)} chunks in Qdrant")

            # Prepare points for batch insertion
            points = []
            for chunk, embedding in zip(chunks, embeddings):
                payload = {
                    "url": chunk.url,
                    "title": chunk.title,
                    "section": chunk.section,
                    "chunk_index": chunk.chunk_index,
                    "content_hash": chunk.content_hash,
                    "content": chunk.content,
                    "created_at": chunk.created_at.isoformat(),
                    "updated_at": chunk.updated_at.isoformat(),
                    "model_name": embedding.model_name,
                    "model_version": embedding.model_version,
                }

                points.append(
                    models.PointStruct(
                        id=chunk.id,
                        vector=embedding.vector,
                        payload=payload
                    )
                )

            # Batch upsert the points
            self.client.upsert(
                collection_name=self.collection_name,
                points=points
            )

            logger.info(f"Successfully stored {len(chunks)} chunks in Qdrant")
            return len(chunks)

        except Exception as e:
            logger.error(f"Error storing chunks in Qdrant: {e}")
            raise StorageError(f"Failed to store chunks: {str(e)}")

    def search_similar(self, query: str, top_k: int = 5, filters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        Search for similar content chunks based on a query.

        Args:
            query: Search query text
            top_k: Number of results to return
            filters: Optional filters for metadata (e.g., {"url": "specific_url", "section": "specific_section"})

        Returns:
            List of similar chunks with metadata and similarity scores
        """
        try:
            logger.debug(f"Searching for similar content to: '{query[:50]}...'")

            # Generate embedding for the query
            # For this to work, we'd need a Cohere client to embed the query
            # For now, we'll assume the query embedding is provided or use a placeholder
            # In a real implementation, we'd have access to the Cohere client here
            from ..embedding.cohere_client import embed_text
            query_embedding = embed_text(query)

            # Build filters if provided
            qdrant_filters = None
            if filters:
                filter_conditions = []
                for key, value in filters.items():
                    if key == "url":
                        filter_conditions.append(
                            models.FieldCondition(
                                key="url",
                                match=models.MatchValue(value=value)
                            )
                        )
                    elif key == "section":
                        filter_conditions.append(
                            models.FieldCondition(
                                key="section",
                                match=models.MatchValue(value=value)
                            )
                        )
                    elif key == "chunk_index":
                        filter_conditions.append(
                            models.FieldCondition(
                                key="chunk_index",
                                range=models.Range(gte=value, lte=value)
                            )
                        )

                if filter_conditions:
                    qdrant_filters = models.Filter(must=filter_conditions)

            # Perform the search
            search_results = self.client.search(
                collection_name=self.collection_name,
                query_vector=query_embedding,
                limit=top_k,
                query_filter=qdrant_filters,
                with_payload=True,
                with_vectors=False
            )

            # Format results
            results = []
            for hit in search_results:
                payload = hit.payload
                result = {
                    "id": hit.id,
                    "url": payload.get("url"),
                    "title": payload.get("title"),
                    "section": payload.get("section"),
                    "content": payload.get("content"),
                    "score": hit.score,
                    "chunk_index": payload.get("chunk_index"),
                    "created_at": payload.get("created_at"),
                    "updated_at": payload.get("updated_at"),
                    "content_hash": payload.get("content_hash")
                }
                results.append(result)

            logger.debug(f"Found {len(results)} similar chunks")
            return results

        except Exception as e:
            logger.error(f"Error searching for similar content: {e}")
            raise StorageError(f"Failed to search for similar content: {str(e)}")

    def get_total_vectors(self) -> int:
        """
        Get the total number of vectors stored in the collection.

        Returns:
            Total number of vectors
        """
        try:
            collection_info = self.client.get_collection(self.collection_name)
            return collection_info.points_count
        except Exception as e:
            logger.error(f"Error getting total vectors count: {e}")
            raise StorageError(f"Failed to get total vectors count: {str(e)}")

    def get_chunk_by_id(self, chunk_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve a specific chunk by its ID.

        Args:
            chunk_id: ID of the chunk to retrieve

        Returns:
            Chunk data if found, None otherwise
        """
        try:
            records = self.client.retrieve(
                collection_name=self.collection_name,
                ids=[chunk_id],
                with_payload=True,
                with_vectors=False
            )

            if records:
                record = records[0]
                payload = record.payload
                return {
                    "id": record.id,
                    "url": payload.get("url"),
                    "title": payload.get("title"),
                    "section": payload.get("section"),
                    "content": payload.get("content"),
                    "chunk_index": payload.get("chunk_index"),
                    "created_at": payload.get("created_at"),
                    "updated_at": payload.get("updated_at"),
                    "content_hash": payload.get("content_hash")
                }

            return None

        except Exception as e:
            logger.error(f"Error retrieving chunk {chunk_id}: {e}")
            raise StorageError(f"Failed to retrieve chunk {chunk_id}: {str(e)}")

    def delete_collection(self) -> None:
        """
        Delete the entire collection (use with caution!).
        """
        try:
            self.client.delete_collection(self.collection_name)
            logger.info(f"Deleted Qdrant collection '{self.collection_name}'")
        except Exception as e:
            logger.error(f"Error deleting collection: {e}")
            raise StorageError(f"Failed to delete collection: {str(e)}")

    def check_content_changed(self, chunk: BookContentChunk) -> bool:
        """
        Check if the content has changed compared to the stored version.

        Args:
            chunk: The chunk to check

        Returns:
            True if content has changed or doesn't exist, False otherwise
        """
        try:
            stored_chunk = self.get_chunk_by_id(chunk.id)
            if not stored_chunk:
                # Chunk doesn't exist, so it's "changed"
                return True

            # Compare content hashes
            stored_hash = stored_chunk.get("content_hash")
            return stored_hash != chunk.content_hash

        except Exception as e:
            logger.error(f"Error checking if content changed for {chunk.id}: {e}")
            # If we can't check, assume it changed to be safe
            return True


def create_qdrant_storage() -> QdrantStorage:
    """
    Create a Qdrant storage instance.

    Returns:
        QdrantStorage instance
    """
    return QdrantStorage()


if __name__ == "__main__":
    # Test the Qdrant client (only if settings are available)
    try:
        storage = QdrantStorage()
        storage.initialize_collection()
        print(f"Qdrant collection '{storage.collection_name}' initialized successfully")
        print(f"Total vectors in collection: {storage.get_total_vectors()}")
    except Exception as e:
        print(f"Could not initialize Qdrant client: {e}")
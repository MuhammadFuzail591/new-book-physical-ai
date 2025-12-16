import os
import logging
from typing import List, Optional
from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.models import Distance, VectorParams, PointStruct
from dotenv import load_dotenv
from ..models.models import Context
import cohere

# Load environment variables
load_dotenv()

# Initialize logging
logger = logging.getLogger(__name__)

class QdrantService:
    """
    Service for interacting with Qdrant vector database for similarity search
    """

    def __init__(self):
        # Get configuration from environment
        self.host = os.getenv("QDRANT_HOST", "localhost")
        self.port = int(os.getenv("QDRANT_PORT", "6333"))
        self.collection_name = os.getenv("QDRANT_COLLECTION_NAME", "book_embeddings")
        self.api_key = os.getenv("QDRANT_API_KEY")  # Optional, for cloud instances

        # Initialize Qdrant client
        if self.api_key:
            self.client = QdrantClient(
                url=self.host,
                port=self.port,
                api_key=self.api_key,
                https=True
            )
        else:
            self.client = QdrantClient(host=self.host, port=self.port)

        logger.info(f"Qdrant client initialized for collection: {self.collection_name}")

    def search_similar(
        self,
        query_vector: List[float],
        limit: int = 5,
        filters: Optional[models.Filter] = None
    ) -> List[Context]:
        """
        Search for similar vectors in the Qdrant collection

        Args:
            query_vector: The vector to search for similarity
            limit: Maximum number of results to return
            filters: Optional filters to apply to the search

        Returns:
            List of Context objects containing the similar content
        """
        try:
            # Perform the search
            search_results = self.client.search(
                collection_name=self.collection_name,
                query_vector=query_vector,
                limit=limit,
                query_filter=filters,
                with_payload=True
            )

            # Convert results to Context objects
            contexts = []
            for result in search_results:
                payload = result.payload
                contexts.append(Context(
                    content=payload.get("text", ""),
                    score=result.score,
                    page_number=payload.get("page_number"),
                    section_title=payload.get("section_title"),
                    metadata=payload
                ))

            logger.info(f"Found {len(contexts)} similar results for query")
            return contexts

        except Exception as e:
            logger.error(f"Error searching in Qdrant: {str(e)}")
            raise

    def get_context_by_ids(self, point_ids: List[str]) -> List[Context]:
        """
        Retrieve specific points by their IDs from Qdrant

        Args:
            point_ids: List of point IDs to retrieve

        Returns:
            List of Context objects
        """
        try:
            points = self.client.retrieve(
                collection_name=self.collection_name,
                ids=point_ids,
                with_payload=True
            )

            contexts = []
            for point in points:
                payload = point.payload
                contexts.append(Context(
                    content=payload.get("text", ""),
                    score=0.0,  # Score is not available when retrieving by ID
                    page_number=payload.get("page_number"),
                    section_title=payload.get("section_title"),
                    metadata=payload
                ))

            return contexts

        except Exception as e:
            logger.error(f"Error retrieving points from Qdrant: {str(e)}")
            raise

    def check_connection(self) -> bool:
        """
        Check if the Qdrant connection is working

        Returns:
            True if connection is successful, False otherwise
        """
        try:
            # Try to get collection info
            self.client.get_collection(self.collection_name)
            return True
        except Exception as e:
            logger.error(f"Qdrant connection check failed: {str(e)}")
            return False

    def get_collection_info(self):
        """
        Get information about the collection

        Returns:
            Collection information
        """
        try:
            return self.client.get_collection(self.collection_name)
        except Exception as e:
            logger.error(f"Error getting collection info: {str(e)}")
            raise

# Global instance for use in other services
qdrant_service = QdrantService()
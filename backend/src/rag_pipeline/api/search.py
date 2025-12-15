"""Search API endpoints for the RAG pipeline."""

from typing import List

from fastapi import APIRouter, HTTPException

from ..storage.qdrant_client import QdrantStorage
from ..utils.logger import logger
from .models import SearchRequest, SearchResponse, SearchResult

router = APIRouter(prefix="/api/v1", tags=["search"])


@router.post("/search", response_model=SearchResponse)
async def semantic_search(request: SearchRequest):
    """
    Semantic search in ingested content.
    """
    try:
        logger.info(f"Processing search request: '{request.query[:50]}...'")

        # Initialize Qdrant storage
        storage = QdrantStorage()
        storage.initialize_collection()  # Ensure collection exists

        # Perform the search
        results = storage.search_similar(
            query=request.query,
            top_k=request.top_k,
            filters=request.filters
        )

        # Convert to response format
        search_results = []
        for result in results:
            search_result = SearchResult(
                id=result["id"],
                url=result["url"],
                title=result["title"],
                section=result["section"],
                content=result["content"],
                score=result["score"],
                chunk_index=result["chunk_index"]
            )
            search_results.append(search_result)

        response = SearchResponse(results=search_results)

        logger.info(f"Search completed with {len(search_results)} results")
        return response

    except Exception as e:
        logger.error(f"Error performing search: {e}")
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")


@router.get("/search/health", response_model=dict)
async def search_health():
    """
    Health check for search functionality.
    """
    try:
        storage = QdrantStorage()
        total_vectors = storage.get_total_vectors()

        return {
            "status": "healthy",
            "total_vectors": total_vectors,
            "message": "Search service is operational"
        }
    except Exception as e:
        logger.error(f"Search health check failed: {e}")
        raise HTTPException(status_code=500, detail=f"Search health check failed: {str(e)}")
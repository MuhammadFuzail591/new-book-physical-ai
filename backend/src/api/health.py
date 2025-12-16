from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from datetime import datetime
from typing import Dict
import logging

from ..models.models import HealthStatus
from ..services.qdrant_service import qdrant_service
from ..services.cohere_service import cohere_service

# Initialize router
router = APIRouter(prefix="/health", tags=["health"])

# Initialize logging
logger = logging.getLogger(__name__)

@router.get(
    "/",
    response_model=HealthStatus,
    responses={
        200: {"description": "Health status with connectivity information"},
        503: {"description": "Service unavailable due to dependency issues"}
    }
)
async def health_check():
    """
    Health check endpoint to verify API operational status and dependencies
    """
    # Check Qdrant connection
    qdrant_status = "connected" if qdrant_service.check_connection() else "disconnected"

    # Check Cohere connection
    try:
        cohere_status = "available" if cohere_service.check_connection() else "unavailable"
    except Exception:
        cohere_status = "error"

    # Determine overall status
    if qdrant_status == "disconnected" or cohere_status == "error" or cohere_status == "unavailable":
        overall_status = "unavailable"
    elif qdrant_status == "connected" and cohere_status == "available":
        overall_status = "healthy"
    else:
        overall_status = "degraded"

    # Prepare dependencies status
    dependencies = {
        "qdrant": qdrant_status,
        "llm": cohere_status
    }

    # Try to get more detailed info about embeddings model if possible
    try:
        # This is just to test if we can access the collection
        collection_info = qdrant_service.get_collection_info()
        dependencies["embeddings_model"] = "loaded"
    except Exception:
        dependencies["embeddings_model"] = "error"

    health_status = HealthStatus(
        status=overall_status,
        dependencies=dependencies,
        timestamp=datetime.utcnow()
    )

    logger.info(f"Health check completed with status: {overall_status}")

    # Return appropriate status code
    if overall_status == "unavailable":
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content=health_status.dict()
        )

    return health_status
"""Main API application for the RAG pipeline."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..config.settings import settings
from ..utils.logger import logger
from .ingestion import router as ingestion_router
from .search import router as search_router


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""

    # Validate settings before starting
    settings.validate()

    app = FastAPI(
        title="RAG Pipeline API",
        description="API for managing the RAG content ingestion pipeline and semantic search",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc"
    )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # In production, specify exact origins
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include API routers
    app.include_router(ingestion_router)
    app.include_router(search_router)

    @app.on_event("startup")
    async def startup_event():
        """Startup event handler."""
        logger.info("Starting RAG Pipeline API")
        # Initialize any required resources here

    @app.on_event("shutdown")
    async def shutdown_event():
        """Shutdown event handler."""
        logger.info("Shutting down RAG Pipeline API")
        # Clean up resources here

    @app.get("/health")
    async def health_check():
        """Health check endpoint."""
        return {
            "status": "healthy",
            "message": "RAG Pipeline API is operational",
            "source_url": settings.SOURCE_URL
        }

    return app


# Create the main application instance
app = create_app()

# For running with uvicorn directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "src.rag_pipeline.api.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
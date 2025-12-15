"""API models for request/response validation."""

from typing import List, Optional
from pydantic import BaseModel, Field, HttpUrl


class IngestionRequest(BaseModel):
    """Request model for ingestion endpoint."""
    source_url: HttpUrl = Field(
        default="https://new-book-physical-ai.vercel.app/",
        description="The base URL of the website to ingest"
    )
    force_reindex: bool = Field(
        default=False,
        description="Whether to force reprocessing all content even if unchanged"
    )
    chunk_size: int = Field(
        default=800,
        ge=100,
        le=2000,
        description="Size of text chunks in tokens"
    )
    overlap_size: int = Field(
        default=100,
        ge=0,
        le=500,
        description="Overlap between chunks in tokens"
    )


class IngestionResponse(BaseModel):
    """Response model for ingestion endpoint."""
    job_id: str = Field(
        description="Unique identifier for the ingestion job"
    )
    status: str = Field(
        description="Current status of the job",
        pattern="^(pending|running)$"
    )
    estimated_completion: Optional[str] = Field(
        default=None,
        description="Estimated time of completion"
    )


class JobStatusResponse(BaseModel):
    """Response model for job status endpoint."""
    job_id: str = Field(
        description="Unique identifier for the ingestion job"
    )
    status: str = Field(
        description="Current status of the job",
        pattern="^(pending|running|completed|failed)$"
    )
    progress: Optional[dict] = Field(
        default=None,
        description="Progress information for the job"
    )
    created_at: Optional[str] = Field(
        default=None,
        description="When the job was created"
    )
    completed_at: Optional[str] = Field(
        default=None,
        description="When the job was completed"
    )


class SearchRequest(BaseModel):
    """Request model for search endpoint."""
    query: str = Field(
        min_length=1,
        max_length=1000,
        description="Search query text"
    )
    top_k: int = Field(
        default=5,
        ge=1,
        le=10,
        description="Number of results to return (default 5, max 10)"
    )
    filters: Optional[dict] = Field(
        default=None,
        description="Optional filters for search results"
    )


class SearchResult(BaseModel):
    """Result model for search endpoint."""
    id: str = Field(
        description="Chunk identifier"
    )
    url: HttpUrl = Field(
        description="Source URL"
    )
    title: str = Field(
        description="Page title"
    )
    section: str = Field(
        description="Section identifier"
    )
    content: str = Field(
        description="Chunk content text"
    )
    score: float = Field(
        description="Similarity score"
    )
    chunk_index: int = Field(
        description="Index of chunk within source page"
    )


class SearchResponse(BaseModel):
    """Response model for search endpoint."""
    results: List[SearchResult] = Field(
        description="List of search results"
    )


class HealthCheckResponse(BaseModel):
    """Response model for health check endpoint."""
    status: str = Field(
        default="healthy",
        description="Health status of the service"
    )
    timestamp: str = Field(
        description="Current timestamp"
    )
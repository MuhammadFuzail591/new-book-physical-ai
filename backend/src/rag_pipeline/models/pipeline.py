"""Data model for the ingestion pipeline."""

from datetime import datetime
from enum import Enum
from typing import Dict, Any, Optional
from dataclasses import dataclass


class PipelineStatus(Enum):
    """Status of the ingestion pipeline run."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class IngestionPipeline:
    """
    Configuration and state tracking for the ingestion pipeline run.
    """

    run_id: str  # Unique identifier for this pipeline run
    status: PipelineStatus  # Current status (pending, running, completed, failed)
    start_time: datetime  # When the pipeline run started
    end_time: Optional[datetime]  # When the pipeline run completed/failed
    processed_urls: int  # Number of URLs processed
    successful_chunks: int  # Number of chunks successfully created
    failed_chunks: int  # Number of chunks that failed processing
    total_chunks: int  # Total number of chunks created in this run
    source_url: str  # Base URL of the site being ingested

    def __post_init__(self):
        """Validate the pipeline after initialization."""
        if not self.run_id.strip():
            raise ValueError("run_id must be valid")
        if self.processed_urls < 0:
            raise ValueError("processed_urls must be non-negative")
        if self.successful_chunks < 0:
            raise ValueError("successful_chunks must be non-negative")
        if self.failed_chunks < 0:
            raise ValueError("failed_chunks must be non-negative")
        if self.total_chunks < 0:
            raise ValueError("total_chunks must be non-negative")
        if self.end_time and self.end_time < self.start_time:
            raise ValueError("end_time must be after start_time if provided")

    @classmethod
    def create_new(
        cls,
        run_id: str,
        source_url: str,
    ) -> "IngestionPipeline":
        """
        Create a new IngestionPipeline in pending state.

        Args:
            run_id: Unique identifier for this pipeline run
            source_url: Base URL of the site being ingested

        Returns:
            IngestionPipeline instance
        """
        now = datetime.now()
        return cls(
            run_id=run_id,
            status=PipelineStatus.PENDING,
            start_time=now,
            end_time=None,
            processed_urls=0,
            successful_chunks=0,
            failed_chunks=0,
            total_chunks=0,
            source_url=source_url,
        )

    def start(self) -> None:
        """Mark the pipeline as running."""
        self.status = PipelineStatus.RUNNING
        self.start_time = datetime.now()

    def complete(self) -> None:
        """Mark the pipeline as completed."""
        self.status = PipelineStatus.COMPLETED
        self.end_time = datetime.now()

    def fail(self) -> None:
        """Mark the pipeline as failed."""
        self.status = PipelineStatus.FAILED
        self.end_time = datetime.now()

    def update_progress(
        self,
        processed_urls: int,
        successful_chunks: int,
        failed_chunks: int,
        total_chunks: int,
    ) -> None:
        """
        Update the pipeline progress.

        Args:
            processed_urls: Number of URLs processed
            successful_chunks: Number of chunks successfully created
            failed_chunks: Number of chunks that failed processing
            total_chunks: Total number of chunks created in this run
        """
        self.processed_urls = processed_urls
        self.successful_chunks = successful_chunks
        self.failed_chunks = failed_chunks
        self.total_chunks = total_chunks

    def to_dict(self) -> Dict[str, Any]:
        """Convert the pipeline to a dictionary representation."""
        return {
            "run_id": self.run_id,
            "status": self.status.value,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "processed_urls": self.processed_urls,
            "successful_chunks": self.successful_chunks,
            "failed_chunks": self.failed_chunks,
            "total_chunks": self.total_chunks,
            "source_url": self.source_url,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "IngestionPipeline":
        """Create an IngestionPipeline from a dictionary representation."""
        return cls(
            run_id=data["run_id"],
            status=PipelineStatus(data["status"]),
            start_time=datetime.fromisoformat(data["start_time"]),
            end_time=datetime.fromisoformat(data["end_time"]) if data["end_time"] else None,
            processed_urls=data["processed_urls"],
            successful_chunks=data["successful_chunks"],
            failed_chunks=data["failed_chunks"],
            total_chunks=data["total_chunks"],
            source_url=data["source_url"],
        )
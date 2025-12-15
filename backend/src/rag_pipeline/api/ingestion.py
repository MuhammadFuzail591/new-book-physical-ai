"""Ingestion API endpoints for the RAG pipeline."""

import asyncio
import uuid
from datetime import datetime
from typing import Dict, Optional

from fastapi import APIRouter, BackgroundTasks, HTTPException

from ..models.pipeline import IngestionPipeline, PipelineStatus
from ..utils.logger import logger
from .models import IngestionRequest, IngestionResponse, JobStatusResponse

# In-memory storage for job status (in production, use a database)
job_storage: Dict[str, IngestionPipeline] = {}

router = APIRouter(prefix="/api/v1", tags=["ingestion"])


@router.post("/ingest", response_model=IngestionResponse)
async def start_ingestion(request: IngestionRequest, background_tasks: BackgroundTasks):
    """
    Start content ingestion pipeline.
    Initiates the process of discovering, extracting, chunking and storing content from a website.
    """
    try:
        # Generate a unique job ID
        job_id = f"ingest_{uuid.uuid4().hex[:8]}"

        # Create a new pipeline record
        pipeline = IngestionPipeline.create_new(
            run_id=job_id,
            source_url=str(request.source_url)
        )
        job_storage[job_id] = pipeline

        # Start the ingestion process in the background
        background_tasks.add_task(
            run_ingestion_background,
            job_id=job_id,
            source_url=str(request.source_url),
            force_reindex=request.force_reindex,
            chunk_size=request.chunk_size,
            overlap_size=request.overlap_size
        )

        response = IngestionResponse(
            job_id=job_id,
            status="running",
            estimated_completion=(datetime.now().timestamp() + 3600).__str__()  # 1 hour estimate
        )

        logger.info(f"Started ingestion job {job_id} for {request.source_url}")
        return response

    except Exception as e:
        logger.error(f"Error starting ingestion: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to start ingestion: {str(e)}")


async def run_ingestion_background(
    job_id: str,
    source_url: str,
    force_reindex: bool,
    chunk_size: int,
    overlap_size: int
):
    """
    Run the ingestion process in the background.
    """
    from ..main import run_ingestion_pipeline

    try:
        # Update job status to running
        if job_id in job_storage:
            job_storage[job_id].start()

        # Run the actual ingestion pipeline
        pipeline = run_ingestion_pipeline(
            source_url=source_url,
            force_reindex=force_reindex,
            chunk_size=chunk_size,
            overlap_size=overlap_size
        )

        # Update the stored job with the completed pipeline info
        job_storage[job_id] = pipeline

        logger.info(f"Ingestion job {job_id} completed successfully")

    except Exception as e:
        logger.error(f"Ingestion job {job_id} failed: {e}")

        # Update job status to failed
        if job_id in job_storage:
            job_storage[job_id].status = PipelineStatus.FAILED
            job_storage[job_id].end_time = datetime.now()


@router.get("/ingest/{job_id}", response_model=JobStatusResponse)
async def get_ingestion_status(job_id: str):
    """
    Get ingestion job status.
    """
    try:
        if job_id not in job_storage:
            raise HTTPException(status_code=404, detail="Job not found")

        pipeline = job_storage[job_id]

        response = JobStatusResponse(
            job_id=pipeline.run_id,
            status=pipeline.status.value,
            progress={
                "total_urls": pipeline.processed_urls,
                "processed_urls": pipeline.processed_urls,
                "successful_chunks": pipeline.successful_chunks,
                "failed_chunks": pipeline.failed_chunks,
            },
            created_at=pipeline.start_time.isoformat() if pipeline.start_time else None,
            completed_at=pipeline.end_time.isoformat() if pipeline.end_time else None
        )

        logger.debug(f"Retrieved status for job {job_id}: {pipeline.status.value}")
        return response

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting ingestion status for job {job_id}: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to get job status: {str(e)}")


# For testing purposes, add a simple endpoint to list jobs
@router.get("/ingest", response_model=Dict[str, str])
async def list_ingestion_jobs():
    """
    List all ingestion jobs (for testing purposes).
    """
    try:
        job_list = {}
        for job_id, pipeline in job_storage.items():
            job_list[job_id] = pipeline.status.value

        return job_list
    except Exception as e:
        logger.error(f"Error listing ingestion jobs: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to list jobs: {str(e)}")
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan event handler for startup and shutdown
    """
    logger.info("Starting up Chatbot API...")
    # Any startup tasks can go here
    yield
    logger.info("Shutting down Chatbot API...")
    # Any cleanup tasks can go here

# Create FastAPI app instance
app = FastAPI(
    title="Chatbot API for Physical AI & Humanoid Robotics Textbook",
    description="API for querying the Physical AI & Humanoid Robotics textbook content using RAG",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Basic root endpoint
@app.get("/")
async def root():
    return {"message": "Chatbot API for Physical AI & Humanoid Robotics Textbook"}

# Include API routes
from .api import chat, health

app.include_router(chat.router, prefix="/api/v1")
app.include_router(health.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
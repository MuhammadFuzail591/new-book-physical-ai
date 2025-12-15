# RAG Pipeline

A backend service that ingests content from the Vercel-deployed book website (https://new-book-physical-ai.vercel.app/), extracts clean textual content, chunks it into semantically coherent segments, generates embeddings using Cohere models, and stores them in Qdrant vector database for semantic retrieval.

## Features

- **URL Discovery**: Automatically discovers and fetches all relevant public URLs from the Vercel deployment
- **Content Extraction**: Extracts meaningful book content while excluding navigation, headers, footers, and boilerplate
- **Smart Chunking**: Chunks content into semantically coherent segments suitable for RAG
- **Embedding Generation**: Generates embeddings using Cohere text embedding models
- **Vector Storage**: Stores vectors in Qdrant Cloud with rich metadata (URL, page title, section, chunk index)
- **Similarity Search**: Supports similarity search and returns relevant chunks for test queries

## Prerequisites

- Python 3.11+
- pip package manager
- Git

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Navigate to the backend directory:
```bash
cd backend
```

3. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. Install dependencies:
```bash
pip install -e .
# or for development:
pip install -e ".[dev]"
```

## Configuration

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` and add your API keys:
```bash
# Cohere API key for embedding generation
COHERE_API_KEY=your_cohere_api_key_here

# Qdrant API key and URL
QDRANT_API_KEY=your_qdrant_api_key_here
QDRANT_URL=your_qdrant_cluster_url_here

# Source website URL (default: https://new-book-physical-ai.vercel.app/)
SOURCE_URL=https://new-book-physical-ai.vercel.app/
```

## Running the Pipeline

1. Run the complete ingestion pipeline:
```bash
python -m src.rag_pipeline.main
```

2. Or run specific modules for testing:
```bash
# Discover URLs
python -c "from src.rag_pipeline.ingestion.url_discovery import discover_urls; print(discover_urls('https://new-book-physical-ai.vercel.app/'))"

# Process a single page
python -c "from src.rag_pipeline.ingestion.content_extractor import extract_content; print(extract_content('https://new-book-physical-ai.vercel.app/some-page'))"
```

## Running the API Server

Start the API server to use the ingestion and search endpoints:

```bash
uvicorn src.rag_pipeline.api.main:app --reload --port 8000
```

## API Endpoints

- `POST /api/v1/ingest` - Start content ingestion pipeline
- `GET /api/v1/ingest/{job_id}` - Get ingestion job status
- `POST /api/v1/search` - Semantic search in ingested content

## Verification

After running the pipeline, verify the results:

1. Check that vectors were stored in Qdrant:
```bash
python -c "
from src.rag_pipeline.storage.qdrant_client import QdrantStorage
storage = QdrantStorage()
print(f'Total vectors stored: {storage.get_total_vectors()}')
"
```

2. Test similarity search:
```bash
python -c "
from src.rag_pipeline.storage.qdrant_client import QdrantStorage
storage = QdrantStorage()
# Search for relevant content
results = storage.search_similar('your search query', top_k=5)
for result in results:
    print(f'URL: {result[\"url\"]}, Score: {result[\"score\"]}, Content: {result[\"content\"][:200]}...')
"
```

## Troubleshooting

- **Rate limit errors**: Ensure your Cohere and Qdrant API keys are valid and within usage limits
- **Connection errors**: Verify QDRANT_URL is accessible and API key is correct
- **Content extraction issues**: Check that SOURCE_URL is accessible and returns valid HTML
- **Memory issues**: For large sites, consider running in batches or increasing system memory

## Architecture

The RAG pipeline is organized into the following modules:

- `ingestion/` - URL discovery and content extraction
- `processing/` - Text cleaning and chunking
- `embedding/` - Embedding generation using Cohere
- `storage/` - Vector storage and retrieval using Qdrant
- `api/` - REST API endpoints
- `config/` - Configuration management
- `utils/` - Utility functions and helpers
- `models/` - Data models and schemas

## Performance Goals

- Process entire book website within 30 minutes
- 99% embedding generation success rate
- 90% precision/recall for similarity search

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`pytest`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
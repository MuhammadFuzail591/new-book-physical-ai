# Quickstart: RAG Pipeline

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

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r rag_pipeline/requirements.txt
```

## Configuration

1. Copy the example environment file:
```bash
cp rag_pipeline/.env.example .env
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
python -m rag_pipeline.scripts.run_ingestion
```

2. Or run specific modules for testing:
```bash
# Discover URLs
python -c "from rag_pipeline.src.ingestion.url_discovery import discover_urls; print(discover_urls('https://new-book-physical-ai.vercel.app/'))"

# Process a single page
python -c "from rag_pipeline.src.ingestion.content_fetcher import extract_content; print(extract_content('https://new-book-physical-ai.vercel.app/some-page'))"
```

## Verification

After running the pipeline, verify the results:

1. Check that vectors were stored in Qdrant:
```python
from rag_pipeline.src.storage.qdrant_client import QdrantStorage
storage = QdrantStorage()
print(f"Total vectors stored: {storage.get_total_vectors()}")
```

2. Test similarity search:
```python
# Search for relevant content
results = storage.search_similar("your search query", top_k=5)
for result in results:
    print(f"URL: {result['url']}, Score: {result['score']}, Content: {result['content'][:200]}...")
```

## Troubleshooting

- **Rate limit errors**: Ensure your Cohere and Qdrant API keys are valid and within usage limits
- **Connection errors**: Verify QDRANT_URL is accessible and API key is correct
- **Content extraction issues**: Check that SOURCE_URL is accessible and returns valid HTML
- **Memory issues**: For large sites, consider running in batches or increasing system memory
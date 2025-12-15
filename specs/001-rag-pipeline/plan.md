# Implementation Plan: RAG Pipeline – Vercel-Deployed Book Ingestion, Embedding Generation, and Vector Storage

**Branch**: `001-rag-pipeline` | **Date**: 2025-12-15 | **Spec**: specs/001-rag-pipeline/spec.md
**Input**: Feature specification from `/specs/001-rag-pipeline/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

The RAG Pipeline implementation will create an automated ingestion system that discovers, extracts, chunks, and stores content from the Vercel-deployed book website (https://new-book-physical-ai.vercel.app/). The system will use URL discovery to find all relevant pages, extract clean content while excluding navigation elements, generate vector embeddings using Cohere models, and store them in Qdrant Cloud with rich metadata for semantic retrieval. The pipeline will be designed as a reusable module suitable for future re-indexing when the site updates.

### Architecture Sketch

```
Vercel Site (https://new-book-physical-ai.vercel.app/)
         ↓ (URL Discovery)
    [URL Discovery Service] ← Sitemap / Crawling Strategy
         ↓ (URL List)
    [HTML Fetch Service] ← Concurrent page fetching
         ↓ (Raw HTML)
    [Content Extraction Service] ← Docusaurus-optimized extraction
         ↓ (Clean Text Content)
    [Text Chunking Service] ← Configurable chunk size/overlap
         ↓ (Content Chunks)
    [Embedding Generator] ← Cohere text embedding models
         ↓ (Vector Embeddings + Metadata)
    [Qdrant Storage] ← Vector database with URL/section filtering
         ↓ (Stored vectors ready for RAG)
    [Similarity Search Interface]
```

### Key Design Decisions

1. **URL Discovery Strategy**: Implement both sitemap parsing and web crawling fallback for comprehensive page discovery
2. **Content Extraction**: Use BeautifulSoup with CSS selectors optimized for Docusaurus-generated HTML structure
3. **Chunking Strategy**: Overlapping chunks with configurable size (512-1024 tokens) to maintain context
4. **Embedding Model**: Cohere's multilingual-22-12 model for technical content understanding
5. **Qdrant Configuration**: Cosine distance metric with metadata payload schema for filtering
6. **Re-indexing Strategy**: Idempotent operations with content hash comparison to detect updates

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: requests, beautifulsoup4, cohere, qdrant-client, python-dotenv, lxml
**Storage**: Qdrant Cloud vector database (external), local configuration files
**Testing**: pytest with integration tests for API calls and vector operations
**Target Platform**: Linux server environment (Vercel deployment compatible)
**Project Type**: Single service application for RAG ingestion pipeline
**Performance Goals**: Process entire book website within 30 minutes, 99% embedding success rate, 90% precision/recall for similarity search
**Constraints**: Cohere API rate limits, Qdrant Cloud Free Tier limitations, environment-based configuration only
**Scale/Scope**: Single Vercel book website (https://new-book-physical-ai.vercel.app/), multiple chapters and sections to be ingested

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Technical Accuracy Validation
- Verify all technical claims align with official documentation for robotics, AI, ROS 2, Gazebo, Isaac, and VLA modules
- Ensure zero hallucination tolerance for robotics and AI frameworks is maintained
- Validate code examples follow PEP8, rclpy conventions, and URDF/SDF standards

### Consistency and Clarity Validation
- Confirm terminology consistency across all chapters/modules
- Verify content clarity for students with diverse CS and robotics backgrounds
- Check adherence to unified chapter structure (intro, outcomes, concepts, examples, exercises)

### AI-Native Structure Validation
- Ensure content is RAG-friendly with short paragraphs and clean headings
- Verify modular, chunkable structure for efficient information retrieval
- Confirm summaries exist at end of each section for RAG use

### Reproducibility Validation
- Validate all code examples can run on specified environments (Ubuntu 22.04 with ROS 2 Humble/Iron)
- Confirm all robotics pipelines are fully reproducible
- Check that all dependencies are properly specified

### Pedagogical Quality Validation
- Verify clear learning outcomes for each section
- Ensure practical examples and executable code are included
- Confirm diagrams are referenced textually for RAG use

### Maintainability Validation
- Confirm Docusaurus/Markdown structure is maintainable
- Verify compatibility with GitHub Pages deployment
- Check uniform file naming, folder structure, and sidebar hierarchy

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
rag_pipeline/
├── src/
│   ├── __init__.py
│   ├── main.py                 # Entry point for the ingestion pipeline
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py         # Environment-based configuration
│   ├── ingestion/
│   │   ├── __init__.py
│   │   ├── url_discovery.py    # URL discovery strategy (sitemap vs crawl)
│   │   ├── content_fetcher.py  # HTML fetch and content extraction
│   │   └── content_processor.py # Content extraction optimized for Docusaurus
│   ├── chunking/
│   │   ├── __init__.py
│   │   └── text_chunker.py     # Chunking with size and overlap tradeoffs
│   ├── embedding/
│   │   ├── __init__.py
│   │   └── generator.py        # Cohere embedding generation
│   ├── storage/
│   │   ├── __init__.py
│   │   └── qdrant_client.py    # Qdrant storage and retrieval
│   └── utils/
│       ├── __init__.py
│       ├── logging.py          # Logging for ingestion progress and failures
│       └── validators.py       # Validation utilities
├── tests/
│   ├── unit/
│   │   ├── test_url_discovery.py
│   │   ├── test_content_extraction.py
│   │   ├── test_chunking.py
│   │   ├── test_embedding.py
│   │   └── test_qdrant_storage.py
│   ├── integration/
│   │   ├── test_end_to_end_ingestion.py
│   │   └── test_similarity_search.py
│   └── fixtures/
│       └── sample_content.html
├── scripts/
│   └── run_ingestion.py        # Script to run the complete pipeline
├── requirements.txt            # Dependencies: requests, beautifulsoup4, cohere, qdrant-client, python-dotenv, lxml
└── .env.example               # Example environment file
```

**Structure Decision**: Single project structure chosen for the RAG ingestion pipeline with clear separation of concerns across modules: ingestion (URL discovery, content fetching), chunking, embedding, and storage layers.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |

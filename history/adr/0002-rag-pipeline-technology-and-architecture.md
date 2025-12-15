# ADR-0002: RAG Pipeline Technology and Architecture

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-15
- **Feature:** 001-rag-pipeline
- **Context:** The RAG pipeline for the Physical AI & Humanoid Robotics textbook requires a robust architecture for ingesting content from a Vercel-deployed book website, extracting clean textual content, chunking it semantically, generating embeddings, and storing them in a vector database for semantic retrieval. This decision cluster encompasses the entire technology stack and architectural approach for the backend processing pipeline.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

- Language: Python 3.11+ for data processing and AI integration
- Content Discovery: Hybrid approach using sitemap parsing with web crawling fallback
- Content Extraction: BeautifulSoup4 with Docusaurus-specific CSS selectors for clean content extraction
- Text Processing: Custom chunking with 800-token chunks and 100-token overlap for semantic coherence
- Embedding Generation: Cohere's embed-multilingual-v3.0 model with 768-dimensional vectors
- Vector Storage: Qdrant Cloud vector database with cosine similarity metric
- Configuration: Environment variables with python-dotenv for deployment flexibility
- Testing: pytest for unit and integration testing
- Architecture: Modular design with separation of concerns (ingestion, processing, embedding, storage modules)

<!-- For technology stacks, list all components:
     - Framework: Next.js 14 (App Router)
     - Styling: Tailwind CSS v3
     - Deployment: Vercel
     - State Management: React Context (start simple)
-->

## Consequences

### Positive

- Cohere embeddings provide high-quality semantic representations for technical content
- Qdrant offers efficient similarity search with metadata filtering capabilities
- Hybrid URL discovery ensures comprehensive content coverage
- Docusaurus-aware extraction preserves document structure while removing boilerplate
- 800-token chunks balance context preservation with search precision
- Modular architecture enables independent development and testing of pipeline components
- Environment-based configuration supports multiple deployment environments
- Content hashing enables efficient re-indexing by detecting changes

### Negative

- Dependency on proprietary Cohere API for embeddings (cost and vendor lock-in)
- Qdrant Cloud introduces external service dependency and potential availability concerns
- Sitemap + crawling approach may miss dynamically generated content
- Fixed chunk size may not optimally handle all content types
- Python-based processing may be slower than compiled alternatives for large datasets
- Complex pipeline has multiple failure points that need monitoring

## Alternatives Considered

Alternative Stack A: OpenAI embeddings + Pinecone + Scrapy
- Pros: Mature ecosystem, good documentation, strong vector search capabilities
- Cons: Higher cost, potential vendor lock-in, different API patterns

Alternative Stack B: Hugging Face Transformers + FAISS + Requests
- Pros: Open source, no vendor lock-in, full control over embedding models
- Cons: More complex setup, self-hosting requirements, larger resource footprint

Alternative Stack C: LangChain framework + various vector stores
- Pros: Pre-built RAG components, abstraction layers, community support
- Cons: Additional abstraction layer, potential performance overhead, learning curve for framework

The chosen approach balances proven technology, cost-effectiveness, and implementation complexity while meeting the specific requirements for technical content processing.

## References

- Feature Spec: /media/fuzail/Work Data/GIAIC/SDD Hackathon/new-book/specs/001-rag-pipeline/spec.md
- Implementation Plan: /media/fuzail/Work Data/GIAIC/SDD Hackathon/new-book/specs/001-rag-pipeline/plan.md
- Related ADRs: none
- Evaluator Evidence: /media/fuzail/Work Data/GIAIC/SDD Hackathon/new-book/history/prompts/001-rag-pipeline/0003-rag-pipeline-plan-generation.plan.prompt.md

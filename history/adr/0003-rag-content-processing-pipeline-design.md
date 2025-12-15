# ADR-0003: RAG Content Processing Pipeline Design

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-15
- **Feature:** 001-rag-pipeline
- **Context:** The RAG pipeline requires a robust content processing workflow that handles URL discovery, content extraction, text chunking, embedding generation, and vector storage. This decision cluster encompasses the architectural approach for processing book content from the Physical AI & Humanoid Robotics textbook for semantic retrieval.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

- URL Discovery: Hybrid approach using sitemap.xml parsing with web crawling fallback
- Content Extraction: BeautifulSoup with Docusaurus-specific CSS selectors targeting content areas while excluding navigation, headers, footers
- Text Chunking: Semantic chunking with 800-token chunks and 100-token overlap to maintain context
- Embedding Pipeline: Sequential processing of chunks through Cohere API with error handling and rate limiting
- Storage Strategy: Idempotent upsert operations with content hash comparison for change detection
- Pipeline Architecture: Modular design with separate modules for ingestion, processing, embedding, and storage
- Error Handling: Comprehensive retry mechanisms with exponential backoff for API calls
- Metadata Management: Rich metadata storage including URL, title, section, and chunk index for filtering

<!-- For technology stacks, list all components:
     - Framework: Next.js 14 (App Router)
     - Styling: Tailwind CSS v3
     - Deployment: Vercel
     - State Management: React Context (start simple)
-->

## Consequences

### Positive

- Hybrid discovery approach ensures comprehensive coverage of website content
- Docusaurus-aware extraction provides clean content without navigation elements
- Overlapping chunks maintain context across semantic boundaries
- Content hash comparison enables efficient incremental updates
- Modular architecture allows independent scaling and maintenance of pipeline components
- Rich metadata enables precise filtering and retrieval
- Robust error handling increases pipeline reliability
- Sequential processing ensures consistent ordering and state management

### Negative

- Complex pipeline has multiple failure points requiring comprehensive monitoring
- Sitemap + crawling approach may be slower than direct URL lists
- Overlapping chunks increase storage and processing overhead
- Sequential processing may be slower than parallel approaches for large sites
- Hash-based change detection requires additional storage for hash values
- Rate limiting may slow down processing for large websites
- Complex error handling adds implementation complexity

## Alternatives Considered

Alternative Pipeline A: Direct API + Bulk Processing
- Pros: Faster processing, simpler error handling, direct integration with source
- Cons: Requires API access which may not be available, less flexible for static sites

Alternative Pipeline B: Real-time Processing on Query
- Pros: Always up-to-date content, no storage overhead for intermediate results
- Cons: Higher latency for queries, more complex real-time processing, less efficient for repeated queries

Alternative Pipeline C: Third-party RAG Service (e.g., VectorFlow, Unstructured.io)
- Pros: Managed service, less implementation work, built-in best practices
- Cons: Less control over processing, potential cost at scale, vendor lock-in

The chosen approach provides a good balance between control, performance, and maintainability while meeting the specific requirements for processing technical book content.

## References

- Feature Spec: /media/fuzail/Work Data/GIAIC/SDD Hackathon/new-book/specs/001-rag-pipeline/spec.md
- Implementation Plan: /media/fuzail/Work Data/GIAIC/SDD Hackathon/new-book/specs/001-rag-pipeline/plan.md
- Related ADRs: ADR-0002 (RAG Pipeline Technology and Architecture)
- Evaluator Evidence: /media/fuzail/Work Data/GIAIC/SDD Hackathon/new-book/history/prompts/001-rag-pipeline/0003-rag-pipeline-plan-generation.plan.prompt.md

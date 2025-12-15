# ADR-0004: RAG Data Model and Storage Strategy

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-15
- **Feature:** 001-rag-pipeline
- **Context:** The RAG pipeline requires a well-designed data model for storing content chunks, embeddings, and pipeline metadata. This decision cluster encompasses the entity design, storage approach, and metadata management strategy for the Physical AI & Humanoid Robotics textbook content.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

- Data Entities: BookContentChunk, VectorEmbedding, and IngestionPipeline entities with clear relationships
- Chunk Structure: Contains content, URL, title, section, chunk_index, content_hash, and timestamps
- Embedding Storage: 768-dimensional vectors stored with model metadata and chunk references
- Metadata Schema: URL, title, section, and chunk_index as searchable/filterable fields in Qdrant payload
- Content Hashing: SHA256 hash for change detection and idempotent operations
- Pipeline Tracking: Comprehensive ingestion pipeline state tracking with progress metrics
- Validation Rules: Content length limits, URL format validation, vector dimension validation
- Relationship Model: One-to-one relationship between BookContentChunk and VectorEmbedding

<!-- For technology stacks, list all components:
     - Framework: Next.js 14 (App Router)
     - Styling: Tailwind CSS v3
     - Deployment: Vercel
     - State Management: React Context (start simple)
-->

## Consequences

### Positive

- Rich metadata enables precise filtering and semantic search capabilities
- Content hashing enables efficient incremental updates and idempotent operations
- Clear entity relationships simplify data management and querying
- Validation rules ensure data quality and consistency
- Comprehensive pipeline tracking enables monitoring and debugging
- Timestamps allow temporal queries and version tracking
- Stable chunk identifiers (URL + chunk_index) enable consistent referencing
- Separation of content and embeddings allows independent querying

### Negative

- Additional storage overhead for metadata and hash values
- Complex validation rules may impact ingestion performance
- Fixed schema may limit flexibility for future content types
- Hash comparison requires additional computation during ingestion
- Multiple entities increase query complexity
- Schema changes require careful migration planning
- Large vector storage may increase costs at scale
- Complex relationships require careful transaction management

## Alternatives Considered

Alternative Data Model A: Single Combined Entity
- Pros: Simpler schema, fewer joins, easier to manage
- Cons: Less flexible querying, larger individual records, less efficient updates

Alternative Data Model B: Document-based Storage (MongoDB)
- Pros: Flexible schema, native text search, good for content storage
- Cons: Less efficient for vector similarity search, no native vector operations

Alternative Data Model C: Graph Database (Neo4j)
- Pros: Natural representation of content relationships, powerful traversal queries
- Cons: Complex for vector similarity search, additional infrastructure, learning curve

The chosen approach provides a good balance between query flexibility, storage efficiency, and the specific requirements for RAG applications with technical content.

## References

- Feature Spec: /media/fuzail/Work Data/GIAIC/SDD Hackathon/new-book/specs/001-rag-pipeline/spec.md
- Implementation Plan: /media/fuzail/Work Data/GIAIC/SDD Hackathon/new-book/specs/001-rag-pipeline/plan.md
- Related ADRs: ADR-0002 (RAG Pipeline Technology and Architecture)
- Evaluator Evidence: /media/fuzail/Work Data/GIAIC/SDD Hackathon/new-book/history/prompts/001-rag-pipeline/0003-rag-pipeline-plan-generation.plan.prompt.md

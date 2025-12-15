# Research Document: RAG Pipeline Implementation

## Decision: URL Discovery Strategy
**Rationale**: For comprehensive discovery of pages from the Vercel site, a hybrid approach combining sitemap parsing and web crawling is optimal. Sitemap parsing provides a reliable list of indexed pages, while web crawling serves as a fallback to discover any pages not included in the sitemap.

**Alternatives considered**:
- Sitemap only: May miss pages not submitted to sitemap
- Web crawling only: More complex, may miss pages or get stuck in loops
- Manual URL list: Not maintainable for dynamic sites

**Selected approach**: Primary sitemap parsing with crawling fallback for comprehensive coverage.

## Decision: HTML Content Extraction Method
**Rationale**: Docusaurus-generated sites have consistent HTML structure with specific CSS classes for content areas. Using BeautifulSoup with targeted CSS selectors will effectively extract clean content while excluding navigation, headers, and footers.

**Key Docusaurus elements to target**:
- Content area: Usually within `<div class="container markdown">` or similar
- Navigation: Elements with classes like `navbar`, `menu`, `sidebar`
- Code blocks: `<pre>` and `<code>` tags to preserve technical content
- Headings: `<h1>`-`<h6>` to maintain document structure

**Alternatives considered**:
- Generic content extraction libraries (like Readability) - may not be optimized for Docusaurus
- Regular expressions - fragile and hard to maintain
- Custom HTML parsing - reinventing the wheel

## Decision: Chunk Size and Overlap Tradeoffs
**Rationale**: For RAG accuracy with technical content, chunks should balance context preservation with search precision. Based on research, 512-1024 tokens is optimal for technical documentation.

**Selected parameters**:
- Chunk size: 800 tokens (approximately 600-800 words)
- Overlap: 100 tokens to maintain context across boundaries
- Minimum chunk size: 100 tokens to avoid overly small fragments

**Alternatives considered**:
- Larger chunks (1500+ tokens): Better context but reduced precision
- Smaller chunks (200-400 tokens): Better precision but potential context loss
- Variable chunking based on document structure: More complex but potentially better

## Decision: Cohere Embedding Model Selection
**Rationale**: For technical content in the Physical AI and robotics domain, Cohere's multilingual embedding model provides good performance for English technical documentation.

**Selected model**: `embed-multilingual-v2.0` - suitable for technical content with good performance on non-English fragments if present

**Vector dimensionality**: 768 dimensions (model default) - provides good balance between storage efficiency and semantic representation quality

**Alternatives considered**:
- `embed-english-v2.0`: Good for English-only content but less flexible
- `embed-english-light-v2.0`: More efficient but potentially lower quality for complex technical content
- Other embedding providers (OpenAI, Hugging Face): Would require different integration

## Decision: Qdrant Collection Configuration
**Rationale**: Qdrant configuration needs to support efficient similarity search with metadata filtering capabilities for the RAG application.

**Selected configuration**:
- Distance metric: Cosine similarity (standard for embedding vectors)
- Vector size: 768 (matching Cohere embedding dimensions)
- Payload schema:
  - `url`: exact match for page identification
  - `title`: text match for search
  - `section`: exact match for filtering
  - `chunk_index`: integer for ordering
  - `content`: text for full-text search if needed

**Alternatives considered**:
- Euclidean distance: Less appropriate for embedding vectors
- Different payload schemas: Could work but this covers all requirements
- Other vector databases: Qdrant was specified in requirements

## Decision: Re-indexing Strategy
**Rationale**: To handle site updates, the system needs to detect content changes and update only affected vectors while maintaining existing ones.

**Selected approach**:
- Content hashing: Calculate hash of extracted content before chunking
- Vector ID generation: Use URL + chunk_index as stable identifier
- Idempotent operations: Always upsert vectors to allow safe re-runs
- Change detection: Compare content hash with stored metadata to identify updates

**Alternatives considered**:
- Full re-index: Wasteful of API calls and processing time
- Timestamp-based detection: May miss content changes without timestamp updates
- Manual triggers: Not automated or maintainable
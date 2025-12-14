# ADR-0001: Separate Landing Page from Textbook Content

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Superseded
- **Date:** 2025-12-14
- **Feature:** 001-physical-ai-textbook
- **Context:** The Physical AI & Humanoid Robotics textbook project requires a clear separation between marketing/exploration landing page and the actual textbook content to improve user experience and navigation structure.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

Route textbook documentation to /book path while serving a custom marketing/exploration landing page at the root path. This involves:
- Changing Docusaurus routeBasePath from '/' to '/book'
- Creating a custom React landing page at src/pages/index.js
- Updating navigation links to point to /book section
- Maintaining all existing textbook content under /book route

## Consequences

### Positive

- Improved user experience with dedicated marketing/exploration page at root
- Clear separation between promotional content and educational content
- Better SEO with dedicated landing page optimized for discovery
- Enhanced visual appeal with custom UI elements and features showcase
- Easier to direct new users to the textbook through prominent CTA buttons
- Follows industry standard pattern seen in similar educational platforms

### Negative

- Additional complexity in routing and navigation configuration
- Need to update all internal links to point to /book path
- Slight increase in initial setup and maintenance overhead
- Potential for broken links if not all references are updated properly

## Alternatives Considered

Alternative A: Keep current approach with textbook index at root
- Pros: Simpler routing, no additional configuration needed
- Cons: Less appealing user experience, no marketing/exploration page, not following industry best practices

Alternative B: Create separate subdomain for landing page (landing.example.com vs book.example.com)
- Pros: Complete separation of concerns, independent deployments possible
- Cons: More complex infrastructure, additional domain management, increased cost

Alternative C: Use Docusaurus custom home page feature with extended MDX
- Pros: Simpler implementation, stays within Docusaurus conventions
- Cons: Less flexibility in UI design, harder to create visually appealing landing page

The chosen approach balances simplicity with user experience improvements while maintaining the existing documentation structure.

## References

- Feature Spec: specs/001-physical-ai-textbook/spec.md
- Implementation Plan: specs/001-physical-ai-textbook/plan.md
- Related ADRs: none
- Evaluator Evidence: history/prompts/001-physical-ai-textbook/0013-create-landing-page-for-textbook.green.prompt.md

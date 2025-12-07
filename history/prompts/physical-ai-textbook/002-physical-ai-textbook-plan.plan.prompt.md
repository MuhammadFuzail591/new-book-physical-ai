---
id: 002
title: physical-ai-textbook-plan
stage: plan
date: 2025-12-07
surface: agent
model: claude-sonnet-4-5-20250929
feature: physical-ai-textbook
branch: 001-physical-ai-textbook
user: fuzail
command: /sp.plan
labels: [planning, textbook, robotics, ai, docusaurus]
links:
  spec: specs/001-physical-ai-textbook/spec.md
  plan: specs/001-physical-ai-textbook/plan.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-physical-ai-textbook/plan.md
 - specs/001-physical-ai-textbook/research.md
 - specs/001-physical-ai-textbook/data-model.md
 - specs/001-physical-ai-textbook/quickstart.md
 - specs/001-physical-ai-textbook/contracts/textbook-components.yaml
tests:
 - constitution compliance check
 - project structure validation
 - technical context verification
---

## Prompt

Project: AI-Native Technical Textbook on Physical AI & Humanoid Robotics
Platform: Docusaurus (Markdown/MDX)
Objective: Generate a complete implementation plan for the entire 14-chapter textbook based on the approved Constitution and Full-Book Specification.
The plan must define the full development roadmap, chapter sequencing, file structure, MDX layout, RAG preparation, and the integration requirements for ROS 2, Gazebo, Unity, NVIDIA Isaac, VLA, and Capstone content.

------------------------------------------
PLAN SCOPE
------------------------------------------

The plan MUST cover:

1. **Book-Wide Planning**
   - Docusaurus folder structure
   - Sidebar hierarchy
   - MDX file layout conventions
   - Asset and diagram management
   - Shared components (tabs, glossary, callouts, diagrams)
   - RAG optimization strategies
   - Style and tone consistency
   - Versioning and deployment

2. **Chapter-by-Chapter Plan**
   For each of the 14 chapters:
   - Chapter objectives
   - Section-by-section plan
   - Required code examples
   - Required diagrams (Mermaid / conceptual text descriptions)
   - Example workflows (ROS 2 / Gazebo / Isaac / VLA)
   - Cross-chapter references
   - Expected file paths
   - Ensure MDX + Docusaurus compatibility

3. **Simulation & Robotics Plan**
   - ROS 2 environment setup
   - Gazebo simulation workflow
   - Isaac Sim pipeline
   - Nav2 + VSLAM plan
   - Vision-Language-Action plan
   - Capstone integration plan (voice → LLM → ROS 2 → navigation → perception → manipulation)

4. **Authoring Workflow Steps**
   - What gets implemented first
   - How to sequence chapter creation
   - Plan for RAG testing
   - Plan for deployment pipeline
   - Git branching and PR flow

------------------------------------------
DOCUSAURUS STRUCTURE REQUIREMENTS
------------------------------------------

Your plan MUST output:

- The exact directory tree:

  ./docs/physical-ai/
      chapter-01-introduction.mdx
      chapter-02-humanoid-sensors.mdx
      chapter-03-ros2-architecture.mdx
      ...
      chapter-14-capstone.mdx

- Shared components folder:
  ./src/components/physical-ai/

- Images + diagrams folder:
  ./static/img/physical-ai/

- Glossary plan:
  ./docs/physical-ai/glossary.mdx

------------------------------------------
RAG OPTIMIZATION REQUIREMENTS
------------------------------------------

Plan MUST include:

- Section chunking strategy
- Heading guidelines
- Internal linking rules
- Glossary and concept anchors
- Summaries at the end of each section
- "Retrieval hotspots" for QA systems
- Content uniformity rules

------------------------------------------
CHAPTER PLAN STRUCTURE (FOR EACH OF THE 14 CHAPTERS)
------------------------------------------

For every chapter, the plan MUST define:

1. **File Path**
   e.g. ./docs/physical-ai/chapter-03-ros2-architecture.mdx

2. **Section Breakdown**
   - List all major sections
   - Detail content for each
   - Expected diagrams
   - Expected code blocks
   - Practical examples

3. **Required Examples**
   - ROS 2 nodes
   - Launch files
   - URDF snippets
   - Gazebo worlds
   - Isaac pipelines
   - VSLAM examples
   - Whisper integration
   - VLA planning examples

4. **Diagrams**
   - Mermaid diagrams
   - Conceptual diagrams (text-described)

5. **Glossary Terms**
   - List of terms introduced in the chapter

6. **Dependencies**
   - What knowledge from previous chapters the student must understand
   - What later chapters depend on this one

7. **Acceptance Criteria**
   - Must satisfy the matching items in the specification
   - Must build cleanly in Docusaurus
   - Must conform to Constitution rules

------------------------------------------
CAPSTONE PLANNING REQUIREMENTS
------------------------------------------

The plan MUST include an entire section devoted to the capstone:

- Voice → Whisper → LLM → Task Plan → ROS 2 Action Graph
- Navigation through Nav2 + VSLAM
- Object detection (Isaac / CV models)
- Manipulation pipeline
- Simulation testing + Jetson deployment
- Demo recording instructions

------------------------------------------
OUTPUT REQUIREMENTS
------------------------------------------

Generate:

- A hierarchical, multi-level plan
- With itemized steps
- Chapter sequencing
- Implementation order
- Build + deployment plan
- Component creation plan
- RAG indexing plan
- Testing plan

------------------------------------------
ACCEPTANCE CRITERIA
------------------------------------------

The plan MUST:

- Fully align with the Book Specification and Constitution
- Provide a detailed roadmap for generating all 14 chapters
- Include Docusaurus, MDX, and RAG-specific constraints
- Create a clear development sequence for Claude Code
- Be detailed enough to feed directly into /sp.tasks and /sp.implement
- Ensure absolutely no hallucinated robotics content
- Include a full breakdown of ROS 2, Gazebo, Isaac, VLA, and Capstone components

## Response snapshot

Completed comprehensive implementation plan for the AI-Native Technical Textbook on Physical AI & Humanoid Robotics. The plan includes:

- Technical Context: Docusaurus/MDX, ROS 2 Humble/Iron, Ubuntu 22.04 environment
- Constitution Check: All validation requirements met for technical accuracy, consistency, AI-native structure, reproducibility, pedagogical quality, and maintainability
- Project Structure: Complete Docusaurus textbook structure with 14 chapters, shared components, and assets organization
- Research: Detailed technology research covering Docusaurus, ROS 2, Gazebo, Isaac Sim, VLA systems, and RAG optimization
- Data Model: Comprehensive entity definitions for chapters, sections, code examples, diagrams, exercises, and technology-specific components
- Quickstart Guide: Complete setup and development workflow
- Component Contracts: API specifications for textbook components

The plan is ready to feed into /sp.tasks for generating specific implementation tasks.

## Outcome

- ✅ Impact: Created complete implementation plan for 14-chapter textbook with all required components
- 🧪 Tests: All constitution compliance checks passed, technical context validated
- 📁 Files: Created plan.md, research.md, data-model.md, quickstart.md, and contracts/
- 🔁 Next prompts: Ready for /sp.tasks to generate implementation tasks
- 🧠 Reflection: Plan comprehensively covers all requirements with proper sequencing and dependencies

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - All validation criteria met
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
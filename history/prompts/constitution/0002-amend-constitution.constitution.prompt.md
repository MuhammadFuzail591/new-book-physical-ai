<!--
id: 0002
title: Amend Constitution
stage: constitution
date: 2025-12-07
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: Muhammad Fuzail
command: /sp.constitution
labels: [constitution, governance, robotics, ai-textbook]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
  - .specify/templates/plan-template.md
  - .specify/templates/spec-template.md
  - .specify/templates/tasks-template.md
tests:
  - null
--->

## Prompt

```
/sp.constitution

Project: AI-Native Technical Textbook on Physical AI & Humanoid Robotics
Platform: Docusaurus (Markdown/MDX), GitHub Pages, Claude Code, Spec-Kit Plus
Additional Systems: RAG chatbot (OpenAI Agents/ChatKit SDKs + FastAPI + Neon Postgres + Qdrant Cloud)

Core principles:
- Technical accuracy across robotics, AI, ROS 2, Gazebo, Isaac, and VLA modules
- Consistency and clarity for students with CS and robotics backgrounds
- AI-native textbook structure (RAG-friendly, modular, chunkable)
- Reproducibility of all code and robotics pipelines
- Terminology consistency across all chapters
- Pedagogical quality: outcomes, examples, code, diagrams, summaries
- Maintainable Docusaurus/Markdown structure
- Zero hallucination tolerance for robotics and AI frameworks

Quality standards:
- All chapters follow a unified structure (intro, outcomes, concepts, examples, exercises)
- All explanations must be accurate according to course details (ROS 2, Gazebo, Isaac, VSLAM, Nav2, VLA)
- All code follows standards:
  - Python code: PEP8
  - ROS 2: rclpy conventions, correct node/topic/action patterns
  - URDF/SDF: validated models
- All content must be RAG-friendly:
  - short paragraphs
  - clean headings
  - no filler text
  - summary at end of each section
- Every chapter must ensure concept traceability (no contradictions)
- All diagrams must be referenced textually for RAG use
- English as primary language; Urdu only via optional translation feature
- If personalization implemented, it must never alter technical correctness
- If authentication implemented, it must use BetterAuth and structured background questions

Constraints:
- Must be deployable on GitHub Pages without build errors
- Must use Docusaurus formatting consistently
- All Markdown must pass linting and formatting rules
- All content must align with official course modules and weekly schedule
- RAG chatbot must rely only on book text (no external hallucinated knowledge)
- Must maintain uniform file naming, folder structure, and sidebar hierarchy
- Optional features (subagents, auth, personalization, translation) must not conflict with base textbook content

Success criteria:
- Book successfully builds and publishes on GitHub Pages
- RAG chatbot answers questions accurately using only content from the textbook
- Zero technical inaccuracies in ROS 2, Gazebo, Unity, Isaac, VSLAM, Nav2
- Code examples run on Ubuntu 22.04 with ROS 2 Humble/Iron
- All chapters follow the same structural template
- No hallucinations when answering robotics questions
- High RAG-quality chunking (validated by querying several chapters)
- Optional: working personalization engine per chapter
- Optional: working Urdu translation button
- Optional: BetterAuth implementation
- Optional: subagents and reusable intelligence integrated
```

## Response snapshot

Updated the project constitution at `.specify/memory/constitution.md` with the specific details for the AI-Native Technical Textbook on Physical AI & Humanoid Robotics project. The constitution now includes:

1. Core Principles:
   - Technical Accuracy: Ensuring all content is technically accurate across robotics, AI, ROS 2, Gazebo, Isaac, and VLA modules
   - Consistency and Clarity: Maintaining consistency for students with diverse backgrounds
   - AI-Native Structure: RAG-friendly, modular, and chunkable content structure
   - Reproducibility: All code and robotics pipelines must be reproducible
   - Pedagogical Quality: High-quality educational content with outcomes, examples, and summaries
   - Maintainable Structure: Docusaurus/Markdown structure that's maintainable and deployable

2. Quality Standards: Detailed standards for chapter structure, code quality, RAG-friendliness, and content quality

3. Constraints: Deployment, formatting, and content alignment requirements

4. Governance: Amendment procedures and compliance requirements

Additionally, updated the following templates to align with the new constitution:
- `.specify/templates/plan-template.md`: Added detailed constitution checks for each principle
- `.specify/templates/spec-template.md`: Added constitution alignment requirements
- `.specify/templates/tasks-template.md`: Added constitution compliance requirements throughout implementation

## Outcome

- ✅ Impact: Project constitution updated with specific principles for robotics/AI textbook project and templates aligned with new principles
- 🧪 Tests: No tests required for this governance update
- 📁 Files: 4 files updated to reflect new constitution and alignment requirements
- 🔁 Next prompts: Ready for feature specification and planning based on new constitution
- 🧠 Reflection: Constitution now properly reflects the specific requirements of the AI-Native Technical Textbook project with clear principles for technical accuracy, consistency, RAG-friendliness, and pedagogical quality

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): Not applicable
- Prompt variant (if applicable): Not applicable
- Next experiment (smallest change to try): Begin feature specification based on new constitution
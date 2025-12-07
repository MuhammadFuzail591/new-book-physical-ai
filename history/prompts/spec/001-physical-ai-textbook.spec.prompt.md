---
id: 001
title: physical-ai-textbook
stage: spec
date: 2025-12-07
surface: agent
model: claude-sonnet-4-5-20250929
feature: physical-ai-textbook
branch: 001-physical-ai-textbook
user: fuzail
command: /sp.specify
labels: [specification, textbook, robotics, ai]
links:
  spec: specs/001-physical-ai-textbook/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-physical-ai-textbook/spec.md
 - specs/001-physical-ai-textbook/checklists/requirements.md
tests:
 - Docusaurus build test
 - Content structure validation
---

## Prompt

/sp.specify

Project: AI-Native Technical Textbook on Physical AI & Humanoid Robotics
Platform: Docusaurus (Markdown/MDX)
Purpose: Generate a full-book specification covering all 14 chapters, Docusaurus structure, MDX formatting rules, navigation hierarchy, code example standards, diagrams, RAG optimization, and cross-chapter dependencies. This becomes the master specification driving all /sp.plan → /sp.tasks → /sp.implement stages.

BOOK DELIVERY REQUIREMENT:
The entire textbook MUST be built and published using Docusaurus with MDX pages.
------------------------------------------
DOCUSAURUS-SPECIFIC REQUIREMENTS (MUST APPLY TO ENTIRE BOOK)
------------------------------------------

Folder Structure Requirements:
- All chapters must live under:
  `./docs/physical-ai/`
- Each chapter is one MDX file OR a folder with an index.mdx + subpages.
- Use a clean URL structure (no .html suffixes).


- Sidebar groups must follow module structure:
  - Foundations
  - ROS2
  - Digital Twin
  - NVIDIA Isaac
  - VLA & Conversational Robotics
  - Capstone

MDX Formatting Rules:
- Use MDX headings: #, ##, ###
- Use Docusaurus admonitions:
  :::note
  :::tip
  :::warning
- Use MDX components:
  - Code blocks: ```python
  - Tabs for variations
  - Mermaid diagrams for flow visuals
- All images referenced from:
  `./static/img/physical-ai/`

RAG + MDX Formatting Constraints:
- Short paragraphs (≤5–6 sentences)
- Headings must match semantic concepts exactly
- Blockquotes used for highlights
- Bullet/numbered lists encouraged
- Subsections < 400 words each for optimal chunking
- End each section with a mini-summary for retrieval

Content Reusability:
- Create shared components under `./src/components/physical-ai/`
- Common diagrams as reusable components
- Glossary as a dedicated page:
  `./docs/physical-ai/glossary.mdx`

Deployment Constraints:
- All MDX must pass the Docusaurus markdown parser
- No broken links, images, or imports
- Final build must succeed with:
  `npm run build`
- Publish using GitHub Pages workflow

------------------------------------------
CHAPTER LIST (14 chapters the specification must describe)
------------------------------------------

1. Introduction to Physical AI & Embodied Intelligence
2. Humanoid Robotics Landscape & Sensor Foundations

3. Understanding the Robotic Nervous System: ROS 2 Architecture
4. Nodes, Topics, Services & Actions in ROS 2
5. Building ROS 2 Packages, Launch Files & Parameters
6. URDF/SDF for Humanoid Robots

7. Gazebo Simulation: Physics, Sensors & World Building
8. Unity Visualization & Human-Robot Interaction

9. NVIDIA Isaac SDK & Isaac Sim Overview
10. AI Perception, Synthetic Data & Manipulation Pipelines
11. VSLAM, Navigation & Sim-to-Real Transfer Techniques

12. Voice-to-Action Robotics (Whisper + ROS 2)
13. Cognitive Planning with Vision-Language-Action Systems

14. Capstone Project: The Autonomous Humanoid

------------------------------------------
CHAPTER STRUCTURE (APPLIES TO EVERY CHAPTER)
------------------------------------------

Each chapter MUST have:
1. Frontmatter metadata (Docusaurus)
2. Chapter Overview
3. 4–7 Sections (clear semantics)
4. Practical Examples
5. Required Diagrams (Mermaid or text-descriptions)
6. Code Examples (ROS 2 / Python / Isaac / VLA depending on module)
7. Real-World Use Cases
8. Glossary Terms
9. Chapter Summary (RAG-friendly)
10. Exercises / Assessments

Each chapter must define:
- Section titles
- Content expectations
- Diagram requirements
- Code blocks (MDX fenced)
- Navigation ID (slug)
- Cross-links to previous chapters

------------------------------------------
BOOK-LEVEL SPECIFICATION REQUIREMENTS
------------------------------------------

The specification MUST include for each chapter:
- Purpose
- Detailed learning outcomes
- Required sections & subsections
- Required diagrams
- Required code examples & workflows
- Required glossary terms
- Dependencies on earlier chapters
- Required navigation hierarchy
- Docusaurus-compatible MDX structure
- RAG-friendly formatting rules
- Acceptance criteria

Additionally, for the whole book:
- A complete sidebar structure
- A global glossary page structure
- A shared component strategy
- An asset strategy (images/diagrams)
- Style rules: tone, pedagogy, format
- Simulation environment configuration rules
- Testing criteria for accurate builds

------------------------------------------
TECHNOLOGY-SPECIFIC REQUIREMENTS
------------------------------------------

ROS 2 Chapters (3–6):
- Explain rclpy, node lifecycle, QoS, launch files, URDF, SDF.
- Provide MDX code blocks runnable on Ubuntu 22.04.

Gazebo & Unity Chapters (7–8):
- Include world-building steps, physics parameters, sensor simulation setups.

NVIDIA Isaac Chapters (9–11):
- Include Omniverse USD workflows, synthetic data pipelines, perception stacks.

VLA Chapters (12–13):
- Whisper pipelines, LLM planning, ROS 2 actions integration.

Capstone Chapter:
- End-to-end integration: Whisper → LLM → ROS 2 → locomotion → manipulation → perception.
- Include deployment instructions for Jetson Orin.

------------------------------------------
ACCEPTANCE CRITERIA
------------------------------------------

- The output is a full-book specification describing all 14 chapters in detail.
- All structure must be MDX + Docusaurus compliant.
- All chapters must inherit the Constitution rules.
- All diagrams must be described for MDX.
- The final specification must enable Claude to generate chapter files with /sp.plan → /sp.tasks → /sp.implement.
- The document must be internally consistent and technically accurate.
- No hallucinated robotics content.
- Builds cleanly as a Docusaurus book.

## Response snapshot

Created comprehensive specification for AI-Native Technical Textbook on Physical AI & Humanoid Robotics with 14 chapters covering Physical AI, ROS 2, Gazebo, NVIDIA Isaac, VLA, and capstone integration. The specification includes user scenarios, functional requirements, success criteria, and detailed requirements for Docusaurus-based deployment with MDX formatting, RAG optimization, and cross-chapter dependencies.

## Outcome

- ✅ Impact: Created complete textbook specification with 14 chapters covering Physical AI & Humanoid Robotics
- 🧪 Tests: Specification validated against quality criteria checklist
- 📁 Files: Created spec.md and requirements checklist in specs/001-physical-ai-textbook/
- 🔁 Next prompts: Ready for /sp.plan to create implementation plan
- 🧠 Reflection: Specification successfully covers all required chapters with proper structure and pedagogical requirements

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - All validation criteria met
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
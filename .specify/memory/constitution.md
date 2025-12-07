<!--
Sync Impact Report:
Version change: 0.0.0 -> 1.0.0
Modified principles: All principles were updated based on user input.
Added sections: Quality Standards, Constraints, Success Criteria
Removed sections: None
Templates requiring updates:
- .specify/templates/plan-template.md: ⚠ pending
- .specify/templates/spec-template.md: ⚠ pending
- .specify/templates/tasks-template.md: ⚠ pending
- .specify/templates/commands/sp.analyze.md: ⚠ not found
- .specify/templates/commands/sp.adr.md: ⚠ not found
- .specify/templates/commands/sp.git.commit_pr.md: ⚠ not found
- .specify/templates/commands/sp.plan.md: ⚠ not found
- .specify/templates/commands/sp.constitution.md: ⚠ not found
- .specify/templates/commands/sp.tasks.md: ⚠ not found
- .specify/templates/commands/sp.checklist.md: ⚠ not found
- .specify/templates/commands/sp.clarify.md: ⚠ not found
- .specify/templates/commands/sp.implement.md: ⚠ not found
- .specify/templates/commands/sp.specify.md: ⚠ not found
Follow-up TODOs: TODO(RATIFICATION_DATE): Original adoption date for the constitution.
-->
# AI-Native Technical Textbook on Physical AI & Humanoid Robotics Constitution

## Core Principles

### I. Technical Accuracy
All content, explanations, and code examples MUST be technically accurate across robotics, AI, ROS 2, Gazebo, Isaac, and VLA modules. Zero hallucination tolerance for robotics and AI frameworks is enforced.

### II. Consistency and Clarity
All content MUST maintain consistency and clarity, especially for students with diverse backgrounds in Computer Science and robotics. Terminology MUST be consistent across all chapters.

### III. AI-Native Textbook Structure
The textbook MUST adopt an AI-native structure that is RAG-friendly, modular, and chunkable, facilitating efficient information retrieval and processing by AI systems. This includes short paragraphs, clean headings, no filler text, and a summary at the end of each section.

### IV. Reproducibility
All code and robotics pipelines presented in the textbook MUST be fully reproducible on specified environments (e.g., Ubuntu 22.04 with ROS 2 Humble/Iron).

### V. Pedagogical Quality
Content MUST adhere to high pedagogical quality standards, including clearly defined learning outcomes, relevant examples, executable code, illustrative diagrams, and concise summaries for each section.

### VI. Maintainable Docusaurus/Markdown Structure
The textbook MUST be built with a maintainable Docusaurus/Markdown structure, ensuring ease of updates, navigation, and deployment on GitHub Pages without build errors. Uniform file naming, folder structure, and sidebar hierarchy MUST be maintained.

## Quality Standards

- All chapters MUST follow a unified structure (introduction, learning outcomes, core concepts, practical examples, and exercises).
- All explanations MUST be accurate according to course details (ROS 2, Gazebo, Isaac, VSLAM, Nav2, VLA).
- All code MUST follow specified standards:
  - Python code: PEP8 compliance.
  - ROS 2: Adherence to `rclpy` conventions, correct node/topic/action patterns.
  - URDF/SDF: Validated models.
- All content MUST be RAG-friendly:
  - Short paragraphs.
  - Clean headings.
  - No filler text.
  - Summary at the end of each section.
- Every chapter MUST ensure concept traceability (no contradictions between sections or chapters).
- All diagrams MUST be referenced textually for RAG use.
- English as the primary language; Urdu only via an optional translation feature.
- If personalization is implemented, it MUST never alter technical correctness or factual accuracy.
- If authentication is implemented, it MUST use BetterAuth and structured background questions for user data collection.

## Constraints

- The textbook MUST be deployable on GitHub Pages without build errors.
- Docusaurus formatting MUST be used consistently throughout the project.
- All Markdown content MUST pass linting and formatting rules.
- All content MUST align with official course modules and the weekly schedule.
- The RAG chatbot MUST rely only on book text for its knowledge base (no external hallucinated knowledge).
- A uniform file naming, folder structure, and sidebar hierarchy MUST be maintained across the project.
- Optional features (subagents, authentication, personalization, translation) MUST not conflict with or compromise the integrity of the base textbook content.

## Governance

This Constitution supersedes all other practices and guidelines within the project. Amendments require thorough documentation, approval by the project lead, and a clear migration plan for any affected systems or content. All pull requests and code reviews MUST verify compliance with the principles and standards outlined herein. Complexity in design or implementation MUST be explicitly justified against the principle of simplicity.

**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE) | **Last Amended**: 2025-12-07

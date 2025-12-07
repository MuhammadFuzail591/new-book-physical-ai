# Data Model: AI-Native Technical Textbook on Physical AI & Humanoid Robotics

## Overview
This document defines the key entities and their relationships for the 14-chapter textbook on Physical AI & Humanoid Robotics. These entities represent the core concepts that will be covered across all chapters.

## Core Entities

### Textbook Chapter
**Description**: A major section of the textbook covering specific topics in Physical AI and Robotics
**Fields**:
- chapterId: string (e.g., "chapter-01-introduction")
- title: string (e.g., "Introduction to Physical AI & Embodied Intelligence")
- number: integer (1-14)
- slug: string (URL-friendly identifier)
- learningOutcomes: array of strings
- prerequisites: array of chapterIds
- dependencies: array of chapterIds
- sections: array of Section entities
- codeExamples: array of CodeExample entities
- diagrams: array of Diagram entities
- exercises: array of Exercise entities
- glossaryTerms: array of strings

### Section
**Description**: A subsection within a chapter that covers a specific concept or topic
**Fields**:
- sectionId: string
- title: string
- content: string (MDX-formatted)
- order: integer
- chapterId: string
- glossaryTerms: array of strings
- crossReferences: array of string references
- summary: string (for RAG)

### Code Example
**Description**: Executable code snippets that demonstrate concepts from the textbook
**Fields**:
- exampleId: string
- title: string
- language: string (python, bash, xml, etc.)
- code: string (the actual code content)
- description: string
- chapterId: string
- sectionId: string
- environment: string (e.g., "Ubuntu 22.04 + ROS 2 Humble")
- dependencies: array of strings
- executionInstructions: string

### Diagram
**Description**: Visual representations of concepts, system architectures, or workflows
**Fields**:
- diagramId: string
- title: string
- type: string (mermaid, conceptual, 3d-model, etc.)
- description: string
- chapterId: string
- sectionId: string
- content: string (Mermaid syntax or description)
- imageUrl: string (path to static image)

### Exercise
**Description**: Assessment problems at the end of each chapter to test understanding
**Fields**:
- exerciseId: string
- title: string
- description: string
- difficulty: enum (beginner, intermediate, advanced)
- type: enum (theoretical, practical, coding, analysis)
- chapterId: string
- solution: string
- hints: array of strings

### Glossary Term
**Description**: Technical terminology with definitions that are consistently used across the textbook
**Fields**:
- termId: string
- term: string
- definition: string
- chapterId: string
- usageExamples: array of strings
- relatedTerms: array of termIds

### Real-World Use Case
**Description**: Practical application examples showing how concepts are used in actual robotics projects
**Fields**:
- useCaseId: string
- title: string
- description: string
- chapterId: string
- technologiesUsed: array of strings
- implementationSteps: array of strings
- outcomes: array of strings

## Technology-Specific Entities

### ROS 2 Component
**Description**: ROS 2 specific entities like nodes, topics, services, actions
**Fields**:
- componentId: string
- name: string
- type: enum (node, topic, service, action, parameter)
- description: string
- codeExampleId: string
- chapterId: string

### URDF/SDF Model
**Description**: Robot description models for humanoid robots
**Fields**:
- modelId: string
- name: string
- type: enum (urdf, sdf)
- description: string
- joints: array of Joint entities
- links: array of Link entities
- chapterId: string

### Joint
**Fields**:
- jointId: string
- name: string
- type: enum (revolute, prismatic, fixed, continuous)
- parent: string (link name)
- child: string (link name)
- axis: object (x, y, z coordinates)
- limits: object (min, max, effort, velocity)

### Link
**Fields**:
- linkId: string
- name: string
- visual: object (geometry, material)
- collision: object (geometry)
- inertial: object (mass, inertia)

### Gazebo World
**Description**: Simulation environments for robot testing
**Fields**:
- worldId: string
- name: string
- description: string
- physicsEngine: string
- models: array of string references
- lighting: object
- chapterId: string

### Isaac Sim Component
**Description**: NVIDIA Isaac Sim specific entities
**Fields**:
- componentId: string
- name: string
- type: string (USD stage, synthetic data generator, perception pipeline)
- description: string
- chapterId: string
- codeExampleId: string

### VLA System
**Description**: Vision-Language-Action system components
**Fields**:
- systemId: string
- name: string
- components: array of string references (voice processing, LLM, action planning)
- description: string
- chapterId: string
- integrationSteps: array of strings

## Relationships

### Chapter Relationships
- Textbook Chapter [1] -- [0..n] Section
- Textbook Chapter [1] -- [0..n] Code Example
- Textbook Chapter [1] -- [0..n] Diagram
- Textbook Chapter [1] -- [0..n] Exercise
- Textbook Chapter [1] -- [0..n] Glossary Term
- Textbook Chapter [1] -- [0..n] Real-World Use Case

### Cross-Chapter Dependencies
- Textbook Chapter [0..n] -- [0..n] Textbook Chapter (prerequisites/dependencies)

### Technology Integration
- Section [1] -- [0..n] ROS 2 Component
- Section [1] -- [0..n] URDF/SDF Model
- Section [1] -- [0..n] Gazebo World
- Section [1] -- [0..n] Isaac Sim Component
- Section [1] -- [0..n] VLA System

## Validation Rules

### Content Validation
- Each chapter must have 4-7 sections
- Each section must have a summary for RAG optimization
- All code examples must be validated in Ubuntu 22.04 + ROS 2 Humble environment
- All diagrams must have textual descriptions for accessibility

### Consistency Validation
- All terminology must match glossary definitions
- Learning outcomes must align with section content
- Exercises must cover material from the chapter
- Cross-references must point to valid sections/chapters

### Technical Validation
- All ROS 2 code must follow rclpy conventions
- URDF/SDF models must be valid XML
- All simulation examples must be reproducible
- All Isaac Sim workflows must follow USD best practices

## State Transitions

### Content States
- DRAFT → REVIEW → APPROVED → PUBLISHED
- Each state has specific validation requirements
- State transitions require specific approvals

This data model provides the structural foundation for organizing and managing all content in the 14-chapter textbook while ensuring consistency, technical accuracy, and pedagogical effectiveness.
# Quickstart Guide: AI-Native Technical Textbook on Physical AI & Humanoid Robotics

## Overview
This quickstart guide provides the essential steps to set up, build, and contribute to the 14-chapter textbook on Physical AI & Humanoid Robotics using Docusaurus and MDX.

## Prerequisites
- Ubuntu 22.04 LTS (for ROS 2 Humble compatibility)
- Node.js 18+ and npm
- Git
- Python 3.10+ (for ROS 2 development)

## Environment Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Install Docusaurus Dependencies
```bash
npm install
```

### 3. Verify ROS 2 Installation (Ubuntu 22.04)
```bash
# Check ROS 2 installation
source /opt/ros/humble/setup.bash
ros2 --version

# Verify required packages
ros2 pkg list | grep -E "(rclpy|std_msgs|sensor_msgs|geometry_msgs)"
```

### 4. Install Additional Tools
```bash
# For diagram generation
npm install -g @mermaid-js/mermaid-cli

# For content validation
npm install -g markdownlint-cli
```

## Development Workflow

### 1. Start Local Development Server
```bash
npm run start
```
This command starts a local development server and opens the textbook in your browser. Most changes are reflected live without restarting the server.

### 2. Create a New Chapter (if needed)
```bash
# Chapters are pre-created, but if adding additional content:
mkdir docs/physical-ai
# Create chapter files as specified in the project structure
```

### 3. Add Content to Existing Chapters
- Edit MDX files in `docs/physical-ai/`
- Follow RAG-friendly formatting (≤5-6 sentences per paragraph)
- Add proper headings and summaries
- Include code examples with proper language identifiers

### 4. Add Diagrams
- Create Mermaid diagrams directly in MDX files using ```mermaid code blocks
- For static images, place in `static/img/physical-ai/` and reference with proper paths

### 5. Add Code Examples
- Use fenced code blocks with appropriate language identifiers
- Include execution instructions in comments
- Test examples in Ubuntu 22.04 + ROS 2 Humble environment

## Content Guidelines

### RAG-Optimized Structure
- Short paragraphs (≤5-6 sentences)
- Clear heading hierarchy (H1, H2, H3)
- Section summaries for context retention
- Consistent terminology across chapters

### Code Example Standards
- Python code follows PEP8
- ROS 2 examples follow rclpy conventions
- Include setup and execution instructions
- Verify in target environment (Ubuntu 22.04 + ROS 2 Humble)

### Diagram Requirements
- Mermaid diagrams for system architectures
- Text descriptions for accessibility
- Clear titles and captions
- Proper file organization in `static/img/physical-ai/`

## Building and Testing

### 1. Build for Production
```bash
npm run build
```
This command generates static content into the `build` directory and can be served using any static hosting service.

### 2. Run Content Validation
```bash
# Check for broken links
npm run serve
# Test in browser or use link checker

# Validate MDX syntax
npm run lint
```

### 3. Test RAG Functionality
```bash
# Ensure content chunks properly for retrieval
# Test search functionality locally
```

## Deployment

### GitHub Pages Deployment
The textbook is configured for GitHub Pages deployment:

1. Push changes to the main branch
2. GitHub Actions will automatically build and deploy the site
3. Monitor the deployment status in the Actions tab

### Manual Deployment
```bash
npm run deploy
```

## Chapter Development Sequence

### Recommended Order for Content Creation:
1. **Chapter 1-2**: Foundations (Introduction, Humanoid Robotics)
2. **Chapter 3-6**: ROS 2 Core (Architecture, Nodes/Topics, Packages, URDF/SDF)
3. **Chapter 7-8**: Simulation (Gazebo, Unity)
4. **Chapter 9-11**: AI & Perception (Isaac, Perception, Navigation)
5. **Chapter 12-13**: Advanced Integration (Voice, Cognitive Planning)
6. **Chapter 14**: Capstone Project

### Cross-Chapter Dependencies:
- Later chapters reference concepts from earlier chapters
- Code examples build on previous implementations
- Exercises assume knowledge from prerequisite chapters

## Quality Assurance

### Technical Accuracy Checks:
- All code examples tested in target environment
- ROS 2 examples follow official documentation
- Simulation examples reproduce as described
- Isaac Sim workflows validated

### Pedagogical Quality Checks:
- Learning outcomes clearly defined
- Exercises appropriate for chapter content
- Prerequisites properly identified
- Cross-references accurate

### RAG Optimization Checks:
- Content structured for retrieval
- Headings and summaries present
- Terminology consistent
- Diagrams properly described

## Troubleshooting

### Common Issues:
1. **Build fails**: Check MDX syntax and file paths
2. **Code examples don't work**: Verify target environment setup
3. **Links broken**: Check relative paths and file names
4. **Diagrams not rendering**: Validate Mermaid syntax

### Getting Help:
- Check the detailed documentation in the `docs/` directory
- Review the implementation plan in `specs/001-physical-ai-textbook/plan.md`
- Consult the research document for technical decisions
- Review the data model for content structure
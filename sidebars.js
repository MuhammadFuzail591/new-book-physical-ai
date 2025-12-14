// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Physical AI & Humanoid Robotics',
      items: [
        {
          type: 'category',
          label: '1. Introduction to Physical AI',
          link: {type: 'doc', id: 'introduction/index'},
          items: [
            'introduction/what-is-physical-ai',
            'introduction/embodied-intelligence',
            'introduction/chapter-summary'
          ]
        },
        {
          type: 'category',
          label: '2. Humanoid Robotics Landscape',
          link: {type: 'doc', id: 'humanoid-robotics/index'},
          items: [
            'humanoid-robotics/landscape',
            'humanoid-robotics/sensor-foundations',
            'humanoid-robotics/chapter-summary'
          ]
        },
        {
          type: 'category',
          label: '3. ROS 2 Architecture',
          link: {type: 'doc', id: 'ros2-architecture/index'},
          items: [
            'ros2-architecture/nodes-topics',
            'ros2-architecture/services-actions',
            'ros2-architecture/chapter-summary'
          ]
        },
        {
          type: 'category',
          label: '4. Building ROS 2 Packages',
          link: {type: 'doc', id: 'ros2-packages/index'},
          items: [
            'ros2-packages/building-packages',
            'ros2-packages/launch-files',
            'ros2-packages/chapter-summary'
          ]
        },
        {
          type: 'category',
          label: '5. URDF/SDF for Humanoid Robots',
          link: {type: 'doc', id: 'ros2-urdf/index'},
          items: [
            'ros2-urdf/urdf-basics',
            'ros2-urdf/sdf-for-simulation',
            'ros2-urdf/chapter-summary'
          ]
        },
        {
          type: 'category',
          label: '6. Advanced ROS 2 Concepts',
          link: {type: 'doc', id: 'ros2-advanced/index'},
          items: [
            'ros2-advanced/parameters',
            'ros2-advanced/quality-of-service',
            'ros2-advanced/chapter-summary'
          ]
        },
        {
          type: 'category',
          label: '7. Gazebo Simulation',
          link: {type: 'doc', id: 'gazebo-simulation/index'},
          items: [
            'gazebo-simulation/physics-engines',
            'gazebo-simulation/world-building',
            'gazebo-simulation/chapter-summary'
          ]
        },
        {
          type: 'category',
          label: '8. Unity Visualization',
          link: {type: 'doc', id: 'unity-visualization/index'},
          items: [
            'unity-visualization/human-robot-interaction',
            'unity-visualization/visualization',
            'unity-visualization/chapter-summary'
          ]
        },
        {
          type: 'category',
          label: '9. NVIDIA Isaac SDK',
          link: {type: 'doc', id: 'nvidia-isaac/index'},
          items: [
            'nvidia-isaac/sdk-overview',
            'nvidia-isaac/isaac-sim',
            'nvidia-isaac/chapter-summary'
          ]
        },
        {
          type: 'category',
          label: '10. AI Perception & Manipulation',
          link: {type: 'doc', id: 'perception-pipelines/index'},
          items: [
            'perception-pipelines/synthetic-data',
            'perception-pipelines/perception-stacks',
            'perception-pipelines/chapter-summary'
          ]
        },
        {
          type: 'category',
          label: '11. VSLAM & Navigation',
          link: {type: 'doc', id: 'navigation-systems/index'},
          items: [
            'navigation-systems/vslam',
            'navigation-systems/navigation',
            'navigation-systems/sim-to-real'
          ]
        },
        {
          type: 'category',
          label: '12. Voice-to-Action Robotics',
          link: {type: 'doc', id: 'voice-robotics/index'},
          items: [
            'voice-robotics/whisper-integration',
            'voice-robotics/voice-to-action',
            'voice-robotics/chapter-summary'
          ]
        },
        {
          type: 'category',
          label: '13. Cognitive Planning with VLA',
          link: {type: 'doc', id: 'cognitive-planning/index'},
          items: [
            'cognitive-planning/vla-systems',
            'cognitive-planning/llm-integration',
            'cognitive-planning/chapter-summary'
          ]
        },
        {
          type: 'category',
          label: '14. Capstone Project',
          link: {type: 'doc', id: 'capstone-project/index'},
          items: [
            'capstone-project/project-overview',
            'capstone-project/implementation',
            'capstone-project/deployment',
            'capstone-project/conclusion'
          ]
        },
        'glossary'  // Glossary page
      ],
    },
  ],
};

module.exports = sidebars;
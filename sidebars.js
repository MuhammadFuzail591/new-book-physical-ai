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
          link: {type: 'doc', id: 'physical-ai/introduction/index'},
          items: [
            'physical-ai/introduction/what-is-physical-ai',
            'physical-ai/introduction/embodied-intelligence',
            'physical-ai/introduction/chapter-summary'
          ]
        },
        {
          type: 'category',
          label: '2. Humanoid Robotics Landscape',
          link: {type: 'doc', id: 'physical-ai/humanoid-robotics/index'},
          items: [
            'physical-ai/humanoid-robotics/landscape',
            'physical-ai/humanoid-robotics/sensor-foundations',
            'physical-ai/humanoid-robotics/chapter-summary'
          ]
        },
        {
          type: 'category',
          label: '3. ROS 2 Architecture',
          link: {type: 'doc', id: 'physical-ai/ros2-architecture/index'},
          items: [
            'physical-ai/ros2-architecture/nodes-topics',
            'physical-ai/ros2-architecture/services-actions',
            'physical-ai/ros2-architecture/chapter-summary'
          ]
        },
        {
          type: 'category',
          label: '4. Building ROS 2 Packages',
          link: {type: 'doc', id: 'physical-ai/ros2-packages/index'},
          items: [
            'physical-ai/ros2-packages/building-packages',
            'physical-ai/ros2-packages/launch-files',
            'physical-ai/ros2-packages/chapter-summary'
          ]
        },
        {
          type: 'category',
          label: '5. URDF/SDF for Humanoid Robots',
          link: {type: 'doc', id: 'physical-ai/ros2-urdf/index'},
          items: [
            'physical-ai/ros2-urdf/urdf-basics',
            'physical-ai/ros2-urdf/sdf-for-simulation',
            'physical-ai/ros2-urdf/chapter-summary'
          ]
        },
        {
          type: 'category',
          label: '6. Advanced ROS 2 Concepts',
          link: {type: 'doc', id: 'physical-ai/ros2-advanced/index'},
          items: [
            'physical-ai/ros2-advanced/parameters',
            'physical-ai/ros2-advanced/quality-of-service',
            'physical-ai/ros2-advanced/chapter-summary'
          ]
        },
        {
          type: 'category',
          label: '7. Gazebo Simulation',
          link: {type: 'doc', id: 'physical-ai/gazebo-simulation/index'},
          items: [
            'physical-ai/gazebo-simulation/physics-engines',
            'physical-ai/gazebo-simulation/world-building',
            'physical-ai/gazebo-simulation/chapter-summary'
          ]
        },
        {
          type: 'category',
          label: '8. Unity Visualization',
          link: {type: 'doc', id: 'physical-ai/unity-visualization/index'},
          items: [
            'physical-ai/unity-visualization/human-robot-interaction',
            'physical-ai/unity-visualization/visualization',
            'physical-ai/unity-visualization/chapter-summary'
          ]
        },
        {
          type: 'category',
          label: '9. NVIDIA Isaac SDK',
          link: {type: 'doc', id: 'physical-ai/nvidia-isaac/index'},
          items: [
            'physical-ai/nvidia-isaac/sdk-overview',
            'physical-ai/nvidia-isaac/isaac-sim',
            'physical-ai/nvidia-isaac/chapter-summary'
          ]
        },
        {
          type: 'category',
          label: '10. AI Perception & Manipulation',
          link: {type: 'doc', id: 'physical-ai/perception-pipelines/index'},
          items: [
            'physical-ai/perception-pipelines/synthetic-data',
            'physical-ai/perception-pipelines/perception-stacks',
            'physical-ai/perception-pipelines/chapter-summary'
          ]
        },
        {
          type: 'category',
          label: '11. VSLAM & Navigation',
          link: {type: 'doc', id: 'physical-ai/navigation-systems/index'},
          items: [
            'physical-ai/navigation-systems/vslam',
            'physical-ai/navigation-systems/navigation',
            'physical-ai/navigation-systems/sim-to-real'
          ]
        },
        {
          type: 'category',
          label: '12. Voice-to-Action Robotics',
          link: {type: 'doc', id: 'physical-ai/voice-robotics/index'},
          items: [
            'physical-ai/voice-robotics/whisper-integration',
            'physical-ai/voice-robotics/voice-to-action',
            'physical-ai/voice-robotics/chapter-summary'
          ]
        },
        {
          type: 'category',
          label: '13. Cognitive Planning with VLA',
          link: {type: 'doc', id: 'physical-ai/cognitive-planning/index'},
          items: [
            'physical-ai/cognitive-planning/vla-systems',
            'physical-ai/cognitive-planning/llm-integration',
            'physical-ai/cognitive-planning/chapter-summary'
          ]
        },
        {
          type: 'category',
          label: '14. Capstone Project',
          link: {type: 'doc', id: 'physical-ai/capstone-project/index'},
          items: [
            'physical-ai/capstone-project/project-overview',
            'physical-ai/capstone-project/implementation',
            'physical-ai/capstone-project/deployment',
            'physical-ai/capstone-project/conclusion'
          ]
        },
        'physical-ai/glossary'  // Glossary page
      ],
    },
  ],
};

module.exports = sidebars;
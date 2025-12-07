import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/physical-ai-textbook/__docusaurus/debug',
    component: ComponentCreator('/physical-ai-textbook/__docusaurus/debug', 'd8f'),
    exact: true
  },
  {
    path: '/physical-ai-textbook/__docusaurus/debug/config',
    component: ComponentCreator('/physical-ai-textbook/__docusaurus/debug/config', '4cd'),
    exact: true
  },
  {
    path: '/physical-ai-textbook/__docusaurus/debug/content',
    component: ComponentCreator('/physical-ai-textbook/__docusaurus/debug/content', '1e9'),
    exact: true
  },
  {
    path: '/physical-ai-textbook/__docusaurus/debug/globalData',
    component: ComponentCreator('/physical-ai-textbook/__docusaurus/debug/globalData', 'bb2'),
    exact: true
  },
  {
    path: '/physical-ai-textbook/__docusaurus/debug/metadata',
    component: ComponentCreator('/physical-ai-textbook/__docusaurus/debug/metadata', 'bab'),
    exact: true
  },
  {
    path: '/physical-ai-textbook/__docusaurus/debug/registry',
    component: ComponentCreator('/physical-ai-textbook/__docusaurus/debug/registry', '463'),
    exact: true
  },
  {
    path: '/physical-ai-textbook/__docusaurus/debug/routes',
    component: ComponentCreator('/physical-ai-textbook/__docusaurus/debug/routes', 'e98'),
    exact: true
  },
  {
    path: '/physical-ai-textbook/',
    component: ComponentCreator('/physical-ai-textbook/', '4a1'),
    routes: [
      {
        path: '/physical-ai-textbook/',
        component: ComponentCreator('/physical-ai-textbook/', '31a'),
        routes: [
          {
            path: '/physical-ai-textbook/',
            component: ComponentCreator('/physical-ai-textbook/', '9f0'),
            routes: [
              {
                path: '/physical-ai-textbook/physical-ai',
                component: ComponentCreator('/physical-ai-textbook/physical-ai', '7fa'),
                exact: true
              },
              {
                path: '/physical-ai-textbook/physical-ai/capstone-project',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/capstone-project', 'd51'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/capstone-project/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/capstone-project/chapter-summary', '9ba'),
                exact: true
              },
              {
                path: '/physical-ai-textbook/physical-ai/capstone-project/conclusion',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/capstone-project/conclusion', '93f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/capstone-project/deployment',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/capstone-project/deployment', 'dba'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/capstone-project/implementation',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/capstone-project/implementation', '50d'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/capstone-project/project-overview',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/capstone-project/project-overview', 'c46'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/cognitive-planning',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/cognitive-planning', '474'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/cognitive-planning/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/cognitive-planning/chapter-summary', '5b2'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/cognitive-planning/llm-integration',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/cognitive-planning/llm-integration', 'aeb'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/cognitive-planning/vla-systems',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/cognitive-planning/vla-systems', '447'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/gazebo-simulation',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/gazebo-simulation', '707'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/gazebo-simulation/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/gazebo-simulation/chapter-summary', '3b4'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/gazebo-simulation/physics-engines',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/gazebo-simulation/physics-engines', '4ae'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/gazebo-simulation/world-building',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/gazebo-simulation/world-building', 'd1b'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/glossary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/glossary', '7cf'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/humanoid-robotics',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/humanoid-robotics', '085'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/humanoid-robotics/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/humanoid-robotics/chapter-summary', '224'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/humanoid-robotics/landscape',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/humanoid-robotics/landscape', '81c'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/humanoid-robotics/sensor-foundations',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/humanoid-robotics/sensor-foundations', '9ce'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/introduction',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/introduction', 'f10'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/introduction/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/introduction/chapter-summary', 'c32'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/introduction/embodied-intelligence',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/introduction/embodied-intelligence', 'c00'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/introduction/what-is-physical-ai',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/introduction/what-is-physical-ai', '97f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/navigation-systems',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/navigation-systems', '252'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/navigation-systems/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/navigation-systems/chapter-summary', '821'),
                exact: true
              },
              {
                path: '/physical-ai-textbook/physical-ai/navigation-systems/navigation',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/navigation-systems/navigation', '7f4'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/navigation-systems/sim-to-real',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/navigation-systems/sim-to-real', '459'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/navigation-systems/vslam',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/navigation-systems/vslam', 'fe7'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/nvidia-isaac',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/nvidia-isaac', 'e20'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/nvidia-isaac/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/nvidia-isaac/chapter-summary', '1f3'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/nvidia-isaac/isaac-sim',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/nvidia-isaac/isaac-sim', '5b7'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/nvidia-isaac/sdk-overview',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/nvidia-isaac/sdk-overview', '145'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/perception-pipelines',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/perception-pipelines', 'f13'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/perception-pipelines/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/perception-pipelines/chapter-summary', 'd29'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/perception-pipelines/perception-stacks',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/perception-pipelines/perception-stacks', '33c'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/perception-pipelines/synthetic-data',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/perception-pipelines/synthetic-data', '250'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/ros2-advanced',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/ros2-advanced', '71b'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/ros2-advanced/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/ros2-advanced/chapter-summary', '0bb'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/ros2-advanced/parameters',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/ros2-advanced/parameters', '35a'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/ros2-advanced/quality-of-service',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/ros2-advanced/quality-of-service', '22e'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/ros2-architecture',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/ros2-architecture', '58b'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/ros2-architecture/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/ros2-architecture/chapter-summary', '9b0'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/ros2-architecture/nodes-topics',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/ros2-architecture/nodes-topics', '768'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/ros2-architecture/services-actions',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/ros2-architecture/services-actions', '3b2'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/ros2-packages',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/ros2-packages', 'b99'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/ros2-packages/building-packages',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/ros2-packages/building-packages', 'ef1'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/ros2-packages/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/ros2-packages/chapter-summary', '24d'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/ros2-packages/launch-files',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/ros2-packages/launch-files', 'd81'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/ros2-urdf',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/ros2-urdf', 'a25'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/ros2-urdf/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/ros2-urdf/chapter-summary', 'cd6'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/ros2-urdf/sdf-for-simulation',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/ros2-urdf/sdf-for-simulation', 'b85'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/ros2-urdf/urdf-basics',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/ros2-urdf/urdf-basics', '0d1'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/unity-visualization',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/unity-visualization', '135'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/unity-visualization/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/unity-visualization/chapter-summary', '3d2'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/unity-visualization/human-robot-interaction',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/unity-visualization/human-robot-interaction', '6a0'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/unity-visualization/visualization',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/unity-visualization/visualization', '39f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/voice-robotics',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/voice-robotics', '6f4'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/voice-robotics/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/voice-robotics/chapter-summary', 'f9d'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/voice-robotics/voice-to-action',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/voice-robotics/voice-to-action', '3db'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/voice-robotics/whisper-integration',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/voice-robotics/whisper-integration', '1bb'),
                exact: true,
                sidebar: "tutorialSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];

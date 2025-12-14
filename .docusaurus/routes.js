import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/physical-ai-textbook/physical-ai/',
    component: ComponentCreator('/physical-ai-textbook/physical-ai/', 'b8d'),
    routes: [
      {
        path: '/physical-ai-textbook/physical-ai/',
        component: ComponentCreator('/physical-ai-textbook/physical-ai/', 'aa3'),
        routes: [
          {
            path: '/physical-ai-textbook/physical-ai/',
            component: ComponentCreator('/physical-ai-textbook/physical-ai/', 'adf'),
            routes: [
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai', '75c'),
                exact: true
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/capstone-project',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/capstone-project', 'ed6'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/capstone-project/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/capstone-project/chapter-summary', '645'),
                exact: true
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/capstone-project/conclusion',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/capstone-project/conclusion', 'a31'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/capstone-project/deployment',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/capstone-project/deployment', '866'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/capstone-project/implementation',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/capstone-project/implementation', 'ce6'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/capstone-project/project-overview',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/capstone-project/project-overview', 'e44'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/cognitive-planning',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/cognitive-planning', '25e'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/cognitive-planning/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/cognitive-planning/chapter-summary', '005'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/cognitive-planning/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/cognitive-planning/chapter-summary', '633'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/cognitive-planning/cognitive-architectures',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/cognitive-planning/cognitive-architectures', 'e99'),
                exact: true
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/cognitive-planning/llm-integration',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/cognitive-planning/llm-integration', 'de3'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/cognitive-planning/vla-systems',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/cognitive-planning/vla-systems', '2fd'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/gazebo-simulation',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/gazebo-simulation', '883'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/gazebo-simulation/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/gazebo-simulation/chapter-summary', 'a47'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/gazebo-simulation/physics-engines',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/gazebo-simulation/physics-engines', 'd5b'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/gazebo-simulation/world-building',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/gazebo-simulation/world-building', 'c81'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/glossary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/glossary', '7f0'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/humanoid-robotics',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/humanoid-robotics', 'c5d'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/humanoid-robotics/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/humanoid-robotics/chapter-summary', 'f90'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/humanoid-robotics/landscape',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/humanoid-robotics/landscape', 'aa9'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/humanoid-robotics/sensor-foundations',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/humanoid-robotics/sensor-foundations', '97f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/introduction',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/introduction', '678'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/introduction/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/introduction/chapter-summary', 'c5a'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/introduction/embodied-intelligence',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/introduction/embodied-intelligence', 'fee'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/introduction/what-is-physical-ai',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/introduction/what-is-physical-ai', '527'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/navigation-systems',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/navigation-systems', '6c1'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/navigation-systems/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/navigation-systems/chapter-summary', '3ef'),
                exact: true
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/navigation-systems/navigation',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/navigation-systems/navigation', '91d'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/navigation-systems/sim-to-real',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/navigation-systems/sim-to-real', '36e'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/navigation-systems/vslam',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/navigation-systems/vslam', 'c56'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/nvidia-isaac',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/nvidia-isaac', 'bff'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/nvidia-isaac/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/nvidia-isaac/chapter-summary', '1a9'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/nvidia-isaac/isaac-sim',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/nvidia-isaac/isaac-sim', '545'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/nvidia-isaac/sdk-overview',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/nvidia-isaac/sdk-overview', '6bc'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/perception-pipelines',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/perception-pipelines', '344'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/perception-pipelines/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/perception-pipelines/chapter-summary', 'da0'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/perception-pipelines/perception-stacks',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/perception-pipelines/perception-stacks', '1ac'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/perception-pipelines/synthetic-data',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/perception-pipelines/synthetic-data', '9f9'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/ros2-advanced',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/ros2-advanced', '106'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/ros2-advanced/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/ros2-advanced/chapter-summary', 'c94'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/ros2-advanced/parameters',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/ros2-advanced/parameters', '0ee'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/ros2-advanced/quality-of-service',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/ros2-advanced/quality-of-service', '8ec'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/ros2-architecture',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/ros2-architecture', '1dd'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/ros2-architecture/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/ros2-architecture/chapter-summary', 'ee1'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/ros2-architecture/nodes-topics',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/ros2-architecture/nodes-topics', 'bba'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/ros2-architecture/services-actions',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/ros2-architecture/services-actions', '63d'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/ros2-communication',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/ros2-communication', 'b66'),
                exact: true
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/ros2-communication/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/ros2-communication/chapter-summary', '5d3'),
                exact: true
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/ros2-communication/nodes-implementation',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/ros2-communication/nodes-implementation', '473'),
                exact: true
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/ros2-communication/services-actions',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/ros2-communication/services-actions', '2c7'),
                exact: true
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/ros2-communication/topics-communication',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/ros2-communication/topics-communication', '50c'),
                exact: true
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/ros2-communication/topics-services-actions',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/ros2-communication/topics-services-actions', 'f4b'),
                exact: true
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/ros2-packages',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/ros2-packages', '904'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/ros2-packages/building-packages',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/ros2-packages/building-packages', '181'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/ros2-packages/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/ros2-packages/chapter-summary', 'f15'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/ros2-packages/launch-files',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/ros2-packages/launch-files', 'cbe'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/ros2-packages/parameters',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/ros2-packages/parameters', 'a08'),
                exact: true
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/ros2-urdf',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/ros2-urdf', '9e7'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/ros2-urdf/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/ros2-urdf/chapter-summary', '6b6'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/ros2-urdf/sdf-for-simulation',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/ros2-urdf/sdf-for-simulation', '9cd'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/ros2-urdf/urdf-basics',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/ros2-urdf/urdf-basics', '0d6'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/unity-visualization',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/unity-visualization', 'fb6'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/unity-visualization/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/unity-visualization/chapter-summary', 'a63'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/unity-visualization/human-robot-interaction',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/unity-visualization/human-robot-interaction', 'ae0'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/unity-visualization/unity-workflows',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/unity-visualization/unity-workflows', '67e'),
                exact: true
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/unity-visualization/visualization',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/unity-visualization/visualization', '641'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/voice-robotics',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/voice-robotics', 'b56'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/voice-robotics/chapter-summary',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/voice-robotics/chapter-summary', '9ac'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/voice-robotics/voice-to-action',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/voice-robotics/voice-to-action', '9fa'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai-textbook/physical-ai/physical-ai/voice-robotics/whisper-integration',
                component: ComponentCreator('/physical-ai-textbook/physical-ai/physical-ai/voice-robotics/whisper-integration', '5b8'),
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

import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/__docusaurus/debug',
    component: ComponentCreator('/__docusaurus/debug', '81a'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/config',
    component: ComponentCreator('/__docusaurus/debug/config', '054'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/content',
    component: ComponentCreator('/__docusaurus/debug/content', '798'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/globalData',
    component: ComponentCreator('/__docusaurus/debug/globalData', 'eb3'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/metadata',
    component: ComponentCreator('/__docusaurus/debug/metadata', '48a'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/registry',
    component: ComponentCreator('/__docusaurus/debug/registry', '6bc'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/routes',
    component: ComponentCreator('/__docusaurus/debug/routes', '87c'),
    exact: true
  },
  {
    path: '/',
    component: ComponentCreator('/', '8ad'),
    routes: [
      {
        path: '/',
        component: ComponentCreator('/', '783'),
        routes: [
          {
            path: '/',
            component: ComponentCreator('/', 'fb3'),
            routes: [
              {
                path: '/capstone-project/chapter-summary',
                component: ComponentCreator('/capstone-project/chapter-summary', '6ed'),
                exact: true
              },
              {
                path: '/cognitive-planning',
                component: ComponentCreator('/cognitive-planning', '9c9'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/cognitive-planning/chapter-summary',
                component: ComponentCreator('/cognitive-planning/chapter-summary', '254'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/cognitive-planning/cognitive-architectures',
                component: ComponentCreator('/cognitive-planning/cognitive-architectures', '47b'),
                exact: true
              },
              {
                path: '/cognitive-planning/llm-integration',
                component: ComponentCreator('/cognitive-planning/llm-integration', '830'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/cognitive-planning/vla-systems',
                component: ComponentCreator('/cognitive-planning/vla-systems', '93a'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/gazebo-simulation',
                component: ComponentCreator('/gazebo-simulation', '166'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/gazebo-simulation/chapter-summary',
                component: ComponentCreator('/gazebo-simulation/chapter-summary', '742'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/gazebo-simulation/physics-engines',
                component: ComponentCreator('/gazebo-simulation/physics-engines', 'a4c'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/gazebo-simulation/world-building',
                component: ComponentCreator('/gazebo-simulation/world-building', '163'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/glossary',
                component: ComponentCreator('/glossary', '03f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/humanoid-robotics',
                component: ComponentCreator('/humanoid-robotics', '9a3'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/humanoid-robotics/chapter-summary',
                component: ComponentCreator('/humanoid-robotics/chapter-summary', '2e6'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/humanoid-robotics/landscape',
                component: ComponentCreator('/humanoid-robotics/landscape', 'fba'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/humanoid-robotics/sensor-foundations',
                component: ComponentCreator('/humanoid-robotics/sensor-foundations', '1be'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/introduction',
                component: ComponentCreator('/introduction', '38b'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/introduction/chapter-summary',
                component: ComponentCreator('/introduction/chapter-summary', 'f73'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/introduction/embodied-intelligence',
                component: ComponentCreator('/introduction/embodied-intelligence', 'd06'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/introduction/what-is-physical-ai',
                component: ComponentCreator('/introduction/what-is-physical-ai', 'dfc'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/navigation-systems',
                component: ComponentCreator('/navigation-systems', '9e4'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/navigation-systems/chapter-summary',
                component: ComponentCreator('/navigation-systems/chapter-summary', '67b'),
                exact: true
              },
              {
                path: '/navigation-systems/navigation',
                component: ComponentCreator('/navigation-systems/navigation', '450'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/navigation-systems/sim-to-real',
                component: ComponentCreator('/navigation-systems/sim-to-real', '390'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/navigation-systems/vslam',
                component: ComponentCreator('/navigation-systems/vslam', '382'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/nvidia-isaac',
                component: ComponentCreator('/nvidia-isaac', 'dfa'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/nvidia-isaac/chapter-summary',
                component: ComponentCreator('/nvidia-isaac/chapter-summary', '29c'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/nvidia-isaac/isaac-sim',
                component: ComponentCreator('/nvidia-isaac/isaac-sim', '2bc'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/nvidia-isaac/sdk-overview',
                component: ComponentCreator('/nvidia-isaac/sdk-overview', '87a'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/perception-pipelines',
                component: ComponentCreator('/perception-pipelines', '0c1'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/perception-pipelines/chapter-summary',
                component: ComponentCreator('/perception-pipelines/chapter-summary', '28c'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/perception-pipelines/perception-stacks',
                component: ComponentCreator('/perception-pipelines/perception-stacks', '4ee'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/perception-pipelines/synthetic-data',
                component: ComponentCreator('/perception-pipelines/synthetic-data', '75c'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai/capstone-project',
                component: ComponentCreator('/physical-ai/capstone-project', 'e67'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai/capstone-project/01-project-overview',
                component: ComponentCreator('/physical-ai/capstone-project/01-project-overview', 'c28'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai/capstone-project/02-implementation',
                component: ComponentCreator('/physical-ai/capstone-project/02-implementation', 'f0d'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai/capstone-project/03-deployment',
                component: ComponentCreator('/physical-ai/capstone-project/03-deployment', 'b7b'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-ai/capstone-project/04-conclusion',
                component: ComponentCreator('/physical-ai/capstone-project/04-conclusion', '7f8'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/ros2-advanced',
                component: ComponentCreator('/ros2-advanced', '80f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/ros2-advanced/chapter-summary',
                component: ComponentCreator('/ros2-advanced/chapter-summary', '275'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/ros2-advanced/parameters',
                component: ComponentCreator('/ros2-advanced/parameters', '2c7'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/ros2-advanced/quality-of-service',
                component: ComponentCreator('/ros2-advanced/quality-of-service', '65a'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/ros2-architecture',
                component: ComponentCreator('/ros2-architecture', '613'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/ros2-architecture/chapter-summary',
                component: ComponentCreator('/ros2-architecture/chapter-summary', 'f83'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/ros2-architecture/nodes-topics',
                component: ComponentCreator('/ros2-architecture/nodes-topics', '6b0'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/ros2-architecture/services-actions',
                component: ComponentCreator('/ros2-architecture/services-actions', '823'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/ros2-communication',
                component: ComponentCreator('/ros2-communication', '17d'),
                exact: true
              },
              {
                path: '/ros2-communication/chapter-summary',
                component: ComponentCreator('/ros2-communication/chapter-summary', '6ac'),
                exact: true
              },
              {
                path: '/ros2-communication/nodes-implementation',
                component: ComponentCreator('/ros2-communication/nodes-implementation', '0d2'),
                exact: true
              },
              {
                path: '/ros2-communication/services-actions',
                component: ComponentCreator('/ros2-communication/services-actions', 'e96'),
                exact: true
              },
              {
                path: '/ros2-communication/topics-communication',
                component: ComponentCreator('/ros2-communication/topics-communication', '800'),
                exact: true
              },
              {
                path: '/ros2-communication/topics-services-actions',
                component: ComponentCreator('/ros2-communication/topics-services-actions', 'a9e'),
                exact: true
              },
              {
                path: '/ros2-packages',
                component: ComponentCreator('/ros2-packages', '541'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/ros2-packages/building-packages',
                component: ComponentCreator('/ros2-packages/building-packages', '23b'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/ros2-packages/chapter-summary',
                component: ComponentCreator('/ros2-packages/chapter-summary', '794'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/ros2-packages/launch-files',
                component: ComponentCreator('/ros2-packages/launch-files', '495'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/ros2-packages/parameters',
                component: ComponentCreator('/ros2-packages/parameters', 'db6'),
                exact: true
              },
              {
                path: '/ros2-urdf',
                component: ComponentCreator('/ros2-urdf', 'c82'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/ros2-urdf/chapter-summary',
                component: ComponentCreator('/ros2-urdf/chapter-summary', 'e3b'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/ros2-urdf/sdf-for-simulation',
                component: ComponentCreator('/ros2-urdf/sdf-for-simulation', 'a67'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/ros2-urdf/urdf-basics',
                component: ComponentCreator('/ros2-urdf/urdf-basics', '26e'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/unity-visualization',
                component: ComponentCreator('/unity-visualization', 'b19'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/unity-visualization/chapter-summary',
                component: ComponentCreator('/unity-visualization/chapter-summary', '25b'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/unity-visualization/human-robot-interaction',
                component: ComponentCreator('/unity-visualization/human-robot-interaction', 'f2c'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/unity-visualization/unity-workflows',
                component: ComponentCreator('/unity-visualization/unity-workflows', '6ff'),
                exact: true
              },
              {
                path: '/unity-visualization/visualization',
                component: ComponentCreator('/unity-visualization/visualization', '697'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/voice-robotics',
                component: ComponentCreator('/voice-robotics', '9d5'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/voice-robotics/chapter-summary',
                component: ComponentCreator('/voice-robotics/chapter-summary', 'e18'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/voice-robotics/voice-to-action',
                component: ComponentCreator('/voice-robotics/voice-to-action', '17a'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/voice-robotics/whisper-integration',
                component: ComponentCreator('/voice-robotics/whisper-integration', '4e3'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/',
                component: ComponentCreator('/', 'cfb'),
                exact: true
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

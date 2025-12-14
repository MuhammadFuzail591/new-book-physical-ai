import React from 'react';
import clsx from 'clsx';
import styles from './HomepageFeatures.module.css';

const FeatureList = [
  {
    title: 'Physical AI & Embodied Intelligence',
    Svg: require('@site/static/img/ai-icon.svg').default,
    description: (
      <>
        Deep dive into the fundamentals of Physical AI and embodied intelligence,
        understanding how robots perceive and interact with the physical world.
      </>
    ),
  },
  {
    title: 'ROS 2 Architecture',
    Svg: require('@site/static/img/ros-icon.svg').default,
    description: (
      <>
        Master the Robot Operating System 2 (ROS 2) architecture, including
        nodes, topics, services, and actions for building robust robotic systems.
      </>
    ),
  },
  {
    title: 'Simulation & Visualization',
    Svg: require('@site/static/img/simulation-icon.svg').default,
    description: (
      <>
        Learn to create realistic simulation environments with Gazebo and Unity,
        essential for testing and validating robotic systems safely.
      </>
    ),
  },
  {
    title: 'AI Integration',
    Svg: require('@site/static/img/nvidia-icon.svg').default,
    description: (
      <>
        Explore NVIDIA Isaac SDK and Isaac Sim for advanced AI perception,
        synthetic data generation, and manipulation pipelines.
      </>
    ),
  },
  {
    title: 'Voice-to-Action Robotics',
    Svg: require('@site/static/img/voice-icon.svg').default,
    description: (
      <>
        Build voice-controlled robotic systems using Whisper and ROS 2 integration
        for natural human-robot interaction.
      </>
    ),
  },
  {
    title: 'Cognitive Planning',
    Svg: require('@site/static/img/planning-icon.svg').default,
    description: (
      <>
        Implement vision-language-action systems and cognitive architectures
        for advanced robotic decision making.
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
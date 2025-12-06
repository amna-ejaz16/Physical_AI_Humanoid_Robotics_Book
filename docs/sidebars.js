/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */

// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  tutorialSidebar: [
    {
      type: 'doc',
      id: 'index',
      label: 'Introduction',
    },
    {
      type: 'category',
      label: 'Module 1: The Robotic Nervous System (ROS 2)',
      items: [
        'modules/module1-ros2/chapter1',
        'modules/module1-ros2/chapter2',
        'modules/module1-ros2/chapter3',
      ],
    },
    {
      type: 'category',
      label: 'Module 2: The Digital Twin (Gazebo & Unity)',
      items: [
        'modules/module2-digital-twin/chapter4',
        'modules/module2-digital-twin/chapter5',
        'modules/module2-digital-twin/chapter6',
      ],
    },
    {
      type: 'category',
      label: 'Module 3: AI-Robot Brain (NVIDIA Isaac)',
      items: [
        'modules/module3-isaac/chapter7',
        'modules/module3-isaac/chapter8',
        'modules/module3-isaac/chapter9',
      ],
    },
    {
      type: 'category',
      label: 'Module 4: Vision-Language-Action (VLA)',
      items: [
        'modules/module4-vla/chapter10',
        'modules/module4-vla/chapter11',
        'modules/module4-vla/chapter12',
      ],
    },
  ],
};

module.exports = sidebars;

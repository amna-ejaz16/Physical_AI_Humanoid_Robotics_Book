# ROS 2 Python Package Setup Example

## Complete Package Structure

```
my_humanoid_package/
├── my_humanoid_package/
│   ├── __init__.py
│   ├── sensor_monitor.py
│   ├── joint_controller.py
│   └── utils.py
├── launch/
│   └── humanoid.launch.py
├── config/
│   └── params.yaml
├── resource/
│   └── my_humanoid_package
├── test/
│   ├── test_copyright.py
│   ├── test_flake8.py
│   └── test_pep257.py
├── package.xml
├── setup.py
├── setup.cfg
└── README.md
```

---

## setup.py

```python
from setuptools import setup
import os
from glob import glob

package_name = 'my_humanoid_package'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        # Install package.xml
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        # Install launch files
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')),

        # Install config files
        (os.path.join('share', package_name, 'config'),
            glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='you@example.com',
    description='Humanoid robot control and monitoring package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sensor_monitor = my_humanoid_package.sensor_monitor:main',
            'joint_controller = my_humanoid_package.joint_controller:main',
        ],
    },
)
```

---

## package.xml

```xml
<?xml version="1.0"?>
<?xml-model href="http://download.ros.org/schema/package_format3.xsd"
  schematypens="http://www.w3.org/2001/XMLSchema"?>
<package format="3">
  <!-- Package metadata -->
  <name>my_humanoid_package</name>
  <version>0.1.0</version>
  <description>Humanoid robot control and monitoring package for ROS 2</description>

  <!-- Maintainer information -->
  <maintainer email="you@example.com">Your Name</maintainer>

  <!-- License -->
  <license>Apache License 2.0</license>

  <!-- Optional: URL to project homepage, bug tracker, repository -->
  <url type="website">https://github.com/yourusername/my_humanoid_package</url>
  <url type="bugtracker">https://github.com/yourusername/my_humanoid_package/issues</url>
  <url type="repository">https://github.com/yourusername/my_humanoid_package</url>

  <!-- Build tool -->
  <buildtool_depend>ament_python</buildtool_depend>

  <!-- Runtime dependencies -->
  <depend>rclpy</depend>
  <depend>std_msgs</depend>
  <depend>geometry_msgs</depend>
  <depend>sensor_msgs</depend>
  <depend>tf2_ros</depend>
  <depend>tf2_geometry_msgs</depend>

  <!-- Test dependencies -->
  <test_depend>ament_copyright</test_depend>
  <test_depend>ament_flake8</test_depend>
  <test_depend>ament_pep257</test_depend>
  <test_depend>python3-pytest</test_depend>

  <!-- Export information -->
  <export>
    <build_type>ament_python</build_type>
  </export>
</package>
```

---

## setup.cfg

```ini
[develop]
script_dir=$base/lib/my_humanoid_package

[install]
install_scripts=$base/lib/my_humanoid_package
```

---

## config/params.yaml

```yaml
/**:
  ros__parameters:
    # Sensor Monitor Parameters
    sensor_monitor:
      update_rate: 10.0
      robot_name: "humanoid_01"
      obstacle_threshold: 0.3
      accel_threshold: 20.0

    # Joint Controller Parameters
    joint_controller:
      control_rate: 50.0
      max_velocity: 2.0
      max_effort: 50.0
```

---

## launch/humanoid.launch.py

```python
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    # Get package share directory
    pkg_share = get_package_share_directory('my_humanoid_package')

    # Path to parameter file
    params_file = os.path.join(pkg_share, 'config', 'params.yaml')

    # Declare launch arguments
    robot_name_arg = DeclareLaunchArgument(
        'robot_name',
        default_value='humanoid_01',
        description='Unique robot identifier'
    )

    # Sensor Monitor Node
    sensor_monitor_node = Node(
        package='my_humanoid_package',
        executable='sensor_monitor',
        name='sensor_monitor',
        output='screen',
        parameters=[params_file]
    )

    # Joint Controller Node
    joint_controller_node = Node(
        package='my_humanoid_package',
        executable='joint_controller',
        name='joint_controller',
        output='screen',
        parameters=[params_file]
    )

    return LaunchDescription([
        robot_name_arg,
        sensor_monitor_node,
        joint_controller_node
    ])
```

---

## Building and Running

### Create Workspace and Package

```bash
# Create workspace
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src

# Create package
ros2 pkg create my_humanoid_package \
  --build-type ament_python \
  --dependencies rclpy std_msgs geometry_msgs sensor_msgs tf2_ros

# Navigate to package
cd my_humanoid_package
```

### Build Package

```bash
# Build from workspace root
cd ~/ros2_ws
colcon build --packages-select my_humanoid_package

# Source the workspace
source install/setup.bash
```

### Run Nodes

```bash
# Run single node
ros2 run my_humanoid_package sensor_monitor

# Run with parameters
ros2 run my_humanoid_package sensor_monitor \
  --ros-args -p robot_name:=atlas -p update_rate:=20.0

# Run with launch file
ros2 launch my_humanoid_package humanoid.launch.py
```

### Debugging

```bash
# List nodes
ros2 node list

# Get node info
ros2 node info /sensor_monitor

# List topics
ros2 topic list

# Echo messages
ros2 topic echo /robot/status

# Get/Set parameters
ros2 param get /sensor_monitor update_rate
ros2 param set /sensor_monitor update_rate 15.0
```

---

## Testing

### test/test_flake8.py

```python
# Copyright 2024 Your Name
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
#
# http://www.apache.org/licenses/LICENSE-2.0

from ament_flake8.main import main_with_errors
import pytest


@pytest.mark.flake8
@pytest.mark.linter
def test_flake8():
    rc, errors = main_with_errors(argv=[])
    assert rc == 0, \
        'Found %d code style errors / warnings:\n' % len(errors) + \
        '\n'.join(errors)
```

### Run Tests

```bash
# Run all tests
cd ~/ros2_ws
colcon test --packages-select my_humanoid_package

# View test results
colcon test-result --verbose
```

---

## Best Practices

### 1. Package Organization

- **Single responsibility**: One package, one purpose
- **Clear naming**: Descriptive, lowercase with underscores
- **Documentation**: README.md with usage instructions

### 2. Dependencies

- **Minimize dependencies**: Only include what you need
- **Version pinning**: Specify ROS distribution compatibility
- **Dependency categories**: Build, runtime, test

### 3. Configuration

- **Use parameters**: Avoid hardcoding values
- **YAML config files**: Centralize configuration
- **Launch files**: Standardize node startup

### 4. Code Quality

- **Follow PEP 8**: Python style guide
- **Type hints**: Improve code clarity
- **Docstrings**: Document classes and methods
- **Linting**: Use flake8, pylint

### 5. Testing

- **Unit tests**: Test individual components
- **Integration tests**: Test node interactions
- **Continuous testing**: Run tests on every build

---

## References

1. Open Robotics. (2024). *Creating a ROS 2 Package*. https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html
2. Open Robotics. (2024). *Using colcon to build packages*. https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Colcon-Tutorial.html
3. Python Packaging Authority. (2024). *Packaging Python Projects*. https://packaging.python.org/tutorials/packaging-projects/

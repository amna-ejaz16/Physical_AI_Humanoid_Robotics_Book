# Module 1 Research: ROS 2 Fundamentals

**Date**: 2025-12-05
**Module**: The Robotic Nervous System (ROS 2)
**Research Focus**: ROS 2 architecture, Python integration, URDF, and humanoid robot description

---

## Research Sources

### Primary Sources (Peer-Reviewed & Official Documentation)

1. **ROS 2 Official Documentation** (High Reputation)
   - Source: https://github.com/ros2/ros2_documentation
   - Coverage: 1562 code snippets, Benchmark Score: 95.6
   - Topics: ROS 2 architecture, nodes, topics, services, actions, middleware

2. **rclpy - ROS Client Library for Python** (High Reputation)
   - Source: https://github.com/ros2/rclpy
   - Coverage: 39 code snippets
   - Topics: Python bindings, node creation, publishers, subscribers, services, actions

3. **ROS 2 Common Interfaces** (High Reputation)
   - Source: https://github.com/ros2/common_interfaces
   - Coverage: 130 code snippets
   - Topics: Standard message types (.msg) and service definitions (.srv)

---

## Key Concepts for Module 1

### 1. ROS 2 Architecture

**Nodes**:
- Fundamental building blocks of ROS 2 applications
- Independent processes that perform computation
- Can publish/subscribe to topics, provide/call services, and implement/use actions
- Example: A camera node publishes image data, a perception node subscribes and processes it

**Communication Patterns**:

1. **Topics** (Publisher-Subscriber):
   - One-way, continuous data streaming
   - Many-to-many communication
   - Best for sensor data, state information
   - Asynchronous, non-blocking

2. **Services** (Request-Response):
   - Two-way, synchronous communication
   - One-to-one (client-server)
   - Best for quick computations and queries
   - Blocking, should return quickly
   - Example: Service to reset robot state

3. **Actions** (Goal-Feedback-Result):
   - Long-running tasks with feedback
   - Built on topics and services
   - Cancellable and preemptable
   - Provides steady feedback during execution
   - Example: Navigation to a goal position

**Middleware (DDS)**:
- ROS 2 uses Data Distribution Service (DDS) as middleware
- Provides discovery, serialization, and transport
- Multiple DDS implementations supported (CycloneDDS, FastDDS)
- Enables real-time, reliable communication

---

### 2. Python Integration with ROS 2 (rclpy)

**Core rclpy Modules**:
- `rclpy.node.Node`: Base class for creating ROS 2 nodes
- `rclpy.publisher.Publisher`: Publishes messages to topics
- `rclpy.subscription.Subscription`: Subscribes to topics
- `rclpy.client.Client`: Calls services
- `rclpy.service.Service`: Provides services
- `rclpy.action.ActionClient`: Sends action goals
- `rclpy.action.ActionServer`: Handles action goals

**Node Lifecycle**:
1. Initialize ROS 2 context: `rclpy.init()`
2. Create node instance: `Node('node_name')`
3. Create publishers/subscribers/services/actions
4. Spin node to process callbacks: `rclpy.spin(node)`
5. Cleanup: `node.destroy_node()`, `rclpy.shutdown()`

**Quality of Service (QoS)**:
- Configurable communication settings
- Controls reliability, durability, history depth
- Essential for real-time robotics applications

---

### 3. URDF (Unified Robot Description Format)

**Purpose**:
- XML format for describing robot kinematic and dynamic properties
- Defines links (rigid bodies) and joints (connections between links)
- Includes visual, collision, and inertial properties
- Used for simulation, visualization, and motion planning

**Key Components**:
1. **Links**: Represent rigid bodies (e.g., limbs, torso, head)
   - Visual geometry (appearance)
   - Collision geometry (physics)
   - Inertial properties (mass, center of mass, inertia tensor)

2. **Joints**: Define kinematic relationships between links
   - Types: fixed, revolute (hinge), prismatic (slider), continuous
   - Limits: position, velocity, effort (torque/force)
   - Dynamics: damping, friction

3. **Sensors**: Cameras, LiDAR, IMU, depth sensors
   - Defined as links with sensor plugins

4. **Actuators**: Motors and controllers
   - Specified via transmission elements

---

### 4. Humanoid Robot Kinematics

**Key Considerations**:
- **Degrees of Freedom (DOF)**: Typical humanoids have 20-40+ DOF
  - Head: 2-3 DOF (pan, tilt, roll)
  - Arms: 7 DOF each (shoulder 3, elbow 1, wrist 3)
  - Hands: 5-15 DOF (fingers)
  - Torso: 2-3 DOF (pitch, roll, yaw)
  - Legs: 6 DOF each (hip 3, knee 1, ankle 2)

- **Forward Kinematics**: Joint angles → end-effector position
- **Inverse Kinematics**: Desired position → joint angles
- **Balance and Stability**: Center of Mass (CoM) within support polygon

---

## Research Findings Summary

### ROS 2 vs ROS 1 Improvements

1. **Real-time Performance**: Built-in support for real-time systems
2. **Security**: Authentication and encryption support
3. **Multi-platform**: Windows, macOS, Linux, RTOS
4. **Modularity**: Better separation of concerns
5. **Quality of Service**: Fine-grained control over communication
6. **No Master Node**: Fully distributed architecture using DDS discovery

### Python Integration Benefits

- Rapid prototyping and development
- Extensive scientific libraries (NumPy, SciPy, OpenCV)
- Integration with AI/ML frameworks (TensorFlow, PyTorch)
- Easier for educational purposes
- Trade-off: Slightly lower performance than C++ (acceptable for most applications)

### URDF Best Practices for Humanoids

1. Use accurate mass and inertia properties for realistic simulation
2. Define collision geometries simpler than visual geometries for performance
3. Use joint limits that match physical hardware
4. Include sensor frames for perception pipeline integration
5. Modularize URDF with xacro macros for maintainability

---

## References (APA Format)

1. Open Robotics. (2024). *ROS 2 Documentation*. GitHub. https://github.com/ros2/ros2_documentation

2. Open Robotics. (2024). *rclpy: ROS Client Library for Python*. GitHub. https://github.com/ros2/rclpy

3. Open Robotics. (2024). *ROS 2 Common Interfaces*. GitHub. https://github.com/ros2/common_interfaces

4. Macenski, S., Foote, T., Gerkey, B., Lalancette, C., & Woodall, W. (2022). Robot Operating System 2: Design, architecture, and uses in the wild. *Science Robotics, 7*(66). https://doi.org/10.1126/scirobotics.abm6074

5. Maruyama, Y., Kato, S., & Azumi, T. (2016). Exploring the performance of ROS2. *Proceedings of the 13th International Conference on Embedded Software (EMSOFT)*, 1-10. https://doi.org/10.1145/2968478.2968502

---

## Notes for Chapter Development

- Emphasize practical examples with rclpy code snippets
- Include diagrams for node communication patterns
- Provide URDF examples for simple humanoid structures
- Reference latest ROS 2 distributions (Humble LTS, Iron, Jazzy)
- Ensure all code examples are tested and reproducible

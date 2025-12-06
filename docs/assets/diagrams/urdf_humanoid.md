# URDF Humanoid Structure Diagram

## Diagram Description

This diagram illustrates the basic URDF (Unified Robot Description Format) structure for a simplified humanoid robot, showing the hierarchical relationship between links and joints.

## Humanoid Robot Components

### Links (Rigid Bodies)
- **base_link**: Root link, typically the torso/pelvis
- **head**: Robot head with sensors
- **torso**: Upper body/chest
- **left_shoulder**, **right_shoulder**: Shoulder links
- **left_upper_arm**, **right_upper_arm**: Upper arm segments
- **left_forearm**, **right_forearm**: Lower arm segments
- **left_hand**, **right_hand**: End-effector hands
- **left_hip**, **right_hip**: Hip links
- **left_thigh**, **right_thigh**: Upper leg segments
- **left_shin**, **right_shin**: Lower leg segments
- **left_foot**, **right_foot**: Feet for ground contact

### Joints (Connections)
- **Fixed Joints**: Non-moving connections (e.g., torso to base_link)
- **Revolute Joints**: Rotating joints with limits (e.g., shoulders, elbows, knees)
- **Continuous Joints**: Unlimited rotation (rare in humanoids)

## Hierarchical Structure (Tree)

```
base_link (root)
├── torso (fixed)
│   ├── head (revolute: neck_pitch, neck_yaw)
│   ├── left_shoulder (revolute: shoulder_pitch)
│   │   └── left_upper_arm (revolute: shoulder_roll)
│   │       └── left_forearm (revolute: elbow)
│   │           └── left_hand (revolute: wrist)
│   └── right_shoulder (revolute: shoulder_pitch)
│       └── right_upper_arm (revolute: shoulder_roll)
│           └── right_forearm (revolute: elbow)
│               └── right_hand (revolute: wrist)
├── left_hip (revolute: hip_yaw)
│   └── left_thigh (revolute: hip_pitch, hip_roll)
│       └── left_shin (revolute: knee)
│           └── left_foot (revolute: ankle_pitch, ankle_roll)
└── right_hip (revolute: hip_yaw)
    └── right_thigh (revolute: hip_pitch, hip_roll)
        └── right_shin (revolute: knee)
            └── right_foot (revolute: ankle_pitch, ankle_roll)
```

## Degrees of Freedom (DOF) Breakdown

| Body Part | DOF | Joints |
|-----------|-----|--------|
| Head | 2 | Neck pitch, Neck yaw |
| Left Arm | 4 | Shoulder pitch/roll, Elbow, Wrist |
| Right Arm | 4 | Shoulder pitch/roll, Elbow, Wrist |
| Left Leg | 6 | Hip yaw/pitch/roll, Knee, Ankle pitch/roll |
| Right Leg | 6 | Hip yaw/pitch/roll, Knee, Ankle pitch/roll |
| **Total** | **22** | |

## Visual Representation

```
         [HEAD]
            |
        (neck_pitch/yaw)
            |
    [LEFT_SHOULDER]---[TORSO]---[RIGHT_SHOULDER]
         |                            |
    (shoulder_pitch/roll)        (shoulder_pitch/roll)
         |                            |
    [LEFT_UPPER_ARM]            [RIGHT_UPPER_ARM]
         |                            |
       (elbow)                      (elbow)
         |                            |
    [LEFT_FOREARM]              [RIGHT_FOREARM]
         |                            |
       (wrist)                      (wrist)
         |                            |
     [LEFT_HAND]                 [RIGHT_HAND]

        [BASE_LINK / PELVIS]

    [LEFT_HIP]                  [RIGHT_HIP]
         |                            |
    (hip_yaw/pitch/roll)        (hip_yaw/pitch/roll)
         |                            |
    [LEFT_THIGH]                [RIGHT_THIGH]
         |                            |
       (knee)                       (knee)
         |                            |
    [LEFT_SHIN]                 [RIGHT_SHIN]
         |                            |
    (ankle_pitch/roll)          (ankle_pitch/roll)
         |                            |
    [LEFT_FOOT]                 [RIGHT_FOOT]
```

## Coordinate Frames

### ROS/URDF Convention (REP 103)
- **X-axis**: Forward (red)
- **Y-axis**: Left (green)
- **Z-axis**: Up (blue)

### Joint Axis Conventions
- **Pitch**: Rotation around Y-axis (nodding)
- **Yaw**: Rotation around Z-axis (turning)
- **Roll**: Rotation around X-axis (tilting)

## URDF Properties

### Link Properties
1. **Visual**: Appearance in visualization (mesh, color, geometry)
2. **Collision**: Simplified geometry for physics simulation
3. **Inertial**: Mass, center of mass, inertia tensor

### Joint Properties
1. **Type**: fixed, revolute, prismatic, continuous
2. **Parent/Child**: Link connections
3. **Origin**: Position and orientation relative to parent
4. **Axis**: Rotation/translation axis
5. **Limits**: Position, velocity, effort (torque/force)
6. **Dynamics**: Damping, friction

## Example URDF Snippet (Simple Arm)

```xml
<robot name="simple_humanoid">
  <!-- Base Link -->
  <link name="base_link">
    <visual>
      <geometry>
        <box size="0.3 0.2 0.4"/>
      </geometry>
    </visual>
    <inertial>
      <mass value="10.0"/>
      <inertia ixx="0.1" ixy="0.0" ixz="0.0"
               iyy="0.1" iyz="0.0" izz="0.1"/>
    </inertial>
  </link>

  <!-- Shoulder Link -->
  <link name="left_upper_arm">
    <visual>
      <geometry>
        <cylinder radius="0.05" length="0.3"/>
      </geometry>
    </visual>
    <inertial>
      <mass value="1.5"/>
      <inertia ixx="0.01" ixy="0.0" ixz="0.0"
               iyy="0.01" iyz="0.0" izz="0.001"/>
    </inertial>
  </link>

  <!-- Shoulder Joint -->
  <joint name="left_shoulder_pitch" type="revolute">
    <parent link="base_link"/>
    <child link="left_upper_arm"/>
    <origin xyz="0.0 0.15 0.15" rpy="0 0 0"/>
    <axis xyz="0 1 0"/>  <!-- Y-axis for pitch -->
    <limit lower="-1.57" upper="3.14"
           effort="50.0" velocity="2.0"/>
    <dynamics damping="0.1" friction="0.05"/>
  </joint>
</robot>
```

## Simulation Considerations

1. **Mass Distribution**: Accurate inertial properties for realistic dynamics
2. **Joint Limits**: Match physical robot constraints
3. **Collision Geometry**: Simplified for performance
4. **Damping/Friction**: Tuned for stable simulation

## Tools for URDF Creation

- **xacro**: XML macro language for modular URDF
- **SolidWorks/Fusion 360**: CAD to URDF export plugins
- **MeshLab**: Mesh simplification for collision geometry
- **RViz**: ROS visualization tool for URDF debugging

## References

1. ROS Wiki. (2024). URDF Tutorials. http://wiki.ros.org/urdf/Tutorials
2. REP 103: Standard Units of Measurement and Coordinate Conventions. https://www.ros.org/reps/rep-0103.html
3. Siciliano, B., & Khatib, O. (Eds.). (2016). *Springer Handbook of Robotics* (2nd ed.). Springer.

---

**Note**: This is a conceptual diagram. For actual implementation, use tools like RViz or Gazebo to visualize and validate URDF models. Proper mass, inertia, and joint properties are critical for accurate simulation.

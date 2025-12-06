# Module 2 Research: The Digital Twin (Gazebo & Unity)

**Date**: 2025-12-05
**Module**: Digital Twin Simulation
**Research Focus**: Physics simulation (Gazebo), high-fidelity visualization (Unity), sensor simulation, URDF/SDF integration

---

## Research Sources

### Primary Sources (Peer-Reviewed & Official Documentation)

1. **Gazebo Simulation Documentation** (High Reputation)
   - Source: https://github.com/gazebosim/docs
   - Coverage: 935 code snippets, Benchmark Score: 85.7
   - Topics: Physics engines, sensor simulation, URDF/SDF, robot spawning

2. **SDFormat (Simulation Description Format)** (High Reputation)
   - Source: http://sdformat.org/
   - Topics: World descriptions, robot models, physics parameters

3. **Unity Robotics Hub** (High Reputation)
   - Source: https://github.com/Unity-Technologies/Unity-Robotics-Hub
   - Topics: ROS-Unity integration, high-fidelity rendering, HRI simulation

---

## Key Concepts for Module 2

### 1. Physics Simulation in Gazebo

**Physics Engines**:
Gazebo supports multiple physics engines:
- **ODE (Open Dynamics Engine)**: Default, fast, suitable for most applications
- **Bullet**: Better collision detection, soft body physics
- **DART (Dynamic Animation and Robotics Toolkit)**: High-fidelity dynamics
- **Simbody**: Biomechanical simulation

**Key Physics Concepts**:
1. **Gravity**: Default 9.81 m/s² (Earth), configurable per world
2. **Collisions**: Contact detection between geometries
3. **Friction**: Static and dynamic friction coefficients
4. **Damping**: Linear and angular damping for stability
5. **Inertia**: Mass distribution affects dynamics
6. **Contact forces**: Normal and tangential forces at contact points

**Physics Parameters** (SDF):
```xml
<physics type="ode">
  <max_step_size>0.001</max_step_size>
  <real_time_factor>1.0</real_time_factor>
  <real_time_update_rate>1000</real_time_update_rate>
  <gravity>0 0 -9.81</gravity>
</physics>
```

---

### 2. SDF vs URDF

**SDF (Simulation Description Format)**:
- Comprehensive world and model description
- Supports multiple robots in one file
- Richer physics parameters
- Sensor definitions with plugins
- Supports joints, links, collision, visual, inertial
- Can describe complete environments

**URDF (Unified Robot Description Format)**:
- Single robot description only
- Simpler, more widely supported in ROS
- Limited physics parameters
- Requires Gazebo plugins for sensors
- Tree structure (no closed loops)

**Conversion**:
- Gazebo can convert URDF to SDF internally
- `sdformat_urdf` library enables ROS 2 to read SDF as URDF
- Limitations: Some SDF features not compatible with URDF

---

### 3. Sensor Simulation

**Supported Sensors in Gazebo**:

1. **Camera**:
   - RGB cameras
   - Depth cameras
   - Wide-angle/fisheye
   - Resolution, FOV, distortion configurable

2. **LiDAR/LaserScan**:
   - 2D: Single plane scanning (e.g., Hokuyo, SICK)
   - 3D: Point cloud generation (e.g., Velodyne)
   - Ray-based: Configurable range, angular resolution, noise

3. **IMU (Inertial Measurement Unit)**:
   - Linear acceleration (3-axis accelerometer)
   - Angular velocity (3-axis gyroscope)
   - Orientation (quaternion or Euler angles)
   - Noise models: Gaussian, bias drift

4. **Contact/Tactile**:
   - Force-torque sensors
   - Bumper sensors
   - Pressure sensors

5. **GPS**:
   - Position (latitude, longitude, altitude)
   - Velocity
   - Noise simulation for realism

**Sensor Noise Models**:
- **Gaussian noise**: Mean and standard deviation
- **Bias**: Constant offset
- **Drift**: Time-varying bias
- **Quantization**: Discrete value steps

---

### 4. URDF/SDF Integration

**Spawning URDF in Gazebo**:
1. Use `gz service` to call `/world/<world_name>/create` service
2. Set `sdf_file_name` field with URDF path
3. Gazebo converts URDF to SDF using libsdformat
4. Robot spawned in world at specified pose

**Gazebo Plugins for ROS 2 Integration**:
- `libgazebo_ros_diff_drive`: Differential drive controller
- `libgazebo_ros_joint_state_publisher`: Publish joint states
- `libgazebo_ros_camera`: Publish camera images
- `libgazebo_ros_ray_sensor`: Publish laser scans
- `libgazebo_ros_imu_sensor`: Publish IMU data

---

### 5. Unity for High-Fidelity Visualization

**Unity Advantages**:
- **Photorealistic rendering**: Advanced shaders, lighting, shadows
- **Performance**: Optimized for real-time graphics
- **VR/AR support**: Immersive HRI simulation
- **Asset ecosystem**: Pre-built 3D models, materials
- **Cross-platform**: Desktop, mobile, web

**Unity Robotics Hub**:
- **ROS-TCP-Connector**: Bidirectional ROS-Unity communication
- **URDF Importer**: Load robot models from URDF
- **Visualization tools**: Joint state visualization, TF frames
- **Sensor simulation**: RGB cameras, depth sensors

**Use Cases for Unity**:
1. **HRI (Human-Robot Interaction)**: Realistic human models, environments
2. **Perception testing**: Evaluate computer vision algorithms
3. **Teleoperation interfaces**: Real-time robot visualization
4. **Marketing/demos**: High-quality renderings

---

### 6. Humanoid Simulation Considerations

**Balance and Stability**:
- Center of Mass (CoM) within support polygon
- Zero Moment Point (ZMP) control
- Compliance control for impact absorption

**Ground Contact**:
- Accurate friction parameters crucial
- Foot collision geometry affects stability
- Contact sensor feedback for gait control

**Joint Control**:
- Position control: Direct joint angle commands
- Velocity control: Joint speed commands
- Effort/Torque control: Force-based control
- PID controllers: Tune gains for stability

**Common Challenges**:
1. **Stiffness**: High gains → instability
2. **Simulation speed**: Real-time factor < 1 for complex robots
3. **Contact instability**: Small time steps, accurate collision
4. **Sensor noise**: Balance realism vs. usability

---

## Research Findings Summary

### Gazebo vs Unity Trade-offs

| Feature | Gazebo | Unity |
|---------|--------|-------|
| **Physics accuracy** | High (multiple engines) | Moderate (PhysX) |
| **Graphics quality** | Moderate | Excellent |
| **ROS integration** | Native (ros_gz) | Via TCP connector |
| **Sensor simulation** | Comprehensive | Limited (cameras, depth) |
| **Performance** | Variable (physics-limited) | High (graphics-optimized) |
| **Open source** | Yes | No (free tier) |
| **Learning curve** | Moderate | Steep (game engine) |
| **Best for** | Physics testing, sim-to-real | Visualization, HRI, demos |

### Recommended Workflow

1. **Development**: Use Gazebo for physics, dynamics, sensor testing
2. **Validation**: Test control algorithms, perception pipelines
3. **Visualization**: Export to Unity for high-fidelity rendering
4. **Deployment**: Sim-to-real transfer from Gazebo-tested controllers

---

## References (APA Format)

### Peer-Reviewed Sources

1. Koenig, N., & Howard, A. (2004). Design and use paradigms for Gazebo, an open-source multi-robot simulator. *2004 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*, 3, 2149-2154. https://doi.org/10.1109/IROS.2004.1389727

2. Collins, J., Chand, S., Vanderkop, A., & Howard, D. (2021). A review of physics simulators for robotic applications. *IEEE Access, 9*, 51416-51431. https://doi.org/10.1109/ACCESS.2021.3068769

3. Ivaldi, S., Peters, J., Padois, V., & Nori, F. (2014). Tools for simulating humanoid robot dynamics: A survey based on user feedback. *2014 IEEE-RAS International Conference on Humanoid Robots*, 842-849. https://doi.org/10.1109/HUMANOIDS.2014.7041462

### Official Documentation

4. Open Source Robotics Foundation. (2024). *Gazebo Documentation*. https://gazebosim.org/docs

5. Open Source Robotics Foundation. (2024). *SDFormat Specification*. http://sdformat.org/

6. Unity Technologies. (2024). *Unity Robotics Hub*. https://github.com/Unity-Technologies/Unity-Robotics-Hub

7. Open Robotics. (2024). *ros_gz: ROS 2 integration with Gazebo*. https://github.com/gazebosim/ros_gz

### Textbooks

8. Rohmer, E., Singh, S. P. N., & Freese, M. (2013). V-REP: A versatile and scalable robot simulation framework. *2013 IEEE/RSJ International Conference on Intelligent Robots and Systems*, 1321-1326.

9. Staranowicz, A., & Mariottini, G. L. (2011). A survey of sensor simulators. *Technical Report*, University of Texas at Arlington.

10. Erez, T., Tassa, Y., & Todorov, E. (2015). Simulation tools for model-based robotics: Comparison of Bullet, Havok, MuJoCo, ODE and PhysX. *2015 IEEE International Conference on Robotics and Automation (ICRA)*, 4397-4404.

---

## Notes for Chapter Development

- Emphasize hands-on Gazebo simulation setup
- Provide SDF examples for humanoid robots
- Include sensor configuration examples (camera, LiDAR, IMU)
- Demonstrate URDF spawning in Gazebo
- Cover physics engine selection and tuning
- Unity section: Focus on visualization, not game development
- Real-world examples: Humanoid walking in simulated environments

---

**Last Updated**: 2025-12-05

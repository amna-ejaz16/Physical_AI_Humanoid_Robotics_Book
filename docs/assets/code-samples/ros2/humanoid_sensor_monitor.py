#!/usr/bin/env python3
"""
Humanoid Sensor Monitor Node - Complete Example
Demonstrates advanced rclpy features for humanoid robotics

This node monitors multiple sensor streams (IMU, Camera, LiDAR) and publishes
aggregated robot status. Includes parameters, QoS configuration, and timers.
"""

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu, Image, LaserScan
from std_msgs.msg import String
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from rcl_interfaces.msg import ParameterDescriptor


class HumanoidSensorMonitor(Node):
    """
    Advanced ROS 2 node for monitoring humanoid robot sensors.

    Features:
    - Multiple sensor subscribers with custom QoS
    - Parameter-based configuration
    - Periodic status publishing
    - Warning detection for safety-critical conditions
    """

    def __init__(self):
        super().__init__('humanoid_sensor_monitor')

        # ============ PARAMETERS ============
        self.declare_parameter(
            'update_rate',
            10.0,
            ParameterDescriptor(description='Status update frequency (Hz)')
        )

        self.declare_parameter(
            'robot_name',
            'humanoid_01',
            ParameterDescriptor(description='Robot identifier')
        )

        self.declare_parameter(
            'obstacle_threshold',
            0.3,
            ParameterDescriptor(description='Minimum safe distance to obstacles (m)')
        )

        self.declare_parameter(
            'accel_threshold',
            20.0,
            ParameterDescriptor(description='High acceleration warning threshold (m/s^2)')
        )

        # Get parameter values
        update_rate = self.get_parameter('update_rate').get_parameter_value().double_value
        self.robot_name = self.get_parameter('robot_name').get_parameter_value().string_value
        self.obstacle_threshold = self.get_parameter('obstacle_threshold').get_parameter_value().double_value
        self.accel_threshold = self.get_parameter('accel_threshold').get_parameter_value().double_value

        # ============ SENSOR DATA STORAGE ============
        self.imu_data = None
        self.camera_data = None
        self.lidar_data = None

        # Timestamps for data freshness
        self.imu_last_update = None
        self.camera_last_update = None
        self.lidar_last_update = None

        # ============ QoS PROFILES ============
        # Best effort for high-frequency sensor data
        sensor_qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            history=HistoryPolicy.KEEP_LAST,
            depth=10,
            durability=DurabilityPolicy.VOLATILE
        )

        # Reliable for status messages
        status_qos = QoSProfile(
            reliability=ReliabilityPolicy.RELIABLE,
            history=HistoryPolicy.KEEP_LAST,
            depth=10,
            durability=DurabilityPolicy.TRANSIENT_LOCAL
        )

        # ============ SUBSCRIBERS ============
        self.imu_sub = self.create_subscription(
            Imu,
            '/imu/data',
            self.imu_callback,
            sensor_qos
        )

        self.camera_sub = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.camera_callback,
            sensor_qos
        )

        self.lidar_sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.lidar_callback,
            sensor_qos
        )

        # ============ PUBLISHERS ============
        self.status_pub = self.create_publisher(
            String,
            '/robot/status',
            status_qos
        )

        self.warning_pub = self.create_publisher(
            String,
            '/robot/warnings',
            10
        )

        # ============ TIMERS ============
        timer_period = 1.0 / update_rate
        self.status_timer = self.create_timer(timer_period, self.publish_status)

        # Data staleness check timer (every 1 second)
        self.staleness_timer = self.create_timer(1.0, self.check_data_freshness)

        self.get_logger().info(
            f'{self.robot_name} Sensor Monitor started '
            f'(update rate: {update_rate} Hz)'
        )

    def imu_callback(self, msg):
        """
        Process IMU (Inertial Measurement Unit) data.

        Args:
            msg (Imu): IMU sensor message with accelerations and angular velocities
        """
        self.imu_data = msg
        self.imu_last_update = self.get_clock().now()

        # Calculate acceleration magnitude
        accel_magnitude = (
            msg.linear_acceleration.x**2 +
            msg.linear_acceleration.y**2 +
            msg.linear_acceleration.z**2
        )**0.5

        # Warning for unusual accelerations
        if accel_magnitude > self.accel_threshold:
            warning_msg = String()
            warning_msg.data = (
                f'HIGH ACCELERATION: {accel_magnitude:.2f} m/s^2 '
                f'(threshold: {self.accel_threshold:.2f})'
            )
            self.warning_pub.publish(warning_msg)
            self.get_logger().warn(warning_msg.data)

        # Log normal operation at debug level
        self.get_logger().debug(
            f'IMU: accel={accel_magnitude:.2f} m/s^2, '
            f'gyro=({msg.angular_velocity.x:.2f}, '
            f'{msg.angular_velocity.y:.2f}, '
            f'{msg.angular_velocity.z:.2f}) rad/s'
        )

    def camera_callback(self, msg):
        """
        Process camera image data.

        Args:
            msg (Image): Camera image message
        """
        self.camera_data = msg
        self.camera_last_update = self.get_clock().now()

        self.get_logger().debug(
            f'Camera frame received: {msg.width}x{msg.height}, '
            f'encoding: {msg.encoding}'
        )

    def lidar_callback(self, msg):
        """
        Process LiDAR scan data.

        Args:
            msg (LaserScan): LiDAR scan message
        """
        self.lidar_data = msg
        self.lidar_last_update = self.get_clock().now()

        # Find minimum distance (filter out invalid readings)
        valid_ranges = [r for r in msg.ranges if r > msg.range_min and r < msg.range_max]

        if valid_ranges:
            min_distance = min(valid_ranges)

            # Warning for close obstacles
            if min_distance < self.obstacle_threshold:
                warning_msg = String()
                warning_msg.data = (
                    f'OBSTACLE DETECTED: {min_distance:.2f}m '
                    f'(threshold: {self.obstacle_threshold:.2f}m)'
                )
                self.warning_pub.publish(warning_msg)
                self.get_logger().warn(warning_msg.data)
            else:
                self.get_logger().debug(
                    f'LiDAR: clear path, min distance: {min_distance:.2f}m'
                )

    def publish_status(self):
        """
        Publish aggregated sensor status message.

        Called periodically by timer at configured update rate.
        """
        status_msg = String()

        # Build status message components
        status_parts = [f'Robot: {self.robot_name}']

        # IMU status
        if self.imu_data:
            status_parts.append('IMU: OK')
        else:
            status_parts.append('IMU: NO DATA')

        # Camera status
        if self.camera_data:
            status_parts.append(f'Camera: OK ({self.camera_data.width}x{self.camera_data.height})')
        else:
            status_parts.append('Camera: NO DATA')

        # LiDAR status
        if self.lidar_data:
            valid_ranges = [r for r in self.lidar_data.ranges
                           if r > self.lidar_data.range_min and r < self.lidar_data.range_max]
            if valid_ranges:
                min_dist = min(valid_ranges)
                status_parts.append(f'LiDAR: OK (min: {min_dist:.2f}m)')
            else:
                status_parts.append('LiDAR: NO VALID DATA')
        else:
            status_parts.append('LiDAR: NO DATA')

        # Assemble and publish
        status_msg.data = ' | '.join(status_parts)
        self.status_pub.publish(status_msg)

    def check_data_freshness(self):
        """
        Check if sensor data is stale (not updated recently).

        Logs warnings if any sensor hasn't sent data in the last 2 seconds.
        """
        current_time = self.get_clock().now()
        stale_threshold = rclpy.duration.Duration(seconds=2.0)

        # Check IMU freshness
        if self.imu_last_update:
            if (current_time - self.imu_last_update) > stale_threshold:
                self.get_logger().warn('IMU data is stale!')

        # Check camera freshness
        if self.camera_last_update:
            if (current_time - self.camera_last_update) > stale_threshold:
                self.get_logger().warn('Camera data is stale!')

        # Check LiDAR freshness
        if self.lidar_last_update:
            if (current_time - self.lidar_last_update) > stale_threshold:
                self.get_logger().warn('LiDAR data is stale!')


def main(args=None):
    """Main function to initialize and run the node."""
    rclpy.init(args=args)

    node = HumanoidSensorMonitor()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Shutting down due to keyboard interrupt')
    except Exception as e:
        node.get_logger().error(f'Unexpected error: {e}')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Minimal Publisher Node Example
Demonstrates basic ROS 2 topic publishing with rclpy

This node publishes string messages to the 'robot_status' topic every 0.5 seconds.
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MinimalPublisher(Node):
    """
    A minimal ROS 2 publisher node that periodically publishes status messages.
    """

    def __init__(self):
        """Initialize the publisher node with a timer and publisher."""
        super().__init__('minimal_publisher')

        # Create publisher: (message_type, topic_name, queue_size)
        self.publisher_ = self.create_publisher(String, 'robot_status', 10)

        # Create timer that calls timer_callback every 0.5 seconds
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.counter = 0
        self.get_logger().info('Minimal Publisher has been started')

    def timer_callback(self):
        """
        Callback function executed by the timer.
        Creates and publishes a status message.
        """
        msg = String()
        msg.data = f'Robot status update {self.counter}'

        # Publish the message
        self.publisher_.publish(msg)

        # Log to console
        self.get_logger().info(f'Publishing: "{msg.data}"')

        self.counter += 1


def main(args=None):
    """Main function to initialize and run the ROS 2 node."""
    # Initialize the rclpy library
    rclpy.init(args=args)

    # Create the node
    minimal_publisher = MinimalPublisher()

    # Spin the node so callbacks are processed
    try:
        rclpy.spin(minimal_publisher)
    except KeyboardInterrupt:
        pass

    # Cleanup
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

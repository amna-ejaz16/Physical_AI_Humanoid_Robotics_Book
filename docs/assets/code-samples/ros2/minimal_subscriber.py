#!/usr/bin/env python3
"""
Minimal Subscriber Node Example
Demonstrates basic ROS 2 topic subscription with rclpy

This node subscribes to the 'robot_status' topic and prints received messages.
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MinimalSubscriber(Node):
    """
    A minimal ROS 2 subscriber node that listens to status messages.
    """

    def __init__(self):
        """Initialize the subscriber node."""
        super().__init__('minimal_subscriber')

        # Create subscription: (message_type, topic_name, callback, queue_size)
        self.subscription = self.create_subscription(
            String,
            'robot_status',
            self.listener_callback,
            10
        )
        # Prevent unused variable warning
        self.subscription

        self.get_logger().info('Minimal Subscriber has been started')

    def listener_callback(self, msg):
        """
        Callback function executed when a message is received.

        Args:
            msg (String): The received message
        """
        self.get_logger().info(f'Received: "{msg.data}"')


def main(args=None):
    """Main function to initialize and run the ROS 2 node."""
    # Initialize the rclpy library
    rclpy.init(args=args)

    # Create the node
    minimal_subscriber = MinimalSubscriber()

    # Spin the node so callbacks are processed
    try:
        rclpy.spin(minimal_subscriber)
    except KeyboardInterrupt:
        pass

    # Cleanup
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

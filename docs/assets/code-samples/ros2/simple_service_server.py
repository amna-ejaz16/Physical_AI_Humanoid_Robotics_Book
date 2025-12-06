#!/usr/bin/env python3
"""
Simple Service Server Example
Demonstrates ROS 2 service implementation with rclpy

This node provides an 'add_two_ints' service that adds two integers.
"""

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class AdditionServiceNode(Node):
    """
    A ROS 2 service server that adds two integers.
    """

    def __init__(self):
        """Initialize the service server node."""
        super().__init__('addition_service')

        # Create service: (service_type, service_name, callback)
        self.srv = self.create_service(
            AddTwoInts,
            'add_two_ints',
            self.add_callback
        )

        self.get_logger().info('Addition Service Server is ready')

    def add_callback(self, request, response):
        """
        Service callback that processes addition requests.

        Args:
            request (AddTwoInts.Request): Contains 'a' and 'b' integers
            response (AddTwoInts.Response): Contains 'sum' result

        Returns:
            AddTwoInts.Response: Response with the sum
        """
        response.sum = request.a + request.b
        self.get_logger().info(
            f'Request: {request.a} + {request.b} = {response.sum}'
        )
        return response


def main(args=None):
    """Main function to initialize and run the ROS 2 node."""
    # Initialize the rclpy library
    rclpy.init(args=args)

    # Create the node
    addition_service = AdditionServiceNode()

    # Spin the node so callbacks are processed
    try:
        rclpy.spin(addition_service)
    except KeyboardInterrupt:
        pass

    # Cleanup
    addition_service.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

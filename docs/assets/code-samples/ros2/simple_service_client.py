#!/usr/bin/env python3
"""
Simple Service Client Example
Demonstrates ROS 2 service client implementation with rclpy

This node calls the 'add_two_ints' service with two numbers.
"""

import sys
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class AdditionClientNode(Node):
    """
    A ROS 2 service client that requests integer addition.
    """

    def __init__(self):
        """Initialize the service client node."""
        super().__init__('addition_client')

        # Create client: (service_type, service_name)
        self.client = self.create_client(AddTwoInts, 'add_two_ints')

        # Wait for the service to be available
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service to become available...')

        self.request = AddTwoInts.Request()
        self.get_logger().info('Addition Service Client is ready')

    def send_request(self, a, b):
        """
        Send an addition request to the service.

        Args:
            a (int): First number
            b (int): Second number

        Returns:
            Future: Async future for the service call
        """
        self.request.a = a
        self.request.b = b

        self.get_logger().info(f'Sending request: {a} + {b}')

        # Call the service asynchronously
        future = self.client.call_async(self.request)
        return future


def main(args=None):
    """Main function to initialize and run the ROS 2 node."""
    # Initialize the rclpy library
    rclpy.init(args=args)

    # Get command line arguments (numbers to add)
    if len(sys.argv) < 3:
        print('Usage: simple_service_client.py <num1> <num2>')
        return

    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    except ValueError:
        print('Error: Arguments must be integers')
        return

    # Create the node
    addition_client = AdditionClientNode()

    # Send the request
    future = addition_client.send_request(a, b)

    # Wait for the response
    rclpy.spin_until_future_complete(addition_client, future)

    # Get the result
    try:
        response = future.result()
        addition_client.get_logger().info(
            f'Result: {a} + {b} = {response.sum}'
        )
    except Exception as e:
        addition_client.get_logger().error(f'Service call failed: {e}')

    # Cleanup
    addition_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

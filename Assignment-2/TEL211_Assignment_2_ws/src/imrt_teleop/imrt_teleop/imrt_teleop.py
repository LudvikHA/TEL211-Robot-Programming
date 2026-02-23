#!/usr/bin/env python3
import rclpy
import numpy as np
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist, Vector3



class TeleopTurtleBot3(Node):
    def __init__(self):  
        super().__init__('teleopturtlebot3')
        self.subscription = self.create_subscription(Joy, 'joy', self.listener_callback, 10)

        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.get_logger().info(f'# Teleop for TurtleBot3 started', once=True)

    def listener_callback(self, msg):
        # Stick up is axes[0]
        # Stick to sides is axes[1]
        movement = Twist()
        movement.linear.x = msg.axes[0]*0.7
        movement.angular.z = msg.axes[1]*0.9
        self.publisher_.publish(movement)

def main(args=None):
    rclpy.init(args=args)
    teleop_turtlebot3 = TeleopTurtleBot3()
    rclpy.spin((teleop_turtlebot3))
    rclpy.shutdown()


if __name__ == '__main__':
    main()
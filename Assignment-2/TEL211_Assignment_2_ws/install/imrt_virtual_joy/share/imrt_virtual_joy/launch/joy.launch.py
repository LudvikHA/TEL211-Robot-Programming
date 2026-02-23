from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            namespace="imrt_virtual_joy",
            package="imrt_virtual_joy",
            executable="gamepad_talker",
            output="screen",
        ),
    ])

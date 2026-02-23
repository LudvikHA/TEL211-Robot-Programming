from launch import LaunchDescription
from launch_ros.actions import Node


# def generate_launch_description():
#     virtual_gamepad_node = launch_ros.actions.Node(
#     namespace="imrt_virtual_joy",
#     package="imrt_virtual_joy",
#     executable="gamepad_talker",
#     output="screen"
#     )

#     return LaunchDescription([
#     virtual_gamepad_node
#     ])


def generate_launch_description():
    return LaunchDescription([
        Node(
            namespace="imrt_virtual_joy",
            package="imrt_virtual_joy",
            executable="gamepad_talker",
            output="screen",
        ),
    ])

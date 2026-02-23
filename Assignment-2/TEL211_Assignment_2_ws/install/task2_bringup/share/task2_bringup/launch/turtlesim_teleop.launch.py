from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    return LaunchDescription([
        Node(
            package="turtlesim",
            executable="turtlesim_node",
        ),

        Node(
            namespace="imrt_virtual_joy",
            package="imrt_virtual_joy",
            executable="gamepad_talker",
            output="screen",
        ),

        Node(
            namespace="imrt_teleop_turtlesim",
            package="imrt_teleop",
            executable="teleop_turtlesim",
        ),
    ])



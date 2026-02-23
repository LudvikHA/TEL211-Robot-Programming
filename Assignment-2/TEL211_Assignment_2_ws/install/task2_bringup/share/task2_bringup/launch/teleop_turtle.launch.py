from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    return LaunchDescription([

        SetEnvironmentVariable(
            name='TURTLEBOT3_MODEL',
            value='burger'
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution([
                    FindPackageShare("turtlebot3_gazebo"),
                    "launch",
                    "empty_world.launch.py"
                ])
            )
        ),
        
        Node(
            namespace="imrt_virtual_joy",
            package="imrt_virtual_joy",
            executable="gamepad_talker",
            output="screen",
        ),

        Node(
            namespace="imrt_teleop",
            package="imrt_teleop",
            executable="teleop",
        ),
    ])



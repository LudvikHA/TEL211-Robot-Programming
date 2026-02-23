from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'task2_bringup'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ludvikha',
    maintainer_email='ludvik.hoibjerg-aslaksen@nmbu.no',
    description='Launch everything required by task',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            # "gamepad_talker = imrt_virtual_joy.gamepad_talker:main",
            # "teleop_turtlesim = imrt_teleop.imrt_teleop_turtlesim:main",
            # "teleop = imrt_teleop.imrt_teleop:main",
        ],
    },
)

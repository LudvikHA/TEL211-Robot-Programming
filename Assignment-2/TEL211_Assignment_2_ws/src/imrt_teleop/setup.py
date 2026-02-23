from setuptools import find_packages, setup

package_name = 'imrt_teleop'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ludvikha',
    maintainer_email='ludvik.hoibjerg-aslaksen@nmbu.no',
    description='Teleop for TurtleBot3',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "teleop = imrt_teleop.imrt_teleop:main",
            "teleop_turtlesim = imrt_teleop.imrt_teleop_turtlesim:main",
        ],
    },
)

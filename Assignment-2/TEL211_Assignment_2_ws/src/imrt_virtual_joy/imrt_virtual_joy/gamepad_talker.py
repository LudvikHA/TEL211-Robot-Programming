#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from PyQt5 import QtWidgets, QtGui, QtCore
import threading
try:
    from .gamepad import GamePad
except ImportError:
    from gamepad import GamePad

class GamepadTalker(Node):
    def __init__(self, gamepad):  
        super().__init__('gamepad_talker')
        self.publisher_ = self.create_publisher(Joy, 'joy', 10)
        timer_period = 0.05 
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.gamepad = gamepad
        self.get_logger().info(f'# Virtual gamepad started', once=True)


    def timer_callback(self):
        [axes, buttons] = self.gamepad._output_data()

        message = Joy()
        message.axes = [float(axis) for axis in axes]
        message.buttons = buttons
        self.publisher_.publish(message)

def start_ros_thread():
    rclpy.init()
    gamepad_talker = GamepadTalker(gamepad)  # Pass gamepad instance
    rclpy.spin(gamepad_talker)
    rclpy.shutdown()

def main(args=None):
    global gamepad
    global app
    app = QtWidgets.QApplication([])
    app.setStyleSheet(
        """
        QMainWindow{background-color: #ECEFF4; 
                    border: 8px double #4C566A;
                    border-radius: 20px;}
        QPushButton{background-color: #88C0D0;
                    color: #4C566A}
        """)
    gamepad = GamePad(autorepeat=False)
    ros_thread = threading.Thread(target=start_ros_thread)
    ros_thread.start()
    app.exec_()
    ros_thread.join()

if __name__ == '__main__':
    main()

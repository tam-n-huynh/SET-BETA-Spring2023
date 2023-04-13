import rclpy
from rclpy.node import Node
from std_msgs.msg import String

import serial

class ServoController(Node):
    def __init__(self):
        super().__init__('servo_controller')
        
        # Set up the serial connection to the Arduino
        self.ser = serial.Serial('COM15', 9600, timeout=1)
        
        # Subscribe to the servo angle topic
        self.subscription = self.create_subscription(String, 'topic', self.servo_angle_callback, 10)
        self.subscription  # prevent unused variable warning
        
    def servo_angle_callback(self, msg):
        # send angle in form of string to the Arduino
        self.ser.write((msg.data).encode())
        self.get_logger().info('I heard: "%s"' % msg.data)
        
        
def main(args=None):
    rclpy.init(args=args)

    servo_controller = ServoController()

    rclpy.spin(servo_controller)


if __name__ == '__main__':
    main()
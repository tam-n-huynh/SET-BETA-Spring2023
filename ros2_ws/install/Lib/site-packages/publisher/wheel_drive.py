import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from adafruit_motorkit import MotorKit

class wheel_drive(Node):
    def __init__(self):
        super().__init__('wheel_drive')
        
        # Subscribe to the servo angle topic
        self.subscription = self.create_subscription(String, 'topic', self.servo_angle_callback, 10)
        self.subscription  # prevent unused variable warning
    

    def servo_angle_callback(self, msg):
        # send angle in form of string to the Arduino

        kit = MotorKit()

        self.get_logger().info('I heard: "%s"' % msg.data)
        if msg.data == 'w' :
            kit.motor1.throttle = 1;
            kit.motor2.throttle = 1;
            kit.motor3.throttle = 1;

            time.sleep(5);

            kit.motor1.throttle = 0;
            kit.motor2.throttle = 0;
            kit.motor3.throttle = 0;
        elif msg.data == 's' :
            kit.motor1.throttle = 0.2;
            kit.motor2.throttle = 1;
            kit.motor3.throttle = 1;

            time.sleep(5);

            kit.motor1.throttle = 0;
            kit.motor2.throttle = 0;
            kit.motor3.throttle = 0;
        elif msg.data == 'a':
            robot.left
        elif msg.data == 'd':
            robot.right
        
        
def main(args=None):
    rclpy.init(args=args)

    wheel_drive = WheelDrive()

    rclpy.spin(wheel_drive)


if __name__ == '__main__':
    main()
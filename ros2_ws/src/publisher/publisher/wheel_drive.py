import rclpy
from rclpy.node import Node
from std_msgs.msg import String

#from adafruit_motorkit import MotorKit

class WheelDrive(Node):
    
    def __init__(self):
        super().__init__('wheel_drive')
        #kit = MotorKit()
        
        # Subscribe to the servo angle topic
        self.subscription = self.create_subscription(String, 'topic', self.servo_angle_callback, 10)
        self.subscription  # prevent unused variable warning
    

    def servo_angle_callback(self, msg, count):
        if read == 'w' :
            self.get_logger().info("going forward")
            #kit.motor1.throttle = 1;
            #kit.motor2.throttle = 1;
            #kit.motor3.throttle = 1;

            #time.sleep(5);

            #kit.motor1.throttle = 0;
            #kit.motor2.throttle = 0;
            #kit.motor3.throttle = 0;
        elif read == 's' :
            self.get_logger().info("going backwards")
            #kit.motor1.throttle = 0.2;
            #kit.motor2.throttle = 1;
            #kit.motor3.throttle = 1;

            #time.sleep(5);

            #kit.motor1.throttle = 0;
            #kit.motor2.throttle = 0;
            #kit.motor3.throttle = 0;
        
        
def main(args=None):
    rclpy.init(args=args)

    wheel_drive = WheelDrive()

    rclpy.spin(wheel_drive)


if __name__ == '__main__':
    main()
import rclpy
from rclpy.node import Node

from std_msgs.msg import String
import readchar


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        #timer_period = 2  # seconds
        self.timer = self.create_timer(1.0, self.timer_callback)
        #self.i = 0

    def timer_callback(self):
        #motions = ['w', 's']
        msg = String()
        msg.data = readchar.readchar()
        #name = input("enter")
        #msg.data = "works"
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg)
        #self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
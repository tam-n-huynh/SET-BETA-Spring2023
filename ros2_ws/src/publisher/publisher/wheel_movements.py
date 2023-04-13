from adafruit_motorkit import MotorKit
import time

class wheel_movements(object):
    # Initialize MotorKit
    kit = MotorKit()

    def forward (self, time):
        kit.motor1.throttle = 1;
        kit.motor2.throttle = 1;
        kit.motor3.throttle = 1;

        time.sleep(5);

        kit.motor1.throttle = 0;
        kit.motor2.throttle = 0;
        kit.motor3.throttle = 0;

    def forward (self, time):
        kit.motor1.throttle = 0.2;
        kit.motor2.throttle = 1;
        kit.motor3.throttle = 1;

        time.sleep(5);

        kit.motor1.throttle = 0;
        kit.motor2.throttle = 0;
        kit.motor3.throttle = 0;






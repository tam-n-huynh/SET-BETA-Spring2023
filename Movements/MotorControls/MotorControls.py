from .PCA9685 import PCA9685

from enum import IntEnum
import math
 

class Direction(IntEnum):
    forward = 0
    backward = 1


# PWM Controller Object Singleton
class PWMController:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PWMController, cls).__new__(cls)
            cls.instance.pwm = PCA9685(address=0x60, debug=False)
            cls.instance.pwm.setPWMFreq(50)
        return cls.instance


class Motor:
    def __init__(self, pwm: int, in1: int, in2: int) -> None:
        self.pwm = pwm 
        self.in1 = in1
        self.in2 = in2


class MotorFunctions:
    @staticmethod
    def motor_run(motor: Motor, index: Direction, speed: int) -> None:
        if speed > 100:
            return

        pwm = PWMController().pwm
        pwm.setDutycycle(motor.pwm, speed)
        pwm.setLevel(motor.in1, int(index))
        pwm.setLevel(motor.in2, int(not bool(int(index))))

    @staticmethod
    def motor_run_signed(motor: Motor, velocity: float) -> None:
        if math.fabs(velocity) > 1:
            return

        MotorFunctions.motor_run(motor, Direction(int(velocity < 0)), int(math.fabs(velocity) * 100))

    @staticmethod
    def motor_stop(motor: Motor) -> None:
        pwm = PWMController().pwm
        pwm.setDutycycle(motor.pwm, 0)
        
    @staticmethod
    def servoDC(motor: Motor, dc : float) -> None:
        pwm = PWMController().pwm
        pwm.setDutycycle(motor.pwm, dc)


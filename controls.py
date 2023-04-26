from Movements.MotorControls.MotorControls import Motor, MotorFunctions

import math

"""
PWM pinouts for each motor on the controller
motor1 = Motor(pwm=7, in1=5, in2=6)
motor2 = Motor(pwm=2, in1=4, in2=3)
motor3 = Motor(pwm=13, in1=11, in2=12)
motor4 = Motor(pwm=8, in1=10, in2=9)
"""


class Robot:
    def __init__(self):
        # motor objects, 1-indexed
        self.motors = [None, Motor(pwm=7, in1=5, in2=6), Motor(pwm=2, in1=4, in2=3), Motor(pwm=13, in1=11, in2=12)]
        # vectors representing the forward direction of rotation of each motor
        self.di = [None, (0., -1.), (math.sqrt(3.) / 2., 0.5), (-math.sqrt(3.) / 2., 0.5)]

    def move(self, angle: float, velocity: float) -> None:
        """
        :param angle: floating point value in the interval [-180, 180] representing the angle
        from the forward direction to travel in
        :param velocity: float in the interval [0, 1] representing the fraction of max velocity to travel at
        :return: void
        """

        if not -180. <= angle <= 180. or not 0 <= velocity <= 1:
            return

        r = (velocity * math.cos(angle / 180. * math.pi), velocity * math.sin(angle / 180. * math.pi))

        for motor, d in zip(self.motors[1:], self.di[1:]):
            print((d[0] * r[0] + d[1] * r[1]))
            MotorFunctions.motor_run_signed(motor=motor, velocity=(d[0] * r[0] + d[1] * r[1]))

    def rotate(self, velocity: float) -> None:
        if not -1 <= velocity <= 1:
            print("Invalid velocity for rotation")
        for motor in self.motors[1:]:
            MotorFunctions.motor_run_signed(motor=motor, velocity=velocity)

    def stop(self) -> None:
        for motor in self.motors[1:]:
            MotorFunctions.motor_stop(motor=motor)


from gpiozero import AngularServo
from time import sleep

servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)
servo2 = AngularServo(15, min_pulse_width=0.0005, max_pulse_width=0.0023)

while(True):
    servo.angle = 90
    servo2.angle = 0
    sleep(0)
    servo.angle = 0
    servo2.angle = 90
    sleep(2)
    servo.angle = -90
    servo2.angle = 0
    sleep(2)



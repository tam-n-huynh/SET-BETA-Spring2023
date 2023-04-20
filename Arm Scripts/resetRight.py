from gpiozero import AngularServo
from time import sleep

servo = AngularServo(15, min_pulse_width=0.0006, max_pulse_width=0.0023)

servo.angle = 0
sleep(2)
servo.angle = 45


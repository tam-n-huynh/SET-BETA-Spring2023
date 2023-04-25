import RPi.GPIO as GPIO
import time

# Set the pin number and frequency for the PWM output
LeftArmPWM = 15
RightArmPWM = 14
frequency = 60

# Set the minimum and maximum duty cycle values for the servo motor
min_duty_cycle = 2.5
max_duty_cycle = 12.5

# Initialize the PWM pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(LeftArmPWM, GPIO.OUT)
GPIO.setup(RightArmPWM, GPIO.OUT)
left = GPIO.PWM(LeftArmPWM, frequency)
right = GPIO.PWM(RightArmPWM, frequency)
right.start(0)
left.start(0)

# Set the angle of the servo motor
def angleLeft(angle):
    duty_cycle = ((angle / 180) * (max_duty_cycle - min_duty_cycle)) + min_duty_cycle
    right.ChangeDutyCycle(duty_cycle)

def angleRight(angle):
    duty_cycle = ((angle / 180) * (max_duty_cycle - min_duty_cycle)) + min_duty_cycle
    right.ChangeDutyCycle(duty_cycle)

def angleMaster(angle):
    angleRight(angle)
    angleLeft(angle)

# Clean up the GPIO pins
pwm.stop()
GPIO.cleanup()


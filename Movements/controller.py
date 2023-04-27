import pygame
import time

pygame.init()

devices = pygame.joystick.get_count() # gets all available joysticks
print(devices)

joystick = pygame.joystick.Joystick(0) # picking joystick
joystick.init()

while True:
    pygame.event.pump()
    x_axis = joystick.get_axis(0)
    y_axis = joystick.get_axis(1) * -1
    if x_axis > 0.5:
        # turn and move right
        # bot.move(90, 1)
        print(x_axis, y_axis)
    elif x_axis < -0.5:
        # turn and move left
        #bot.move(-90, 1)
        print(x_axis, y_axis)
    elif y_axis > 0.5:
        # move forward
        # bot.move(0, 1)
        print(x_axis, y_axis)
    elif y_axis < -0.5:
        # move backward
        # bot.move(180, 1)
        print(x_axis, y_axis)
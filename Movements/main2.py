from controls import Robot
import readchar
import time
import pygame
from evdev import InputDevice, categorize, ecodes
import math


def griddy(bot : Robot()):
	bot.arms(0)
	for i in range(3):
		bot.move(0, 0.6)
		bot.arms(90)
		time.sleep(0.75)
		bot.stop()
		bot.move(0, 1)
		bot.arms(0)
		time.sleep(0.75)
	bot.stop()

def main(args=None):
    pygame.init()
    pygame.joystick.init()

    devices = pygame.joystick.get_count()

    bot = Robot()
    sleep = 0.5

    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    x_axis, y_axis = 0, 0
    gamepad = InputDevice('/dev/input/event4')
    for event in gamepad.read_loop():
        if event.type == ecodes.EV_KEY:
            griddy(bot)
        elif event.type == ecodes.EV_ABS:
            absevent = categorize(event)
            if absevent.event.code in [ecodes.ABS_X, ecodes.ABS_Y]:
                if absevent.event.code == ecodes.ABS_X:
                    x_axis = absevent.event.value
                elif absevent.event.code == ecodes.ABS_Y:
                    y_axis = absevent.event.value

                # This is where the controls will go
                try:
                    x, y = (x_axis - 128) / 128, ((y_axis - 128) / 128) * -1
                
                    modulus = math.sqrt(x**2+y**2) if x != 0 else 0

                    angle= math.atan(y/x) if x != 0 else 0
                    print("angle and modulus",angle, modulus)
                    bot.move(angle, modulus)
                except KeyboardInterrupt:
                    bot.stop()
                #bot.stop()
                # print(x, y)

                # print("helo")
                # if y > 0.5:
                #     bot.move(0, 1)
                #     # time.sleep(sleep)
                #     # bot.stop()
                #     print("bot move forward")
                # elif y < -0.5:
                #     bot.move(180, 1)
                #     # time.sleep(sleep)
                #     # bot.stop()
                #     print("bot move back")
                
                

main()

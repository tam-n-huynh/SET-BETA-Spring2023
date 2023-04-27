from controls import Robot
import readchar
import time
import pygame.joystick



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

	bot = Robot()
	sleep = 0.5
	while (True): 
		print("helo")
		op = readchar.readchar()
		if op == 'w':
			bot.move(0, 1)
			time.sleep(sleep)
			bot.stop()
		elif op == 'e':
			bot.move(-45, 1)
			time.sleep(sleep)
			bot.stop()
		elif op == 'd':
			bot.move(-90, 1)
			time.sleep(sleep)
			bot.stop()
		elif op == 'c':
			bot.move(-135, 1)
			time.sleep(sleep)
			bot.stop()
		elif op == 'x':
			bot.move(180, 1)
			time.sleep(sleep)
			bot.stop()
		elif op == 'z':
			bot.move(135, 1)
			time.sleep(sleep)
			bot.stop()
		elif op == 'a':
			bot.move(90, 1)
			time.sleep(sleep)
			bot.stop()
		elif op == 'q':
			bot.move(45, 1)
			time.sleep(sleep)
			bot.stop()

		elif op == 'p':
			armAng = armAng-5
			armAng = armAng % 181
			bot.arms(armAng)
		elif op =='o':
			armAng = 5+armAng
			armAng = armAng % 181
			bot.arms(armAng)
		elif op == 's':
			bot.move(180, 1)
			time.sleep(1)
			bot.stop()
		elif op == ',':
			bot.rotate(1)
			time.sleep(0.25)
			bot.stop()
		elif op == '.':
			bot.rotate(0)
			time.sleep(0.25)
			bot.stop()
		elif op == '`':
			break;

main()

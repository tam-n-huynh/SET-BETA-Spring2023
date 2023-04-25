from controls import Robot
import readchar
import time

def griddy(bot : Robot()):
	bot.arms(0)
	for i in range(3):
		bot.move(0, 1)
		bot.arms(90)
		time.sleep(0.75)
		bot.arms(0)
		time.sleep(0.75)
	bot.stop()

def main(args=None):
	bot = Robot()
	while (True): 
		print("helo")
		op = readchar.readchar()
		if op == 'w':
			bot.move(0, 1)
			time.sleep(1)
			bot.stop()
			print("works")
		elif op == 'p':
			griddy(bot)
		elif op =='o':
			bot.arms(90)
		elif op == 's':
			bot.move(180, 1)
			time.sleep(1)
			bot.stop()
		elif op == 'r':
			bot.rotate()
			time.sleep(1)
			bot.stop()

		else:
			break

main()

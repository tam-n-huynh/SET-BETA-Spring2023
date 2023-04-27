from screen import Display
import readchar

def main(args=None):
	face = Display()
	face.show(1)
	while (True): 
		op = readchar.readchar()
		if op == 'w':
			face.show(0)
		elif op == 'e':
			face.show(1)
		elif op == '`':
			break;

main()
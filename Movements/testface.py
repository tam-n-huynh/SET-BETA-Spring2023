from screen import Display
import time

def main():
    face = Display()
    for i in range(15):
        face.show(i)
        time.sleep(2)

main()
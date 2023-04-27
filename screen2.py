from tkinter import *
import os
from PIL import Image, ImageTk

class Display():
    def __init__(self): 
        # Define image filenames and paths
        IMAGE_PATHS = ['cute.gif', 'blink.gif']
        IMAGE_DIR = ''

        # Create Tk object
        root = Tk()
        root.attributes("-fullscreen", True)

        # Create canvas and pack it into the root window
        canvas = Canvas(root)
        canvas.pack(fill=BOTH, expand=YES)

        # Initialize variables
        curr_image_index = 0
        delay_time = 1000  # milliseconds

    def show(self, num : int):
        curr_image_index = num
        # Open current image file
        image_path = os.path.join(IMAGE_DIR, IMAGE_PATHS[curr_image_index])
        image = Image.open(image_path)
        image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)

        # Create PhotoImage object using the Tk object
        photo = ImageTk.PhotoImage(image, master=root)

        # Display image on canvas
        canvas.delete("all")
        canvas.create_image(0, 0, anchor=NW, image=photo)
        canvas.update()


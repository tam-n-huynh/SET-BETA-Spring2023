from tkinter import *
import os
from PIL import Image, ImageTk

class Display():
    def __init__(self): 
        # Define image filenames and paths
        self.IMAGE_PATHS = ['cute.gif', 'blink.gif']
        self.IMAGE_DIR = ''

        # Create Tk object
        self.root = Tk()
        self.root.attributes("-fullscreen", False)

        # Create canvas and pack it into the root window
        self.canvas = Canvas(self.root)
        #self.canvas.pack(fill=BOTH, expand=YES)

        # Initialize variables
        self.curr_image_index = 0
        self.delay_time = 1000  # milliseconds

    def show(self, num : int):
        self.curr_image_index = num
        # Open current image file
        image_path = os.path.join(self.IMAGE_DIR, self.IMAGE_PATHS[self.curr_image_index])
        image = Image.open(image_path)
        #image = image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.ANTIALIAS)

        # Create PhotoImage object using the Tk object
        photo = ImageTk.PhotoImage(image, master=self.root)

        # Display image on canvas
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor=NW, image=photo)
        self.canvas.update()


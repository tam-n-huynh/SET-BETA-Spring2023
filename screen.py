from PIL import Image
import os
import time

# Define image filenames and paths
IMAGE_PATHS = ['image1.jpg', 'image2.jpg']
IMAGE_DIR = ''

# Define function to toggle between images
def toggle_image(curr_image_index):
    curr_image_index += 1
    if curr_image_index >= len(IMAGE_PATHS):
        curr_image_index = 0
    return curr_image_index

# Initialize variables
curr_image_index = 0
delay_time = 1  # seconds

while True:
    # Open current image file
    image_path = os.path.join(IMAGE_DIR, IMAGE_PATHS[curr_image_index])
    image = Image.open(image_path)
    
    # Display image
    image.show()
    
    # Wait for delay time
    time.sleep(delay_time)
    
    # Close image
    image.close()
    
    # Toggle to next image
    curr_image_index = toggle_image(curr_image_index)

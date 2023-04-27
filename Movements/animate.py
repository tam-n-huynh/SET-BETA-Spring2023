import pygame
from PIL import Image, ImageSequence

def animate(filename : str) :
    # Initialize pygame screen
    pygame.init()
    pygame.display.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # Open current image file
    image = Image.open(filename)

    # create a list of image frames
    frames = []
    for frame in ImageSequence.Iterator(image):
        frames.append(frame.copy().convert('RGB'))

    # create a list of pygame surfaces
    surfaces = []
    for frame in frames:
        frame = frame.resize(screen.get_size())
        surfaces.append(pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode))

    # display the gif animation
    running = True
    while running:
        clock = pygame.time.Clock()
        for surface in surfaces:
            for event in pygame.event.get():
              if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                  running = False
            screen.blit(surface, (0,0))
            pygame.display.flip()
            clock.tick(5)

    pygame.quit()
    exit()
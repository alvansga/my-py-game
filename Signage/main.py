# import the pygame module, so you can use it
import pygame
from urllib.request import urlopen
import io

# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((1366,768),)

    image_url = "https://alvansga.github.io/img/res/pic%20(2).jpg"

    # image_url = "http://matplotlib.org/_images/fill_demo.png"
    
    image_str = urlopen(image_url).read()
    image_file = io.BytesIO(image_str)
    image = pygame.image.load(image_file)
    image = pygame.transform.scale(image, (1366,768))
     
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        screen.blit(image, (0, 0))
        pygame.display.flip()

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
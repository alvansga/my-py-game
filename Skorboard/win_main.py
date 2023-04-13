# import the pygame module, so you can use it
import pygame
# import evdev
 
# dev = evdev.InputDevice('/dev/input/event3')
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((1366,768))
    # screen = pygame.display.set_mode((1366,768), pygame.FULLSCREEN)
     
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                screen.fill((255,255,255))
                pygame.display.flip()
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
                screen.fill((128,0,0))
                pygame.display.flip()
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
                screen.fill((0,128,0))
                pygame.display.flip()
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
                screen.fill((0,0,128))
                pygame.display.flip()
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
                screen.fill((128,0,128))
                pygame.display.flip()

        # for event in dev.read_loop():
        # #	print(evdev.categorize(event))
        #     if hex(event.value) == "0x0":
        #         continue
        #     elif hex(event.value) == "0x800b":
        #         screen.fill((255,255,255))
        #         pygame.display.flip()
        #     elif hex(event.value) == "0x800c":
        #         screen.fill((128,0,0))
        #         pygame.display.flip()
        #     elif hex(event.value) == "0x800d":
        #         screen.fill((0,128,0))
        #         pygame.display.flip()
        #     elif hex(event.value) == "0x800e":
        #         screen.fill((0,0,128))
        #         pygame.display.flip()
        #     elif hex(event.value) == "0x800f":
        #         screen.fill((128,0,128))
        #         pygame.display.flip()
            
        #     #print("\nCode:",hex(event.value))
        #     #print("---------------")
        #     pass
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()

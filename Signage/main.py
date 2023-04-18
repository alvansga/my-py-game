# import the pygame module, so you can use it
import pygame
from urllib.request import urlopen
import io

import evdev
dev = evdev.InputDevice('/dev/input/event0')

IRKEY_UP = "0x800c"
IRKEY_DOWN = "0x800d"
IRKEY_RIGHT = "0x800e"
IRKEY_LEFT = "0x800f"

IRKEY_SELECT = "0x8014"

IRKEY_NUM1 = "0x8001"
IRKEY_NUM2 = "0x8002"
IRKEY_NUM3 = "0x8003"
IRKEY_NUM4 = "0x8004"
IRKEY_NUM5 = "0x8005"
IRKEY_NUM6 = "0x8006"
IRKEY_NUM7 = "0x8007"
IRKEY_NUM8 = "0x8008"
IRKEY_NUM9 = "0x8009"

IRKEY_STOP = "0x801f"

# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((1366,768), pygame.FULLSCREEN)

    # image_url = "http://matplotlib.org/_images/fill_demo.png"
    
    list_image = list()
    for i in range(1,27):
        image_url = "https://alvansga.github.io/img/res/pic%20("+ str(i) + ").jpg"
        image_str = urlopen(image_url).read()
        list_image.append(image_str)
    
    idx = 0
    # print(list_image)

    image_file = io.BytesIO(list_image[idx])
    image = pygame.image.load(image_file)
    image = pygame.transform.scale(image, (1366,768))
     
    # define a variable to control the main loop
    running = True

    stamp_time = pygame.time.get_ticks()
     
    # main loop
    while running:
        try:
            screen.blit(image, (0, 0))
        except:
            print("no image")
            pass
        pygame.display.flip()

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        # for event in dev.read_loop():
        event = dev.read_one()
        if event:
            if pygame.time.get_ticks() - stamp_time < 200: #200ms
                continue
            stamp_time = pygame.time.get_ticks()
            
            if hex(event.value) == "0x0":
                continue
            elif hex(event.value) == IRKEY_NUM1:
                image_file = io.BytesIO(list_image[10])
                image = pygame.image.load(image_file)
                image = pygame.transform.scale(image, (1366,768))
            elif hex(event.value) == IRKEY_NUM2:
                image_file = io.BytesIO(list_image[11])
                image = pygame.image.load(image_file)
                image = pygame.transform.scale(image, (1366,768))
            elif hex(event.value) == IRKEY_NUM3:
                image_file = io.BytesIO(list_image[12])
                image = pygame.image.load(image_file)
                image = pygame.transform.scale(image, (1366,768))
            elif hex(event.value) == IRKEY_NUM4:
                image_file = io.BytesIO(list_image[13])
                image = pygame.image.load(image_file)
                image = pygame.transform.scale(image, (1366,768))
            elif hex(event.value) == IRKEY_NUM5:
                image_file = io.BytesIO(list_image[14])
                image = pygame.image.load(image_file)
                image = pygame.transform.scale(image, (1366,768))
            elif hex(event.value) == IRKEY_NUM6:
                image_file = io.BytesIO(list_image[15])
                image = pygame.image.load(image_file)
                image = pygame.transform.scale(image, (1366,768))
            elif hex(event.value) == IRKEY_NUM7:
                image_file = io.BytesIO(list_image[16])
                image = pygame.image.load(image_file)
                image = pygame.transform.scale(image, (1366,768))
            elif hex(event.value) == IRKEY_NUM8:
                image_file = io.BytesIO(list_image[17])
                image = pygame.image.load(image_file)
                image = pygame.transform.scale(image, (1366,768))
            elif hex(event.value) == IRKEY_NUM9:
                image_file = io.BytesIO(list_image[18])
                image = pygame.image.load(image_file)
                image = pygame.transform.scale(image, (1366,768))

            elif hex(event.value) == IRKEY_UP:
                # screen.fill((128,0,0))
                # image_url = "https://alvansga.github.io/img/res/pic%20(2).jpg"
                # image_str = urlopen(image_url).read()
                # image_file = io.BytesIO(image_str)
                # image = pygame.image.load(image_file)
                # image = pygame.transform.scale(image, (1366,768))
                pass
            elif hex(event.value) == IRKEY_DOWN:
                # screen.fill((0,128,0))
                # image_url = "https://alvansga.github.io/img/res/pic%20(21).jpg"
                # image_str = urlopen(image_url).read()
                # image_file = io.BytesIO(image_str)
                # image = pygame.image.load(image_file)
                # image = pygame.transform.scale(image, (1366,768))
                pass
            elif hex(event.value) == IRKEY_RIGHT:
                idx += 1
                if idx == len(list_image):
                    idx = 0
                print("inc idx --> ",idx)
                
                image_file = io.BytesIO(list_image[idx])
                image = pygame.image.load(image_file)
                image = pygame.transform.scale(image, (1366,768))
                pass
            elif hex(event.value) == IRKEY_LEFT:
                idx -= 1
                if idx < 0:
                    idx = len(list_image)-1
                print("dec idx --> ",idx)

                image_file = io.BytesIO(list_image[idx])
                image = pygame.image.load(image_file)
                image = pygame.transform.scale(image, (1366,768))
                pass
            elif hex(event.value) == IRKEY_SELECT:
                print("refreshing images...")
                top = pygame.Surface((1366, 768//24))
                top.set_alpha(128)
                top.fill((0,0,0))
                screen.blit(top,(0,0))

                font = pygame.font.Font('freesansbold.ttf', 14)
                txt_color = (255,255,255)
                text = font.render("Please wait...", True, txt_color)
                textRect = text.get_rect()
                textRect.center = (1366//2, 768//24//2)
                screen.blit(text, textRect)
                pygame.display.flip()

                list_image = list()
                for i in range(1,27):
                    image_url = "https://alvansga.github.io/img/res/pic%20("+ str(i) + ").jpg"
                    image_str = urlopen(image_url).read()
                    list_image.append(image_str)
                print("done!")
                pass

            elif hex(event.value) == IRKEY_STOP:
                running = False
                
            print("\nCode:",hex(event.value))
            print("---------------")
            pass
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
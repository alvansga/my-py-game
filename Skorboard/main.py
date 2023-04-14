# import the pygame module, so you can use it
import evdev
dev = evdev.InputDevice('/dev/input/event3')

from Game import *

IRKEY_EXIT = "0x804b"
IRKEY_MENU = "0x800b"

IRKEY_UP = "0x800c"
IRKEY_DOWN = "0x800d"
IRKEY_RIGHT = "0x800e"
IRKEY_LEFT = "0x800f"

#IRKEY_SELECT = "0x8014"
IRKEY_PRDOWN = "0x8018"

IRKEY_NUM0 = "0x8000"
IRKEY_NUM1 = "0x8001"
IRKEY_NUM3 = "0x8003"
IRKEY_NUM5 = "0x8005"
IRKEY_NUM7 = "0x8007"
IRKEY_NUM9 = "0x8009"

# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Score Board")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGTH) , pygame.FULLSCREEN)
     
    # define a variable to control the main loop
    running = True
    
    room = Game("TT", 2)
    stamp_time = pygame.time.get_ticks() #time.time()

    # main loop
    while running:
        #print(".")
        room.updateScreen(screen)
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                # screen.fill((255,255,255))
                pass
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
                # screen.fill((128,0,0))
                pass
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
                # screen.fill((0,128,0))
                pass
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
                # screen.fill((0,0,128))
                room.serv = -1
                pass
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
                # screen.fill((128,0,128))
                room.serv = 0
                pass
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_1):
                room.skor[len(room.skor)-1][TEAM_LEFT] += 1
                room.checkService()
                pass
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_3):
                room.skor[len(room.skor)-1][TEAM_RIGHT] += 1
                room.checkService()
                pass
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_7):
                # screen.fill((128,0,0))
                room.skor[len(room.skor)-1][TEAM_LEFT] -= 1
                room.checkService()
                pass
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_9):
                # screen.fill((128,0,0))
                room.skor[len(room.skor)-1][TEAM_RIGHT] -= 1
                room.checkService()
                pass
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_5):
                # screen.fill((128,0,0))
                room.skor.append([0,0])
                room.checkService()
                print(room.skor)
                pass
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_r):
                # screen.fill((128,0,0))
                room.reset()
                room.checkService()
                pass
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_s):
                # screen.fill((128,0,0))
                room.changeCourt()
                print(room.skor)
                pass

        for event in dev.read_loop():
            if pygame.time.get_ticks() - stamp_time < 200: #200ms
                break
            stamp_time = pygame.time.get_ticks()
            
            if hex(event.value) == "0x0":
                continue
            # elif hex(event.value) == IRKEY_EXIT:
            #     running = False
            #     print("exiting...")
            #     break
            elif hex(event.value) == IRKEY_MENU:
                # screen.fill((0,0,0))
                pass
            elif hex(event.value) == IRKEY_UP:
                # screen.fill((128,0,0))
                pass
            elif hex(event.value) == IRKEY_DOWN:
                # screen.fill((0,128,0))
                pass
            elif hex(event.value) == IRKEY_RIGHT:
                # screen.fill((0,0,128))
                room.serv = -1
                break
            elif hex(event.value) == IRKEY_LEFT:
                # screen.fill((128,0,128))
                room.serv = 0
                break
            elif hex(event.value) == IRKEY_NUM1:
                # screen.fill((0,128,0))
                room.skor[len(room.skor)-1][TEAM_LEFT] += 1
                room.checkService()
                break
            elif hex(event.value) == IRKEY_NUM3:
                room.skor[len(room.skor)-1][TEAM_RIGHT] += 1
                room.checkService()
                break
            elif hex(event.value) == IRKEY_NUM7:
                room.skor[len(room.skor)-1][TEAM_LEFT] -= 1
                room.checkService()
                break
            elif hex(event.value) == IRKEY_NUM9:
                room.skor[len(room.skor)-1][TEAM_RIGHT] -= 1
                room.checkService()
                break
            elif hex(event.value) == IRKEY_NUM5:
                room.skor.append([0,0])
                room.checkService()
                print(room.skor)
                break
            elif hex(event.value) == IRKEY_PRDOWN:
                room.reset()
                room.checkService()
                break
            elif hex(event.value) == IRKEY_NUM0:
                room.changeCourt()
                print(room.skor)
                break
        #     print("\nCode:",hex(event.value))
        #     print("---------------")
            pass
                 
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
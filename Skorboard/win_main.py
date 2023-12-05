# import the pygame module, so you can use it
from Game import *
# import evdev
# dev = evdev.InputDevice('/dev/input/event3')
import sys 
try:
    SPORT = sys.argv[1]
except:
    SPORT = "TT"
try:
    CHGSERV = int(sys.argv[2])
except:
    CHGSERV = 2

# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Score Board")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGTH))
     
    # define a variable to control the main loop
    running = True
    
    room = Game(SPORT, CHGSERV)

    start_time = pygame.time.get_ticks()
    time_hms = 0, 0
    timer_font = pygame.font.SysFont("freesansbold", 38)
    timer_surf = timer_font.render(str(time_hms[0]//10) + str(time_hms[0]%10) + ":" + str(time_hms[1]//10) + str(time_hms[1]%10), True, (255, 255, 255))

    # main loop
    while running:
        room.updateScreen(screen)

        time_ms = pygame.time.get_ticks() - start_time
        new_hms = (time_ms//(1000*60)), (time_ms//1000)%60
        if new_hms != time_hms:
            time_hms = new_hms
            timer_surf = timer_font.render(str(time_hms[0]//10) + str(time_hms[0]%10) + ":" + str(time_hms[1]//10) + str(time_hms[1]%10), True, (255, 255, 255))
        screen.blit(timer_surf, (1280, 4))

        pygame.display.flip()
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
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_w):
                room.skor[len(room.skor)-1][TEAM_LEFT] += 1
                if room.sport == "TT":
                    room.checkService()
                else:
                    room.checkService(0)
                pass
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_i):
                room.skor[len(room.skor)-1][TEAM_RIGHT] += 1
                if room.sport == "TT":
                    room.checkService()
                else:
                    room.checkService(-1)
                pass
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_s):
                room.skor[len(room.skor)-1][TEAM_LEFT] -= 1
                # room.checkService()
                pass
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_k):
                room.skor[len(room.skor)-1][TEAM_RIGHT] -= 1
                # room.checkService()
                pass
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
                room.skor.append([0,0])
                room.checkService()
                print(room.skor)
                pass
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_n):
                room.reset()
                start_time = pygame.time.get_ticks()
                room.checkService()
                pass
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_t):
                room.changeCourt()
                print(room.skor)
                pass
            # if event.type == pygame.KEYDOWN:
            #     print(room.skor)
            #     print(event.key)     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()

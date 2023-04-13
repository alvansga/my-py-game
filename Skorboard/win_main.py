# import the pygame module, so you can use it
import pygame
# import evdev
# dev = evdev.InputDevice('/dev/input/event3')

# CUSTOMIZATION
CHGSERVAFTER = 2 # 2 or 5
WIN_WIDTH = 640
WIN_HEIGTH = 480
L_COLOR = [40,40,40]#[180,0,0]
R_COLOR = [255,255,255]#[0,0,180]
CIRCLE_COLOR = [255,255,255]
# -------------

IRKEY_EXIT = "0x804b"
IRKEY_MENU = "0x800b"

IRKEY_UP = "0x800c"
IRKEY_DOWN = "0x800d"
IRKEY_RIGHT = "0x800e"
IRKEY_LEFT = "0x800f"

TEAM_LEFT , TEAM_RIGHT = 0 , 1

class Game():
    def __init__(self):
        self.serv = 0
        self.skor = [[0,0]]

    def reset(self):
        self.serv = 0
        self.skor = [[0,0]]

def checkService(game):
    if sum(game.skor[len(game.skor)-1]) % CHGSERVAFTER == 0:
        game.serv = ~game.serv #toggle

def updateScreen(screen, game):
    pygame.draw.rect(screen, L_COLOR, pygame.Rect(0, 0, WIN_WIDTH//2, WIN_HEIGTH))
    pygame.draw.rect(screen, R_COLOR, pygame.Rect(WIN_WIDTH//2, 0, WIN_WIDTH//2, WIN_HEIGTH))

    top = pygame.Surface((WIN_WIDTH, WIN_HEIGTH//12))
    top.set_alpha(128)
    top.fill((0,0,0))
    screen.blit(top,(0,0))

    font = pygame.font.Font('freesansbold.ttf', int(WIN_HEIGTH/1.5))
    if sum(L_COLOR) < 150:
        txt_color = (255,255,255)
    else:
        txt_color = (0,0,0)
    text = font.render(str(game.skor[len(game.skor)-1][TEAM_LEFT]), True, txt_color)
    textRect = text.get_rect()
    textRect.center = (WIN_WIDTH//2//2, WIN_HEIGTH//12 + WIN_HEIGTH//2)
    screen.blit(text, textRect)

    if sum(R_COLOR) < 180:
        txt_color = (255,255,255)
    else:
        txt_color = (0,0,0)
    text = font.render(str(game.skor[len(game.skor)-1][TEAM_RIGHT]), True, txt_color)
    textRect = text.get_rect()
    textRect.center = ((WIN_WIDTH//2) + WIN_WIDTH//2//2, WIN_HEIGTH//12 + WIN_HEIGTH//2)
    screen.blit(text, textRect)

    if game.serv == 0:
        pygame.draw.circle(screen, CIRCLE_COLOR, (WIN_WIDTH//2 - WIN_HEIGTH//24, WIN_HEIGTH//12//2 ), WIN_HEIGTH//32)
    elif game.serv == -1:
        pygame.draw.circle(screen, CIRCLE_COLOR, (WIN_WIDTH//2 + WIN_HEIGTH//24, WIN_HEIGTH//12//2 ), WIN_HEIGTH//32)

    pygame.display.flip()

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
    
    room = Game()

    # main loop
    while running:
        updateScreen(screen, room)
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
                updateScreen(screen, room)
                pass
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
                # screen.fill((128,0,128))
                room.serv = 0
                updateScreen(screen, room)
                pass
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_1):
                # screen.fill((128,0,0))
                room.skor[len(room.skor)-1][TEAM_LEFT] += 1
                checkService(room)
                updateScreen(screen, room)
                pass
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_3):
                # screen.fill((128,0,0))
                room.skor[len(room.skor)-1][TEAM_RIGHT] += 1
                checkService(room)
                updateScreen(screen, room)
                pass
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_7):
                # screen.fill((128,0,0))
                room.skor[len(room.skor)-1][TEAM_LEFT] -= 1
                checkService(room)
                updateScreen(screen, room)
                pass
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_9):
                # screen.fill((128,0,0))
                room.skor[len(room.skor)-1][TEAM_RIGHT] -= 1
                checkService(room)
                updateScreen(screen, room)
                pass
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_5):
                # screen.fill((128,0,0))
                room.skor.append([0,0])
                checkService(room)
                updateScreen(screen, room)
                pass
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_r):
                # screen.fill((128,0,0))
                room.reset()
                checkService(room)
                updateScreen(screen, room)
                pass
            # if event.type == pygame.KEYDOWN:
            #     print(room.skor)
            #     print(event.key)

        # for event in dev.read_loop():
        # #	print(evdev.categorize(event))
        #     if hex(event.value) == "0x0":
        #         continue
        #     # elif hex(event.value) == IRKEY_EXIT:
        #     #     running = False
        #     #     print("exiting...")
        #     #     break
        #     elif hex(event.value) == IRKEY_MENU:
        #         # screen.fill((0,0,0))
        #         pass
        #     elif hex(event.value) == IRKEY_UP:
        #         # screen.fill((128,0,0))
        #         pass
        #     elif hex(event.value) == IRKEY_DOWN:
        #         # screen.fill((0,128,0))
        #         pass
        #     elif hex(event.value) == IRKEY_RIGHT:
        #         # screen.fill((0,0,128))
        #         serv = 1
        #         updateScreen(screen, serv)
        #         pass
        #     elif hex(event.value) == IRKEY_LEFT:
        #         # screen.fill((128,0,128))
        #         serv = 0
        #         updateScreen(screen, serv)
        #         pass
            
        #     print("\nCode:",hex(event.value))
        #     print("---------------")
        #     pass
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()

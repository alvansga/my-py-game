import pygame,sys,random
from pygame.locals import *


FPS = 60
LEBARWINDOW = 480
TINGGIWINDOW = 480

# XMARGIN = int((LEBARWINDOW - (LEBARPAPAN * (UKURANMARBLE + UKURANCELAH))) / 2)
# YMARGIN = int((TINGGIWINDOW - (TINGGIPAPAN * (UKURANMARBLE + UKURANCELAH))) / 2)

def startAnimation():
    print("Space")
    awal = 240
    while True:
        DISPLAYSURF.fill((0,0,0))
        pygame.draw.circle(DISPLAYSURF,(255,180,0),(240,awal),30)
        awal += 10
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        if awal >= 480-30:
            DISPLAYSURF.fill((0,0,0))
            break




def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((LEBARWINDOW,TINGGIWINDOW))
    pygame.display.set_caption('animation')
    start = 0
    while True:
        pygame.draw.circle(DISPLAYSURF,(255,180,0),(240,240),30)
        # DISPLAYSURF.blit()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP and event.key == K_SPACE:
                start = 1
                startAnimation()

        if start == 1:
            pass

        pygame.display.update()
        FPSCLOCK.tick(FPS)



if __name__ == '__main__':
    main()
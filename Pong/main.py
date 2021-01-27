# BIGPROJECT4
# marble
# by ejra
# inspired by childhood games
# start date 26 mei 2020
# finish date 26 juni 2020

import pygame,sys,random
from pygame.locals import *
from ball import *
FPS = 60
LEBARWINDOW = 320
TINGGIWINDOW = 480

UKURANMARBLE = 36
JARI2MARBLE = int (UKURANMARBLE* 0.5)
UKURANCELAH = 10

LEBARPAPAN = 7
TINGGIPAPAN = 7

#############
MAXLEVEL = 7
#############

#ukuran margin
XMARGIN = int((LEBARWINDOW - (LEBARPAPAN * (UKURANMARBLE + UKURANCELAH))) / 2)
YMARGIN = int((TINGGIWINDOW - (TINGGIPAPAN * (UKURANMARBLE + UKURANCELAH))) / 2)

# warna yang dibutuhkan
#               R   G   B
PUTIH       = (255,255,255)
JINGGA      = (255,180,  0)
JINGGATUA   = (150, 75,  0)
UNGU        = (200, 10,255)
LIMEHIJAU   = (150,255,  0)
BIRU        = (170,100,255)
BIRUTUA     = (100,  0,150)
MERAH       = (255,  0,  0)
KUNING      = (255,255,  0)
HITAM       = (  0,  0,  0)
ABU2        = ( 10, 10, 10)
ABU2_1      = ( 20, 20, 20)

#dark theme
# BGCOLOR1 = HITAM
# BGCOLOR2 = ABU2

# MARBLECOLOR = ABU2_1
# MARBLECOLOR2 = HITAM
# RINGCOLOR = ABU2
# BOARDCOLOR = HITAM
# BOARDCOLOR2 = ABU2
# WINTEKSCOLOR = PUTIH

#original
BGCOLOR1 = BIRU
BGCOLOR2 = LIMEHIJAU

MARBLECOLOR = JINGGA
MARBLECOLOR2 = JINGGATUA
RINGCOLOR = PUTIH
BOARDCOLOR = BIRU
BOARDCOLOR2 = BIRUTUA
WINTEKSCOLOR = PUTIH


# gambar objek
MARBLE = 'marble'
CURMARBLE = 'curmarble'
RING = 'ring'

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((LEBARWINDOW,TINGGIWINDOW))
    DISPLAYSURF.fill(BGCOLOR1)
    pygame.display.set_caption('Pong')
    # player = pygame.image.load("media/marble.png")
    # DISPLAYSURF.blit(player,(0,0))
    bola = Ball(DISPLAYSURF,int(LEBARWINDOW/2),int(TINGGIWINDOW/2))
    xmouse = 0
    ymouse = 0
    prevselect = (None,None)
    mousehold = False
    win = False

    while True:
        DISPLAYSURF.fill(BGCOLOR1)
        bola.StartMoving(DISPLAYSURF)
        bola.CollideCheck(LEBARWINDOW,TINGGIWINDOW)
        mouseklik = False
        mouserelease = False

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and (event.key == K_ESCAPE or event.key == K_q)):
                pygame.quit()
                sys.exit()
            
            elif event.type == MOUSEMOTION and mousehold == True:
                print ("mouse hold")
                xmouse, ymouse = event.pos
            
            elif event.type == MOUSEBUTTONUP:
                print ("mouse lepas")
                xmouse, ymouse = event.pos
                mousehold = False
                mouserelease = True

            elif event.type == MOUSEBUTTONDOWN:
                xmouse, ymouse = event.pos
                mouseklik = True
                print("mouse tekan")

            elif event.type == MOUSEMOTION:
                xmouse, ymouse = event.pos

        
        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
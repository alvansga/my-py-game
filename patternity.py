# BIGPROJECT5
# patternity
# by ejra
# start date 10 juni 2020
# finish date 10 juli 2020

import pygame,sys,random
from pygame.locals import *

FPS = 60
WIDTHWINDOW = 360
HEIGHTWINDOW = 360

LAMPSIZE = 36
LAMPRADIUS = int (LAMPSIZE * 0.5)
GAPSIZE = 10

WIDTHBOARD = 5
HEIGHTBOARD = 5

#ukuran margin
XMARGIN = int((WIDTHWINDOW - (WIDTHBOARD * (LAMPSIZE + GAPSIZE))) / 2)
YMARGIN = int((HEIGHTWINDOW - (HEIGHTBOARD * (LAMPSIZE + GAPSIZE))) / 2)

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

# gradasi nyala LAMPU
GRADMERAH1   = (240, 65, 240)
GRADMERAH2   = (240, 65, 200)
GRADMERAH3   = (240, 65, 160)
GRADMERAH4   = (240, 65, 120)
GRADMERAH5   = (240, 65,  80)
GRADBIRU1    = (200, 65,  240)
GRADBIRU2    = (160, 65,  240)
GRADBIRU3    = (120, 65,  240)
GRADBIRU4    = (80, 65,  240)
GRADBIRU5    = (40, 65,  240)
GRADHIJAU1    = (65, 240,  240)
GRADHIJAU2    = (65, 200,  240)
GRADHIJAU3    = (65, 160,  240)
GRADHIJAU4    = (65, 120,  240)
GRADHIJAU5    = (65, 80,  240)
GRADTOSCA1    = (65, 240,  200)
GRADTOSCA2    = (65, 240,  160)
GRADTOSCA3    = (65, 240,  120)
GRADTOSCA4    = (65, 240,  80)
GRADTOSCA5    = (65, 240,  40)
GRADKUNING1   = (240,240, 65)
GRADKUNING2   = (240,200, 65)
GRADKUNING3   = (240,160, 65)
GRADKUNING4   = (240,120, 65)
GRADKUNING5   = (240,80, 65)

urutanwarna = [[GRADMERAH1,GRADMERAH2,GRADMERAH3,GRADMERAH4,GRADMERAH5],
               [GRADBIRU1,GRADBIRU2,GRADBIRU3,GRADBIRU4,GRADBIRU5],
               [GRADHIJAU1,GRADHIJAU2,GRADHIJAU3,GRADHIJAU4,GRADHIJAU5],
               [GRADTOSCA1,GRADTOSCA2,GRADTOSCA3,GRADTOSCA4,GRADTOSCA5],
               [GRADKUNING1,GRADKUNING2,GRADKUNING3,GRADKUNING4,GRADKUNING5]]

NYALA,MATI = 1,0

#original
BGCOLOR1 = HITAM

# gambar objek
LAMP = 'lamp'
RING = 'ring'

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WIDTHWINDOW,HEIGHTWINDOW))
    pygame.display.set_caption('Patternity')
    
    animasimulai()
    pygame.time.wait(500)
    xmouse = 0
    ymouse = 0
    prevselect = (None,None)
    mousehold = False
    win = False
    
    while True:
        mouseklik = False
        mouserelease = False
        # refreshlampu()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
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

def lefttopkoordinatbox(boxx,boxy):
    left = boxx * (LAMPSIZE + GAPSIZE) + XMARGIN
    top = boxy * (LAMPSIZE + GAPSIZE) + YMARGIN
    return (left,top)

def buatlampu(nyala,boxx,boxy):
    left,top = lefttopkoordinatbox(boxx,boxy)
    if nyala == 1:
        pygame.draw.circle(DISPLAYSURF,urutanwarna[boxx][boxy],(left+LAMPRADIUS+2,top+LAMPRADIUS+2),LAMPRADIUS)
        # pygame.draw.circle(DISPLAYSURF,LINE12,(left+LAMPRADIUS,top+LAMPRADIUS),LAMPRADIUS)
    else:
        pygame.draw.circle(DISPLAYSURF,ABU2_1,(left+LAMPRADIUS+2,top+LAMPRADIUS+2),LAMPRADIUS)
        # pygame.draw.circle(DISPLAYSURF,ABU2_1,(left+LAMPRADIUS,top+LAMPRADIUS),LAMPRADIUS)

def refreshlampu():
    for i in range(WIDTHBOARD):
        for j in range(HEIGHTBOARD):
            buatlampu(MATI,i,j)

def animasimulai():
    for i in range(WIDTHBOARD):
        for j in range(HEIGHTBOARD):
            buatlampu(NYALA,j,i)
            pygame.display.update()
            pygame.time.wait(50)


if __name__ == '__main__':
    main()
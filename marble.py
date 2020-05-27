# BIGPROJECT4
# marble
# by ejra
# inspired by childhood games
# start date 26 mei 2020
# finish date 26 juni 2020

import pygame,sys
from pygame.locals import *

FPS = 60
LEBARWINDOW = 480
TINGGIWINDOW = 480
LAJUPINDAH = 10
UKURANMARBLE = 36
JARI2MARBLE = int (UKURANMARBLE* 0.5)
UKURANCELAH = 10
LEBARPAPAN = 7
TINGGIPAPAN = 1

#ukuran margin
XMARGIN = int((LEBARWINDOW - (LEBARPAPAN * (UKURANMARBLE + UKURANCELAH))) / 2)
YMARGIN = int((TINGGIWINDOW - (TINGGIPAPAN * (UKURANMARBLE + UKURANCELAH))) / 2)

# warna yang dibutuhkan
#               R   G   B
PUTIH       = (255,255,255)
JINGGA      = (255,180,  0)
JINGGATUA   = (150, 75,  0)
UNGU        = (200, 10,255)
KUNING      = (255,230,  0)
BIRU        = (170,100,255)
BIRUTUA     = (100,  0,150)

REAL,SHADOW = 0,1

BGCOLOR = UNGU
MARBLECOLOR = JINGGA
MARBLECOLOR2 = JINGGATUA
RINGCOLOR = PUTIH
SHADOWCOLOR = KUNING
BOARDCOLOR = BIRU
BOARDCOLOR2 = BIRUTUA


MARBLE = 'marble'
SHMARBLE = 'shmarble'
RING = 'ring'


def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((LEBARWINDOW,TINGGIWINDOW))
    pygame.display.set_caption('Marbles')
    DISPLAYSURF.fill(BGCOLOR)
    gambarBG()
    xmouse = 0
    ymouse = 0
    prevselect = (None,None)
    marbles = []
    mousehold = False
    mouserelease = False
    for i in range(LEBARPAPAN):
        marbles.append([False] * TINGGIPAPAN)
    
    #level 1
    marbles[int(LEBARPAPAN/2)-2][int(TINGGIPAPAN/2)] = True
    marbles[int(LEBARPAPAN/2)-1][int(TINGGIPAPAN/2)] = True
    marbles[int(LEBARPAPAN/2)+1][int(TINGGIPAPAN/2)] = True

    while True:
        mouseklik = False
        DISPLAYSURF.fill(BGCOLOR)
        gambarBG()
        # tampil semua marble ########
        # for i in range(LEBARPAPAN):
        #     for j in range(TINGGIPAPAN):
        #         gambarMarble(MARBLE,REAL,i,j)
        ########################
        refreshMarble(marbles)
        
        # if prevselect != None and not mousehold == True:
        #     left,top = prevselect

        
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
                print (marbles)

            elif event.type == MOUSEBUTTONDOWN:
                xmouse, ymouse = event.pos
                mouseklik = True
                print("mouse tekan")

            elif event.type == MOUSEMOTION:
                xmouse, ymouse = event.pos
                
        # CURSOR MARBLE
        if mousehold == True:
            xmouse, ymouse = pygame.mouse.get_pos()
            gambarfreeMarble(MARBLE,REAL,xmouse,ymouse,marbles)
        else:
            boxx,boxy = sentuhMarble(xmouse,ymouse)
            if mouserelease == True:
                mouserelease = False
                cekmarblerelease(boxx,boxy,prevselect,marbles)
                # kembalikan marble
                

            
            if boxx != None and boxy != None:
                # print("tersentuh")
                if marbles[boxx][boxy]:
                    gambarRing(boxx,boxy)
                if marbles[boxx][boxy] and mouseklik == True:
                    mousehold = True
                    prevselect = (boxx,boxy)
                    marbles[boxx][boxy] = False 

        
                


        pygame.display.update()
        FPSCLOCK.tick(FPS)

def lefttopkoordinatbox(boxx,boxy):
    left = boxx * (UKURANMARBLE + UKURANCELAH) + XMARGIN
    top = boxy * (UKURANMARBLE + UKURANCELAH) + YMARGIN
    return (left,top)

def gambarBG():
    for i in range(LEBARPAPAN):
        for j in range(TINGGIPAPAN):
            gambarWadah2(i,j)
    for i in range(LEBARPAPAN):
        for j in range(TINGGIPAPAN):
            gambarWadah(i,j)

def gambarWadah2(boxx,boxy):
    left,top = lefttopkoordinatbox(boxx,boxy)
    pygame.draw.circle(DISPLAYSURF,BOARDCOLOR2,(left+JARI2MARBLE+3,top+JARI2MARBLE+3),JARI2MARBLE+15)

def gambarWadah(boxx,boxy):
    left,top = lefttopkoordinatbox(boxx,boxy)
    pygame.draw.circle(DISPLAYSURF,BOARDCOLOR,(left+JARI2MARBLE,top+JARI2MARBLE),JARI2MARBLE+10)
    # pygame.draw.circle(DISPLAYSURF,BOARDCOLOR2,(left+JARI2MARBLE,top+JARI2MARBLE),JARI2MARBLE-3)

def gambarMarble(bentuk,asli,boxx,boxy):
    left,top = lefttopkoordinatbox(boxx,boxy)
    if asli == REAL:
        pygame.draw.circle(DISPLAYSURF,MARBLECOLOR2,(left+JARI2MARBLE+2,top+JARI2MARBLE+2),JARI2MARBLE)
        pygame.draw.circle(DISPLAYSURF,MARBLECOLOR,(left+JARI2MARBLE,top+JARI2MARBLE),JARI2MARBLE)
    elif asli == SHADOW:
        pygame.draw.circle(DISPLAYSURF,SHADOWCOLOR,(left+JARI2MARBLE,top+JARI2MARBLE),JARI2MARBLE)

def gambarfreeMarble(bentuk,asli,left,top,marblelist):
    if asli == REAL:
        pygame.draw.circle(DISPLAYSURF,MARBLECOLOR2,(left+2,top+2),JARI2MARBLE)
        pygame.draw.circle(DISPLAYSURF,MARBLECOLOR,(left,top),JARI2MARBLE)
        # marblelist[boxx][boxy] = True
    elif asli == SHADOW:
        pygame.draw.circle(DISPLAYSURF,SHADOWCOLOR,(left+JARI2MARBLE,top+JARI2MARBLE),JARI2MARBLE)


def gambarRing(boxx,boxy):
    left,top = lefttopkoordinatbox(boxx,boxy)
    pygame.draw.circle(DISPLAYSURF,RINGCOLOR,(left+JARI2MARBLE,top+JARI2MARBLE),JARI2MARBLE+3,3)

def sentuhMarble(x,y):
    for boxx in range(LEBARPAPAN):
        for boxy in range(TINGGIPAPAN):
            left, top = lefttopkoordinatbox(boxx,boxy)
            boxrect = pygame.Rect(left,top,UKURANMARBLE,UKURANMARBLE)
            if boxrect.collidepoint(x,y):
                return (boxx,boxy)
    return (None,None)

def refreshMarble(marbles):
    for i in range(LEBARPAPAN):
        for j in range(TINGGIPAPAN):
            if marbles[i][j] == True:
                gambarMarble(MARBLE,REAL,i,j)

def cekmarblerelease(boxx,boxy,prevselect,marbles):
    oldboxx,oldboxy = prevselect
    #               kanan                                           
    
    
    if boxx == None and boxy == None :
        boxx,boxy = prevselect
        marbles[boxx][boxy] = True 
    if marbles[boxx][boxy] == True :
        boxx,boxy = prevselect
        marbles[boxx][boxy] = True 
    else:
        if (boxx == oldboxx + 1 + 1 and boxy == oldboxy and marbles[oldboxx + 1][oldboxy] == True) :
            marbles[boxx][boxy] = True
            marbles[oldboxx + 1][oldboxy] = False
            marbles[oldboxx + 1 + 1][oldboxy] = False
        #               left
        elif (boxx == oldboxx - 1 - 1 and boxy == oldboxy and marbles[oldboxx - 1][oldboxy] == True):
            marbles[boxx][boxy] = True
            marbles[oldboxx - 1][oldboxy] = False
            marbles[oldboxx - 1 - 1][oldboxy] = False
        else:
            boxx,boxy = prevselect
            marbles[boxx][boxy] = True 
    return marbles

if __name__ == '__main__':
    main()
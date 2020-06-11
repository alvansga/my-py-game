# BIGPROJECT5
# light it up
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


def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WIDTHWINDOW,HEIGHTWINDOW))
    pygame.display.set_caption('Light It Up')
    
    # animasimulai()
    # pygame.time.wait(1000)
    
    # #level 1
    lamp = initlampu()
    refreshlampu(lamp)
    pygame.display.update()
    pygame.time.wait(1000)

    #TINGKAT KESULITAN#
    level = 1 # 1~6
    LVLMAX = 6
    kesulitan = [(3,1000),(4,900),(5,800),(6,700),(7,600),(8,500)]

    num,waktu = kesulitan[level-1]
    ###################
    jumlahlamp = []
    for i in range(num):
        jumlahlamp.append((0,0))
    jumlahlamp=animasilevel(jumlahlamp,waktu)

    pointerjumlahlamp = 0

    xmouse = 0
    ymouse = 0
    mousehold = False
    win = False
    
    while True:
        mouseklik = False
        mouserelease = False
        refreshlampu(lamp)
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

        boxx,boxy = sentuhLampMati(xmouse,ymouse)
        if win == True:
            win = False
            lamp = initlampu()
            animasimulai()
            animasimati()
            pygame.time.wait(1000)

            #TINGKAT KESULITAN#
            level += 1
            if level > LVLMAX:
                level = 1
            num,waktu = kesulitan[level-1]
            ###################
            jumlahlamp = []
            for i in range(num):
                jumlahlamp.append((0,0))
            jumlahlamp=animasilevel(jumlahlamp,waktu)

            pointerjumlahlamp = 0
            # pygame.quit()
            # sys.exit()
        else:
            if boxx != None and boxy != None:
                if lamp[boxx][boxy] != True:
                    buatcincin(boxx,boxy)
                    if mouserelease == True:
                        if boxx == jumlahlamp[pointerjumlahlamp][0] and boxy == jumlahlamp[pointerjumlahlamp][1]:
                            lamp[boxx][boxy] = True
                            pointerjumlahlamp += 1
                            if pointerjumlahlamp == len(jumlahlamp):
                                win = True
                                print("menang")
                        else:
                            lamp = initlampu()
                            pointerjumlahlamp = 0

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def lefttopkoordinatbox(boxx,boxy):
    left = boxx * (LAMPSIZE + GAPSIZE) + XMARGIN
    top = boxy * (LAMPSIZE + GAPSIZE) + YMARGIN
    return (left,top)

def buatlampu(nyala,boxx,boxy):
    left,top = lefttopkoordinatbox(boxx,boxy)
    if nyala == 1:
        # pygame.draw.circle(DISPLAYSURF,urutanwarna[boxx][boxy],(left+LAMPRADIUS+2,top+LAMPRADIUS+2),LAMPRADIUS)
        pygame.draw.circle(DISPLAYSURF,urutanwarna[boxx][boxy],(left+LAMPRADIUS,top+LAMPRADIUS),LAMPRADIUS)
    else:
        # pygame.draw.circle(DISPLAYSURF,ABU2_1,(left+LAMPRADIUS+2,top+LAMPRADIUS+2),LAMPRADIUS)
        pygame.draw.circle(DISPLAYSURF,ABU2_1,(left+LAMPRADIUS,top+LAMPRADIUS),LAMPRADIUS)

def buatcincin(boxx,boxy):
    left,top = lefttopkoordinatbox(boxx,boxy)
    pygame.draw.circle(DISPLAYSURF,PUTIH,(left+LAMPRADIUS,top+LAMPRADIUS),LAMPRADIUS+2,3)

def sentuhLampMati(x,y):
    for boxx in range(WIDTHBOARD):
        for boxy in range(HEIGHTBOARD):
            left, top = lefttopkoordinatbox(boxx,boxy)
            boxrect = pygame.Rect(left,top,LAMPSIZE,LAMPSIZE)
            if boxrect.collidepoint(x,y):
                return (boxx,boxy)
    return (None,None)

def initlampu():
    lamp = []
    for i in range(WIDTHBOARD):
        lamp.append([False] * HEIGHTBOARD)
    return lamp

def refreshlampu(lamp):
    DISPLAYSURF.fill(BGCOLOR1)
    for i in range(WIDTHBOARD):
        for j in range(HEIGHTBOARD):
            if lamp[i][j] == False:
                buatlampu(MATI,i,j)
            else:
                buatlampu(NYALA,i,j)
    
def animasimulai():
    for i in range(WIDTHBOARD):
        for j in range(HEIGHTBOARD):
            buatlampu(NYALA,j,i)
            pygame.display.update()
            pygame.time.wait(50)

def animasimati():
    for i in range(WIDTHBOARD):
        for j in range(HEIGHTBOARD):
            buatlampu(MATI,j,i)
            pygame.display.update()
            pygame.time.wait(50)

def animasilevel(jumlahlamplist,waktu):
    lamp = initlampu()
    jumlahlamplist = shufflejumlahlamplist(jumlahlamplist)
    for count in range(len(jumlahlamplist)):
        refreshlampu(lamp)
        pygame.display.update()
        pygame.time.wait(100)

        kolom,baris = jumlahlamplist[count]
        buatlampu(NYALA,kolom,baris)
        pygame.display.update()
        pygame.time.wait(waktu)
    return jumlahlamplist

def shufflejumlahlamplist(jumlahlamplist):
    count = 0
    while True:
        kolom = random.choice(range(WIDTHBOARD))
        baris = random.choice(range(HEIGHTBOARD))
        if (kolom,baris) in jumlahlamplist:
            continue
        jumlahlamplist[count] = (kolom,baris)
        count += 1
        if count == len(jumlahlamplist):
            break
    return jumlahlamplist
        
if __name__ == '__main__':
    main()
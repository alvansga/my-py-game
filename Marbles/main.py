# BIGPROJECT4
# marble
# by ejra
# inspired by childhood games
# start date 26 mei 2020
# finish date 26 juni 2020

import pygame,sys,random
from pygame.locals import *

FPS = 60
LEBARWINDOW = 480
TINGGIWINDOW = 480

if (LEBARWINDOW == TINGGIWINDOW and LEBARWINDOW == 480):
    SCALE = 1
# else if (LEBARWINDOW == TINGGIWINDOW and LEBARWINDOW > 480):
#     SCALE = int(LEBARWINDOW)

UKURANMARBLE = int(36*SCALE)
JARI2MARBLE = int (UKURANMARBLE* 0.5)
UKURANCELAH = int(10*SCALE)

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
BGCOLOR1 = UNGU
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
    global FPSCLOCK, DISPLAYSURF, LEBARWINDOW,TINGGIWINDOW, UKURANCELAH,UKURANMARBLE,JARI2MARBLE, XMARGIN, YMARGIN, SCALE
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((LEBARWINDOW,TINGGIWINDOW),RESIZABLE)
    pygame.display.set_caption('Marbles')

    xmouse = 0
    ymouse = 0
    prevselect = (None,None)
    mousehold = False
    win = False
    congratsteks = ['Fantastic!','Magnificent!','Amazing!','Well Played!','Awesome!','Good Game!','Well Done!']
    randomcongrats = ''

    #set level
    #set marble tabel LEBARPAPAN x TINGGIPAPAN
    # levellist = [1,2,3,4,5]
    level = 1
    marbles = setLevel(level)

    while True:
        

        mouseklik = False
        mouserelease = False
        gambarBG(level)
        refreshMarble(marbles)
        
        
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

            elif event.type == VIDEORESIZE:
                screen = pygame.display.set_mode(
                    event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
                pic = pygame.image.load("resource/marbles.png")
                screen.blit(pygame.transform.scale(pic, event.dict['size']), (0, 0))
                (LEBARWINDOW, TINGGIWINDOW) = event.dict['size']
                
                if (LEBARWINDOW == TINGGIWINDOW and LEBARWINDOW == 480):
                    SCALE = 1
                elif (LEBARWINDOW > TINGGIWINDOW and LEBARWINDOW != 480 and TINGGIWINDOW != 480):
                    SCALE = float(TINGGIWINDOW/480)
                else:
                    SCALE = float(LEBARWINDOW/480)
                print("SCALE:",SCALE,"LEBARWINDOW:",LEBARWINDOW,"TINGGIWINDOW:",TINGGIWINDOW)

                UKURANMARBLE = int(36*SCALE)
                JARI2MARBLE = int (UKURANMARBLE* 0.5)
                UKURANCELAH = int(10*SCALE)

                                #ukuran margin
                XMARGIN = int((LEBARWINDOW - (LEBARPAPAN * (UKURANMARBLE + UKURANCELAH))) / 2)
                YMARGIN = int((TINGGIWINDOW - (TINGGIPAPAN * (UKURANMARBLE + UKURANCELAH))) / 2)
                pygame.display.flip()

        tampillevel(level)
        tampilauthor()
        if tampilReset(xmouse,ymouse,mouseklik) == True:
            #set level
            marbles = setLevel(level)
            win = False
        if tampilNewLevel(xmouse,ymouse,mouseklik) == True:
            #set level
            level += 1
            if level > MAXLEVEL:
                level = 1
            marbles = setLevel(level)
            win = False

        if win == True:
            wincelebration(randomcongrats)
        else:
            if mousehold == True:
                xmouse, ymouse = pygame.mouse.get_pos()
                gambarObjek(CURMARBLE,xmouse,ymouse)
            else:
                boxx,boxy = sentuhMarble(xmouse,ymouse)
                if mouserelease == True:
                    mouserelease = False
                    marbles = cekmarblerelease(boxx,boxy,prevselect,marbles)
                    if marbles != None:
                        if hitungmarbles(marbles) == 1:
                            win = True
                            print('menang')
                            randomcongrats = random.choice(congratsteks)
                        prevselect = (None,None)
                    
                if boxx != None and boxy != None:
                    if marbles[boxx][boxy]:
                        gambarObjek(RING,boxx,boxy)
                    if marbles[boxx][boxy] and mouseklik == True:
                        mousehold = True
                        prevselect = (boxx,boxy)
                        marbles[boxx][boxy] = False 

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def lefttopkoordinatbox(boxx,boxy):
    global UKURANCELAH,UKURANMARBLE,JARI2MARBLE, XMARGIN, YMARGIN
    left = boxx * (UKURANMARBLE + UKURANCELAH) + XMARGIN
    top = boxy * (UKURANMARBLE + UKURANCELAH) + YMARGIN
    return (left,top)

def gambarWadah2(boxx,boxy):
    global UKURANCELAH,UKURANMARBLE,JARI2MARBLE
    left,top = lefttopkoordinatbox(boxx,boxy)
    pygame.draw.circle(DISPLAYSURF,BOARDCOLOR2,(left+JARI2MARBLE+3,top+JARI2MARBLE+3),JARI2MARBLE+15)

def gambarWadah(boxx,boxy):
    global UKURANCELAH,UKURANMARBLE,JARI2MARBLE
    left,top = lefttopkoordinatbox(boxx,boxy)
    pygame.draw.circle(DISPLAYSURF,BOARDCOLOR,(left+JARI2MARBLE,top+JARI2MARBLE),JARI2MARBLE+10)

def gambarObjek(bentuk,boxx,boxy):
    global UKURANCELAH,UKURANMARBLE,JARI2MARBLE
    left,top = lefttopkoordinatbox(boxx,boxy)
    if bentuk == MARBLE:
        marble = pygame.image.load("resource/marbles.png")
        DISPLAYSURF.blit(pygame.transform.scale(marble,(int(JARI2MARBLE*2),int(JARI2MARBLE*2))),(left,top))
        # pygame.draw.circle(DISPLAYSURF,MARBLECOLOR2,(left+JARI2MARBLE+2,top+JARI2MARBLE+2),JARI2MARBLE)
        # pygame.draw.circle(DISPLAYSURF,MARBLECOLOR,(left+JARI2MARBLE,top+JARI2MARBLE),JARI2MARBLE)
    elif bentuk == RING:
        pygame.draw.circle(DISPLAYSURF,RINGCOLOR,(left+JARI2MARBLE,top+JARI2MARBLE),JARI2MARBLE+3,3)
    elif bentuk == CURMARBLE:
        marble = pygame.image.load("resource/marbles.png")
        DISPLAYSURF.blit(pygame.transform.scale(marble,(int(JARI2MARBLE*2),int(JARI2MARBLE*2))),(boxx-17,boxy-17))
        # pygame.draw.circle(DISPLAYSURF,MARBLECOLOR2,(boxx+2,boxy+2),JARI2MARBLE)
        # pygame.draw.circle(DISPLAYSURF,MARBLECOLOR,(boxx,boxy),JARI2MARBLE)

def sentuhMarble(x,y):
    global UKURANCELAH,UKURANMARBLE,JARI2MARBLE
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
                gambarObjek(MARBLE,i,j)

def cekmarblerelease(boxx,boxy,prevselect,marbles):
    if prevselect == (None,None):
        return marbles
    oldboxx,oldboxy = prevselect                               
    if boxx == None and boxy == None :
        boxx,boxy = prevselect
        marbles[boxx][boxy] = True 
    if marbles[boxx][boxy] == True :
        boxx,boxy = prevselect
        marbles[boxx][boxy] = True 
    else:
        #               kanan            
        if (boxx == oldboxx + 2 and boxy == oldboxy and marbles[oldboxx + 1][oldboxy] == True) :
            marbles[boxx][boxy] = True
            marbles[oldboxx + 1][oldboxy] = False
        #               kiri
        elif (boxx == oldboxx - 2 and boxy == oldboxy and marbles[oldboxx - 1][oldboxy] == True):
            marbles[boxx][boxy] = True
            marbles[oldboxx - 1][oldboxy] = False
        #               atas
        elif (boxx == oldboxx  and boxy == oldboxy + 2 and marbles[oldboxx][oldboxy  + 1] == True):
            marbles[boxx][boxy] = True
            marbles[oldboxx][oldboxy + 1] = False
        #               bawah
        elif (boxx == oldboxx  and boxy == oldboxy - 2 and marbles[oldboxx][oldboxy  - 1] == True):
            marbles[boxx][boxy] = True
            marbles[oldboxx][oldboxy - 1] = False
        else:
            boxx,boxy = prevselect
            marbles[boxx][boxy] = True 
    return marbles

def hitungmarbles(marbles):
    jum = 0
    for i in sum(marbles,[]):
        if i == True:
            jum += 1
    print(jum)
    return jum

def wincelebration(randomcongrats):
    global LEBARWINDOW,TINGGIWINDOW
    settingFont = pygame.font.Font('freesansbold.ttf',36)
    permukaanteks = settingFont.render(randomcongrats,True,WINTEKSCOLOR)
    teksRectObj = permukaanteks.get_rect()
    teksRectObj.center = (int(LEBARWINDOW/2),int(TINGGIWINDOW/10))

    DISPLAYSURF.blit(permukaanteks,teksRectObj)

def gambarBG(level):
    if level == 1:
        DISPLAYSURF.fill(BGCOLOR1)
        for i in range(7):
            gambarWadah2(i,3)
        for i in range(7):
            gambarWadah(i,3)

    elif level == 2:
        DISPLAYSURF.fill(BGCOLOR1)
        for i in range(1,6):
            for j in range(1,6):
                gambarWadah2(i,j)
        for i in range(1,6):
            for j in range(1,6):
                gambarWadah(i,j)
    else:
        #default papan 7x7
        DISPLAYSURF.fill(BGCOLOR1)
        for i in range(7):
            for j in range(7):
                gambarWadah2(i,j)
        for i in range(7):
            for j in range(7):
                gambarWadah(i,j)

def setLevel(level):
    # kosongkan marbles table
    marbles = []
    
    # isi dengan False
    for i in range(LEBARPAPAN):
        marbles.append([False] * TINGGIPAPAN)

    # inisialisasi level
    if level == 1:
        pola = ["-------",
                "-------",
                "-------",
                "-**-*--",
                "-------",
                "-------",
                "-------"]
    elif level == 2:
        pola = ["-------",
                "-------",
                "--*----",
                "---**--",
                "---*---",
                "-------",
                "-------"]
    elif level == 3:
        pola = ["-------",
                "---*---",
                "--***--",
                "-*****-",
                "-------",
                "-------",
                "-------"]
    elif level == 4:
        pola = ["-------",
                "---*---",
                "--***--",
                "-**-**-",
                "--***--",
                "---*---",
                "-------"]
    elif level == 5:
        pola = ["-------",
                "---*---",
                "--***--",
                "-*****-",
                "*******",
                "-------",
                "-------"]
    elif level == 6:
        pola = ["---*---",
                "--***--",
                "-*****-",
                "---*---",
                "-*****-",
                "--***--",
                "---*---"]
    elif level == 7:
        pola = ["--***--",
                "--***--",
                "*******",
                "***-***",
                "*******",
                "--***--",
                "--***--"]
        #===========================================
        # ========= tambah level disini ===========
        #===========================================
    else:
        #default level 1
        pola = ["-------",
                "-------",
                "-------",
                "--**-*-",
                "-------",
                "-------",
                "-------"]
        # marbles[int(LEBARPAPAN/2)-2][int(TINGGIPAPAN/2)] = True
        # marbles[int(LEBARPAPAN/2)-1][int(TINGGIPAPAN/2)] = True
        # marbles[int(LEBARPAPAN/2)+1][int(TINGGIPAPAN/2)] = True
    
    # kembalikan nilai marbles table
    marbles=bacapola(pola,marbles)
    return marbles

def tampilReset(x,y,mouseklik):
    fontsize = 40
    settingFont = pygame.font.SysFont('Arial.ttf',fontsize)
    permukaanteks = settingFont.render('Reset',True,WINTEKSCOLOR)
    teksRectObj = permukaanteks.get_rect()
    teksRectObj.topleft = (0,0)

    if teksRectObj.collidepoint(x,y):
        fontsize = 44
        settingFont = pygame.font.SysFont('Arial.ttf',fontsize)
        permukaanteks = settingFont.render('Reset',True,KUNING)
        teksRectObj = permukaanteks.get_rect()
        teksRectObj.topleft = (0,0)
        DISPLAYSURF.blit(permukaanteks,teksRectObj)
        if mouseklik == True:
            return True
        else:
            return False
    DISPLAYSURF.blit(permukaanteks,teksRectObj)
    
def tampilNewLevel(x,y,mouseklik):
    global LEBARWINDOW,TINGGIWINDOW
    fontsize = 40
    settingFont = pygame.font.SysFont('Calibri.ttf',fontsize)
    permukaanteks = settingFont.render('Next Level',True,WINTEKSCOLOR)
    teksRectObj = permukaanteks.get_rect()
    teksRectObj.topright = (LEBARWINDOW,0)
    if teksRectObj.collidepoint(x,y):
        fontsize = 44
        settingFont = pygame.font.SysFont('Calibri.ttf',fontsize)
        permukaanteks = settingFont.render('Next Level',True,KUNING)
        teksRectObj = permukaanteks.get_rect()
        teksRectObj.topright = (LEBARWINDOW,0)
        DISPLAYSURF.blit(permukaanteks,teksRectObj)
        if mouseklik == True:
            return True
        else:
            return False
    DISPLAYSURF.blit(permukaanteks,teksRectObj)

def bacapola(pola,marbles):
    #contoh pola
    
    assert (len(pola)*len(min(pola))) == (LEBARPAPAN * TINGGIPAPAN) , 'jumlah pola dan papan tidak seimbang'
    for baris in range(LEBARPAPAN):
        for kolom in range(TINGGIPAPAN):
            if pola[kolom][baris] == "*":
                marbles[baris][kolom] = True
            else:
                marbles[baris][kolom] = False
    return marbles

def tampilauthor():
    global LEBARWINDOW,TINGGIWINDOW
    fontsize = 36
    settingFont = pygame.font.SysFont('Arial.ttf',fontsize)
    permukaanteks = settingFont.render('@zralvansga',True,BIRUTUA)
    teksRectObj = permukaanteks.get_rect()
    teksRectObj.bottomright = (LEBARWINDOW,TINGGIWINDOW)

    DISPLAYSURF.blit(permukaanteks,teksRectObj)

def tampillevel(level):
    global LEBARWINDOW,TINGGIWINDOW
    fontsize = 48
    settingFont = pygame.font.SysFont('Arial.ttf',fontsize)
    permukaanteks = settingFont.render("LEVEL "+str(level),True,WINTEKSCOLOR)
    teksRectObj = permukaanteks.get_rect()
    teksRectObj.midtop = (int(LEBARWINDOW/2),0)
    DISPLAYSURF.blit(permukaanteks,teksRectObj)


if __name__ == '__main__':
    main()
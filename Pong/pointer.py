import pygame

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

POINTERSIZE = 24
POINTERRADIUS = int (POINTERSIZE * 0.5)
POINTERCOLOR = PUTIH
POINTERCOLOR2 = MERAH

class Pointer():
    def __init__(self):
        self.pos = (0,0) # init pos
        self.r = POINTERRADIUS
        self.color = POINTERCOLOR
        self.color2 = POINTERCOLOR2
        pygame.mouse.set_visible(False)

    def DrawPointer(self,DISPLAYSURF,pos):
        self.pos = pos
        pygame.draw.circle(DISPLAYSURF,self.color,self.pos,self.r)
        pygame.draw.circle(DISPLAYSURF,self.color2,self.pos,self.r-int(self.r/3))
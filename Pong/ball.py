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

UKURANMARBLE = 16
JARI2MARBLE = int (UKURANMARBLE* 0.5)

class Ball():
    def __init__(self,DISPLAYSURF,left,top):
        self.pos = (left,top)
        self.r = JARI2MARBLE
        self.d = self.r * 2
        self.color = MARBLECOLOR
        pygame.draw.circle(DISPLAYSURF,self.color,self.pos,self.r)
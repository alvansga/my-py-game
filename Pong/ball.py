import pygame
from random import choice

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


BALLCOLOR = JINGGA

BALLSPEED = 1
BALLSIZE = 24
BALLRADIUS = int (BALLSIZE * 0.5)

def pickRandomDirection(dir):
    if dir == 'everywhere':
        # ret = [(1,1),(1,-1),(-1,1),(-1,-1),(0,1),(1,0),(0,-1),(-1,0)]
        ret = [(1,1),(1,-1),(-1,1),(-1,-1)]
    elif dir == 'down':
        # ret = [(1,1),(0,1),(-1,1)]
        ret = [(1,1),(-1,1)]
    elif dir == 'up':
        # ret = [(1,-1),(0,-1),(-1,-1)]
        ret = [(1,-1),(-1,-1)]
    elif dir == 'right':
        # ret = [(1,0),(1,-1),(1,1)]
        ret = [(1,-1),(1,1)]
    elif dir == 'left':
        # ret = [(-1,-1),(-1,0),(-1,1)]
        ret = [(-1,-1),(-1,1)]
    else:
        print("warning in pickRandomDirection!")
        ret = []
    return choice(ret)

class Ball():
    def __init__(self,DISPLAYSURF,left,top):
        self.pos = (left,top)
        self.r = BALLRADIUS
        self.speed = BALLSPEED
        self.perim = (self.pos[0]-self.r,self.pos[1]-self.r,self.pos[0]+self.r,self.pos[1]+self.r)
        
        self.d = self.r * 2
        self.color = BALLCOLOR
        self.rect = pygame.draw.circle(DISPLAYSURF,self.color,self.pos,self.r)
        self.initdir = pickRandomDirection('everywhere')
        self.dir = self.initdir

    def StartMoving(self,DISPLAYSURF):
        # need to fill blank first
        (left,top) = self.pos
        self.pos = (left + (self.dir[0] * self.speed),top + (self.dir[1] * self.speed))
        self.perim = (self.pos[0]-self.r,self.pos[1]-self.r,self.pos[0]+self.r,self.pos[1]+self.r)
        # print("ball:",self.perim)
        self.rect = pygame.draw.circle(DISPLAYSURF,self.color,self.pos,self.r)


    def CollideWindow(self,width,height):
        # check perimeter and change direction if collide with window perimeter
        if (self.pos[1] - self.r) < 0 + 1:
            # print(self.pos[1] - self.r)
            # self.dir = pickRandomDirection('down')
            self.dir = (self.dir[0],1)
        elif (self.pos[0] - self.r) < 0 + 1:
            # print(self.pos[0] - self.r)
            # self.dir = pickRandomDirection('right')
            self.dir = (1,self.dir[1])
        elif (self.pos[1] + self.r) > height - 1:
            # print(self.pos[1] + self.r)
            # self.dir = pickRandomDirection('up')
            self.dir = (self.dir[0],-1)
        elif (self.pos[0] + self.r) > width - 1:
            # print(self.pos[0] + self.r)
            # self.dir = pickRandomDirection('left')
            self.dir = (-1,self.dir[1])
        else:
            # masih dalam frame
            pass

    def CollideSomething(self,objek):
        if self.rect.colliderect(objek):
            print("collision")
            self.dir = pickRandomDirection('everywhere')
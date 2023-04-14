import pygame
# CUSTOMIZATION
# CHGSERVAFTER = 2 # 2 or 5
WIN_WIDTH = 1366
WIN_HEIGTH = 768
L_COLOR = [150,0,0]#[180,0,0]
R_COLOR = [0,0,150]#[0,0,180]
SKORLIST_COLOR = [255,255,255]#[0,0,180]
CIRCLE_COLOR = [255,255,255]
# -------------

IRKEY_EXIT = "0x804b"
IRKEY_MENU = "0x800b"

IRKEY_UP = "0x800c"
IRKEY_DOWN = "0x800d"
IRKEY_RIGHT = "0x800e"
IRKEY_LEFT = "0x800f"

TEAM_LEFT , TEAM_RIGHT = 0 , 1

#sport: "TT" , "BD"
TABLETENNIS = "TT"
BADMINTON = "BD"

class Game():
    def __init__(self, sport, changeserv=2):
        self.changeserv = changeserv
        self.sport = sport
        self.serv = 0
        self.skor = [[0,0]]

    def reset(self):
        self.serv = 0
        self.skor = [[0,0]]

    def checkService(game, leftorright=0): #first arguments of method always consider as self
        if game.sport == TABLETENNIS:
            if sum(game.skor[len(game.skor)-1]) % game.changeserv == 0:
                game.serv = ~game.serv #toggle
        elif game.sport == BADMINTON:
            game.serv = leftorright
        else:
            print("unknown sport")

    def changeCourt(game):
        global L_COLOR, R_COLOR
        L_COLOR , R_COLOR = R_COLOR , L_COLOR
        for ele in game.skor:
            ele[0] , ele[1] = ele[1] , ele[0]

    def updateScreen(game, screen):
        pygame.draw.rect(screen, L_COLOR, pygame.Rect(0, 0, WIN_WIDTH//2, WIN_HEIGTH))
        pygame.draw.rect(screen, R_COLOR, pygame.Rect(WIN_WIDTH//2, 0, WIN_WIDTH//2, WIN_HEIGTH))

        top = pygame.Surface((WIN_WIDTH, WIN_HEIGTH//24))
        top.set_alpha(128)
        top.fill((0,0,0))
        screen.blit(top,(0,0))

        font = pygame.font.Font('freesansbold.ttf', int(WIN_HEIGTH/1.5))
        if sum(L_COLOR) < 180:
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

        font = pygame.font.Font('freesansbold.ttf', int(WIN_HEIGTH//32))
        skorlist = ""
        try:
            for i in range(len(game.skor) - 1):
                skorlist += str(game.skor[i][0]) + "-" + str(game.skor[i][1]) + " "
        except:
            pass
        text = font.render(skorlist, True, SKORLIST_COLOR)
        textRect = text.get_rect()
        textRect.left = 4
        textRect.top = 4
        screen.blit(text, textRect)

        if game.serv == 0:
            pygame.draw.circle(screen, CIRCLE_COLOR, (WIN_WIDTH//2 - WIN_HEIGTH//24, WIN_HEIGTH//12//2 + WIN_HEIGTH//24), WIN_HEIGTH//32)
        elif game.serv == -1:
            pygame.draw.circle(screen, CIRCLE_COLOR, (WIN_WIDTH//2 + WIN_HEIGTH//24, WIN_HEIGTH//12//2 + WIN_HEIGTH//24), WIN_HEIGTH//32)

        pygame.display.flip()
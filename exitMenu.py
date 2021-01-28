import pygame
from pygame.locals import *

class ExitMenu(object):
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("comicsansms", 40)
        self.font.set_bold(True)
        self.text = 'Do you really want to exit?'
        self.menuControl = 230
        self.count = 0
        self.buttoms = ['yes','no']
        self.yes = [pygame.image.load(f"Imagens/buttons/yes"+str(i)+".png") for i in range (2)]
        self.yesState = self.yes[0]
        self.no = [pygame.image.load(f"Imagens/buttons/no"+str(i)+".png") for i in range (2)]
        self.noState = self.no[0]
        self.run = True
        self.allPosition = [(230, 250), (430, 250)]



    def settingExitMenu(self):
        self.back = pygame.image.load("Imagens/buttons/Menu1.png").convert_alpha()
        self.screen.blit(self.back, (0, 0))

        # Controling menu buttons efects
        if (self.menuControl == 230):
            self.yesState = self.yes[1]
            self.noState = self.no[0]

        elif(self.menuControl == 430):
            self.yesState = self.yes[0]
            self.noState = self.no[1]


        size = pygame.font.Font.size(self.font, self.text)
        line = self.font.render(self.text, True, (255, 255,255))
        self.screen.blit(line, ((700/2-size[0]/2)+20, 100))
        self.screen.blit(self.yesState, self.allPosition[0])
        self.screen.blit(self.noState, self.allPosition[1])



    def drawExitMenu(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

            pressed_keys = pygame.key.get_pressed()
            if(pressed_keys[K_RIGHT]):
                pygame.time.delay(200)
                if(self.menuControl == 430):
                    self.menuControl = 430
                else:
                    self.menuControl += 200
            elif(pressed_keys[K_LEFT]):
                pygame.time.delay(200)
                if(self.menuControl == 230):
                    self.menuControl = 230
                else:
                    self.menuControl -= 200

            if((pressed_keys[K_RETURN])and(self.menuControl==230)):
                pygame.time.delay(100)
                exit()
            elif((pressed_keys[K_RETURN])and(self.menuControl==430)):
                pygame.time.delay(200)
                return 'main_menu'

            self.settingExitMenu()
            pygame.display.update()
        return True
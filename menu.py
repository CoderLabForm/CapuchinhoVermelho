import pygame
from pygame.locals import *

class MainMenu(object):
    def __init__(self, screen):
        self.screen = screen
        # self.font = pygame.font.SysFont("Arial", 24)
        self.menuControl = 300
        self.count = 0
        self.buttoms = ['play','exit']
        self.play = [pygame.image.load(f"Imagens/buttons/play"+str(i)+".png") for i in range (2)]
        self.playState = self.play[1]
        self.exit = [pygame.image.load(f"Imagens/buttons/exit"+str(i)+".png") for i in range (2)]
        self.exitState = self.exit[0]
        self.tutorial = [pygame.image.load(f"Imagens/buttons/tutorial"+str(i)+".png") for i in range (2)]
        self.tutorialState = self.tutorial[0]
        self.allButtom = []
        self.run = True
        self.allPosition = [(430, 200), (430, 250), (430, 300)]
        # self.displayButtoms()

    # def displayButtoms(self):
    #     self.allButtom = []
    #     self.allPosition = []
    #     x = 265
    #     y = 300
    #     for buttom in self.buttoms:
    #         if(self.currentButtom == buttom):
    #             img = pygame.image.load("Imagens/buttons/"+buttom+"1.png").convert_alpha()
    #             x = 260
    #         else:
    #             x = 265
    #             img = pygame.image.load("Imagens/buttons/"+buttom+"0.png").convert_alpha()

    #         self.allButtom.append(img)
    #         self.allPosition.append((x, y))
    #         y += 50

    def settingMainMenu(self):
        # self.background.settingBackgroundMenu(2)
        self.back = pygame.image.load("Imagens/buttons/Menu.png").convert_alpha()
        self.screen.blit(self.back, (0, 0))

        # Controling menu buttons efects
        if (self.menuControl == 200):
            self.playState = self.play[1]
            self.exitState = self.exit[0]
            self.tutorialState = self.tutorial[0]
        elif(self.menuControl == 300):
            self.playState = self.play[0]
            self.exitState = self.exit[1]
            self.tutorialState = self.tutorial[0]
        elif(self.menuControl == 400):
            self.playState = self.play[0]
            self.exitState = self.exit[0]
            self.tutorialState = self.tutorial[1]

        self.screen.blit(self.playState, self.allPosition[0])
        self.screen.blit(self.exitState, self.allPosition[1])
        self.screen.blit(self.tutorialState, self.allPosition[2])


        # [self.screen.blit(img, pos) for img, pos in zip(self.allButtom, self.allPosition)]

    # Method to move in this menu and return the choose
    def drawMainMenu(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            pressed_keys = pygame.key.get_pressed()
            if(pressed_keys[K_DOWN]):
                print("ok")
                pygame.time.delay(200)
                if(self.menuControl == 400):
                    self.menuControl = 200
                else:
                    self.menuControl += 100
            elif(pressed_keys[K_UP]):
                pygame.time.delay(200)
                if(self.menuControl == 200):
                    self.menuControl = 200
                else:
                    self.menuControl -= 100

            if((pressed_keys[K_RETURN])and(self.menuControl==200)):
                
                return 'game'
            elif((pressed_keys[K_RETURN])and(self.menuControl==300)):
                return 'exit_game'
            elif((pressed_keys[K_RETURN])and(self.menuControl==300)):
                return 'game_tutorial'

            self.settingMainMenu()
            pygame.display.update()
        return True
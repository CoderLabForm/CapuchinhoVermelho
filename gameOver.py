
import pygame
from pygame.locals import *

class GameOver(object):
    def __init__(self, screen):
        self.screen = screen
        # self.font = pygame.font.SysFont("Arial", 24)
        self.menuControl = 200
        self.font = pygame.font.SysFont("comicsansms", 120)
        self.font.set_bold(True)
        self.play = [pygame.image.load(f"Imagens/buttons/play"+str(i)+".png") for i in range (2)]
        self.playState = self.play[1]
        self.mainMenu = [pygame.image.load(f"Imagens/buttons/mainMenu"+str(i)+".png") for i in range (2)]
        self.mainMenuState = self.mainMenu[0]
        self.savingBestsScores()
        self.save = False
        self.run = True
        self.allPosition = [(280, 350), (280, 400)]



    def settingGameOverMenu(self):
        self.back = pygame.image.load("Imagens/buttons/gameOver.png").convert_alpha()
        self.screen.blit(self.back, (0, 0))

        # Controling menu buttons efects
        if (self.menuControl == 200):
            self.playState = self.play[1]
            self.mainMenuState = self.mainMenu[0]
        elif(self.menuControl == 300):
            self.playState = self.play[0]
            self.mainMenuState = self.mainMenu[1]

        self.font = pygame.font.SysFont("comicsansms", 120)
        size = pygame.font.Font.size(self.font,'Game Over')
        line = self.font.render('Game Over', True, (120, 0,0))
        self.screen.blit(line, ((720/2-size[0]/2), 20))

        self.font = pygame.font.SysFont("comicsansms", 50)

        y=270
        for text in self.text:
            size = pygame.font.Font.size(self.font,text)
            line = self.font.render(text, True, (255, 157,53))
            self.screen.blit(line, (20, y))
            y += 30

        self.screen.blit(self.playState, self.allPosition[0])
        self.screen.blit(self.mainMenuState, self.allPosition[1])


    def drawGameOverMenu(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

            pressed_keys = pygame.key.get_pressed()
            if(pressed_keys[K_DOWN]):
                pygame.time.delay(200)
                if(self.menuControl == 300):
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
                pygame.time.delay(200)
                return 'game'
            elif((pressed_keys[K_RETURN])and(self.menuControl==300)):
                pygame.time.delay(200)
                return 'exit_menu'

            if self.save:
                self.savingBestsScores()

            self.settingGameOverMenu()
            pygame.display.update()
        return True


    def savingBestsScores(self):

        text1 = 'Score: '
        text2 = 'Basket: '
        # data last game
        file = open('save/resultado_partida.txt','r')
        data = file.read().split(" ")
        file.close()
        score = int(data[0])
        sweets = int(data[1])

        # Data Best score ever
        file = open('save/data.txt','r')
        data = file.read().split(' ')
        file.close()
        currentBestScore = int(data[0])
        currentBestSweets = int(data[1])

        if(score > currentBestScore):
            text1 = 'New best Score: '
            currentBestScore = score
            text2 = 'Basket: '
            currentBestSweets = sweets
        else:
            currentBestScore = score

        #score
        self.text = [text1+str(currentBestScore),text2+str(currentBestSweets)]

        self.save = False
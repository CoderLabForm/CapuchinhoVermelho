import pygame
from pygame.locals import *


class GameOver(object):
    def __init__(self, screen):
        self.screen = screen
        self.menuControl = 200
        self.font = pygame.font.SysFont("comicsansms", 120)
        self.font.set_bold(True)
        self.play = [pygame.image.load(f"Imagens/buttons/play"+str(i)+".png") for i in range(2)]
        self.playState = self.play[1]
        self.mainMenu = [pygame.image.load(f"Imagens/buttons/mainMenu"+str(i)+".png") for i in range(2)]
        self.mainMenuState = self.mainMenu[0]
        self.text = []
        self.savingBestsScores()
        self.back = None
        self.run = True
        self.allPosition = [(280, 350), (280, 400)]

    def settingGameOverMenu(self):
        self.back = pygame.image.load("Imagens/buttons/gameOver.png").convert_alpha()
        self.screen.blit(self.back, (0, 0))

        # Controling menu buttons efects
        if self.menuControl == 200:
            self.playState = self.play[1]
            self.mainMenuState = self.mainMenu[0]
        elif self.menuControl == 300:
            self.playState = self.play[0]
            self.mainMenuState = self.mainMenu[1]

        self.font = pygame.font.SysFont("comicsansms", 120)
        size = pygame.font.Font.size(self.font, 'Game Over')
        line = self.font.render('Game Over', True, (120, 0, 0))
        self.screen.blit(line, ((720/2-size[0]/2), 20))
        self.font = pygame.font.SysFont("comicsansms", 50)
        y=270
        for text in self.text:
            line = self.font.render(text, True, (255, 157, 53))
            self.screen.blit(line, (20, y))
            y += 30
        self.screen.blit(self.playState, self.allPosition[0])
        self.screen.blit(self.mainMenuState, self.allPosition[1])

    def drawGameOverMenu(self):
        pygame.time.delay(200)
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    pressed_keys = pygame.key.get_pressed()
                    if pressed_keys[K_DOWN]:
                        if self.menuControl == 300:
                            self.menuControl = 200
                        else:
                            self.menuControl += 100
                    elif pressed_keys[K_UP]:
                        if self.menuControl != 200:
                            self.menuControl -= 100
                    if pressed_keys[K_RETURN] and self.menuControl==200:
                        return 'game'
                    elif pressed_keys[K_RETURN] and self.menuControl==300:
                        return 'main_menu'
            self.settingGameOverMenu()
            pygame.display.update()
        return True

    def savingBestsScores(self):
        sweets_flag = False
        score_flag = False
        # data last game
        file = open('save/resultado_partida.txt', 'r')
        data = file.read().split(" ")
        file.close()
        score = int(data[0])
        sweets = int(data[1])
        # Data Best score ever
        file = open('save/data.txt', 'r')
        data = file.read().split(' ')
        file.close()
        currentBestScore = int(data[0])
        currentBestSweets = int(data[1])
        if sweets> currentBestSweets:
            currentBestSweets = sweets
            sweets_flag = True
        if score > currentBestScore:
            text1 = 'New best Score: '
            currentBestScore = score
            text2 = 'Basket: '
            currentBestSweets = sweets
            """file = open("save/data.txt", "w")
            file.write(f"{currentBestScore} {currentBestSweets}")
            file.close()"""
            score_flag = True
        else:
            currentBestScore = score
            currentBestSweets = sweets
            text1 = 'Score: '
            text2 = 'Basket: '
        if score_flag:
            file = open("save/data.txt", "w")
            file.write(f"{currentBestScore} {currentBestSweets}")
            file.close()
        if sweets_flag:
            file = open("save/data.txt", "w")
            file.write(f"{currentBestScore} {currentBestSweets}")
            file.close()
        # score
        self.text = [text1+str(currentBestScore), text2+str(currentBestSweets)]

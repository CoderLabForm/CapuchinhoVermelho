import pygame
import opc


class Jogo:
    def __init__(self, screen):
        self.screen = screen
        # Game objects
        self.capuchinho = opc.Personagem()
        self.caminho = opc.Caminho()
        self.obstaculos = opc.Obstaculos()
        #self.doces = opc.Doces()
        self.doces_coletados = 0
        # HUD stuff
        self.vidas = 3
        #self.hud = opc.HUD(self.screen)
        # loop stuff
        self.velocidade = 0
        self.clock = pygame.time.Clock()
        self.voltar_ao_menu = False
        self.run = True
        self.bandeira_velocidade = True
        self.tempo = 0

    def refresh_game(self):
        self.caminho.draw(self.screen)
        #self.doces.draw(self.screen)
        self.obstaculos.draw(self.screen)
        #self.hud.draw(self.doces_coletados, self.vidas)
        pygame.display.update()

    def manage_buttons(self, keys):
        if keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]:
            self.capuchinho.movement("S")
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.capuchinho.movement("E")
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.capuchinho.movement("D")
        elif keys[pygame.K_ESCAPE]:
            self.voltar_ao_menu = True

    def continue_game(self):
        if self.vidas <= 0:
            return False
        return True

    def update_speed(self):
        if int(self.tempo) % 10 == 0 and self.bandeira_velocidade:
            self.capuchinho.velocidade += 1
            self.caminho.velocidade += 1
            self.obstaculos.velocidade += 1
            #self.doces.velocidade += 1
            self.bandeira_velocidade = False
        elif int(self.tempo) % 10 != 0 and not self.bandeira_velocidade:
            self.bandeira_velocidade = True

    def game_loop(self):
        damage_count = 4
        while self.run:
            self.tempo += self.clock.tick(60) / (60 * 30)
    # terminate execution
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    self.manage_buttons(pygame.key.get_pressed())
                    if self.voltar_ao_menu:
                        return True
            #self.doces.remover_doces(self.obstaculos.internal_list)
            #self.doces.criar_doces()
            #if self.tempo >= 4:
                #if damage_count >= 0.5:
                    #if self.capuchinho.collisao_obstaculos(self.obstaculos.internal_list):
                        #self.vidas -= 1
                        #self.capuchinho.x -= 10
                        #damage_count = 0
                #else:
                    #damage_count += 0.01
            #self.doces.internal_list, value = self.capuchinho.colisao_doces(self.doces.internal_list)
            #self.doces_coletados += value
            self.obstaculos.remover_obstaculos()
            self.update_speed()
            if self.run:
                self.run = self.continue_game()
            self.refresh_game()
        return True

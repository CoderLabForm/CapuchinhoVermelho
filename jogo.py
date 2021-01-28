import pygame
import funcoes as f
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
        self.score = 0
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
        self.capuchinho.draw(self.screen)
        #self.doces.draw(self.screen)
        self.obstaculos.draw(self.screen)
        self.mostrar_informacao()
        pygame.display.update()

    def mostrar_informacao(self):
        imagens = f.imagens_pontos_doces(self.score, self.doces_coletados)
        self.screen.blit(imagens[0], (5, 35))
        self.screen.blit(imagens[1], (625, 35))

    def manage_buttons(self, keys):
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.capuchinho.movement("S")
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.capuchinho.movement("E")
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.capuchinho.movement("D")
        elif keys[pygame.K_ESCAPE] or keys[pygame.K_SPACE]:
            self.voltar_ao_menu = True

    def continue_game(self):
        if self.vidas <= 0:
            return False
        return True

    def gravar_resultados(self):
        ficheiro = open("save/resultado_partida.txt", "w")
        self.atualizar_score()
        ficheiro.write(f"{self.score} {self.doces_coletados}")
        ficheiro.close()

    def update_speed(self):
        if int(self.tempo) % 10 == 0 and self.bandeira_velocidade:
            self.capuchinho.velocidade += 1
            self.caminho.velocidade += 1
            self.obstaculos.velocidade += 1
            #self.doces.velocidade += 1
            self.bandeira_velocidade = False
        elif int(self.tempo) % 10 != 0 and not self.bandeira_velocidade:
            self.bandeira_velocidade = True

    def atualizar_score(self):
        self.score = int((self.velocidade+1)*10*(self.tempo*2)+self.doces_coletados)

    def game_loop(self):
        damage_count = 4
        while self.run:
            self.tempo += self.clock.tick(60) / (60 * 30)
    # terminate execution
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gravar_resultados()
                    return False
                if event.type == pygame.KEYDOWN:
                    self.manage_buttons(pygame.key.get_pressed())
                    if self.voltar_ao_menu:
                        self.gravar_resultados()
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
            self.atualizar_score()
            self.refresh_game()
        self.gravar_resultados()
        return True

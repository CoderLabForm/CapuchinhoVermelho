import pygame
import random
import funcoes as f

distancia_obstaculos = 250
velocidade_inicial = 3
espaco_entre_obstaculos = [o for o in range(0, 600, distancia_obstaculos)]


class Personagem:
    def __init__(self):
        self.coordenadas_x = [137, 310, 483]
        self.imagens = [pygame.image.load(f"Imagens/capuchinho/capuchinho"+str(i)+".png") for i in range(5)]
        self.ordem_imagens = [0, 1, 2, 3, 4, 3, 2, 1]
        self.indice_imagem = 0
        self.aumento_indice = 0
        self.velocidade = 10
        self.x = 310
        self.y = 200
        self.altura_salto = 20
        self.keep_moving = False
        self.destination = 1
        self.direction = None
        self.rect = (self.x, self.y, self.imagens[0].get_size()[0], self.imagens[0].get_size()[1])

    def collisao_obstaculos(self, obstaculos):
        for obst in obstaculos:
            if False:
                return True
        return False

    def colisao_doces(self, coletaveis):
        value = 0
        newdoces = []
        for doce in coletaveis:
            if doce.x + 32 >= self.rect[0] and doce.x <= self.rect[0] + self.rect[2]:
                if doce.y + 32 >= self.rect[1] and doce.y <= self.rect[1] + self.rect[3]:
                    value += doce.value
                    continue
                else:
                    newdoces.append(doce)
            else:
                newdoces.append(doce)
        return newdoces, value

    def draw(self, screen):
        screen.blit(self.imagens[self.ordem_imagens[self.indice_imagem]], (self.x, self.y))
        self.aumento_indice += 0.15
        self.indice_imagem += int(self.aumento_indice)
        if int(self.aumento_indice) == 1:
            self.aumento_indice = 0
        if self.indice_imagem >= len(self.ordem_imagens)-1:
            self.indice_imagem = 0

    def movement(self, event):
        movements = {"D": self.velocidade, "E": -self.velocidade}
        self.x += movements[event]
        if self.x > self.coordenadas_x[2]:
            self.x = self.coordenadas_x[2]
        elif self.coordenadas_x[0] > self.x:
            self.x = self.coordenadas_x[0]
        self.rect = (self.x, self.y, self.imagens[0].get_size()[0], self.imagens[0].get_size()[1])


class Caminho:
    def __init__(self):
        self.current_frame = 0
        self.velocidade = velocidade_inicial
        self.imagem_fundo = pygame.image.load("Imagens/Game Background.png")
        self.imagem_enfeite1 = pygame.image.load("Imagens/enfeites/1.png")
        self.imagem_enfeite2 = pygame.image.load("Imagens/enfeites/2.png")
        self.imagem_enfeite3 = pygame.image.load("Imagens/enfeites/3.png")
        self.coordenadas_y_1 = [y for y in range(0, 480, 35)]
        self.coordenadas_y_2 = [y for y in range(0, 480, 35)]
        self.primeira_fila = [random.choice([1, 2, 3]) if random.random() > 0.7 else 0 for _ in range(len(self.coordenadas_y_1))]
        self.segunda_fila = [random.choice([1, 2, 3]) if random.random() > 0.7 else 0 for _ in range(len(self.coordenadas_y_1))]

    def modificar(self):
        for i in range(len(self.coordenadas_y_1)):
            self.coordenadas_y_1[i] += self.velocidade
            self.coordenadas_y_2[i] += self.velocidade
            if self.coordenadas_y_1[i] > 480:
                self.coordenadas_y_1.pop()
                self.primeira_fila.pop()
                self.coordenadas_y_1.insert(0, 0)
                if random.random() < 0.7:
                    self.primeira_fila.insert(0, random.choice([1, 2, 3]))
                else:
                    self.primeira_fila.insert(0, 0)
            if self.coordenadas_y_2[i] > 480:
                self.coordenadas_y_2.pop()
                self.segunda_fila.pop()
                self.coordenadas_y_2.insert(0, 0)
                if random.random() < 0.7:
                    self.segunda_fila.insert(0, random.choice([1, 2, 3]))
                else:
                    self.segunda_fila.insert(0, 0)

    def draw(self, screen):
        escolha_img = {1: self.imagem_enfeite1, 2: self.imagem_enfeite2, 3: self.imagem_enfeite3}
        screen.blit(self.imagem_fundo, self.imagem_fundo.get_rect())
        for c, e in zip(self.coordenadas_y_1, self.primeira_fila):
            if e:
                screen.blit(escolha_img[e], (270, c))
        for c, e in zip(self.coordenadas_y_2, self.segunda_fila):
            if e:
                screen.blit(escolha_img[e], (443, c))
        self.modificar()


class _obstaculo:
    def __init__(self, x, y):
        self.x = x
        self.ajuste = -23
        self.y = y
        self.imagem = pygame.Surface((1, 1))
        self.choose_image()
        self.hit_box = pygame.mask.from_surface(self.imagem.convert_alpha())
        self.rect = self.imagem.get_rect()
        self.width = 100

    def choose_image(self):
        tipo = str(random.randint(1, 4))
        self.imagem = pygame.image.load(f"Imagens/Obstaculos/{tipo}.png")

    def calculate_position_x(self, ultimo_x):
        if ultimo_x == 0:
            return random.choice([107, 280, 453])
        possibilities = {107: [280, 453], 280: [107, 453], 453: [107, 280]}
        return random.choice(possibilities[ultimo_x])

    def draw(self, screen):
        screen.blit(self.imagem, (self.x, self.y))

    def mover(self, velocidade):
        self.y += velocidade


class Obstaculos:
    def __init__(self):
        self.lista_interna = []
        self.max = len(espaco_entre_obstaculos)
        self.velocidade = velocidade_inicial
        self.criar_obstaculos(True)

    def criar_obstaculos(self, inicializacao=False):
        posicoes_x = [107, 280, 453]
        posi1, posi2, posi3 = 0, 0, 0
        if inicializacao:
            posi1 = random.choice(posicoes_x)
            while posi2 == posi1 or posi2 == 0:
                posi2 = random.choice(posicoes_x)
            while posi3 == posi2 or posi3 == 0:
                posi3 = random.choice(posicoes_x)
            self.lista_interna.append(_obstaculo(posi1, espaco_entre_obstaculos[0]-400))
            self.lista_interna.append(_obstaculo(posi2, espaco_entre_obstaculos[1]-400))
            self.lista_interna.append(_obstaculo(posi3, espaco_entre_obstaculos[2]-400))
        else:
            posi1 = random.choice(posicoes_x)
            self.lista_interna.append(_obstaculo(posi1, -250))

    def remover_obstaculos(self):
        for obstaculo in self.lista_interna:
            if obstaculo.y > 480:
                self.lista_interna.remove(obstaculo)
        if len(self.lista_interna) < self.max:
            self.criar_obstaculos()

    def draw(self, screen):
        for obst in self.lista_interna:
            # print(obst.x, obst.y)
            obst.draw(screen)
            obst.mover(self.velocidade)


class doce:
    def __init__(self, y, type_p, x, ajuste_vel):
        self.type_p = type_p
        self.y = y
        self.x = x
        self.value = self.type_p
        self.image = pygame.image.load(f"Imagens/Doces/{self.type_p}.png")
        self.hit_box = pygame.mask.from_surface(self.image.convert_alpha())
        self.comprimento = 32
        self.velocidade = velocidade_inicial+ ajuste_vel
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def mover(self):
        self.y += self.velocidade


class Doces:
    def __init__(self):
        self.lista_interna = []
        self.primeiros_doces = True
        self.coordenadas = [167, 340, 513]
        self.x = random.choice(self.coordenadas)
        self.distancia_entre_doces = 10
        self.velocidade_adicional = 0
        self.ultima_velocidade = 0
        self.min_dist_between_blocs = 100
        self.max_dist_between_blocs = 200
        self.ultimo_y = 0
        self.mindoces = 3
        self.maxdoces = 5

    def controlar_ultimo(self):
        if len(self.lista_interna):
            if self.lista_interna[-1].y > 480:
                return True
            else:
                return False
        else:
            return True

    def criar_doces(self):
        self.x = random.choice(self.coordenadas)
        self.lista_interna = [doce(-50-i*32*7, self.calculate_typedoce(), random.choice(self.coordenadas),
                                   self.velocidade_adicional) for i in
                              range(random.randint(self.mindoces, self.maxdoces))]

    @staticmethod
    def calculate_typedoce():
        probability = random.random()
        if probability <= 0.3:
            return 1
        elif 0.3 < probability <= 0.55:
            return 2
        elif 0.55 < probability <= 0.75:
            return 3
        elif 0.75 < probability <= 0.9:
            return 4
        else:
            return 5

    def mudar_velocidade(self):
        self.velocidade_adicional += 1

    def remover_doces(self, lista_interna_obst):
        for d, obst in zip(self.lista_interna, lista_interna_obst):
            if d.y < d.comprimento:
                self.lista_interna.remove(d)

    def draw(self, screen):
        for d in self.lista_interna:
            d.draw(screen)
            d.mover()

import pygame
import random
import funcoes as f

distancia_obstaculos = 250
parts_distance = 5
velocidade_inicial = 3
espaco_entre_obstaculos = [o for o in range(0, 600, distancia_obstaculos)]


class Personagem:
    def __init__(self):
        self.coordenadas_x = [137, 310, 483]
        self.imagens = [pygame.image.load(f"Imagens/capuchinho/capuchinho"+str(i)+".png") for i in range(5)]
        self.ordem_imagens = [0, 1, 2, 3, 4, 3, 2, 1]
        self.indice_imagem = 0
        self.aumento_indice = 0
        self.velocidade = 19
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
            if doce.x + 44 >= self.rect[0] and doce.x <= self.rect[0] + self.rect[2]:
                if doce.y + 24 >= self.rect[1] and doce.y <= self.rect[1] + self.rect[3]:
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
        # pygame.draw.rect(screen, (255, 255, 0), self.rect, 5)

    def movement(self, event):
        movements = {"D": -self.velocidade, "E": self.velocidade}
        self.y += movements[event]
        if self.destination == 1:
            if self.direction == "R":
                self.destination = 2
            elif self.direction == "L":
                self.destination = 0
        elif self.destination == 2:
            if self.direction == "R":
                self.destination = 2
            elif self.direction == "L":
                self.destination = 1
        elif self.destination == 0:
            if self.direction == "R":
                self.destination = 1
            elif self.direction == "L":
                self.destination = 0
        self.keep_moving = True
        if self.x > self.coordenadas_x[2]:
            self.x = self.coordenadas_x[2]
        elif self.coordenadas_x[0] > self.x:
            self.x = self.coordenadas_x[0]
        self.rect = (self.x, self.y, self.imagens[0].get_size()[0], self.imagens[0].get_size()[1])

    def continua_mov(self):
        if self.keep_moving:
            self.movement(self.direction)
        if self.y in self.coordenadas_x:
            self.keep_moving = False


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
            return random.choice([187, 360, 533]) + self.adjust
        possibilities = {187: [360, 533], 360: [187, 533], 533: [187, 360]}
        return random.choice(possibilities[ultimo_x - self.adjust]) + self.adjust

    def draw(self, screen):
        screen.blit(self.imagem, (self.x, self.y))

    def mover(self, velocidade):
        self.y += velocidade


class Obstaculos:
    def __init__(self):
        self.lista_interna = []
        self.max = len(espaco_entre_obstaculos)
        self.ajuste = 80
        self.velocidade = velocidade_inicial
        self.criar_obstaculos(True)

    def criar_obstaculos(self, inicializacao=False):
        posicoes_x = [187-self.ajuste, 360-self.ajuste, 533-self.ajuste]
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

"""
class doce:
    def __init__(self, x, type_p, y, cardinality):
        self.type_p = type_p
        self.adjust = 15
        self.y_middle = y + self.adjust
        self.y = self.y_middle + cardinality
        self.x = x
        self.value = self.type_p ** 2
        self.image = pygame.image.load(f"Imagens/Doces/{self.type_p}.png")
        self.hit_box = pygame.mask.from_surface(self.image.convert_alpha())
        self.comprimento = 32
        self.movement_module = 10
        self.upwards = True
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def mover(self):
        alternation = {True: -1, False: 1}
        advancement_y = alternation[self.upwards]
        self.x -= 10
        self.y += advancement_y
        if self.y_middle + self.movement_module * advancement_y == self.y and self.upwards:
            self.upwards = not self.upwards
        elif self.y_middle + self.movement_module * advancement_y == self.y and not self.upwards:
            self.upwards = not self.upwards



class Doces:
    def __init__(self):
        self.internal_list = []
        self.firstdoces = True
        self.choices = [20, 130, 240]
        self.y = random.choice(self.choices)
        self.distancia_entre_doces = 5 + 44
        self.min_dist_between_blocs = 100
        self.max_dist_between_blocs = 200
        self.mindoces = 3
        self.maxdoces = 7

    def control_last(self):
        if self.internal_list[-1].x <= espaco_entre_obstaculos[-2]:
            return True
        else:
            return False

    def criar_doces(self):
        dist_between_blocs = random.randint(self.min_dist_between_blocs, self.max_dist_between_blocs)
        type_p = self.calculate_typedoce()
        if self.firstdoces:
            for i in range(random.randint(self.mindoces, self.maxdoces)):
                self.internal_list.append(
                    doce(espaco_entre_obstaculos[-1] + dist_between_blocs + i * self.distancia_entre_doces, type_p,
                          self.y, i % 10))
            self.firstdoces = False
            return 0
        if self.control_last():
            for i in range(random.randint(self.mindoces, self.maxdoces)):
                self.internal_list.append(
                    doce(espaco_entre_obstaculos[-1] + dist_between_blocs + i * self.distancia_entre_doces,
                          type_p, self.y, i % 10))
            self.y = random.choice(self.choices)
            return 0

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

    def remover_doces(self, internal_list_obst):
        for d, obst in zip(self.internal_list, internal_list_obst):
            if d.x < d.comprimento:
                self.internal_list.remove(d)

    def draw(self, screen):
        for d in self.internal_list:
            d.draw()
            d.mover()


class HUD:
    def __init__(self, screen, mode=False):
        self.screen = screen
        #self.speed_meter_image = pygame.image.load("images/HUD/meter/7.png")
        #self.precision_meter_image = pygame.image.load("images/HUD/meter/7.png")
        self.speed = 0
        self.precision = 0
        self.energy = 0
        self.resistance = 0
        self.doces = 0
        self.mode = mode
        if mode:
            self.time = "infinite"
        else:
            self.time = 60
        self.set_up_HUD()

    def set_up_HUD(self):
        pass

    def draw(self, numero_doces, numero_vidas):
        f.mostrar_vidas(self.screen, numero_vidas)
        f.mostrar_doces(self.screen, numero_doces)
"""
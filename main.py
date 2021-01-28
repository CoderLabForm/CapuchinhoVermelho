import pygame
import linkagem as lnk


class Game:
    link_function_dict: dict

    def __init__(self, screen_width, screen_length, screen_lable, link_functions):
        self.screen = None
        self.link_function_dict = link_functions
        self.previous_link = None
        self.create_screen(screen_width, screen_length, screen_lable)

    def create_screen(self, width, length, lable):
        self.screen = pygame.display.set_mode((length, width))
        pygame.display.set_caption(lable)

    def start(self, link, state=True):
        if state:
            keys_list = list(self.link_function_dict.keys())
            self.previous_link = keys_list[keys_list.index(link)]
            state = self.link_function_dict[link](self.screen)
            if state:
                link = state
                state = True
        else:
            state = self.link_function_dict["exit_menu"](self.screen)
            link = self.previous_link
        self.start(link, state)


pygame.init()
links = {"main_menu": lnk.main_menu, "exit_menu": lnk.exit_game, "game": lnk.game}
Capuchinho_Vermelho = Game(480, 720, "Capuchinho Vermelho", links)
Capuchinho_Vermelho.start("main_menu")

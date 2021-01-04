import pygame
import link_functions as lf


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
            self.previous_link = keys_list[keys_list.index(link)]  # Current link is saved in case the state turns False
            state = self.link_function_dict[link](self.screen)
            if state:
                link = state
                state = True
        else:  # In case the user wants to exit the game by clicking on the red crux the state is set to False
            state = self.link_function_dict["exit1"](self.screen)
            link = self.previous_link
        self.start(link, state)


pygame.init()
# this dictionary has string keys and the corresponding function values.
links = {"main_menu": lf.main_menu, "exit1": lf.exit_game, "game": lf.game}
Capuchinho_Vermelho = Game(700, 1080, "Capuchinho Vermelho", links)  # create the game
Fast_and_Curious.start("main_menu")  # start the game

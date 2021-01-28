import jogo as j
import menu as mn


def main_menu(screen):
    class_menu = mn.MainMenu(screen)
    class_menu.drawMainMenu()
    return 'main_menu'


def exit_game(screen):
    exit()


def game(screen):
    classe_jogo = j.Jogo(screen)
    classe_jogo.game_loop()
    return "main_menu"

import jogo as j
import menu as mn
import exitMenu as exmn


def main_menu(screen):
    class_menu = mn.MainMenu(screen)
    next_link = class_menu.drawMainMenu()
    return next_link


def exit_game(screen):
    class_exitMenu = exmn.ExitMenu(screen)
    return class_exitMenu.drawExitMenu()


def game(screen):
    classe_jogo = j.Jogo(screen)
    classe_jogo.game_loop()
    return "main_menu"

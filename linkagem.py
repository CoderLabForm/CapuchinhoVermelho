import jogo as j
import menu as mn
import exitMenu as exmn
import gameOver as go


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
    return "game_over"


def game_over(screen):
    return "main_menu"


def game_over(screen):
    class_gameOver = go.GameOver(screen)
    return class_gameOver.drawGameOverMenu()

import jogo as j


def main_menu(screen):
    exit(100)


def exit_game(screen):
    exit()


def game(screen):
    classe_jogo = j.Jogo(screen)
    classe_jogo.game_loop()
    return "main_menu"
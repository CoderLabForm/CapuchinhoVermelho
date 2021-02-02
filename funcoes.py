import pygame

pygame.mixer.init()


def criar_imagens(texto):
    pygame.font.init()
    rendered_text = None
    for i in range(14, 40)[::-1]:
        text_font = pygame.font.SysFont('Calibri', i)
        text_font.set_bold(True)
        rendered_text = text_font.render(texto, True, (255, 255, 0))
        if rendered_text.get_size()[0] <= 57:
            break
    return rendered_text


def imagens_pontos_doces(score, doces):
    imagem_score = criar_imagens(str(score))
    imagem_doces = criar_imagens(str(doces))
    return [imagem_score, imagem_doces]


def carregar_som(nome):
    try:
        som = pygame.mixer.Sound("sons/"+nome+".WAV")
    except FileNotFoundError:
        som = pygame.mixer.Sound("sons/"+nome+".mp3")
    return som


def reproduzir(som, musica=False):
    if musica:
        som.play(-1)
    else:
        som.play()


def parar_gradualmente():
    pygame.mixer.fadeout(1)

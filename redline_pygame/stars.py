import pygame
import random
import math
from itertools import combinations

# === CONFIGURAÇÕES CUSTOMIZÁVEIS ===
NUM_LINHAS = 100
INTERVALO_MS = 50  # intervalo entre cada linha em milissegundos
STARS_RADIUS = 1

#colors
BG_COLOR = (25, 27, 26)
STAR_COLOR = (153, 201, 179)
SQUARE_COLOR = (87, 156, 154)

#line
#LINE_COLORS = (41, 66, 87)
LINE_COLORS = BG_COLOR

# ===================================

pygame.init()
screen = pygame.display.set_mode((900, 900))
pygame.display.set_caption("points by jprs.drw")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 20)

# Área de desenho com padding
padding = 50
area = pygame.Rect(padding, padding, 800, 800)

linhas = []
bolinhas = set()
tempo_ultima_linha = 0

def ponto_na_borda():
    lado = random.choice(['top', 'bottom', 'left', 'right'])
    if lado == 'top':
        return (random.randint(area.left, area.right), area.top)
    elif lado == 'bottom':
        return (random.randint(area.left, area.right), area.bottom)
    elif lado == 'left':
        return (area.left, random.randint(area.top, area.bottom))
    else:  # right
        return (area.right, random.randint(area.top, area.bottom))

def gerar_linha():
    p1 = ponto_na_borda()
    p2 = ponto_na_borda()
    # evita que a linha seja um ponto (mesmo ponto duas vezes)
    while p1 == p2:
        p2 = ponto_na_borda()
    return (p1, p2)

def intersecao(l1, l2):
    (x1, y1), (x2, y2) = l1
    (x3, y3), (x4, y4) = l2

    denom = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
    if denom == 0:
        return None

    px = ((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)) / denom
    py = ((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4)) / denom

    if area.collidepoint(px, py):
        return (int(px), int(py))
    return None

def desenhar_texto(texto, pos):
    img = font.render(texto, True, SQUARE_COLOR)
    screen.blit(img, pos)

# === LOOP PRINCIPAL ===
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    agora = pygame.time.get_ticks()

    if len(linhas) < NUM_LINHAS and agora - tempo_ultima_linha > INTERVALO_MS:
        nova_linha = gerar_linha()
        for linha_existente in linhas:
            ponto = intersecao(nova_linha, linha_existente)
            if ponto:
                bolinhas.add(ponto)
        linhas.append(nova_linha)
        tempo_ultima_linha = agora

    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, SQUARE_COLOR, area, 2)

    # linha
    for linha in linhas:
        pygame.draw.line(screen, LINE_COLORS, linha[0], linha[1], 1)

    # balls
    for ponto in bolinhas:
        pygame.draw.circle(screen, STAR_COLOR, ponto, STARS_RADIUS)

    desenhar_texto(f"{len(bolinhas)} points", (padding, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

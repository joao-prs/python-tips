import pygame
import random
import math

# Inicialização do Pygame
pygame.init()

# Configurações da janela
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Teia da Aranha")

# Cores
SPIDER_COLOR = (196, 240, 194)
LINE_1_COLOR = (30, 96, 110)
LINE_2_COLOR = (90, 185, 168)
BG_COLOR = (29, 18, 0)



# Configurações da área quadrada
PADDING = 100
BOX_RECT = pygame.Rect(PADDING, PADDING, WIDTH - 2 * PADDING, HEIGHT - 2 * PADDING)

# Velocidade da bolinha (quanto menor, mais rápido)
speed = 100  # pixels por frame

# Número máximo de linhas (ajuste este valor conforme necessário)
max_lines = 40

# Estado da aranha
points = []  # Pontos já conectados
lines = []   # Linhas já desenhadas
current_line = None
dot_radius = 5
teia_completa = False  # Flag para indicar que a teia está completa

def random_wall_point():
    """Gera um ponto aleatório em uma das paSPIDER_COLORes do quadrado"""
    wall = random.choice(["top", "bottom", "left", "right"])
    if wall == "top":
        return (random.randint(BOX_RECT.left, BOX_RECT.right), BOX_RECT.top)
    elif wall == "bottom":
        return (random.randint(BOX_RECT.left, BOX_RECT.right), BOX_RECT.bottom)
    elif wall == "left":
        return (BOX_RECT.left, random.randint(BOX_RECT.top, BOX_RECT.bottom))
    else:
        return (BOX_RECT.right, random.randint(BOX_RECT.top, BOX_RECT.bottom))

def random_midpoint():
    """Gera um ponto aleatório no meio de uma linha existente"""
    if not lines:
        return random_wall_point()
    line = random.choice(lines)
    x = (line[0][0] + line[1][0]) // 2
    y = (line[0][1] + line[1][1]) // 2
    return (x, y)

def get_next_target():
    """Escolhe o próximo ponto de destino"""
    start = spider["pos"]
    use_mid = random.random() < 0.5 and lines
    end = random_midpoint() if use_mid else random_wall_point()
    return start, end

# Aranha começa no centro
spider = {
    "pos": (PADDING, PADDING),
    "target": None
}

# Loop principal
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, LINE_2_COLOR, BOX_RECT, 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Verifica se atingiu o número máximo de linhas
    if len(lines) >= max_lines and not teia_completa:
        teia_completa = True
        spider["target"] = None  # Para a aranha

    # Inicia nova linha se necessário (só se não tiver completado ainda)
    if not teia_completa and not spider["target"]:
        start, end = get_next_target()
        current_line = [start, end]
        spider["target"] = end
        points.append(start)

    # Move a bolinha (só se não tiver completado ainda)
    if spider["target"] and not teia_completa:
        x1, y1 = spider["pos"]
        x2, y2 = spider["target"]
        dx, dy = x2 - x1, y2 - y1
        dist = math.hypot(dx, dy)

        if dist < speed:
            # Chegou ao destino
            spider["pos"] = spider["target"]
            lines.append((current_line[0], spider["target"]))
            spider["target"] = None
        else:
            # Move em direção ao destino
            dx /= dist
            dy /= dist
            spider["pos"] = (x1 + dx * speed, y1 + dy * speed)

    # Desenha as linhas existentes
    for line in lines:
        pygame.draw.line(screen, LINE_1_COLOR, line[0], line[1], 1)

    # Desenha a linha atual em construção (só se não tiver completado)
    if current_line and spider["target"] and not teia_completa:
        pygame.draw.line(screen, LINE_1_COLOR, current_line[0], spider["pos"], 1)

    # Desenha a bolinha (aranha)
    pygame.draw.circle(screen, SPIDER_COLOR, (int(spider["pos"][0]), int(spider["pos"][1])), dot_radius)

    # Mostra o número de linhas criadas
    font = pygame.font.SysFont(None, 20)
    #text = font.render(f"LINES: {len(lines)} / {max_lines}", True, LINE_2_COLOR)
    text = font.render(f"LINES: {max_lines}", True, LINE_2_COLOR)
    screen.blit(text, (50, 20))

    # Mostra mensagem quando a teia estiver completa
    if teia_completa:
        font = pygame.font.SysFont(None, 30)
        texto_completo = font.render("Done!", True, LINE_2_COLOR)
        text_rect = texto_completo.get_rect(center=(WIDTH//2, 30))
        screen.blit(texto_completo, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
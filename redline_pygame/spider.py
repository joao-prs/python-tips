import pygame
import random
import math

# Inicialização do Pygame
pygame.init()

# Configurações da janela
WIDTH, HEIGHT = 900, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("spiders's lines by jprs.drw")

# Cores
SPIDER_COLORS = [
    (196, 240, 194),  # Verde claro
    #(255, 150, 150),  # Vermelho claro
    #(150, 150, 255),  # Azul claro
    #(255, 255, 150),  # Amarelo claro
]
LINE_COLORS = [
    (30, 96, 110),    # Verde-azulado escuro
    #(110, 30, 96),    # Roxo
    #(96, 30, 110),    # Azul-roxo
    #(110, 96, 30),    # Amarelo-esverdeado
]
BG_COLOR = (29, 18, 0)
speed = 30

# Configurações da área quadrada
PADDING = 50
BOX_RECT = pygame.Rect(PADDING, PADDING, WIDTH - 2 * PADDING, HEIGHT - 2 * PADDING)

# Configurações das aranhas
max_lines = 40    # Número total de linhas
num_spiders = 5  # Número de aranhas (ajuste conforme necessário)
default_dot_radius = 2  # Raio padrão quando a aranha está ativa

#line
line_size = 3
line_size_creating = 2
lines_per_spider = max_lines // num_spiders

def random_wall_point():
    """Gera um ponto aleatório em uma das paredes do quadrado"""
    wall = random.choice(["top", "bottom", "left", "right"])
    if wall == "top":
        return (random.randint(BOX_RECT.left, BOX_RECT.right), BOX_RECT.top)
    elif wall == "bottom":
        return (random.randint(BOX_RECT.left, BOX_RECT.right), BOX_RECT.bottom)
    elif wall == "left":
        return (BOX_RECT.left, random.randint(BOX_RECT.top, BOX_RECT.bottom))
    else:
        return (BOX_RECT.right, random.randint(BOX_RECT.top, BOX_RECT.bottom))

def random_midpoint(lines):
    """Gera um ponto aleatório no meio de uma linha existente"""
    if not lines:
        return random_wall_point()
    line = random.choice(lines)
    x = (line[0][0] + line[1][0]) // 2
    y = (line[0][1] + line[1][1]) // 2
    return (x, y)

def get_next_target(spider, all_lines):
    """Escolhe o próximo ponto de destino para uma aranha específica"""
    start = spider["pos"]
    use_mid = random.random() < 0.5 and all_lines
    end = random_midpoint(all_lines) if use_mid else random_wall_point()
    return start, end

# Inicializa as aranhas
spiders = []
for i in range(num_spiders):
    # Posições iniciais distribuídas pelas bordas
    if i == 0:
        pos = (PADDING, PADDING)
    elif i == 1:
        pos = (WIDTH - PADDING, HEIGHT - PADDING)
    elif i == 2:
        pos = (PADDING, HEIGHT - PADDING)
    else:
        pos = (WIDTH - PADDING, PADDING)
    
    spiders.append({
        "pos": pos,
        "target": None,
        "lines": [],
        "current_line": None,
        "lines_drawn": 0,
        "color": SPIDER_COLORS[i % len(SPIDER_COLORS)],
        "line_color": LINE_COLORS[i % len(LINE_COLORS)],
        "active": True  # Indica se a aranha ainda está tecendo
    })

# Variável para verificar se todas completaram
all_complete = False

# Loop principal
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, (90, 185, 168), BOX_RECT, 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Verifica se todas as aranhas completaram
    if not all_complete:
        all_complete = all(spider["lines_drawn"] >= lines_per_spider for spider in spiders)

    # Processa cada aranha
    for spider in spiders:
        # Só processa se não tiver completado sua quota
        if spider["lines_drawn"] < lines_per_spider and not all_complete:
            spider["active"] = True  # Aranha está ativa
            
            # Inicia nova linha se necessário
            if not spider["target"]:
                start, end = get_next_target(spider, [line for s in spiders for line in s["lines"]])
                spider["current_line"] = [start, end]
                spider["target"] = end

            # Move a aranha
            if spider["target"]:
                x1, y1 = spider["pos"]
                x2, y2 = spider["target"]
                dx, dy = x2 - x1, y2 - y1
                dist = math.hypot(dx, dy)

                if dist < speed:
                    # Chegou ao destino
                    spider["pos"] = spider["target"]
                    spider["lines"].append((spider["current_line"][0], spider["target"]))
                    spider["lines_drawn"] += 1
                    spider["target"] = None
                    
                    # Verifica se completou sua parte
                    if spider["lines_drawn"] >= lines_per_spider:
                        spider["active"] = False  # Aranha concluiu seu trabalho
                else:
                    # Move em direção ao destino
                    dx /= dist
                    dy /= dist
                    spider["pos"] = (x1 + dx * speed, y1 + dy * speed)
        else:
            spider["active"] = False  # Aranha concluiu seu trabalho

    # Desenha todas as linhas de todas as aranhas
    for spider in spiders:
        for line in spider["lines"]:
            pygame.draw.line(screen, spider["line_color"], line[0], line[1], line_size)

    # Desenha as linhas em construção
    for spider in spiders:
        if spider["current_line"] and spider["target"] and spider["active"]:
            pygame.draw.line(screen, spider["line_color"], spider["current_line"][0], spider["pos"], line_size_creating)

    # Desenha as aranhas (só as ativas terão dot_radius > 0)
    for spider in spiders:
        dot_radius = default_dot_radius if spider["active"] else 0
        pygame.draw.circle(screen, spider["color"], (int(spider["pos"][0]), int(spider["pos"][1])), dot_radius)

    # Mostra informações na tela
    font = pygame.font.SysFont(None, 20)
    
    # Número total de linhas (texto)
    total_lines = sum(spider["lines_drawn"] for spider in spiders)
    #text = font.render(f"Total Lines: {total_lines}/{max_lines}", True, (30, 96, 110))
    text = font.render(f"{max_lines} lines", True, (30, 96, 110))
    screen.blit(text, (PADDING, 20))
    
    # Linhas por aranha (texto)
    #for i, spider in enumerate(spiders):
    #    status = "DONE" if spider["lines_drawn"] >= lines_per_spider else "WORKING"
    #    text = font.render(f"Spider {i+1}: {spider['lines_drawn']}/{lines_per_spider} ({status})", 
    #                      True, spider["color"])
    #    screen.blit(text, (20, 60 + i * 30))

    # Mostra mensagem quando todas completarem (texto)
    #if all_complete:
    #    font = pygame.font.SysFont(None, 30)
    #    texto_completo = font.render("All Spiders Done!", True, (30, 96, 110))
    #    text_rect = texto_completo.get_rect(center=(WIDTH//2, 30))
    #    screen.blit(texto_completo, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
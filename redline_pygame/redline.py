import pygame
import math

# Inicializa o pygame
pygame.init()

# Define o tamanho da janela
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Linha Vermelha Giratória")

# Define as cores
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Define as propriedades da linha
line_length = 100
line_angle = 0
line_speed = 2  # Velocidade de rotação (graus por frame)

# Posição inicial do centro da linha
center_x = width // 2
center_y = height // 2

# Direção inicial da linha (velocidade em x e y)
line_direction = [3, 3]

# Função para desenhar a linha rotacionada
def draw_rotating_line(surface, center_x, center_y, length, angle):
    # Calcula as coordenadas das extremidades da linha com base no ângulo
    x1 = center_x + length * math.cos(math.radians(angle))
    y1 = center_y + length * math.sin(math.radians(angle))
    x2 = center_x - length * math.cos(math.radians(angle))
    y2 = center_y - length * math.sin(math.radians(angle))

    # Desenha a linha na tela
    pygame.draw.line(surface, RED, (x1, y1), (x2, y2), 3)

# Loop principal
running = True
while running:
    # Preenche o fundo com preto
    screen.fill(BLACK)

    # Desenha a linha rotacionada
    draw_rotating_line(screen, center_x, center_y, line_length, line_angle)

    # Atualiza o ângulo da linha para ela girar
    line_angle += line_speed
    if line_angle >= 360:
        line_angle = 0

    # Atualiza a posição do centro da linha
    center_x += line_direction[0]
    center_y += line_direction[1]

    # Verifica se a linha bateu nas bordas e inverte a direção
    if center_x + line_length > width or center_x - line_length < 0:
        line_direction[0] = -line_direction[0]
    if center_y + line_length > height or center_y - line_length < 0:
        line_direction[1] = -line_direction[1]

    # Atualiza a tela
    pygame.display.flip()

    # Verifica se o usuário fechou a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controla a taxa de frames
    pygame.time.Clock().tick(60)
    
pygame.quit()
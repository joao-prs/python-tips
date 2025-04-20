import pygame
import random
import math
import sys
import signal

# =================== CONFIGURAÇÕES ===================
LINE_LENGTH = 300                 # Tamanho de cada linha
LINE_SPEED = 100                  # Velocidade (pixels por frame)
MAX_BRANCHES = 3                  # Máximo de linhas por branch
LINE_COLOR = (110, 80, 140)       # Cor da linha (R, G, B)
LINE_WIDTH = 1                    # Largura da linha
MAX_DEPTH = 5                     # Quantidade de subníveis de branch
SCREEN_SIZE = (900, 900)          # Tamanho da janela
FPS = 60                          # Frames por segundo
# =====================================================

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Gerador de Linhas Ramificadas")
clock = pygame.time.Clock()

# Permitir encerrar com Ctrl+C
signal.signal(signal.SIGINT, lambda sig, frame: pygame.quit() or sys.exit())

# Armazena todas as linhas animadas
animated_lines = []

# Armazena todas as linhas finalizadas (para desenhar depois)
static_lines = []

class Line:
    def __init__(self, start, angle, depth):
        self.start = start
        self.angle = angle
        self.depth = depth
        self.length = 0
        self.target_length = LINE_LENGTH
        self.end = start
        self.children_created = False

    def update(self):
        if self.length < self.target_length:
            self.length += LINE_SPEED
            dx = math.cos(self.angle) * self.length
            dy = math.sin(self.angle) * self.length
            self.end = (self.start[0] + dx, self.start[1] + dy)
        else:
            if not self.children_created and self.depth < MAX_DEPTH:
                branch_count = random.randint(0, MAX_BRANCHES)
                for _ in range(branch_count):
                    new_angle = self.angle + random.uniform(-math.pi / 3, math.pi / 3)
                    new_line = Line(self.end, new_angle, self.depth + 1)
                    animated_lines.append(new_line)
                self.children_created = True
            static_lines.append(self)
            return False  # Remover da lista de animação
        return True

# Inicialização das linhas principais
initial_branch_count = random.randint(1, MAX_BRANCHES)
for _ in range(initial_branch_count):
    angle = random.uniform(0, 2 * math.pi)
    animated_lines.append(Line((SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2), angle, 1))

running = True
while running:
    try:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fundo preto

        # Atualizar e desenhar linhas animadas
        new_animated_lines = []
        for line in animated_lines:
            if line.update():
                new_animated_lines.append(line)
        animated_lines = new_animated_lines

        # Desenhar linhas completas
        for line in static_lines:
            pygame.draw.line(screen, LINE_COLOR, line.start, line.end, LINE_WIDTH)

        pygame.display.flip()

        # Quando todas as linhas tiverem sido animadas, parar o loop
        if not animated_lines:
            print("Finalizado. Pressione Ctrl+C para sair.")
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        break
                clock.tick(FPS)
                for line in static_lines:
                    pygame.draw.line(screen, LINE_COLOR, line.start, line.end, LINE_WIDTH)
                pygame.display.flip()

    except KeyboardInterrupt:
        pygame.quit()
        sys.exit()

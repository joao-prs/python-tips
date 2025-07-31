import pygame
import random
import sys

# Configurações
WIDTH, HEIGHT = 800, 800
STEP = 16               # movimento de 5 pixels
PIXEL_SIZE = 16         # pixel desenhado tem tamanho 5x5
STEPS_TOTAL = 750
DELAY_MS = 10

# cores iniciais (escala de cinza que vai clareando)
valor_1 = 1
valor_2 = 1
valor_3 = 1

# Cores de fundo
FUNDO = (0, 0, 0)

# Direções
directions = {
    "up": (0, -STEP),
    "down": (0, STEP),
    "left": (-STEP, 0),
    "right": (STEP, 0)
}
opposite = {
    "up": "down",
    "down": "up",
    "left": "right",
    "right": "left"
}

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel que Desenha")
screen.fill(FUNDO)
clock = pygame.time.Clock()

# Superfície para salvar depois
surface_array = pygame.Surface((WIDTH, HEIGHT))
surface_array.fill(FUNDO)

# Posição inicial
# Define uma margem para evitar as bordas
MARGIN_X = WIDTH // 10
MARGIN_Y = HEIGHT // 10

# Gera ponto aleatório dentro da área central
x = random.randrange(MARGIN_X, WIDTH - MARGIN_X, STEP)
y = random.randrange(MARGIN_Y, HEIGHT - MARGIN_Y, STEP)

last_direction = random.choice(list(directions.keys()))
step_count = 0

running = True
animation_done = False
last_move_time = pygame.time.get_ticks()

while running:
    now = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if animation_done and event.key == pygame.K_s:
                pygame.image.save(surface_array, "pixel_rastro.png")
                print("Imagem salva como 'pixel_rastro.png'")
            elif event.key == pygame.K_ESCAPE:
                running = False

    if not animation_done and now - last_move_time >= DELAY_MS:
        last_move_time = now

        # Atualiza a cor gradualmente
        if valor_3 < 255:
            valor_3 += 1
        elif valor_1 < 255:
            valor_1 += 1
        elif valor_2 < 255:
            valor_2 += 1

        cor_atual = (valor_1, valor_2, valor_3)

        valid_directions = [d for d in directions if d != opposite[last_direction]]
        random.shuffle(valid_directions)

        for d in valid_directions:
            dx, dy = directions[d]
            new_x = x + dx
            new_y = y + dy

            if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT:
                x, y = new_x, new_y
                pygame.draw.rect(screen, cor_atual, (x, y, PIXEL_SIZE, PIXEL_SIZE))
                pygame.draw.rect(surface_array, cor_atual, (x, y, PIXEL_SIZE, PIXEL_SIZE))
                last_direction = d
                break

        step_count += 1
        if step_count >= STEPS_TOTAL:
            animation_done = True
            print("Animação concluída. Pressione 'S' para salvar, 'ESC' para sair.")

    pygame.display.flip()
    clock.tick(1000 // DELAY_MS)

pygame.quit()
sys.exit()

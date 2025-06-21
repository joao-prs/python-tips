from PIL import Image
import random

# Parâmetros personalizáveis
largura =  16
altura = 16
seed = "aaa"

# Inicializa gerador com a seed
random.seed(seed)

# Cria uma nova imagem RGB
imagem = Image.new("RGB", (largura, altura))
pixels = imagem.load()

# Gera pixels baseados na seed
for y in range(altura):
    for x in range(largura):
        r = random.randint(0, 200)
        g = random.randint(0, 200)
        b = random.randint(0, 255)
        pixels[x, y] = (r, g, b)

# Salva imagem com o nome da seed e tamanho
#nome_arquivo = f"imagem_{largura}x{altura}_seed_{seed}.png"
nome_arquivo = f"image.png"
imagem.save(nome_arquivo)

print(f"Imagem salva como: {nome_arquivo}")

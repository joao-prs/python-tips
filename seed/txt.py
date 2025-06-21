import random
import string
import time

# Parâmetros personalizáveis
tamanho_texto = 3000  # número de caracteres no texto

# Entrada interativa
entrada_seed = input("Digite a seed (ou pressione Enter para gerar aleatoriamente): ")

if entrada_seed.strip() == "":
    seed = str(time.time())  # Seed aleatória com base no tempo atual
    print(f"Usando seed aleatória: {seed}")
else:
    seed = entrada_seed
    print(f"Usando seed fornecida: {seed}")

# Inicializa gerador com a seed
random.seed(seed)

# Caracteres possíveis (letras, números, pontuação e espaços)
caracteres_possiveis = string.ascii_letters + string.digits + string.punctuation + ' ' * 10

# Gera texto com base na seed
texto_gerado = ''.join(random.choices(caracteres_possiveis, k=tamanho_texto))

# Nome do arquivo
#nome_arquivo = f"texto_seed_{seed.replace(' ', '_')[:20]}_len_{tamanho_texto}.txt"
nome_arquivo = f"texto.txt"

# Salva o texto no arquivo
with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write(texto_gerado)

print(f"\nTexto salvo como: {nome_arquivo}")

import random

# Definir o número de nomes a serem gerados
contas = 100

# Função para ler os arquivos e retornar uma lista de nomes
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        return [linha.strip() for linha in file.readlines()]

# Carregar arquivos
primeiro_nome_f = ler_arquivo('primeiro_nome_f.txt')
segundo_nome_f = ler_arquivo('segundo_nome_f.txt')
primeiro_nome_m = ler_arquivo('primeiro_nome_m.txt')
segundo_nome_m = ler_arquivo('segundo_nome_m.txt')
terceiro_nome = ler_arquivo('terceiro_nome.txt')
quarto_nome = ler_arquivo('quarto_nome.txt')
quinto_nome = ler_arquivo('quinto_nome.txt')
sexto_nome = ler_arquivo('sexto_nome.txt')

# Função para gerar nome de acordo com o gênero
def gerar_nome(genero):
    if genero == 'feminino':
        primeiro = random.choice(primeiro_nome_f)
        segundo = random.choice(segundo_nome_f)
    elif genero == 'masculino':
        primeiro = random.choice(primeiro_nome_m)
        segundo = random.choice(segundo_nome_m)
    
    # Gerar o nome até o quarto nome
    nome = (
        primeiro + ' ' +
        segundo + ' ' +
        random.choice(terceiro_nome) + ' ' +
        random.choice(quarto_nome)
    )
    
    # 10% de chance de adicionar o quinto nome
    if random.random() < 0.1:
        nome += ' ' + random.choice(quinto_nome)
    
    # 5% de chance de adicionar o sexto nome
    if random.random() < 0.05:
        nome += ' ' + random.choice(sexto_nome)
    
    return nome

# Gerar os nomes
nomes_gerados = []

for _ in range(contas):
    # Alterna entre masculino e feminino (ou você pode definir de outra forma)
    genero = random.choice(['masculino', 'feminino'])
    nome = gerar_nome(genero)
    nomes_gerados.append(nome)

# Exibir os nomes gerados
for nome in nomes_gerados:
    print(nome)
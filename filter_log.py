
# Nome do arquivo de log original
arquivo_original = 'arquivo_de_log.txt'

# Nome do arquivo de log para o Mikrotik 1
arquivo_mikrotik_1 = 'mikrotik_1_log.txt'

# Nome do arquivo de log para o Mikrotik 2
arquivo_mikrotik_2 = 'mikrotik_2_log.txt'

# Números dos Mikrotiks
mikrotik_1 = '54'
mikrotik_2 = '56'

# Função para extrair e deletar linhas específicas
def extrair_e_deletar_linhas(origem, destino, identificador):
    with open(origem, 'r') as arquivo_origem:
        linhas = arquivo_origem.readlines()

    # Filtra as linhas do identificador desejado
    linhas_identificadas = [linha for linha in linhas if f'mikrotik{identificador}' in linha]

    # Escreve as linhas identificadas no arquivo de destino
    with open(destino, 'a') as arquivo_destino:
        arquivo_destino.writelines(linhas_identificadas)

    # Remove as linhas identificadas do arquivo original
    linhas_restantes = [linha for linha in linhas if f'mikrotik{identificador}' not in linha]
    
    with open(origem, 'w') as arquivo_origem:
        arquivo_origem.writelines(linhas_restantes)

# Extrai e deleta as linhas para o Mikrotik 1
extrair_e_deletar_linhas(arquivo_original, arquivo_mikrotik_1, mikrotik_1)

# Extrai e deleta as linhas para o Mikrotik 2
extrair_e_deletar_linhas(arquivo_original, arquivo_mikrotik_2, mikrotik_2)
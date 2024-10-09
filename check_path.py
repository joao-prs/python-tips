import os

# checa 
caminho_pasta = "/pasta_teste"

# Verifica se a pasta existe
if not os.path.exists(caminho_pasta):
  # Se não existir, cria
  os.makedirs(caminho_pasta)
  print(f"A pasta '{caminho_pasta}' foi criada com sucesso!")
else:
  # ja tinha
  print(f"A pasta '{caminho_pasta}' já existe.")
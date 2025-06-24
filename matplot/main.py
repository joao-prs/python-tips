# $ yay -S python-matplotlib
# $ yay -S python-pandas
# $ yay -S python-seaborn


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = pd.read_csv('agua_2022.csv', sep=';')

dados['Quantidade (m3)'] = pd.to_numeric(dados['Quantidade (m3)'], errors='coerce')

# tabela de campus
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=dados,
    y='Quantidade (m3)',
    x='Mes',
    hue='Campus/Unidade',   # random cor
    palette='tab10',        # cores
    s=70                   # ponto
)

plt.xlabel('Quantidade (m³)')
plt.ylabel('Mes')
plt.title('Dispersão por Campus/Unidade')
plt.grid(False)
plt.legend(title='Campus')
plt.tight_layout()
plt.show()
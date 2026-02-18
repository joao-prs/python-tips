import csv
import matplotlib.pyplot as plt

arquivo_csv = "mapa.csv"

nomes = []
xs = []
ys = []
zs = []
cores_ponto = []
cores_texto = []

with open(arquivo_csv, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        nomes.append(row["nome"])
        xs.append(float(row["x"]))
        ys.append(float(row["y"]))
        zs.append(float(row["z"]))
        cores_ponto.append(row["cor_ponto"])
        cores_texto.append(row["cor_texto"])

plt.figure(figsize=(8, 8))

# scatter aceita lista de cores
plt.scatter(xs, zs, c=cores_ponto)

# Adiciona o nome em cada ponto
for nome, x, y, z, cor_txt in zip(nomes, xs, ys, zs, cores_texto):
    plt.annotate(
        #nome,
        (nome, x, y, z),
        (x, z),
        textcoords="offset points",
        xytext=(-30, 5),
        fontsize=9,
        color="#" + cor_txt,
        bbox=dict(
            boxstyle="round,pad=0.2",
            fc="black",
            alpha=0.1
        )
    )

plt.xlabel("Eixo X (Oeste a Leste)")
plt.ylabel("Eixo Z (Sul a Norte)")
plt.title("Mapa dos portais no Nether")

# Z negativo para cima, positivo para baixo
plt.gca().invert_yaxis()
plt.grid(True)

plt.show()

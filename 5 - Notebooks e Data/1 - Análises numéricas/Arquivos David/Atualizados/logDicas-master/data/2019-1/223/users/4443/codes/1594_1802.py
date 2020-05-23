# importar funcoes do modulo math:
from math import *

# Leitura dos pontos de vida iniciais do monstro:
pts = int(input("Quantos pontos de vida o monstro tem? "))

# Leitura dos pontos dos dados de 20 faces
D1 = int(input("Digite o resultado para o dado um: "))
D2 = int(input("Digite o resultado para o dado dois: "))

# Dano causado pelo golpe:
dano = int(((5 * D1)**0.5) + (pi)**(D2/3))

print(pts - dano)
pts_iniciais = float(input("Pontos de vida iniciais: "))
d1 = int(input("dado de 20 faces 1: "))
d2 = int(input("dado de 20 faces 2: "))
from math import *
dano = sqrt(5 * d1) + (pi) ** (d2/3)
dano = int(dano)
print(pts_iniciais - dano)
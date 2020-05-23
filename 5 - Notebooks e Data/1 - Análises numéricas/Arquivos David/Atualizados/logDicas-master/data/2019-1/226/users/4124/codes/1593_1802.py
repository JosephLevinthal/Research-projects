from math import *
pv = int(input("Informe os pontos de vida do monstro: "))
d1 = int(input("Valor do dado 1: "))
d2 = int(input("Valor do dado 2: "))

dam = int(sqrt(5 * d1) + pi ** (d2/3))
lif = pv - dam
print(lif)

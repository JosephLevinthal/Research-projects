# Modulo Math
from math import *
# Entradas
PV = int(input("PV: "))
D1 = int(input("D1: "))
D2 = int(input("D2: "))
# Variavel
f = abs(sqrt(5 * D1) + (pi*(D2 / 3)))
dano = PV - int(f)
# Saida
print(dano)
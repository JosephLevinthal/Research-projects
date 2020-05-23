a = int(input("pontos de vida iniciais: "))
d1 = int(input("valor sorteado 1: "))
d2 = int(input("valor sorteado 2: "))
from math import *
f = sqrt(5*d1) + pi** (d2/3)
dano = int(f)
print(a-dano)

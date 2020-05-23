#pontos de vida iniciais do RPG
p = int(input("digite pontos de vida: "))

#valores sorteados nos dados D1 e D2
d1 = int(input("digite D1: "))
d2 = int(input("digite D2: "))

#pontos de vida RESTANTES
from math import *
dano = int((5*d1)**0.5 + pi ** (d2 / 3))
dano_final1 = (p - dano)

#saídas
print(dano_final1)

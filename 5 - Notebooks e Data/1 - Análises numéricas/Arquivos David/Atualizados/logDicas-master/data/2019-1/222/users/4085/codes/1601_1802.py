pvi = int(input("escreva os pontos de vida iniciais "))
D1 = int(input("valor sorteado no dado 1 "))
D2 = int(input("valor sorteado no dado 2 "))
from math import *
dano = (sqrt(5 * D1) + pi ** (D2/3))
vida = (pvi - dano)
a = int(vida)
print(a + 1)
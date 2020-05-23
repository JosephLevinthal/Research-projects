P = int(input("Pontos de Vida: "))
D1 = int(input("Dado 1: "))
D2 = int(input("Dado 2: "))

from math import*
dano = (sqrt(5*D1)+(pi**(3*D2)))

restante = P - dano

print(restante)
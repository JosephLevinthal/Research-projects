from math import *
vida = float(input("Vida do monstro: "))
D1 = int(input("Primeiro dado: "))
D2 = int(input("Segundo dado: "))

dano = abs((5*D1)**0.5 + pi**(D2/3))
danototal = int(dano)
print(vida - danototal)
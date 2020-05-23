from math import*

hp = float(input("vida do monstro: "))

d1 = int(input("Numero do dado 1: "))
d2 = int(input("Numero do dado 2: "))

dano = abs((5* d1)**0.52 + pi**(d2 /3))

x = int(dano)
print(hp - x)
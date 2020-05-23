from math import *
HPM = int(input("digite a vida do monstro: "))
D1 = int(input("digite um numero de 1 a 20: "))
D2 = int(input("digite um numero de 1 a 20: "))

d = int((sqrt(5*D1))+pi**(D2/3))

Vida = HPM - d
print(Vida)
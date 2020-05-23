from math import*
hp = float(input("vida do monstro: "))
d1 = float(input("dado: "))
d2 = float(input("dado: "))
dano = int(sqrt(5*d1)+ pi**(d2/3))
print(hp-dano)
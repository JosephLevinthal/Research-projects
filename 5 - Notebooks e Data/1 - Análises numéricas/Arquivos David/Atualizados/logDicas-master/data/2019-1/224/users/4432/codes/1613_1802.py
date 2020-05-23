from math import *
vida=int(input("pontos de vida inicial do monstro:     "))
d1=int(input("valor do dado sorteado 1:   "))
d2=int(input("valor do dado sorteado 2:    "))
dano=((5*d1)**0.5)+(pi**(d2/3))
dano=int(dano)
vida=vida-dano
print(vida)
from math import *
vida=int(input("Pontos de vida incial do monstro:"))
D1=int(input("Valor do dado sorteado 1:"))
D2=int(input("Valor do dado sorteado 2 :"))
dano=((5*D1)**0.5)+(pi**(D2/3))
dano=int(dano)
vida=vida-dano
print(vida)

from math import *
P = int(input())
D1 = int(input())
D2 = int (input())
dano = sqrt(5*D1) + pi**(D2/3)
vida = P - int(dano)
print(vida)
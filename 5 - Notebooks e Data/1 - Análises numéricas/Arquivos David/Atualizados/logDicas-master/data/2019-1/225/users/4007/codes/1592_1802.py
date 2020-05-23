from math import*
pvi = int(input("vida inicial: "))
d1 = int(input("dado 1: "))
d2 = int(input("dado 2: "))
dano = sqrt(5 * d1) + (pi ** (d2/3))
danof = int(dano)
pvr = pvi - danof
print(pvr)

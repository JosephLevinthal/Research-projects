from math import*
vida_ini = int(input())
vl_d1 = int(input())
vl_d2 = int(input())
dano = int(sqrt(5*vl_d1)+pi**(vl_d2/3))
print(vida_ini-dano)
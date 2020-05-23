from math import *
vida = int(input("vida:"))
d1 = int(input("d1:"))
d2 = int(input("d2:"))
dano = int( sqrt(5*d1) + ( pi**(d2/3)))
print(vida-dano)
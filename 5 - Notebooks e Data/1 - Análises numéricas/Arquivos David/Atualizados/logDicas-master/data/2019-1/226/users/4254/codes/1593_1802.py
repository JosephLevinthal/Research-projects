from math import*
vida = int(input("valor da vida: "))
d1 = int(input("valor de d1: "))
d2 = int(input("valor de d2: "))

dano = ((sqrt(5*d1)) + pi**(d2/3))
rest = (vida-int(dano))
print(rest)
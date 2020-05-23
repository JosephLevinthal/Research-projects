from math import*

a = int(input("Pontos iniciais: "))
d1 = int(input("D1: "))
d2 = int(input("D2: "))

dano = int(sqrt(5*d1) + pi**(d2/3))

vida_rest = a - dano

print(vida_rest)
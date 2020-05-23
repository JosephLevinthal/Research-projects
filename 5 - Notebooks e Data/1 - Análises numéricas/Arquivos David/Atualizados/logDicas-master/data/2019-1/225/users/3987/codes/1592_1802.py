from math import *
p = int(input("pontos de vida iniciais:"))
d1 = int(input("d1:"))
d2 = int(input("d2:"))
dano = ((5*d1)**0.5) + pi**((d2)//3)
print(p-int(dano))

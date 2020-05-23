from math import *
pv = int(input("insira a vida: "))
D1 = int(input("insira o valor1: "))
D2 = int(input("insira o valor2: "))


dano1 = (sqrt(5 * D1))
dano2 = (pi ** (D2/3))
dt = abs(int(dano1 + dano2))
r = pv - dt
print(r)
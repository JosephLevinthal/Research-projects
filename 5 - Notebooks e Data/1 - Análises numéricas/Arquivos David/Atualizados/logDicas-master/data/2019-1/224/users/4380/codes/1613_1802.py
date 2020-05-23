vida_inicial=int(input("vida inicial: "))
D1=int(input("dado 1: "))
D2=int(input("dado 2: "))
from math import pi
dano=int(((5*D1)**0.5)+pi**(D2/3))
print(vida_inicial-dano)
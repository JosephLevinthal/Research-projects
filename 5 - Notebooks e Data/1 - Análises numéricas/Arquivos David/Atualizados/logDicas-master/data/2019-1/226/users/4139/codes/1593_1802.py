vm=float(input("pontos de vida de um monstro:"))
d1=float(input("valor sorteado de 1:"))
d2=float(input("valor sorteado de 2:"))
from math import *
dano=int(sqrt(5*d1)+pi**(d2/3))
vr=(vm-dano)
print(vr)
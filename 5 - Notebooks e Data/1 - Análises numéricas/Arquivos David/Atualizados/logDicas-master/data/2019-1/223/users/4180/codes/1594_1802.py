pv = int(input('pontos de vida: '))
d1 = int(input('dado 1: '))
d2 = int(input('dado 2: '))

from math import*
dano = ((5*d1)**0.5)+(pi**(d2/3))
a= int(dano)
b= int(pv-a)

print(b)
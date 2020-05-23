from math import*
q= float(input("pontos de vida: "))
d1= int(input("dado 1: "))
d2= int(input("dado 2: "))
dano= ((5*d1)**0.5)+ (pi**(d2/3))
dano2= int(dano)
o= q-dano2
print(o)
from math import*
vida=int(input("pontos de vida:"))
d1=int(input("resultado do d1:"))
d2=int(input("resultado do d2:"))
dano=int(((5*d1)**0.5)+(pi**(d2/3)))
print(vida-dano)
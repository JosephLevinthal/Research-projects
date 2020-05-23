from math import*
x=int(input("pontos de vida: "))
d1=int(input("valor1: "))
d2=int(input("valor2: "))
dano=int(sqrt(5*d1)+pi**(d2/3))
vida=x-dano
print(vida)

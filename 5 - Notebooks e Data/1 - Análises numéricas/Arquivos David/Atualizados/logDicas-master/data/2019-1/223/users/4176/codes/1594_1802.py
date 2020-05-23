from math import* 

a=int(input("Pontos de vida: "))
b=int(input("Dado1: "))
c=int(input("Dado2: "))



dano=((5*b)**0.5) + (pi**(c/3))

z= int(dano)
x= int(a-z)

print(x)
a=input("Pontos de vida: ")
D1=int(input("Numero D1 de 1 a 20: "))
D2=int(input("Numero D2 de 1 a 20: "))

from math import pi

dano= (5*D1)**(1/2) + pi * (D2/3)
f=int(dano)
print(f)
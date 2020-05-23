from math import *

vida =  int(input("Digite a quantidade de vida: "))
d1=int(input("Digite o dado 1: "))
d2=int(input("Digite o dado 2: "))

dano=int(sqrt(5*d1)+(pi**(d2/3)))

vida = vida - dano

print(vida)
from math import *
n1 = int(input("Pontos de vida do monstro:"))
d1 = int(input("Valor primeiro d20:"))
d2 = int(input("Valor segundo d20:"))
n2 =  5*d1
n3 = int(n2**0.5)
n4 = int(d2/3)
n5 = pi**n4
dano = n3+n5
print(int(n1-dano))
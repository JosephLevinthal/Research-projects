from math import *
f = int(input("Quantos pontos de vida iniciais? "))
D1 = int(input("Qual o valor sorteado no primeiro dado? "))
D2 = int(input("Qual o valor sorteado no segundo dado? ")) 
dano = sqrt(5*D1) + pi**(D2/3)
vida= (f - dano)
a = int(vida)
print(a+1)
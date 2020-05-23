from math import *
pvi=int(input("Insira os pontos de vidas iniciais: "))
D1=int(input("Insira os valores sorteados: "))
D2=int(input("Insira os valores sorteados: "))

dano=int(((5*D1)**0.5)+(pi**(D2/3)))
vmd=pvi-dano

print(vmd)
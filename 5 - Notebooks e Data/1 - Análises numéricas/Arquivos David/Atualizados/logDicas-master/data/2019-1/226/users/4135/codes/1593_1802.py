pts_vida = float (input("Digite os pontos de vida do monstro:"))
D1 = int (input("Digite o valor do lancamento do dado 1:"))
D2 = int (input("Digite o valor do lancamento do dado 2:"))
from math import *
dano = int(sqrt(5*D1)+(pi**(D2/3)))
print (pts_vida - dano)
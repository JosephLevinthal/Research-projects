# Pontos de vida iniciais de um monstro antes de uma batalha de RPG (Role Playing Game): 
vida = int(input(" Digite os pontos de vida iniciais de um monstro: "))

# Os valores sorteados no lançamento de dois dados de vinte faces (d1 e d2):
d1 = int(input(" Digite os valores sorteados no lancamento de um dado: "))
d2 = int(input(" Digite os valores sorteados no lancamento do outro dado: "))

#  O dano causado pelo golpe corresponde à parte inteira do seguinte resultado:
from math import sqrt
from math import pi

dano = int (sqrt ( 5 * d1 ) +  pi ** (d2 / 3))
s = int(vida - dano)
print (s)


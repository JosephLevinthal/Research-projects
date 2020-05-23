from math import *

corA1 = float(input("Digite aqui a primeira coordenada do ponto A: "))

corA2 = float(input("Digite aqui a segunda coordenada do ponto A: "))

corB1 = float(input("Digite aqui a primeira coordenada do ponto B: "))

corB2 = float(input("Digite aqui a segunda coordenada do ponto B: "))

dAB = sqrt(((corB1 - corA1) ** 2) + ((corB2 - corA2) ** 2))

print(round(dAB, 3))
from math import *

vida = int(input("Escreva os pontos de vida inicial: "))

D1 = int(input("Escreva o resultado do dado 1: "))

D2 = int(input("Escreva o resultado do dado 2: "))

dano = int(sqrt((5 * D1)) + (pi ** (D2 / 3)))

print(vida - dano)
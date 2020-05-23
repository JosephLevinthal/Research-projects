# Modulo math
from math import *
# Entradas
np = int(input("Determine: "))
# Variavel
prob = 1 - (factorial(365) / factorial(365-np)) * (1 / 365**np)
# Saida
print(round(prob*100, 2))
from math import *

n = int(input("Digite aqui o total de pessoas: "))

prob = float(1 - (factorial(365) / factorial(365 - n)) * (1 / 365 ** n)) * 100

print(round(prob, 2))
n = float(input("Digite o numero de pessoas: "))
from math import *
pn = (1 - (factorial(365) / factorial(365 - n)) * 1 / 365**n) * 100
print(round(pn, 2))
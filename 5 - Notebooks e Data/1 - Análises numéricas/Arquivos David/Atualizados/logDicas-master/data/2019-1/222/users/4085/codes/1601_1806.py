n = int(input("escreva o numero de pessoas: "))
from math import *
p = 1 - (factorial(365)/factorial(365 - n) * 1/365**n)
resultado = p * 100

print(round(resultado, 2))

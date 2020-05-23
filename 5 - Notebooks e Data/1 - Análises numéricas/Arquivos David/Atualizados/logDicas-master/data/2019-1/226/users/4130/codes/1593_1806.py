from math import *

x = int(input("Digite um numero: "))
p = 1 - (factorial(365) / factorial(365 - x)) * (1 / 365 ** x)

y = p * 100

print(round(y, 2))
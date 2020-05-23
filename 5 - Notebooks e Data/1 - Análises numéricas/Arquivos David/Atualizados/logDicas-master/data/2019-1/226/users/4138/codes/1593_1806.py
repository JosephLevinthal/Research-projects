n = float(input("insira o numero de pessoas:"))
from math import *
P = 1 - (factorial(365)/factorial(365 - n) * (1/365**n))
prob = 100 *P

print(round(prob, 2))


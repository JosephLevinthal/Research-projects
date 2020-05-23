n = int(input("quantas pessoas estao no grupo? "))

from math import *
formula = (1 - factorial(365)/ factorial(365 - n) * (1/365**n))*100

print(round(formula, 2))
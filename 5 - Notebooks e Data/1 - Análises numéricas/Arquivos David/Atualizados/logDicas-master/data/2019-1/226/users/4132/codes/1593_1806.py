from math import *

n = int(input("DIgite o numero de pessoas: "))

p= 1 - (factorial(365)/factorial(365-n)) * (1/(365**n))

p = 100*p

print(round(p,2))
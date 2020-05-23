from math import *
n = int(input("no. de pessoas: "))
p = 1 - (factorial(365) / factorial(365 - n)) * 1/(365**n)
print(round(p*100, 2))


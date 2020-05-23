from math import*

n = int(input("Numero de pessoas: "))

p1 = 1 - (factorial(365)/factorial(365 - n)) * (1/365**n)

p = p1 * 100
print(round(p,2))
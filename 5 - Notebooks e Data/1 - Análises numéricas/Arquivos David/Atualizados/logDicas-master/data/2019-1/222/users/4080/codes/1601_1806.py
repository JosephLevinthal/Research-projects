from math import*
n = int(input("N. pessoas: "))
pn = 1 - (365 / (365 - n)) * 1/(365**n)
f = factorial(pn)
print(pn)
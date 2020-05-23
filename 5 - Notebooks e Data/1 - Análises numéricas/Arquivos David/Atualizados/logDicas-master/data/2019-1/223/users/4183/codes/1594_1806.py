from math import *
p = int(input("Digite o numero de pessoas do grupo: "))
pn = factorial(1 - (365/365-p)*(1/365**p))
print(round(pn,2))
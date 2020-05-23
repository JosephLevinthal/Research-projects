np = int(input("Numero de pessoas:"))
from math import*
a = factorial(365)
b = factorial(365-np)
probabilidade =  (1 - (a/b)* (1/365**np))*100
print(round(probabilidade, 2))

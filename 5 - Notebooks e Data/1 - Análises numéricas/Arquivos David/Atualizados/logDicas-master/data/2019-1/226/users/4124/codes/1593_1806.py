from math import *
n = int(input("Informe o numero de pessoas: "))
prob = (1 - (factorial(365)/factorial(365-n)) * (1/365**n))*100
print(round(prob,2))
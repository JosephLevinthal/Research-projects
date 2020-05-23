from math import *

n=float(input("Insira o numero de pessoas "))

p=1-(factorial(365)/factorial(365-n))*(1/365**n)
prob=p*100.00

print(round(prob,2))
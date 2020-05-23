from math import *
n = int(input("insira o valor de n: "))
P = 1 - (((factorial(365)/factorial(365-n))*(1/365**n)))
p = P*100
print(round(p,2))
from math import *
n = int(input("Qual o numero de pessoas? "))
a = factorial(365)
b = factorial(365 - n)
c = 365**n
p = 1-(a/b)*(1/c)
pp = p * 100
print(round(pp, 2))
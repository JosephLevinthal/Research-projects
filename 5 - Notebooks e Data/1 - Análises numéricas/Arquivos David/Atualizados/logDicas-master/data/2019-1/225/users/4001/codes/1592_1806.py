from math import *
n = int(input("Numeros de pessoas: "))
exp = (1 - (factorial(365)/factorial(365 - n)) * (1/365 ** n))
 
print(round(exp * 100, 2))
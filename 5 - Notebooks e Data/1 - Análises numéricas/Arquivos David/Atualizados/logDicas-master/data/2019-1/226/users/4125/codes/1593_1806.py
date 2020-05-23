from math import*
x = int(input("Digite um numero : "))
n = 1 - (factorial(365)/factorial(365-x)) * 1/365**x
n1 = n*100
print(round(n1, 2))
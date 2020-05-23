from math import*
n = int(input("Digite o numero de pessoas: "))
a = factorial(365)/factorial(365-n)
b = 1/(365**n)
p = (1 - a * b) * 100
print(round(p,2))

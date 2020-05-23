from math import*
n = float(input("No. de pessoas:"))
eq = 1 - factorial(365)/factorial(365 - n) * 1/(365**n)
d = eq * 100
print(float(round(d , 2)))
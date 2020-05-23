from math import*
n=float(input("digite o numero de pessoas:  "))
b=1-(factorial(365)/factorial(365-n))*((1)/(365**n))
b=b*100
print(round(b,2))
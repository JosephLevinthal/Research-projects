from math import*

n=float(input("Insira o numero de pessoas:"))

p= 1- factorial(365)/factorial(365-n) * 1 /(365**n)
t=p*100
print(round(t,2))
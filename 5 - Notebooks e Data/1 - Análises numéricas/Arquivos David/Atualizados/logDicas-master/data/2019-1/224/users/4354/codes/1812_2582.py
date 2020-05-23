from math import *
x = float(input("digite o angulo: "))
k = int(input('digite o numero de termos: '))
soma = 0
b = 0
for i in range(k):
	soma = soma + (x**b)/factorial(b)
	b = b + 2
print(round(soma,8))
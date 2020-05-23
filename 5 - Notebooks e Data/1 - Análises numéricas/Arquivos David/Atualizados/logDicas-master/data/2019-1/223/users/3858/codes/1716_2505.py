from math import *
x = eval(input())
k = int(input())
i = 1
a = 3
sinal = -1
soma = x
while(i<k):
	soma = soma + (sinal * ((x**a)/factorial(a)))
	a = a +2
	i = i+1
	sinal = sinal*(-1)

print(round(soma,10))
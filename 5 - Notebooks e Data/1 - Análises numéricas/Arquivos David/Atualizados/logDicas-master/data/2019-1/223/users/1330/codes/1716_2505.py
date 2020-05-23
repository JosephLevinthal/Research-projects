from math import *
x = eval(input())
k = int(input())
v = 1
a = 3
sinal = -1
calculo = x
while(v<k):
	calculo = calculo + (sinal * ((x**a)/factorial(a)))
	a = a +2
	v = v+1
	sinal = sinal*(-1)

print(round(calculo,10))
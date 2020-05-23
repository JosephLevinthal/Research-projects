from math import *
ang = eval(input("digite o angulo: "))
k = int(input("digite a quantidade de termos: "))
if(-1 < ang < 1):
	soma = 0
	b = 0
	for i in range(k):
		sinal = (-1)**i
		soma = soma + sinal*((ang**b)/factorial(b))
		b = b + 2
print(round(soma,11))
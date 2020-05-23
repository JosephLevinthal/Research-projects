from math import *
ang = eval(input("digite o angulo!: "))
k = int(input("digite o valor de k: "))
i = 0
soma = 0
while(k>i):
	soma = soma + ((ang**(2*i+1))/factorial(2*i+1)) * (-1)**i
	i = i+1
print(round(soma,10))
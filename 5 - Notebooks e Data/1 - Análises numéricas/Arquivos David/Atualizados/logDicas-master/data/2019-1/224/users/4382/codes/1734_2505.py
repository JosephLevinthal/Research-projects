from math import *
ang = eval(input("Digite o angulo : "))
k = int(input("Numero de termos : "))
soma = 0
b = 1
i = 0 

while(i < k):
	sinal = (-1)**i
	sen = sinal * ((ang**b)/factorial(b))
	soma = soma + sen
	b = b + 2
	i = i + 1
print(round(soma , 10))
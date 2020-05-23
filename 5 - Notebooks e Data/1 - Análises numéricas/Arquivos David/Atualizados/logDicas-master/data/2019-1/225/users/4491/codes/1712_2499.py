from math import *
x = float(input("termo geral: "))
factorial(x)
soma = 0		#variavel acumuladora
i = 0			#variavel contadora
while(i < x):
	soma = soma + 1 / factorial(i)
	i = i + 1
print(round(soma, 8))
	
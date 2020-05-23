from math import *
n = int(input('Digite n: '))
soma = 0
sinal = 1
cont = 1
d1 = 1
d2 = 3 
exd2 = 0 
while (cont <= n):
	soma = soma + (1/(d1*(d2**exd2))) * sinal
	sinal = sinal * (-1)
	d1 = d1 + 2
	exd2 = exd2 + 1
	cont = cont + 1
soma = soma * sqrt(12)
print(round(soma,8))
	
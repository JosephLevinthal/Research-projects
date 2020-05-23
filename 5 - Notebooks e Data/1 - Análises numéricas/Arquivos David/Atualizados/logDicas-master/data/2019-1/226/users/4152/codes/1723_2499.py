from math import *
k = int(input("Quantidades de termos: "))
#1 / factorial(i)
i = 0            #Variável Contadora
soma = 0         #Variável Acumuladora
fim = k - 1
while (fim >= i):
	soma = soma + 1 / factorial(i)
	i = i + 1
print(round(soma, 8))
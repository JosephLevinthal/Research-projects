# Instituto de Computacao - UFAM
# Nathaly Leite

from math import *

x = eval(input("Informe valor de x: "))
k = int(input("Informe um numero K: "))

soma = x
i = 1
sinal = -1
expoente = 3

while (i < k):
	#f = factorial(expoente)
	soma = soma + (sinal * (x ** expoente)) / factorial(expoente)
	sinal = sinal * (-1)
	expoente = expoente + 2
	i = i + 1
	
print (round(soma,10))
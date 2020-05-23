from math import*
x = eval(input("valor de x: "))
k = int(input("valor de k: "))
soma = x
i = 1
sinal = -1
expoente = 3
while(i<k):
	f = factorial(expoente)
	soma = soma + (sinal*(x**(expoente)))/f
	sinal = sinal * (-1)
	expoente = expoente + 2
	i = i + 1
print(round(soma, 10))


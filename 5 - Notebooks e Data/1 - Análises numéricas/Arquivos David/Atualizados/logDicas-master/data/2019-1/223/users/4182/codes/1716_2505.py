from math import*

x = eval(input("x: "))
k =  int(input())
contador = 1
sinal = -1
soma = x
expoente = 3 

while (contador < k):
	soma =  soma + (sinal * (x**expoente/factorial(expoente)))
	sinal = sinal*(-1)
	expoente = expoente + 2
	contador += 1
print(round(soma,10))
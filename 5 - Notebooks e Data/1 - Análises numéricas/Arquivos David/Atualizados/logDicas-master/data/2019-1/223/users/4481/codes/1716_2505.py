from math import *
x = eval(input(" digite o valor de x: "))
k = int(input("digite o valor de y: "))
contador = 1
sinal = -1
result = x
expoente = 3
while(contador < k):
	result = result + (sinal * (x ** expoente / factorial(expoente)))
	sinal = sinal * (-1)
	expoente = expoente + 2
	contador +=1
print(round(result, 10))
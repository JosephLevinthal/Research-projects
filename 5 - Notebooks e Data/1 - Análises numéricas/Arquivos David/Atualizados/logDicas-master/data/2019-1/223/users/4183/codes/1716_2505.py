from math import *
x = eval(input("Digite o valor de x: "))
k = int(input("Digite o valor de k: "))
cont = 1
sinal = -1 
result = x
exp = 3
while(cont < k):
	result = result + ((sinal * (x ** exp) / factorial(exp)))
	sinal = sinal * (-1)
	exp = exp + 2
	cont = cont + 1
print(round(result,10))
							 
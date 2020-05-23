from math import *   
x = eval(input('digite    '))
k = int(input('digite s:  '))
contador = 1
sinal = -1 
resultado = x
expoente = 3
while (contador < k):
	resultado = resultado + (sinal*(x**expoente/factorial(expoente)))
	sinal = sinal*(-1)
	expoente = expoente +2
	contador = contador +1
	
print(round(resultado,10))











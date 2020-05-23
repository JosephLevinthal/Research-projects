from math import *
k=int(input("Um numero natural: "))
contador = 1
resultado = 1
denominador = 1
while (contador < k):
	resultado = resultado + (1/factorial(denominador))
	denominador = denominador + 1
	contador = contador + 1
print(round(resultado,8))
	
	
	
	


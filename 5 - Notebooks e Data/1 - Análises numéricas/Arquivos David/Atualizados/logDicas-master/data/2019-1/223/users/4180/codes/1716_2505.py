from math import*

x = eval(input("Valor de x:" ))
k = int(input("Valor de k: "))

cont = 1
sinal = -1
resultado = x
exp = 3

while( cont < k ):
	resultado = resultado + (sinal * (x ** exp / factorial (exp)))
	sinal = sinal * -1
	exp = exp + 2
	cont+=1
print(round(resultado, 10))
	
	
	
	
	
	

from math import *

x = float(input("Valor de x: "))
k = int(input("Quantidade de termos: "))
#Valor constante
soma = 1

#Valores que variam
e = 2
c = 0

if (k == 1):
	print(soma)
else:	
	while (c <= k - 2):
		h = (x**e)/factorial(e)
		soma = soma + h
		c = c + 1
		e = e + 2
	print(round(soma, 8))	
	

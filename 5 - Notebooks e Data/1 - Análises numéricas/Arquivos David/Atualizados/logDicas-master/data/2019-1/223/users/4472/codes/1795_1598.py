from numpy import *

valor = array(eval(input("Valores: ")))

i = 0

while i < size(valor):
	
	if valor[i] > 80:
		soma = sum(valor) - 5
	else:
		soma = sum(valor)
	i = i + 1

print (round(soma,2))
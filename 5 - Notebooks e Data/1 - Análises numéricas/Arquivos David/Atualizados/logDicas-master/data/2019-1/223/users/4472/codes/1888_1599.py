from numpy import *

valor = array(eval(input("Valores: ")))
i=0

if valor[i] > 80:
	valor[i] = valor[i] - (valor[i]*15/100)
	resultado = sum(valor)
else:
	resultado = sum(valor)
	
print(round(resultado,2))
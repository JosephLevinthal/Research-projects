from numpy import*
from math import*
compra=eval(input("compras: "))

aux=sum(compra)

for i in compra:
	if (i >= 80 ):
		aux=aux-5
	
print(round(aux, 2))
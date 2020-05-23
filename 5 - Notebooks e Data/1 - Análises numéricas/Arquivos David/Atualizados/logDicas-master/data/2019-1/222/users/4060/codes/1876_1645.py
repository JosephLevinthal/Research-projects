from numpy import*
from math import*

valores=eval(input("valores: "))
cont=0
aux=0
aux1=0
for i in valores:
	if (i>=2000):
		cont=cont+1
zeros=zeros(cont, dtype=int)
for i in valores:
	if(i>=2000):
		zeros[aux1]=zeros[aux1]+aux
		aux1=aux1+1
	aux=aux+1	
print(cont)
print(zeros)
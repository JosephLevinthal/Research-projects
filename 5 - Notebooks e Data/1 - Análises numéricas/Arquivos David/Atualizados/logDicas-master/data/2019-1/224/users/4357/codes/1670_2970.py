t=float(input("digite o numero"))
from math import*
qf= 1042000
qo=1500
i= ((qf/qo)**(1/t))-1
if ( i<=0.01):
	mensagem= "Real"
else:
	mensagem= "Irreal"
print(round(i,5))
print(mensagem)
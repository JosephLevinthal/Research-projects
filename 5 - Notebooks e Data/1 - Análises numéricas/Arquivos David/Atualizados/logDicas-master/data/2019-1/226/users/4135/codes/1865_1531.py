from numpy import*
from math import*
x=eval(input("Digite o angulo: "))
k=int(input("Gite o n de termos: "))
i=0
sinal=1
while(x>0):
	i=(i+1)*2
	x=x**i
	sinal=-sinal
	fac=factorial(i)
	
cos=sinal*x/fac
if(k>0):
	print(round(cos,10))	
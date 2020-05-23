from math import factorial
from math import pi
x=eval(input("valor de x: "))
k=int(input("valor de k: "))
contador=1
sinal=-1
soma=x
expoente=3
while(contador <k):
	soma=soma+(sinal*(x**expoente/factorial(expoente)))
	sinal=sinal*(-1)
	expoente=expoente+2
	contador=contador+1
print(round(soma, 10))	

from math import factorial
from math import pi
x=eval(input("Valor de x: "))
k=int(input("Valor de k: "))
cont=1
sinal=-1
resultado=x
expoente=3

while(cont<k):
	resultado=resultado+(sinal*(x**expoente/factorial(expoente)))
	sinal=sinal*(-1)
	expoente=expoente+2
	cont=cont+1
print(round(resultado, 10))	
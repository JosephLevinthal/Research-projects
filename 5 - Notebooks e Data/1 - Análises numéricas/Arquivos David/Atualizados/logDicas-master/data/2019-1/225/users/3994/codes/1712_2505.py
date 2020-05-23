from math import*
x=eval(input("Digite o angulo: "))
k=int(input("Digite o numero de termos: "))
a=0
i=0
sinal=+x
while(i<k):
	a = a+sinal**(2*i+1)/factorial(2*i+1)
	sinal=-sinal
	i=i+1
print(round(a,10))

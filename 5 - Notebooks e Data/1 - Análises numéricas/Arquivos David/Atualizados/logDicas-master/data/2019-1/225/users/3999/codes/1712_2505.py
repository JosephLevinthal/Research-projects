from math import*
x=eval(input("angulo: "))
n=int(input("numero de termos: "))
soma=0
i=0
sinal=+x
while(i<n):
	soma=soma+sinal**(2*i+1)/factorial(2*i+1)
	sinal=-sinal
	i=i+1
print(round(soma,10))	
	
		 
from math import*
an=eval(input("angulo: "))
k=int(input("numero: "))
i=0
soma=0
while(i<k):
	soma=soma+(-1)**i*an**(2*i+1)/factorial(2*i+1)
	i=i+1
print(round(soma,10))


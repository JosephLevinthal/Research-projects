from math import sqrt
npi=int(input("digite o numero:"))
a=0
b=1
i=0
soma=0
if(npi==1):
	print(sqrt(12))
else:
	while(i<npi):
		sinal=(-1)**i
		soma= soma+sinal*(1/(b*(3**a)))
		a=a+1
		b=b+2
		i=i+1
	print(round(sqrt(12)*soma,8))
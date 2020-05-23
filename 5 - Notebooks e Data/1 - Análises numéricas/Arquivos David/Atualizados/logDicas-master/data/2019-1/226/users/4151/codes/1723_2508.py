from math import*
k=int(input("digite um numero: "))
soma=3
i=2
j=0
while(1<k):
	soma=soma+(4/(i*(1+i)*(i+2)))*(-i)**j
	i=i+2
	j=j+1
	k=k-1
	
print(round(soma,8))
from math import*
k=int(input("digite um numero: "))
i=0
soma=0
while(i<k):
	soma=soma+(1/factorial(i))
	i=i+1
print(round(soma,8))

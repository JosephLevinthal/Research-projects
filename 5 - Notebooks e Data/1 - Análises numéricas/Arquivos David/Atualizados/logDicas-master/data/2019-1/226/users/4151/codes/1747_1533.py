from math import*
x=float(input("digite um numero: "))
k=int(input("digite um numero: "))
i=1
soma=1
while(i<k):
	soma=soma+1*x**(2*i)/factorial(2*i)
	i=i+1
print(round(soma,8))
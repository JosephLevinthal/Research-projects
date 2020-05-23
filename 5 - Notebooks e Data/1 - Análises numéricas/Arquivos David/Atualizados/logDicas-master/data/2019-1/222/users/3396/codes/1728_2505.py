
from math import*
x=eval(input("digite o angulo:"))
k=int(input())
soma=0
n=1
f=1
while	(k>0):
	k=k-1
	soma = soma+ (pow(x,n)/factorial(n)*f)
	f=f*-1
	n=n+2
print(round(soma,10))
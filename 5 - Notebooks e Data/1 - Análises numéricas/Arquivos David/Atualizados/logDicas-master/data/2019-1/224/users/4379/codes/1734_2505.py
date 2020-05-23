from math import *
x=eval(input("digite o angulo"))
k=int(input("digite o termo"))
soma=0
i=0
b=1

while(i<k):
	sinal=(-1)**i
	soma=soma+sinal*(x**b/factorial(b))
	i=i+1
	b=b+2
print(round(soma,10))
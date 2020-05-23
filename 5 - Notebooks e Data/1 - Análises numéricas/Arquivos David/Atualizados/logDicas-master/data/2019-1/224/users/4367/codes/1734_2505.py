from math import*
x=eval(input("angulo: "))
k=int(input("numero em series: "))
c=0
soma = 0
b = 1
while(c<k):
	sinal = (-1)**c
	soma = soma + sinal*((x**b)/factorial(b))
	c=c+1
	b = b + 2
print(round(soma,10))

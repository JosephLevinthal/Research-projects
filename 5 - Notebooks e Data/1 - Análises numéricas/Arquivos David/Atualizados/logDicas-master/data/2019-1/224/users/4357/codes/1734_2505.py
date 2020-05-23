from math import*
angulo=eval(input("digite o numero:"))
k=int(input("digite o numero:"))
soma=0
a=1
e=0
while(e<k):
	sinal=(-1)**e
	sen= sinal*((angulo**a)/factorial(a))
	soma= soma+sen
	a=a+2
	e=e+1
print(round(soma,10))
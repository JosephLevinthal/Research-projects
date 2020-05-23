from math import*
x=eval(input("Digite um numero: "))
y=int(input("Digite os termos: "))
d=2
t=1
l=1
j=1
while(y>j):
	l=l-(((x**d)/factorial(d))*t)
	d=d+2
	t=-t
	j=j+1
print(round(l,11))	
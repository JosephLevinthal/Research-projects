from math import*
x=eval(input("angulo de x:"))
k=int(input("termos da serie:"))

c=0
d=1
e=0
aux=1
while(c<k):
	e=e+(aux*((x**d)/factorial(d)))
	if(aux==1):
		aux=-1
	else:
		aux=1
	c=c+1
	d=d+2
print(round(e, 10))
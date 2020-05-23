from math import*
x=eval(input("o angulo: "))
k=int(input("digite o numero de termos na serie: "))
c=0
s=0
b=1
while(c<k):
	si=(-1)**c
	s=s+si*((x**b)/factorial(b))
	c=c+1
	b=b+2
print(round(s, 10))
from math import*

x=eval(input("O angulo x, medido em radianos:"))
k=int(input("numero natural:"))
i=0
o=0
d=0
y=0
while(i<k):
	s=d+1
	e=(x**s)/(factorial(s))
	y=e-y
	z=y*(-1)**(i)
	d=d+2
	i=i+1

print(round(z,10))


from math import*
x=eval(input("Angulo: "))
k=int(input("n: "))
i=1
d=1
c=0
f=1
soma=0
while(c<k):
	cosx = f -(x**(i+1)/factorial(2*d))
	b =(((-1)**(i+1)))
	g= cosx*b
	c=c+1
	d=d+1
	i=i+1
print(round(cosx,6))
	
	
	



from math import*
x=eval(input("coloque o angulo: "))
y=eval(input("coloque o numero de serie: "))
g=0
s=x
d=0
f=1
k=1
while(y>g):
	s=s+(d*f)
	k=k+2
	d=((x**k)/((factorial(k))))
	f=-f
	g=g+1
	
print(round(s,10))	
	
	
from numpy import*
a=float(input("entre com o valor;"))
v=float(input("entre ae neguin"))
n=int(input("entre com um numero neguin:"))

t=arange(n)
i=0
d= zeros(n)
while(i<size(t)):
	d[i]=((a*t[i]**2)/2)+v*t[i]
	i=i+1
print(d)

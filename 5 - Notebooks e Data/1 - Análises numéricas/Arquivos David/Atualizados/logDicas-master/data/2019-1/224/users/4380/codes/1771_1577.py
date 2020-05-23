from numpy import *
a=float(input("aceleracao: "))
vel=float(input("velocidade inicial: "))
n=int(input("elementos: "))
i=0
v=arange(n)
d=zeros(n)
while (i<size(v)):
	d[i]=a*v[i]**2/2.+vel*v[i]
	i=i+1
print(d)
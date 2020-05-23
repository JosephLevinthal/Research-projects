from numpy import *
a=float(input("aceleracao: "))
vi=float(input("velocidade inicial: "))
n=array(eval(input("numero inteiro: ")))
t=arange(n)
d=zeros(n)
s=((a*t**2/2)+vi*t)
i=0

while(i<n):
	dt=(a*t[i]**2/2)+vi*t[i]
	d[i]=dt
	i=i+1
print(d)

from numpy import*
a=float(input("aceleracao: "))
v=float(input("velocidade: "))
n=int(input("digite um numero: "))
i=0
t=arange(n)
d=zeros(n)
while(i< size(t)):
	d[i]=(a*t[i]**2/2)+v*t[i]
	i=i+1
print(d)
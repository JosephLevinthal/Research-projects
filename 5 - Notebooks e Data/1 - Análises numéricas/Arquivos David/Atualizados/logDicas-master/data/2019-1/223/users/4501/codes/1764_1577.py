from numpy import*
a=float(input("aceleracao: "))
v0=float(input("velocidade inicial: "))
N=int(input("numero inteiro: "))
c=0
b=arange(N)
d=zeros(N)
while(c<size(b)):
	t=b[c]
	dt=(a*t**2)/2+v0*t
	d[c]=dt
	c=c+1
print(d)	
	
	


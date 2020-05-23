from numpy import*

a=float(input("aceleracao: "))
v=float(input("velocida inicial: "))
N=int(input("nu: "))
f=arange(N)
b=zeros(N)

d1=(a*((f)**2))/2
d2=d1+(v*f)
print(d2)


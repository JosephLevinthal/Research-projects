from numpy import *
a = float(input("aceleracao"))
v0= float(input("velocidade inicial"))
n= int(input("numero qualquer"))
vet=arange(n)
var=zeros(n,dtype=float)
d=((a*vet**2)/2)+v0*vet
print(d)

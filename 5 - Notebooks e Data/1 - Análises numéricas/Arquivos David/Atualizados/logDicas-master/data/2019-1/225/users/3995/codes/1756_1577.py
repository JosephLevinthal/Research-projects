a=float(input("aceleracao:"))
v0=float(input("velocidade:"))
n=int(input("numero:"))
from numpy import*
t=arange(n)
d=zeros(n)
d=((a*(t**2))/2)+v0*t
print(d)
from numpy import*
a=float(input("escreva a: "))
vi=float(input("escreva vi: "))
n=int(input("escreva n: "))
d=zeros(n)
t=arange(n)
d=((a*(t**2))/2)+vi*t
print(d)
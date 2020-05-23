from numpy import*
a=float(input("digite a aceleracao:"))
v0=float(input("digite a velocidade inicial:"))
N=int(input("digite um numero N:"))
vt=arange(N)
vd=zeros(N)
vd=((a*vt**2)/2)+v0*vt
print(vd)

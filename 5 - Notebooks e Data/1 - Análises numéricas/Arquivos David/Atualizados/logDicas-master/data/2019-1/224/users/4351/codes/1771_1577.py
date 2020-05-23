from numpy import*
a=float(input("aceleracao: "))
v0=float(input("vel.. inicial : "))
N=int(input("positivo : "))
vt=arange(N)
vd=zeros(N)
vd=((a*vt**2)/2)+v0*vt
print(vd)

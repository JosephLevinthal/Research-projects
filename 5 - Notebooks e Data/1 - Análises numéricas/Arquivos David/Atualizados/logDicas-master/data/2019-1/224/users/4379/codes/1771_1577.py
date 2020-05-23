from numpy import*
A=float(input("digite a aceleracao"))
V=float(input("digite a velocidade"))
N=int(input("digite o n"))
t=0
Va=arange(N,dtype=int)
d0=(A*(Va**2)/2)+Va*V
print(d0)


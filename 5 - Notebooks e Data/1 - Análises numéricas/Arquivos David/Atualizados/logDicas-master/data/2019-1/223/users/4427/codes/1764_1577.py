# ADRIANA BINDA LIMA
# VETOR DE POSICOES DO CARRO

from numpy import*
a=float(input("aceleracao: "))
v=float(input("velocidade: "))
N=int(input("Numero Positivo: "))

t=arange(N)
d=zeros(N,dtype=int)
vf=((a*(t**2)/2)) + (v*t)

print(array(vf))

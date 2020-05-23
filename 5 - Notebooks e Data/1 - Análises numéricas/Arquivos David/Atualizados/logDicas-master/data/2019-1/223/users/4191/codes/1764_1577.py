from numpy import *

a=float(input("aceleracao: "))
v=float(input("velocidade inicial: "))
n=float(input('Numero: '))

t=arange(n)




p=(a*t**2/2)+v*t

print(p)
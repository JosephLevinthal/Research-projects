from numpy import *

aceleracao =float(input('aceleracao do carro: '))
velocidade =float(input('velocidade d0 carro: '))
N = int(input('numero positivo: '))

t = arange(N)
d = zeros(N,dtype=int)

vetorfinal =((aceleracao * (t**2) / 2)) + (velocidade * t)

print(array(vetorfinal))
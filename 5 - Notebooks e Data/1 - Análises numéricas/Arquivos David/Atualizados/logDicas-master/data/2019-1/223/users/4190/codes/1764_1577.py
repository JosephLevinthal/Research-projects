from numpy import *

a = float(input('Aceleracao: '))
v = float(input('Velocidade inicial: '))
n = int(input('Numero: '))

t = arange(n)
d = zeros(n)

k = ((a*(t**2))/2)+v*t
print(k)
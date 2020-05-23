from numpy import *

a = float(input("Aceleracao: "))
v0 = float(input("Velocidade incial: "))
N = int(input("N: "))

t = arange(N)

d = zeros(N)

i = 0

while (i < N):
	ti = t[i]
	dti = (a*(ti**2)/2) + v0*ti
	d[i] = d[i] + dti
	i = i + 1
print(d)
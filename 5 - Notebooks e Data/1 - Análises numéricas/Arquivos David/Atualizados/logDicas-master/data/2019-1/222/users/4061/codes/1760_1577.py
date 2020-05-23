from numpy import *
acel = float(input("digite aceleracao: "))
vel = float(input("digite velocidade: "))
N = int(input("digite numero: "))

i = 0
t = arange(N)
tam = N
d = zeros(tam,dtype = float)

while (N > i):
	d[i] = ((acel * (t[i] ** 2)) / 2) + vel * t[i]
	i = i + 1
print(d)
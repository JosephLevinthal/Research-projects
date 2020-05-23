from numpy import *
a = float(input('aceleracao: '))
b = float(input('vel inicial: '))
n = int(input('numero: '))
i = 0
l1 = arange(n)
l2 = zeros(n,dtype=float)
while i < n:
	l2[i] = (a*l1[i]**2)/2 + b*l1[i]
	i+=1
print(l2)
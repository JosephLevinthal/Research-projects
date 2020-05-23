from math import *
n = int(input("n: "))
soma = 1
i = 1
f = 3
v = 1
s = -1
while(n>i):
	soma = soma + (s*(1/(f * 3 ** v)))
	f = f + 2
	s = s*(-1)
	v = v + 1
	i = i + 1
resultado = 12**0.5 * soma
print(round(resultado, 8))
from numpy import *
v = array(eval(input("Digite o vetor: ")))

par = 0

for i in range(size(v)):
	if v[i] % 2 == 0:
		par = par + 1
print(par)

v2 = zeros(par, dtype=int)

j = 0

for i in range(size(v)):
	if v[i] % 2 == 0:
		v2[j] = i
		j = j + 1
print(v2)
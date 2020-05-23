from numpy import *

v = array(eval(input('Vetor: ')))
a = 0

for i in range(size(v)):
	if v[i]>=2000:
		a = a+1
vet = zeros(a, dtype=int)
b = 0
for i in range(size(vet)):
	if v[i]>=2000:
		vet[i] = v[b]
	b = b+1
print(a)
print(vet)
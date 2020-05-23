from numpy import *
v = array(eval(input()))
a=0
for x in range(size(v)):
	if(v[x]%5 == 0):
		a=a+1
vet = zeros(a, dtype=int)
i = 0
for x in range(size(v)):
	if(v[x]%5 == 0):
		vet[i] = x
		i=i+1
print(a)
print(vet)
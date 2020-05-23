from numpy import *
v = array(eval(input("Valores dos saques: ")))
val = 0
for i in range(size(v)):
	if (v[i] >= 2000):
		val = val + 1
vet = zeros(val, dtype = int)
k = 0
for j in range(size(v)):
	#vet = zeros(val, dtype = int)
	if v[j] >= 2000:
		vet[j] = j + k
		k = k + 1
print(val)
print(vet)
	
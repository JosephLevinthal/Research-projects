from numpy import *

vet = array(eval(input("insira:")))
x = 0
for i in range(size(vet)):
	if(vet[i] >= 2000):
		x = x + 1


a = zeros(x,dtype = int)
k = 0
aux = 0
for j in range(size(vet)):
	vet[j] = aux[j]
	j = j + 1
	
print(x)
print(a)
		
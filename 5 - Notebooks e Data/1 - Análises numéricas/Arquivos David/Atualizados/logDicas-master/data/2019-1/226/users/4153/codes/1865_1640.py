from numpy import *

#vetor de entrada
v = array(eval(input("Insira um veror: ")))

impar = 0
for i in range(size(v)):
	if((v[i]%2) != 0):
		impar = impar + 1
print(impar)
k = 0
#vetor que vai conter os indices.
x = zeros(impar, dtype=int)
for j in range(size(v)):
	if((v[j]%2) != 0):
		x[k] = j
		k = k + 1
print(x)
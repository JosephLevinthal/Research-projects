from numpy import *
from numpy.linalg import *

n = array(eval(input("Matriz: ")))
x = shape(n)[0]
x1 = ((x**2 - x)//2)
vet = zeros(x1)

for i in range(x1):
	for j in range(x1):
		if(i > j):
			vet[i] = n[i,j]

print(vet)
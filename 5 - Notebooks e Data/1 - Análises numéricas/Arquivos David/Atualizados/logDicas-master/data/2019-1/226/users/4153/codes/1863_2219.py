from numpy import *
from numpy.linalg import *

m = array(eval(input("Insira uma matriz quadrada: ")))

k = shape(m)[0]
soma = 0
c = 0
for i in range(k):
	for j in range(k):
		if(i > j):
			soma = soma + m[i,j]
			c = c + 1
print(round((soma/c),2))
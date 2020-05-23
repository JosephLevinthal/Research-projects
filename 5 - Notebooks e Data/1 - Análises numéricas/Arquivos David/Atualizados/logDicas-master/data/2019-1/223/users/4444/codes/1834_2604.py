from numpy import *
from numpy.linalg import *
diaria = array(eval(input("Digite a diaria de cada funcionario: ")))
n = shape(diaria)[0]

for i in range(n):
	diaria[i,:] = sorted(diaria[i,:], reverse=True)
	print(diaria[i,0])

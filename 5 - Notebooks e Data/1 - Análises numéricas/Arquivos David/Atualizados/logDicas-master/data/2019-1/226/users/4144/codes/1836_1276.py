from numpy import *
from numpy.linalg import *
mat = array(eval(input("digite:")))
funcionarios = shape(mat)[0]
horas = zeros(7, dtype=int)
for j in range(7):
	horas[j] = sum(mat[:,j])
for i in range(size(horas)):
	if(max(horas)==horas[i]):
		print(i+1)
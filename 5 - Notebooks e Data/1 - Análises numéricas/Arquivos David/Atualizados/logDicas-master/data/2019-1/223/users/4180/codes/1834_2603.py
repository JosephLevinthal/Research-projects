from numpy import *
from numpy.linalg import *

matriz = array(eval(input(":")))

for i in range(shape(matriz)[1]):
	matriz[:,i] =  sorted(matriz[:,i],reverse=True)
print(matriz)
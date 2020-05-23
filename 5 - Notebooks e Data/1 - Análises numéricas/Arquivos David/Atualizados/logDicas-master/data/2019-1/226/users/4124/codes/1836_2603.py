from numpy import *
from numpy.linalg import *

mat = array(eval(input("Insira a matriz: ")))
for i in range(4):
	mat[:,i] = sorted(mat[:,i], reverse = True)
print(mat)
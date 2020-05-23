from numpy import *
from numpy.linalg import *

mat = array(eval(input("Insira a matriz: ")))
for i in range(shape(mat)[0]):
	print(max(mat[i]))
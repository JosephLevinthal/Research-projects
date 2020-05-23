from numpy import*
from numpy.linalg import*
mat = array(eval(input("Digite uma matriz: ")))
for i in range(shape(mat)[0]):
	print(max(mat[i]))
	
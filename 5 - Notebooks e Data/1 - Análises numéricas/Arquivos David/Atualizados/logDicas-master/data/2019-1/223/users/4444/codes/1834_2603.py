from numpy import *
from numpy.linalg import *
mat = array(eval(input("Digite uma matiz 4x4: ")))
for j in range(4):
	mat[:,j] = sorted(mat[:,j], reverse=True)
print(mat)
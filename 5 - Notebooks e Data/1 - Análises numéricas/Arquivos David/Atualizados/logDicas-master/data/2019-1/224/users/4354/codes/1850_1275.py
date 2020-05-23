from numpy import *
from numpy.linalg import *
mat = array(eval(input("digite a matriz: ")))
sh = mat.shape [0]
z = zeros(sh,dtype = int)
for i in range(sh):
	z[i] = sum(mat[i,:])
print(z)
	


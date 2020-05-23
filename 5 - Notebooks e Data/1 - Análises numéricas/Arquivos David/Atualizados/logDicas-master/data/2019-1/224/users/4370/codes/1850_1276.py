from numpy import*
from numpy.linalg import*
mat=array(eval(input("dig a matriz: ")))
c = mat.shape [1]
z = zeros(c, dtype = int)
for j in range (c):
	z[j] = sum(mat[:,j])
for m in range (size(z)):
	if(z[m] == max(z)):
		print(m+1)
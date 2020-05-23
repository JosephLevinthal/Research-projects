from numpy import*
from numpy.linalg import*

mat = array(eval(input("matriz:")))
n = size(mat[1])
t = (n**2-n)//2
a = 0
mat1 = zeros(n, dtype = float)
for i in range (n):
	for j in range (n):
		if i > j:
			mat1[a] = mat[i,j]
			a = a + 1
print(min(mat1))
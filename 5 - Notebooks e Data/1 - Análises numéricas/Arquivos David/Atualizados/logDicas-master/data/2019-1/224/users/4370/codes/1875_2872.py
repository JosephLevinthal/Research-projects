from numpy import*
from numpy. linalg import*
mat = array(eval(input("digite: ")))
l=shape(mat)[0]
c=mat.shape[1]
pro=0
for i in range(l):
	p=mat[i,:]
	
	pro= pro + (p[0]* p[1])/2
print(round(pro/l,2))



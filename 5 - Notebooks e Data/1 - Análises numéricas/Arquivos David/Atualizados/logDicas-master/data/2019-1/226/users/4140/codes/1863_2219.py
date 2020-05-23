from numpy import*
from numpy.linalg import*
mat=array(eval(input()))
a=0

for i in range(shape(mat)[0]):
	for j in range(shape(mat)[1]):
		if i>j:
			a=a+mat[i,j]
n=shape(mat)[0]	
k=(n**2-n)//2
b=a/k

print(round(b,2))
		
	
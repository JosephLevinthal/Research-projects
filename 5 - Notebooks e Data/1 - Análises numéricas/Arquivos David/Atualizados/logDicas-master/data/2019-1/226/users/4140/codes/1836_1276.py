from numpy import*
from numpy.linalg import*
mat=array(eval(input()))
a=zeros(7,dtype=int)
for i in range(7):
	a[i]=sum(mat[0:,i])
for j in range(7):
	if(sum(mat[0:,j])==max(a)):
		print(j+1)
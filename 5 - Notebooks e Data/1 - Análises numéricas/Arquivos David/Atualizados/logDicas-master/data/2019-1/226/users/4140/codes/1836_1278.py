from numpy import *
from numpy.linalg import*
i=int(input())
j=-1
a=0
soma=0
mat=array([[0,2,11,6,15,11,1],[2,0,7,12,4,2,15],[11,7,0,11,8,3,13],[6,12,11,0,10,2,1],[15,4,8,10,0,5,13],[11,2,3,2,5,0,14],[1,15,13,1,13,14,0]])
while (i!=-1):	
	if j==-1:
		j=int(input())
		i=i//111
		i=i-1
		j=j//111
		j=j-1
	else:
		a=i
		i=j
		j=(a//111)-1
	soma=mat[i,j] + soma
	i=int(input())
print(soma)